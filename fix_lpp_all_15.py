import json

print("Writing clean 15 LPP problems with embedded graph metadata...")

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
            {"title": "Optimal Production Plan", "explain": "Intersection of binding constraints M1 and M2 yields optimal point B.", "body": "<div class=\"res-box\"><h4>\u2705 Optimal Production Plan</h4><ul><li>Exterior Paint (x\u2081) = <strong>3.33 tons/day</strong></li><li>Interior Paint (x\u2082) = <strong>1.33 tons/day</strong></li><li><strong>Maximum Daily Profit Z = $21,980</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 5, "c2": 4, "maxX1": 6, "maxX2": 4,
            "constraints": [
                {"a1": 6, "a2": 4, "b": 24, "dir": "<=", "label": "6x₁ + 4x₂ ≤ 24 (M1)", "color": "#ef4444"},
                {"a1": 1, "a2": 2, "b": 6,  "dir": "<=", "label": "x₁ + 2x₂ ≤ 6 (M2)",   "color": "#3b82f6"},
                {"a1": -1, "a2": 1, "b": 1, "dir": "<=", "label": "-x₁ + x₂ ≤ 1 (Market)","color": "#8b5cf6"},
                {"a1": 0, "a2": 1, "b": 2,  "dir": "<=", "label": "x₂ ≤ 2 (Demand)",      "color": "#f59e0b"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 4, "x2": 0, "z": 20, "isOpt": False},
                {"label": "B", "x1": 3.33, "x2": 1.33, "z": 21.98, "isOpt": True},
                {"label": "C", "x1": 3, "x2": 1.5, "z": 21, "isOpt": False},
                {"label": "D", "x1": 1, "x2": 2, "z": 13, "isOpt": False},
                {"label": "E", "x1": 0, "x2": 1, "z": 4, "isOpt": False}
            ]
        }
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
        ],
        "graph": {
            "type": "max", "c1": 3, "c2": 5, "maxX1": 6, "maxX2": 8,
            "constraints": [
                {"a1": 1, "a2": 0, "b": 4,  "dir": "<=", "label": "x₁ ≤ 4 (Plant 1)", "color": "#ef4444"},
                {"a1": 0, "a2": 2, "b": 12, "dir": "<=", "label": "2x₂ ≤ 12 (Plant 2)", "color": "#3b82f6"},
                {"a1": 3, "a2": 2, "b": 18, "dir": "<=", "label": "3x₁ + 2x₂ ≤ 18 (Plant 3)", "color": "#10b981"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 4, "x2": 0, "z": 12, "isOpt": False},
                {"label": "B", "x1": 4, "x2": 3, "z": 27, "isOpt": False},
                {"label": "C", "x1": 2, "x2": 6, "z": 36, "isOpt": True},
                {"label": "D", "x1": 0, "x2": 6, "z": 30, "isOpt": False}
            ]
        }
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
    },
    {
        "id": "lpp_4", "title": "4. Furniture Production (Carpentry & Painting)",
        "difficulty": "medium", "tags": ["lpp", "product-mix"],
        "context": "A furniture maker produces tables (profit $6) and chairs (profit $8). Carpentry available = 48 hrs, Painting available = 20 hrs.",
        "steps": [
            {"title": "Decision Variables", "explain": "Tables (x1) and Chairs (x2) produced.", "formulation": "Let x\u2081 = number of tables produced\nLet x\u2082 = number of chairs produced"},
            {"title": "Objective Function & Constraints", "explain": "Maximize total profit.", "formulation": "Maximize Z = 6x\u2081 + 8x\u2082\nSubject to:\n  3x\u2081 + 2x\u2082 \u2264 48 (Carpentry)\n   x\u2081 + 2x\u2082 \u2264 20 (Painting)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Tables (x\u2081) = <strong>14</strong></li><li>Chairs (x\u2082) = <strong>3</strong></li><li><strong>Maximum Profit = $108</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 6, "c2": 8, "maxX1": 20, "maxX2": 15,
            "constraints": [
                {"a1": 3, "a2": 2, "b": 48, "dir": "<=", "label": "3x₁ + 2x₂ ≤ 48 (Carpentry)", "color": "#ef4444"},
                {"a1": 1, "a2": 2, "b": 20, "dir": "<=", "label": "x₁ + 2x₂ ≤ 20 (Painting)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 16, "x2": 0, "z": 96, "isOpt": False},
                {"label": "B", "x1": 14, "x2": 3, "z": 108, "isOpt": True},
                {"label": "C", "x1": 0, "x2": 10, "z": 80, "isOpt": False}
            ]
        }
    },
    {
        "id": "lpp_5", "title": "5. Farm Feed Diet Cost Minimization",
        "difficulty": "medium", "tags": ["lpp", "diet-problem"],
        "context": "Mix grain (cost $2/bag) and soybean (cost $3/bag) to meet minimum protein (90 units) and fat (30 units) requirements.",
        "steps": [
            {"title": "Decision Variables", "explain": "Grain (x1) and Soybean (x2) bags.", "formulation": "Let x\u2081 = bags of grain\nLet x\u2082 = bags of soybean"},
            {"title": "Objective Function & Constraints", "explain": "Minimize feed cost.", "formulation": "Minimize Z = 2x\u2081 + 3x\u2082\nSubject to:\n  3x\u2081 + 5x\u2082 \u2265 90 (Protein requirement)\n   x\u2081 +  x\u2082 \u2265 30 (Fat requirement)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation for minimization.", "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Grain (x\u2081) = <strong>30 bags</strong></li><li>Soybean (x\u2082) = <strong>0 bags</strong></li><li><strong>Minimum Feed Cost = $60</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "min", "c1": 2, "c2": 3, "maxX1": 40, "maxX2": 35,
            "constraints": [
                {"a1": 3, "a2": 5, "b": 90, "dir": ">=", "label": "3x₁ + 5x₂ ≥ 90 (Protein)", "color": "#ef4444"},
                {"a1": 1, "a2": 1, "b": 30, "dir": ">=", "label": "x₁ + x₂ ≥ 30 (Fat)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "A", "x1": 0, "x2": 30, "z": 90, "isOpt": False},
                {"label": "B", "x1": 15, "x2": 15, "z": 75, "isOpt": False},
                {"label": "C", "x1": 30, "x2": 0, "z": 60, "isOpt": True}
            ]
        }
    },
    {
        "id": "lpp_6", "title": "6. Clothing Production (Parkas & Overcoats)",
        "difficulty": "medium", "tags": ["lpp", "garment"],
        "context": "Parkas (profit $30) need 1 sqft leather. Overcoats (profit $50) need 2 sqft. Total leather available = 40 sqft. Max parkas = 20, max overcoats = 15.",
        "steps": [
            {"title": "Decision Variables", "explain": "Parkas (x1) and Overcoats (x2).", "formulation": "Let x\u2081 = number of parkas\nLet x\u2082 = number of overcoats"},
            {"title": "Objective Function & Constraints", "explain": "Maximize total profit.", "formulation": "Maximize Z = 30x\u2081 + 50x\u2082\nSubject to:\n  x\u2081 + 2x\u2082 \u2264 40 (Leather limit)\n  x\u2081       \u2264 20 (Parka demand)\n       x\u2082 \u2264 15 (Overcoat demand)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Parkas (x\u2081) = <strong>20</strong></li><li>Overcoats (x\u2082) = <strong>10</strong></li><li><strong>Maximum Profit = $1,100</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 30, "c2": 50, "maxX1": 25, "maxX2": 20,
            "constraints": [
                {"a1": 1, "a2": 2, "b": 40, "dir": "<=", "label": "x₁ + 2x₂ ≤ 40 (Leather)", "color": "#ef4444"},
                {"a1": 1, "a2": 0, "b": 20, "dir": "<=", "label": "x₁ ≤ 20 (Parka Limit)", "color": "#3b82f6"},
                {"a1": 0, "a2": 1, "b": 15, "dir": "<=", "label": "x₂ ≤ 15 (Overcoat Limit)", "color": "#10b981"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 20, "x2": 0, "z": 600, "isOpt": False},
                {"label": "B", "x1": 20, "x2": 10, "z": 1100, "isOpt": True},
                {"label": "C", "x1": 10, "x2": 15, "z": 1050, "isOpt": False},
                {"label": "D", "x1": 0, "x2": 15, "z": 750, "isOpt": False}
            ]
        }
    },
    {
        "id": "lpp_7", "title": "7. Warehouse Transportation LPP Model",
        "difficulty": "medium", "tags": ["lpp", "transportation-lpp"],
        "context": "Minimize shipping cost from 2 warehouses to 3 regional customer centers.",
        "steps": [
            {"title": "Decision Variables", "explain": "Let x_ij = units shipped from warehouse i to customer j.", "formulation": "x₁₁, x₁₂, x₁₃ (Warehouse 1)\nx₂₁, x₂₂, x₂₃ (Warehouse 2)"},
            {"title": "Objective Function & Constraints", "explain": "Minimize total transportation cost.", "formulation": "Minimize Z = 2x₁₁ + 3x₁₂ + x₁₃ + 5x₂₁ + 4x₂₂ + 8x₂₃\nSubject to:\n  x₁₁+x₁₂+x₁₃ \u2264 120 (Supply 1)\n  x₂₁+x₂₂+x₂₃ \u2264 80  (Supply 2)\n  x₁₁+x₂₁ \u2265 150 (Demand 1)\n  x₁₂+x₂₂ \u2265 40  (Demand 2)\n  x₁₃+x₂₃ \u2265 10  (Demand 3)"},
            {"title": "Optimal Solution", "explain": "Solved via Simplex / Transportation Algorithm.", "body": "<div class='res-box'><h4>\u2705 Optimal Transportation Schedule</h4><ul><li>Optimal shipping pattern minimizes cost across supply hubs.</li></ul></div>"}
        ]
    },
    {
        "id": "lpp_8", "title": "8. Refinery Crude Oil Blending",
        "difficulty": "medium", "tags": ["lpp", "blending"],
        "context": "Blend Crude A ($4/bbl profit) and Crude B ($5/bbl profit) under octane ratio and total capacity (50 barrels) limits.",
        "steps": [
            {"title": "Decision Variables", "explain": "Crude A (x1) and Crude B (x2) barrels.", "formulation": "Let x\u2081 = barrels of Crude A\nLet x\u2082 = barrels of Crude B"},
            {"title": "Objective Function & Constraints", "explain": "Maximize blending profit.", "formulation": "Maximize Z = 4x\u2081 + 5x\u2082\nSubject to:\n  x\u2081 - x\u2082 \u2264 0 (Octane ratio: x\u2081 \u2264 x\u2082)\n  x\u2081 + x\u2082 \u2264 50 (Total plant capacity)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Blend</h4><ul><li>Crude A (x\u2081) = <strong>0 bbl</strong></li><li>Crude B (x\u2082) = <strong>50 bbl</strong></li><li><strong>Maximum Profit = $250</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 4, "c2": 5, "maxX1": 60, "maxX2": 60,
            "constraints": [
                {"a1": 1, "a2": -1, "b": 0, "dir": "<=", "label": "x₁ - x₂ ≤ 0 (Octane Ratio)", "color": "#ef4444"},
                {"a1": 1, "a2": 1, "b": 50, "dir": "<=", "label": "x₁ + x₂ ≤ 50 (Plant Cap)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 25, "x2": 25, "z": 225, "isOpt": False},
                {"label": "B", "x1": 0, "x2": 50, "z": 250, "isOpt": True}
            ]
        }
    },
    {
        "id": "lpp_9", "title": "9. Financial Portfolio Asset Allocation",
        "difficulty": "medium", "tags": ["lpp", "portfolio"],
        "context": "Invest in Stocks (x1), Bonds (x2), and Cash (x3) to maximize return meeting risk limits.",
        "steps": [
            {"title": "Decision Variables", "explain": "x1 = Stocks %, x2 = Bonds %, x3 = Cash %.", "formulation": "Let x\u2081 = Stocks %, x\u2082 = Bonds %, x\u2083 = Cash %"},
            {"title": "Objective Function & Constraints", "explain": "Maximize total portfolio return.", "formulation": "Maximize Z = 0.12x\u2081 + 0.08x\u2082 + 0.04x\u2083\nSubject to:\n  x\u2081 + x\u2082 + x\u2083 = 100 (Total %)\n  x\u2081 \u2264 60 (Risk cap on stocks)\n  x\u2082 \u2265 20 (Min bond allocation)\n  x\u2081, x\u2082, x\u2083 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Optimal 3-variable portfolio allocation.", "body": "<div class='res-box'><h4>\u2705 Optimal Portfolio</h4><ul><li>Stocks (x\u2081) = <strong>60%</strong></li><li>Bonds (x\u2082) = <strong>40%</strong></li><li>Cash (x\u2083) = <strong>0%</strong></li><li><strong>Maximum Portfolio Return = 10.4%</strong></li></ul></div>"}
        ]
    },
    {
        "id": "lpp_10", "title": "10. Garment Factory Production",
        "difficulty": "medium", "tags": ["lpp", "apparel"],
        "context": "Shirts need 2 hrs cutting, 1 hr sewing (profit $5). Trousers need 1 hr cutting, 3 hrs sewing (profit $7). Available: Cutting = 40 hrs, Sewing = 45 hrs.",
        "steps": [
            {"title": "Decision Variables", "explain": "Shirts (x1) and Trousers (x2).", "formulation": "Let x\u2081 = Shirts, x\u2082 = Trousers"},
            {"title": "Objective Function & Constraints", "explain": "Maximize profit.", "formulation": "Maximize Z = 5x\u2081 + 7x\u2082\nSubject to:\n  2x\u2081 + x\u2082 \u2264 40 (Cutting)\n   x\u2081 + 3x\u2082 \u2264 45 (Sewing)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Mix</h4><ul><li>Shirts (x\u2081) = <strong>15</strong></li><li>Trousers (x\u2082) = <strong>10</strong></li><li><strong>Maximum Profit = $145</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 5, "c2": 7, "maxX1": 25, "maxX2": 20,
            "constraints": [
                {"a1": 2, "a2": 1, "b": 40, "dir": "<=", "label": "2x₁ + x₂ ≤ 40 (Cutting)", "color": "#ef4444"},
                {"a1": 1, "a2": 3, "b": 45, "dir": "<=", "label": "x₁ + 3x₂ ≤ 45 (Sewing)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 20, "x2": 0, "z": 100, "isOpt": False},
                {"label": "B", "x1": 15, "x2": 10, "z": 145, "isOpt": True},
                {"label": "C", "x1": 0, "x2": 15, "z": 105, "isOpt": False}
            ]
        }
    },
    {
        "id": "lpp_11", "title": "11. Electronics Assembly & Testing",
        "difficulty": "medium", "tags": ["lpp", "electronics"],
        "context": "TVs (profit $12) need 3 hrs assembly, 1 hr testing. Radios (profit $7) need 2 hrs assembly, 2 hrs testing. Available: Assembly = 60 hrs, Testing = 40 hrs.",
        "steps": [
            {"title": "Decision Variables", "explain": "TVs (x1) and Radios (x2).", "formulation": "Let x\u2081 = TVs, x\u2082 = Radios"},
            {"title": "Objective Function & Constraints", "explain": "Maximize total profit.", "formulation": "Maximize Z = 12x\u2081 + 7x\u2082\nSubject to:\n  3x\u2081 + 2x\u2082 \u2264 60 (Assembly)\n   x\u2081 + 2x\u2082 \u2264 40 (Testing)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>TVs (x\u2081) = <strong>20</strong></li><li>Radios (x\u2082) = <strong>0</strong></li><li><strong>Maximum Profit = $240</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 12, "c2": 7, "maxX1": 25, "maxX2": 25,
            "constraints": [
                {"a1": 3, "a2": 2, "b": 60, "dir": "<=", "label": "3x₁ + 2x₂ ≤ 60 (Assembly)", "color": "#ef4444"},
                {"a1": 1, "a2": 2, "b": 40, "dir": "<=", "label": "x₁ + 2x₂ ≤ 40 (Testing)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 20, "x2": 0, "z": 240, "isOpt": True},
                {"label": "B", "x1": 10, "x2": 15, "z": 225, "isOpt": False},
                {"label": "C", "x1": 0, "x2": 20, "z": 140, "isOpt": False}
            ]
        }
    },
    {
        "id": "lpp_12", "title": "12. Chemical Reaction Blending",
        "difficulty": "medium", "tags": ["lpp", "chemical"],
        "context": "Mix Chemical A ($8 profit) and B ($5 profit) under total volume (200 units) and reaction rate (3x1 + x2 <= 360) constraints.",
        "steps": [
            {"title": "Decision Variables", "explain": "Chemical A (x1) and B (x2).", "formulation": "Let x\u2081 = Chemical A, x\u2082 = Chemical B"},
            {"title": "Objective Function & Constraints", "explain": "Maximize profit.", "formulation": "Maximize Z = 8x\u2081 + 5x\u2082\nSubject to:\n   x\u2081 + x\u2082 \u2264 200 (Total Volume)\n  3x\u2081 + x\u2082 \u2264 360 (Reaction Limit)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Chemical A (x\u2081) = <strong>80 units</strong></li><li>Chemical B (x\u2082) = <strong>120 units</strong></li><li><strong>Maximum Profit = $1,240</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 8, "c2": 5, "maxX1": 150, "maxX2": 220,
            "constraints": [
                {"a1": 1, "a2": 1, "b": 200, "dir": "<=", "label": "x₁ + x₂ ≤ 200 (Total Volume)", "color": "#ef4444"},
                {"a1": 3, "a2": 1, "b": 360, "dir": "<=", "label": "3x₁ + x₂ ≤ 360 (Reaction Cap)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 120, "x2": 0, "z": 960, "isOpt": False},
                {"label": "B", "x1": 80, "x2": 120, "z": 1240, "isOpt": True},
                {"label": "C", "x1": 0, "x2": 200, "z": 1000, "isOpt": False}
            ]
        }
    },
    {
        "id": "lpp_13", "title": "13. Media Advertising Allocation",
        "difficulty": "medium", "tags": ["lpp", "advertising"],
        "context": "TV ads reach 200K viewers ($5K). Newspaper ads reach 80K viewers ($2K). Budget = $20K. TV ad cap = 3, Newspaper cap = 7.",
        "steps": [
            {"title": "Decision Variables", "explain": "TV ads (x1) and Newspaper ads (x2).", "formulation": "Let x\u2081 = TV ads, x\u2082 = Newspaper ads"},
            {"title": "Objective Function & Constraints", "explain": "Maximize total viewers (in 1000s).", "formulation": "Maximize Z = 200x\u2081 + 80x\u2082\nSubject to:\n  5x\u2081 + 2x\u2082 \u2264 20 (Budget)\n   x\u2081       \u2264 3  (TV cap)\n        x\u2082 \u2264 7  (Paper cap)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Ad Mix</h4><ul><li>TV Ads (x\u2081) = <strong>3</strong></li><li>Newspaper Ads (x\u2082) = <strong>2.5</strong></li><li><strong>Maximum Audience Reach = 800,000 viewers</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 200, "c2": 80, "maxX1": 5, "maxX2": 10,
            "constraints": [
                {"a1": 5, "a2": 2, "b": 20, "dir": "<=", "label": "5x₁ + 2x₂ ≤ 20 (Budget)", "color": "#ef4444"},
                {"a1": 1, "a2": 0, "b": 3,  "dir": "<=", "label": "x₁ ≤ 3 (TV Cap)", "color": "#3b82f6"},
                {"a1": 0, "a2": 1, "b": 7,  "dir": "<=", "label": "x₂ ≤ 7 (Paper Cap)", "color": "#10b981"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 3, "x2": 0, "z": 600, "isOpt": False},
                {"label": "B", "x1": 3, "x2": 2.5, "z": 800, "isOpt": True},
                {"label": "C", "x1": 1.2, "x2": 7, "z": 800, "isOpt": True},
                {"label": "D", "x1": 0, "x2": 7, "z": 560, "isOpt": False}
            ]
        }
    },
    {
        "id": "lpp_14", "title": "14. Bakery Pastry Production",
        "difficulty": "medium", "tags": ["lpp", "bakery"],
        "context": "Cakes take 2 hrs baking, 1 hr icing (profit $10). Pastries take 1 hr baking, 2 hrs icing (profit $6). Hours available: Baking = 16, Icing = 16.",
        "steps": [
            {"title": "Decision Variables", "explain": "Cakes (x1) and Pastries (x2).", "formulation": "Let x\u2081 = Cakes, x\u2082 = Pastries"},
            {"title": "Objective Function & Constraints", "explain": "Maximize total profit.", "formulation": "Maximize Z = 10x\u2081 + 6x\u2082\nSubject to:\n  2x\u2081 + x\u2082 \u2264 16 (Baking)\n   x\u2081 + 2x\u2082 \u2264 16 (Icing)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Production</h4><ul><li>Cakes (x\u2081) = <strong>5.33</strong></li><li>Pastries (x\u2082) = <strong>5.33</strong></li><li><strong>Maximum Profit = $85.33</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 10, "c2": 6, "maxX1": 10, "maxX2": 10,
            "constraints": [
                {"a1": 2, "a2": 1, "b": 16, "dir": "<=", "label": "2x₁ + x₂ ≤ 16 (Baking)", "color": "#ef4444"},
                {"a1": 1, "a2": 2, "b": 16, "dir": "<=", "label": "x₁ + 2x₂ ≤ 16 (Icing)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 8, "x2": 0, "z": 80, "isOpt": False},
                {"label": "B", "x1": 5.33, "x2": 5.33, "z": 85.33, "isOpt": True},
                {"label": "C", "x1": 0, "x2": 8, "z": 48, "isOpt": False}
            ]
        }
    },
    {
        "id": "lpp_15", "title": "15. Steel Plant Rolling Mill Production",
        "difficulty": "medium", "tags": ["lpp", "manufacturing"],
        "context": "Hot-rolled steel needs 4 hrs mill time ($15 profit). Cold-rolled needs 2 hrs mill, 2 hrs finishing ($12 profit). Mill available = 80 hrs, Finishing available = 40 hrs.",
        "steps": [
            {"title": "Decision Variables", "explain": "Hot-rolled (x1) and Cold-rolled (x2).", "formulation": "Let x\u2081 = Hot-rolled tons, x\u2082 = Cold-rolled tons"},
            {"title": "Objective Function & Constraints", "explain": "Maximize mill profit.", "formulation": "Maximize Z = 15x\u2081 + 12x\u2082\nSubject to:\n  4x\u2081 + 2x\u2082 \u2264 80 (Mill Time)\n        2x\u2082 \u2264 40 (Finishing)\n  x\u2081, x\u2082 \u2265 0"},
            {"title": "Optimal Solution", "explain": "Corner point evaluation.", "body": "<div class='res-box'><h4>\u2705 Optimal Production</h4><ul><li>Hot-rolled (x\u2081) = <strong>10 tons</strong></li><li>Cold-rolled (x\u2082) = <strong>20 tons</strong></li><li><strong>Maximum Profit = $390</strong></li></ul></div>"}
        ],
        "graph": {
            "type": "max", "c1": 15, "c2": 12, "maxX1": 25, "maxX2": 25,
            "constraints": [
                {"a1": 4, "a2": 2, "b": 80, "dir": "<=", "label": "4x₁ + 2x₂ ≤ 80 (Mill Time)", "color": "#ef4444"},
                {"a1": 0, "a2": 2, "b": 40, "dir": "<=", "label": "2x₂ ≤ 40 (Finishing)", "color": "#3b82f6"}
            ],
            "corners": [
                {"label": "O", "x1": 0, "x2": 0, "z": 0, "isOpt": False},
                {"label": "A", "x1": 20, "x2": 0, "z": 300, "isOpt": False},
                {"label": "B", "x1": 10, "x2": 20, "z": 390, "isOpt": True},
                {"label": "C", "x1": 0, "x2": 20, "z": 240, "isOpt": False}
            ]
        }
    }
]

with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace lpp_problems array in build script
start_idx = code.find("lpp_problems = [")
end_idx = code.find("# ─────────────────────────────────────────────────────────────────────────────\n# 2. TRANSPORTATION PROBLEMS")

new_lpp_code = "lpp_problems = " + json.dumps(lpp_problems, indent=4).replace("false", "False").replace("true", "True") + "\n"

if start_idx != -1 and end_idx != -1:
    updated_code = code[:start_idx] + new_lpp_code + "\n" + code[end_idx:]
    with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
        f.write(updated_code)
    print("Successfully replaced lpp_problems section with 15 explicit problems!")
else:
    print(f"Error finding markers: start_idx={start_idx}, end_idx={end_idx}")
