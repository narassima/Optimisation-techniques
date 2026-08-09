import json
from mst_solver import solve_prims_mst

print("Generating 15 rich, multi-clustered MST problems using Prim's algorithm...")

coords_7_clustered = {
    "Hub": (14, 50, "Hub"),
    "A": (30, 20, "A"),
    "B": (30, 80, "B"),
    "C": (50, 50, "C"),
    "D": (72, 20, "D"),
    "E": (72, 80, "E"),
    "T": (88, 50, "T")
}

coords_8_clustered = {
    "Hub": (10, 50, "Hub"),
    "A": (28, 20, "A"),
    "B": (28, 80, "B"),
    "Top": (48, 15, "Top"),
    "C": (48, 50, "C"),
    "D": (70, 20, "D"),
    "E": (70, 80, "E"),
    "T": (88, 50, "T")
}

mst_configs = [
    # 1. Seervada Park Telephone Line MST
    ("mst_1", "1. Seervada Park Telephone Line MST", "seervada-park",
     "Seervada Park management needs to install telephone lines to connect all 7 stations (O, A, B, C, D, E, T) with minimum total cable length.",
     {"O":(8,50,"O"),"A":(30,22,"A"),"B":(30,72,"B"),"C":(55,10,"C"),"D":(80,25,"D"),"E":(62,60,"E"),"T":(92,50,"T")},
     [("O","A",2),("O","B",4),("O","C",3),("A","B",2),("A","D",7),("B","C",1),("B","E",3),("C","D",4),("D","E",1),("D","T",5),("E","T",7)], "O"),

    # 2. Midwest TV Cable Regional Network
    ("mst_2", "2. Midwest TV Cable Regional Network", "midwest-tv",
     "Midwest TV Cable Company provides cable service to five housing developments with minimum total cable distance.",
     {"City":(10,50,"City"),"A":(32,20,"Sub-A"),"B":(55,15,"Sub-B"),"C":(75,30,"Sub-C"),"D":(80,65,"Sub-D"),"E":(55,80,"Sub-E")},
     [("City","A",4),("City","E",8),("A","B",3),("A","E",6),("B","C",2),("B","D",7),("C","D",5),("D","E",3)], "City"),

    # 3. Office Fiber Optic Network Cluster
    ("mst_3", "3. Office Fiber Optic Network Cluster", "office-fiber",
     "Connect all office department clusters (Hub, A, B, C, D, E, Gateway) with minimum total fiber optic cabling.",
     coords_7_clustered,
     [("Hub","A",3),("Hub","B",4),("Hub","C",6),("A","B",2),("A","C",4),("B","C",3),("C","D",5),("C","E",4),("C","T",8),("D","E",3),("D","T",4),("E","T",2)], "Hub"),

    # 4. Village Water Supply Pipeline Network
    ("mst_4", "4. Village Water Supply Pipeline Network", "water-pipeline",
     "Design a water supply distribution grid connecting all 7 village sectors with minimum total pipeline distance.",
     coords_7_clustered,
     [("Hub","A",4),("Hub","B",5),("Hub","C",7),("A","B",3),("A","C",4),("B","C",2),("C","D",3),("C","E",5),("C","T",6),("D","E",4),("D","T",3),("E","T",2),("A","D",8)], "Hub"),

    # 5. Campus LAN High-Speed Infrastructure
    ("mst_5", "5. Campus LAN High-Speed Infrastructure", "campus-lan",
     "Connect all academic building clusters to the campus core network with minimum fiber run length.",
     coords_7_clustered,
     [("Hub","A",2),("Hub","B",4),("Hub","C",5),("A","B",3),("A","C",3),("B","C",4),("C","D",4),("C","E",3),("C","T",7),("D","E",2),("D","T",5),("E","T",3)], "Hub"),

    # 6. Railway Track Regional Interconnection
    ("mst_6", "6. Railway Track Regional Interconnection", "railway-track",
     "Connect 8 regional railway stations and freight yards with minimum track laying distance.",
     coords_8_clustered,
     [("Hub","A",5),("Hub","B",6),("Hub","C",8),("A","B",4),("A","C",3),("A","Top",2),("B","C",5),("Top","D",4),("C","D",3),("C","E",4),("C","T",7),("D","E",3),("D","T",4),("E","T",3)], "Hub"),

    # 7. Substation Electrical Grid Wiring
    ("mst_7", "7. Substation Electrical Grid Wiring", "electrical-grid",
     "Interconnect regional substations and power plants to form an electrical minimum spanning tree.",
     coords_7_clustered,
     [("Hub","A",6),("Hub","B",5),("Hub","C",9),("A","B",3),("A","C",4),("B","C",5),("C","D",3),("C","E",4),("C","T",7),("D","E",2),("D","T",4),("E","T",3)], "Hub"),

    # 8. Irrigation Canal Distribution Network
    ("mst_8", "8. Irrigation Canal Distribution Network", "irrigation-canal",
     "Connect headworks to all agricultural canal clusters with minimum total canal length.",
     coords_7_clustered,
     [("Hub","A",4),("Hub","B",6),("Hub","C",7),("A","B",3),("A","C",3),("B","C",4),("C","D",2),("C","E",5),("C","T",6),("D","E",3),("D","T",4),("E","T",2)], "Hub"),

    # 9. Smart City Broadband Fiber Mesh
    ("mst_9", "9. Smart City Broadband Fiber Mesh", "smart-city",
     "Link 8 urban smart-city data nodes into a minimum spanning broadband backbone.",
     coords_8_clustered,
     [("Hub","A",3),("Hub","B",4),("Hub","C",5),("A","B",2),("A","C",3),("B","C",4),("C","Top",3),("Top","D",4),("C","D",3),("C","E",4),("C","T",6),("D","E",2),("D","T",5),("E","T",3),("A","Top",6)], "Hub"),

    # 10. Gas Pipeline Regional Grid
    ("mst_10", "10. Gas Pipeline Regional Grid", "gas-pipeline",
     "Connect natural gas compressor station to regional distribution stations with minimum pipeline length.",
     coords_7_clustered,
     [("Hub","A",5),("Hub","B",4),("Hub","C",8),("A","B",3),("A","C",4),("B","C",5),("C","D",3),("C","E",4),("C","T",6),("D","E",2),("D","T",5),("E","T",3)], "Hub"),

    # 11. Hospital Emergency Data Network
    ("mst_11", "11. Hospital Emergency Data Network", "hospital-data",
     "Connect critical care units (ER, ICU, OR, Lab, Radiology) with minimum data cabling latency.",
     coords_7_clustered,
     [("Hub","A",2),("Hub","B",3),("Hub","C",4),("A","B",2),("A","C",3),("B","C",2),("C","D",3),("C","E",4),("C","T",5),("D","E",2),("D","T",4),("E","T",3)], "Hub"),

    # 12. Chemical Safety Sensor Mesh
    ("mst_12", "12. Chemical Safety Sensor Mesh", "chemical-sensor",
     "Connect industrial chemical sensors and alarm units to the central control room with minimum total wire length.",
     coords_7_clustered,
     [("Hub","A",3),("Hub","B",5),("Hub","C",6),("A","B",3),("A","C",2),("B","C",4),("C","D",3),("C","E",3),("C","T",5),("D","E",2),("D","T",4),("E","T",2)], "Hub"),

    # 13. ISP Regional Fiber Backbone
    ("mst_13", "13. ISP Regional Fiber Backbone", "isp-backbone",
     "Connect 8 regional internet exchange POPs with minimum fiber optic trunk distance.",
     coords_8_clustered,
     [("Hub","A",4),("Hub","B",5),("Hub","C",7),("A","B",3),("A","C",3),("A","Top",4),("B","C",4),("Top","D",5),("C","D",3),("C","E",4),("C","T",6),("D","E",2),("D","T",4),("E","T",3)], "Hub"),

    # 14. University Campus Multi-Building Cable
    ("mst_14", "14. University Campus Multi-Building Cable", "university-cable",
     "Interconnect 7 campus academic complexes with minimum total utility trenching distance.",
     coords_7_clustered,
     [("Hub","A",3),("Hub","B",4),("Hub","C",5),("A","B",2),("A","C",3),("B","C",4),("C","D",3),("C","E",4),("C","T",6),("D","E",2),("D","T",4),("E","T",3)], "Hub"),

    # 15. E-Commerce Warehouse Automated Conveyor
    ("mst_15", "15. E-Commerce Warehouse Automated Conveyor", "warehouse-conveyor",
     "Link 8 warehouse sorting, packing, and dispatch zones with minimum conveyor track length.",
     coords_8_clustered,
     [("Hub","A",3),("Hub","B",4),("Hub","C",6),("A","B",2),("A","C",3),("A","Top",5),("B","C",4),("Top","D",4),("C","D",3),("C","E",4),("C","T",6),("D","E",2),("D","T",4),("E","T",2)], "Hub")
]

mst_problems = []
for p_id, title, tag, context, coords, edges, start_node in mst_configs:
    prob = solve_prims_mst(p_id, title, tag, context, coords, edges, start_node)
    mst_problems.append(prob)
    print(f"Verified {title}")

print("All 15 MST problems generated and verified!")

# Patch build_clean_75_direct_perfect.py
with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    code = f.read()

start_idx = code.find("mst_problems = [")
end_idx = code.find("# ─────────────────────────────────────────────────────────────────────────────\n# SERIALIZE")

new_mst_code = "mst_problems = " + json.dumps(mst_problems, indent=4) + "\n"

if start_idx != -1 and end_idx != -1:
    updated_code = code[:start_idx] + new_mst_code + "\n" + code[end_idx:]
    with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
        f.write(updated_code)
    print("Successfully patched build_clean_75_direct_perfect.py with 15 rich clustered MST problems!")
else:
    print(f"Error finding markers: start_idx={start_idx}, end_idx={end_idx}")
