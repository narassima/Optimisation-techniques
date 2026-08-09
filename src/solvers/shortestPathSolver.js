// Shortest Path Solver: Dijkstra's Algorithm with Step-by-Step Distance & Edge Relaxation

window.solveShortestPath = function(problem) {
  const { startNode, endNode, nodes, edges } = problem;
  const steps = [];

  // Initialize distance and predecessor maps
  const dist = {};
  const prev = {};
  const visited = new Set();

  nodes.forEach(n => {
    dist[n.id] = Infinity;
    prev[n.id] = null;
  });

  dist[startNode] = 0;

  steps.push({
    stepIndex: 0,
    title: 'Initialization: Set Initial Distances',
    description: `Set distance to Start Node (${startNode}) d(${startNode}) = 0. Set all other nodes d(v) = ∞. All nodes unvisited.`,
    currentNode: startNode,
    dist: { ...dist },
    prev: { ...prev },
    visited: Array.from(visited),
    activeEdge: null,
    phase: 'init',
    explanation: 'Dijkstra algorithm starting state.'
  });

  let current = startNode;

  while (current && visited.size < nodes.length) {
    visited.add(current);

    steps.push({
      stepIndex: steps.length,
      title: `Select Node (${current}) with Min Distance d(${current}) = ${dist[current]}`,
      description: `Mark node (${current}) as Visited. Explore all outgoing/adjacent edges from node (${current}).`,
      currentNode: current,
      dist: { ...dist },
      prev: { ...prev },
      visited: Array.from(visited),
      activeEdge: null,
      phase: 'select-node',
      explanation: `Permanent label assigned to node (${current}).`
    });

    if (current === endNode) {
      break; // Reached target
    }

    // Find outgoing edges from current
    const neighborEdges = edges.filter(e => e.source === current || e.target === current);

    neighborEdges.forEach(edge => {
      const neighbor = edge.source === current ? edge.target : edge.source;
      if (!visited.has(neighbor)) {
        const alt = dist[current] + edge.weight;

        const isRelaxed = alt < dist[neighbor];
        if (isRelaxed) {
          dist[neighbor] = alt;
          prev[neighbor] = current;
        }

        steps.push({
          stepIndex: steps.length,
          title: `Relax Edge (${current} → ${neighbor}, weight = ${edge.weight})`,
          description: isRelaxed
            ? `New path distance d(${current}) + ${edge.weight} = ${alt} < current d(${neighbor}) = ${dist[neighbor] !== Infinity ? dist[neighbor] : '∞'}. Update d(${neighbor}) = ${alt}, Predecessor π(${neighbor}) = ${current}.`
            : `Path via ${current} (d=${alt}) is not shorter than existing d(${neighbor}) = ${dist[neighbor]}. No update.`,
          currentNode: current,
          dist: { ...dist },
          prev: { ...prev },
          visited: Array.from(visited),
          activeEdge: edge,
          phase: 'relax-edge',
          explanation: `Triangle inequality check: d(v) = min(d(v), d(u) + w(u,v))`
        });
      }
    });

    // Select next unvisited node with min distance
    let nextNode = null;
    let minD = Infinity;

    nodes.forEach(n => {
      if (!visited.has(n.id) && dist[n.id] < minD) {
        minD = dist[n.id];
        nextNode = n.id;
      }
    });

    current = nextNode;
  }

  // Reconstruct Shortest Path
  const path = [];
  let curr = endNode;
  while (curr) {
    path.unshift(curr);
    curr = prev[curr];
  }

  const pathEdges = [];
  for (let i = 0; i < path.length - 1; i++) {
    const u = path[i];
    const v = path[i + 1];
    const e = edges.find(ed => (ed.source === u && ed.target === v) || (ed.source === v && ed.target === u));
    if (e) pathEdges.push(e);
  }

  steps.push({
    stepIndex: steps.length,
    title: 'Shortest Path Reached!',
    description: `Optimal Shortest Path from (${startNode}) to (${endNode}): ${path.join(' → ')}. Total Path Distance = ${dist[endNode]}.`,
    currentNode: endNode,
    dist: { ...dist },
    prev: { ...prev },
    visited: Array.from(visited),
    activeEdge: null,
    path,
    pathEdges,
    totalDistance: dist[endNode],
    phase: 'optimal',
    explanation: `Trace predecessors backwards from destination (${endNode}) to origin (${startNode}).`
  });

  return { steps, shortestPath: path, pathEdges, distance: dist[endNode] };
};
