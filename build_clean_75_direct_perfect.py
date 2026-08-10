import json, os, copy
from generate_perfect_75_hub import solve_nwc, solve_lcm, solve_vam

print("Building OR Hub with SVG Network Diagrams for SP and MST...")

# ─────────────────────────────────────────────────────────────────────────────
# 1. LPP PROBLEMS (15)
# ─────────────────────────────────────────────────────────────────────────────
lpp_problems = [
    {
        "id": "lpp_1",
        "title": "1. Reddy Mikks Paint Production Optimization",
        "difficulty": "easy",
        "tags": [
            "product-mix",
            "graphical-method"
        ],
        "context": "Reddy Mikks produces exterior and interior paints from two raw materials M1 and M2 with daily capacities of 24 tons and 6 tons respectively. Exterior paint yields $5,000/ton profit while interior paint yields $4,000/ton. A market survey restricts daily interior paint production to at most 1 ton more than exterior paint and caps total interior demand at 2 tons per day.",
        "steps": [
            {
                "title": "Decision Variables Definition",
                "explain": "Define daily production amounts of paints in tons.",
                "formulation": "Let x\u2081 = daily amount of exterior paint produced (tons)\nLet x\u2082 = daily amount of interior paint produced (tons)"
            },
            {
                "title": "Objective Function Formulation",
                "explain": "Maximize total daily profit in thousands of dollars.",
                "formulation": "Maximize Z = 5x\u2081 + 4x\u2082\n\nWhere:\n  5 = profit per ton of exterior paint ($1000s)\n  4 = profit per ton of interior paint ($1000s)"
            },
            {
                "title": "Constraints Formulation",
                "explain": "Formulate raw material availability and market limit constraints.",
                "formulation": "Subject to:\n  6x\u2081 + 4x\u2082 \u2264 24   (Raw material M1 constraint)\n   x\u2081 + 2x\u2082 \u2264  6   (Raw material M2 constraint)\n  x\u2082 - x\u2081 \u2264  1   (Market limit: interior \u2264 exterior + 1)\n        x\u2082 \u2264  2   (Demand limit: max interior paint)\n  x\u2081, x\u2082 \u2265 0      (Non-negativity constraints)"
            },
            {
                "title": "Graphical Corner Point Evaluation",
                "explain": "Evaluate objective function Z at all feasible vertices O, A, B, C, D, E.",
                "body": "<div class=\"table-wrap\"><table class=\"ppt-table\"><thead><tr><th>Corner Point</th><th>x\u2081 (Exterior)</th><th>x\u2082 (Interior)</th><th>Z = 5x\u2081 + 4x\u2082 ($1000s)</th></tr></thead><tbody><tr><td>O (Origin)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A (M1 x-intercept)</td><td>4</td><td>0</td><td>20</td></tr><tr><td>B (M1 \u2229 M2)</td><td>3.33</td><td>1.33</td><td class=\"opt\">21.98 (Optimal)</td></tr><tr><td>C (M1 \u2229 Market limit)</td><td>3</td><td>1.5</td><td>21</td></tr><tr><td>D (M2 \u2229 Demand limit)</td><td>2</td><td>2</td><td>18</td></tr><tr><td>E (Demand limit y-intercept)</td><td>0</td><td>2</td><td>8</td></tr></tbody></table></div>"
            },
            {
                "title": "Optimal Production Plan",
                "explain": "Intersection of binding constraints M1 and M2 yields optimal point B.",
                "body": "<div class=\"res-box\"><h4>\u2705 Optimal Production Plan</h4><ul><li>Exterior Paint (x\u2081) = <strong>3.33 tons/day</strong></li><li>Interior Paint (x\u2082) = <strong>1.33 tons/day</strong></li><li><strong>Maximum Daily Profit Z = $21,980</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 5,
            "c2": 4,
            "maxX1": 6,
            "maxX2": 4,
            "constraints": [
                {
                    "a1": 6,
                    "a2": 4,
                    "b": 24,
                    "dir": "<=",
                    "label": "6x\u2081 + 4x\u2082 \u2264 24 (M1)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 2,
                    "b": 6,
                    "dir": "<=",
                    "label": "x\u2081 + 2x\u2082 \u2264 6 (M2)",
                    "color": "#3b82f6"
                },
                {
                    "a1": -1,
                    "a2": 1,
                    "b": 1,
                    "dir": "<=",
                    "label": "-x\u2081 + x\u2082 \u2264 1 (Market)",
                    "color": "#8b5cf6"
                },
                {
                    "a1": 0,
                    "a2": 1,
                    "b": 2,
                    "dir": "<=",
                    "label": "x\u2082 \u2264 2 (Demand)",
                    "color": "#f59e0b"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 4,
                    "x2": 0,
                    "z": 20,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 3.33,
                    "x2": 1.33,
                    "z": 21.98,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 3,
                    "x2": 1.5,
                    "z": 21,
                    "isOpt": False
                },
                {
                    "label": "D",
                    "x1": 1,
                    "x2": 2,
                    "z": 13,
                    "isOpt": False
                },
                {
                    "label": "E",
                    "x1": 0,
                    "x2": 1,
                    "z": 4,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_2",
        "title": "2. Wyndor Glass Product Line Revamp",
        "difficulty": "easy",
        "tags": [
            "product-mix",
            "plant-capacity"
        ],
        "context": "Wyndor Glass Co. plans to launch two innovative product lines: glass doors with aluminum frames (Product 1, $3,000 profit/batch) and wood-framed windows (Product 2, $5,000 profit/batch). Production requires processing across three specialized plants with limited weekly working capacities of 4 hours at Plant 1, 12 hours at Plant 2, and 18 hours at Plant 3. Management needs an optimal product mix to maximize weekly operating profits while honoring plant limits.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Batches produced per week.",
                "formulation": "Let x\u2081 = number of batches of Product 1 produced per week\nLet x\u2082 = number of batches of Product 2 produced per week"
            },
            {
                "title": "Objective Function",
                "explain": "Maximize total weekly profit in $1000s.",
                "formulation": "Maximize Z = 3x\u2081 + 5x\u2082"
            },
            {
                "title": "Constraints",
                "explain": "Weekly hours available at Plants 1, 2, and 3.",
                "formulation": "Subject to:\n   x\u2081      \u2264  4   (Plant 1 capacity)\n        2x\u2082 \u2264 12   (Plant 2 capacity)\n  3x\u2081 + 2x\u2082 \u2264 18   (Plant 3 capacity)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Corner Point Evaluation",
                "explain": "Evaluate Z at all feasible vertices.",
                "body": "<div class=\"table-wrap\"><table class=\"ppt-table\"><thead><tr><th>Corner Point</th><th>x\u2081</th><th>x\u2082</th><th>Z = 3x\u2081 + 5x\u2082</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>4</td><td>0</td><td>12</td></tr><tr><td>B</td><td>4</td><td>3</td><td>27</td></tr><tr><td>C</td><td>2</td><td>6</td><td class=\"opt\">36 (Optimal)</td></tr><tr><td>D</td><td>0</td><td>6</td><td>30</td></tr></tbody></table></div>"
            },
            {
                "title": "Optimal Solution",
                "explain": "Maximum profit occurs at point C.",
                "body": "<div class=\"res-box\"><h4>\u2705 Optimal Product Mix</h4><ul><li>Product 1 = <strong>2 batches/week</strong></li><li>Product 2 = <strong>6 batches/week</strong></li><li><strong>Maximum Weekly Profit = $36,000</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 3,
            "c2": 5,
            "maxX1": 6,
            "maxX2": 8,
            "constraints": [
                {
                    "a1": 1,
                    "a2": 0,
                    "b": 4,
                    "dir": "<=",
                    "label": "x\u2081 \u2264 4 (Plant 1)",
                    "color": "#ef4444"
                },
                {
                    "a1": 0,
                    "a2": 2,
                    "b": 12,
                    "dir": "<=",
                    "label": "2x\u2082 \u2264 12 (Plant 2)",
                    "color": "#3b82f6"
                },
                {
                    "a1": 3,
                    "a2": 2,
                    "b": 18,
                    "dir": "<=",
                    "label": "3x\u2081 + 2x\u2082 \u2264 18 (Plant 3)",
                    "color": "#10b981"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 4,
                    "x2": 0,
                    "z": 12,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 4,
                    "x2": 3,
                    "z": 27,
                    "isOpt": False
                },
                {
                    "label": "C",
                    "x1": 2,
                    "x2": 6,
                    "z": 36,
                    "isOpt": True
                },
                {
                    "label": "D",
                    "x1": 0,
                    "x2": 6,
                    "z": 30,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_3",
        "title": "3. 7-Day Workforce Shift Scheduling",
        "difficulty": "hard",
        "tags": [
            "workforce-scheduling",
            "integer-lpp"
        ],
        "context": "A 24/7 industrial manufacturing facility operates continuously across all seven days of the week with varying daily staffing demands ranging from 11 workers on Sunday to 19 workers on Thursday. Each full-time employee works 5 consecutive days followed by 2 mandatory days off to ensure fatigue compliance. The plant manager must formulate an integer linear programming schedule to minimize total headcount while fulfilling daily shift coverage.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "x_i = workers starting 5-day shift on day i.",
                "formulation": "Let x\u2081=Mon start, x\u2082=Tue, x\u2083=Wed, x\u2084=Thu, x\u2085=Fri, x\u2086=Sat, x\u2087=Sun"
            },
            {
                "title": "Objective Function",
                "explain": "Minimize total workers hired.",
                "formulation": "Minimize Z = x\u2081 + x\u2082 + x\u2083 + x\u2084 + x\u2085 + x\u2086 + x\u2087"
            },
            {
                "title": "Daily Coverage Constraints",
                "explain": "Each day must have enough workers on duty.",
                "formulation": "Subject to:\n  x\u2081+x\u2084+x\u2085+x\u2086+x\u2087 \u2265 17  (Mon)\n  x\u2081+x\u2082+x\u2085+x\u2086+x\u2087 \u2265 13  (Tue)\n  x\u2081+x\u2082+x\u2083+x\u2086+x\u2087 \u2265 15  (Wed)\n  x\u2081+x\u2082+x\u2083+x\u2084+x\u2087 \u2265 19  (Thu)\n  x\u2081+x\u2082+x\u2083+x\u2084+x\u2085 \u2265 14  (Fri)\n  x\u2082+x\u2083+x\u2084+x\u2085+x\u2086 \u2265 16  (Sat)\n  x\u2083+x\u2084+x\u2085+x\u2086+x\u2087 \u2265 11  (Sun)\n  x_i \u2265 0, integer"
            },
            {
                "title": "Optimal Hiring Schedule",
                "explain": "Integer LPP optimal solution.",
                "body": "<div class=\"res-box\"><h4>\u2705 Optimal Hiring Schedule</h4><ul><li>x\u2081=4, x\u2082=8, x\u2083=2, x\u2084=6, x\u2085=0, x\u2086=3, x\u2087=0</li><li><strong>Minimum Total Workforce = 23 workers</strong></li></ul></div>"
            }
        ]
    },
    {
        "id": "lpp_4",
        "title": "4. Furniture Production (Carpentry & Painting)",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "product-mix"
        ],
        "context": "A custom furniture workshop manufactures dining tables (yielding $6 profit each) and ergonomic chairs (yielding $8 profit each) using shared carpentry and painting workshops. Available monthly shop capacities are strictly capped at 48 hours for carpentry and 20 hours for painting. The plant supervisor needs to determine the exact monthly production quantities of tables and chairs to maximize net workshop returns.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Tables (x1) and Chairs (x2) produced.",
                "formulation": "Let x\u2081 = number of tables produced\nLet x\u2082 = number of chairs produced"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize total profit.",
                "formulation": "Maximize Z = 6x\u2081 + 8x\u2082\nSubject to:\n  3x\u2081 + 2x\u2082 \u2264 48 (Carpentry)\n   x\u2081 + 2x\u2082 \u2264 20 (Painting)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Tables (x\u2081) = <strong>14</strong></li><li>Chairs (x\u2082) = <strong>3</strong></li><li><strong>Maximum Profit = $108</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 6,
            "c2": 8,
            "maxX1": 20,
            "maxX2": 15,
            "constraints": [
                {
                    "a1": 3,
                    "a2": 2,
                    "b": 48,
                    "dir": "<=",
                    "label": "3x\u2081 + 2x\u2082 \u2264 48 (Carpentry)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 2,
                    "b": 20,
                    "dir": "<=",
                    "label": "x\u2081 + 2x\u2082 \u2264 20 (Painting)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 16,
                    "x2": 0,
                    "z": 96,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 14,
                    "x2": 3,
                    "z": 108,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 0,
                    "x2": 10,
                    "z": 80,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_5",
        "title": "5. Farm Feed Diet Cost Minimization",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "diet-problem"
        ],
        "context": "A commercial livestock feed manufacturer blends natural grain ($2 per bag) and processed soybean meal ($3 per bag) to formulate a daily cattle diet. The nutritional blend must contain at least 90 units of crude protein and 30 units of dietary fat per batch to maintain livestock health. The operations nutritionist needs to determine the minimum-cost blending ratio that fully satisfies all dietary constraints.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Grain (x1) and Soybean (x2) bags.",
                "formulation": "Let x\u2081 = bags of grain\nLet x\u2082 = bags of soybean"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Minimize feed cost.",
                "formulation": "Minimize Z = 2x\u2081 + 3x\u2082\nSubject to:\n  3x\u2081 + 5x\u2082 \u2265 90 (Protein requirement)\n   x\u2081 +  x\u2082 \u2265 30 (Fat requirement)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation for minimization.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Grain (x\u2081) = <strong>30 bags</strong></li><li>Soybean (x\u2082) = <strong>0 bags</strong></li><li><strong>Minimum Feed Cost = $60</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "min",
            "c1": 2,
            "c2": 3,
            "maxX1": 40,
            "maxX2": 35,
            "constraints": [
                {
                    "a1": 3,
                    "a2": 5,
                    "b": 90,
                    "dir": ">=",
                    "label": "3x\u2081 + 5x\u2082 \u2265 90 (Protein)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 1,
                    "b": 30,
                    "dir": ">=",
                    "label": "x\u2081 + x\u2082 \u2265 30 (Fat)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "A",
                    "x1": 0,
                    "x2": 30,
                    "z": 90,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 15,
                    "x2": 15,
                    "z": 75,
                    "isOpt": False
                },
                {
                    "label": "C",
                    "x1": 30,
                    "x2": 0,
                    "z": 60,
                    "isOpt": True
                }
            ]
        }
    },
    {
        "id": "lpp_6",
        "title": "6. Clothing Production (Parkas & Overcoats)",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "garment"
        ],
        "context": "An outdoor apparel manufacturer produces premium leather parkas (profit $30/unit) and insulated overcoats (profit $50/unit) from high-grade leather stock. Total raw leather availability is constrained to 40 square feet per batch, with parkas requiring 1 sq ft and overcoats requiring 2 sq ft. Seasonal market demand caps maximum production at 20 parkas and 15 overcoats, requiring an optimal batch decision.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Parkas (x1) and Overcoats (x2).",
                "formulation": "Let x\u2081 = number of parkas\nLet x\u2082 = number of overcoats"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize total profit.",
                "formulation": "Maximize Z = 30x\u2081 + 50x\u2082\nSubject to:\n  x\u2081 + 2x\u2082 \u2264 40 (Leather limit)\n  x\u2081       \u2264 20 (Parka demand)\n       x\u2082 \u2264 15 (Overcoat demand)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Parkas (x\u2081) = <strong>20</strong></li><li>Overcoats (x\u2082) = <strong>10</strong></li><li><strong>Maximum Profit = $1,100</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 30,
            "c2": 50,
            "maxX1": 25,
            "maxX2": 20,
            "constraints": [
                {
                    "a1": 1,
                    "a2": 2,
                    "b": 40,
                    "dir": "<=",
                    "label": "x\u2081 + 2x\u2082 \u2264 40 (Leather)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 0,
                    "b": 20,
                    "dir": "<=",
                    "label": "x\u2081 \u2264 20 (Parka Limit)",
                    "color": "#3b82f6"
                },
                {
                    "a1": 0,
                    "a2": 1,
                    "b": 15,
                    "dir": "<=",
                    "label": "x\u2082 \u2264 15 (Overcoat Limit)",
                    "color": "#10b981"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 20,
                    "x2": 0,
                    "z": 600,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 20,
                    "x2": 10,
                    "z": 1100,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 10,
                    "x2": 15,
                    "z": 1050,
                    "isOpt": False
                },
                {
                    "label": "D",
                    "x1": 0,
                    "x2": 15,
                    "z": 750,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_7",
        "title": "7. Warehouse Transportation LPP Model",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "transportation-lpp"
        ],
        "context": "A regional logistics company manages 2 central distribution hubs supplying 3 major retail markets with varying unit freight rates. Total warehouse inventories and customer demand quotas must be balanced under transport capacity bounds. The logistics director needs an LP formulation to minimize total regional distribution costs across all supply channels.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Let x_ij = units shipped from warehouse i to customer j.",
                "formulation": "x\u2081\u2081, x\u2081\u2082, x\u2081\u2083 (Warehouse 1)\nx\u2082\u2081, x\u2082\u2082, x\u2082\u2083 (Warehouse 2)"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Minimize total transportation cost.",
                "formulation": "Minimize Z = 2x\u2081\u2081 + 3x\u2081\u2082 + x\u2081\u2083 + 5x\u2082\u2081 + 4x\u2082\u2082 + 8x\u2082\u2083\nSubject to:\n  x\u2081\u2081+x\u2081\u2082+x\u2081\u2083 \u2264 120 (Supply 1)\n  x\u2082\u2081+x\u2082\u2082+x\u2082\u2083 \u2264 80  (Supply 2)\n  x\u2081\u2081+x\u2082\u2081 \u2265 150 (Demand 1)\n  x\u2081\u2082+x\u2082\u2082 \u2265 40  (Demand 2)\n  x\u2081\u2083+x\u2082\u2083 \u2265 10  (Demand 3)"
            },
            {
                "title": "Optimal Solution",
                "explain": "Solved via Simplex / Transportation Algorithm.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Transportation Schedule</h4><ul><li>Optimal shipping pattern minimizes cost across supply hubs.</li></ul></div>"
            }
        ]
    },
    {
        "id": "lpp_8",
        "title": "8. Refinery Crude Oil Blending",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "blending"
        ],
        "context": "A petroleum refinery processes Crude Oil A (profit $4/barrel) and Crude Oil B (profit $5/barrel) into commercial gasoline blends. Operational safety guidelines require that Crude A cannot exceed Crude B in the blend ratio, while overall refinery distillation capacity is capped at 50 barrels per hour. The chemical engineer must optimize crude throughput to maximize hourly refinery margins.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Crude A (x1) and Crude B (x2) barrels.",
                "formulation": "Let x\u2081 = barrels of Crude A\nLet x\u2082 = barrels of Crude B"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize blending profit.",
                "formulation": "Maximize Z = 4x\u2081 + 5x\u2082\nSubject to:\n  x\u2081 - x\u2082 \u2264 0 (Octane ratio: x\u2081 \u2264 x\u2082)\n  x\u2081 + x\u2082 \u2264 50 (Total plant capacity)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Blend</h4><ul><li>Crude A (x\u2081) = <strong>0 bbl</strong></li><li>Crude B (x\u2082) = <strong>50 bbl</strong></li><li><strong>Maximum Profit = $250</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 4,
            "c2": 5,
            "maxX1": 60,
            "maxX2": 60,
            "constraints": [
                {
                    "a1": 1,
                    "a2": -1,
                    "b": 0,
                    "dir": "<=",
                    "label": "x\u2081 - x\u2082 \u2264 0 (Octane Ratio)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 1,
                    "b": 50,
                    "dir": "<=",
                    "label": "x\u2081 + x\u2082 \u2264 50 (Plant Cap)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 25,
                    "x2": 25,
                    "z": 225,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 0,
                    "x2": 50,
                    "z": 250,
                    "isOpt": True
                }
            ]
        }
    },
    {
        "id": "lpp_9",
        "title": "9. Financial Portfolio Asset Allocation",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "portfolio"
        ],
        "context": "An asset management firm allocates institutional funds across high-yield stocks (12% expected return), corporate bonds (8% return), and liquid cash (4% return). Risk management policy dictates that stock holdings cannot exceed 60% of total capital, while bond allocations must comprise at least 20%. The portfolio manager aims to maximize overall portfolio yield under strict capital allocation rules.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "x1 = Stocks %, x2 = Bonds %, x3 = Cash %.",
                "formulation": "Let x\u2081 = Stocks %, x\u2082 = Bonds %, x\u2083 = Cash %"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize total portfolio return.",
                "formulation": "Maximize Z = 0.12x\u2081 + 0.08x\u2082 + 0.04x\u2083\nSubject to:\n  x\u2081 + x\u2082 + x\u2083 = 100 (Total %)\n  x\u2081 \u2264 60 (Risk cap on stocks)\n  x\u2082 \u2265 20 (Min bond allocation)\n  x\u2081, x\u2082, x\u2083 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Optimal 3-variable portfolio allocation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Portfolio</h4><ul><li>Stocks (x\u2081) = <strong>60%</strong></li><li>Bonds (x\u2082) = <strong>40%</strong></li><li>Cash (x\u2083) = <strong>0%</strong></li><li><strong>Maximum Portfolio Return = 10.4%</strong></li></ul></div>"
            }
        ]
    },
    {
        "id": "lpp_10",
        "title": "10. Garment Factory Production",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "apparel"
        ],
        "context": "An apparel manufacturing facility produces formal shirts ($5 profit per unit) and tailored trousers ($7 profit per unit) across cutting and sewing departments. Shirts require 2 hours of cutting and 1 hour of sewing, whereas trousers require 1 hour of cutting and 3 hours of sewing. With total available shop time capped at 40 cutting hours and 45 sewing hours per week, management seeks the profit-maximizing unit output.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Shirts (x1) and Trousers (x2).",
                "formulation": "Let x\u2081 = Shirts, x\u2082 = Trousers"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize profit.",
                "formulation": "Maximize Z = 5x\u2081 + 7x\u2082\nSubject to:\n  2x\u2081 + x\u2082 \u2264 40 (Cutting)\n   x\u2081 + 3x\u2082 \u2264 45 (Sewing)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Mix</h4><ul><li>Shirts (x\u2081) = <strong>15</strong></li><li>Trousers (x\u2082) = <strong>10</strong></li><li><strong>Maximum Profit = $145</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 5,
            "c2": 7,
            "maxX1": 25,
            "maxX2": 20,
            "constraints": [
                {
                    "a1": 2,
                    "a2": 1,
                    "b": 40,
                    "dir": "<=",
                    "label": "2x\u2081 + x\u2082 \u2264 40 (Cutting)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 3,
                    "b": 45,
                    "dir": "<=",
                    "label": "x\u2081 + 3x\u2082 \u2264 45 (Sewing)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 20,
                    "x2": 0,
                    "z": 100,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 15,
                    "x2": 10,
                    "z": 145,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 0,
                    "x2": 15,
                    "z": 105,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_11",
        "title": "11. Electronics Assembly & Testing",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "electronics"
        ],
        "context": "An electronics firm manufactures smart televisions (profit $12/unit) and digital radios (profit $7/unit) using automated assembly and quality testing lines. Producing a television requires 3 assembly hours and 1 testing hour, while a radio requires 2 assembly hours and 2 testing hours. Total weekly resource availability is limited to 60 assembly hours and 40 testing hours, requiring an optimal production plan.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "TVs (x1) and Radios (x2).",
                "formulation": "Let x\u2081 = TVs, x\u2082 = Radios"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize total profit.",
                "formulation": "Maximize Z = 12x\u2081 + 7x\u2082\nSubject to:\n  3x\u2081 + 2x\u2082 \u2264 60 (Assembly)\n   x\u2081 + 2x\u2082 \u2264 40 (Testing)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>TVs (x\u2081) = <strong>20</strong></li><li>Radios (x\u2082) = <strong>0</strong></li><li><strong>Maximum Profit = $240</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 12,
            "c2": 7,
            "maxX1": 25,
            "maxX2": 25,
            "constraints": [
                {
                    "a1": 3,
                    "a2": 2,
                    "b": 60,
                    "dir": "<=",
                    "label": "3x\u2081 + 2x\u2082 \u2264 60 (Assembly)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 2,
                    "b": 40,
                    "dir": "<=",
                    "label": "x\u2081 + 2x\u2082 \u2264 40 (Testing)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 20,
                    "x2": 0,
                    "z": 240,
                    "isOpt": True
                },
                {
                    "label": "B",
                    "x1": 10,
                    "x2": 15,
                    "z": 225,
                    "isOpt": False
                },
                {
                    "label": "C",
                    "x1": 0,
                    "x2": 20,
                    "z": 140,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_12",
        "title": "12. Chemical Reaction Blending",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "chemical"
        ],
        "context": "A chemical processing plant blends Compound A ($8 profit per unit) and Compound B ($5 profit per unit) in a pressurized reactor. Total batch volume cannot exceed 200 units, while thermal stability requires the combined reaction rate index 3A + B to remain within 360 units. The chemical supervisor needs to maximize financial yield without triggering reactor instability.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Chemical A (x1) and B (x2).",
                "formulation": "Let x\u2081 = Chemical A, x\u2082 = Chemical B"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize profit.",
                "formulation": "Maximize Z = 8x\u2081 + 5x\u2082\nSubject to:\n   x\u2081 + x\u2082 \u2264 200 (Total Volume)\n  3x\u2081 + x\u2082 \u2264 360 (Reaction Limit)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Plan</h4><ul><li>Chemical A (x\u2081) = <strong>80 units</strong></li><li>Chemical B (x\u2082) = <strong>120 units</strong></li><li><strong>Maximum Profit = $1,240</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 8,
            "c2": 5,
            "maxX1": 150,
            "maxX2": 220,
            "constraints": [
                {
                    "a1": 1,
                    "a2": 1,
                    "b": 200,
                    "dir": "<=",
                    "label": "x\u2081 + x\u2082 \u2264 200 (Total Volume)",
                    "color": "#ef4444"
                },
                {
                    "a1": 3,
                    "a2": 1,
                    "b": 360,
                    "dir": "<=",
                    "label": "3x\u2081 + x\u2082 \u2264 360 (Reaction Cap)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 120,
                    "x2": 0,
                    "z": 960,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 80,
                    "x2": 120,
                    "z": 1240,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 0,
                    "x2": 200,
                    "z": 1000,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_13",
        "title": "13. Media Advertising Allocation",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "advertising"
        ],
        "context": "A corporate marketing manager distributes an advertising budget between prime-time television broadcasts ($5,000 per ad, reaching 200,000 viewers) and daily newspaper features ($2,000 per ad, reaching 80,000 viewers). Total available campaign budget is $20,000, with contracts limiting television ads to at most 3 and newspaper placements to at most 7. The campaign goal is to maximize total audience reach.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "TV ads (x1) and Newspaper ads (x2).",
                "formulation": "Let x\u2081 = TV ads, x\u2082 = Newspaper ads"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize total viewers (in 1000s).",
                "formulation": "Maximize Z = 200x\u2081 + 80x\u2082\nSubject to:\n  5x\u2081 + 2x\u2082 \u2264 20 (Budget)\n   x\u2081       \u2264 3  (TV cap)\n        x\u2082 \u2264 7  (Paper cap)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Ad Mix</h4><ul><li>TV Ads (x\u2081) = <strong>3</strong></li><li>Newspaper Ads (x\u2082) = <strong>2.5</strong></li><li><strong>Maximum Audience Reach = 800,000 viewers</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 200,
            "c2": 80,
            "maxX1": 5,
            "maxX2": 10,
            "constraints": [
                {
                    "a1": 5,
                    "a2": 2,
                    "b": 20,
                    "dir": "<=",
                    "label": "5x\u2081 + 2x\u2082 \u2264 20 (Budget)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 0,
                    "b": 3,
                    "dir": "<=",
                    "label": "x\u2081 \u2264 3 (TV Cap)",
                    "color": "#3b82f6"
                },
                {
                    "a1": 0,
                    "a2": 1,
                    "b": 7,
                    "dir": "<=",
                    "label": "x\u2082 \u2264 7 (Paper Cap)",
                    "color": "#10b981"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 3,
                    "x2": 0,
                    "z": 600,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 3,
                    "x2": 2.5,
                    "z": 800,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 1.2,
                    "x2": 7,
                    "z": 800,
                    "isOpt": True
                },
                {
                    "label": "D",
                    "x1": 0,
                    "x2": 7,
                    "z": 560,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_14",
        "title": "14. Bakery Pastry Production",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "bakery"
        ],
        "context": "A commercial bakery produces artisanal cakes ($10 profit per unit) and specialty pastries ($6 profit per unit) requiring baking and icing processes. Each cake requires 2 hours of baking and 1 hour of icing, while each pastry batch requires 1 hour of baking and 2 hours of icing. Available shift capacities are 16 hours for baking and 16 hours for icing, requiring an optimal product mix.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Cakes (x1) and Pastries (x2).",
                "formulation": "Let x\u2081 = Cakes, x\u2082 = Pastries"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize total profit.",
                "formulation": "Maximize Z = 10x\u2081 + 6x\u2082\nSubject to:\n  2x\u2081 + x\u2082 \u2264 16 (Baking)\n   x\u2081 + 2x\u2082 \u2264 16 (Icing)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Production</h4><ul><li>Cakes (x\u2081) = <strong>5.33</strong></li><li>Pastries (x\u2082) = <strong>5.33</strong></li><li><strong>Maximum Profit = $85.33</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 10,
            "c2": 6,
            "maxX1": 10,
            "maxX2": 10,
            "constraints": [
                {
                    "a1": 2,
                    "a2": 1,
                    "b": 16,
                    "dir": "<=",
                    "label": "2x\u2081 + x\u2082 \u2264 16 (Baking)",
                    "color": "#ef4444"
                },
                {
                    "a1": 1,
                    "a2": 2,
                    "b": 16,
                    "dir": "<=",
                    "label": "x\u2081 + 2x\u2082 \u2264 16 (Icing)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 8,
                    "x2": 0,
                    "z": 80,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 5.33,
                    "x2": 5.33,
                    "z": 85.33,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 0,
                    "x2": 8,
                    "z": 48,
                    "isOpt": False
                }
            ]
        }
    },
    {
        "id": "lpp_15",
        "title": "15. Steel Plant Rolling Mill Production",
        "difficulty": "medium",
        "tags": [
            "lpp",
            "manufacturing"
        ],
        "context": "A steel manufacturing mill produces hot-rolled sheets ($15 profit/ton) and cold-rolled coils ($12 profit/ton) using rolling and finishing mills. Hot-rolled steel requires 4 hours of rolling mill time, whereas cold-rolled steel requires 2 hours of rolling and 2 hours of finishing mill time. Weekly capacities are 80 hours for the rolling mill and 40 hours for the finishing mill, requiring an optimal production schedule.",
        "steps": [
            {
                "title": "Decision Variables",
                "explain": "Hot-rolled (x1) and Cold-rolled (x2).",
                "formulation": "Let x\u2081 = Hot-rolled tons, x\u2082 = Cold-rolled tons"
            },
            {
                "title": "Objective Function & Constraints",
                "explain": "Maximize mill profit.",
                "formulation": "Maximize Z = 15x\u2081 + 12x\u2082\nSubject to:\n  4x\u2081 + 2x\u2082 \u2264 80 (Mill Time)\n        2x\u2082 \u2264 40 (Finishing)\n  x\u2081, x\u2082 \u2265 0"
            },
            {
                "title": "Optimal Solution",
                "explain": "Corner point evaluation.",
                "body": "<div class='res-box'><h4>\u2705 Optimal Production</h4><ul><li>Hot-rolled (x\u2081) = <strong>10 tons</strong></li><li>Cold-rolled (x\u2082) = <strong>20 tons</strong></li><li><strong>Maximum Profit = $390</strong></li></ul></div>"
            }
        ],
        "graph": {
            "type": "max",
            "c1": 15,
            "c2": 12,
            "maxX1": 25,
            "maxX2": 25,
            "constraints": [
                {
                    "a1": 4,
                    "a2": 2,
                    "b": 80,
                    "dir": "<=",
                    "label": "4x\u2081 + 2x\u2082 \u2264 80 (Mill Time)",
                    "color": "#ef4444"
                },
                {
                    "a1": 0,
                    "a2": 2,
                    "b": 40,
                    "dir": "<=",
                    "label": "2x\u2082 \u2264 40 (Finishing)",
                    "color": "#3b82f6"
                }
            ],
            "corners": [
                {
                    "label": "O",
                    "x1": 0,
                    "x2": 0,
                    "z": 0,
                    "isOpt": False
                },
                {
                    "label": "A",
                    "x1": 20,
                    "x2": 0,
                    "z": 300,
                    "isOpt": False
                },
                {
                    "label": "B",
                    "x1": 10,
                    "x2": 20,
                    "z": 390,
                    "isOpt": True
                },
                {
                    "label": "C",
                    "x1": 0,
                    "x2": 20,
                    "z": 240,
                    "isOpt": False
                }
            ]
        }
    }
]

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
        "context": "Klyne's household needs to assign 4 children to 4 weekly household chores based on secret bid prices submitted by each child in dollars. To prevent conflict, each child must be assigned to exactly one unique chore while minimizing overall household allowance expenditure. After standard row and column reductions, minimum lines test fails (3 lines < n=4), requiring Hungarian matrix adjustment.",
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
        "context": "A manufacturing plant needs to assign 3 heavy industrial machines to 4 newly built shop-floor locations to minimize material handling costs. A dummy machine with zero cost everywhere is added to balance the 3x4 non-square matrix into a 4x4 Hungarian formulation. Direct assignment becomes possible immediately following row reduction.",
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
        "context": "An IT consulting firm needs to assign 4 senior consultants (Alex, Ben, Cara, Dev) to 4 client software projects (P1 through P4) based on estimated cost bids in thousands of dollars. Initial row and column reduction produces a matrix where three consultants share zeros in only two project columns. Applying the Hungarian coverage test forces a matrix adjustment with k=2 to achieve a valid 1-to-1 matching.",
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
        "context": "A corporate marketing department assigns 4 creative marketing teams to 4 product promotion campaigns (TV, Radio, Print, Online) to minimize total budget requirements in thousands of dollars. Three teams exhibit identical low-cost structures for TV and Radio, creating a 3-vs-2 zero conflict. The Hungarian algorithm adjusts the matrix with k=2 to break the bottleneck and form an optimal matching.",
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
        "context": "A hospital nursing supervisor needs to assign 4 specialized nurses to 4 hospital wards (ICU, ER, Pediatric, Geriatric) based on shift difficulty scores. Three nurses share identical low difficulty ratings for ICU and ER, violating Hall's condition after initial reduction. Subtracting k=1 from uncovered cells creates a new zero at the Pediatric ward, enabling a complete unique assignment.",
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
        "context": "An academic journal editor assigns 4 research scholars to review 4 submitted research manuscripts based on estimated review turnaround times in hours. Three junior scholars require equal review times for Papers 1 and 2, causing 3 rows to compete for 2 zero-columns. The Hungarian method applies matrix adjustment with k=4 hours to allocate all manuscripts optimally.",
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
        "context": "A commercial sales director assigns 4 senior sales representatives to 4 new product lines to minimize total transition and training costs in dollars. Three representatives possess identical proficiency for Product Lines 1 and 2, preventing direct assignment after reduction. Performing Hungarian matrix adjustment with k=6 resolves the conflict and minimizes total training expenditure.",
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
        "context": "A university athletics department assigns 4 track coaches to 4 event categories (100m, 200m, 400m, Relay) based on coaching effort index scores. Three sprint coaches have identical high aptitude for 100m and 200m events, creating a 3-coach conflict for 2 event slots. Matrix adjustment with k=3 expands zero coverage into the 400m event to achieve an optimal assignment.",
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
        "context": "A urban logistics manager assigns 4 delivery vans to 4 delivery routes based on estimated round-trip travel times in minutes. Three vans exhibit identical efficiency on Routes 1 and 2, requiring line coverage adjustment after initial reduction. Subtracting k=7 minutes from uncovered cells generates new zero entries on Route 3, achieving a total time minimization.",
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
        "context": "An Agile scrum master assigns 4 developers (Alice, Bob, Carol, Tech Lead) to 4 sprint modules (Frontend, Backend, Database, Testing) based on estimated story-point effort. Alice, Bob, and Carol are equally skilled in Frontend and Backend, producing a 3-vs-2 zero constraint after reduction. Applying Hungarian adjustment with k=4 story points unlocks optimal task distribution.",
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
        "context": "A university department head assigns 4 faculty members to 4 teaching time slots (8 AM, 10 AM, 12 PM, 2 PM) to minimize total faculty inconvenience scores. Three professors express equal preference for early morning slots, creating zero overlap in 8 AM and 10 AM columns. Matrix adjustment with k=3 inconvenience points resolves the schedule overlap.",
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
        "context": "A construction site manager assigns 4 skilled workers to 4 specialized tasks (Excavation, Concreting, Carpentry, Electrical) based on task completion hours. Three workers have identical productivity in Excavation and Concreting, preventing direct assignment. Executing Hungarian matrix adjustment with k=4 hours enables a complete task allocation at minimum total labor time.",
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
        "context": "A university examination board assigns 4 faculty invigilators to 4 exam halls based on travel and setup time in minutes. Three invigilators have equal proximity to Halls A and B, requiring line coverage matrix modification. Subtracting k=5 minutes from uncovered cells opens Hall C for assignment, minimizing total setup time.",
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
        "context": "A investment bank assigns 4 financial analysts to 4 asset portfolios (Equity, Debt, Hybrid, Gold) based on risk-adjusted management cost scores. Three analysts possess identical competence in Equity and Debt portfolios, violating Hall's condition. Performing Hungarian adjustment with k=5 risk points yields a unique portfolio matching.",
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
        "context": "A supply chain director assigns 4 regional field agents to 4 sales territories (North, South, East, West) based on total travel logistics costs in dollars. Three agents demonstrate identical efficiency in North and South territories, requiring matrix adjustment. Subtracting k=6 dollars from uncovered cells generates a new zero in the East territory for an optimal assignment.",
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
        "context": "Seervada Park management needs to determine the shortest path from the park entrance (Node O) to remote scenic station T for daily tram operations. The sightseeing trail network includes multiple intermediate junction stops (A, B, C, D, E) connected by scenic roads with known mileages. Using Dijkstra's algorithm step-by-step, the park supervisor computes the shortest path of 13 miles.",
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
        "context": "A urban traffic authority needs to optimize the emergency vehicle route from central station S to peripheral industrial park T across 5 intermediate highway junctions. Road segments have varying speed limits and distance bottlenecks. Dijkstra's algorithm evaluates candidate paths step-by-step to establish the shortest distance route of 16 miles.",
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
        "context": "A logistics enterprise coordinates cargo shipments from central manufacturing hub S to retail distribution terminal T through 5 regional transit hubs. Transit times and toll fees are evaluated across all connecting corridors. The supply chain planner applies Dijkstra's algorithm to determine the minimum-cost routing of 12 units.",
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
        "context": "An emergency response center calculates the fastest route for an ambulance traveling from accident site S to trauma hospital T through 5 city intersections. Traffic congestion indexes dictate transit times across all intermediate street links. Dijkstra's algorithm evaluates real-time network states to establish the minimum response path of 11 minutes.",
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
        "context": "A university facilities management department designs a pedestrian walkway guide connecting the main campus entrance S to the library complex T across 5 campus plazas. Distance measurements in meters are evaluated along paved pathways. Dijkstra's algorithm identifies the shortest walking route of 12 units.",
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
        "context": "A cloud infrastructure provider routes high-frequency data packets from origin server S to destination server T through 5 intermediate router nodes. Network latency and transmission delay in milliseconds are evaluated across all fiber connections. Dijkstra's algorithm calculates the minimum-latency network path of 13 ms.",
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
        "context": "An energy corporation transports crude oil from extraction well S to coastal refinery T through 5 intermediate pumping stations. Energy consumption per barrel varies across pipeline terrain segments. Dijkstra's algorithm determines the minimum pumping energy path of 11 units.",
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
        "context": "A railway authority optimizes the express passenger train route connecting terminal station S to regional destination T through 5 intermediate junction cities. Track distance in kilometers is evaluated across all connecting rail segments. Dijkstra's algorithm computes the shortest rail route of 23 units.",
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
        "context": "An e-commerce logistics firm plans the delivery van route from central distribution hub S to customer parcel locker T through 5 urban neighborhood checkpoints. Transit delays in minutes are calculated for each road link. Dijkstra's algorithm identifies the fastest delivery path of 12 minutes.",
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
        "context": "An airport operations group determines the fastest passenger transit path between arrival gate S and departure gate T across 5 terminal concourse junctions. Pedestrian walkway travel times in minutes are evaluated for all connecting corridors. Dijkstra's algorithm establishes the minimum layover travel path of 14 minutes.",
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
        "context": "A telecommunications engineer routes a microwave communications signal from broadcasting tower S to receiver tower T through 5 relay repeater towers. Signal attenuation in decibels is evaluated across all line-of-sight links. Dijkstra's algorithm computes the minimum signal loss path of 15 dB.",
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
        "context": "A municipal water authority plans a high-pressure main supply pipe from reservoir S to district storage tank T through 5 distribution junctions. Hydraulic friction loss is calculated for all pipe segments. Dijkstra's algorithm determines the path of minimum total pressure loss (15 units).",
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
        "context": "A travel agency compiles the lowest-cost flight itinerary connecting departure airport S to vacation destination T across 5 layover airport hubs. Airfare prices in hundreds of dollars are evaluated across all connecting flight legs. Dijkstra's algorithm calculates the cheapest flight path of 12 units.",
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
        "context": "A port authority optimizes container drayage truck movements from receiving gate S to berth terminal T through 5 port yard intersections. Transit times in minutes are calculated across all internal port roadways. Dijkstra's algorithm establishes the minimum drayage route of 17 minutes.",
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
        "context": "An electric utility company routes a high-voltage power transmission line from power plant S to regional substation T across 5 grid node towers. Electrical resistance and line loss are evaluated for all candidate transmission corridors. Dijkstra's algorithm computes the path of minimum line resistance (15 units).",
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
        "context": "Seervada Park management needs to install a permanent telephone communications network connecting all 7 stations (O, A, B, C, D, E, T) with minimum total cable length. The park terrain contains 11 candidate underground cable routes forming multiple closed loops. Prim's algorithm builds the minimum spanning tree step-by-step, achieving a total cable requirement of 14 miles.",
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
        "context": "Midwest TV Cable Company provides cable television service to 5 residential housing developments connected to a central headend station. A total of 8 candidate cable corridors connect adjacent developments, forming 3 closed loops. Prim's algorithm connects all housing developments into a minimum spanning tree with a total cable length of 17 miles.",
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
        "context": "An enterprise IT department needs to interconnect 7 departmental office clusters (Hub, A, B, C, D, E, Gateway) into a unified fiber optic network. The building floorplan features 12 candidate conduit paths forming 5 distinct structural cycles. Prim's algorithm selects the optimal non-cyclic links to construct a minimum spanning tree of 17 units.",
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
        "context": "A rural water development agency plans a clean water distribution grid connecting 7 village residential sectors. The planned layout includes 13 candidate pipeline routes forming 6 closed hydraulic loops. Prim's algorithm identifies the minimum total pipe length (16 units) required to supply all sectors without redundant looping.",
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
        "context": "A university IT team installs high-speed fiber optic cabling to connect 7 academic building clusters to the campus network core. The campus layout offers 12 candidate duct paths with 5 structural cycles. Prim's algorithm connects all buildings into a minimum spanning tree requiring 16 units of fiber.",
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
        "context": "A regional rail network connects 8 passenger stations and freight yards across 14 candidate track corridors forming 6 closed loops. Rail engineers apply Prim's algorithm to determine the minimum total track construction distance (19 units) that ensures full network connectivity.",
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
        "context": "A power utility company designs an interconnected electrical grid linking 7 regional substations and power plants. The network includes 12 high-voltage transmission lines forming 5 closed grid loops. Prim's algorithm constructs a minimum spanning tree requiring 19 units of transmission line.",
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
        "context": "An agricultural irrigation authority connects a river headworks to 6 farming canal sectors through 12 candidate canal channels forming 5 closed loops. Prim's algorithm determines the minimum total canal excavation length (16 units) that guarantees water flow to all sectors.",
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
        "context": "A municipal smart-city initiative connects 8 urban data collection nodes with fiber optic broadband across 15 candidate duct pathways forming 7 structural loops. Prim's algorithm builds a minimum spanning network requiring 18 units of fiber cabling.",
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
        "context": "A natural gas distributor connects a central compressor station to 6 regional distribution points across 12 candidate pipeline corridors forming 5 closed loops. Prim's algorithm identifies the minimum pipeline construction length of 19 units.",
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
        "context": "A medical center installs high-speed data cabling to link 7 critical care units (ER, ICU, OR, Lab, Radiology, Main Server, Switch) across 12 candidate conduit paths forming 5 loops. Prim's algorithm connects all medical units into a minimum spanning tree with a total latency length of 13 ms.",
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
        "context": "An industrial chemical plant connects 7 hazardous material sensors and alarm units to the central control room across 12 candidate wiring channels forming 5 closed loops. Prim's algorithm calculates the minimum total wiring length of 15 units.",
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
        "context": "A telecommunications ISP connects 8 regional internet exchange POPs across 14 candidate fiber trunk routes forming 6 closed loops. Prim's algorithm establishes a minimum spanning backbone requiring 19 units of fiber cabling.",
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
        "context": "A university physical plant department connects 7 academic complexes across 12 candidate utility trenches forming 5 closed loops. Prim's algorithm determines the minimum trenching distance of 16 units required to connect all buildings.",
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
        "context": "An automated e-commerce fulfillment center connects 8 sorting, packing, and dispatch zones across 14 candidate conveyor tracks forming 6 closed loops. Prim's algorithm calculates the minimum total conveyor track length (16 units) to link all warehouse zones.",
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
    </div>

    <!-- Academic References & Primary Citations Footer -->
    <div class="academic-citations-footer" style="margin-top:36px;padding:24px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;">
      <h3 style="font-size:1.02rem;font-weight:700;color:#1b365d;margin-bottom:12px;display:flex;align-items:center;gap:8px;">
        📚 Academic Textbooks & Primary References
      </h3>
      <p style="font-size:.84rem;color:#475569;margin-bottom:14px;line-height:1.6;">
        The problem formulations, decision models, and solution algorithms in this hub are benchmarked against standard graduate operations research literature:
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;">
        <div style="background:#fff;padding:12px 16px;border-radius:6px;border:1px solid #cbd5e1;font-size:.82rem;line-height:1.5;">
          <strong style="color:#0f172a;">1. Hillier, F. S., & Lieberman, G. J.</strong><br/>
          <em>Introduction to Operations Research</em> (11th Ed.). McGraw-Hill Education.<br/>
          <span style="color:#64748b;font-size:.78rem;">Primary reference for Wyndor Glass LPP, Seervada Park Network, Dijkstra, and Prim algorithms.</span>
        </div>
        <div style="background:#fff;padding:12px 16px;border-radius:6px;border:1px solid #cbd5e1;font-size:.82rem;line-height:1.5;">
          <strong style="color:#0f172a;">2. Taha, H. A.</strong><br/>
          <em>Operations Research: An Introduction</em> (10th Ed.). Pearson Prentice Hall.<br/>
          <span style="color:#64748b;font-size:.78rem;">Primary reference for Reddy Mikks LPP, MG Auto Transportation, and Hungarian Assignment Method.</span>
        </div>
        <div style="background:#fff;padding:12px 16px;border-radius:6px;border:1px solid #cbd5e1;font-size:.82rem;line-height:1.5;">
          <strong style="color:#0f172a;">3. Winston, W. L.</strong><br/>
          <em>Operations Research: Applications and Algorithms</em> (4th Ed.). Cengage Learning.<br/>
          <span style="color:#64748b;font-size:.78rem;">Reference for multi-period workforce shift scheduling, diet cost models, and VAM penalty costs.</span>
        </div>
        <div style="background:#fff;padding:12px 16px;border-radius:6px;border:1px solid #cbd5e1;font-size:.82rem;line-height:1.5;">
          <strong style="color:#0f172a;">4. Vohra, N. D.</strong><br/>
          <em>Quantitative Techniques in Management</em> (5th Ed.). McGraw-Hill Education.<br/>
          <span style="color:#64748b;font-size:.78rem;">Reference for managerial optimization models, VAM penalty tests, and line coverage adjustments.</span>
        </div>
      </div>
    </div>`;
}


// ─── LPP SVG GRAPH RENDERER (DYNAMIC EXPANDING AXES) ───────────────────────
function drawLppGraph(g, customZ, activePoint) {
  if (!g) return '';
  const W = 480, H = 340, pad = 45;
  
  // Calculate dynamic axis bounds so graph automatically expands when values/sliders change!
  let maxValX1 = g.maxX1 || 10;
  let maxValX2 = g.maxX2 || 10;
  
  // Expand bounds based on constraint intercepts
  (g.constraints || []).forEach(c => {
    if (c.a1 > 0) { const x1Int = c.b / c.a1; if (x1Int > 0 && x1Int < 1000) maxValX1 = Math.max(maxValX1, x1Int * 1.15); }
    if (c.a2 > 0) { const x2Int = c.b / c.a2; if (x2Int > 0 && x2Int < 1000) maxValX2 = Math.max(maxValX2, x2Int * 1.15); }
  });
  
  // Expand bounds based on custom Z slider
  const optCorner = g.corners ? g.corners.find(c => c.isOpt) || g.corners[0] : null;
  const zVal = customZ !== undefined ? customZ : (optCorner ? optCorner.z : 0);
  if (g.c1 > 0) maxValX1 = Math.max(maxValX1, (zVal / g.c1) * 1.1);
  if (g.c2 > 0) maxValX2 = Math.max(maxValX2, (zVal / g.c2) * 1.1);
  
  // Round up bounds for clean ticks
  const maxX1 = Math.ceil(maxValX1 / 5) * 5 || 10;
  const maxX2 = Math.ceil(maxValX2 / 5) * 5 || 10;
  
  const toX = x => pad + (x / maxX1) * (W - pad - 25);
  const toY = y => (H - pad) - (y / maxX2) * (H - pad - 25);
  
  // 1. Grid & Axes
  let gridSvg = '';
  const xStep = maxX1 / 5, yStep = maxX2 / 5;
  for (let i = 0; i <= 5; i++) {
    const valX = (i * xStep).toFixed(1).replace(/\.0$/, '');
    const valY = (i * yStep).toFixed(1).replace(/\.0$/, '');
    const px = toX(i * xStep), py = toY(i * yStep);
    
    gridSvg += `<line x1="${px}" y1="${pad-10}" x2="${px}" y2="${H-pad}" stroke="#e2e8f0" stroke-dasharray="2,2"/>`;
    gridSvg += `<text x="${px}" y="${H-pad+15}" text-anchor="middle" font-size="10" fill="#64748b" font-weight="600">${valX}</text>`;
    
    gridSvg += `<line x1="${pad}" y1="${py}" x2="${W-15}" y2="${py}" stroke="#e2e8f0" stroke-dasharray="2,2"/>`;
    gridSvg += `<text x="${pad-8}" y="${py+3}" text-anchor="end" font-size="10" fill="#64748b" font-weight="600">${valY}</text>`;
  }
  
  gridSvg += `<line x1="${pad}" y1="${pad-15}" x2="${pad}" y2="${H-pad+5}" stroke="#334155" stroke-width="2.5"/>`;
  gridSvg += `<line x1="${pad-5}" y1="${H-pad}" x2="${W-10}" y2="${H-pad}" stroke="#334155" stroke-width="2.5"/>`;
  gridSvg += `<text x="${W-12}" y="${H-pad-6}" text-anchor="end" font-size="11" font-weight="800" fill="#1b365d">x₁</text>`;
  gridSvg += `<text x="${pad+8}" y="${pad-5}" font-size="11" font-weight="800" fill="#1b365d">x₂</text>`;

  // 2. Feasible Polygon (Shaded area)
  let polygonSvg = '';
  if (g.corners && g.corners.length >= 3) {
    const cx = g.corners.reduce((sum, c) => sum + c.x1, 0) / g.corners.length;
    const cy = g.corners.reduce((sum, c) => sum + c.x2, 0) / g.corners.length;
    const sorted = [...g.corners].sort((a, b) => Math.atan2(a.x2 - cy, a.x1 - cx) - Math.atan2(b.x2 - cy, b.x1 - cx));
    const pointsStr = sorted.map(c => `${toX(c.x1)},${toY(c.x2)}`).join(' ');
    polygonSvg = `<polygon points="${pointsStr}" fill="rgba(34, 197, 94, 0.25)" stroke="#16a34a" stroke-width="2.2" stroke-dasharray="4,2"/>`;
  }

  // 3. Constraint Lines
  let linesSvg = '';
  (g.constraints || []).forEach((c, idx) => {
    let p1, p2;
    if (c.a2 === 0) {
      const xVal = c.b / c.a1;
      p1 = { x: toX(xVal), y: toY(0) };
      p2 = { x: toX(xVal), y: toY(maxX2) };
    } else if (c.a1 === 0) {
      const yVal = c.b / c.a2;
      p1 = { x: toX(0), y: toY(yVal) };
      p2 = { x: toX(maxX1), y: toY(yVal) };
    } else {
      const xInt = c.b / c.a1, yInt = c.b / c.a2;
      p1 = { x: toX(0), y: toY(yInt) };
      p2 = { x: toX(xInt), y: toY(0) };
    }
    const color = c.color || ['#ef4444','#3b82f6','#10b981','#8b5cf6','#f59e0b'][idx % 5];
    linesSvg += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${color}" stroke-width="2.2"/>`;
  });

  // 4. Objective Isoprofit Line
  let isoSvg = '';
  if (g.c1 !== undefined && g.c2 !== undefined && g.c2 !== 0) {
    const yAt0 = zVal / g.c2;
    const yAtMaxX = (zVal - g.c1 * maxX1) / g.c2;
    const ix1 = toX(0), iy1 = toY(yAt0);
    const ix2 = toX(maxX1), iy2 = toY(yAtMaxX);
    isoSvg += `<line x1="${ix1}" y1="${iy1}" x2="${ix2}" y2="${iy2}" stroke="#eab308" stroke-width="3.5" stroke-dasharray="6,4"/>`;
  }

  // 5. Corner Points
  let cornersSvg = '';
  (g.corners || []).forEach(c => {
    const cx = toX(c.x1), cy = toY(c.x2);
    const r = c.isOpt ? 7.5 : 5.5;
    const fill = c.isOpt ? '#16a34a' : '#2563eb';
    const stroke = c.isOpt ? '#fff' : '#1d4ed8';
    
    cornersSvg += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="2"/>`;
    const labelZ = c.z !== undefined ? ` (Z=${c.z.toFixed(1).replace(/\.0$/, '')})` : '';
    cornersSvg += `<text x="${cx+8}" y="${cy-6}" font-size="11" font-weight="800" fill="${c.isOpt?'#15803d':'#1e293b'}">${c.label}${labelZ}</text>`;
  });

  return `
    <div class="lpp-graph-container" style="background:#fff;border:1px solid #cbd5e1;border-radius:8px;padding:14px;margin:14px 0;">
      <div style="font-size:.88rem;font-weight:700;color:#1b365d;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
        📈 Parallel Graphical Solution View (Auto-Scaling Axes: 0 to ${maxX1} x₁)
        <span style="font-size:.75rem;font-weight:600;color:#16a34a;background:#dcfce7;padding:2px 8px;border-radius:4px;margin-left:auto;">Feasible Region & Isoprofit Sweep Line</span>
      </div>
      <svg viewBox="0 0 ${W} ${H}" width="100%" style="max-width:${W}px;display:block;margin:0 auto;background:#f8fafc;border-radius:6px;border:1px solid #e2e8f0;">
        ${gridSvg}
        ${polygonSvg}
        ${linesSvg}
        ${isoSvg}
        ${cornersSvg}
      </svg>
      <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:10px;font-size:.76rem;color:#475569;justify-content:center;">
        <span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;background:rgba(34,197,94,0.3);border:1px solid #16a34a;display:inline-block;border-radius:2px;"></span> Feasible Region</span>
        <span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;background:#16a34a;border-radius:50%;display:inline-block;"></span> Optimal Corner Vertex</span>
        <span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#eab308;display:inline-block;"></span> Objective Line Z (${zVal.toFixed(1)})</span>
      </div>
    </div>
  `;
}

// ─── LPP THEORY SECTION ──────────────────────────────────────────────────────
function renderLppTheory() {
  return `
    <div class="lpp-theory-box" style="background:linear-gradient(135deg,#f0f9ff 0%,#e0f2fe 100%);border:1px solid #7dd3fc;border-radius:8px;padding:18px 22px;margin:16px 0;">
      <h3 style="font-size:1.05rem;font-weight:700;color:#0369a1;margin-bottom:8px;display:flex;align-items:center;gap:8px;">
        🎓 Fundamental Theorem of LPP: Why Solutions MUST Lie on Boundary or Corner Points
      </h3>
      <p style="font-size:.86rem;color:#334155;line-height:1.65;margin-bottom:14px;">
        Students often ask: <em>"Why can't an optimal solution lie strictly inside the interior of the feasible region?"</em> Here is the exact mathematical and visual breakdown:
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;">
        <div style="background:#fff;padding:14px;border-radius:6px;border:1px solid #bae6fd;">
          <h4 style="font-size:.88rem;font-weight:700;color:#0284c7;margin-bottom:4px;">1. The Gradient / Push Intuition</h4>
          <p style="font-size:.82rem;color:#475569;line-height:1.55;">
            Inside an interior point, there is 360° open room in all directions. Moving in the direction of the objective gradient vector <strong>∇Z = (c₁, c₂)</strong> strictly increases Z. Because you can always step further in direction ∇Z without leaving the feasible region, no interior point can ever maximize Z! You keep pushing until you hit a constraint boundary wall.
          </p>
        </div>
        <div style="background:#fff;padding:14px;border-radius:6px;border:1px solid #bae6fd;">
          <h4 style="font-size:.88rem;font-weight:700;color:#0284c7;margin-bottom:4px;">2. Boundary to Corner Sliding</h4>
          <p style="font-size:.82rem;color:#475569;line-height:1.55;">
            Once pushed to a boundary constraint line, you can still slide along that line towards higher Z until you hit a second constraint line. Where two constraint lines intersect is a <strong>Corner Point (Vertex)</strong>. Here, no further feasible movement increases Z, establishing the corner point as optimal!
          </p>
        </div>
        <div style="background:#fff;padding:14px;border-radius:6px;border:1px solid #bae6fd;">
          <h4 style="font-size:.88rem;font-weight:700;color:#0284c7;margin-bottom:4px;">3. Convex Combination Proof</h4>
          <p style="font-size:.82rem;color:#475569;line-height:1.55;">
            Any interior point <strong>x</strong> is a weighted average (convex combination) of the vertices <strong>vᵢ</strong>: x = Σ λᵢ vᵢ. The linear objective Z(x) = Σ λᵢ Z(vᵢ) is a weighted average of vertex values. Since a weighted average can never strictly exceed the maximum component, <strong>max Z(vᵢ) ≥ Z(x)</strong>.
          </p>
        </div>
      </div>
    </div>
  `;
}

// ─── INTERACTIVE LPP BUILDER & PLAYGROUND ─────────────────────────────────────
const builderState = {
  type: 'max', c1: 5, c2: 4,
  constraints: [
    { a1: 6, a2: 4, b: 24, dir: '<=' },
    { a1: 1, a2: 2, b: 6, dir: '<=' }
  ],
  customZ: null
};

function renderLppBuilder() {
  const g = solveBuilderLpp();
  return `
    <div style="background:#fff;border:1px solid #cbd5e1;border-radius:8px;padding:20px;margin:20px 0;">
      <h3 style="font-size:1.15rem;font-weight:700;color:#1b365d;margin-bottom:6px;display:flex;align-items:center;gap:8px;">
        🛠️ Interactive Linear Programming Builder & Sensitivity Playground
      </h3>
      <p style="font-size:.85rem;color:#64748b;margin-bottom:16px;">
        Build custom 2D LPP problems by modifying decision variable coefficients ($c_1, c_2$) and constraints. Watch the feasible region, corner point intersections, and isoprofit sweep line adjust live!
      </p>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;">
        <!-- Controls Column -->
        <div>
          <div style="background:#f8fafc;padding:14px;border-radius:6px;border:1px solid #e2e8f0;margin-bottom:14px;">
            <h4 style="font-size:.9rem;font-weight:700;color:#1e293b;margin-bottom:8px;">1. Objective Function</h4>
            <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px;">
              <select onchange="updateBuilder('type', this.value)" style="padding:6px;border-radius:4px;border:1px solid #cbd5e1;font-weight:700;background:#fff;">
                <option value="max" ${builderState.type==='max'?'selected':''}>Maximize Z</option>
                <option value="min" ${builderState.type==='min'?'selected':''}>Minimize Z</option>
              </select>
              <span>=</span>
              <input type="number" value="${builderState.c1}" onchange="updateBuilder('c1', parseFloat(this.value)|0)" style="width:65px;padding:6px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;font-weight:700;"/>
              <span>x₁ +</span>
              <input type="number" value="${builderState.c2}" onchange="updateBuilder('c2', parseFloat(this.value)|0)" style="width:65px;padding:6px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;font-weight:700;"/>
              <span>x₂</span>
            </div>
          </div>

          <div style="background:#f8fafc;padding:14px;border-radius:6px;border:1px solid #e2e8f0;margin-bottom:14px;">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;">
              <h4 style="font-size:.9rem;font-weight:700;color:#1e293b;">2. Constraints (Subject to:)</h4>
              <button onclick="addBuilderConstraint()" style="background:#2563eb;color:#fff;border:none;border-radius:4px;padding:4px 10px;font-size:.78rem;font-weight:700;cursor:pointer;">+ Add Constraint</button>
            </div>
            ${builderState.constraints.map((c, i) => `
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;flex-wrap:wrap;">
                <input type="number" value="${c.a1}" onchange="updateBuilderConstraint(${i}, 'a1', parseFloat(this.value)|0)" style="width:55px;padding:5px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;"/>
                <span style="font-size:.8rem;">x₁ +</span>
                <input type="number" value="${c.a2}" onchange="updateBuilderConstraint(${i}, 'a2', parseFloat(this.value)|0)" style="width:55px;padding:5px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;"/>
                <span style="font-size:.8rem;">x₂</span>
                <select onchange="updateBuilderConstraint(${i}, 'dir', this.value)" style="padding:5px;border-radius:4px;border:1px solid #cbd5e1;font-weight:700;background:#fff;">
                  <option value="<=" ${c.dir==='<='?'selected':''}>≤</option>
                  <option value=">=" ${c.dir==='>='?'selected':''}>≥</option>
                </select>
                <input type="number" value="${c.b}" onchange="updateBuilderConstraint(${i}, 'b', parseFloat(this.value)|0)" style="width:60px;padding:5px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;font-weight:700;"/>
                ${builderState.constraints.length > 1 ? `<button onclick="removeBuilderConstraint(${i})" style="background:#ef4444;color:#fff;border:none;border-radius:4px;padding:4px 8px;font-size:.75rem;cursor:pointer;margin-left:auto;">✕</button>` : ''}
              </div>`).join('')}
            <div style="font-size:.76rem;color:#64748b;margin-top:6px;">Non-negativity: x₁, x₂ ≥ 0 (implicit)</div>
          </div>

          <!-- Sensitivity Slider -->
          <div style="background:#fef9c3;padding:14px;border-radius:6px;border:1px solid #fde047;">
            <h4 style="font-size:.86rem;font-weight:700;color:#854d0e;margin-bottom:6px;">🎚️ Interactive Isoprofit Line Slider</h4>
            <p style="font-size:.78rem;color:#713f12;margin-bottom:8px;">Drag Z value to sweep objective line across feasible region:</p>
            <input type="range" min="0" max="${(g.optZ*1.4)||50}" step="1" value="${builderState.customZ!==null?builderState.customZ:(g.optZ||0)}" oninput="updateBuilderCustomZ(parseFloat(this.value))" style="width:100%;cursor:pointer;"/>
            <div style="display:flex;justify-content:space-between;font-size:.8rem;font-weight:700;color:#854d0e;margin-top:4px;">
              <span>Current Z: ${builderState.customZ!==null?builderState.customZ:(g.optZ||0)}</span>
              <span>Optimal Z: ${(g.optZ||0).toFixed(1)}</span>
            </div>
          </div>
        </div>

        <!-- Output Graph Column -->
        <div>
          ${drawLppGraph(g, builderState.customZ !== null ? builderState.customZ : undefined)}
          <div style="background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:12px;margin-top:10px;">
            <h4 style="font-size:.86rem;font-weight:700;color:#166534;margin-bottom:4px;">✅ Builder Solution</h4>
            <div style="font-size:.83rem;color:#166534;">
              ${g.optCorner ? `Optimal Point: <strong>${g.optCorner.label} (${g.optCorner.x1.toFixed(2)}, ${g.optCorner.x2.toFixed(2)})</strong><br/>Optimal Z = <strong>${g.optZ.toFixed(2)}</strong>` : 'No feasible solution found with current constraints.'}
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}

function updateBuilder(key, val) { builderState[key] = val; builderState.customZ = null; renderApp(); }
function updateBuilderConstraint(i, key, val) { builderState.constraints[i][key] = val; builderState.customZ = null; renderApp(); }
function addBuilderConstraint() { builderState.constraints.push({ a1: 1, a2: 1, b: 10, dir: '<=' }); builderState.customZ = null; renderApp(); }
function removeBuilderConstraint(i) { builderState.constraints.splice(i, 1); builderState.customZ = null; renderApp(); }
function updateBuilderCustomZ(val) { builderState.customZ = val; renderApp(); }

function solveBuilderLpp() {
  const lines = builderState.constraints.map((c, idx) => ({
    a1: c.a1, a2: c.a2, b: c.b, dir: c.dir, label: `${c.a1}x₁ + ${c.a2}x₂ ${c.dir==='<='?'≤':'≥'} ${c.b}`,
    color: ['#ef4444','#3b82f6','#10b981','#8b5cf6','#f59e0b'][idx % 5]
  }));
  
  // Find all pairwise line intersections + axes
  const pts = [{ x1: 0, x2: 0 }];
  const allLines = [...lines, { a1: 1, a2: 0, b: 0, dir: '>=' }, { a1: 0, a2: 1, b: 0, dir: '>=' }];
  
  for (let i = 0; i < allLines.length; i++) {
    for (let j = i + 1; j < allLines.length; j++) {
      const l1 = allLines[i], l2 = allLines[j];
      const det = l1.a1 * l2.a2 - l1.a2 * l2.a1;
      if (Math.abs(det) > 1e-6) {
        const x1 = (l1.b * l2.a2 - l1.a2 * l2.b) / det;
        const x2 = (l1.a1 * l2.b - l1.b * l2.a1) / det;
        if (x1 >= -1e-4 && x2 >= -1e-4) {
          pts.push({ x1: Math.max(0, x1), x2: Math.max(0, x2) });
        }
      }
    }
  }
  
  // Filter feasible points
  const feasible = pts.filter(p => {
    return lines.every(c => {
      const val = c.a1 * p.x1 + c.a2 * p.x2;
      return c.dir === '<=' ? val <= c.b + 1e-4 : val >= c.b - 1e-4;
    });
  });
  
  // Unique corners
  const corners = [];
  const labels = ['O','A','B','C','D','E','F','G'];
  let maxX1 = 5, maxX2 = 5;
  
  feasible.forEach((p) => {
    if (!corners.some(c => Math.abs(c.x1 - p.x1) < 1e-3 && Math.abs(c.x2 - p.x2) < 1e-3)) {
      const z = builderState.c1 * p.x1 + builderState.c2 * p.x2;
      corners.push({ label: labels[corners.length % labels.length], x1: p.x1, x2: p.x2, z: z, isOpt: false });
      if (p.x1 > maxX1) maxX1 = p.x1;
      if (p.x2 > maxX2) maxX2 = p.x2;
    }
  });
  
  // Determine optimal corner
  let optZ = builderState.type === 'max' ? -Infinity : Infinity;
  let optCorner = null;
  corners.forEach(c => {
    if (builderState.type === 'max' ? c.z > optZ : c.z < optZ) {
      optZ = c.z; optCorner = c;
    }
  });
  if (optCorner) optCorner.isOpt = true;
  
  return {
    type: builderState.type, c1: builderState.c1, c2: builderState.c2,
    constraints: lines, corners: corners, optCorner: optCorner, optZ: optZ || 0,
    maxX1: Math.ceil(maxX1 * 1.3), maxX2: Math.ceil(maxX2 * 1.3)
  };
}


// PROBLEM LIST
function renderProblemList(mod) {
  const filtered = state.difficultyFilter === 'all' ? mod.problems : mod.problems.filter(p => p.difficulty === state.difficultyFilter);
  if (mod.id === 'lpp') {
    return `
      <button class="back-btn" onclick="gotoTab('home')">← Back to Modules</button>
      <div class="sec-title">${mod.icon} ${mod.title}</div>
      <p class="sec-desc">${mod.desc}</p>
      ${renderLppTheory()}
      ${renderLppBuilder()}
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
  const graphHtml = p.graph ? drawLppGraph(p.graph) : '';
  const stepsHtml = (p.steps||[]).map((s,i) => {
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
  return stepsHtml + graphHtml;
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
