// MSTView Component: Kruskal & Prim Minimum Spanning Tree SVG Network Visualizer

window.MSTView = function({ problem, currentStepIndex, onCellClick }) {
  const [algorithm, setAlgorithm] = React.useState('Kruskal');

  const solverRes = React.useMemo(() => {
    return window.solveMST(problem, algorithm);
  }, [problem, algorithm]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { nodes, edges } = problem;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {/* Algorithm Switcher */}
      <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <button
          className={`action-btn ${algorithm === 'Kruskal' ? 'primary' : ''}`}
          onClick={() => setAlgorithm('Kruskal')}
        >
          🌲 Kruskal's Algorithm (Sorted Edges + Union-Find)
        </button>
        <button
          className={`action-btn ${algorithm === 'Prim' ? 'primary' : ''}`}
          onClick={() => setAlgorithm('Prim')}
        >
          🌿 Prim's Algorithm (Growing Tree Set)
        </button>
      </div>

      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click edge to view MST status</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* SVG Canvas */}
        <div className="network-canvas-wrapper" style={{ marginTop: '1rem' }}>
          <svg viewBox="0 0 650 360" className="network-svg">
            {/* Render Edges */}
            {edges.map((edge, idx) => {
              const srcNode = nodes.find(n => n.id === edge.source);
              const tgtNode = nodes.find(n => n.id === edge.target);
              if (!srcNode || !tgtNode) return null;

              const isInMST = currentStep.mstEdges &&
                currentStep.mstEdges.some(e => (e.source === edge.source && e.target === edge.target) || (e.source === edge.target && e.target === edge.source));

              const isActive = currentStep.activeEdge &&
                ((currentStep.activeEdge.source === edge.source && currentStep.activeEdge.target === edge.target) ||
                 (currentStep.activeEdge.source === edge.target && currentStep.activeEdge.target === edge.source));

              let lineClass = 'edge-line';
              if (isInMST) lineClass += ' in-mst';
              else if (isActive) lineClass += ' active';

              const midX = (srcNode.x + tgtNode.x) / 2;
              const midY = (srcNode.y + tgtNode.y) / 2;

              return (
                <g key={idx} cursor="pointer" onClick={() => onCellClick({
                  title: `Cable Link (${edge.source} ↔ ${edge.target})`,
                  formula: `Length / Cost = ${edge.weight}`,
                  description: isInMST
                    ? 'ACCEPTED MST EDGE: Included in the minimum spanning cable network!'
                    : isActive
                    ? currentStep.accepted === false
                      ? 'REJECTED EDGE: Creating closed cycle!'
                      : 'EVALUATING EDGE: Testing cycle condition.'
                    : `Network link with weight ${edge.weight}.`,
                  calculation: `Weight = ${edge.weight}`
                })}>
                  <line
                    x1={srcNode.x}
                    y1={srcNode.y}
                    x2={tgtNode.x}
                    y2={tgtNode.y}
                    className={lineClass}
                  />

                  {/* Weight badge */}
                  <rect
                    x={midX - 14}
                    y={midY - 10}
                    width="28"
                    height="20"
                    rx="4"
                    className="edge-weight-badge"
                  />
                  <text
                    x={midX}
                    y={midY + 1}
                    className="edge-weight-text"
                  >
                    {edge.weight}
                  </text>
                </g>
              );
            })}

            {/* Render Nodes */}
            {nodes.map((node) => {
              const isInTree = currentStep.inTree
                ? currentStep.inTree.includes(node.id)
                : currentStep.mstEdges && currentStep.mstEdges.some(e => e.source === node.id || e.target === node.id);

              return (
                <g key={node.id}>
                  <circle
                    cx={node.x}
                    cy={node.y}
                    r="20"
                    className={`node-circle ${isInTree ? 'visited' : ''}`}
                  />
                  <text
                    x={node.x}
                    y={node.y}
                    className="node-text"
                  >
                    {node.id}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>

        {/* Kruskal Sorted Edge Table */}
        {algorithm === 'Kruskal' && currentStep.sortedEdges && (
          <div className="matrix-container" style={{ marginTop: '1rem' }}>
            <h4 style={{ color: 'var(--accent-rose)', marginBottom: '0.5rem' }}>📋 Edge List (Sorted by Weight):</h4>
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Edge (u - v)</th>
                  <th>Weight w</th>
                  <th>MST Action Status</th>
                </tr>
              </thead>
              <tbody>
                {currentStep.sortedEdges.map((e, idx) => {
                  const isMST = currentStep.mstEdges.some(m => (m.source === e.source && m.target === e.target) || (m.source === e.target && m.target === e.source));
                  const isActive = currentStep.activeEdge &&
                    ((currentStep.activeEdge.source === e.source && currentStep.activeEdge.target === e.target) ||
                     (currentStep.activeEdge.source === e.target && currentStep.activeEdge.target === e.source));

                  return (
                    <tr key={idx} style={{ background: isActive ? 'rgba(251, 191, 36, 0.15)' : 'transparent' }}>
                      <td>#{idx + 1}</td>
                      <td style={{ fontWeight: 700 }}>{e.source} ↔ {e.target}</td>
                      <td style={{ color: 'var(--accent-blue)', fontWeight: 700 }}>{e.weight}</td>
                      <td>
                        {isMST ? (
                          <span style={{ color: 'var(--accent-emerald)', fontWeight: 700 }}>✅ Included in MST</span>
                        ) : isActive && currentStep.accepted === false ? (
                          <span style={{ color: 'var(--accent-rose)', fontWeight: 700 }}>❌ Rejected (Cycle)</span>
                        ) : (
                          <span style={{ color: 'var(--text-muted)' }}>— Pending</span>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
