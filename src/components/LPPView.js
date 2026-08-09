// LPPView Component: PPT-Style Formulation Table, 2D Vector Plotter & Simplex Visualizer

window.LPPView = function({ problem, currentStepIndex, onCellClick }) {
  const [method, setMethod] = React.useState('ppt-formulation'); // 'ppt-formulation', 'simplex', 'graphical'

  const simplexRes = React.useMemo(() => {
    return window.solveLPPSimplex(problem);
  }, [problem]);

  const graphicalRes = React.useMemo(() => {
    return window.solveLPPGraphical(problem);
  }, [problem]);

  const simplexStep = simplexRes.steps[Math.min(currentStepIndex, simplexRes.steps.length - 1)] || simplexRes.steps[0];
  const graphicalStep = graphicalRes.steps[Math.min(currentStepIndex, graphicalRes.steps.length - 1)] || graphicalRes.steps[0];

  const obj = problem.objective || [0, 0];
  const vars = problem.variables || ['x₁', 'x₂'];
  const objType = problem.objectiveType ? problem.objectiveType.toUpperCase() : 'MAX';

  // Iso-profit slope calculation
  const isoSlope = obj[1] !== 0 ? (-obj[0] / obj[1]).toFixed(2) : 'Undefined';

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {/* View Method Switcher */}
      <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <button
          className={`action-btn ${method === 'ppt-formulation' ? 'primary' : ''}`}
          onClick={() => setMethod('ppt-formulation')}
        >
          📋 Course PPT Model Formulation
        </button>
        <button
          className={`action-btn ${method === 'simplex' ? 'primary' : ''}`}
          onClick={() => setMethod('simplex')}
        >
          📊 Simplex Method (Tableau)
        </button>
        <button
          className={`action-btn ${method === 'graphical' ? 'primary' : ''}`}
          onClick={() => setMethod('graphical')}
        >
          📈 Graphical Method (2D Plane)
        </button>
      </div>

      {method === 'ppt-formulation' && (
        <div className="card">
          <div className="explanation-title">
            <h3>📖 Structured LPP Model Formulation (Course PPT Standard)</h3>
            <span className="source-badge">{problem.source}</span>
          </div>

          {/* Decision Variable Definition Box */}
          <div style={{ background: 'rgba(2, 132, 199, 0.05)', border: '1px solid rgba(2, 132, 199, 0.2)', padding: '1rem', borderRadius: '8px', margin: '0.8rem 0' }}>
            <h4 style={{ color: 'var(--accent-blue)', marginBottom: '0.4rem' }}>1. Decision Variables Definition:</h4>
            <div style={{ display: 'flex', gap: '1.5rem', fontSize: '0.9rem' }}>
              <div><strong>x₁:</strong> {vars[0]}</div>
              <div><strong>x₂:</strong> {vars[1]}</div>
            </div>
          </div>

          {/* Slide 24/25 PPT Parameter Grid Table */}
          <h4 style={{ color: 'var(--text-primary)', marginTop: '1rem', marginBottom: '0.4rem' }}>2. Resource Usage & Profit Matrix (PPT Slide 24/25 Table):</h4>
          <div className="matrix-container">
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Resource i</th>
                  <th>Activity 1 ({vars[0]})</th>
                  <th>Activity 2 ({vars[1]})</th>
                  <th>Resource Available (b_i)</th>
                  <th>Constraint Equation</th>
                </tr>
              </thead>
              <tbody>
                {problem.constraints.map((c, idx) => (
                  <tr key={idx}>
                    <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>
                      {c.name ? c.name.split('(')[0] : `Resource ${idx + 1}`}
                    </td>
                    <td style={{ fontWeight: 600 }}>{c.coeffs[0]}</td>
                    <td style={{ fontWeight: 600 }}>{c.coeffs[1]}</td>
                    <td style={{ fontWeight: 700, color: 'var(--accent-amber)' }}>{c.type} {c.rhs}</td>
                    <td style={{ fontFamily: 'var(--font-family-mono)', color: 'var(--text-secondary)' }}>
                      {c.coeffs[0]}x₁ + {c.coeffs[1]}x₂ {c.type} {c.rhs}
                    </td>
                  </tr>
                ))}
                <tr style={{ background: 'rgba(5, 150, 105, 0.1)', fontWeight: 700 }}>
                  <td style={{ color: 'var(--accent-emerald)' }}>Unit Contribution (c_j)</td>
                  <td style={{ color: 'var(--accent-emerald)' }}>${obj[0]}</td>
                  <td style={{ color: 'var(--accent-emerald)' }}>${obj[1]}</td>
                  <td colSpan={2} style={{ color: 'var(--accent-emerald)', textAlign: 'left', paddingLeft: '1rem' }}>
                    <strong>Objective:</strong> {objType} Z = ${obj[0]}x₁ + ${obj[1]}x₂
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          {/* Iso-Profit Slope & Constraint Slope Analysis Box */}
          <div style={{ background: 'rgba(217, 119, 6, 0.08)', border: '1px solid var(--accent-amber)', borderRadius: '8px', padding: '1rem', marginTop: '1rem' }}>
            <h4 style={{ color: 'var(--accent-amber)', marginBottom: '0.4rem' }}>3. Slope Analysis & Solvability (Course PPT Standard):</h4>
            <div style={{ fontSize: '0.85rem', lineHeight: 1.6 }}>
              <div>• <strong>Objective Iso-Profit Line Equation:</strong> {obj[0]}x₁ + {obj[1]}x₂ = Z ➔ Slope m_Z = -c₁/c₂ = <strong>{isoSlope}</strong></div>
              {problem.pptDetails && problem.pptDetails.slopes && (
                <div style={{ marginTop: '0.4rem' }}>
                  <strong>Constraint Slopes (m = -a₁/a₂):</strong>
                  <ul style={{ paddingLeft: '1.2rem', marginTop: '0.2rem' }}>
                    {problem.pptDetails.slopes.map((s, i) => (
                      <li key={i}>{s.name}: <strong>Slope m = {s.slope}</strong></li>
                    ))}
                  </ul>
                </div>
              )}
              {problem.pptDetails && problem.pptDetails.cornerPointsNote && (
                <div style={{ marginTop: '0.5rem', color: 'var(--accent-emerald)', fontWeight: 600 }}>
                  💡 {problem.pptDetails.cornerPointsNote}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {method === 'simplex' && (
        <div className="card">
          <div className="explanation-title">
            <h3>{simplexStep.title}</h3>
            <span className="click-hint-badge">💡 Click cell to inspect formula</span>
          </div>
          <p className="explanation-text">{simplexStep.description}</p>

          {/* Simplex Tableau */}
          {simplexStep.tableau && (
            <div className="matrix-container">
              <table className="custom-table">
                <thead>
                  <tr>
                    <th>Basis</th>
                    <th>C_b</th>
                    {simplexStep.colNames.map((name, j) => (
                      <th key={j} style={{ color: j === simplexStep.pivotCol ? 'var(--accent-emerald)' : 'inherit' }}>
                        {name} {j === simplexStep.pivotCol ? '⤓' : ''}
                      </th>
                    ))}
                    <th>Solution (RHS)</th>
                    {simplexStep.ratios && <th>Ratio Test (b_i / a_ij)</th>}
                  </tr>
                </thead>
                <tbody>
                  {simplexStep.tableau.map((row, r) => {
                    const basisVarIndex = simplexStep.basis[r];
                    const basisName = simplexStep.colNames[basisVarIndex];
                    const cb = simplexStep.cj[basisVarIndex] || 0;
                    const isPivotRow = r === simplexStep.pivotRow;

                    return (
                      <tr key={r} style={{ background: isPivotRow ? 'rgba(225, 29, 72, 0.08)' : 'transparent' }}>
                        <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>{basisName}</td>
                        <td>{cb}</td>
                        {row.slice(0, simplexStep.colNames.length).map((val, c) => {
                          const isPivotCell = r === simplexStep.pivotRow && c === simplexStep.pivotCol;
                          const isEnteringCol = c === simplexStep.pivotCol;
                          const isLeavingRow = r === simplexStep.pivotRow;

                          let cellClass = '';
                          if (isPivotCell) cellClass = 'cell-pivot';
                          else if (isEnteringCol) cellClass = 'cell-entering';
                          else if (isLeavingRow) cellClass = 'cell-leaving';

                          return (
                            <td
                              key={c}
                              className={cellClass}
                              onClick={() => onCellClick({
                                title: `Tableau Cell [${basisName}, ${simplexStep.colNames[c]}]`,
                                formula: `Value = ${val.toFixed(2)}`,
                                description: isPivotCell
                                  ? `PIVOT ELEMENT = ${val.toFixed(2)}. This element will be normalized to 1 in the next tableau.`
                                  : `Current tableau coefficient for variable ${simplexStep.colNames[c]} in row ${basisName}.`,
                                calculation: `CB = ${cb}, Variable = ${simplexStep.colNames[c]}`
                              })}
                            >
                              {val.toFixed(2)}
                            </td>
                          );
                        })}
                        <td style={{ fontWeight: 700 }}>{row[simplexStep.colNames.length].toFixed(2)}</td>
                        {simplexStep.ratios && (
                          <td style={{ color: isPivotRow ? 'var(--accent-amber)' : 'var(--text-muted)', fontWeight: isPivotRow ? 700 : 400 }}>
                            {simplexStep.ratios[r] !== null ? simplexStep.ratios[r].toFixed(2) : '— (N/A)'}
                          </td>
                        )}
                      </tr>
                    );
                  })}

                  {/* Indicator Rows */}
                  {simplexStep.zj && (
                    <tr style={{ background: 'rgba(15,23,42,0.04)', fontWeight: 600 }}>
                      <td colSpan={2}>Z_j</td>
                      {simplexStep.zj.slice(0, simplexStep.colNames.length).map((val, c) => (
                        <td key={c}>{val.toFixed(2)}</td>
                      ))}
                      <td style={{ color: 'var(--accent-emerald)', fontSize: '1rem' }}>{simplexStep.currentZ.toFixed(2)}</td>
                      {simplexStep.ratios && <td>—</td>}
                    </tr>
                  )}
                  {simplexStep.cj_zj && (
                    <tr style={{ background: 'rgba(2, 132, 199, 0.08)', fontWeight: 700 }}>
                      <td colSpan={2} style={{ color: 'var(--accent-blue)' }}>C_j - Z_j</td>
                      {simplexStep.cj_zj.map((val, c) => (
                        <td key={c} style={{ color: c === simplexStep.pivotCol ? 'var(--accent-emerald)' : 'inherit' }}>
                          {val.toFixed(2)}
                        </td>
                      ))}
                      <td>—</td>
                      {simplexStep.ratios && <td>—</td>}
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {method === 'graphical' && (
        <div className="card">
          <div className="explanation-title">
            <h3>{graphicalStep.title}</h3>
          </div>
          <p className="explanation-text">{graphicalStep.description}</p>

          <div className="network-canvas-wrapper" style={{ marginTop: '1rem' }}>
            <svg viewBox="-20 -20 440 340" className="network-svg">
              <line x1="0" y1="300" x2="400" y2="300" stroke="var(--text-muted)" strokeWidth="2" />
              <line x1="0" y1="0" x2="0" y2="300" stroke="var(--text-muted)" strokeWidth="2" />

              <text x="390" y="290" fill="var(--text-secondary)" fontSize="12" fontWeight="700">x₁</text>
              <text x="10" y="15" fill="var(--text-secondary)" fontSize="12" fontWeight="700">x₂</text>

              {[1, 2, 3, 4, 5, 6, 7, 8].map(tick => (
                <g key={tick}>
                  <line x1={tick * 45} y1="295" x2={tick * 45} y2="305" stroke="var(--text-muted)" />
                  <text x={tick * 45} y="318" fill="var(--text-muted)" fontSize="10" textAnchor="middle">{tick * 5}</text>
                  <line x1="-5" y1={300 - tick * 35} x2="5" y2={300 - tick * 35} stroke="var(--text-muted)" />
                  <text x="-12" y={300 - tick * 35 + 4} fill="var(--text-muted)" fontSize="10" textAnchor="end">{tick * 5}</text>
                </g>
              ))}

              {graphicalRes.lines.map((line, idx) => {
                const x1 = 0;
                const y1 = line.yIntercept !== null ? 300 - (line.yIntercept / 5) * 35 : 0;
                const x2 = line.xIntercept !== null ? (line.xIntercept / 5) * 45 : 400;
                const y2 = 300;

                const colors = ['#0284c7', '#d97706', '#9333ea', '#059669'];
                const col = colors[idx % colors.length];

                return (
                  <g key={idx}>
                    <line x1={x1} y1={y1} x2={x2} y2={y2} stroke={col} strokeWidth="3" strokeDasharray="4 2" />
                    <text x={x2 > 350 ? 320 : x2 + 5} y={y1 + 15} fill={col} fontSize="11" fontWeight="600">
                      {line.name}
                    </text>
                  </g>
                );
              })}

              {graphicalRes.evaluatedPoints.length > 0 && (
                <polygon
                  points={graphicalRes.evaluatedPoints.map(pt => `${(pt.x / 5) * 45},${300 - (pt.y / 5) * 35}`).join(' ')}
                  fill="rgba(2, 132, 199, 0.2)"
                  stroke="var(--accent-blue)"
                  strokeWidth="2"
                />
              )}

              {graphicalRes.evaluatedPoints.map((pt, idx) => {
                const cx = (pt.x / 5) * 45;
                const cy = 300 - (pt.y / 5) * 35;
                const isBest = graphicalRes.optimalPoint && Math.abs(pt.x - graphicalRes.optimalPoint.x) < 1e-4 && Math.abs(pt.y - graphicalRes.optimalPoint.y) < 1e-4;

                return (
                  <g key={idx} cursor="pointer" onClick={() => onCellClick({
                    title: `Corner Point (${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`,
                    formula: `Z = ${problem.objective[0]}×(${pt.x.toFixed(2)}) + ${problem.objective[1]}×(${pt.y.toFixed(2)}) = ${pt.z.toFixed(2)}`,
                    description: isBest ? 'OPTIMAL VERTEX! Yields maximum objective value.' : 'Feasible corner vertex point.',
                    calculation: `Source: ${pt.source}`
                  })}>
                    <circle cx={cx} cy={cy} r={isBest ? 7 : 5} fill={isBest ? 'var(--accent-amber)' : 'var(--accent-emerald)'} stroke="#fff" strokeWidth="2" />
                    <text x={cx + 10} y={cy - 5} fill="var(--text-primary)" fontSize="11" fontWeight="700">
                      ({pt.x.toFixed(1)}, {pt.y.toFixed(1)}) Z={pt.z.toFixed(1)}
                    </text>
                  </g>
                );
              })}
            </svg>
          </div>
        </div>
      )}
    </div>
  );
};
