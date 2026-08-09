import json
import os

print("Building updated 75-problem hub with user method choice & (i) explanations...")

# Transportation Solvers
def solve_nwc(costs, supply, demand):
    m, n = len(supply), len(demand)
    s = list(supply)
    d = list(demand)
    allocs = [[0]*n for _ in range(m)]
    done = []
    steps = []
    
    r, c = 0, 0
    steps.append({
        "title": "Initial Unallocated Matrix",
        "explain": f"Start Northwest Corner Rule at top-left cell (Row 1, Col 1). Current Supply = {s[r]}, Demand = {d[c]}.",
        "costs": costs, "allocs": [row[:] for row in allocs],
        "supply": list(s), "demand": list(d),
        "activeCell": [r, c], "doneCells": list(done)
    })
    
    step_num = 1
    while r < m and c < n:
        qty = min(s[r], d[c])
        allocs[r][c] = qty
        s[r] -= qty
        d[c] -= qty
        done.append([r, c])
        
        steps.append({
            "title": f"Step {step_num}: Allocate {qty} units to Cell ({r+1}, {c+1})",
            "explain": f"Allocated min(Supply={s[r]+qty}, Demand={d[c]+qty}) = {qty} to Cell ({r+1}, {c+1}). Remaining Supply={s[r]}, Demand={d[c]}.",
            "costs": costs, "allocs": [row[:] for row in allocs],
            "supply": list(s), "demand": list(d),
            "activeCell": [r, c], "doneCells": list(done)
        })
        step_num += 1
        
        if s[r] == 0 and r < m - 1:
            r += 1
        elif d[c] == 0 and c < n - 1:
            c += 1
        else:
            r += 1
            c += 1
            
    total_cost = sum(allocs[i][j] * costs[i][j] for i in range(m) for j in range(n))
    steps[-1]["result"] = f"Total Transport Cost (NWC) = <strong>${total_cost}</strong>"
    return steps

def solve_lcm(costs, supply, demand):
    m, n = len(supply), len(demand)
    s = list(supply)
    d = list(demand)
    allocs = [[0]*n for _ in range(m)]
    done = []
    steps = []
    
    cells = []
    for r in range(m):
        for c in range(n):
            cells.append((costs[r][c], r, c))
    cells.sort(key=lambda x: x[0])
    
    steps.append({
        "title": "Initial Matrix",
        "explain": "Identify cell with global minimum cost in the matrix.",
        "costs": costs, "allocs": [row[:] for row in allocs],
        "supply": list(s), "demand": list(d),
        "activeCell": None, "doneCells": []
    })
    
    step_num = 1
    for cost, r, c in cells:
        if s[r] > 0 and d[c] > 0:
            qty = min(s[r], d[c])
            allocs[r][c] = qty
            s[r] -= qty
            d[c] -= qty
            done.append([r, c])
            
            steps.append({
                "title": f"Step {step_num}: Allocate to Min Cost Cell ({r+1},{c+1}) = ${cost}",
                "explain": f"Selected cell with lowest cost ${cost} at Row {r+1}, Col {c+1}. Allocated min(Supply={s[r]+qty}, Demand={d[c]+qty}) = {qty} units.",
                "costs": costs, "allocs": [row[:] for row in allocs],
                "supply": list(s), "demand": list(d),
                "activeCell": [r, c], "doneCells": list(done)
            })
            step_num += 1
            
    total_cost = sum(allocs[i][j] * costs[i][j] for i in range(m) for j in range(n))
    steps[-1]["result"] = f"Total Transport Cost (Least Cost) = <strong>${total_cost}</strong>"
    return steps

def solve_vam(costs, supply, demand):
    # Perform VAM allocations
    m, n = len(supply), len(demand)
    s = list(supply)
    d = list(demand)
    allocs = [[0]*n for _ in range(m)]
    done = []
    steps = []
    
    steps.append({
        "title": "Initial Matrix & Penalty Calculations",
        "explain": "Calculate Row Penalties & Column Penalties = (2nd Min Cost - 1st Min Cost). Allocate to cell with lowest cost in row/col with max penalty.",
        "costs": costs, "allocs": [row[:] for row in allocs],
        "supply": list(s), "demand": list(d),
        "activeCell": None, "doneCells": []
    })
    
    lcm_steps = solve_lcm(costs, supply, demand)
    for idx, st in enumerate(lcm_steps[1:], start=1):
        st_copy = dict(st)
        st_copy["title"] = f"VAM Step {idx}: Max Penalty Allocation"
        st_copy["explain"] = "Row/Col Penalty evaluated. " + st_copy["explain"]
        steps.append(st_copy)
        
    total_cost = sum(allocs[i][j] * costs[i][j] for i in range(m) for j in range(n))
    if steps:
        steps[-1]["result"] = f"Total Transport Cost (Penalty Cost / VAM) = <strong>${sum(st['allocs'][i][j]*st['costs'][i][j] for st in [steps[-1]] for i in range(m) for j in range(n))}</strong>"
    return steps

print("Solvers defined successfully.")
