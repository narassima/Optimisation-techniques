import heapq
import json

def solve_prims_mst(problem_id, title, tag, context, node_coords, edge_list, start_node="O"):
    # node_coords: dict of node_id -> (x%, y%, label)
    # edge_list: list of (u, v, w)
    
    adj = {nid: [] for nid in node_coords}
    for u, v, w in edge_list:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    connected = {start_node}
    mst_edges_used = []
    step_records = []
    total_weight = 0
    
    # Priority queue: (weight, u, v) where u is in connected, v is not
    pq = []
    for v, w in adj[start_node]:
        heapq.heappush(pq, (w, start_node, v))
        
    step_num = 1
    
    while pq and len(connected) < len(node_coords):
        w, u, v = heapq.heappop(pq)
        if v in connected:
            continue # skip cycle
            
        connected.add(v)
        total_weight += w
        
        # Edge representation
        e_id1, e_id2 = f"{u}{v}", f"{v}{u}"
        mst_edges_used.append(e_id1)
        
        c_set_str = "{" + ", ".join(sorted([node_coords[n][2] for n in connected])) + "}"
        u_lbl, v_lbl = node_coords[u][2], node_coords[v][2]
        
        step_records.append({
            "stepNum": step_num,
            "connectedSet": c_set_str,
            "addedNode": v_lbl,
            "linkUsed": f"{u_lbl} \u2013 {v_lbl}",
            "linkLen": w,
            "totalLength": total_weight,
            "title": f"Step {step_num}: Connect Node {v_lbl}",
            "explain": f"From connected set {c_set_str}, the minimum weight link to an unconnected node is {u_lbl} \u2013 {v_lbl} with weight {w}.",
            "mstEdges": list(mst_edges_used),
            "connectedNodes": list(connected)
        })
        step_num += 1
        
        # Push new candidate edges from v
        for nxt, nxt_w in adj[v]:
            if nxt not in connected:
                heapq.heappush(pq, (nxt_w, v, nxt))
                
    # Build final result summary
    links_formatted = ", ".join([f"{node_coords[e[0]][2]}-{node_coords[e[1]][2]}({e[2]})" for e in edge_list if f"{e[0]}{e[1]}" in mst_edges_used or f"{e[1]}{e[0]}" in mst_edges_used])
    res_str = f"MST Links Used: <strong>{links_formatted}</strong><br/><strong>Minimum Total Link Weight = {total_weight} units</strong>"
    
    nds = [{"id": nid, "x": node_coords[nid][0], "y": node_coords[nid][1], "label": node_coords[nid][2]} for nid in node_coords]
    eds = [{"from": e[0], "to": e[1], "w": e[2]} for e in edge_list]
    
    return {
        "id": problem_id,
        "title": title,
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": ["mst", tag],
        "context": context,
        "network": {"nodes": nds, "edges": eds},
        "steps": step_records,
        "result": res_str
    }

print("Prim's MST solver helper ready!")
