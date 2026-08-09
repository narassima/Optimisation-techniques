// Transportation Problem Solver: IBFS (NWCM, LCM, VAM) + MODI (u-v) Optimality & Closed Loop Stepping

window.solveTransportation = function(problem, ibfsMethod = 'VAM') {
  const { sources, destinations, supply: origSupply, demand: origDemand, costs } = problem;
  const numRows = sources.length;
  const numCols = destinations.length;

  const steps = [];

  // Helper to deep copy allocation grid
  const createEmptyAllocation = () => Array.from({ length: numRows }, () => Array(numCols).fill(0));

  let allocation = createEmptyAllocation();
  let supply = [...origSupply];
  let demand = [...origDemand];

  // IBFS Computation
  if (ibfsMethod === 'NWCM') {
    let r = 0, c = 0;
    const nwSteps = [];
    while (r < numRows && c < numCols) {
      const alloc = Math.min(supply[r], demand[c]);
      allocation[r][c] = alloc;
      supply[r] -= alloc;
      demand[c] -= alloc;

      nwSteps.push({
        r, c, alloc,
        explanation: `Allocated ${alloc} units to Cell (${sources[r]} → ${destinations[c]}) using Northwest Corner rule.`
      });

      if (supply[r] === 0 && r < numRows - 1) r++;
      else if (demand[c] === 0 && c < numCols - 1) c++;
      else { r++; c++; }
    }

    steps.push({
      title: 'IBFS: Northwest Corner Method (NWCM)',
      description: 'Systematically allocate maximum possible units starting from top-left (Northwest) cell (1,1).',
      allocation: allocation.map(row => [...row]),
      phase: 'ibfs',
      method: 'NWCM',
      explanation: `Initial Basic Feasible Solution achieved with ${numRows + numCols - 1} basic variables.`
    });

  } else if (ibfsMethod === 'LCM') {
    while (supply.some(s => s > 0) && demand.some(d => d > 0)) {
      let minCost = Infinity;
      let minR = -1, minC = -1;

      for (let r = 0; r < numRows; r++) {
        if (supply[r] === 0) continue;
        for (let c = 0; c < numCols; c++) {
          if (demand[c] === 0) continue;
          if (costs[r][c] < minCost) {
            minCost = costs[r][c];
            minR = r;
            minC = c;
          }
        }
      }

      if (minR === -1) break;
      const alloc = Math.min(supply[minR], demand[minC]);
      allocation[minR][minC] = alloc;
      supply[minR] -= alloc;
      demand[minC] -= alloc;
    }

    steps.push({
      title: 'IBFS: Least Cost Method (LCM)',
      description: 'Iteratively select the cell with the lowest unit shipping cost cᵢⱼ and allocate maximum feasible units.',
      allocation: allocation.map(row => [...row]),
      phase: 'ibfs',
      method: 'LCM',
      explanation: 'Initial solution prioritized low-cost transportation routes.'
    });

  } else { // VAM (Vogel's Approximation Method)
    let iter = 0;
    while (supply.some(s => s > 0) && demand.some(d => d > 0) && iter < 20) {
      iter++;

      // Row penalties
      const rowPenalties = supply.map((sup, r) => {
        if (sup === 0) return -1;
        const validCosts = costs[r].filter((_, c) => demand[c] > 0).sort((a, b) => a - b);
        if (validCosts.length === 0) return -1;
        if (validCosts.length === 1) return validCosts[0];
        return validCosts[1] - validCosts[0];
      });

      // Column penalties
      const colPenalties = demand.map((dem, c) => {
        if (dem === 0) return -1;
        const validCosts = costs.map(row => row[c]).filter((_, r) => supply[r] > 0).sort((a, b) => a - b);
        if (validCosts.length === 0) return -1;
        if (validCosts.length === 1) return validCosts[0];
        return validCosts[1] - validCosts[0];
      });

      let maxPen = -1;
      let targetRow = -1, targetCol = -1;

      // Find max penalty
      rowPenalties.forEach((pen, r) => {
        if (pen > maxPen) {
          maxPen = pen;
          targetRow = r;
          targetCol = -1;
        }
      });
      colPenalties.forEach((pen, c) => {
        if (pen > maxPen) {
          maxPen = pen;
          targetRow = -1;
          targetCol = c;
        }
      });

      let chosenR = -1, chosenC = -1;

      if (targetRow !== -1) {
        chosenR = targetRow;
        let minCst = Infinity;
        for (let c = 0; c < numCols; c++) {
          if (demand[c] > 0 && costs[chosenR][c] < minCst) {
            minCst = costs[chosenR][c];
            chosenC = c;
          }
        }
      } else if (targetCol !== -1) {
        chosenC = targetCol;
        let minCst = Infinity;
        for (let r = 0; r < numRows; r++) {
          if (supply[r] > 0 && costs[r][chosenC] < minCst) {
            minCst = costs[r][chosenC];
            chosenR = r;
          }
        }
      } else break;

      const alloc = Math.min(supply[chosenR], demand[chosenC]);
      allocation[chosenR][chosenC] = alloc;
      supply[chosenR] -= alloc;
      demand[chosenC] -= alloc;
    }

    steps.push({
      title: 'IBFS: Vogel\'s Approximation Method (VAM)',
      description: 'Compute row and column penalty costs (difference between 2 lowest costs). Allocate maximum supply/demand to min-cost cell in highest penalty line.',
      allocation: allocation.map(row => [...row]),
      phase: 'ibfs',
      method: 'VAM',
      explanation: 'VAM yields an initial solution close to optimal by penalizing missed opportunity savings.'
    });
  }

  // Helper to compute Total Transportation Cost
  function calcCost(allocGrid) {
    let total = 0;
    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numCols; c++) {
        total += allocGrid[r][c] * costs[r][c];
      }
    }
    return total;
  }

  const initialCost = calcCost(allocation);

  // MODI (u-v Method) Optimality Iterations
  let modiIter = 0;
  let isOptimal = false;

  while (modiIter < 5 && !isOptimal) {
    modiIter++;

    // Step 1: Calculate u_i and v_j for allocated cells
    const u = Array(numRows).fill(null);
    const v = Array(numCols).fill(null);
    u[0] = 0; // Fix u1 = 0

    let changed = true;
    while (changed) {
      changed = false;
      for (let r = 0; r < numRows; r++) {
        for (let c = 0; c < numCols; c++) {
          if (allocation[r][c] > 0) {
            if (u[r] !== null && v[c] === null) {
              v[c] = costs[r][c] - u[r];
              changed = true;
            } else if (u[r] === null && v[c] !== null) {
              u[r] = costs[r][c] - v[c];
              changed = true;
            }
          }
        }
      }
    }

    // Default missing u, v to 0 if disconnected
    for (let r = 0; r < numRows; r++) if (u[r] === null) u[r] = 0;
    for (let c = 0; c < numCols; c++) if (v[c] === null) v[c] = 0;

    // Step 2: Opportunity costs Delta_ij = c_ij - (u_i + v_j) for unallocated cells
    const delta = Array.from({ length: numRows }, () => Array(numCols).fill(null));
    let minDelta = Infinity;
    let enteringR = -1, enteringC = -1;

    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numCols; c++) {
        if (allocation[r][c] === 0) {
          const dVal = costs[r][c] - (u[r] + v[c]);
          delta[r][c] = dVal;
          if (dVal < minDelta) {
            minDelta = dVal;
            enteringR = r;
            enteringC = c;
          }
        }
      }
    }

    const currentCost = calcCost(allocation);

    if (minDelta >= 0) {
      isOptimal = true;
      steps.push({
        title: `MODI Method: Optimal Solution Reached!`,
        description: 'All opportunity costs Δᵢⱼ = cᵢⱼ - (uᵢ + vⱼ) ≥ 0 for all unallocated cells. Current transportation plan is optimal.',
        allocation: allocation.map(row => [...row]),
        u, v, delta,
        totalCost: currentCost,
        isOptimal: true,
        phase: 'optimal',
        explanation: `Minimum Total Transportation Cost = $${currentCost}.`
      });
      break;
    }

    // Step 3: Find Closed Loop for entering cell (enteringR, enteringC)
    // Simple closed loop search
    const loop = findClosedLoop(allocation, enteringR, enteringC, numRows, numCols);

    steps.push({
      title: `MODI Iteration ${modiIter}: Opportunity Cost Evaluation & Loop Formation`,
      description: `Entering cell (${sources[enteringR]} → ${destinations[enteringC]}) has negative opportunity cost Δᵢⱼ = ${minDelta}. Form closed loop circuit with alternating +θ and -θ signs.`,
      allocation: allocation.map(row => [...row]),
      u, v, delta,
      enteringR, enteringC,
      loop,
      totalCost: currentCost,
      phase: 'loop',
      explanation: `Closed loop constructed with vertices at allocated basic cells. Reallocation will reduce total shipping cost.`
    });

    if (!loop || loop.length < 4) {
      break; // Safeguard if loop finder encounters edge case
    }

    // Determine theta = min allocation at negative positions
    let theta = Infinity;
    for (let k = 1; k < loop.length; k += 2) {
      const [lr, lc] = loop[k];
      if (allocation[lr][lc] < theta) theta = allocation[lr][lc];
    }

    // Adjust allocations along loop
    const newAlloc = allocation.map(row => [...row]);
    for (let k = 0; k < loop.length; k++) {
      const [lr, lc] = loop[k];
      if (k % 2 === 0) {
        newAlloc[lr][lc] += theta;
      } else {
        newAlloc[lr][lc] -= theta;
      }
    }

    allocation = newAlloc;
  }

  return { steps, finalCost: calcCost(allocation) };
};

// Helper: DFS to find closed orthogonal loop
function findClosedLoop(alloc, startR, startC, numRows, numCols) {
  const path = [[startR, startC]];

  function search(r, c, horizontalOnly) {
    if (horizontalOnly) {
      for (let nextC = 0; nextC < numCols; nextC++) {
        if (nextC === c) continue;
        if (nextC === startC && r === startR && path.length >= 4) {
          return true;
        }
        if (alloc[r][nextC] > 0 || (r === startR && nextC === startC)) {
          if (!path.some(([pr, pc]) => pr === r && pc === nextC)) {
            path.push([r, nextC]);
            if (search(r, nextC, false)) return true;
            path.pop();
          }
        }
      }
    } else {
      for (let nextR = 0; nextR < numRows; nextR++) {
        if (nextR === r) continue;
        if (nextR === startR && c === startC && path.length >= 4) {
          return true;
        }
        if (alloc[nextR][c] > 0 || (nextR === startR && c === startC)) {
          if (!path.some(([pr, pc]) => pr === nextR && pc === c)) {
            path.push([nextR, c]);
            if (search(nextR, c, true)) return true;
            path.pop();
          }
        }
      }
    }
    return false;
  }

  if (search(startR, startC, true) || search(startR, startC, false)) {
    return path;
  }
  return [[startR, startC]];
}
