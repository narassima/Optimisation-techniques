// ShortestPathView Component: SVG Network Graph Visualizer for Dijkstra Shortest Path

window.ShortestPathView = function({ problem, currentStepIndex, onCellClick }) {
  const solverRes = React.useMemo(() => {
    return window.solveShortestPath(problem);
  }, [problem]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { nodes, edges, startNode, endNode } = problem;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click node/edge to inspect distance</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* Interactive SVG Canvas */}
        <div className="network-canvas-wrapper" style={{ marginTop: '1rem' }}>
          <svg viewBox="0 0 650 380" className="network-svg">
            {/* Render Edges */}
            {edges.map((edge, idx) => {
              const srcNode = nodes.find(n => n.id === edge.source);
              const tgtNode = nodes.find(n => n.id === edge.target);
              if (!srcNode || !tgtNode) return null;

              const isActive = currentStep.activeEdge &&
                ((currentStep.activeEdge.source === edge.source && currentStep.activeEdge.target === edge.target) ||
                 (currentStep.activeEdge.source === edge.target && currentStep.activeEdge.target === edge.source));

              const isShortestPath = currentStep.pathEdges &&
                currentStep.pathEdges.some(e => (e.source === edge.source && e.target === edge.target) || (e.source === edge.target && e.target === edge.source));

              let lineClass = 'edge-line';
              if (isShortestPath) lineClass += ' shortest-path';
              else if (isActive) lineClass += ' active';

              const midX = (srcNode.x + tgtNode.x) / 2;
              const midY = (srcNode.y + tgtNode.y) / 2;

              return (
                <g key={idx} cursor="pointer" onClick={() => onCellClick({
                  title: `Edge (${edge.source} ↔ ${edge.target})`,
                  formula: `Weight w(${edge.source}, ${edge.target}) = ${edge.weight}`,
                  description: isShortestPath
                    ? 'CRITICAL PATH EDGE: Included in final optimal shortest route!'
                    : isActive
                    ? 'ACTIVE RELAXATION: Currently checking triangle inequality d(v) <= d(u) + w(u,v).'
                    : `Road link connecting ${edge.source} and ${edge.target} with length ${edge.weight}.`,
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
              const isVisited = currentStep.visited && currentStep.visited.includes(node.id);
              const isCurrent = currentStep.currentNode === node.id;
              const distVal = currentStep.dist ? currentStep.dist[node.id] : Infinity;
              const prevVal = currentStep.prev ? currentStep.prev[node.id] : null;

              let nodeClass = 'node-circle';
              if (isCurrent) nodeClass += ' current';
              else if (isVisited) nodeClass += ' visited';

              return (
                <g key={node.id} cursor="pointer" onClick={() => onCellClick({
                  title: `Node (${node.label || node.id})`,
                  formula: `d(${node.id}) = ${distVal !== Infinity ? distVal : '∞'}, π(${node.id}) = ${prevVal || 'None'}`,
                  description: isVisited
                    ? `VISITED NODE: Shortest path to ${node.id} is permanently determined as ${distVal}.`
                    : `UNVISITED NODE: Current tentative distance d(${node.id}) = ${distVal !== Infinity ? distVal : '∞'}.`,
                  calculation: `Predecessor = ${prevVal || 'None'}`
                })}>
                  <circle
                    cx={node.x}
                    cy={node.y}
                    r="22"
                    className={nodeClass}
                  />
                  <text
                    x={node.x}
                    y={node.y}
                    className="node-text"
                  >
                    {node.id}
                  </text>

                  {/* Distance & Predecessor Badge */}
                  <text
                    x={node.x}
                    y={node.y + 35}
                    fill={isVisited ? 'var(--accent-emerald)' : 'var(--text-secondary)'}
                    fontSize="11"
                    fontWeight="700"
                    textAnchor="middle"
                  >
                    d={distVal !== Infinity ? distVal : '∞'} {prevVal ? `(π=${prevVal})` : ''}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>

        {/* Distance Vector Table */}
        {currentStep.dist && (
          <div className="matrix-container" style={{ marginTop: '1rem' }}>
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Node</th>
                  {nodes.map(n => (
                    <th key={n.id} style={{ color: n.id === currentStep.currentNode ? 'var(--accent-amber)' : 'inherit' }}>
                      {n.id} {n.id === startNode ? '(Start)' : n.id === endNode ? '(End)' : ''}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style={{ fontWeight: 700 }}>Distance d(v)</td>
                  {nodes.map(n => {
                    const dVal = currentStep.dist[n.id];
                    return (
                      <td key={n.id} style={{ fontWeight: 700, color: dVal !== Infinity ? 'var(--accent-emerald)' : 'var(--text-muted)' }}>
                        {dVal !== Infinity ? dVal : '∞'}
                      </td>
                    );
                  })}
                </tr>
                <tr>
                  <td style={{ fontWeight: 700 }}>Predecessor π(v)</td>
                  {nodes.map(n => (
                    <td key={n.id} style={{ color: 'var(--accent-blue)' }}>
                      {currentStep.prev[n.id] || '—'}
                    </td>
                  ))}
                </tr>
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
