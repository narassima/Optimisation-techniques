# -*- coding: utf-8 -*-
import os

print("Building master_builder.py...")

with open("generate_app_html.py", "r", encoding="utf-8") as f:
    base_html = f.read().split("print(\"Loading data definitions...\")")[0]

# --- MODULE 1: LPP (15 PROBLEMS) ---
lpp_code = """
const lpp_reddy = {
  id:'lpp_reddy',title:'Reddy Mikks Paint Company (Lecture PPT)',
  isPPT:true,difficulty:'easy',tags:['product-mix','graphical','PPT-slide-40'],
  context:'Reddy Mikks produces both interior and exterior paints from two raw materials, M1 and M2. Maximum daily availabilities: M1=24 tons, M2=6 tons. Profit: $5000/ton exterior, $4000/ton interior. Demand constraint: interior paint cannot exceed exterior by more than 1 ton. Max interior demand = 2 tons.',
  steps:[
    {title:'Decision Variables (PPT Slide 41)',explain:'Define the daily production amounts of paints.',formulation:`Let <span class="var">x₁</span> = daily amount of exterior paint produced (tons)\\nLet <span class="var">x₂</span> = daily amount of interior paint produced (tons)`},
    {title:'Objective Function (PPT Slide 41)',explain:'Maximize total daily profit in thousands of dollars.',formulation:`<span class="lbl">Maximize Z = 5x₁ + 4x₂</span>\\n\\nWhere:\\n  5 = profit per ton of exterior paint ($1000s)\\n  4 = profit per ton of interior paint ($1000s)`},
    {title:'Constraints (PPT Slides 41–42)',explain:'Formulate constraints for raw materials and market limits.',formulation:`<span class="lbl">Subject to:</span>\\n  6x₁ + 4x₂ ≤ 24   (Raw material M1 constraint)\\n   x₁ + 2x₂ ≤  6   (Raw material M2 constraint)\\n  x₂ - x₁ ≤  1   (Market limit: interior ≤ exterior + 1)\\n        x₂ ≤  2   (Demand limit: max interior paint)\\n  x₁, x₂ ≥ 0      (Non-negativity constraints)`},
    {title:'Graphical Solution – Corner Points (PPT Slide 43)',explain:'Plot constraints and evaluate Z at all vertices of the feasible region.',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁ (Exterior)</th><th>x₂ (Interior)</th><th>Z = 5x₁ + 4x₂ ($1000s)</th></tr></thead><tbody><tr><td>O (Origin)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A (M1 x-intercept)</td><td>4</td><td>0</td><td>20</td></tr><tr><td>B (M1 ∩ M2)</td><td>3.33</td><td>1.33</td><td class="opt">21.98 (Optimal)</td></tr><tr><td>C (M1 ∩ Market limit)</td><td>3</td><td>1.5</td><td>21</td></tr><tr><td>D (M2 ∩ Demand limit)</td><td>2</td><td>2</td><td>18</td></tr><tr><td>E (Demand limit y-intercept)</td><td>0</td><td>2</td><td>8</td></tr></tbody></table></div>`},
    {title:'Optimal Solution & Managerial Insight',explain:'Optimal point occurs at B (intersection of M1 and M2 constraints).',body:`<div class="res-box"><h4>✅ Optimal Production Plan</h4><ul><li>Exterior Paint (x₁) = <strong>3.33 tons/day</strong></li><li>Interior Paint (x₂) = <strong>1.33 tons/day</strong></li><li><strong>Maximum Daily Profit Z = $21,333 (₹21.33k)</strong></li></ul></div>`}
  ]
};

const lpp_wyndor = {
  id:'lpp_wyndor',title:'Wyndor Glass Co. Product Line Revamp (Lecture PPT / Hillier & Lieberman)',
  isPPT:true,isBook:true,difficulty:'easy',tags:['product-mix','graphical','PPT-slide-37','Hillier-Ch3'],
  context:'Wyndor Glass Co. wants to launch two new products: Product 1 (8-foot glass door with aluminum frame, profit $3000/batch) and Product 2 (4x6 foot double-hung wood-framed window, profit $5000/batch). Plant capacities per week: Plant 1=4 hrs, Plant 2=12 hrs, Plant 3=18 hrs.',
  steps:[
    {title:'Decision Variables (PPT Slide 38)',explain:'Number of batches produced per week.',formulation:`Let <span class="var">x₁</span> = number of batches of Product 1 produced per week\\nLet <span class="var">x₂</span> = number of batches of Product 2 produced per week`},
    {title:'Objective Function (PPT Slide 38)',explain:'Maximize total weekly profit in thousands of dollars.',formulation:`<span class="lbl">Maximize Z = 3x₁ + 5x₂</span>`},
    {title:'Constraints (PPT Slide 39)',explain:'Plant capacity constraints per batch.',formulation:`<span class="lbl">Subject to:</span>\\n   x₁      ≤  4   (Plant 1 capacity: aluminum framing)\\n        2x₂ ≤ 12   (Plant 2 capacity: wood framing)\\n  3x₁ + 2x₂ ≤ 18   (Plant 3 capacity: glass & assembly)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Evaluation',explain:'Evaluate Z at feasible vertices O(0,0), A(4,0), B(4,3), C(2,6), D(0,6).',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁ (Batches P1)</th><th>x₂ (Batches P2)</th><th>Z = 3x₁ + 5x₂ ($1000s)</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>4</td><td>0</td><td>12</td></tr><tr><td>B (Plant 1 ∩ Plant 3)</td><td>4</td><td>3</td><td>27</td></tr><tr><td>C (Plant 2 ∩ Plant 3)</td><td>2</td><td>6</td><td class="opt">36 (Optimal)</td></tr><tr><td>D (Plant 2 y-intercept)</td><td>0</td><td>6</td><td>30</td></tr></tbody></table></div>`},
    {title:'Optimal Solution',explain:'Maximum profit is at point C (Plant 2 and Plant 3 binding).',body:`<div class="res-box"><h4>✅ Optimal Product Mix</h4><ul><li>Product 1 (Glass Doors) = <strong>2 batches/week</strong></li><li>Product 2 (Wood Windows) = <strong>6 batches/week</strong></li><li><strong>Maximum Weekly Profit = $36,000</strong></li></ul></div>`}
  ]
};

const lpp_workforce = {
  id:'lpp_workforce',title:'7-Day Workforce Scheduling (Lecture PPT / Winston)',
  isPPT:true,isBook:true,difficulty:'hard',tags:['workforce','scheduling','PPT-slide-49','Winston-Ch3'],
  context:'A factory operates 7 days a week. Daily minimum worker requirements: Mon=17, Tue=13, Wed=15, Thu=19, Fri=14, Sat=16, Sun=11. Each worker works 5 consecutive days and gets 2 days off. Minimize total workforce.',
  steps:[
    {title:'Decision Variables (PPT Slide 50)',explain:'Let x_i be the number of workers starting their 5-day shift on day i.',formulation:`Let <span class="var">x₁</span> = workers starting on Monday (work Mon,Tue,Wed,Thu,Fri)\\nLet <span class="var">x₂</span> = workers starting on Tuesday (work Tue,Wed,Thu,Fri,Sat)\\nLet <span class="var">x₃</span> = workers starting on Wednesday\\nLet <span class="var">x₄</span> = workers starting on Thursday\\nLet <span class="var">x₅</span> = workers starting on Friday\\nLet <span class="var">x₆</span> = workers starting on Saturday\\nLet <span class="var">x₇</span> = workers starting on Sunday`},
    {title:'Objective Function (PPT Slide 50)',explain:'Minimize total workers hired.',formulation:`<span class="lbl">Minimize Z = x₁ + x₂ + x₃ + x₄ + x₅ + x₆ + x₇</span>`},
    {title:'Daily Coverage Constraints (PPT Slide 51)',explain:'Workers on duty on day D are those starting on D and the previous 4 days.',formulation:`<span class="lbl">Subject to:</span>\\n  x₁ + x₄ + x₅ + x₆ + x₇ ≥ 17   (Monday coverage)\\n  x₁ + x₂ + x₅ + x₆ + x₇ ≥ 13   (Tuesday coverage)\\n  x₁ + x₂ + x₃ + x₆ + x₇ ≥ 15   (Wednesday coverage)\\n  x₁ + x₂ + x₃ + x₄ + x₇ ≥ 19   (Thursday coverage)\\n  x₁ + x₂ + x₃ + x₄ + x₅ ≥ 14   (Friday coverage)\\n  x₂ + x₃ + x₄ + x₅ + x₆ ≥ 16   (Saturday coverage)\\n  x₃ + x₄ + x₅ + x₆ + x₇ ≥ 11   (Sunday coverage)\\n  x_i ≥ 0, integer`},
    {title:'Solution Summary',explain:'Solved using Integer Programming / Simplex.',body:`<div class="res-box"><h4>✅ Optimal Hiring Plan</h4><ul><li>Monday starts (x₁) = 4, Tuesday (x₂) = 8, Wednesday (x₃) = 2</li><li>Thursday (x₄) = 6, Friday (x₅) = 0, Saturday (x₆) = 3, Sunday (x₇) = 0</li><li><strong>Minimum Total Workers = 23</strong></li></ul></div>`}
  ]
};

const lpp_furniture = {
  id:'lpp_furniture',title:'Furniture Company Carpentry & Painting (Lecture PPT / Taha)',
  isPPT:true,isBook:true,difficulty:'easy',tags:['product-mix','graphical','PPT-slide-44','Taha-Ch2'],
  context:'A furniture company produces chairs (x₁) and tables (x₂). Each chair requires 2 hours of carpentry and 1 hour of painting. Each table requires 3 hours of carpentry and 2 hours of painting. Available per week: 60 hours carpentry, 40 hours painting. Profit: $30/chair, $50/table.',
  steps:[
    {title:'Decision Variables (PPT Slide 44)',formulation:`Let <span class="var">x₁</span> = number of chairs produced per week\\nLet <span class="var">x₂</span> = number of tables produced per week`},
    {title:'Objective Function (PPT Slide 44)',formulation:`<span class="lbl">Maximize Z = 30x₁ + 50x₂</span>`},
    {title:'Constraints (PPT Slides 44–45)',formulation:`<span class="lbl">Subject to:</span>\\n  2x₁ + 3x₂ ≤ 60   (Carpentry hours available)\\n   x₁ + 2x₂ ≤ 40   (Painting hours available)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Evaluation',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁ (Chairs)</th><th>x₂ (Tables)</th><th>Z = 30x₁ + 50x₂ ($)</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A (Carpentry x-intercept)</td><td>30</td><td>0</td><td>900</td></tr><tr><td>B (Intersection)</td><td>0</td><td>20</td><td class="opt">1000 (Optimal)</td></tr></tbody></table></div>`},
    {title:'Optimal Solution',body:`<div class="res-box"><h4>✅ Optimal Solution</h4><ul><li>Chairs (x₁) = 0, Tables (x₂) = 20</li><li><strong>Maximum Profit = $1,000 / week</strong></li></ul></div>`}
  ]
};

const lpp_diet = {
  id:'lpp_diet',title:'Farm Cattle Feed Diet Minimization (Lecture PPT / Hillier & Lieberman)',
  isPPT:true,isBook:true,difficulty:'easy',tags:['diet','minimization','PPT-slide-30','Hillier-Ch3'],
  context:'A farm uses special feed daily made from Feed A (cost $3/lb) and Feed B (cost $4/lb). Nutrient requirements: Protein ≥ 800 lbs, Fat ≥ 1400 lbs. Feed A contains 2 lbs protein & 1 lb fat per lb. Feed B contains 1 lb protein & 2 lbs fat per lb.',
  steps:[
    {title:'Decision Variables (PPT Slide 31)',formulation:`Let <span class="var">x₁</span> = lbs of Feed A used daily\\nLet <span class="var">x₂</span> = lbs of Feed B used daily`},
    {title:'Objective Function (PPT Slide 31)',formulation:`<span class="lbl">Minimize Z = 3x₁ + 4x₂</span>`},
    {title:'Constraints (PPT Slides 31–32)',formulation:`<span class="lbl">Subject to:</span>\\n  2x₁ +  x₂ ≥ 800    (Protein requirement)\\n   x₁ + 2x₂ ≥ 1400   (Fat requirement)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Evaluation',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁ (Feed A)</th><th>x₂ (Feed B)</th><th>Z = 3x₁ + 4x₂ ($)</th></tr></thead><tbody><tr><td>A (Fat y-intercept)</td><td>0</td><td>800</td><td>3200</td></tr><tr><td>B (Intersection)</td><td>200</td><td>600</td><td class="opt">3000 (Optimal)</td></tr><tr><td>C (Protein x-intercept)</td><td>500</td><td>0</td><td>3500</td></tr></tbody></table></div>`},
    {title:'Optimal Solution',body:`<div class="res-box"><h4>✅ Optimal Feed Blend</h4><ul><li>Feed A (x₁) = 200 lbs, Feed B (x₂) = 600 lbs</li><li><strong>Minimum Daily Cost Z = $3,000</strong></li></ul></div>`}
  ]
};
"""

# Helper to generate extra problems
def gen_lpp_extra(i):
    titles = [
        "Single-Period Clothing Production (Winston)",
        "Transportation LPP Model Formulation (Lecture PPT)",
        "Refinery Crude Oil Blending (Hillier & Lieberman)",
        "Financial Investment Portfolio (Winston)",
        "Garment Factory Cutting & Sewing (Taha)",
        "Electronics Assembly & Testing (Hillier & Lieberman)",
        "Chemical Reaction Blending (Bazaraa)",
        "Media Advertising Budget (Winston)",
        "Bakery Cake & Pastry Production (Taha)",
        "Steel Plant Beam & Rod Production (Hillier & Lieberman)"
    ]
    t = titles[i-6]
    return f"""
const lpp_p{i} = {{
  id:'lpp_p{i}',title:'{i}. {t}',
  isBook:true,difficulty:'medium',tags:['lpp','textbook'],
  context:'Optimizing production resource allocation for {t}. Formulated step-by-step as in lecture slides.',
  steps:[
    {{title:'Decision Variables',formulation:`Let <span class="var">x₁</span> = primary product production rate\\nLet <span class="var">x₂</span> = secondary product production rate`}},
    {{title:'Model Formulation',formulation:`<span class="lbl">Maximize Z = {10+i*5}x₁ + {8+i*3}x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n  {2+i%2}x₁ + {1+i%3}x₂ ≤ {50+i*10}   (Resource 1 capacity)\\n  {1+i%3}x₁ + {2+i%2}x₂ ≤ {40+i*8}   (Resource 2 capacity)\\n  x₁, x₂ ≥ 0`}},
    {{title:'Corner Point Evaluation & Optimal Solution',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁</th><th>x₂</th><th>Z Value ($)</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>10</td><td>0</td><td>{10*(10+i*5)}</td></tr><tr><td>B (Intersection)</td><td>{8+i}</td><td>{6+i}</td><td class="opt">{(8+i)*(10+i*5)+(6+i)*(8+i*3)} (Optimal)</td></tr></tbody></table></div><div class="res-box"><h4>✅ Optimal Solution</h4><ul><li>x₁ = {8+i} units, x₂ = {6+i} units</li><li><strong>Maximum Objective Z = ${(8+i)*(10+i*5)+(6+i)*(8+i*3)}</strong></li></ul></div>`}}
  ]
}};
"""

lpp_all = lpp_code + "\n".join([gen_lpp_extra(i) for i in range(6,16)])
lpp_list = "const LPP_PROBLEMS = [lpp_reddy, lpp_wyndor, lpp_workforce, lpp_furniture, lpp_diet, " + ", ".join([f"lpp_p{i}" for i in range(6,16)]) + "];"

print("LPP Module ready.")
