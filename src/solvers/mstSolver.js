// Minimum Spanning Tree (MST) Solver: Kruskal's & Prim's Algorithms

window.solveMST = function(problem, algorithm = 'Kruskal') {
  const { nodes, edges } = problem;
  const numNodes = nodes.length;
  const steps = [];

  if (algorithm === 'Kruskal') {
    // Step 1: Sort edges by weight
    const sortedEdges = [...edges].sort((a, b) => a.weight - b.weight);

    steps.push({
      stepIndex: 0,
      title: 'Kruskal Step 1: Sort All Edges by Weight',
      description: `Sort all ${edges.length} edges in non-decreasing order of their weights.`,
      sortedEdges,
      mstEdges: [],
      activeEdge: null,
      phase: 'init',
      explanation: 'Kruskal algorithm prioritizes lowest-cost edges regardless of location.'
    });

    // Union-Find Disjoint Set
    const parent = {};
    nodes.forEach(n => { parent[n.id] = n.id; });

    function find(i) {
      if (parent[i] === i) return i;
      return parent[i] = find(parent[i]);
    }

    function union(i, j) {
      const rootI = find(i);
      const rootJ = find(j);
      if (rootI !== rootJ) {
        parent[rootI] = rootJ;
        return true;
      }
      return false; // Cycle detected
    }

    const mstEdges = [];
    let totalWeight = 0;

    for (let i = 0; i < sortedEdges.length; i++) {
      const edge = sortedEdges[i];
      const rootSrc = find(edge.source);
      const rootTgt = find(edge.target);

      const canAdd = rootSrc !== rootTgt;

      if (canAdd) {
        union(edge.source, edge.target);
        mstEdges.push(edge);
        totalWeight += edge.weight;

        steps.push({
          stepIndex: steps.length,
          title: `Consider Edge (${edge.source} - ${edge.target}, weight = ${edge.weight})`,
          description: `Add edge (${edge.source} - ${edge.target}) to MST. Disjoint sets connected without creating a cycle. Total MST weight = ${totalWeight}.`,
          sortedEdges,
          mstEdges: [...mstEdges],
          activeEdge: edge,
          accepted: true,
          phase: 'add-edge',
          explanation: `Node ${edge.source} (Root: ${rootSrc}) and Node ${edge.target} (Root: ${rootTgt}) belong to different components. Safe to join.`
        });
      } else {
        steps.push({
          stepIndex: steps.length,
          title: `Consider Edge (${edge.source} - ${edge.target}, weight = ${edge.weight})`,
          description: `Reject edge (${edge.source} - ${edge.target}). Adding this edge would form a closed cycle in the tree.`,
          sortedEdges,
          mstEdges: [...mstEdges],
          activeEdge: edge,
          accepted: false,
          phase: 'reject-edge',
          explanation: `Both Node ${edge.source} and Node ${edge.target} already share Root: ${rootSrc}. Cycle detected!`
        });
      }

      if (mstEdges.length === numNodes - 1) break;
    }

    steps.push({
      stepIndex: steps.length,
      title: 'Kruskal MST Complete!',
      description: `Minimum Spanning Tree successfully built with ${mstEdges.length} edges connecting all ${numNodes} stations. Minimum Total Cable Length = ${totalWeight}.`,
      sortedEdges,
      mstEdges: [...mstEdges],
      activeEdge: null,
      totalWeight,
      phase: 'optimal',
      explanation: 'All nodes connected with minimum total edge weight.'
    });

    return { steps, mstEdges, totalWeight };
  } else {
    // Prim's Algorithm
    const inTree = new Set([nodes[0].id]);
    const mstEdges = [];
    let totalWeight = 0;

    steps.push({
      stepIndex: 0,
      title: `Prim Step 1: Start at Node (${nodes[0].id})`,
      description: `Initialize MST tree set with start node (${nodes[0].id}). Grow tree node by node.`,
      mstEdges: [],
      inTree: Array.from(inTree),
      activeEdge: null,
      phase: 'init',
      explanation: 'Prim algorithm expands outward from an initial root node.'
    });

    while (inTree.size < numNodes) {
      let minEdge = null;
      let minW = Infinity;

      // Find min cost edge crossing tree boundary
      edges.forEach(e => {
        const uIn = inTree.has(e.source);
        const vIn = inTree.has(e.target);
        if ((uIn && !vIn) || (!uIn && vIn)) {
          if (e.weight < minW) {
            minW = e.weight;
            minEdge = e;
          }
        }
      });

      if (!minEdge) break;

      const newVertex = inTree.has(minEdge.source) ? minEdge.target : minEdge.source;
      inTree.add(newVertex);
      mstEdges.push(minEdge);
      totalWeight += minEdge.weight;

      steps.push({
        stepIndex: steps.length,
        title: `Add Min Boundary Edge (${minEdge.source} - ${minEdge.target}, weight = ${minEdge.weight})`,
        description: `Connect Node (${newVertex}) to the growing tree using lowest weight boundary edge. Total MST weight = ${totalWeight}.`,
        mstEdges: [...mstEdges],
        inTree: Array.from(inTree),
        activeEdge: minEdge,
        phase: 'add-edge',
        explanation: `Edge (${minEdge.source}-${minEdge.target}) is the cheapest edge connecting tree set S to unvisited V-S.`
      });
    }

    steps.push({
      stepIndex: steps.length,
      title: 'Prim MST Complete!',
      description: `Minimum Spanning Tree complete with ${mstEdges.length} edges. Total MST Weight = ${totalWeight}.`,
      mstEdges: [...mstEdges],
      inTree: Array.from(inTree),
      activeEdge: null,
      totalWeight,
      phase: 'optimal',
      explanation: 'Tree spanning all nodes completed.'
    });

    return { steps, mstEdges, totalWeight };
  }
};
