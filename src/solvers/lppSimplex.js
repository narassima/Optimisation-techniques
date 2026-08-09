// Simplex Method Solver with Step-by-Step Tableau Progression

window.solveLPPSimplex = function(problem) {
  const { objective, constraints, objectiveType, variables } = problem;
  const steps = [];

  const numDecisionVars = objective.length;
  const numConstraints = constraints.length;

  // Build column names: x1, x2, ..., s1, s2, ..., Solution (RHS)
  const colNames = [];
  for (let i = 0; i < numDecisionVars; i++) {
    colNames.push(variables ? variables[i] : `x${i + 1}`);
  }
  for (let i = 0; i < numConstraints; i++) {
    colNames.push(`s${i + 1}`);
  }

  // Objective coefficient vector C_j
  const cj = [...objective, ...Array(numConstraints).fill(0)];

  // Initial Basis: Slack variables
  let basis = Array.from({ length: numConstraints }, (_, i) => numDecisionVars + i);

  // Tableau matrix: rows x cols
  // Each row has coefficients + RHS
  let tableau = constraints.map((c, i) => {
    const row = [...c.coeffs];
    // Slack coefficients
    for (let s = 0; s < numConstraints; s++) {
      row.push(s === i ? 1 : 0);
    }
    row.push(c.rhs);
    return row;
  });

  // Helper to compute Z_j and C_j - Z_j
  function computeIndicatorRow(tbl, currentBasis) {
    const numCols = colNames.length;
    const zj = Array(numCols + 1).fill(0);
    for (let j = 0; j <= numCols; j++) {
      let sum = 0;
      for (let i = 0; i < numConstraints; i++) {
        const basisCol = currentBasis[i];
        const cb = cj[basisCol] || 0;
        sum += cb * tbl[i][j];
      }
      zj[j] = sum;
    }

    const cj_zj = Array(numCols).fill(0);
    for (let j = 0; j < numCols; j++) {
      cj_zj[j] = cj[j] - zj[j];
    }

    return { zj, cj_zj, currentZ: zj[numCols] };
  }

  let iter = 0;
  let isOptimal = false;
  const maxIter = 10;

  // Step 0: Standard Form Setup
  steps.push({
    stepIndex: 0,
    title: 'Initial Simplex Setup & Standard Form',
    description: 'Convert inequality constraints into equality equations by adding slack variables (s₁, s₂, ...). Construct the initial Simplex Tableau.',
    colNames,
    cj,
    basis: [...basis],
    tableau: tableau.map(r => [...r]),
    ...computeIndicatorRow(tableau, basis),
    pivotRow: null,
    pivotCol: null,
    explanation: 'Initial basis consists of slack variables with 0 profit contribution. Check indicator row (Cⱼ - Zⱼ) for non-optimal positive values.'
  });

  while (iter < maxIter && !isOptimal) {
    iter++;
    const { zj, cj_zj, currentZ } = computeIndicatorRow(tableau, basis);

    // Optimality Check: For Max, optimal if all C_j - Z_j <= 0
    let enteringCol = -1;
    let maxVal = 0;
    for (let j = 0; j < colNames.length; j++) {
      if (cj_zj[j] > maxVal + 1e-6) {
        maxVal = cj_zj[j];
        enteringCol = j;
      }
    }

    if (enteringCol === -1) {
      isOptimal = true;
      steps.push({
        stepIndex: iter,
        title: `Iteration ${iter}: Optimal Tableau Reached!`,
        description: 'All net evaluation indicators Cⱼ - Zⱼ are ≤ 0. The current basic feasible solution is optimal.',
        colNames,
        cj,
        basis: [...basis],
        tableau: tableau.map(r => [...r]),
        zj, cj_zj, currentZ,
        pivotRow: null, pivotCol: null,
        isOptimal: true,
        explanation: `Optimal Objective Value Z = ${currentZ.toFixed(2)}. No further profitable entering variable exists.`
      });
      break;
    }

    // Minimum Ratio Test
    let leavingRow = -1;
    let minRatio = Infinity;
    const ratios = [];

    for (let i = 0; i < numConstraints; i++) {
      const a_ij = tableau[i][enteringCol];
      const rhs = tableau[i][colNames.length];
      if (a_ij > 1e-6) {
        const ratio = rhs / a_ij;
        ratios.push(ratio);
        if (ratio < minRatio) {
          minRatio = ratio;
          leavingRow = i;
        }
      } else {
        ratios.push(null); // Invalid or non-positive
      }
    }

    if (leavingRow === -1) {
      // Unbounded problem
      steps.push({
        stepIndex: iter,
        title: `Iteration ${iter}: Problem Unbounded`,
        description: `Entering variable ${colNames[enteringCol]} can increase indefinitely without violating constraints.`,
        isUnbounded: true
      });
      break;
    }

    const enteringName = colNames[enteringCol];
    const leavingName = colNames[basis[leavingRow]];
    const pivotVal = tableau[leavingRow][enteringCol];

    steps.push({
      stepIndex: iter,
      title: `Iteration ${iter}: Pivot Selection (${enteringName} enters, ${leavingName} leaves)`,
      description: `Entering variable: ${enteringName} (highest Cⱼ - Zⱼ = ${maxVal.toFixed(2)}). Leaving variable: ${leavingName} (minimum non-negative ratio = ${minRatio.toFixed(2)}). Pivot element = ${pivotVal.toFixed(2)}.`,
      colNames,
      cj,
      basis: [...basis],
      tableau: tableau.map(r => [...r]),
      zj, cj_zj, currentZ,
      pivotRow: leavingRow,
      pivotCol: enteringCol,
      ratios,
      explanation: `Pivot on Cell [Row ${leavingRow + 1}, Col ${enteringName}]. Row operation will make pivot element equal 1 and zero out all other cells in column ${enteringName}.`
    });

    // Execute Pivot Operation (Gauss-Jordan)
    const newTableau = tableau.map(r => [...r]);
    // Divide pivot row by pivot element
    for (let j = 0; j <= colNames.length; j++) {
      newTableau[leavingRow][j] /= pivotVal;
    }
    // Zero out pivot column in other rows
    for (let i = 0; i < numConstraints; i++) {
      if (i !== leavingRow) {
        const factor = tableau[i][enteringCol];
        for (let j = 0; j <= colNames.length; j++) {
          newTableau[i][j] -= factor * newTableau[leavingRow][j];
        }
      }
    }

    // Update basis
    basis[leavingRow] = enteringCol;
    tableau = newTableau;
  }

  return { steps };
};
