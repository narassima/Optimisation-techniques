// AssignmentView Component: Hungarian Method Interactive Matrix & Zero Matching Visualizer

window.AssignmentView = function({ problem, currentStepIndex, onCellClick }) {
  const solverRes = React.useMemo(() => {
    return window.solveAssignment(problem);
  }, [problem]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { agents, tasks, costs: origCosts } = problem;
  const N = agents.length;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click cell to inspect Hungarian reduction</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* Matrix Grid */}
        <div className="matrix-container" style={{ marginTop: '1rem' }}>
          <table className="custom-table">
            <thead>
              <tr>
                <th>Agents \ Tasks</th>
                {tasks.map((t, c) => (
                  <th key={c}>
                    {t}
                    {currentStep.colMins && (
                      <div style={{ fontSize: '0.75rem', color: 'var(--accent-purple)', fontWeight: 600 }}>
                        Min = {currentStep.colMins[c]}
                      </div>
                    )}
                  </th>
                ))}
                {currentStep.rowMins && <th>Row Min</th>}
              </tr>
            </thead>
            <tbody>
              {agents.map((agent, r) => (
                <tr key={r}>
                  <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>{agent}</td>
                  {tasks.map((task, c) => {
                    const val = currentStep.matrix ? currentStep.matrix[r][c] : origCosts[r][c];

                    const isRowCovered = currentStep.coveredRows && currentStep.coveredRows.includes(r);
                    const isColCovered = currentStep.coveredCols && currentStep.coveredCols.includes(c);
                    const isAssigned = currentStep.assignments && currentStep.assignments.some(a => a.r === r && a.c === c);

                    let cellClass = '';
                    if (isAssigned) cellClass = 'cell-zero-match';
                    else if (isRowCovered || isColCovered) cellClass = 'cell-covered-line';

                    return (
                      <td
                        key={c}
                        className={cellClass}
                        style={{ position: 'relative' }}
                        onClick={() => onCellClick({
                          title: `Cell [${agent} → ${task}]`,
                          formula: `Current Value = ${val}`,
                          description: isAssigned
                            ? `MATCHED ASSIGNMENT! Agent ${agent} is assigned to ${task} with original cost = $${origCosts[r][c]}.`
                            : val === 0
                            ? `OPPORTUNITY ZERO: Candidate assignment option.`
                            : `Reduced cost cell value after row/column transformations.`,
                          calculation: `Original Cost = $${origCosts[r][c]}, Current Reduced Value = ${val}`
                        })}
                      >
                        {val}
                        {isAssigned && (
                          <div style={{ fontSize: '0.7rem', color: 'var(--accent-purple)', fontWeight: 800 }}>
                            ★ MATCH
                          </div>
                        )}
                      </td>
                    );
                  })}
                  {currentStep.rowMins && (
                    <td style={{ color: 'var(--accent-purple)', fontWeight: 600 }}>
                      {currentStep.rowMins[r]}
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Final Optimal Assignment Summary */}
        {currentStep.assignments && (
          <div style={{ marginTop: '1rem', background: 'rgba(192, 132, 252, 0.1)', border: '1px solid var(--accent-purple)', borderRadius: '8px', padding: '1rem' }}>
            <h4 style={{ color: 'var(--accent-purple)', marginBottom: '0.5rem' }}>🎯 Optimal Job-Machine Assignment Pairs:</h4>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.5rem' }}>
              {currentStep.assignments.map(({ r, c }, idx) => (
                <div key={idx} style={{ background: 'var(--bg-surface)', padding: '0.5rem 0.8rem', borderRadius: '6px', border: '1px solid var(--bg-card-border)', fontSize: '0.85rem' }}>
                  <strong>{agents[r]}</strong> ➔ <span>{tasks[c]}</span> <span style={{ color: 'var(--accent-amber)', fontWeight: 700 }}>(Cost: ${origCosts[r][c]})</span>
                </div>
              ))}
            </div>
            <div style={{ marginTop: '0.8rem', textAlign: 'right', fontSize: '1.1rem', fontWeight: 800, color: 'var(--accent-purple)' }}>
              Total Minimum Cost = ${currentStep.totalCost}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
