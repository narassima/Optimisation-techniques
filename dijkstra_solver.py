import heapq

def solve_dijkstra_for_problem(problem_id, title, tag, context, node_coords, edge_list, start_node="S", end_node="T"):
    # node_coords: dict of node_id -> (x%, y%, label)
    # edge_list: list of (from_id, to_id, weight)
    
    # Build graph
    adj = {}
    for nid in node_coords:
        adj[nid] = []
    for u, v, w in edge_list:
        adj[u].append((v, w))
        adj[v].append((u, w)) # undirected graph
        
    # Run Dijkstra
    dist = {nid: float('inf') for nid in node_coords}
    parent = {nid: None for nid in node_coords}
    dist[start_node] = 0
    
    solved_set = []
    solved_order = []
    
    # Priority queue: (distance, node)
    pq = [(0, start_node)]
    visited = set()
    
    step_records = []
    step_n = 1
    
    # Track steps as nodes are added to solved set
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        solved_set.append(u)
        
        if u != start_node:
            # Record step of adding u
            p = parent[u]
            edge_id = f"{p}{u}" if f"{p}{u}" in [f"{e[0]}{e[1]}" for e in edge_list] else f"{u}{p}"
            prev_solved_str = ", ".join([node_coords[n][2] for n in solved_set[:-1]])
            
            # Find candidate edges from currently solved set to unsolved
            active_e = []
            for s in solved_set[:-1]:
                for v_nbr, w_nbr in adj[s]:
                    if v_nbr not in solved_set[:-1]:
                        active_e.append(f"{s}{v_nbr}")
            
            step_records.append({
                "n": step_n,
                "solvedNodes": prev_solved_str,
                "closestUnsolved": node_coords[u][2],
                "totalDist": str(d),
                "nthNode": node_coords[u][2],
                "minDist": str(d),
                "lastConn": f"{node_coords[p][2]}-{node_coords[u][2]}",
                "solvedSet": list(solved_set),
                "activeEdges": active_e
            })
            step_n += 1
            
        # Relax neighbors
        for v, w in adj[u]:
            if v not in visited:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
                    
    # Reconstruct shortest path from end_node back to start_node
    path_nodes = []
    curr = end_node
    while curr is not None:
        path_nodes.append(curr)
        curr = parent[curr]
    path_nodes.reverse()
    
    path_edges = []
    for i in range(len(path_nodes)-1):
        u, v = path_nodes[i], path_nodes[i+1]
        path_edges.append(f"{u}{v}")
        path_edges.append(f"{v}{u}")
        
    # Mark path_edges on the last step
    if step_records:
        step_records[-1]["pathEdges"] = path_edges
        
    # Build traceback string
    tb_str = " Destination to Origin: " + " \u2190 ".join([node_coords[n][2] for n in reversed(path_nodes)])
    route_str = " \u2192 ".join([node_coords[n][2] for n in path_nodes])
    total_dist = dist[end_node]
    
    res_str = f"Shortest Route: <strong>{route_str}</strong><br/>Total Distance = <strong>{total_dist} units</strong>"
    
    # Format network dict for SVG
    nds = [{"id": nid, "x": node_coords[nid][0], "y": node_coords[nid][1], "label": node_coords[nid][2]} for nid in node_coords]
    eds = [{"from": e[0], "to": e[1], "w": e[2]} for e in edge_list]
    
    return {
        "id": problem_id,
        "title": title,
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": ["shortest-path", tag],
        "context": context,
        "network": {"nodes": nds, "edges": eds},
        "steps": step_records,
        "traceback": tb_str,
        "result": res_str
    }

print("Dijkstra solver helper ready!")
