// Assignment Problem Solver: Hungarian Method Step-by-Step

window.solveAssignment = function(problem) {
  const { agents, tasks, costs: origCosts } = problem;
  const N = agents.length;
  const steps = [];

  let matrix = origCosts.map(row => [...row]);

  // Step 0: Original Cost Matrix
  steps.push({
    stepIndex: 0,
    title: 'Initial Assignment Cost Matrix',
    description: `Original ${N}×${N} cost matrix representing cost of assigning agent i to task j.`,
    matrix: matrix.map(row => [...row]),
    phase: 'initial',
    explanation: 'Goal: Find a 1-to-1 assignment matching that minimizes overall total cost.'
  });

  // Step 1: Row Reduction
  const rowMins = matrix.map(row => Math.min(...row));
  const rowReduced = matrix.map((row, r) => row.map(val => val - rowMins[r]));
  matrix = rowReduced;

  steps.push({
    stepIndex: 1,
    title: 'Step 1: Row Minimum Reduction',
    description: 'Subtract the minimum value of each row from every element in that row. Ensures at least one zero per row.',
    matrix: matrix.map(row => [...row]),
    rowMins,
    phase: 'row-reduction',
    explanation: `Row minimums subtracted: [${rowMins.join(', ')}]. Creates opportunity zeros in each row.`
  });

  // Step 2: Column Reduction
  const colMins = [];
  for (let c = 0; c < N; c++) {
    let min = Infinity;
    for (let r = 0; r < N; r++) {
      if (matrix[r][c] < min) min = matrix[r][c];
    }
    colMins.push(min);
  }

  const colReduced = matrix.map((row) => row.map((val, c) => val - colMins[c]));
  matrix = colReduced;

  steps.push({
    stepIndex: 2,
    title: 'Step 2: Column Minimum Reduction',
    description: 'Subtract the minimum value of each column from every element in that column. Ensures at least one zero per column.',
    matrix: matrix.map(row => [...row]),
    colMins,
    phase: 'col-reduction',
    explanation: `Column minimums subtracted: [${colMins.join(', ')}]. Creates opportunity zeros in each column.`
  });

  // Step 3 & 4: Minimum Lines & Matrix Modifications
  let iter = 0;
  let linesCovered = false;

  while (iter < 4 && !linesCovered) {
    iter++;

    // Helper to compute min lines covering all zeros
    const coverage = computeMinLineCoverage(matrix, N);

    if (coverage.numLines >= N) {
      linesCovered = true;
      break;
    }

    // Uncovered minimum element k
    let minUncovered = Infinity;
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < N; c++) {
        if (!coverage.coveredRows.includes(r) && !coverage.coveredCols.includes(c)) {
          if (matrix[r][c] < minUncovered) {
            minUncovered = matrix[r][c];
          }
        }
      }
    }

    // Modify Matrix: Subtract k from uncovered, add k to double-covered (intersections)
    const newMatrix = matrix.map((row, r) => row.map((val, c) => {
      const isRowCovered = coverage.coveredRows.includes(r);
      const isColCovered = coverage.coveredCols.includes(c);

      if (!isRowCovered && !isColCovered) return val - minUncovered;
      if (isRowCovered && isColCovered) return val + minUncovered;
      return val;
    }));

    steps.push({
      stepIndex: 2 + iter,
      title: `Step 3 (Iteration ${iter}): Minimum Line Coverage & Matrix Adjustment`,
      description: `Cover all zeros with minimum lines (${coverage.numLines} lines drawn < ${N} matrix size). Minimum uncovered element k = ${minUncovered}. Subtract k from uncovered cells, add k to line intersections.`,
      matrix: matrix.map(row => [...row]),
      coveredRows: coverage.coveredRows,
      coveredCols: coverage.coveredCols,
      minUncovered,
      phase: 'line-coverage',
      explanation: `Drawn ${coverage.numLines} lines (Rows: ${coverage.coveredRows.map(r=>r+1).join(',')||'None'}, Cols: ${coverage.coveredCols.map(c=>c+1).join(',')||'None'}). Adjusted matrix to generate additional zero options.`
    });

    matrix = newMatrix;
  }

  // Step 5: Final Zero Assignment Matching
  const assignments = findOptimalAssignments(matrix, N);
  let totalCost = 0;
  assignments.forEach(({ r, c }) => {
    totalCost += origCosts[r][c];
  });

  steps.push({
    stepIndex: steps.length,
    title: 'Step 4: Optimal Assignment Matching Reached!',
    description: `Identify independent zeros to establish optimal 1-to-1 matching. Total Minimum Cost = ${totalCost}.`,
    matrix: matrix.map(row => [...row]),
    assignments,
    origCosts,
    totalCost,
    phase: 'optimal',
    explanation: assignments.map(({ r, c }) => `${agents[r]} → ${tasks[c]} (Cost = ${origCosts[r][c]})`).join(' | ')
  });

  return { steps, assignments, totalCost };
};

// Helper: Line coverage heuristic
function computeMinLineCoverage(matrix, N) {
  const coveredRows = [];
  const coveredCols = [];

  // Simple heuristic: count zeros per row/col and cover line with highest zeros
  const rowZeros = matrix.map(row => row.filter(v => v === 0).length);
  const colZeros = Array(N).fill(0);
  for (let c = 0; c < N; c++) {
    for (let r = 0; r < N; r++) if (matrix[r][c] === 0) colZeros[c]++;
  }

  // Cover rows/cols
  rowZeros.forEach((cnt, r) => {
    if (cnt >= 2) coveredRows.push(r);
  });
  colZeros.forEach((cnt, c) => {
    if (cnt >= 1) {
      // Check if any uncovered zero remains in col c
      let uncoveredZero = false;
      for (let r = 0; r < N; r++) {
        if (matrix[r][c] === 0 && !coveredRows.includes(r)) uncoveredZero = true;
      }
      if (uncoveredZero) coveredCols.push(c);
    }
  });

  return {
    numLines: coveredRows.length + coveredCols.length,
    coveredRows,
    coveredCols
  };
}

// Helper: Zero assignment matcher
function findOptimalAssignments(matrix, N) {
  const assignments = [];
  const assignedRows = new Set();
  const assignedCols = new Set();

  // Greedy match rows with single zero
  for (let iter = 0; iter < N; iter++) {
    for (let r = 0; r < N; r++) {
      if (assignedRows.has(r)) continue;
      const zeroCols = [];
      for (let c = 0; c < N; c++) {
        if (matrix[r][c] === 0 && !assignedCols.has(c)) {
          zeroCols.push(c);
        }
      }
      if (zeroCols.length === 1) {
        const c = zeroCols[0];
        assignments.push({ r, c });
        assignedRows.add(r);
        assignedCols.add(c);
      }
    }
  }

  // Pick remaining zeros
  for (let r = 0; r < N; r++) {
    if (assignedRows.has(r)) continue;
    for (let c = 0; c < N; c++) {
      if (matrix[r][c] === 0 && !assignedCols.has(c)) {
        assignments.push({ r, c });
        assignedRows.add(r);
        assignedCols.add(c);
        break;
      }
    }
  }

  return assignments;
}
