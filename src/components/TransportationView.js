// TransportationView Component: IBFS Solvers & MODI u-v Closed Loop Visualizer

window.TransportationView = function({ problem, currentStepIndex, onCellClick }) {
  const [ibfsMethod, setIbfsMethod] = React.useState('VAM');

  const solverRes = React.useMemo(() => {
    return window.solveTransportation(problem, ibfsMethod);
  }, [problem, ibfsMethod]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { sources, destinations, supply, demand, costs } = problem;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {/* IBFS Method Switcher */}
      <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <button
          className={`action-btn ${ibfsMethod === 'VAM' ? 'primary' : ''}`}
          onClick={() => setIbfsMethod('VAM')}
        >
          ⭐ Vogel's Approx Method (VAM)
        </button>
        <button
          className={`action-btn ${ibfsMethod === 'LCM' ? 'primary' : ''}`}
          onClick={() => setIbfsMethod('LCM')}
        >
          🏷️ Least Cost Method (LCM)
        </button>
        <button
          className={`action-btn ${ibfsMethod === 'NWCM' ? 'primary' : ''}`}
          onClick={() => setIbfsMethod('NWCM')}
        >
          ↖️ Northwest Corner Method (NWCM)
        </button>
      </div>

      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click cell to view u-v math</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* Transportation Matrix Grid */}
        <div className="matrix-container" style={{ marginTop: '1rem' }}>
          <table className="custom-table">
            <thead>
              <tr>
                <th>Sources \ Dests</th>
                {destinations.map((d, c) => (
                  <th key={c}>
                    {d}
                    {currentStep.v && (
                      <div style={{ fontSize: '0.75rem', color: 'var(--accent-emerald)', fontWeight: 600 }}>
                        v_{c+1} = {currentStep.v[c]}
                      </div>
                    )}
                  </th>
                ))}
                <th>Supply</th>
                {currentStep.u && <th>u_i</th>}
              </tr>
            </thead>
            <tbody>
              {sources.map((src, r) => (
                <tr key={r}>
                  <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>{src}</td>
                  {destinations.map((_, c) => {
                    const costVal = costs[r][c];
                    const allocVal = currentStep.allocation ? currentStep.allocation[r][c] : 0;
                    const deltaVal = currentStep.delta ? currentStep.delta[r][c] : null;

                    const isEntering = currentStep.enteringR === r && currentStep.enteringC === c;
                    const isInLoop = currentStep.loop && currentStep.loop.some(([lr, lc]) => lr === r && lc === c);

                    let cellClass = '';
                    if (isEntering) cellClass = 'cell-pivot';
                    else if (allocVal > 0) cellClass = 'cell-allocated';

                    return (
                      <td
                        key={c}
                        className={cellClass}
                        style={{ position: 'relative', height: '65px' }}
                        onClick={() => onCellClick({
                          title: `Cell [${src} → ${destinations[c]}]`,
                          formula: `Cost c_{${r+1}${c+1}} = $${costVal}`,
                          description: allocVal > 0
                            ? `ALLOCATED: ${allocVal} units shipped on this route. Total route cost = $${allocVal * costVal}.`
                            : deltaVal !== null
                            ? `UNALLOCATED: Opportunity cost Δ_{${r+1}${c+1}} = c_{${r+1}${c+1}} - (u_${r+1} + v_${c+1}) = ${costVal} - (${currentStep.u[r]} + ${currentStep.v[c]}) = ${deltaVal.toFixed(1)}.`
                            : `Unallocated route with unit shipping cost $${costVal}.`,
                          calculation: `Supply = ${supply[r]}, Demand = ${demand[c]}`
                        })}
                      >
                        {/* Unit cost badge */}
                        <div style={{ position: 'absolute', top: 4, right: 6, fontSize: '0.7rem', color: 'var(--accent-amber)', background: 'rgba(0,0,0,0.3)', padding: '1px 4px', borderRadius: '4px' }}>
                          ${costVal}
                        </div>

                        {/* Allocated Units */}
                        {allocVal > 0 ? (
                          <div style={{ fontSize: '1.1rem', fontWeight: 800, color: 'var(--accent-blue)', marginTop: '8px' }}>
                            [{allocVal}]
                          </div>
                        ) : deltaVal !== null ? (
                          <div style={{ fontSize: '0.8rem', color: deltaVal < 0 ? 'var(--accent-rose)' : 'var(--text-muted)', marginTop: '12px' }}>
                            Δ = {deltaVal.toFixed(1)}
                          </div>
                        ) : null}

                        {/* Loop Sign Indicator */}
                        {isInLoop && (
                          <div style={{ position: 'absolute', bottom: 2, left: 6, fontSize: '0.75rem', fontWeight: 800, color: 'var(--accent-amber)' }}>
                            {currentStep.loop.findIndex(([lr, lc]) => lr === r && lc === c) % 2 === 0 ? '+θ' : '-θ'}
                          </div>
                        )}
                      </td>
                    );
                  })}
                  <td style={{ fontWeight: 700 }}>{supply[r]}</td>
                  {currentStep.u && (
                    <td style={{ color: 'var(--accent-emerald)', fontWeight: 600 }}>u_{r+1} = {currentStep.u[r]}</td>
                  )}
                </tr>
              ))}

              {/* Demand Row */}
              <tr style={{ background: 'rgba(0,0,0,0.3)', fontWeight: 700 }}>
                <td style={{ color: 'var(--text-secondary)' }}>Demand</td>
                {demand.map((d, c) => (
                  <td key={c}>{d}</td>
                ))}
                <td style={{ color: 'var(--accent-emerald)' }}>
                  {supply.reduce((a, b) => a + b, 0)} (Total)
                </td>
                {currentStep.u && <td>—</td>}
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
