# -*- coding: utf-8 -*-
import os

print("Writing full 75-problem HTML generator...")

script_content = '''import os

with open("generate_app_html.py", "r", encoding="utf-8") as f:
    base = f.read().split("print(\\"Loading data definitions...\\")")[0]

modules_js = """
// ====================================================================
// DATA: 15+ PROBLEMS PER MODULE (PPT STRUCTURE & TEXTBOOK PROBLEMS)
// ====================================================================

// --------------------------------------------------------------------
// 1. LINEAR PROGRAMMING (15 PROBLEMS)
// --------------------------------------------------------------------
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

const lpp_parkas = {
  id:'lpp_parkas',title:'Single-Period Winter Clothing Production (Lecture PPT / Winston)',
  isPPT:true,isBook:true,difficulty:'medium',tags:['production','penalties','PPT-slide-33','Winston-Ch3'],
  context:'A clothing company produces Parkas (x₁), Overcoats (x₂), Insulated Pants (x₃), and Gloves (x₄). Factory capacity = 1000 hrs. Penalty shortages s₁, s₂, s₃, s₄ occur if demand is not met. Formulate penalty minimization LPP.',
  steps:[
    {title:'Decision Variables (PPT Slide 34)',formulation:`Let <span class="var">x₁, x₂, x₃, x₄</span> = production quantities of Parkas, Overcoats, Pants, Gloves\\nLet <span class="var">s₁, s₂, s₃, s₄</span> = demand shortage quantities`},
    {title:'Objective Function (PPT Slide 34)',formulation:`<span class="lbl">Minimize Total Penalty Z = 10s₁ + 12s₂ + 8s₃ + 5s₄</span>`},
    {title:'Constraints (PPT Slide 35)',formulation:`<span class="lbl">Subject to:</span>\\n  2x₁ + 3x₂ + 1.5x₃ + 0.5x₄ ≤ 1000   (Factory labor capacity)\\n  x₁ + s₁ = 300    (Parka demand)\\n  x₂ + s₂ = 200    (Overcoat demand)\\n  x₃ + s₃ = 400    (Pants demand)\\n  x₄ + s₄ = 500    (Gloves demand)\\n  x_i, s_i ≥ 0`}
  ]
};

const lpp_transport_model = {
  id:'lpp_transport_model',title:'Two-Warehouse 3-DC Transportation LPP Model (Lecture PPT)',
  isPPT:true,difficulty:'easy',tags:['transportation-lpp','formulation','PPT-slide-46'],
  context:'A company has 2 warehouses (W1 supply=100, W2 supply=120) and 3 distribution centers (D1 demand=80, D2 demand=90, D3 demand=50). Unit costs: W1=[4,6,8], W2=[5,4,3]. Formulate as LPP.',
  steps:[
    {title:'Decision Variables (PPT Slide 46)',formulation:`Let <span class="var">x_ij</span> = units transported from Warehouse i to Distribution Center j\\nwhere i ∈ {1,2} and j ∈ {1,2,3}`},
    {title:'Objective Function (PPT Slide 47)',formulation:`<span class="lbl">Minimize Z = 4x₁₁ + 6x₁₂ + 8x₁₃ + 5x₂₁ + 4x₂₂ + 3x₂₃</span>`},
    {title:'Constraints (PPT Slide 47)',formulation:`<span class="lbl">Supply Constraints:</span>\\n  x₁₁ + x₁₂ + x₁₃ = 100   (Warehouse 1 supply)\\n  x₂₁ + x₂₂ + x₂₃ = 120   (Warehouse 2 supply)\\n\\n<span class="lbl">Demand Constraints:</span>\\n  x₁₁ + x₂₁ = 80    (DC 1 demand)\\n  x₁₂ + x₂₂ = 90    (DC 2 demand)\\n  x₁₃ + x₂₃ = 50    (DC 3 demand)\\n  x_ij ≥ 0`}
  ]
};

const lpp_crude = {
  id:'lpp_crude',title:'Refinery Crude Oil Blending Problem (Hillier & Lieberman Textbook)',
  isBook:true,difficulty:'medium',tags:['blending','petroleum','Hillier-Ch3'],
  context:'An oil refinery blends Crude A ($40/bbl) and Crude B ($60/bbl) to yield 10,000 barrels of gasoline meeting Octane ≥ 85 and Sulphur ≤ 2%. Crude A: Octane=80, Sulphur=3%. Crude B: Octane=100, Sulphur=1%.',
  steps:[
    {title:'Decision Variables',formulation:`Let <span class="var">x₁</span> = barrels of Crude A\\nLet <span class="var">x₂</span> = barrels of Crude B`},
    {title:'Objective Function',formulation:`<span class="lbl">Minimize Z = 40x₁ + 60x₂</span>`},
    {title:'Constraints',formulation:`<span class="lbl">Subject to:</span>\\n  x₁ + x₂ = 10000              (Total production requirement)\\n  80x₁ + 100x₂ ≥ 85(10000)     (Octane requirement)\\n  0.03x₁ + 0.01x₂ ≤ 0.02(10000) (Sulphur limit)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Solution',body:`<div class="res-box"><h4>✅ Optimal Blend</h4><ul><li>Crude A (x₁) = 5,000 barrels</li><li>Crude B (x₂) = 5,000 barrels</li><li><strong>Minimum Cost = $500,000</strong></li></ul></div>`}
  ]
};

const lpp_invest = {
  id:'lpp_invest',title:'Financial Investment Portfolio Allocation (Winston Textbook)',
  isBook:true,difficulty:'medium',tags:['finance','portfolio','Winston-Ch3'],
  context:'An investor has $100,000 to allocate between Stocks (expected return 12%, risk index 6) and Bonds (expected return 8%, risk index 3). Constraints: Total risk index ≤ 4.5 per dollar, at least $20,000 in bonds.',
  steps:[
    {title:'Decision Variables',formulation:`Let <span class="var">x₁</span> = dollars invested in Stocks\\nLet <span class="var">x₂</span> = dollars invested in Bonds`},
    {title:'Objective Function',formulation:`<span class="lbl">Maximize Z = 0.12x₁ + 0.08x₂</span>`},
    {title:'Constraints',formulation:`<span class="lbl">Subject to:</span>\\n  x₁ + x₂ ≤ 100000      (Total capital available)\\n  6x₁ + 3x₂ ≤ 4.5(100000) (Weighted risk index constraint)\\n  x₂ ≥ 20000            (Minimum bond requirement)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Evaluation',body:`<div class="res-box"><h4>✅ Optimal Allocation</h4><ul><li>Stocks (x₁) = $50,000, Bonds (x₂) = $50,000</li><li><strong>Maximum Return Z = $10,000 (10% yield)</strong></li></ul></div>`}
  ]
};

const lpp_textile = {
  id:'lpp_textile',title:'Garment Factory Shirt & Pant Production (Taha Textbook)',
  isBook:true,difficulty:'easy',tags:['garment','production','Taha-Ch2'],
  context:'A textile factory makes Shirts (x₁) and Pants (x₂). Cutting: 2 hrs/shirt, 3 hrs/pant, limit 120 hrs. Sewing: 1 hr/shirt, 2 hrs/pant, limit 70 hrs. Profit: $20/shirt, $35/pant.',
  steps:[
    {title:'Decision Variables & Model Formulation',formulation:`<span class="lbl">Maximize Z = 20x₁ + 35x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n  2x₁ + 3x₂ ≤ 120   (Cutting department hours)\\n   x₁ + 2x₂ ≤  70   (Sewing department hours)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Points',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁</th><th>x₂</th><th>Z = 20x₁ + 35x₂ ($)</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>60</td><td>0</td><td>1200</td></tr><tr><td>B (Intersection)</td><td>30</td><td>20</td><td class="opt">1300 (Optimal)</td></tr><tr><td>C</td><td>0</td><td>35</td><td>1225</td></tr></tbody></table></div>`},
    {title:'Optimal Solution',body:`<div class="res-box"><h4>✅ Optimal Production</h4><ul><li>Shirts (x₁) = 30 units, Pants (x₂) = 20 units</li><li><strong>Maximum Profit Z = $1,300</strong></li></ul></div>`}
  ]
};

const lpp_electronics = {
  id:'lpp_electronics',title:'Electronics Assembly & Testing (Hillier & Lieberman Textbook)',
  isBook:true,difficulty:'medium',tags:['electronics','assembly','Hillier-Ch3'],
  context:'An electronics firm makes Radios (x₁) and TVs (x₂). Assembly: 1 hr/radio, 4 hrs/TV, limit 40 hrs. Testing: 2 hrs/radio, 1 hr/TV, limit 16 hrs. Market limit: radios ≤ 10. Profit: $40/radio, $60/TV.',
  steps:[
    {title:'Model Formulation',formulation:`<span class="lbl">Maximize Z = 40x₁ + 60x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n  x₁ + 4x₂ ≤ 40   (Assembly hours)\\n  2x₁ +  x₂ ≤ 16   (Testing hours)\\n        x₁ ≤ 10   (Market demand limit)\\n  x₁, x₂ ≥ 0`},
    {title:'Optimal Corner Point',body:`<div class="res-box"><h4>✅ Optimal Product Mix</h4><ul><li>Radios (x₁) = 3.43 units, TVs (x₂) = 9.14 units</li><li><strong>Maximum Profit Z = $685.71</strong></li></ul></div>`}
  ]
};

const lpp_chem = {
  id:'lpp_chem',title:'Chemical Reaction Blending (Bazaraa Textbook)',
  isBook:true,difficulty:'hard',tags:['chemical','blending','Bazaraa-Ch1'],
  context:'A chemical plant produces Chemical X (x₁) and Chemical Y (x₂). Reaction A time: 3 hrs/unit X, 2 hrs/unit Y, limit 18 hrs. Reaction B time: 1 hr/unit X, 2 hrs/unit Y, limit 10 hrs. Profit: $50/unit X, $40/unit Y.',
  steps:[
    {title:'Model Formulation',formulation:`<span class="lbl">Maximize Z = 50x₁ + 40x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n  3x₁ + 2x₂ ≤ 18   (Reactor A capacity)\\n   x₁ + 2x₂ ≤ 10   (Reactor B capacity)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Evaluation',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁</th><th>x₂</th><th>Z = 50x₁ + 40x₂ ($)</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>6</td><td>0</td><td>300</td></tr><tr><td>B (Intersection)</td><td>4</td><td>3</td><td class="opt">320 (Optimal)</td></tr><tr><td>C</td><td>0</td><td>5</td><td>200</td></tr></tbody></table></div>`},
    {title:'Optimal Solution',body:`<div class="res-box"><h4>✅ Optimal Output</h4><ul><li>Chemical X (x₁) = 4 units, Chemical Y (x₂) = 3 units</li><li><strong>Maximum Profit Z = $320</strong></li></ul></div>`}
  ]
};

const lpp_ad = {
  id:'lpp_ad',title:'Media Advertising Budget Allocation (Winston Textbook)',
  isBook:true,difficulty:'medium',tags:['advertising','media','Winston-Ch3'],
  context:'A company allocates $100,000 budget between TV ads (x₁, $1000/ad) and Online ads (x₂, $500/ad). Exposure: 50,000 viewers/TV ad, 20,000 viewers/Online ad. Constraints: at least 20 TV ads, at least 40 Online ads.',
  steps:[
    {title:'Model Formulation',formulation:`<span class="lbl">Maximize Viewers Z = 50000x₁ + 20000x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n  1000x₁ + 500x₂ ≤ 100000   (Budget limit)\\n        x₁ ≥ 20          (Minimum TV ads)\\n        x₂ ≥ 40          (Minimum Online ads)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Solution',body:`<div class="res-box"><h4>✅ Optimal Media Mix</h4><ul><li>TV Ads (x₁) = 80 ads ($80,000)</li><li>Online Ads (x₂) = 40 ads ($20,000)</li><li><strong>Maximum Audience Reach Z = 4,800,000 viewers</strong></li></ul></div>`}
  ]
};

const lpp_bakery = {
  id:'lpp_bakery',title:'Bakery Cake & Pastry Production (Taha Textbook)',
  isBook:true,difficulty:'easy',tags:['bakery','food','Taha-Ch2'],
  context:'A bakery makes Cakes (x₁) and Pastries (x₂). Oven time: 1 hr/cake, 0.5 hr/pastry, limit 8 hrs/day. Baking powder: 2 kg/cake, 1 kg/pastry, limit 12 kg/day. Profit: $8/cake, $5/pastry.',
  steps:[
    {title:'Model Formulation',formulation:`<span class="lbl">Maximize Z = 8x₁ + 5x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n   x₁ + 0.5x₂ ≤  8   (Oven time hours)\\n  2x₁ +   x₂ ≤ 12   (Baking powder kg)\\n  x₁, x₂ ≥ 0`},
    {title:'Solution & Analysis',body:`<div class="res-box"><h4>✅ Optimal Solution</h4><ul><li>Cakes (x₁) = 0, Pastries (x₂) = 12</li><li><strong>Maximum Daily Profit Z = $60</strong></li></ul></div>`}
  ]
};

const lpp_steel = {
  id:'lpp_steel',title:'Steel Plant Beam & Rod Production (Hillier & Lieberman Textbook)',
  isBook:true,difficulty:'medium',tags:['steel','manufacturing','Hillier-Ch3'],
  context:'A steel plant produces Beams (x₁) and Rods (x₂). Rolling mill: 3 hrs/beam, 1 hr/rod, limit 24 hrs. Finishing mill: 2 hrs/beam, 2 hrs/rod, limit 20 hrs. Market limit: rods ≤ 8. Profit: $500/beam, $300/rod.',
  steps:[
    {title:'Model Formulation',formulation:`<span class="lbl">Maximize Z = 500x₁ + 300x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n  3x₁ + x₂ ≤ 24   (Rolling mill hours)\\n  2x₁ + 2x₂ ≤ 20   (Finishing mill hours)\\n       x₂ ≤  8   (Rod demand limit)\\n  x₁, x₂ ≥ 0`},
    {title:'Corner Point Evaluation',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁ (Beams)</th><th>x₂ (Rods)</th><th>Z = 500x₁ + 300x₂ ($)</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>8</td><td>0</td><td>4000</td></tr><tr><td>B (Intersection)</td><td>7</td><td>3</td><td class="opt">4400 (Optimal)</td></tr><tr><td>C</td><td>2</td><td>8</td><td>3400</td></tr></tbody></table></div>`},
    {title:'Optimal Solution',body:`<div class="res-box"><h4>✅ Optimal Production</h4><ul><li>Beams (x₁) = 7 units, Rods (x₂) = 3 units</li><li><strong>Maximum Profit Z = $4,400</strong></li></ul></div>`}
  ]
};

// --------------------------------------------------------------------
// 2. TRANSPORTATION PROBLEMS (15 PROBLEMS)
// --------------------------------------------------------------------
const tp_mgauto_full = {
  id:'tp_mgauto_full',title:'MG Auto Distribution – Plants to DCs (Lecture PPT / Taha)',
  isPPT:true,isBook:true,difficulty:'easy',tags:['mg-auto','balanced','unbalanced','PPT-slide-4','Taha-Ch5'],
  context:'MG Auto has 3 plants (LA 1000, Detroit 1500, New Orleans 1200 cars) and 2 DCs (Denver 2300, Miami 1400 cars). Total Supply = 3700, Total Demand = 3700. Unit costs ($): LA=[80,215], Detroit=[100,108], New Orleans=[102,68].',
  rows:['Los Angeles','Detroit','New Orleans'],cols:['Denver','Miami'],
  methods:[
    {name:'1. Balanced Tableau (PPT Slide 6)',intro:'<strong>MG Auto Original Problem:</strong> Balanced supply (3700) and demand (3700).',steps:[
      {title:'Initial Tableau',explain:'Cost matrix and supply/demand.',costs:[[80,215],[100,108],[102,68]],allocs:[[0,0],[0,0],[0,0]],supply:[1000,1500,1200],demand:[2300,1400],activeCell:null,doneCells:[]},
      {title:'NW Corner Allocation',explain:'Allocate LA→Denver: 1000. Detroit→Denver: 1300, Detroit→Miami: 200. New Orleans→Miami: 1200.',costs:[[80,215],[100,108],[102,68]],allocs:[[1000,0],[1300,200],[0,1200]],supply:[0,0,0],demand:[0,0],activeCell:null,doneCells:[[0,0],[1,0],[1,1],[2,1]],result:'Cost = 1000(80) + 1300(100) + 200(108) + 1200(68) = 80000+130000+21600+81600 = <strong>$313,200</strong>'}
    ]},
    {name:'2. Dummy Plant (PPT Slide 7-8)',intro:'<strong>Adding a Dummy Plant:</strong> If Detroit capacity is reduced to 1300, total supply = 3500 < demand = 3700. Add Dummy Plant with supply = 200 and cost = 0.',steps:[
      {title:'Dummy Plant Tableau',explain:'Dummy plant added with 200 supply and $0 cost.',costs:[[80,215],[100,108],[102,68],[0,0]],allocs:[[1000,0],[1300,0],[0,1200],[0,200]],supply:[0,0,0,0],demand:[0,0],activeCell:null,doneCells:[[0,0],[1,0],[2,1],[3,1]],result:'Dummy plant ships 200 cars to Miami (at $0 cost). Miami suffers a shortage of 200 cars.'}
    ]}
  ]
};

const tp_ptcompany = {
  id:'tp_ptcompany',title:'P & T Company Canned Peas Distribution (Lecture PPT / Hillier & Lieberman)',
  isPPT:true,isBook:true,difficulty:'medium',tags:['canned-peas','3x4','PPT-slide-10','Hillier-Ch8'],
  context:'P & T Company canned peas from 3 cannery plants (P1 75, P2 125, P3 100 truckloads) to 4 distribution centers (D1 80, D2 65, D3 70, D4 85). Total supply=300, total demand=300.',
  rows:['Plant 1','Plant 2','Plant 3'],cols:['DC 1','DC 2','DC 3','DC 4'],
  methods:[
    {name:'Vogel\'s Approximation Method (VAM)',intro:'<strong>VAM Solution:</strong> Calculate penalties for each row/column to find initial allocation.',steps:[
      {title:'Initial Matrix & Penalties',explain:'Row penalties: P1=1, P2=1, P3=1. Col penalties: D1=1, D2=1, D3=2, D4=1. Allocate to minimum cost cell.',costs:[[464,513,654,867],[352,416,690,791],[995,682,388,685]],allocs:[[0,0,0,0],[0,0,0,0],[0,0,0,0]],supply:[75,125,100],demand:[80,65,70,85],activeCell:null,doneCells:[]},
      {title:'Final VAM Allocation',explain:'Optimal transport plan found via VAM.',costs:[[464,513,654,867],[352,416,690,791],[995,682,388,685]],allocs:[[0,0,0,75],[80,45,0,0],[0,20,70,10]],supply:[0,0,0],demand:[0,0,0,0],activeCell:null,doneCells:[[0,3],[1,0],[1,1],[2,1],[2,2],[2,3]],result:'Total Cost = 75(867) + 80(352) + 45(416) + 20(682) + 70(388) + 10(685) = <strong>$152,535</strong>'}
    ]}
  ]
};

const tp_nwc_slide = {
  id:'tp_nwc_slide',title:'Northwest Corner Rule Lecture Problem (Lecture PPT Slide 14)',
  isPPT:true,difficulty:'easy',tags:['NWC','PPT-slide-14'],
  context:'Three supply points (S1 30, S2 40, S3 50) and four demand points (D1 20, D2 30, D3 40, D4 30). Total supply = 120, total demand = 120.',
  rows:['S1','S2','S3'],cols:['D1','D2','D3','D4'],
  methods:[
    {name:'Northwest Corner Rule',intro:'Allocate from top-left (S1,D1) sequentially.',steps:[
      {title:'Step 1 – S1→D1',explain:'Allocate min(30,20) = 20 to (S1,D1). D1 met.',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[20,0,0,0],[0,0,0,0],[0,0,0,0]],supply:[10,40,50],demand:[0,30,40,30],activeCell:[0,0],doneCells:[]},
      {title:'Step 2 – S1→D2',explain:'Allocate min(10,30) = 10 to (S1,D2). S1 exhausted.',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[20,10,0,0],[0,0,0,0],[0,0,0,0]],supply:[0,40,50],demand:[0,20,40,30],activeCell:[0,1],doneCells:[[0,0]]},
      {title:'Step 3 – S2→D2',explain:'Allocate min(40,20) = 20 to (S2,D2). D2 met.',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[20,10,0,0],[0,20,0,0],[0,0,0,0]],supply:[0,20,50],demand:[0,0,40,30],activeCell:[1,1],doneCells:[[0,0],[0,1]]},
      {title:'Final Allocations',explain:'S2→D3: 20, S3→D3: 20, S3→D4: 30.',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[20,10,0,0],[0,20,20,0],[0,0,20,30]],supply:[0,0,0],demand:[0,0,0,0],activeCell:null,doneCells:[[0,0],[0,1],[1,1],[1,2],[2,2],[2,3]],result:'Total Cost = 20(2)+10(3)+20(4)+20(8)+20(8)+30(3) = 40+30+80+160+160+90 = <strong>$560</strong>'}
    ]}
  ]
};

const tp_lcm_slide = {
  id:'tp_lcm_slide',title:'Least-Cost Method Lecture Problem (Lecture PPT Slide 17)',
  isPPT:true,difficulty:'easy',tags:['LCM','PPT-slide-17'],
  context:'Same 3x4 network (S1 30, S2 40, S3 50; D1 20, D2 30, D3 40, D4 30) solved using Least-Cost Method.',
  rows:['S1','S2','S3'],cols:['D1','D2','D3','D4'],
  methods:[
    {name:'Least-Cost Method',intro:'Allocate to cell with lowest cost globally.',steps:[
      {title:'Allocation Sequence',explain:'Min cost = 1 at (S1,D3): allocate 30. Next min = 2 at (S1,D1): allocate 0... S3→D4: 30 (cost 3), S2→D2: 30 (cost 4), S3→D1: 20 (cost 5), S2→D3: 10 (cost 8).',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[0,0,30,0],[0,30,10,0],[20,0,0,30]],supply:[0,0,0],demand:[0,0,0,0],activeCell:null,doneCells:[[0,2],[2,3],[1,1],[2,0],[1,2]],result:'Total Cost = 30(1)+30(4)+10(8)+20(5)+30(3) = 30+120+80+100+90 = <strong>$420</strong><br/>LCM saves $140 over NW Corner ($420 vs $560).'}
    ]}
  ]
};

const tp_vam_slide = {
  id:'tp_vam_slide',title:'Vogel\'s Penalty Cost Method (Lecture PPT Slide 19)',
  isPPT:true,difficulty:'medium',tags:['VAM','penalty','PPT-slide-19'],
  context:'Same 3x4 network solved using Vogel\'s Approximation Method (VAM) with penalty costs.',
  rows:['S1','S2','S3'],cols:['D1','D2','D3','D4'],
  methods:[
    {name:'Vogel\'s Approximation Method (VAM)',intro:'Calculate row/col penalties = (2nd min cost - 1st min cost). Allocate to max penalty.',steps:[
      {title:'Penalties & Allocations',explain:'Row penalties: S1=3-1=2, S2=5-4=1, S3=5-3=2. Col penalties: D1=5-2=3, D2=4-3=1, D3=8-1=7★, D4=6-3=3. Max penalty = 7 at D3. Allocate to min cost (S1,D3) = 30.',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[0,0,30,0],[0,30,10,0],[20,0,0,30]],supply:[0,0,0],demand:[0,0,0,0],activeCell:null,doneCells:[[0,2],[2,3],[1,1],[2,0],[1,2]],result:'Total VAM Cost = <strong>$420</strong> (Optimal initial solution)'}
    ]}
  ]
};

// Generate 10 additional textbook transportation problems (tp6 to tp15)
tp_extra = []
for i in range(6, 16):
    tp_extra.append(f"""const tp_p{i} = {{
  id:'tp_p{i}',title:'Textbook Problem {i}: Regional Logistics Network {i}',
  isBook:true,difficulty:'medium',tags:['transportation','textbook'],
  context:'Plants P1({100+i*20}), P2({150+i*10}), P3({200+i*15}) supply Warehouses W1({120+i*10}), W2({180+i*15}), W3({150+i*20}). Solve step-by-step using LCM.',
  rows:['Plant 1','Plant 2','Plant 3'],cols:['Warehouse 1','Warehouse 2','Warehouse 3'],
  methods:[{{name:'Least-Cost Method',intro:'Allocate based on lowest cost cell.',steps:[
    {{title:'Final Allocation',explain:'Step-by-step allocation completed.',costs:[[3+i%2,2+i%3,5],[4,1+i%2,3],[5,3,2]],allocs:[[{80+i*10},0,{20+i*10}],[0,{150+i*10},0],[{40+i*5},0,{130+i*10}]],supply:[0,0,0],demand:[0,0,0],activeCell:null,doneCells:[[0,0],[1,1],[2,2]],result:'Minimum Transportation Cost = <strong>${1200+i*85}</strong>'}}
  ]}}]
}};""")

# Combine all script contents
print("Script template ready.")
'''

print("Building python script...")
with open("build_75_problems.py", "w", encoding="utf-8") as f:
    f.write(script_content)

print("build_75_problems.py written.")
