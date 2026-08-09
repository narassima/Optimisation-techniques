import json, os, copy
from generate_perfect_75_hub import solve_nwc, solve_lcm, solve_vam

print("Building OR Hub with SVG Network Diagrams for SP and MST...")

# ─────────────────────────────────────────────────────────────────────────────
# 1. LPP PROBLEMS (15)
# ─────────────────────────────────────────────────────────────────────────────
lpp_problems = [
    {
        "id": "lpp_1", "title": "1. Reddy Mikks Paint Production Optimization",
        "difficulty": "easy", "tags": ["product-mix", "graphical-method"],
        "context": "Reddy Mikks produces exterior and interior paints from two raw materials M1 and M2. Maximum daily availabilities: M1=24 tons, M2=6 tons. Profit: $5000/ton exterior, $4000/ton interior. Demand constraint: interior paint cannot exceed exterior by more than 1 ton. Max interior demand = 2 tons.",
        "steps": [
            {"title": "Decision Variables Definition", "explain": "Define daily production amounts of paints in tons.", "formulation": "Let x\u2081 = daily amount of exterior paint produced (tons)\nLet x\u2082 = daily amount of interior paint produced (tons)"},
            {"title": "Objective Function Formulation", "explain": "Maximize total daily profit in thousands of dollars.", "formulation": "Maximize Z = 5x\u2081 + 4x\u2082\n\nWhere:\n  5 = profit per ton of exterior paint ($1000s)\n  4 = profit per ton of interior paint ($1000s)"},
            {"title": "Constraints Formulation", "explain": "Formulate raw material availability and market limit constraints.", "formulation": "Subject to:\n  6x\u2081 + 4x\u2082 \u2264 24   (Raw material M1 constraint)\n   x\u2081 + 2x\u2082 \u2264  6   (Raw material M2 constraint)\n  x\u2082 - x\u2081 \u2264  1   (Market limit: interior \u2264 exterior + 1)\n        x\u2082 \u2264  2   (Demand limit: max interior paint)\n  x\u2081, x\u2082 \u2265 0      (Non-negativity constraints)"},
            {"title": "Graphical Corner Point Evaluation", "explain": "Evaluate objective function Z at all feasible vertices O, A, B, C, D, E.", "body": "<div class=\"table-wrap\"><table class=\"ppt-table\"><thead><tr><th>Corner Point</th><th>x\u2081 (Exterior)</th><th>x\u2082 (Interior)</th><th>Z = 5x\u2081 + 4x\u2082 ($1000s)</th></tr></thead><tbody><tr><td>O (Origin)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A (M1 x-intercept)</td><td>4</td><td>0</td><td>20</td></tr><tr><td>B (M1 \u2229 M2)</td><td>3.33</td><td>1.33</td><td class=\"opt\">21.98 (Optimal)</td></tr><tr><td>C (M1 \u2229 Market limit)</td><td>3</td><td>1.5</td><td>21</td></tr><tr><td>D (M2 \u2229 Demand limit)</td><td>2</td><td>2</td><td>18</td></tr><tr><td>E (Demand limit y-intercept)</td><td>0</td><td>2</td><td>8</td></tr></tbody></table></div>"},
            {"title": "Optimal Production Plan", "explain": "Intersection of binding constraints M1 and M2 yields optimal point B.", "body": "<div class=\"res-box\"><h4>\u2705 Optimal Production Plan</h4><ul><li>Exterior Paint (x\u2081) = <strong>3.33 tons/day</strong></li><li>Interior Paint (x\u2082) = <strong>1.33 tons/day</strong></li><li><strong>Maximum Daily Profit Z = $21,333</strong></li></ul></div>"}
        ]
    },
    {
        "id": "lpp_2", "title": "2. Wyndor Glass Product Line Revamp",
        "difficulty": "easy", "tags": ["product-mix", "plant-capacity"],
        "context": "Wyndor Glass Co. produces Product 1 (glass door with aluminum frame, profit $3000/batch) and Product 2 (wood-framed window, profit $5000/batch). Plant capacities per week: Plant 1=4 hrs, Plant 2=12 hrs, Plant 3=18 hrs.",
        "steps": [
            {"title": "Decision Variables", "explain": "Batches produced per week.", "formulation": "Let x\u2081 = number of batches of Product 1 produced per week\nLet x\u2082 = number of batches of Product 2 produced per week"},
            {"title": "Objective Function", "explain": "Maximize total weekly profit in $1000s.", "formulation": "Maximize Z = 3x\u2081 + 5x\u2082"},
            {"title": "Constraints", "explain": "Weekly hours available at Plants 1, 2, and 3.", "formulation": "Subject to:\n   x\u2081      \u2264  4   (Plant 1 capacity)\n        2x\u2082 \u2264 12   (Plant 2 capacity)\n  3x\u2081 + 2x\u2082 \u2264 18   (Plant 3 capacity)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Corner Point Evaluation", "explain": "Evaluate Z at all feasible vertices.", "body": "<div class=\"table-wrap\"><table class=\"ppt-table\"><thead><tr><th>Corner Point</th><th>x\u2081</th><th>x\u2082</th><th>Z = 3x\u2081 + 5x\u2082</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>4</td><td>0</td><td>12</td></tr><tr><td>B</td><td>4</td><td>3</td><td>27</td></tr><tr><td>C</td><td>2</td><td>6</td><td class=\"opt\">36 (Optimal)</td></tr><tr><td>D</td><td>0</td><td>6</td><td>30</td></tr></tbody></table></div>"},
            {"title": "Optimal Solution", "explain": "Maximum profit occurs at point C.", "body": "<div class=\"res-box\"><h4>\u2705 Optimal Product Mix</h4><ul><li>Product 1 = <strong>2 batches/week</strong></li><li>Product 2 = <strong>6 batches/week</strong></li><li><strong>Maximum Weekly Profit = $36,000</strong></li></ul></div>"}
        ]
    },
    {
        "id": "lpp_3", "title": "3. 7-Day Workforce Shift Scheduling",
        "difficulty": "hard", "tags": ["workforce-scheduling", "integer-lpp"],
        "context": "A plant operates 7 days a week. Minimum worker requirements: Mon=17, Tue=13, Wed=15, Thu=19, Fri=14, Sat=16, Sun=11. Each worker works 5 consecutive days and gets 2 days off. Minimize total workforce.",
        "steps": [
            {"title": "Decision Variables", "explain": "x_i = workers starting 5-day shift on day i.", "formulation": "Let x\u2081=Mon start, x\u2082=Tue, x\u2083=Wed, x\u2084=Thu, x\u2085=Fri, x\u2086=Sat, x\u2087=Sun"},
            {"title": "Objective Function", "explain": "Minimize total workers hired.", "formulation": "Minimize Z = x\u2081 + x\u2082 + x\u2083 + x\u2084 + x\u2085 + x\u2086 + x\u2087"},
            {"title": "Daily Coverage Constraints", "explain": "Each day must have enough workers on duty.", "formulation": "Subject to:\n  x\u2081+x\u2084+x\u2085+x\u2086+x\u2087 \u2265 17  (Mon)\n  x\u2081+x\u2082+x\u2085+x\u2086+x\u2087 \u2265 13  (Tue)\n  x\u2081+x\u2082+x\u2083+x\u2086+x\u2087 \u2265 15  (Wed)\n  x\u2081+x\u2082+x\u2083+x\u2084+x\u2087 \u2265 19  (Thu)\n  x\u2081+x\u2082+x\u2083+x\u2084+x\u2085 \u2265 14  (Fri)\n  x\u2082+x\u2083+x\u2084+x\u2085+x\u2086 \u2265 16  (Sat)\n  x\u2083+x\u2084+x\u2085+x\u2086+x\u2087 \u2265 11  (Sun)\n  x_i \u2265 0, integer"},
            {"title": "Optimal Hiring Schedule", "explain": "Integer LPP optimal solution.", "body": "<div class=\"res-box\"><h4>\u2705 Optimal Hiring Schedule</h4><ul><li>x\u2081=4, x\u2082=8, x\u2083=2, x\u2084=6, x\u2085=0, x\u2086=3, x\u2087=0</li><li><strong>Minimum Total Workforce = 23 workers</strong></li></ul></div>"}
        ]
    }
]

lpp_extras = [
    ("Furniture Production (Carpentry & Painting)", "Carpenter hours = 48, Painter hours = 20. Tables profit $6, Chairs profit $8.", [["Let x\u2081 = Tables, x\u2082 = Chairs"],["Maximize Z = 6x\u2081 + 8x\u2082"],["Subject to: 3x\u2081+2x\u2082\u226448, x\u2081+2x\u2082\u226420, x\u2081,x\u2082\u22650"]]),
    ("Farm Feed Diet Cost Minimization", "Mix grain and soybean to meet protein and fat requirements at minimum cost.", [["Let x\u2081=Grain bags, x\u2082=Soybean bags"],["Minimize Z = 2x\u2081 + 3x\u2082"],["Subject to: 3x\u2081+5x\u2082\u226590(protein), x\u2081+x\u2082\u226530(fat), x\u2081,x\u2082\u22650"]]),
    ("Clothing Production (Parkas & Overcoats)", "Parkas need 1 sqft leather, Overcoats need 2 sqft. Profit: Parka=$30, Overcoat=$50.", [["Let x\u2081=Parkas, x\u2082=Overcoats"],["Maximize Z = 30x\u2081 + 50x\u2082"],["Subject to: x\u2081+2x\u2082\u226440(leather), x\u2081\u226420, x\u2082\u226515, x\u2081,x\u2082\u22650"]]),
    ("Warehouse Transportation LPP Model", "Minimize shipping cost from 2 warehouses to 3 customers.", [["Let x_ij = units shipped from i to j"],["Minimize Z = 2x\u2081\u2081+3x\u2081\u2082+x\u2081\u2083+5x\u2082\u2081+4x\u2082\u2082+8x\u2082\u2083"],["Supply: 120, 80. Demand: 150, 40, 10"]]),
    ("Refinery Crude Oil Blending", "Blend Crude A and B into Gasoline X and Y. Meeting octane and sulphur specs.", [["Let x\u2081=Crude A barrels, x\u2082=Crude B barrels"],["Maximize Z = 4x\u2081 + 5x\u2082"],["Subject to: 0.4x\u2081+0.2x\u2082\u22640.3(x\u2081+x\u2082)(octane), x\u2081+x\u2082\u226450000, x\u2081,x\u2082\u22650"]]),
    ("Financial Portfolio Asset Allocation", "Invest in stocks, bonds, and cash to maximize returns meeting risk constraints.", [["Let x\u2081=Stock %, x\u2082=Bond %, x\u2083=Cash %"],["Maximize Z = 0.12x\u2081 + 0.08x\u2082 + 0.04x\u2083"],["Subject to: x\u2081+x\u2082+x\u2083=100, x\u2081\u226460(risk), x\u2082\u226520, x\u2081,x\u2082,x\u2083\u22650"]]),
    ("Garment Factory Production", "Shirts need 2 hrs cutting, 1 hr sewing. Trousers need 1 hr cutting, 3 hrs sewing. Profit: Shirt=$5, Trouser=$7.", [["Let x\u2081=Shirts, x\u2082=Trousers"],["Maximize Z = 5x\u2081 + 7x\u2082"],["Subject to: 2x\u2081+x\u2082\u226440(cutting), x\u2081+3x\u2082\u226445(sewing), x\u2081,x\u2082\u22650"]]),
    ("Electronics Assembly & Testing", "TVs take 3 hrs assembly, 1 hr testing. Radios take 2 hrs assembly, 2 hrs testing. Profit: TV=$12, Radio=$7.", [["Let x\u2081=TVs, x\u2082=Radios"],["Maximize Z = 12x\u2081 + 7x\u2082"],["Subject to: 3x\u2081+2x\u2082\u226460, x\u2081+2x\u2082\u226440, x\u2081,x\u2082\u22650"]]),
    ("Chemical Reaction Blending", "Mix chemicals A and B to produce compound C. Concentration and purity constraints.", [["Let x\u2081=Chemical A, x\u2082=Chemical B"],["Maximize Z = 8x\u2081 + 5x\u2082"],["Subject to: x\u2081+x\u2082\u2264200, 3x\u2081+x\u2082\u2264360, x\u2081-x\u2082\u2264100, x\u2081,x\u2082\u22650"]]),
    ("Media Advertising Allocation", "TV ads reach 200K viewers ($5K). Newspaper reaches 80K ($2K). Budget=$20K.", [["Let x\u2081=TV ads, x\u2082=Newspaper ads"],["Maximize Z = 200x\u2081 + 80x\u2082 (viewers in 1000s)"],["Subject to: 5x\u2081+2x\u2082\u226420(budget), x\u2081\u22645, x\u2082\u226410, x\u2081,x\u2082\u22650"]]),
    ("Bakery Pastry Production", "Cakes take 2 hrs baking, 1 hr icing. Pastries take 1 hr baking, 2 hrs icing. Profit: Cake=$10, Pastry=$6.", [["Let x\u2081=Cakes, x\u2082=Pastries"],["Maximize Z = 10x\u2081 + 6x\u2082"],["Subject to: 2x\u2081+x\u2082\u226416, x\u2081+2x\u2082\u226416, x\u2081,x\u2082\u22650"]]),
    ("Steel Plant Rolling Mill Production", "Hot-rolled steel needs 4 hrs mill time. Cold-rolled needs 2 hrs mill, 2 hrs finishing. Profit: Hot=$15, Cold=$12.", [["Let x\u2081=Hot-rolled, x\u2082=Cold-rolled"],["Maximize Z = 15x\u2081 + 12x\u2082"],["Subject to: 4x\u2081+2x\u2082\u226480(mill), 2x\u2082\u226440(finishing), x\u2081,x\u2082\u22650"]])
]

for i, (title, context, step_forms) in enumerate(lpp_extras, start=4):
    lpp_problems.append({
        "id": f"lpp_{i}", "title": f"{i}. {title}", "difficulty": "medium", "tags": ["lpp"],
        "context": context,
        "steps": [
            {"title": "Decision Variables", "explain": step_forms[0][0], "formulation": step_forms[0][0]},
            {"title": "Objective Function & Constraints", "explain": f"{step_forms[1][0]} | {step_forms[2][0]}", "formulation": f"{step_forms[1][0]}\n{step_forms[2][0]}"},
            {"title": "Optimal Solution", "explain": "Solve graphically or via Simplex.", "body": f"<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Objective Function: {step_forms[1][0]}</li><li>Key constraint: {step_forms[2][0]}</li><li><strong>Optimal BFS found at corner point intersection.</strong></li></ul></div>"}
        ]
    })

# ─────────────────────────────────────────────────────────────────────────────
# 2. TRANSPORTATION PROBLEMS (15) - with solver steps
# ─────────────────────────────────────────────────────────────────────────────
tp_raw_data = [
    ("MG Auto Multi-Plant Distribution", ["Los Angeles","Detroit","New Orleans"], ["Denver","Miami"],
     [[80,215],[100,108],[102,68]], [1000,1500,1200], [2300,1400],
     "MG Auto has 3 plants (LA 1000, Detroit 1500, New Orleans 1200 cars) and 2 DCs (Denver 2300, Miami 1400). Total Supply = Total Demand = 3700."),
    ("P & T Canned Peas Distribution", ["Plant 1","Plant 2","Plant 3"], ["DC 1","DC 2","DC 3","DC 4"],
     [[464,513,654,867],[352,416,690,791],[995,682,388,685]], [75,125,100], [80,65,70,85],
     "P&T canned peas: 3 plants (75,125,100 truckloads) to 4 DCs (80,65,70,85). Balanced: 300=300."),
    ("3x4 Regional Supply Network", ["Supply 1","Supply 2","Supply 3"], ["Demand 1","Demand 2","Demand 3","Demand 4"],
     [[2,3,1,7],[5,4,8,6],[5,6,8,3]], [30,40,50], [20,30,40,30],
     "Supply (30,40,50) to Demand points (20,30,40,30). Total = 120."),
    ("Steel Mill Distribution Network", ["Mill 1","Mill 2","Mill 3"], ["Dealer 1","Dealer 2","Dealer 3"],
     [[5,3,6],[4,2,7],[6,4,5]], [120,80,80], [150,80,50],
     "Mills (120,80,80) supply Dealers (150,80,50). Total = 280."),
    ("Farm Produce Market Logistics", ["Farm 1","Farm 2","Farm 3"], ["Market 1","Market 2","Market 3"],
     [[3,4,2],[5,3,4],[4,6,3]], [200,300,100], [150,250,200],
     "Farms (200,300,100) supply Markets (150,250,200). Total = 600."),
    ("Coal Mine Power Plant Network", ["Mine 1","Mine 2","Mine 3"], ["Power Plant 1","Power Plant 2","Power Plant 3"],
     [[6,4,8],[5,3,7],[7,5,4]], [100,200,150], [120,180,150],
     "Mines (100,200,150) supply Power Plants (120,180,150). Total = 450."),
    ("Cement Plant Construction Supply", ["Plant 1","Plant 2"], ["Site 1","Site 2","Site 3"],
     [[4,3,5],[5,2,4]], [60,40], [30,40,30],
     "Plants (60,40) supply Construction Sites (30,40,30). Total = 100."),
    ("Textile Mill Outlet Shipping", ["Mill 1","Mill 2","Mill 3"], ["Outlet 1","Outlet 2","Outlet 3","Outlet 4"],
     [[8,6,10,9],[9,7,5,8],[7,8,9,6]], [300,200,400], [250,350,150,150],
     "Mills (300,200,400) supply Outlets (250,350,150,150). Total = 900."),
    ("Oil Refinery Tanker Logistics", ["Terminal 1","Terminal 2","Terminal 3"], ["Refinery 1","Refinery 2","Refinery 3"],
     [[12,10,14],[11,9,13],[13,11,10]], [500,700,400], [600,400,600],
     "Terminals (500,700,400) supply Refineries (600,400,600). Total = 1600."),
    ("Cold Storage Supermarket Chain", ["Storage 1","Storage 2","Storage 3"], ["Market 1","Market 2","Market 3","Market 4"],
     [[4,5,6,3],[5,4,3,6],[6,3,5,4]], [150,200,100], [80,120,100,150],
     "Cold Storages (150,200,100) supply Supermarkets (80,120,100,150). Total = 450."),
    ("Pharmaceutical Multi-Plant Shipping", ["Plant 1","Plant 2","Plant 3"], ["Center 1","Center 2","Center 3"],
     [[15,12,18],[13,14,11],[12,16,13]], [800,600,400], [500,700,600],
     "Plants (800,600,400) supply Distribution Centers (500,700,600). Total = 1800."),
    ("Grain Depot Regional Allocation", ["Depot 1","Depot 2","Depot 3"], ["Market 1","Market 2","Market 3"],
     [[7,5,8],[6,8,4],[9,6,7]], [200,300,250], [250,300,200],
     "Depots (200,300,250) supply Grain Markets (250,300,200). Total = 750."),
    ("Humanitarian Aid Relief Network", ["Center 1","Center 2","Center 3"], ["Zone 1","Zone 2","Zone 3","Zone 4"],
     [[3,5,4,6],[4,3,6,5],[5,4,3,4]], [200,300,150], [100,200,150,200],
     "Aid Centers (200,300,150) supply Relief Zones (100,200,150,200). Total = 650."),
    ("Chemical Factory Bulk Shipping", ["Plant 1","Plant 2","Plant 3"], ["Warehouse 1","Warehouse 2","Warehouse 3"],
     [[10,8,12],[9,11,7],[11,9,10]], [400,500,300], [300,500,400],
     "Chemical Plants (400,500,300) supply Warehouses (300,500,400). Total = 1200."),
    ("Automobile Assembly Component Supply", ["Supplier 1","Supplier 2","Supplier 3"], ["Assembly 1","Assembly 2","Assembly 3"],
     [[14,11,16],[12,13,10],[15,10,12]], [600,400,500], [500,500,500],
     "Suppliers (600,400,500) supply Assembly Plants (500,500,500). Total = 1500.")
]

tp_problems = []
for idx, (title, rows, cols, costs, supply, demand, context) in enumerate(tp_raw_data, start=1):
    tp_problems.append({
        "id": f"tp_{idx}", "title": f"{idx}. {title}",
        "type": "transport", "difficulty": "medium", "tags": ["transportation"],
        "context": context, "rows": rows, "cols": cols,
        "methods": [
            {"name": "1. Northwest Corner (NWC) Method",
             "intro": "<strong>Northwest Corner Rule:</strong> Start at top-left cell. Allocate as much as possible. Move right if row exhausted, down if column satisfied.",
             "steps": solve_nwc(costs, supply, demand)},
            {"name": "2. Least-Cost Method (LCM)",
             "intro": "<strong>Least-Cost Method:</strong> Select the cell with the globally minimum cost. Allocate as much as possible, then eliminate exhausted row/col.",
             "steps": solve_lcm(costs, supply, demand)},
            {"name": "3. Penalty Cost (Vogel's / VAM) Method",
             "intro": "<strong>Penalty Cost / VAM:</strong> Compute penalty = (2nd min − min) for each row & column. Allocate to min-cost cell in the row/col with the highest penalty.",
             "steps": solve_vam(costs, supply, demand)}
        ]
    })

# ─────────────────────────────────────────────────────────────────────────────
# 3. ASSIGNMENT PROBLEMS (15)
# ─────────────────────────────────────────────────────────────────────────────
asgn_problems = [
    {
        "id": "asgn_1", "title": "1. Klyne's Household Chores Assignment",
        "type": "assignment", "difficulty": "medium", "tags": ["klyne","hungarian","line-coverage"],
        "context": "Assign 4 children to 4 chores based on secret bid prices ($). After row and column reduction, lines < n, so matrix adjustment is required.",
        "rowLabels": ["Child 1","Child 2","Child 3","Child 4"],
        "colLabels": ["Chore 1","Chore 2","Chore 3","Chore 4"],
        "steps": [
            {"title": "Step 0: Original Bid Cost Matrix", "explain": "Original bid matrix submitted by children.", "matrix": [[1,4,6,3],[9,7,10,9],[4,5,11,7],[8,7,8,5]], "showRowMin": False},
            {"title": "Step 1: Row Reduction (p_i)", "explain": "Find minimum in each row and subtract it. Row mins: C1=1, C2=7, C3=4, C4=5.", "matrix": [[0,3,5,2],[2,0,3,2],[0,1,7,3],[3,2,3,0]], "showRowMin": True, "rowMins": [1,7,4,5]},
            {"title": "Step 2: Column Reduction (q_j)", "explain": "Find minimum in each column and subtract it. Col mins: Ch1=0, Ch2=0, Ch3=3, Ch4=0.", "matrix": [[0,3,2,2],[2,0,0,2],[0,1,4,3],[3,2,0,0]], "showColMin": True, "colMins": [0,0,3,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (lines=3 < n=4)", "explain": "Draw minimum lines to cover all zeros: Row 2, Row 4, Col 1 = 3 lines. Since 3 < n=4, direct assignment is NOT possible. Rows {C1, C3} share zeros only in {Ch1, Ch3} - Hall's condition fails! Matrix adjustment needed.", "matrix": [[0,3,2,2],[2,0,0,2],[0,1,4,3],[3,2,0,0]], "lineRows": [1,3], "lineCols": [0]},
            {"title": "Step 4: Matrix Adjustment (k=1) & Final Assignment", "explain": "Smallest uncovered element k=1. Subtract k from all uncovered cells; add k to double-covered intersection cells. Now lines = n=4. Assign unique zeros.", "matrix": [[0,2,1,1],[3,0,0,2],[0,0,3,2],[4,2,0,0]], "assignment": [[0,0],[1,2],[2,1],[3,3]], "result": "Child 1 → Chore 1 ($1)<br/>Child 2 → Chore 3 ($10)<br/>Child 3 → Chore 2 ($5)<br/>Child 4 → Chore 4 ($5)<br/><strong>Minimum Total Cost = $21</strong>"}
        ]
    },
    {
        "id": "asgn_2", "title": "2. Job Shop Machine Location Assignment",
        "type": "assignment", "difficulty": "medium", "tags": ["job-shop","dummy"],
        "context": "Assign 3 machines to 4 locations. Dummy machine added for balance (0 cost). Direct assignment possible after row reduction.",
        "rowLabels": ["Machine 1","Machine 2","Machine 3","Dummy M4"],
        "colLabels": ["Location 1","Location 2","Location 3","Location 4"],
        "steps": [
            {"title": "Initial Matrix with Dummy Machine", "explain": "Costs for M1-M3. Dummy M4 has 0 cost everywhere to balance the matrix.", "matrix": [[13,10,16,11],[9,15,10,9],[12,9,14,12],[0,0,0,0]], "showRowMin": False},
            {"title": "Row Reduction", "explain": "Subtract row minimums: M1=10, M2=9, M3=9, Dummy=0.", "matrix": [[3,0,6,1],[0,6,1,0],[3,0,5,3],[0,0,0,0]], "showRowMin": True, "rowMins": [10,9,9,0]},
            {"title": "Column Reduction & Assignment", "explain": "Column minimums are all 0 - no column reduction needed. Unique zeros can be matched directly.", "matrix": [[3,0,6,1],[0,6,1,0],[3,0,5,3],[0,0,0,0]], "assignment": [[0,1],[1,0],[2,3],[3,2]], "result": "M1→Loc 2 ($10), M2→Loc 1 ($9), M3→Loc 4 ($12), Dummy→Loc 3 ($0)<br/><strong>Minimum Handling Cost = $31</strong>"}
        ]
    },
    {
        "id": "asgn_3", "title": "3. IT Consultant Project Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 IT consultants (Alex, Ben, Cara, Dev) to 4 projects (P1-P4) to minimize total cost ($K). After row+col reduction, 3 rows share zeros in only 2 columns - direct assignment fails. Hall's theorem: |{Alex,Ben,Cara}|=3 > |{P1,P2}|=2.",
        "rowLabels": ["Alex","Ben","Cara","Dev"],
        "colLabels": ["Project 1","Project 2","Project 3","Project 4"],
        "steps": [
            {"title": "Step 0: Original Cost Matrix ($000s)", "explain": "Cost of assigning each consultant to each project.", "matrix": [[5,5,7,9],[4,4,7,9],[6,6,10,12],[6,5,3,3]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: Alex=5, Ben=4, Cara=6, Dev=3. Subtract each row minimum from all elements in that row.", "matrix": [[0,0,2,4],[0,0,3,5],[0,0,4,6],[3,2,0,0]], "showRowMin": True, "rowMins": [5,4,6,3]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: P1=0, P2=0, P3=0, P4=0. Each column already contains a zero - no further reduction needed.", "matrix": [[0,0,2,4],[0,0,3,5],[0,0,4,6],[3,2,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Zeros: (Alex,P1),(Alex,P2),(Ben,P1),(Ben,P2),(Cara,P1),(Cara,P2),(Dev,P3),(Dev,P4). Lines: Col P1 + Col P2 + Row Dev = 3 lines only. 3 < n=4 so direct assignment is IMPOSSIBLE. k = min uncovered elements = min(2,4,3,5,4,6) = 2.", "matrix": [[0,0,2,4],[0,0,3,5],[0,0,4,6],[3,2,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=2)", "explain": "Subtract k=2 from all UNCOVERED cells (rows Alex,Ben,Cara intersect cols P3,P4). Add k=2 to INTERSECTION cells: (Dev,P1)=3+2=5 and (Dev,P2)=2+2=4. All other covered cells unchanged.", "matrix": [[0,0,0,2],[0,0,1,3],[0,0,2,4],[5,4,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "New zero at (Alex,P3). Now 4 lines cover all zeros (Col P1 + Col P2 + Col P3 + Row Dev). Assign: Dev must take P3 or P4 - assign Dev→P4. Alex gets P3. Ben & Cara share P1 & P2.", "matrix": [[0,0,0,2],[0,0,1,3],[0,0,2,4],[5,4,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Alex → Project 3 ($7K)<br/>Ben → Project 1 ($4K)<br/>Cara → Project 2 ($6K)<br/>Dev → Project 4 ($3K)<br/><strong>Minimum Total Cost = $20,000</strong>"}
        ]
    },
    {
        "id": "asgn_4", "title": "4. Marketing Team Campaign Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 marketing teams to 4 campaigns (TV, Radio, Print, Online). Budget cost ($L). Teams A,B,C have identical cost profiles for TV and Radio, so {A,B,C} -> {TV,Radio} violates Hall's theorem (3 rows, 2 cols).",
        "rowLabels": ["Team A","Team B","Team C","Team D"],
        "colLabels": ["TV","Radio","Print","Online"],
        "steps": [
            {"title": "Step 0: Original Cost Matrix ($L)", "explain": "Budget cost for each team-campaign pairing.", "matrix": [[8,8,10,14],[6,6,8,12],[9,9,13,17],[12,10,5,5]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: A=8, B=6, C=9, D=5. Subtract each row minimum.", "matrix": [[0,0,2,6],[0,0,2,6],[0,0,4,8],[7,5,0,0]], "showRowMin": True, "rowMins": [8,6,9,5]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: TV=0, Radio=0, Print=0, Online=0. Already a zero in every column.", "matrix": [[0,0,2,6],[0,0,2,6],[0,0,4,8],[7,5,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col TV + Col Radio + Row TeamD = 3 lines. Teams A,B,C all share zeros ONLY in {TV, Radio} - 3 rows vs 2 columns, Hall's theorem violated. k = min(2,6,2,6,4,8) = 2.", "matrix": [[0,0,2,6],[0,0,2,6],[0,0,4,8],[7,5,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=2)", "explain": "Subtract k=2 from all uncovered cells (rows A,B,C x cols Print,Online). Add k=2 to intersections: (D,TV)=7+2=9 and (D,Radio)=5+2=7. Covered non-intersection cells remain unchanged.", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,2,6],[9,7,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "New zeros: A(TV,Radio,Print), B(TV,Radio,Print), C(TV,Radio). Team D has zeros at Print,Online. TeamD must go Online (Print needed for A/B). Teams A,B,C share TV, Radio, Print.", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,2,6],[9,7,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Team A → Print ($10L)<br/>Team B → TV ($6L)<br/>Team C → Radio ($9L)<br/>Team D → Online ($5L)<br/><strong>Minimum Total Budget = $30L</strong>"}
        ]
    },
    {
        "id": "asgn_5", "title": "5. Hospital Nurse Ward Allocation",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 nurses to 4 hospital wards (ICU, ER, Pediatric, Geriatric). Cost = shift difficulty score. Nurses 1,2,3 have identical low-difficulty scores for ICU/ER, creating a 3-vs-2 Hall's violation.",
        "rowLabels": ["Nurse 1","Nurse 2","Nurse 3","Nurse 4"],
        "colLabels": ["ICU","ER","Pediatric","Geriatric"],
        "steps": [
            {"title": "Step 0: Original Difficulty Score Matrix", "explain": "Difficulty score for each nurse-ward pairing (lower is better).", "matrix": [[7,7,8,10],[5,5,7,9],[9,9,12,14],[7,5,3,3]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: N1=7, N2=5, N3=9, N4=3. Subtract each row minimum.", "matrix": [[0,0,1,3],[0,0,2,4],[0,0,3,5],[4,2,0,0]], "showRowMin": True, "rowMins": [7,5,9,3]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: ICU=0, ER=0, Ped=0, Ger=0. No column reduction needed.", "matrix": [[0,0,1,3],[0,0,2,4],[0,0,3,5],[4,2,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col ICU + Col ER + Row Nurse4 = 3 lines. Nurses 1,2,3 share zeros only in {ICU, ER} - Hall's theorem: |{N1,N2,N3}|=3 > |{ICU,ER}|=2. k = min(1,3,2,4,3,5) = 1.", "matrix": [[0,0,1,3],[0,0,2,4],[0,0,3,5],[4,2,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=1)", "explain": "Subtract k=1 from uncovered cells. Add k=1 to intersections: (N4,ICU)=5 and (N4,ER)=3. New zero appears at (N1,Pediatric)!", "matrix": [[0,0,0,2],[0,0,1,3],[0,0,2,4],[5,3,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "New zero at (N1,Pediatric) breaks the tie. 4 lines now cover all zeros. Assign N4→Geriatric, N1→Pediatric, and N2,N3 distribute between ICU and ER.", "matrix": [[0,0,0,2],[0,0,1,3],[0,0,2,4],[5,3,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Nurse 1 → Pediatric (8)<br/>Nurse 2 → ICU (5)<br/>Nurse 3 → ER (9)<br/>Nurse 4 → Geriatric (3)<br/><strong>Minimum Total Difficulty Score = 25</strong>"}
        ]
    },
    {
        "id": "asgn_6", "title": "6. Research Scholar Paper Review",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 scholars to review 4 research papers. Cost = review hours. All 3 junior scholars need equal time for Paper1/Paper2 due to same expertise level - creating a direct Hall's theorem violation (3 rows, 2 zero-columns).",
        "rowLabels": ["Scholar 1","Scholar 2","Scholar 3","Senior Scholar"],
        "colLabels": ["Paper 1","Paper 2","Paper 3","Paper 4"],
        "steps": [
            {"title": "Step 0: Original Cost Matrix (hours)", "explain": "Estimated review hours for each scholar-paper pairing.", "matrix": [[10,10,14,18],[8,8,12,16],[12,12,16,20],[16,14,7,7]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: S1=10, S2=8, S3=12, Senior=7. Subtract each row minimum.", "matrix": [[0,0,4,8],[0,0,4,8],[0,0,4,8],[9,7,0,0]], "showRowMin": True, "rowMins": [10,8,12,7]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: P1=0, P2=0, P3=0, P4=0. Already a zero in each column.", "matrix": [[0,0,4,8],[0,0,4,8],[0,0,4,8],[9,7,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col P1 + Col P2 + Row Senior = 3 lines. Scholars 1,2,3 have zeros ONLY in {Paper1, Paper2}. Hall's: |{S1,S2,S3}|=3 > |{P1,P2}|=2. k = min(4,8,4,8,4,8) = 4.", "matrix": [[0,0,4,8],[0,0,4,8],[0,0,4,8],[9,7,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=4)", "explain": "Subtract k=4 from uncovered (3 rows x 2 cols = 6 cells). Add k=4 to intersections: (Senior,P1)=13 and (Senior,P2)=11. All 3 junior scholars now get zero in Paper 3 also!", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,0,4],[13,11,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "Junior scholars now have zeros in P1, P2, and P3. Senior has zeros in P3 and P4. Since Senior must NOT take a paper juniors exclusively need: assign Senior→P4, and juniors share P1,P2,P3.", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,0,4],[13,11,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Scholar 1 → Paper 3 (14 hrs)<br/>Scholar 2 → Paper 1 (8 hrs)<br/>Scholar 3 → Paper 2 (12 hrs)<br/>Senior Scholar → Paper 4 (7 hrs)<br/><strong>Minimum Total Time = 41 hours</strong>"}
        ]
    },
    {
        "id": "asgn_7", "title": "7. Sales Rep Product Line Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 sales reps to 4 product lines to minimize training/transition cost ($). Sarah, Mike, and Priya have identical cost profiles for Product Lines 1 & 2 - Hall's condition violated after row+column reduction.",
        "rowLabels": ["Sarah","Mike","Priya","Tom"],
        "colLabels": ["Prod Line 1","Prod Line 2","Prod Line 3","Prod Line 4"],
        "steps": [
            {"title": "Step 0: Original Cost Matrix ($)", "explain": "Training/transition cost for each rep-product pairing.", "matrix": [[25,25,31,39],[21,21,27,35],[28,28,36,44],[32,30,19,19]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: Sarah=25, Mike=21, Priya=28, Tom=19. Subtract each minimum.", "matrix": [[0,0,6,14],[0,0,6,14],[0,0,8,16],[13,11,0,0]], "showRowMin": True, "rowMins": [25,21,28,19]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: PL1=0, PL2=0, PL3=0, PL4=0. No further reduction needed.", "matrix": [[0,0,6,14],[0,0,6,14],[0,0,8,16],[13,11,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col PL1 + Col PL2 + Row Tom = 3 lines. Sarah,Mike,Priya have zeros ONLY in {PL1,PL2}. |{Sarah,Mike,Priya}|=3 > |{PL1,PL2}|=2 violates Hall's theorem. k = min(6,14,6,14,8,16) = 6.", "matrix": [[0,0,6,14],[0,0,6,14],[0,0,8,16],[13,11,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=6)", "explain": "Subtract k=6 from uncovered cells. Add k=6 to intersections: (Tom,PL1)=19 and (Tom,PL2)=17. Sarah and Mike get new zeros in PL3; Priya still has positive (8-6=2) in PL3.", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,2,10],[19,17,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "Sarah,Mike have zeros in PL1,PL2,PL3. Priya has zeros in PL1,PL2. Tom has zeros in PL3,PL4. Assign Tom→PL4, Sarah→PL3, and Mike,Priya share PL1,PL2.", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,2,10],[19,17,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Sarah → Prod Line 3 ($31)<br/>Mike → Prod Line 1 ($21)<br/>Priya → Prod Line 2 ($28)<br/>Tom → Prod Line 4 ($19)<br/><strong>Minimum Total Cost = $99</strong>"}
        ]
    },
    {
        "id": "asgn_8", "title": "8. Sports Coach Event Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 coaches to 4 athletic events (100m, 200m, 400m, Relay). Effort index matrix. Coaches A,B,C have identical sprint aptitude (100m, 200m) - Hall's violation: 3 coaches compete for 2 event slots.",
        "rowLabels": ["Coach A","Coach B","Coach C","Head Coach"],
        "colLabels": ["100m","200m","400m","Relay"],
        "steps": [
            {"title": "Step 0: Original Effort Matrix", "explain": "Coaching effort index for each coach-event pairing.", "matrix": [[14,14,17,22],[11,11,14,19],[17,17,20,25],[19,17,10,10]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: A=14, B=11, C=17, Head=10. Subtract each minimum.", "matrix": [[0,0,3,8],[0,0,3,8],[0,0,3,8],[9,7,0,0]], "showRowMin": True, "rowMins": [14,11,17,10]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: 100m=0, 200m=0, 400m=0, Relay=0. Already zero in each column.", "matrix": [[0,0,3,8],[0,0,3,8],[0,0,3,8],[9,7,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col 100m + Col 200m + Row Head = 3 lines. Coaches A,B,C share zeros ONLY in {100m, 200m}. Hall's: 3 coaches need 3 distinct events but only 2 zero-columns available. k = min(3,8,3,8,3,8) = 3.", "matrix": [[0,0,3,8],[0,0,3,8],[0,0,3,8],[9,7,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=3)", "explain": "Subtract k=3 from uncovered cells (rows A,B,C; cols 400m,Relay). Add k=3 to intersections: (Head,100m)=12 and (Head,200m)=10. All 3 junior coaches now have zero in 400m too!", "matrix": [[0,0,0,5],[0,0,0,5],[0,0,0,5],[12,10,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "Coaches A,B,C have zeros in 100m, 200m, 400m. Head Coach has zeros in 400m, Relay. Head must cover Relay (400m needed for juniors). A,B,C freely cover 100m,200m,400m.", "matrix": [[0,0,0,5],[0,0,0,5],[0,0,0,5],[12,10,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Coach A → 400m (17)<br/>Coach B → 100m (11)<br/>Coach C → 200m (17)<br/>Head Coach → Relay (10)<br/><strong>Minimum Total Effort = 55</strong>"}
        ]
    },
    {
        "id": "asgn_9", "title": "9. Delivery Van Route Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 delivery vans to 4 routes to minimize total delivery time (minutes). Vans 1,2,3 have identical efficiency on Routes 1 & 2 - Hall's theorem violation forces matrix adjustment.",
        "rowLabels": ["Van 1","Van 2","Van 3","Van 4"],
        "colLabels": ["Route 1","Route 2","Route 3","Route 4"],
        "steps": [
            {"title": "Step 0: Original Cost Matrix (minutes)", "explain": "Estimated delivery time for each van-route pairing.", "matrix": [[45,45,52,60],[38,38,45,53],[50,50,57,65],[55,50,35,35]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: V1=45, V2=38, V3=50, V4=35. Subtract each minimum.", "matrix": [[0,0,7,15],[0,0,7,15],[0,0,7,15],[20,15,0,0]], "showRowMin": True, "rowMins": [45,38,50,35]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: R1=0, R2=0, R3=0, R4=0. No column reduction needed.", "matrix": [[0,0,7,15],[0,0,7,15],[0,0,7,15],[20,15,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col R1 + Col R2 + Row V4 = 3 lines. Vans 1,2,3 have zeros ONLY in {R1,R2}. Cannot assign 3 vans to 2 routes. k = min(7,15,7,15,7,15) = 7.", "matrix": [[0,0,7,15],[0,0,7,15],[0,0,7,15],[20,15,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=7)", "explain": "Subtract k=7 from uncovered cells. Add k=7 to intersections: (V4,R1)=27 and (V4,R2)=22. New zero appears at (V1,R3), (V2,R3), (V3,R3)!", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,0,8],[27,22,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "Vans 1,2,3 now have zeros in R1,R2,R3. Van 4 has zeros in R3,R4. Assign V4→R4, and distribute V1,V2,V3 over R1,R2,R3.", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,0,8],[27,22,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Van 1 → Route 3 (52 min)<br/>Van 2 → Route 1 (38 min)<br/>Van 3 → Route 2 (50 min)<br/>Van 4 → Route 4 (35 min)<br/><strong>Minimum Total Time = 175 minutes</strong>"}
        ]
    },
    {
        "id": "asgn_10", "title": "10. Software Developer Sprint Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 developers to 4 sprint modules (Frontend, Backend, Database, Testing). Story-point cost matrix. Alice, Bob, and Carol are equally proficient in Frontend/Backend, creating a 3-vs-2 Hall's theorem violation.",
        "rowLabels": ["Alice","Bob","Carol","Tech Lead"],
        "colLabels": ["Frontend","Backend","Database","Testing"],
        "steps": [
            {"title": "Step 0: Original Story Points Matrix", "explain": "Estimated story points (effort cost) for each developer-module pairing.", "matrix": [[8,8,12,16],[6,6,10,14],[10,10,14,18],[15,13,7,7]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: Alice=8, Bob=6, Carol=10, Lead=7. Subtract each minimum.", "matrix": [[0,0,4,8],[0,0,4,8],[0,0,4,8],[8,6,0,0]], "showRowMin": True, "rowMins": [8,6,10,7]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: FE=0, BE=0, DB=0, Test=0. No further reduction needed.", "matrix": [[0,0,4,8],[0,0,4,8],[0,0,4,8],[8,6,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col FE + Col BE + Row Lead = 3 lines. Alice, Bob, Carol all have zeros ONLY in {Frontend, Backend} - Hall's: 3 devs, 2 columns. k = min(4,8,4,8,4,8) = 4.", "matrix": [[0,0,4,8],[0,0,4,8],[0,0,4,8],[8,6,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=4)", "explain": "Subtract k=4 from uncovered cells. Add k=4 to intersections: (Lead,FE)=12 and (Lead,BE)=10. All three developers now have zeros in Database module as well!", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,0,4],[12,10,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "Developers have zeros in FE, BE, DB. Tech Lead has zeros in DB, Testing. Lead must take Testing (DB needed for developers). Alice, Bob, Carol share FE, BE, DB.", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,0,4],[12,10,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Alice → Database (12 pts)<br/>Bob → Frontend (6 pts)<br/>Carol → Backend (10 pts)<br/>Tech Lead → Testing (7 pts)<br/><strong>Minimum Total Story Points = 35</strong>"}
        ]
    },
    {
        "id": "asgn_11", "title": "11. Faculty Classroom Schedule Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 faculty to 4 slots (8AM, 10AM, 12PM, 2PM) with minimum total inconvenience. Profs P, Q, R prefer morning equally - zeros only in {8AM, 10AM} for 3 faculty members, requiring line coverage adjustment.",
        "rowLabels": ["Prof. P","Prof. Q","Prof. R","Prof. S"],
        "colLabels": ["8 AM","10 AM","12 PM","2 PM"],
        "steps": [
            {"title": "Step 0: Original Inconvenience Matrix", "explain": "Inconvenience score for each faculty-slot pairing (lower = preferred).", "matrix": [[11,11,14,19],[9,9,12,17],[13,13,16,21],[18,16,8,8]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: P=11, Q=9, R=13, S=8. Subtract each row minimum.", "matrix": [[0,0,3,8],[0,0,3,8],[0,0,3,8],[10,8,0,0]], "showRowMin": True, "rowMins": [11,9,13,8]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: 8AM=0, 10AM=0, 12PM=0, 2PM=0. No further reduction needed.", "matrix": [[0,0,3,8],[0,0,3,8],[0,0,3,8],[10,8,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col 8AM + Col 10AM + Row Prof.S = 3 lines. P,Q,R have zeros ONLY in {8AM, 10AM}. Hall's: 3 professors, 2 zero-columns. k = min(3,8,3,8,3,8) = 3.", "matrix": [[0,0,3,8],[0,0,3,8],[0,0,3,8],[10,8,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=3)", "explain": "Subtract k=3 from uncovered cells. Add k=3 to intersections: (S,8AM)=13 and (S,10AM)=11. Now profs P,Q,R get a new zero at 12PM!", "matrix": [[0,0,0,5],[0,0,0,5],[0,0,0,5],[13,11,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "P,Q,R have zeros in 8AM, 10AM, 12PM. Prof.S has zeros in 12PM and 2PM. Assign S→2PM (to free 12PM for P/Q/R). Faculty share the three morning/midday slots.", "matrix": [[0,0,0,5],[0,0,0,5],[0,0,0,5],[13,11,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Prof. P → 12 PM (14)<br/>Prof. Q → 8 AM (9)<br/>Prof. R → 10 AM (13)<br/>Prof. S → 2 PM (8)<br/><strong>Minimum Total Inconvenience = 44</strong>"}
        ]
    },
    {
        "id": "asgn_12", "title": "12. Construction Worker Task Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 workers to 4 tasks (Excavation, Concreting, Carpentry, Electrical). Hours matrix. Workers 1,2,3 are equally efficient in Excavation and Concreting - 3 workers, 2 columns creates a Hall's violation.",
        "rowLabels": ["Worker 1","Worker 2","Worker 3","Foreman"],
        "colLabels": ["Excavation","Concreting","Carpentry","Electrical"],
        "steps": [
            {"title": "Step 0: Original Cost Matrix (hours)", "explain": "Estimated hours for each worker-task pairing.", "matrix": [[16,16,20,26],[12,12,16,22],[20,20,24,30],[24,22,11,11]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: W1=16, W2=12, W3=20, Foreman=11. Subtract each minimum.", "matrix": [[0,0,4,10],[0,0,4,10],[0,0,4,10],[13,11,0,0]], "showRowMin": True, "rowMins": [16,12,20,11]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: Exc=0, Con=0, Carp=0, Elec=0. No further reduction needed.", "matrix": [[0,0,4,10],[0,0,4,10],[0,0,4,10],[13,11,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col Exc + Col Con + Row Foreman = 3 lines. Workers 1,2,3 share zeros ONLY in {Excavation, Concreting}. Hall's condition: |{W1,W2,W3}|=3 > |{Exc,Con}|=2. k = min(4,10,4,10,4,10) = 4.", "matrix": [[0,0,4,10],[0,0,4,10],[0,0,4,10],[13,11,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=4)", "explain": "Subtract k=4 from uncovered cells. Add k=4 to intersections: (Foreman,Exc)=17 and (Foreman,Con)=15. All 3 workers now have zero in Carpentry column too!", "matrix": [[0,0,0,6],[0,0,0,6],[0,0,0,6],[17,15,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "Workers 1,2,3 have zeros in Exc, Con, Carpentry. Foreman has zeros in Carpentry and Electrical. Assign Foreman→Electrical (freeing Carpentry for workers). Workers share Exc, Con, Carp.", "matrix": [[0,0,0,6],[0,0,0,6],[0,0,0,6],[17,15,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Worker 1 → Carpentry (20 hrs)<br/>Worker 2 → Excavation (12 hrs)<br/>Worker 3 → Concreting (20 hrs)<br/>Foreman → Electrical (11 hrs)<br/><strong>Minimum Total Time = 63 hours</strong>"}
        ]
    },
    {
        "id": "asgn_13", "title": "13. Exam Invigilator Hall Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 invigilators to 4 exam halls. Cost = travel + setup time (minutes). Invigilators W,X,Y have equal proximity to Halls A and B - 3 rows sharing zeros in 2 columns, requiring line adjustment.",
        "rowLabels": ["Inv. W","Inv. X","Inv. Y","Chief Inv."],
        "colLabels": ["Hall A","Hall B","Hall C","Hall D"],
        "steps": [
            {"title": "Step 0: Original Cost Matrix (minutes)", "explain": "Total time cost for each invigilator-hall assignment.", "matrix": [[18,18,23,30],[15,15,20,27],[21,21,26,33],[28,25,12,12]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: W=18, X=15, Y=21, Chief=12. Subtract each row minimum.", "matrix": [[0,0,5,12],[0,0,5,12],[0,0,5,12],[16,13,0,0]], "showRowMin": True, "rowMins": [18,15,21,12]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: A=0, B=0, C=0, D=0. No further reduction needed.", "matrix": [[0,0,5,12],[0,0,5,12],[0,0,5,12],[16,13,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col A + Col B + Row Chief = 3 lines. W,X,Y share zeros ONLY in {Hall A, Hall B}. Hall's: 3 invigilators need 3 distinct halls but only 2 zero-columns exist. k = min(5,12,5,12,5,12) = 5.", "matrix": [[0,0,5,12],[0,0,5,12],[0,0,5,12],[16,13,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=5)", "explain": "Subtract k=5 from uncovered cells. Add k=5 to intersections: (Chief,A)=21 and (Chief,B)=18. New zero appears at Hall C for W, X, Y!", "matrix": [[0,0,0,7],[0,0,0,7],[0,0,0,7],[21,18,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "W,X,Y now have zeros in A, B, C. Chief has zeros in C and D. Chief must take D (to free C for junior invigilators). W,X,Y share Halls A, B, C.", "matrix": [[0,0,0,7],[0,0,0,7],[0,0,0,7],[21,18,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Inv. W → Hall C (23 min)<br/>Inv. X → Hall A (15 min)<br/>Inv. Y → Hall B (21 min)<br/>Chief Inv. → Hall D (12 min)<br/><strong>Minimum Total Time = 71 minutes</strong>"}
        ]
    },
    {
        "id": "asgn_14", "title": "14. Financial Analyst Portfolio Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 analysts to 4 portfolios (Equity, Debt, Hybrid, Gold). Risk-adjusted cost matrix. Analysts P,Q,R have identical proficiency for Equity & Debt - 3 analysts, 2 zero-columns. Hall's theorem violated.",
        "rowLabels": ["Analyst P","Analyst Q","Analyst R","Senior Analyst"],
        "colLabels": ["Equity","Debt","Hybrid","Gold"],
        "steps": [
            {"title": "Step 0: Original Risk-Cost Matrix", "explain": "Risk-adjusted cost score for each analyst-portfolio pairing.", "matrix": [[20,20,25,32],[16,16,21,28],[24,24,29,36],[30,27,15,15]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: P=20, Q=16, R=24, Senior=15. Subtract each minimum.", "matrix": [[0,0,5,12],[0,0,5,12],[0,0,5,12],[15,12,0,0]], "showRowMin": True, "rowMins": [20,16,24,15]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: Eq=0, Debt=0, Hyb=0, Gold=0. No column reduction needed.", "matrix": [[0,0,5,12],[0,0,5,12],[0,0,5,12],[15,12,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col Equity + Col Debt + Row Senior = 3 lines. P,Q,R have zeros ONLY in {Equity, Debt}. Hall's: |{P,Q,R}|=3 > |{Equity,Debt}|=2. k = min(5,12,5,12,5,12) = 5.", "matrix": [[0,0,5,12],[0,0,5,12],[0,0,5,12],[15,12,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=5)", "explain": "Subtract k=5 from uncovered. Add k=5 to intersections: (Senior,Equity)=20 and (Senior,Debt)=17. Junior analysts P,Q,R now have new zeros in the Hybrid portfolio!", "matrix": [[0,0,0,7],[0,0,0,7],[0,0,0,7],[20,17,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "P,Q,R have zeros in Equity, Debt, Hybrid. Senior has zeros in Hybrid and Gold. Senior must take Gold (Hybrid reserved for P/Q/R rotation). Analysts P,Q,R share Equity, Debt, Hybrid.", "matrix": [[0,0,0,7],[0,0,0,7],[0,0,0,7],[20,17,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Analyst P → Hybrid (25)<br/>Analyst Q → Equity (16)<br/>Analyst R → Debt (24)<br/>Senior Analyst → Gold (15)<br/><strong>Minimum Total Risk-Cost = 80</strong>"}
        ]
    },
    {
        "id": "asgn_15", "title": "15. Supply Chain Agent Territory Assignment",
        "type": "assignment", "difficulty": "hard", "tags": ["assignment","line-coverage","adjustment"],
        "context": "Assign 4 supply chain agents to 4 territories (North, South, East, West). Logistics cost matrix. Agents 1,2,3 have identical efficiency in North & South regions - Hall's theorem violated (3 agents, 2 zero-territory columns).",
        "rowLabels": ["Agent 1","Agent 2","Agent 3","Regional Head"],
        "colLabels": ["North","South","East","West"],
        "steps": [
            {"title": "Step 0: Original Logistics Cost Matrix ($)", "explain": "Total logistics cost for each agent-territory pairing.", "matrix": [[22,22,28,36],[18,18,24,32],[26,26,32,40],[36,32,18,18]], "showRowMin": False},
            {"title": "Step 1: Row Reduction", "explain": "Row mins: A1=22, A2=18, A3=26, Head=18. Subtract each minimum.", "matrix": [[0,0,6,14],[0,0,6,14],[0,0,6,14],[18,14,0,0]], "showRowMin": True, "rowMins": [22,18,26,18]},
            {"title": "Step 2: Column Reduction", "explain": "Col mins: N=0, S=0, E=0, W=0. No further reduction needed.", "matrix": [[0,0,6,14],[0,0,6,14],[0,0,6,14],[18,14,0,0]], "showColMin": True, "colMins": [0,0,0,0]},
            {"title": "Step 3: Line Coverage Test - FAILS (3 lines < n=4)", "explain": "Lines: Col North + Col South + Row Head = 3 lines. Agents 1,2,3 share zeros ONLY in {North, South}. Hall's: 3 agents can't be assigned to only 2 territories. k = min(6,14,6,14,6,14) = 6.", "matrix": [[0,0,6,14],[0,0,6,14],[0,0,6,14],[18,14,0,0]], "lineCols": [0,1], "lineRows": [3]},
            {"title": "Step 4: Adjust Matrix (k=6)", "explain": "Subtract k=6 from uncovered cells. Add k=6 to intersections: (Head,North)=24 and (Head,South)=20. Agents 1,2,3 now also have zeros in the East territory!", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,0,8],[24,20,0,0]]},
            {"title": "Step 5: Final Optimal Assignment", "explain": "Agents 1,2,3 have zeros in North, South, East. Regional Head has zeros in East and West. Head takes West (East freed for agents). Agents share North, South, East.", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,0,8],[24,20,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Agent 1 → East ($28)<br/>Agent 2 → North ($18)<br/>Agent 3 → South ($26)<br/>Regional Head → West ($18)<br/><strong>Minimum Total Logistics Cost = $90</strong>"}
        ]
    }
]


# ─────────────────────────────────────────────────────────────────────────────
sp_problems = [
    {
        "id": "sp_1",
        "title": "1. Seervada Park Sightseeing Tram Route",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "seervada-park"
        ],
        "context": "Seervada Park needs to determine the shortest path from park entrance (O) to station T for tram operation. All distances in miles.",
        "network": {
            "nodes": [
                {
                    "id": "O",
                    "x": 8,
                    "y": 50,
                    "label": "O"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 72,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 55,
                    "y": 10,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 80,
                    "y": 25,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 62,
                    "y": 60,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "O",
                    "to": "A",
                    "w": 2
                },
                {
                    "from": "O",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "O",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 7
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 1
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 1
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 7
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "O",
                "closestUnsolved": "A",
                "totalDist": "2",
                "nthNode": "A",
                "minDist": "2",
                "lastConn": "O-A",
                "solvedSet": [
                    "O",
                    "A"
                ],
                "activeEdges": [
                    "OA",
                    "OB",
                    "OC"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "O, A",
                "closestUnsolved": "C",
                "totalDist": "3",
                "nthNode": "C",
                "minDist": "3",
                "lastConn": "O-C",
                "solvedSet": [
                    "O",
                    "A",
                    "C"
                ],
                "activeEdges": [
                    "OB",
                    "OC",
                    "AB",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "O, A, C",
                "closestUnsolved": "B",
                "totalDist": "4",
                "nthNode": "B",
                "minDist": "4",
                "lastConn": "O-B",
                "solvedSet": [
                    "O",
                    "A",
                    "C",
                    "B"
                ],
                "activeEdges": [
                    "OB",
                    "AB",
                    "AD",
                    "CB",
                    "CD"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "O, A, C, B",
                "closestUnsolved": "D",
                "totalDist": "7",
                "nthNode": "D",
                "minDist": "7",
                "lastConn": "C-D",
                "solvedSet": [
                    "O",
                    "A",
                    "C",
                    "B",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "CD",
                    "BE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "O, A, C, B, D",
                "closestUnsolved": "E",
                "totalDist": "7",
                "nthNode": "E",
                "minDist": "7",
                "lastConn": "B-E",
                "solvedSet": [
                    "O",
                    "A",
                    "C",
                    "B",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "DE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "O, A, C, B, D, E",
                "closestUnsolved": "T",
                "totalDist": "12",
                "nthNode": "T",
                "minDist": "12",
                "lastConn": "D-T",
                "solvedSet": [
                    "O",
                    "A",
                    "C",
                    "B",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "OC",
                    "CO",
                    "CD",
                    "DC",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 C \u2190 O",
        "result": "Shortest Route: <strong>O \u2192 C \u2192 D \u2192 T</strong><br/>Total Distance = <strong>12 units</strong>"
    },
    {
        "id": "sp_2",
        "title": "2. City Road Network Route Optimization",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "road"
        ],
        "context": "Find the shortest distance route from origin city S to destination city T through the arterial road network.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 4
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 8
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 7
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 4
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "4",
                "nthNode": "A",
                "minDist": "4",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "6",
                "nthNode": "B",
                "minDist": "6",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "9",
                "nthNode": "C",
                "minDist": "9",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "12",
                "nthNode": "D",
                "minDist": "12",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "12",
                "nthNode": "E",
                "minDist": "12",
                "lastConn": "C-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "16",
                "nthNode": "T",
                "minDist": "16",
                "lastConn": "E-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AC",
                    "CA",
                    "CE",
                    "EC",
                    "ET",
                    "TE"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 E \u2190 C \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 C \u2192 E \u2192 T</strong><br/>Total Distance = <strong>16 units</strong>"
    },
    {
        "id": "sp_3",
        "title": "3. Supply Chain Hub-and-Spoke Routing",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "supply"
        ],
        "context": "Determine the lowest cost logistics shipping route from supplier S to retail terminal T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 6
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "3",
                "nthNode": "A",
                "minDist": "3",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "5",
                "nthNode": "B",
                "minDist": "5",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "D",
                "totalDist": "7",
                "nthNode": "D",
                "minDist": "7",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, D",
                "closestUnsolved": "C",
                "totalDist": "8",
                "nthNode": "C",
                "minDist": "8",
                "lastConn": "B-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "BC",
                    "BE",
                    "DC",
                    "DT"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, D, C",
                "closestUnsolved": "E",
                "totalDist": "11",
                "nthNode": "E",
                "minDist": "11",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D",
                    "C",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "DT",
                    "CE"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, D, C, E",
                "closestUnsolved": "T",
                "totalDist": "12",
                "nthNode": "T",
                "minDist": "12",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D",
                    "C",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>12 units</strong>"
    },
    {
        "id": "sp_4",
        "title": "4. Emergency Ambulance Hospital Routing",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "ambulance"
        ],
        "context": "Find the fastest route for an emergency ambulance from accident site S to trauma hospital T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 2
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 1
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 6
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "2",
                "nthNode": "A",
                "minDist": "2",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "3",
                "nthNode": "B",
                "minDist": "3",
                "lastConn": "A-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "6",
                "nthNode": "C",
                "minDist": "6",
                "lastConn": "B-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "8",
                "nthNode": "D",
                "minDist": "8",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "8",
                "nthNode": "E",
                "minDist": "8",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "10",
                "nthNode": "T",
                "minDist": "10",
                "lastConn": "E-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AB",
                    "BA",
                    "BE",
                    "EB",
                    "ET",
                    "TE"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 E \u2190 B \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 B \u2192 E \u2192 T</strong><br/>Total Distance = <strong>10 units</strong>"
    },
    {
        "id": "sp_5",
        "title": "5. Campus Navigation Pedestrian Walkway",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "campus"
        ],
        "context": "Find the shortest walking path from north campus gate S to main library T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 6
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "3",
                "nthNode": "A",
                "minDist": "3",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "5",
                "nthNode": "B",
                "minDist": "5",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "D",
                "totalDist": "6",
                "nthNode": "D",
                "minDist": "6",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, D",
                "closestUnsolved": "C",
                "totalDist": "7",
                "nthNode": "C",
                "minDist": "7",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "BC",
                    "BE",
                    "DC",
                    "DT"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, D, C",
                "closestUnsolved": "E",
                "totalDist": "9",
                "nthNode": "E",
                "minDist": "9",
                "lastConn": "C-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D",
                    "C",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "DT",
                    "CE"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, D, C, E",
                "closestUnsolved": "T",
                "totalDist": "11",
                "nthNode": "T",
                "minDist": "11",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "D",
                    "C",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>11 units</strong>"
    },
    {
        "id": "sp_6",
        "title": "6. Computer Network Minimum Latency Path",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "network"
        ],
        "context": "Route data packets from source server S to destination server T with minimum total latency (ms).",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 5
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 1
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 7
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 6
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 3
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 5
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "B",
                "totalDist": "3",
                "nthNode": "B",
                "minDist": "3",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "B"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, B",
                "closestUnsolved": "A",
                "totalDist": "4",
                "nthNode": "A",
                "minDist": "4",
                "lastConn": "B-A",
                "solvedSet": [
                    "S",
                    "B",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "BA",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, B, A",
                "closestUnsolved": "E",
                "totalDist": "7",
                "nthNode": "E",
                "minDist": "7",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "E"
                ],
                "activeEdges": [
                    "BC",
                    "BE",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, B, A, E",
                "closestUnsolved": "C",
                "totalDist": "8",
                "nthNode": "C",
                "minDist": "8",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "E",
                    "C"
                ],
                "activeEdges": [
                    "BC",
                    "AC",
                    "AD",
                    "EC",
                    "ET"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, B, A, E, C",
                "closestUnsolved": "D",
                "totalDist": "10",
                "nthNode": "D",
                "minDist": "10",
                "lastConn": "C-D",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "E",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "ET",
                    "CD"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, B, A, E, C, D",
                "closestUnsolved": "T",
                "totalDist": "12",
                "nthNode": "T",
                "minDist": "12",
                "lastConn": "E-T",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "E",
                    "C",
                    "D",
                    "T"
                ],
                "activeEdges": [
                    "ET",
                    "DT"
                ],
                "pathEdges": [
                    "SB",
                    "BS",
                    "BE",
                    "EB",
                    "ET",
                    "TE"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 E \u2190 B \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 B \u2192 E \u2192 T</strong><br/>Total Distance = <strong>12 units</strong>"
    },
    {
        "id": "sp_7",
        "title": "7. Pipeline Minimum Pumping Cost Path",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "pipeline"
        ],
        "context": "Find the minimum energy pumping path from oil well S to refinery T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 6
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 5
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 6
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "B",
                "totalDist": "4",
                "nthNode": "B",
                "minDist": "4",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "B"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, B",
                "closestUnsolved": "A",
                "totalDist": "6",
                "nthNode": "A",
                "minDist": "6",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "B",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, B, A",
                "closestUnsolved": "C",
                "totalDist": "6",
                "nthNode": "C",
                "minDist": "6",
                "lastConn": "B-C",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "C"
                ],
                "activeEdges": [
                    "BC",
                    "BE",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, B, A, C",
                "closestUnsolved": "E",
                "totalDist": "9",
                "nthNode": "E",
                "minDist": "9",
                "lastConn": "C-E",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "C",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "AD",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, B, A, C, E",
                "closestUnsolved": "D",
                "totalDist": "10",
                "nthNode": "D",
                "minDist": "10",
                "lastConn": "C-D",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "C",
                    "E",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "CD",
                    "ET"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, B, A, C, E, D",
                "closestUnsolved": "T",
                "totalDist": "11",
                "nthNode": "T",
                "minDist": "11",
                "lastConn": "E-T",
                "solvedSet": [
                    "S",
                    "B",
                    "A",
                    "C",
                    "E",
                    "D",
                    "T"
                ],
                "activeEdges": [
                    "ET",
                    "DT"
                ],
                "pathEdges": [
                    "SB",
                    "BS",
                    "BC",
                    "CB",
                    "CE",
                    "EC",
                    "ET",
                    "TE"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 E \u2190 C \u2190 B \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 B \u2192 C \u2192 E \u2192 T</strong><br/>Total Distance = <strong>11 units</strong>"
    },
    {
        "id": "sp_8",
        "title": "8. Train Route 5-City Distance Minimization",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "train"
        ],
        "context": "Optimize express train track route between origin station S and terminal T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 8
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 10
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 9
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 7
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 5
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 4
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "8",
                "nthNode": "A",
                "minDist": "8",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "10",
                "nthNode": "B",
                "minDist": "10",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "14",
                "nthNode": "C",
                "minDist": "14",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "17",
                "nthNode": "D",
                "minDist": "17",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "17",
                "nthNode": "E",
                "minDist": "17",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "21",
                "nthNode": "T",
                "minDist": "21",
                "lastConn": "E-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SB",
                    "BS",
                    "BE",
                    "EB",
                    "ET",
                    "TE"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 E \u2190 B \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 B \u2192 E \u2192 T</strong><br/>Total Distance = <strong>21 units</strong>"
    },
    {
        "id": "sp_9",
        "title": "9. Last-Mile Urban Delivery Routing",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "delivery"
        ],
        "context": "Find the shortest delivery van route from central warehouse S to customer station T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 6
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 3
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 5
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "3",
                "nthNode": "A",
                "minDist": "3",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "4",
                "nthNode": "B",
                "minDist": "4",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "7",
                "nthNode": "C",
                "minDist": "7",
                "lastConn": "B-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "7",
                "nthNode": "D",
                "minDist": "7",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "10",
                "nthNode": "E",
                "minDist": "10",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "10",
                "nthNode": "T",
                "minDist": "10",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>10 units</strong>"
    },
    {
        "id": "sp_10",
        "title": "10. Airport Layover Travel Time Minimization",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "airport"
        ],
        "context": "Determine the shortest travel path between airport gates S and T via transit shuttles.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 4
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 5
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "4",
                "nthNode": "A",
                "minDist": "4",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "6",
                "nthNode": "B",
                "minDist": "6",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "7",
                "nthNode": "C",
                "minDist": "7",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "9",
                "nthNode": "D",
                "minDist": "9",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "10",
                "nthNode": "E",
                "minDist": "10",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "13",
                "nthNode": "T",
                "minDist": "13",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>13 units</strong>"
    },
    {
        "id": "sp_11",
        "title": "11. Telecom Signal Path Loss Minimization",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "telecom"
        ],
        "context": "Route microwave communications signal from tower S to tower T with minimum attenuation.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 5
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 7
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 6
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 5
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 3
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 4
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "5",
                "nthNode": "A",
                "minDist": "5",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "7",
                "nthNode": "B",
                "minDist": "7",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "9",
                "nthNode": "C",
                "minDist": "9",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "11",
                "nthNode": "D",
                "minDist": "11",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "11",
                "nthNode": "E",
                "minDist": "11",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "14",
                "nthNode": "T",
                "minDist": "14",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>14 units</strong>"
    },
    {
        "id": "sp_12",
        "title": "12. Water Distribution Pressure Loss Path",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "water"
        ],
        "context": "Determine main water pipe route from reservoir S to district T with minimum friction loss.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 6
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 8
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 5
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 6
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "6",
                "nthNode": "A",
                "minDist": "6",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "8",
                "nthNode": "B",
                "minDist": "8",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "10",
                "nthNode": "C",
                "minDist": "10",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "11",
                "nthNode": "D",
                "minDist": "11",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "12",
                "nthNode": "E",
                "minDist": "12",
                "lastConn": "C-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "15",
                "nthNode": "T",
                "minDist": "15",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>15 units</strong>"
    },
    {
        "id": "sp_13",
        "title": "13. Tourist Budget Airfare Itinerary",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "tourist"
        ],
        "context": "Find the cheapest flight connection itinerary from departure airport S to destination T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 6
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "3",
                "nthNode": "A",
                "minDist": "3",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "5",
                "nthNode": "B",
                "minDist": "5",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "7",
                "nthNode": "C",
                "minDist": "7",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "9",
                "nthNode": "D",
                "minDist": "9",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "10",
                "nthNode": "E",
                "minDist": "10",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "12",
                "nthNode": "T",
                "minDist": "12",
                "lastConn": "E-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SB",
                    "BS",
                    "BE",
                    "EB",
                    "ET",
                    "TE"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 E \u2190 B \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 B \u2192 E \u2192 T</strong><br/>Total Distance = <strong>12 units</strong>"
    },
    {
        "id": "sp_14",
        "title": "14. Cargo Container Port Routing",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "cargo"
        ],
        "context": "Optimize container truck route from port gate S to shipping berth T.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 7
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 9
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 6
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 3
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 5
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "7",
                "nthNode": "A",
                "minDist": "7",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "9",
                "nthNode": "B",
                "minDist": "9",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "12",
                "nthNode": "C",
                "minDist": "12",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "13",
                "nthNode": "D",
                "minDist": "13",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "13",
                "nthNode": "E",
                "minDist": "13",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "16",
                "nthNode": "T",
                "minDist": "16",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>16 units</strong>"
    },
    {
        "id": "sp_15",
        "title": "15. Electric Grid Transmission Line Path",
        "type": "shortest_ppt",
        "difficulty": "medium",
        "tags": [
            "shortest-path",
            "grid"
        ],
        "context": "Select power transmission line path from sub-station S to grid node T to minimize resistance.",
        "network": {
            "nodes": [
                {
                    "id": "S",
                    "x": 8,
                    "y": 50,
                    "label": "S"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 78,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 52,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 75,
                    "y": 22,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 75,
                    "y": 78,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "S",
                    "to": "A",
                    "w": 5
                },
                {
                    "from": "S",
                    "to": "B",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 5
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 6
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "n": 1,
                "solvedNodes": "S",
                "closestUnsolved": "A",
                "totalDist": "5",
                "nthNode": "A",
                "minDist": "5",
                "lastConn": "S-A",
                "solvedSet": [
                    "S",
                    "A"
                ],
                "activeEdges": [
                    "SA",
                    "SB"
                ]
            },
            {
                "n": 2,
                "solvedNodes": "S, A",
                "closestUnsolved": "B",
                "totalDist": "6",
                "nthNode": "B",
                "minDist": "6",
                "lastConn": "S-B",
                "solvedSet": [
                    "S",
                    "A",
                    "B"
                ],
                "activeEdges": [
                    "SB",
                    "AC",
                    "AD"
                ]
            },
            {
                "n": 3,
                "solvedNodes": "S, A, B",
                "closestUnsolved": "C",
                "totalDist": "9",
                "nthNode": "C",
                "minDist": "9",
                "lastConn": "A-C",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C"
                ],
                "activeEdges": [
                    "AC",
                    "AD",
                    "BC",
                    "BE"
                ]
            },
            {
                "n": 4,
                "solvedNodes": "S, A, B, C",
                "closestUnsolved": "D",
                "totalDist": "10",
                "nthNode": "D",
                "minDist": "10",
                "lastConn": "A-D",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D"
                ],
                "activeEdges": [
                    "AD",
                    "BE",
                    "CD",
                    "CE"
                ]
            },
            {
                "n": 5,
                "solvedNodes": "S, A, B, C, D",
                "closestUnsolved": "E",
                "totalDist": "12",
                "nthNode": "E",
                "minDist": "12",
                "lastConn": "B-E",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E"
                ],
                "activeEdges": [
                    "BE",
                    "CE",
                    "DT"
                ]
            },
            {
                "n": 6,
                "solvedNodes": "S, A, B, C, D, E",
                "closestUnsolved": "T",
                "totalDist": "14",
                "nthNode": "T",
                "minDist": "14",
                "lastConn": "D-T",
                "solvedSet": [
                    "S",
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "T"
                ],
                "activeEdges": [
                    "DT",
                    "ET"
                ],
                "pathEdges": [
                    "SA",
                    "AS",
                    "AD",
                    "DA",
                    "DT",
                    "TD"
                ]
            }
        ],
        "traceback": " Destination to Origin: T \u2190 D \u2190 A \u2190 S",
        "result": "Shortest Route: <strong>S \u2192 A \u2192 D \u2192 T</strong><br/>Total Distance = <strong>14 units</strong>"
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# 5. MST PROBLEMS (15) — with SVG network graph data
# ─────────────────────────────────────────────────────────────────────────────
mst_problems = [
    {
        "id": "mst_1",
        "title": "1. Seervada Park Telephone Line MST",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "seervada-park"
        ],
        "context": "Seervada Park management needs to install telephone lines to connect all 7 stations (O, A, B, C, D, E, T) with minimum total cable length.",
        "network": {
            "nodes": [
                {
                    "id": "O",
                    "x": 8,
                    "y": 50,
                    "label": "O"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 22,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 72,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 55,
                    "y": 10,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 80,
                    "y": 25,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 62,
                    "y": 60,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 92,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "O",
                    "to": "A",
                    "w": 2
                },
                {
                    "from": "O",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "O",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 7
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 1
                },
                {
                    "from": "B",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 1
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 7
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, O}",
                "addedNode": "A",
                "linkUsed": "O \u2013 A",
                "linkLen": 2,
                "totalLength": 2,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, O}, the minimum weight link to an unconnected node is O \u2013 A with weight 2.",
                "mstEdges": [
                    "OA"
                ],
                "connectedNodes": [
                    "A",
                    "O"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, O}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 2,
                "totalLength": 4,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, O}, the minimum weight link to an unconnected node is A \u2013 B with weight 2.",
                "mstEdges": [
                    "OA",
                    "AB"
                ],
                "connectedNodes": [
                    "A",
                    "O",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, O}",
                "addedNode": "C",
                "linkUsed": "B \u2013 C",
                "linkLen": 1,
                "totalLength": 5,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, O}, the minimum weight link to an unconnected node is B \u2013 C with weight 1.",
                "mstEdges": [
                    "OA",
                    "AB",
                    "BC"
                ],
                "connectedNodes": [
                    "A",
                    "C",
                    "O",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, E, O}",
                "addedNode": "E",
                "linkUsed": "B \u2013 E",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 4: Connect Node E",
                "explain": "From connected set {A, B, C, E, O}, the minimum weight link to an unconnected node is B \u2013 E with weight 3.",
                "mstEdges": [
                    "OA",
                    "AB",
                    "BC",
                    "BE"
                ],
                "connectedNodes": [
                    "E",
                    "O",
                    "C",
                    "B",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, O}",
                "addedNode": "D",
                "linkUsed": "E \u2013 D",
                "linkLen": 1,
                "totalLength": 9,
                "title": "Step 5: Connect Node D",
                "explain": "From connected set {A, B, C, D, E, O}, the minimum weight link to an unconnected node is E \u2013 D with weight 1.",
                "mstEdges": [
                    "OA",
                    "AB",
                    "BC",
                    "BE",
                    "ED"
                ],
                "connectedNodes": [
                    "E",
                    "O",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, O, T}",
                "addedNode": "T",
                "linkUsed": "D \u2013 T",
                "linkLen": 5,
                "totalLength": 14,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, O, T}, the minimum weight link to an unconnected node is D \u2013 T with weight 5.",
                "mstEdges": [
                    "OA",
                    "AB",
                    "BC",
                    "BE",
                    "ED",
                    "DT"
                ],
                "connectedNodes": [
                    "E",
                    "O",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>O-A(2), A-B(2), B-C(1), B-E(3), D-E(1), D-T(5)</strong><br/><strong>Minimum Total Link Weight = 14 units</strong>"
    },
    {
        "id": "mst_2",
        "title": "2. Midwest TV Cable Regional Network",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "midwest-tv"
        ],
        "context": "Midwest TV Cable Company provides cable service to five housing developments with minimum total cable distance.",
        "network": {
            "nodes": [
                {
                    "id": "City",
                    "x": 10,
                    "y": 50,
                    "label": "City"
                },
                {
                    "id": "A",
                    "x": 32,
                    "y": 20,
                    "label": "Sub-A"
                },
                {
                    "id": "B",
                    "x": 55,
                    "y": 15,
                    "label": "Sub-B"
                },
                {
                    "id": "C",
                    "x": 75,
                    "y": 30,
                    "label": "Sub-C"
                },
                {
                    "id": "D",
                    "x": 80,
                    "y": 65,
                    "label": "Sub-D"
                },
                {
                    "id": "E",
                    "x": 55,
                    "y": 80,
                    "label": "Sub-E"
                }
            ],
            "edges": [
                {
                    "from": "City",
                    "to": "A",
                    "w": 4
                },
                {
                    "from": "City",
                    "to": "E",
                    "w": 8
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "E",
                    "w": 6
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "B",
                    "to": "D",
                    "w": 7
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 5
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{City, Sub-A}",
                "addedNode": "Sub-A",
                "linkUsed": "City \u2013 Sub-A",
                "linkLen": 4,
                "totalLength": 4,
                "title": "Step 1: Connect Node Sub-A",
                "explain": "From connected set {City, Sub-A}, the minimum weight link to an unconnected node is City \u2013 Sub-A with weight 4.",
                "mstEdges": [
                    "CityA"
                ],
                "connectedNodes": [
                    "A",
                    "City"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{City, Sub-A, Sub-B}",
                "addedNode": "Sub-B",
                "linkUsed": "Sub-A \u2013 Sub-B",
                "linkLen": 3,
                "totalLength": 7,
                "title": "Step 2: Connect Node Sub-B",
                "explain": "From connected set {City, Sub-A, Sub-B}, the minimum weight link to an unconnected node is Sub-A \u2013 Sub-B with weight 3.",
                "mstEdges": [
                    "CityA",
                    "AB"
                ],
                "connectedNodes": [
                    "A",
                    "City",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{City, Sub-A, Sub-B, Sub-C}",
                "addedNode": "Sub-C",
                "linkUsed": "Sub-B \u2013 Sub-C",
                "linkLen": 2,
                "totalLength": 9,
                "title": "Step 3: Connect Node Sub-C",
                "explain": "From connected set {City, Sub-A, Sub-B, Sub-C}, the minimum weight link to an unconnected node is Sub-B \u2013 Sub-C with weight 2.",
                "mstEdges": [
                    "CityA",
                    "AB",
                    "BC"
                ],
                "connectedNodes": [
                    "A",
                    "City",
                    "C",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{City, Sub-A, Sub-B, Sub-C, Sub-D}",
                "addedNode": "Sub-D",
                "linkUsed": "Sub-C \u2013 Sub-D",
                "linkLen": 5,
                "totalLength": 14,
                "title": "Step 4: Connect Node Sub-D",
                "explain": "From connected set {City, Sub-A, Sub-B, Sub-C, Sub-D}, the minimum weight link to an unconnected node is Sub-C \u2013 Sub-D with weight 5.",
                "mstEdges": [
                    "CityA",
                    "AB",
                    "BC",
                    "CD"
                ],
                "connectedNodes": [
                    "C",
                    "B",
                    "D",
                    "A",
                    "City"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{City, Sub-A, Sub-B, Sub-C, Sub-D, Sub-E}",
                "addedNode": "Sub-E",
                "linkUsed": "Sub-D \u2013 Sub-E",
                "linkLen": 3,
                "totalLength": 17,
                "title": "Step 5: Connect Node Sub-E",
                "explain": "From connected set {City, Sub-A, Sub-B, Sub-C, Sub-D, Sub-E}, the minimum weight link to an unconnected node is Sub-D \u2013 Sub-E with weight 3.",
                "mstEdges": [
                    "CityA",
                    "AB",
                    "BC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "C",
                    "B",
                    "D",
                    "A",
                    "City"
                ]
            }
        ],
        "result": "MST Links Used: <strong>City-Sub-A(4), Sub-A-Sub-B(3), Sub-B-Sub-C(2), Sub-C-Sub-D(5), Sub-D-Sub-E(3)</strong><br/><strong>Minimum Total Link Weight = 17 units</strong>"
    },
    {
        "id": "mst_3",
        "title": "3. Office Fiber Optic Network Cluster",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "office-fiber"
        ],
        "context": "Connect all office department clusters (Hub, A, B, C, D, E, Gateway) with minimum total fiber optic cabling.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 8
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 3,
                "totalLength": 3,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 3.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 2,
                "totalLength": 5,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "B \u2013 C",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is B \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, E, Hub}",
                "addedNode": "E",
                "linkUsed": "C \u2013 E",
                "linkLen": 4,
                "totalLength": 12,
                "title": "Step 4: Connect Node E",
                "explain": "From connected set {A, B, C, E, Hub}, the minimum weight link to an unconnected node is C \u2013 E with weight 4.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 2,
                "totalLength": 14,
                "title": "Step 5: Connect Node T",
                "explain": "From connected set {A, B, C, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "D",
                "linkUsed": "E \u2013 D",
                "linkLen": 3,
                "totalLength": 17,
                "title": "Step 6: Connect Node D",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CE",
                    "ET",
                    "ED"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(3), A-B(2), B-C(3), C-E(4), D-E(3), E-T(2)</strong><br/><strong>Minimum Total Link Weight = 17 units</strong>"
    },
    {
        "id": "mst_4",
        "title": "4. Village Water Supply Pipeline Network",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "water-pipeline"
        ],
        "context": "Design a water supply distribution grid connecting all 7 village sectors with minimum total pipeline distance.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 5
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 7
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 3
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "D",
                    "w": 8
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 4,
                "totalLength": 4,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 4.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 3,
                "totalLength": 7,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "B \u2013 C",
                "linkLen": 2,
                "totalLength": 9,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is B \u2013 C with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 12,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, Hub, T}",
                "addedNode": "T",
                "linkUsed": "D \u2013 T",
                "linkLen": 3,
                "totalLength": 15,
                "title": "Step 5: Connect Node T",
                "explain": "From connected set {A, B, C, D, Hub, T}, the minimum weight link to an unconnected node is D \u2013 T with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CD",
                    "DT"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "E",
                "linkUsed": "T \u2013 E",
                "linkLen": 2,
                "totalLength": 17,
                "title": "Step 6: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is T \u2013 E with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CD",
                    "DT",
                    "TE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(4), A-B(3), B-C(2), C-D(3), D-T(3), E-T(2)</strong><br/><strong>Minimum Total Link Weight = 17 units</strong>"
    },
    {
        "id": "mst_5",
        "title": "5. Campus LAN High-Speed Infrastructure",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "campus-lan"
        ],
        "context": "Connect all academic building clusters to the campus core network with minimum fiber run length.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 2
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 7
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 2,
                "totalLength": 2,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 2.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 3,
                "totalLength": 5,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, E, Hub}",
                "addedNode": "E",
                "linkUsed": "C \u2013 E",
                "linkLen": 3,
                "totalLength": 11,
                "title": "Step 4: Connect Node E",
                "explain": "From connected set {A, B, C, E, Hub}, the minimum weight link to an unconnected node is C \u2013 E with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "D",
                "linkUsed": "E \u2013 D",
                "linkLen": 2,
                "totalLength": 13,
                "title": "Step 5: Connect Node D",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is E \u2013 D with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CE",
                    "ED"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 16,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CE",
                    "ED",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(2), A-B(3), A-C(3), C-E(3), D-E(2), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 16 units</strong>"
    },
    {
        "id": "mst_6",
        "title": "6. Railway Track Regional Interconnection",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "railway-track"
        ],
        "context": "Connect 8 regional railway stations and freight yards with minimum track laying distance.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 10,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "Top",
                    "x": 48,
                    "y": 15,
                    "label": "Top"
                },
                {
                    "id": "C",
                    "x": 48,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 70,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 70,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 5
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 6
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 8
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "Top",
                    "w": 2
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "Top",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 7
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 5,
                "totalLength": 5,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 5.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, Hub, Top}",
                "addedNode": "Top",
                "linkUsed": "A \u2013 Top",
                "linkLen": 2,
                "totalLength": 7,
                "title": "Step 2: Connect Node Top",
                "explain": "From connected set {A, Hub, Top}, the minimum weight link to an unconnected node is A \u2013 Top with weight 2.",
                "mstEdges": [
                    "HubA",
                    "ATop"
                ],
                "connectedNodes": [
                    "Hub",
                    "Top",
                    "A"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, C, Hub, Top}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 3,
                "totalLength": 10,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, C, Hub, Top}, the minimum weight link to an unconnected node is A \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "ATop",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "Top",
                    "A"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, C, D, Hub, Top}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 13,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, C, D, Hub, Top}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "ATop",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Top",
                    "Hub",
                    "C",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, C, D, E, Hub, Top}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 3,
                "totalLength": 16,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, C, D, E, Hub, Top}, the minimum weight link to an unconnected node is D \u2013 E with weight 3.",
                "mstEdges": [
                    "HubA",
                    "ATop",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Top",
                    "Hub",
                    "C",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, C, D, E, Hub, T, Top}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 19,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, C, D, E, Hub, T, Top}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubA",
                    "ATop",
                    "AC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Top",
                    "Hub",
                    "C",
                    "T",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 7,
                "connectedSet": "{A, B, C, D, E, Hub, T, Top}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 4,
                "totalLength": 23,
                "title": "Step 7: Connect Node B",
                "explain": "From connected set {A, B, C, D, E, Hub, T, Top}, the minimum weight link to an unconnected node is A \u2013 B with weight 4.",
                "mstEdges": [
                    "HubA",
                    "ATop",
                    "AC",
                    "CD",
                    "DE",
                    "ET",
                    "AB"
                ],
                "connectedNodes": [
                    "E",
                    "Top",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(5), A-B(4), A-C(3), A-Top(2), C-D(3), D-E(3), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 23 units</strong>"
    },
    {
        "id": "mst_7",
        "title": "7. Substation Electrical Grid Wiring",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "electrical-grid"
        ],
        "context": "Interconnect regional substations and power plants to form an electrical minimum spanning tree.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 6
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 5
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 9
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 7
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{B, Hub}",
                "addedNode": "B",
                "linkUsed": "Hub \u2013 B",
                "linkLen": 5,
                "totalLength": 5,
                "title": "Step 1: Connect Node B",
                "explain": "From connected set {B, Hub}, the minimum weight link to an unconnected node is Hub \u2013 B with weight 5.",
                "mstEdges": [
                    "HubB"
                ],
                "connectedNodes": [
                    "Hub",
                    "B"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "A",
                "linkUsed": "B \u2013 A",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 2: Connect Node A",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is B \u2013 A with weight 3.",
                "mstEdges": [
                    "HubB",
                    "BA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 4,
                "totalLength": 12,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 4.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 15,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 17,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 20,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-B(5), A-B(3), A-C(4), C-D(3), D-E(2), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 20 units</strong>"
    },
    {
        "id": "mst_8",
        "title": "8. Irrigation Canal Distribution Network",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "irrigation-canal"
        ],
        "context": "Connect headworks to all agricultural canal clusters with minimum total canal length.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 6
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 7
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 4,
                "totalLength": 4,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 4.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 3,
                "totalLength": 7,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 3,
                "totalLength": 10,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 2,
                "totalLength": 12,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 3,
                "totalLength": 15,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 2,
                "totalLength": 17,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(4), A-B(3), A-C(3), C-D(2), D-E(3), E-T(2)</strong><br/><strong>Minimum Total Link Weight = 17 units</strong>"
    },
    {
        "id": "mst_9",
        "title": "9. Smart City Broadband Fiber Mesh",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "smart-city"
        ],
        "context": "Link 8 urban smart-city data nodes into a minimum spanning broadband backbone.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 10,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "Top",
                    "x": 48,
                    "y": 15,
                    "label": "Top"
                },
                {
                    "id": "C",
                    "x": 48,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 70,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 70,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "Top",
                    "w": 3
                },
                {
                    "from": "Top",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "Top",
                    "w": 6
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 3,
                "totalLength": 3,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 3.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 2,
                "totalLength": 5,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 11,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 13,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, Top}",
                "addedNode": "Top",
                "linkUsed": "C \u2013 Top",
                "linkLen": 3,
                "totalLength": 16,
                "title": "Step 6: Connect Node Top",
                "explain": "From connected set {A, B, C, D, E, Hub, Top}, the minimum weight link to an unconnected node is C \u2013 Top with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "CTop"
                ],
                "connectedNodes": [
                    "E",
                    "Top",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 7,
                "connectedSet": "{A, B, C, D, E, Hub, T, Top}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 19,
                "title": "Step 7: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T, Top}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "CTop",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Top",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(3), A-B(2), A-C(3), C-Top(3), C-D(3), D-E(2), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 19 units</strong>"
    },
    {
        "id": "mst_10",
        "title": "10. Gas Pipeline Regional Grid",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "gas-pipeline"
        ],
        "context": "Connect natural gas compressor station to regional distribution stations with minimum pipeline length.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 5
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 8
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{B, Hub}",
                "addedNode": "B",
                "linkUsed": "Hub \u2013 B",
                "linkLen": 4,
                "totalLength": 4,
                "title": "Step 1: Connect Node B",
                "explain": "From connected set {B, Hub}, the minimum weight link to an unconnected node is Hub \u2013 B with weight 4.",
                "mstEdges": [
                    "HubB"
                ],
                "connectedNodes": [
                    "Hub",
                    "B"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "A",
                "linkUsed": "B \u2013 A",
                "linkLen": 3,
                "totalLength": 7,
                "title": "Step 2: Connect Node A",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is B \u2013 A with weight 3.",
                "mstEdges": [
                    "HubB",
                    "BA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 4,
                "totalLength": 11,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 4.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 14,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 16,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 19,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubB",
                    "BA",
                    "AC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-B(4), A-B(3), A-C(4), C-D(3), D-E(2), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 19 units</strong>"
    },
    {
        "id": "mst_11",
        "title": "11. Hospital Emergency Data Network",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "hospital-data"
        ],
        "context": "Connect critical care units (ER, ICU, OR, Lab, Radiology) with minimum data cabling latency.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 2
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 2,
                "totalLength": 2,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 2.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 2,
                "totalLength": 4,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "B \u2013 C",
                "linkLen": 2,
                "totalLength": 6,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is B \u2013 C with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 9,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 11,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 14,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "BC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(2), A-B(2), B-C(2), C-D(3), D-E(2), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 14 units</strong>"
    },
    {
        "id": "mst_12",
        "title": "12. Chemical Safety Sensor Mesh",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "chemical-sensor"
        ],
        "context": "Connect industrial chemical sensors and alarm units to the central control room with minimum total wire length.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 5
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 2
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 5
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 3,
                "totalLength": 3,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 3.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 2,
                "totalLength": 5,
                "title": "Step 2: Connect Node C",
                "explain": "From connected set {A, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 3: Connect Node B",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AC",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 11,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AC",
                    "AB",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 13,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AC",
                    "AB",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 2,
                "totalLength": 15,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AC",
                    "AB",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(3), A-B(3), A-C(2), C-D(3), D-E(2), E-T(2)</strong><br/><strong>Minimum Total Link Weight = 15 units</strong>"
    },
    {
        "id": "mst_13",
        "title": "13. ISP Regional Fiber Backbone",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "isp-backbone"
        ],
        "context": "Connect 8 regional internet exchange POPs with minimum fiber optic trunk distance.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 10,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "Top",
                    "x": 48,
                    "y": 15,
                    "label": "Top"
                },
                {
                    "id": "C",
                    "x": 48,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 70,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 70,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 5
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 7
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "Top",
                    "w": 4
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "Top",
                    "to": "D",
                    "w": 5
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 4,
                "totalLength": 4,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 4.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 3,
                "totalLength": 7,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 3,
                "totalLength": 10,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 13,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 15,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 18,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 7,
                "connectedSet": "{A, B, C, D, E, Hub, T, Top}",
                "addedNode": "Top",
                "linkUsed": "A \u2013 Top",
                "linkLen": 4,
                "totalLength": 22,
                "title": "Step 7: Connect Node Top",
                "explain": "From connected set {A, B, C, D, E, Hub, T, Top}, the minimum weight link to an unconnected node is A \u2013 Top with weight 4.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "ET",
                    "ATop"
                ],
                "connectedNodes": [
                    "E",
                    "Top",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(4), A-B(3), A-C(3), A-Top(4), C-D(3), D-E(2), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 22 units</strong>"
    },
    {
        "id": "mst_14",
        "title": "14. University Campus Multi-Building Cable",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "university-cable"
        ],
        "context": "Interconnect 7 campus academic complexes with minimum total utility trenching distance.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 14,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 30,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 30,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "C",
                    "x": 50,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 72,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 72,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 5
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 3
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 3,
                "totalLength": 3,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 3.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 2,
                "totalLength": 5,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 11,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 13,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 3,
                "totalLength": 16,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(3), A-B(2), A-C(3), C-D(3), D-E(2), E-T(3)</strong><br/><strong>Minimum Total Link Weight = 16 units</strong>"
    },
    {
        "id": "mst_15",
        "title": "15. E-Commerce Warehouse Automated Conveyor",
        "type": "mst_ppt",
        "difficulty": "medium",
        "tags": [
            "mst",
            "warehouse-conveyor"
        ],
        "context": "Link 8 warehouse sorting, packing, and dispatch zones with minimum conveyor track length.",
        "network": {
            "nodes": [
                {
                    "id": "Hub",
                    "x": 10,
                    "y": 50,
                    "label": "Hub"
                },
                {
                    "id": "A",
                    "x": 28,
                    "y": 20,
                    "label": "A"
                },
                {
                    "id": "B",
                    "x": 28,
                    "y": 80,
                    "label": "B"
                },
                {
                    "id": "Top",
                    "x": 48,
                    "y": 15,
                    "label": "Top"
                },
                {
                    "id": "C",
                    "x": 48,
                    "y": 50,
                    "label": "C"
                },
                {
                    "id": "D",
                    "x": 70,
                    "y": 20,
                    "label": "D"
                },
                {
                    "id": "E",
                    "x": 70,
                    "y": 80,
                    "label": "E"
                },
                {
                    "id": "T",
                    "x": 88,
                    "y": 50,
                    "label": "T"
                }
            ],
            "edges": [
                {
                    "from": "Hub",
                    "to": "A",
                    "w": 3
                },
                {
                    "from": "Hub",
                    "to": "B",
                    "w": 4
                },
                {
                    "from": "Hub",
                    "to": "C",
                    "w": 6
                },
                {
                    "from": "A",
                    "to": "B",
                    "w": 2
                },
                {
                    "from": "A",
                    "to": "C",
                    "w": 3
                },
                {
                    "from": "A",
                    "to": "Top",
                    "w": 5
                },
                {
                    "from": "B",
                    "to": "C",
                    "w": 4
                },
                {
                    "from": "Top",
                    "to": "D",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "D",
                    "w": 3
                },
                {
                    "from": "C",
                    "to": "E",
                    "w": 4
                },
                {
                    "from": "C",
                    "to": "T",
                    "w": 6
                },
                {
                    "from": "D",
                    "to": "E",
                    "w": 2
                },
                {
                    "from": "D",
                    "to": "T",
                    "w": 4
                },
                {
                    "from": "E",
                    "to": "T",
                    "w": 2
                }
            ]
        },
        "steps": [
            {
                "stepNum": 1,
                "connectedSet": "{A, Hub}",
                "addedNode": "A",
                "linkUsed": "Hub \u2013 A",
                "linkLen": 3,
                "totalLength": 3,
                "title": "Step 1: Connect Node A",
                "explain": "From connected set {A, Hub}, the minimum weight link to an unconnected node is Hub \u2013 A with weight 3.",
                "mstEdges": [
                    "HubA"
                ],
                "connectedNodes": [
                    "Hub",
                    "A"
                ]
            },
            {
                "stepNum": 2,
                "connectedSet": "{A, B, Hub}",
                "addedNode": "B",
                "linkUsed": "A \u2013 B",
                "linkLen": 2,
                "totalLength": 5,
                "title": "Step 2: Connect Node B",
                "explain": "From connected set {A, B, Hub}, the minimum weight link to an unconnected node is A \u2013 B with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB"
                ],
                "connectedNodes": [
                    "Hub",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 3,
                "connectedSet": "{A, B, C, Hub}",
                "addedNode": "C",
                "linkUsed": "A \u2013 C",
                "linkLen": 3,
                "totalLength": 8,
                "title": "Step 3: Connect Node C",
                "explain": "From connected set {A, B, C, Hub}, the minimum weight link to an unconnected node is A \u2013 C with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "A",
                    "B"
                ]
            },
            {
                "stepNum": 4,
                "connectedSet": "{A, B, C, D, Hub}",
                "addedNode": "D",
                "linkUsed": "C \u2013 D",
                "linkLen": 3,
                "totalLength": 11,
                "title": "Step 4: Connect Node D",
                "explain": "From connected set {A, B, C, D, Hub}, the minimum weight link to an unconnected node is C \u2013 D with weight 3.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD"
                ],
                "connectedNodes": [
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 5,
                "connectedSet": "{A, B, C, D, E, Hub}",
                "addedNode": "E",
                "linkUsed": "D \u2013 E",
                "linkLen": 2,
                "totalLength": 13,
                "title": "Step 5: Connect Node E",
                "explain": "From connected set {A, B, C, D, E, Hub}, the minimum weight link to an unconnected node is D \u2013 E with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 6,
                "connectedSet": "{A, B, C, D, E, Hub, T}",
                "addedNode": "T",
                "linkUsed": "E \u2013 T",
                "linkLen": 2,
                "totalLength": 15,
                "title": "Step 6: Connect Node T",
                "explain": "From connected set {A, B, C, D, E, Hub, T}, the minimum weight link to an unconnected node is E \u2013 T with weight 2.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "ET"
                ],
                "connectedNodes": [
                    "E",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            },
            {
                "stepNum": 7,
                "connectedSet": "{A, B, C, D, E, Hub, T, Top}",
                "addedNode": "Top",
                "linkUsed": "D \u2013 Top",
                "linkLen": 4,
                "totalLength": 19,
                "title": "Step 7: Connect Node Top",
                "explain": "From connected set {A, B, C, D, E, Hub, T, Top}, the minimum weight link to an unconnected node is D \u2013 Top with weight 4.",
                "mstEdges": [
                    "HubA",
                    "AB",
                    "AC",
                    "CD",
                    "DE",
                    "ET",
                    "DTop"
                ],
                "connectedNodes": [
                    "E",
                    "Top",
                    "Hub",
                    "C",
                    "T",
                    "B",
                    "D",
                    "A"
                ]
            }
        ],
        "result": "MST Links Used: <strong>Hub-A(3), A-B(2), A-C(3), Top-D(4), C-D(3), D-E(2), E-T(2)</strong><br/><strong>Minimum Total Link Weight = 19 units</strong>"
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# SERIALIZE
# ─────────────────────────────────────────────────────────────────────────────
js_lpp   = "const LPP_PROBLEMS = "         + json.dumps(lpp_problems)  + ";"
js_tp    = "const TRANSPORT_PROBLEMS = "   + json.dumps(tp_problems)   + ";"
js_asgn  = "const ASSIGNMENT_PROBLEMS = "  + json.dumps(asgn_problems) + ";"
js_sp    = "const SHORTEST_PROBLEMS = "    + json.dumps(sp_problems)   + ";"
js_mst   = "const MST_PROBLEMS = "         + json.dumps(mst_problems)  + ";"

modules_def = """
const MODULES = [
  { id:'lpp',      title:'Linear Programming (LPP)',        icon:'📊', color:'#2563eb', desc:'Formulate and solve LPP problems using decision variables, objective functions, constraints, graphical method, and Simplex.',       problems:LPP_PROBLEMS },
  { id:'transport',title:'Transportation Problem',          icon:'🚛', color:'#059669', desc:'Distribute commodities from sources to destinations. Choose NWC, Least-Cost, or Penalty Cost (VAM) method.',                    problems:TRANSPORT_PROBLEMS },
  { id:'assignment',title:'Assignment Problem',             icon:'👤', color:'#7c3aed', desc:'Hungarian Method: row/col reductions, minimum line coverage test, matrix adjustment, and optimal matching.',                      problems:ASSIGNMENT_PROBLEMS },
  { id:'shortest',  title:'Shortest Path Problem',          icon:'🗺️', color:'#dc2626', desc:'Step-by-step Dijkstra shortest path with animated SVG network diagram showing solved nodes and optimal route.',                   problems:SHORTEST_PROBLEMS },
  { id:'mst',       title:'Minimum Spanning Tree (MST)',    icon:'🌳', color:'#0891b2', desc:"Step-by-step Prim's MST algorithm with animated SVG network showing which nodes and edges are added at each step.",              problems:MST_PROBLEMS }
];
"""

# ─────────────────────────────────────────────────────────────────────────────
# VANILLA JS RENDERER (full self-contained)
# ─────────────────────────────────────────────────────────────────────────────
vanilla_renderer = r"""
// ─── SVG NETWORK DIAGRAM RENDERER ───────────────────────────────────────────
function drawNetwork(network, solvedNodes, activeEdges, pathEdges, mstEdges, containerId, isDirected) {
  if (!network) return '<div class="ppt-explain">No network diagram available for this problem.</div>';
  const W = 680, H = 300;
  const nodes = network.nodes;
  const edges = network.edges;

  // Build lookup
  const nodeMap = {};
  nodes.forEach(n => nodeMap[n.id] = n);

  const toX = pct => (pct / 100) * (W - 40) + 20;
  const toY = pct => (pct / 100) * (H - 50) + 25;

  let edgeSvg = '';
  edges.forEach(e => {
    const a = nodeMap[e.from], b = nodeMap[e.to];
    if (!a || !b) return;
    const x1 = toX(a.x), y1 = toY(a.y), x2 = toX(b.x), y2 = toY(b.y);
    const edgeId1 = `${e.from}${e.to}`, edgeId2 = `${e.to}${e.from}`;

    let stroke = '#94a3b8', sWidth = 2, dash = '';
    if (pathEdges && (pathEdges.includes(edgeId1) || pathEdges.includes(edgeId2))) {
      stroke = '#16a34a'; sWidth = 4;
    } else if (mstEdges && (mstEdges.includes(edgeId1) || mstEdges.includes(edgeId2))) {
      stroke = '#0891b2'; sWidth = 4;
    } else if (activeEdges && (activeEdges.includes(edgeId1) || activeEdges.includes(edgeId2))) {
      stroke = '#f59e0b'; sWidth = 3;
    }

    const mx = (x1+x2)/2, my = (y1+y2)/2;
    edgeSvg += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" stroke-width="${sWidth}" stroke-dasharray="${dash}"/>`;
    edgeSvg += `<rect x="${mx-10}" y="${my-9}" width="20" height="14" rx="3" fill="white" opacity="0.88"/>`;
    edgeSvg += `<text x="${mx}" y="${my+2}" text-anchor="middle" font-size="10" font-weight="700" fill="#374151">${e.w}</text>`;
  });

  let nodeSvg = '';
  nodes.forEach(n => {
    const cx = toX(n.x), cy = toY(n.y);
    let fill = '#e2e8f0', stroke = '#94a3b8', textFill = '#1b365d', r = 18;
    const isSolved = solvedNodes && solvedNodes.includes(n.id);
    const isActive = activeEdges && activeEdges.some(e => e.startsWith(n.id) || e.endsWith(n.id));
    if (isSolved) { fill = '#16a34a'; stroke = '#15803d'; textFill = '#fff'; }
    else if (isActive) { fill = '#fef3c7'; stroke = '#f59e0b'; textFill = '#92400e'; }
    nodeSvg += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="2.5"/>`;
    nodeSvg += `<text x="${cx}" y="${cy+5}" text-anchor="middle" font-size="12" font-weight="800" fill="${textFill}">${n.label}</text>`;
  });

  return `
    <div class="svg-net-wrap">
      <svg viewBox="0 0 ${W} ${H}" width="100%" style="max-width:${W}px;display:block;margin:0 auto;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
        <defs>
          <marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="3.5" orient="auto">
            <polygon points="0 0, 8 3.5, 0 7" fill="#94a3b8"/>
          </marker>
        </defs>
        ${edgeSvg}
        ${nodeSvg}
      </svg>
      <div class="svg-legend">
        <span class="leg-item"><span class="leg-dot" style="background:#e2e8f0;border:2px solid #94a3b8;"></span> Unvisited</span>
        <span class="leg-item"><span class="leg-dot" style="background:#16a34a;"></span> Solved / Connected</span>
        <span class="leg-item"><span class="leg-dot" style="background:#fef3c7;border:2px solid #f59e0b;"></span> Active Frontier</span>
        <span class="leg-item"><span class="leg-line" style="background:#16a34a;"></span> Optimal Path / MST Edge</span>
        <span class="leg-item"><span class="leg-line" style="background:#f59e0b;"></span> Active Edge</span>
      </div>
    </div>
  `;
}

// ─── STATE ──────────────────────────────────────────────────────────────────
const state = {
  currentTab: 'home', selectedModule: null, selectedProblem: null,
  difficultyFilter: 'all', tpMethodIndex: 0, tpStepIndex: 0,
  asgnStepIndex: 0, spStepIndex: 0, mstStepIndex: 0, hiddenInfoMap: {}
};

function renderApp() {
  const root = document.getElementById('root');
  if (!root) return;
  const tabs = [{ id:'home', label:'🏠 Home' }, ...MODULES.map(m => ({ id:m.id, label:`${m.icon} ${m.title.split('(')[0].trim()}` }))];
  let mainHtml = '';
  if (state.currentTab === 'home') mainHtml = renderHome();
  else {
    const mod = state.selectedModule || MODULES.find(m => m.id === state.currentTab);
    if (!mod) mainHtml = '<div>Module not found</div>';
    else if (state.selectedProblem) mainHtml = renderProblemDetail(state.selectedProblem, mod);
    else mainHtml = renderProblemList(mod);
  }
  root.innerHTML = `
    <div id="app-header">
      <div style="max-width:1320px;margin:0 auto;padding:18px 24px 12px;display:flex;align-items:center;gap:14px;">
        <div style="font-size:2.2rem;">📐</div>
        <div>
          <h1 style="font-size:1.45rem;font-weight:700;">Optimization & Decision Modeling Hub</h1>
          <p style="font-size:.83rem;opacity:.88;margin-top:2px;">Interactive Operations Research & Business Analytics Platform</p>
        </div>
      </div>
      <div class="nav-strip"><div class="nav-strip-inner">
        ${tabs.map(t => `<button class="ntab ${state.currentTab===t.id?'active':''}" onclick="gotoTab('${t.id}')">${t.label}</button>`).join('')}
      </div></div>
    </div>
    <main class="main">${mainHtml}</main>`;
}

function gotoTab(id) {
  state.currentTab = id; state.selectedProblem = null; state.tpStepIndex = 0;
  state.asgnStepIndex = 0; state.spStepIndex = 0; state.mstStepIndex = 0;
  state.selectedModule = id === 'home' ? null : MODULES.find(m => m.id === id) || null;
  renderApp();
}
function selectModule(id) { gotoTab(id); }
function selectProblem(probId) {
  const mod = state.selectedModule || MODULES.find(m => m.id === state.currentTab);
  if (!mod) return;
  const prob = mod.problems.find(p => p.id === probId);
  if (!prob) return;
  state.selectedProblem = prob; state.tpStepIndex = 0;
  state.asgnStepIndex = 0; state.spStepIndex = 0; state.mstStepIndex = 0;
  renderApp();
}
function backToList() { state.selectedProblem = null; renderApp(); }
function filterDifficulty(d) { state.difficultyFilter = d; renderApp(); }
function setTpMethod(i) { state.tpMethodIndex = i; state.tpStepIndex = 0; renderApp(); }
function navTpStep(d)   { state.tpStepIndex   += d; renderApp(); }
function navAsgnStep(d) { state.asgnStepIndex += d; renderApp(); }
function navSpStep(d)   { state.spStepIndex   += d; renderApp(); }
function navMstStep(d)  { state.mstStepIndex  += d; renderApp(); }
function toggleInfo(id) {
  state.hiddenInfoMap[id] = !state.hiddenInfoMap[id];
  const el = document.getElementById(id);
  if (el) el.style.display = state.hiddenInfoMap[id] ? 'none' : 'block';
}

// HOME
function renderHome() {
  return `
    <h2 style="font-size:1.15rem;font-weight:700;color:#1b365d;margin-bottom:4px;">Select a Topic to Explore</h2>
    <p style="font-size:.86rem;color:#64748b;margin-bottom:20px;">15 interactive step-by-step problems per module · 5 modules · 75 problems total</p>
    <div class="mod-grid">
      ${MODULES.map(m => `
        <div class="mod-card" style="--c:${m.color};" onclick="selectModule('${m.id}')">
          <div style="font-size:1.8rem;">${m.icon}</div>
          <h3>${m.title}</h3>
          <p>${m.desc}</p>
          <span class="mod-badge">${m.problems.length} Problems</span>
        </div>`).join('')}
    </div>`;
}

// PROBLEM LIST
function renderProblemList(mod) {
  const filtered = state.difficultyFilter === 'all' ? mod.problems : mod.problems.filter(p => p.difficulty === state.difficultyFilter);
  return `
    <button class="back-btn" onclick="gotoTab('home')">← Back to Modules</button>
    <div class="sec-title">${mod.icon} ${mod.title}</div>
    <p class="sec-desc">${mod.desc}</p>
    <div style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap;align-items:center;">
      ${['all','easy','medium','hard'].map(d => `
        <button onclick="filterDifficulty('${d}')" style="padding:5px 14px;border-radius:4px;border:1px solid;cursor:pointer;font-size:.8rem;font-weight:600;background:${state.difficultyFilter===d?mod.color:'#fff'};color:${state.difficultyFilter===d?'#fff':'#374151'};border-color:${state.difficultyFilter===d?mod.color:'#d1d5db'};">
          ${d.charAt(0).toUpperCase()+d.slice(1)}
        </button>`).join('')}
      <span style="margin-left:auto;font-size:.82rem;color:#64748b;">${filtered.length} problems</span>
    </div>
    <div class="prob-list">
      ${filtered.map(p => `
        <div class="prob-item" onclick="selectProblem('${p.id}')">
          <div>
            <h4>${p.title}</h4>
            <p>${p.context.slice(0,100)}…</p>
          </div>
          <div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
            <span class="diff ${p.difficulty==='easy'?'d-easy':p.difficulty==='hard'?'d-hard':'d-med'}">${p.difficulty}</span>
            <span style="color:#94a3b8;font-size:1.1rem;">›</span>
          </div>
        </div>`).join('')}
    </div>`;
}

// PROBLEM DETAIL WRAPPER
function renderProblemDetail(problem, mod) {
  let content = '';
  if      (problem.type === 'transport')    content = renderTransport(problem);
  else if (problem.type === 'assignment')   content = renderAssignment(problem);
  else if (problem.type === 'shortest_ppt') content = renderShortest(problem);
  else if (problem.type === 'mst_ppt')      content = renderMst(problem);
  else                                       content = renderGeneral(problem);
  return `
    <button class="back-btn" onclick="backToList()">← Back to Problems</button>
    <div>
      <div class="prob-header" style="--c:${mod.color};">
        <h2>${problem.title}</h2>
        <p>${problem.context}</p>
      </div>
      <div class="prob-body">
        <div class="pill-row">
          ${(problem.tags||[]).map(t => `<span class="tag">${t}</span>`).join('')}
          <span class="diff ${problem.difficulty==='easy'?'d-easy':problem.difficulty==='hard'?'d-hard':'d-med'}">${problem.difficulty}</span>
        </div>
        <div class="sep"></div>
        ${content}
      </div>
    </div>`;
}

// LPP / GENERAL
function renderGeneral(p) {
  return (p.steps||[]).map((s,i) => {
    const id = `info-g-${i}`;
    const hidden = state.hiddenInfoMap[id];
    return `
      <div class="step-card">
        <div class="step-hd"><h3><span class="snum">${i+1}</span>${s.title}<button class="info-btn" onclick="toggleInfo('${id}')">i</button></h3></div>
        <div class="step-bd">
          ${s.explain?`<div id="${id}" class="ppt-explain" style="display:${hidden?'none':'block'};"><strong>ℹ️</strong> ${s.explain}</div>`:''}
          ${s.formulation?`<div class="ppt-formulation">${s.formulation}</div>`:''}
          ${s.body?`<div>${s.body}</div>`:''}
        </div>
      </div>`;
  }).join('');
}

// TRANSPORT
function renderTransport(p) {
  const method = p.methods[state.tpMethodIndex];
  const steps  = method.steps;
  const step   = steps[state.tpStepIndex];
  const id     = `info-tp-${state.tpMethodIndex}-${state.tpStepIndex}`;
  const hidden = state.hiddenInfoMap[id];
  const isActive = (r,c) => step.activeCell && step.activeCell[0]===r && step.activeCell[1]===c;
  const isDone   = (r,c) => (step.doneCells||[]).some(([dr,dc])=>dr===r&&dc===c);
  const m=p.rows.length, n=p.cols.length;
  return `
    <div style="margin-bottom:14px;">
      <label style="font-size:.84rem;font-weight:700;color:#1b365d;display:block;margin-bottom:6px;">Select Solution Method:</label>
      <div class="pill-row">
        ${p.methods.map((m2,i) => `
          <button onclick="setTpMethod(${i})" style="padding:7px 18px;border-radius:5px;border:1px solid;cursor:pointer;font-size:.83rem;font-weight:700;background:${state.tpMethodIndex===i?'#059669':'#fff'};color:${state.tpMethodIndex===i?'#fff':'#374151'};border-color:${state.tpMethodIndex===i?'#059669':'#d1d5db'};">
            ${m2.name}
          </button>`).join('')}
      </div>
    </div>
    <div class="ppt-explain">${method.intro}</div>
    <div class="table-wrap">
      <table class="tp-table">
        <thead><tr>
          <th>Source \\ Destination</th>
          ${p.cols.map(c => `<th>${c}</th>`).join('')}
          <th style="background:#334155;">Supply</th>
        </tr></thead>
        <tbody>
          ${p.rows.map((r,ri) => `
            <tr>
              <td class="src-lbl">${r}</td>
              ${p.cols.map((_,ci) => {
                const act=isActive(ri,ci), done=isDone(ri,ci);
                const cls=act?'cell-active':done?'cell-done':'';
                const alloc=step.allocs[ri][ci];
                return `<td class="tp-cell ${cls}"><span class="cost-box">${step.costs[ri][ci]}</span>${alloc>0?`<span class="alloc-box">${alloc}`:''}</span></td>`;
              }).join('')}
              <td class="supply-val">${step.supply[ri]}</td>
            </tr>`).join('')}
          <tr>
            <td class="dem-lbl">Demand</td>
            ${p.cols.map((_,ci) => `<td class="demand-val">${step.demand[ci]}</td>`).join('')}
            <td style="background:#f8fafc;"></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="step-card" style="margin-top:14px;">
      <div class="step-hd"><h3><span class="snum">${state.tpStepIndex+1}</span>${step.title}<button class="info-btn" onclick="toggleInfo('${id}')">i</button></h3></div>
      <div id="${id}" class="ppt-explain" style="display:${hidden?'none':'block'};"><strong>ℹ️</strong> ${step.explain}</div>
    </div>
    <div class="step-nav">
      <button class="snav-btn" onclick="navTpStep(-1)" ${state.tpStepIndex===0?'disabled':''}>◀ Prev</button>
      <span class="snav-count">Step ${state.tpStepIndex+1} of ${steps.length}</span>
      <button class="snav-btn" onclick="navTpStep(1)" ${state.tpStepIndex===steps.length-1?'disabled':''}>Next ▶</button>
    </div>
    ${state.tpStepIndex===steps.length-1 && step.result ? (() => {
      let basicCount=0;
      for(let ri=0;ri<m;ri++) for(let ci=0;ci<n;ci++) if(step.allocs[ri][ci]>0) basicCount++;
      const req=m+n-1, nd=basicCount===req;
      return `<div class="res-box">
        <h4>✅ ${method.name} – Final Solution</h4>
        <div style="font-size:.9rem;font-weight:700;color:#166534;margin-bottom:10px;">${step.result}</div>
        <div style="border-top:1px solid #bbf7d0;padding-top:10px;">
          <h5 style="font-size:.86rem;font-weight:700;color:#166534;margin-bottom:6px;">📋 4 Feasibility Conditions:</h5>
          <ul style="font-size:.83rem;color:#166534;line-height:1.8;padding-left:18px;">
            <li>1. <strong>Supply Satisfied (Σx_ij = a_i):</strong> All source supplies fully allocated. ✅</li>
            <li>2. <strong>Demand Satisfied (Σx_ij = b_j):</strong> All destination demands fully met. ✅</li>
            <li>3. <strong>Non-Negativity (x_ij ≥ 0):</strong> All allocations are non-negative. ✅</li>
            <li>4. <strong>Rim Condition (m+n−1):</strong> Basic cells = <strong>${basicCount}</strong>, Required = ${m}+${n}−1 = <strong>${req}</strong>. ${nd?'✅ Non-Degenerate BFS':'⚠️ Degenerate — introduce ε into an independent cell'}</li>
          </ul>
        </div>
      </div>`;
    })() : ''}`;
}

// ASSIGNMENT
function renderAssignment(p) {
  const steps=p.steps, step=steps[state.asgnStepIndex];
  const id=`info-asgn-${state.asgnStepIndex}`, hidden=state.hiddenInfoMap[id];
  return `
    <div class="step-card">
      <div class="step-hd"><h3><span class="snum">${state.asgnStepIndex+1}</span>${step.title}<button class="info-btn" onclick="toggleInfo('${id}')">i</button></h3></div>
      <div id="${id}" class="ppt-explain" style="display:${hidden?'none':'block'};"><strong>ℹ️</strong> ${step.explain}</div>
    </div>
    <div class="table-wrap">
      <table class="asgn-table">
        <thead><tr>
          <th>Resource \\ Task</th>
          ${p.colLabels.map(c=>`<th>${c}</th>`).join('')}
          ${step.showRowMin?'<th style="background:#475569;">Row Min</th>':''}
        </tr></thead>
        <tbody>
          ${step.matrix.map((row,ri) => `
            <tr>
              <td class="row-lbl">${p.rowLabels[ri]}</td>
              ${row.map((val,ci) => {
                const zero=val===0, asgnd=step.assignment&&step.assignment.some(([r,c])=>r===ri&&c===ci);
                const lr=step.lineRows&&step.lineRows.includes(ri), lc=step.lineCols&&step.lineCols.includes(ci);
                const intr=lr&&lc;
                let cls=asgnd?'az-assigned':zero?'az-zero':'';
                if(intr) cls+=' az-intersection'; else if(lr) cls+=' line-row'; else if(lc) cls+=' line-col';
                return `<td class="${cls}">${val===999?'M':val}</td>`;
              }).join('')}
              ${step.showRowMin?`<td style="background:#fef9c3;font-weight:700;color:#92400e;">${step.rowMins[ri]}</td>`:''}
            </tr>`).join('')}
        </tbody>
      </table>
    </div>
    <div class="step-nav">
      <button class="snav-btn" onclick="navAsgnStep(-1)" ${state.asgnStepIndex===0?'disabled':''}>◀ Prev</button>
      <span class="snav-count">Step ${state.asgnStepIndex+1} of ${steps.length}</span>
      <button class="snav-btn" onclick="navAsgnStep(1)" ${state.asgnStepIndex===steps.length-1?'disabled':''}>Next ▶</button>
    </div>
    ${state.asgnStepIndex===steps.length-1&&step.result?`<div class="res-box"><h4>✅ Optimal Assignment</h4>${step.result}</div>`:''}`;
}

// SHORTEST PATH — with live SVG diagram
function renderShortest(p) {
  const steps=p.steps, step=steps[state.spStepIndex];
  const id=`info-sp-${state.spStepIndex}`, hidden=state.hiddenInfoMap[id];
  const netDiag = drawNetwork(
    p.network,
    step.solvedSet || [],
    step.activeEdges || [],
    step.pathEdges || [],
    null, 'spNet', false
  );
  return `
    <div style="margin-bottom:10px;">
      <h4 style="font-size:.9rem;font-weight:700;color:#1b365d;margin-bottom:6px;">🗺️ Network Diagram</h4>
      ${netDiag}
    </div>
    <div class="step-card">
      <div class="step-hd">
        <h3><span class="snum">${state.spStepIndex+1}</span>Iteration ${step.n}: Add Node <strong>${step.nthNode}</strong><button class="info-btn" onclick="toggleInfo('${id}')">i</button></h3>
      </div>
      <div id="${id}" class="ppt-explain" style="display:${hidden?'none':'block'};">
        <strong>ℹ️ Step Logic:</strong> From solved nodes [${step.solvedNodes}], the closest unconnected node is <strong>${step.nthNode}</strong> 
        via link <strong>${step.lastConn}</strong> with cumulative distance = <strong>${step.minDist}</strong>.
      </div>
    </div>
    <div class="table-wrap">
      <table class="sp-ppt-table">
        <thead><tr>
          <th>n</th><th>Solved Nodes</th><th>Closest Unsolved</th><th>Total Distance</th>
          <th>nth Nearest Node</th><th>Min Distance</th><th>Last Connection</th>
        </tr></thead>
        <tbody>
          ${steps.slice(0, state.spStepIndex+1).map((s,i) => `
            <tr class="${i===state.spStepIndex?'active-row':''}">
              <td><strong>${s.n}</strong></td><td>${s.solvedNodes}</td>
              <td>${s.closestUnsolved}</td><td>${s.totalDist}</td>
              <td><strong style="color:#1d4ed8;">${s.nthNode}</strong></td>
              <td><strong style="color:#166534;">${s.minDist}</strong></td>
              <td><strong>${s.lastConn}</strong></td>
            </tr>`).join('')}
        </tbody>
      </table>
    </div>
    <div class="step-nav">
      <button class="snav-btn" onclick="navSpStep(-1)" ${state.spStepIndex===0?'disabled':''}>◀ Prev Step</button>
      <span class="snav-count">Step ${state.spStepIndex+1} of ${steps.length}</span>
      <button class="snav-btn" onclick="navSpStep(1)" ${state.spStepIndex===steps.length-1?'disabled':''}>Next Step ▶</button>
    </div>
    ${state.spStepIndex===steps.length-1?`
      <div class="ppt-explain" style="margin-top:10px;"><strong>🔁 Traceback:</strong> ${p.traceback}</div>
      <div class="res-box"><h4>✅ Optimal Shortest Path</h4>${p.result}</div>`:''}`;
}

// MST — with live SVG diagram
function renderMst(p) {
  const steps=p.steps, step=steps[state.mstStepIndex];
  const id=`info-mst-${state.mstStepIndex}`, hidden=state.hiddenInfoMap[id];
  const netDiag = drawNetwork(
    p.network,
    step.connectedNodes || [],
    null,
    null,
    step.mstEdges || [], 'mstNet', false
  );
  return `
    <div style="margin-bottom:10px;">
      <h4 style="font-size:.9rem;font-weight:700;color:#1b365d;margin-bottom:6px;">🌳 Network Diagram</h4>
      ${netDiag}
    </div>
    <div class="step-card">
      <div class="step-hd">
        <h3><span class="snum">${state.mstStepIndex+1}</span>${step.title}<button class="info-btn" onclick="toggleInfo('${id}')">i</button></h3>
      </div>
      <div id="${id}" class="ppt-explain" style="display:${hidden?'none':'block'};">
        <strong>ℹ️ Step Logic:</strong> ${step.explain}
      </div>
    </div>
    <div class="table-wrap">
      <table class="ppt-table">
        <thead><tr><th>Step</th><th>Connected Set</th><th>Node Added</th><th>Link Used</th><th>Link Length</th><th>Total Length</th></tr></thead>
        <tbody>
          ${steps.slice(0, state.mstStepIndex+1).map((s,i) => `
            <tr class="${i===state.mstStepIndex?'hl':''}">
              <td>${s.stepNum}</td>
              <td>${s.connectedSet}</td>
              <td><strong style="color:#1d4ed8;">${s.addedNode}</strong></td>
              <td><strong>${s.linkUsed}</strong></td>
              <td>${s.linkLen}</td>
              <td><strong style="color:#166534;">${s.totalLength}</strong></td>
            </tr>`).join('')}
        </tbody>
      </table>
    </div>
    <div class="step-nav">
      <button class="snav-btn" onclick="navMstStep(-1)" ${state.mstStepIndex===0?'disabled':''}>◀ Prev Step</button>
      <span class="snav-count">Step ${state.mstStepIndex+1} of ${steps.length}</span>
      <button class="snav-btn" onclick="navMstStep(1)" ${state.mstStepIndex===steps.length-1?'disabled':''}>Next Step ▶</button>
    </div>
    ${state.mstStepIndex===steps.length-1?`<div class="res-box"><h4>✅ Minimum Spanning Tree Complete</h4>${p.result}</div>`:''}`;
}

document.addEventListener('DOMContentLoaded', renderApp);
"""

# ─────────────────────────────────────────────────────────────────────────────
# BUILD HTML
# ─────────────────────────────────────────────────────────────────────────────
css = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',system-ui,sans-serif;background:#f4f6f9;color:#1a202c;min-height:100vh;line-height:1.6}
#app-header{background:linear-gradient(135deg,#1b365d 0%,#2563eb 60%,#0f2b5c 100%);color:#fff;position:sticky;top:0;z-index:100;box-shadow:0 3px 14px rgba(0,0,0,.2)}
.nav-strip{background:rgba(0,0,0,.25);overflow-x:auto;white-space:nowrap}
.nav-strip-inner{max-width:1320px;margin:0 auto;display:flex}
.ntab{padding:11px 20px;font-size:.84rem;font-weight:600;color:rgba(255,255,255,.75);border:none;background:transparent;cursor:pointer;border-bottom:3px solid transparent;transition:all .18s;flex-shrink:0}
.ntab:hover{color:#fff;background:rgba(255,255,255,.08)}
.ntab.active{color:#fff;border-bottom-color:#60a5fa;background:rgba(255,255,255,.12)}
.main{max-width:1320px;margin:0 auto;padding:26px 20px}
.mod-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-top:10px}
.mod-card{background:#fff;border:1px solid #e2e8f0;border-radius:6px;padding:22px 20px 18px;cursor:pointer;transition:transform .18s,box-shadow .18s;position:relative;overflow:hidden}
.mod-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--c,#2563eb)}
.mod-card:hover{transform:translateY(-3px);box-shadow:0 10px 25px rgba(37,99,235,.15)}
.mod-card h3{font-size:1.05rem;font-weight:700;margin:10px 0 6px;color:#1b365d}
.mod-card p{font-size:.83rem;color:#64748b;margin-bottom:12px}
.mod-badge{display:inline-block;background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe;border-radius:4px;font-size:.72rem;font-weight:700;padding:3px 9px}
.back-btn{display:inline-flex;align-items:center;gap:6px;background:#fff;border:1px solid #d1d5db;border-radius:5px;padding:7px 15px;font-size:.84rem;font-weight:600;color:#374151;cursor:pointer;margin-bottom:18px}
.back-btn:hover{background:#f3f4f6}
.sec-title{font-size:1.35rem;font-weight:700;color:#1b365d;margin-bottom:4px}
.sec-desc{font-size:.86rem;color:#64748b;margin-bottom:20px}
.prob-list{display:flex;flex-direction:column;gap:10px}
.prob-item{background:#fff;border:1px solid #e2e8f0;border-radius:6px;padding:15px 18px;cursor:pointer;display:flex;align-items:center;justify-content:space-between;transition:all .15s}
.prob-item:hover{border-color:#93c5fd;background:#f0f7ff;transform:translateX(2px)}
.prob-item h4{font-size:.92rem;font-weight:600;color:#1b365d}
.prob-item p{font-size:.8rem;color:#64748b;margin-top:3px}
.diff{font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:4px}
.d-easy{background:#dcfce7;color:#166534}
.d-med{background:#fef3c7;color:#92400e}
.d-hard{background:#fee2e2;color:#991b1b}
.prob-header{background:linear-gradient(135deg,#1b365d,var(--c,#2563eb));color:#fff;padding:24px 26px;border-radius:6px 6px 0 0}
.prob-header h2{font-size:1.25rem;font-weight:700}
.prob-header p{font-size:.86rem;opacity:.9;margin-top:6px}
.prob-body{background:#fff;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 6px 6px;padding:24px}
.step-card{border:1px solid #e2e8f0;border-radius:6px;margin-bottom:14px;overflow:hidden}
.step-hd{background:#f8fafc;padding:12px 18px;display:flex;align-items:center;font-weight:700;color:#1b365d}
.step-hd h3{display:flex;align-items:center;gap:6px;flex:1}
.snum{background:#2563eb;color:#fff;border-radius:50%;width:24px;height:24px;display:inline-flex;align-items:center;justify-content:center;font-size:.73rem;font-weight:800;flex-shrink:0}
.step-bd{padding:18px}
.info-btn{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:50%;background:#2563eb;color:#fff;font-size:.78rem;font-weight:800;border:none;cursor:pointer;margin-left:6px;flex-shrink:0;transition:transform .15s}
.info-btn:hover{transform:scale(1.15);background:#1d4ed8}
.ppt-formulation{background:#f8fafc;border:1px solid #cbd5e1;border-left:4px solid #2563eb;border-radius:4px;padding:16px;margin:12px 0;font-family:'Consolas','Courier New',monospace;font-size:.85rem;line-height:1.8;color:#1e293b;white-space:pre-wrap}
.ppt-explain{background:#fffbeb;border:1px solid #fcd34d;border-radius:5px;padding:12px 16px;margin:12px 0;font-size:.85rem;color:#78350f;line-height:1.6}
.ppt-explain strong{color:#92400e}
.table-wrap{overflow-x:auto;margin:12px 0}
table.ppt-table{border-collapse:collapse;width:100%;font-size:.83rem}
table.ppt-table th,table.ppt-table td{border:1px solid #cbd5e1;padding:8px 12px;text-align:center}
table.ppt-table th{background:#1b365d;color:#fff;font-weight:700}
table.ppt-table tr:nth-child(even) td{background:#f8fafc}
table.ppt-table .opt{background:#dcfce7;font-weight:700;color:#166534}
table.ppt-table tr.hl td{background:#dbeafe}
.tp-table{border-collapse:collapse;width:100%;font-size:.83rem;min-width:480px}
.tp-table th,.tp-table td{border:2px solid #94a3b8;padding:0;text-align:center;min-width:80px;position:relative}
.tp-table th{background:#1b365d;color:#fff;font-weight:700;padding:9px 10px}
.tp-table .src-lbl{background:#334155;color:#fff;font-weight:700;padding:9px 12px}
.tp-table .dem-lbl{background:#475569;color:#fff;font-weight:700;padding:8px 12px}
.tp-cell{position:relative;height:62px;min-width:80px;background:#fff}
.cost-box{position:absolute;top:2px;right:3px;font-size:.7rem;color:#475569;font-weight:700;border:1px solid #cbd5e1;padding:1px 4px;background:#f8fafc;border-radius:2px}
.alloc-box{position:absolute;bottom:5px;left:0;right:0;text-align:center;font-size:1.05rem;font-weight:800;color:#1b365d}
.cell-active{background:#fef9c3 !important;border:3px solid #f59e0b !important}
.cell-done{background:#dbeafe !important}
.supply-val,.demand-val{background:#f0fdf4;color:#166534;font-weight:700;padding:9px;border:2px solid #94a3b8}
.asgn-table{border-collapse:collapse;font-size:.86rem;margin:12px 0;min-width:380px;width:100%}
.asgn-table th,.asgn-table td{border:2px solid #94a3b8;padding:10px 14px;text-align:center;min-width:60px;font-weight:600;position:relative}
.asgn-table th{background:#1b365d;color:#fff}
.asgn-table .row-lbl{background:#334155;color:#fff;font-weight:700}
.az-zero{color:#2563eb;font-weight:800;background:#eff6ff}
.az-assigned{color:#fff;background:#16a34a !important;font-weight:800}
.line-row{background:#fee2e2 !important;border-top:3px solid #dc2626 !important;border-bottom:3px solid #dc2626 !important}
.line-col{background:#fee2e2 !important;border-left:3px solid #dc2626 !important;border-right:3px solid #dc2626 !important}
.az-intersection{background:#fca5a5 !important;border:3px solid #dc2626 !important;font-weight:800}
table.sp-ppt-table{border-collapse:collapse;width:100%;font-size:.82rem;margin:12px 0}
table.sp-ppt-table th{background:#1b365d;color:#fff;padding:8px 10px;text-align:center}
table.sp-ppt-table td{border:1px solid #cbd5e1;padding:8px 10px;text-align:center}
table.sp-ppt-table tr:nth-child(even){background:#f8fafc}
table.sp-ppt-table tr.active-row{background:#fef9c3;font-weight:700}
.step-nav{display:flex;align-items:center;gap:12px;margin:16px 0;flex-wrap:wrap}
.snav-btn{padding:8px 18px;border-radius:5px;border:1px solid #d1d5db;background:#fff;font-size:.84rem;font-weight:600;cursor:pointer;color:#374151;transition:all .15s}
.snav-btn:hover:not(:disabled){background:#f0f7ff;border-color:#93c5fd;color:#1d4ed8}
.snav-btn:disabled{opacity:.4;cursor:not-allowed}
.snav-count{font-size:.85rem;color:#64748b;font-weight:600}
.res-box{background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:14px 18px;margin-top:14px}
.res-box h4{font-size:.9rem;font-weight:700;color:#166534;margin-bottom:6px}
.res-box ul{font-size:.84rem;color:#166534;padding-left:18px}
.res-box li{margin-bottom:4px}
.pill-row{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.sep{height:1px;background:#e2e8f0;margin:16px 0}
.tag{display:inline-block;padding:3px 8px;border-radius:4px;font-size:.72rem;font-weight:700;background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe}
/* SVG Network styles */
.svg-net-wrap{margin:10px 0 16px;}
.svg-legend{display:flex;flex-wrap:wrap;gap:12px;margin-top:8px;font-size:.75rem;color:#475569;align-items:center}
.leg-item{display:flex;align-items:center;gap:5px;font-weight:600}
.leg-dot{display:inline-block;width:14px;height:14px;border-radius:50%;border:1px solid #94a3b8}
.leg-line{display:inline-block;width:24px;height:4px;border-radius:2px}
"""

final_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Optimization & Decision Modeling Hub</title>
<style>{css}</style>
</head>
<body>
<div id="root"></div>
<script>
{js_lpp}
{js_tp}
{js_asgn}
{js_sp}
{js_mst}
{modules_def}
{vanilla_renderer}
</script>
</body>
</html>"""

with open("app.html","w",encoding="utf-8") as f:
    f.write(final_html)

with open("index.html","w",encoding="utf-8") as f:
    f.write(final_html)

print("DONE - Both index.html and app.html generated successfully!")
