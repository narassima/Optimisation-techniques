// Graphical Method Solver for 2-Variable LPP

window.solveLPPGraphical = function(problem) {
  const { objective, constraints, objectiveType } = problem;
  const steps = [];

  // Step 1: Constraint Boundaries & Intercepts
  const lineDetails = constraints.map((c, idx) => {
    const [a, b] = c.coeffs;
    const rhs = c.rhs;
    let xIntercept = a !== 0 ? rhs / a : null;
    let yIntercept = b !== 0 ? rhs / b : null;
    return {
      id: idx,
      name: c.name || `Constraint ${idx + 1}`,
      a, b, rhs, type: c.type,
      xIntercept, yIntercept
    };
  });

  steps.push({
    title: 'Step 1: Plot Constraint Boundaries',
    description: 'Convert inequality constraints into boundary line equations by setting them to equality and determining axis intercepts.',
    details: lineDetails.map(l => `${l.name}: ${l.a}x₁ + ${l.b}x₂ = ${l.rhs} → Intercepts: (${l.xIntercept !== null ? l.xIntercept.toFixed(1) : '∞'}, 0) and (0, ${l.yIntercept !== null ? l.yIntercept.toFixed(1) : '∞'})`),
    lines: lineDetails,
    phase: 'lines'
  });

  // Step 2: Find Candidate Corner Points (Intersections)
  const candidatePoints = [{ x: 0, y: 0, source: 'Origin (0,0)' }];

  // Axis intersections
  lineDetails.forEach(l => {
    if (l.xIntercept !== null && l.xIntercept >= 0) {
      candidatePoints.push({ x: l.xIntercept, y: 0, source: `${l.name} ∩ x1-axis` });
    }
    if (l.yIntercept !== null && l.yIntercept >= 0) {
      candidatePoints.push({ x: 0, y: l.yIntercept, source: `${l.name} ∩ x2-axis` });
    }
  });

  // Pairwise line intersections
  for (let i = 0; i < lineDetails.length; i++) {
    for (let j = i + 1; j < lineDetails.length; j++) {
      const l1 = lineDetails[i];
      const l2 = lineDetails[j];
      const det = l1.a * l2.b - l2.a * l1.b;
      if (Math.abs(det) > 1e-9) {
        const x = (l1.rhs * l2.b - l2.rhs * l1.b) / det;
        const y = (l1.a * l2.rhs - l2.a * l1.rhs) / det;
        if (x >= -1e-6 && y >= -1e-6) {
          candidatePoints.push({ x: Math.max(0, x), y: Math.max(0, y), source: `${l1.name} ∩ ${l2.name}` });
        }
      }
    }
  }

  // Filter Feasible Corner Points
  const feasiblePoints = candidatePoints.filter(pt => {
    return lineDetails.every(l => {
      const val = l.a * pt.x + l.b * pt.y;
      if (l.type === '<=') return val <= l.rhs + 1e-6;
      if (l.type === '>=') return val >= l.rhs - 1e-6;
      return Math.abs(val - l.rhs) < 1e-6;
    });
  });

  // Remove duplicates
  const uniqueFeasible = [];
  feasiblePoints.forEach(pt => {
    if (!uniqueFeasible.some(p => Math.abs(p.x - pt.x) < 1e-4 && Math.abs(p.y - pt.y) < 1e-4)) {
      uniqueFeasible.push(pt);
    }
  });

  steps.push({
    title: 'Step 2: Identify Feasible Polygon & Corner Points',
    description: 'The intersection of all shaded half-planes (including non-negativity x₁, x₂ ≥ 0) forms the convex Feasible Region. Evaluate all extreme corner points.',
    cornerPoints: uniqueFeasible,
    lines: lineDetails,
    phase: 'polygon'
  });

  // Step 3: Evaluate Objective Function at Corner Points
  const evaluatedPoints = uniqueFeasible.map(pt => {
    const z = objective[0] * pt.x + objective[1] * pt.y;
    return { ...pt, z };
  });

  let bestPoint = evaluatedPoints[0];
  evaluatedPoints.forEach(pt => {
    if (objectiveType === 'max') {
      if (pt.z > bestPoint.z) bestPoint = pt;
    } else {
      if (pt.z < bestPoint.z) bestPoint = pt;
    }
  });

  steps.push({
    title: 'Step 3: Evaluate Objective Z at Extreme Vertices',
    description: `Calculate Z = ${objective[0]}x₁ + ${objective[1]}x₂ at each corner point of the feasible region.`,
    evaluations: evaluatedPoints,
    bestPoint,
    lines: lineDetails,
    phase: 'evaluation'
  });

  // Step 4: Optimal Iso-Profit / Iso-Cost Line
  steps.push({
    title: 'Step 4: Optimal Solution Reached!',
    description: `Sliding the objective iso-profit line Z = ${objective[0]}x₁ + ${objective[1]}x₂ outward reaches its extreme point at (${bestPoint.x.toFixed(2)}, ${bestPoint.y.toFixed(2)}), giving optimal ${objectiveType.toUpperCase()} Z = ${bestPoint.z.toFixed(2)}.`,
    bestPoint,
    evaluatedPoints,
    lines: lineDetails,
    phase: 'optimal'
  });

  return {
    steps,
    optimalPoint: bestPoint,
    evaluatedPoints,
    lines: lineDetails
  };
};
