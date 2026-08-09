import json
from dijkstra_solver import solve_dijkstra_for_problem

print("Generating 15 verified Shortest Path problems connecting S to T...")

# Standard 7-node layout coordinates (S at left, T at right)
coords_7 = {
    "S": (8, 50, "S"),
    "A": (28, 22, "A"),
    "B": (28, 78, "B"),
    "C": (52, 50, "C"),
    "D": (75, 22, "D"),
    "E": (75, 78, "E"),
    "T": (92, 50, "T")
}

sp_configs = [
    # 1. Seervada Park (O to T)
    ("sp_1", "1. Seervada Park Sightseeing Tram Route", "seervada-park",
     "Seervada Park needs to determine the shortest path from park entrance (O) to station T for tram operation. All distances in miles.",
     {"O":(8,50,"O"),"A":(30,22,"A"),"B":(30,72,"B"),"C":(55,10,"C"),"D":(80,25,"D"),"E":(62,60,"E"),"T":(92,50,"T")},
     [("O","A",2),("O","B",4),("O","C",3),("A","B",2),("A","D",7),("B","C",1),("B","E",3),("C","D",4),("D","E",1),("D","T",5),("E","T",7)],
     "O", "T"),
     
    # 2. City Road Network
    ("sp_2", "2. City Road Network Route Optimization", "road",
     "Find the shortest distance route from origin city S to destination city T through the arterial road network.",
     coords_7, [("S","A",4),("S","B",6),("A","B",2),("A","C",5),("A","D",8),("B","C",3),("B","E",7),("C","D",4),("C","E",3),("D","T",6),("E","T",4)], "S", "T"),

    # 3. Supply Chain Hub-and-Spoke
    ("sp_3", "3. Supply Chain Hub-and-Spoke Routing", "supply",
     "Determine the lowest cost logistics shipping route from supplier S to retail terminal T.",
     coords_7, [("S","A",3),("S","B",5),("A","B",2),("A","C",6),("A","D",4),("B","C",3),("B","E",6),("C","D",2),("C","E",4),("D","T",5),("E","T",3)], "S", "T"),

    # 4. Emergency Ambulance Hospital Routing
    ("sp_4", "4. Emergency Ambulance Hospital Routing", "ambulance",
     "Find the fastest route for an emergency ambulance from accident site S to trauma hospital T.",
     coords_7, [("S","A",2),("S","B",4),("A","B",1),("A","C",5),("A","D",6),("B","C",3),("B","E",5),("C","D",2),("C","E",3),("D","T",4),("E","T",2)], "S", "T"),

    # 5. Campus Navigation Pedestrian Walk
    ("sp_5", "5. Campus Navigation Pedestrian Walkway", "campus",
     "Find the shortest walking path from north campus gate S to main library T.",
     coords_7, [("S","A",3),("S","B",5),("A","C",4),("A","D",3),("B","C",2),("B","E",6),("C","D",3),("C","E",2),("D","T",5),("E","T",3)], "S", "T"),

    # 6. Computer Network Minimum Latency
    ("sp_6", "6. Computer Network Minimum Latency Path", "network",
     "Route data packets from source server S to destination server T with minimum total latency (ms).",
     coords_7, [("S","A",5),("S","B",3),("A","B",1),("A","C",4),("A","D",7),("B","C",6),("B","E",4),("C","D",2),("C","E",3),("D","T",3),("E","T",5)], "S", "T"),

    # 7. Pipeline Minimum Pumping Cost
    ("sp_7", "7. Pipeline Minimum Pumping Cost Path", "pipeline",
     "Find the minimum energy pumping path from oil well S to refinery T.",
     coords_7, [("S","A",6),("S","B",4),("A","C",3),("A","D",5),("B","C",2),("B","E",6),("C","D",4),("C","E",3),("D","T",4),("E","T",2)], "S", "T"),

    # 8. Train Route Distance Minimization
    ("sp_8", "8. Train Route 5-City Distance Minimization", "train",
     "Optimize express train track route between origin station S and terminal T.",
     coords_7, [("S","A",8),("S","B",10),("A","B",3),("A","C",6),("A","D",9),("B","C",4),("B","E",7),("C","D",3),("C","E",5),("D","T",5),("E","T",4)], "S", "T"),

    # 9. Last-Mile Urban Delivery Routing
    ("sp_9", "9. Last-Mile Urban Delivery Routing", "delivery",
     "Find the shortest delivery van route from central warehouse S to customer station T.",
     coords_7, [("S","A",3),("S","B",4),("A","C",5),("A","D",4),("B","C",3),("B","E",6),("C","D",2),("C","E",4),("D","T",3),("E","T",5)], "S", "T"),

    # 10. Airport Layover Travel Time
    ("sp_10", "10. Airport Layover Travel Time Minimization", "airport",
     "Determine the shortest travel path between airport gates S and T via transit shuttles.",
     coords_7, [("S","A",4),("S","B",6),("A","C",3),("A","D",5),("B","C",2),("B","E",4),("C","D",3),("C","E",3),("D","T",4),("E","T",3)], "S", "T"),

    # 11. Telecom Signal Path Loss
    ("sp_11", "11. Telecom Signal Path Loss Minimization", "telecom",
     "Route microwave communications signal from tower S to tower T with minimum attenuation.",
     coords_7, [("S","A",5),("S","B",7),("A","C",4),("A","D",6),("B","C",3),("B","E",4),("C","D",2),("C","E",5),("D","T",3),("E","T",4)], "S", "T"),

    # 12. Water Distribution Pressure Loss
    ("sp_12", "12. Water Distribution Pressure Loss Path", "water",
     "Determine main water pipe route from reservoir S to district T with minimum friction loss.",
     coords_7, [("S","A",6),("S","B",8),("A","C",4),("A","D",5),("B","C",3),("B","E",6),("C","D",3),("C","E",2),("D","T",4),("E","T",3)], "S", "T"),

    # 13. Tourist Budget Airfare Itinerary
    ("sp_13", "13. Tourist Budget Airfare Itinerary", "tourist",
     "Find the cheapest flight connection itinerary from departure airport S to destination T.",
     coords_7, [("S","A",3),("S","B",5),("A","C",4),("A","D",6),("B","C",2),("B","E",5),("C","D",3),("C","E",3),("D","T",4),("E","T",2)], "S", "T"),

    # 14. Cargo Container Port Routing
    ("sp_14", "14. Cargo Container Port Routing", "cargo",
     "Optimize container truck route from port gate S to shipping berth T.",
     coords_7, [("S","A",7),("S","B",9),("A","C",5),("A","D",6),("B","C",3),("B","E",4),("C","D",2),("C","E",4),("D","T",3),("E","T",5)], "S", "T"),

    # 15. Electric Grid Transmission Line
    ("sp_15", "15. Electric Grid Transmission Line Path", "grid",
     "Select power transmission line path from sub-station S to grid node T to minimize resistance.",
     coords_7, [("S","A",5),("S","B",6),("A","C",4),("A","D",5),("B","C",3),("B","E",6),("C","D",2),("C","E",3),("D","T",4),("E","T",2)], "S", "T")
]

sp_problems = []
for p_id, title, tag, context, coords, edges, s_node, t_node in sp_configs:
    prob = solve_dijkstra_for_problem(p_id, title, tag, context, coords, edges, s_node, t_node)
    sp_problems.append(prob)
    print(f"Verified {title}")

print("All 15 Shortest Path problems generated and verified!")

# Now patch into build_clean_75_direct_perfect.py
with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    code = f.read()

start_idx = code.find("sp_problems = [")
end_idx = code.find("# ─────────────────────────────────────────────────────────────────────────────\n# 5. MST PROBLEMS")

new_sp_code = "sp_problems = " + json.dumps(sp_problems, indent=4) + "\n"

if start_idx != -1 and end_idx != -1:
    updated_code = code[:start_idx] + new_sp_code + "\n" + code[end_idx:]
    with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
        f.write(updated_code)
    print("Successfully patched build_clean_75_direct_perfect.py with 15 verified Shortest Path problems!")
else:
    print(f"Error finding markers: start_idx={start_idx}, end_idx={end_idx}")
