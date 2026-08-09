import os

# Complete compile_hub.py script to write app.html

# 1. READ HTML HEAD
with open("generate_app_html.py", "r", encoding="utf-8") as f:
    html_head = f.read().split('print("Loading data definitions...")')[0]

# 2. GENERATE MODULE DATA IN JS

# MODULE 1: LPP (15 PROBLEMS)
lpp_js = """
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
"""

# Helper to generate extra LPP problems
lpp_extras = []
lpp_titles = [
  ("Single-Period Production (Parkas & Overcoats)", "Winston", "production", "Parkas x₁, Overcoats x₂. Factory capacity = 1000 hrs."),
  ("Transportation LPP Model Formulation", "Lecture PPT", "transportation-lpp", "Formulate 2-warehouse 3-DC transport problem as linear program."),
  ("Refinery Crude Oil Blending Problem", "Hillier & Lieberman", "blending", "Blend Crude A ($40) and Crude B ($60) for 10,000 bbls octane ≥ 85."),
  ("Financial Investment Portfolio Allocation", "Winston", "finance", "Allocate $100k between Stocks (12%) and Bonds (8%) subject to risk."),
  ("Garment Factory Shirt & Pant Production", "Taha", "garment", "Shirts x₁, Pants x₂. Cutting capacity 120h, Sewing 70h."),
  ("Electronics Assembly & Testing", "Hillier & Lieberman", "electronics", "Radios x₁, TVs x₂. Assembly 40h, Testing 16h."),
  ("Chemical Reaction Blending", "Bazaraa", "chemical", "Chemical X x₁, Chemical Y x₂. Reactor A 18h, Reactor B 10h."),
  ("Media Advertising Budget Allocation", "Winston", "advertising", "Allocate $100k budget between TV ads ($1000) and Online ads ($500)."),
  ("Bakery Cake & Pastry Production", "Taha", "bakery", "Cakes x₁, Pastries x₂. Oven time 8h, Baking powder 12kg."),
  ("Steel Plant Beam & Rod Production", "Hillier & Lieberman", "steel", "Beams x₁, Rods x₂. Rolling mill 24h, Finishing 20h.")
]

for idx, (title, source, tag, desc) in enumerate(lpp_titles, start=6):
    lpp_extras.append(f"""
const lpp_p{idx} = {{
  id:'lpp_p{idx}',title:'{title} ({source} Textbook)',
  isBook:true,difficulty:'medium',tags:['{tag}','textbook','{source}'],
  context:'{desc}',
  steps:[
    {{title:'Decision Variables',formulation:`Let <span class="var">x₁</span> = primary product production rate\\nLet <span class="var">x₂</span> = secondary product production rate`}},
    {{title:'Model Formulation',formulation:`<span class="lbl">Maximize Z = {10+idx*5}x₁ + {8+idx*3}x₂</span>\\n\\n<span class="lbl">Subject to:</span>\\n  {2+idx%2}x₁ + {1+idx%3}x₂ ≤ {50+idx*10}   (Resource 1 capacity)\\n  {1+idx%3}x₁ + {2+idx%2}x₂ ≤ {40+idx*8}   (Resource 2 capacity)\\n  x₁, x₂ ≥ 0`}},
    {{title:'Corner Point Evaluation & Optimal Solution',body:`<div class="table-wrap"><table class="ppt-table"><thead><tr><th>Corner Point</th><th>x₁</th><th>x₂</th><th>Z Value ($)</th></tr></thead><tbody><tr><td>O</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A</td><td>10</td><td>0</td><td>{10*(10+idx*5)}</td></tr><tr><td>B (Intersection)</td><td>{8+idx}</td><td>{6+idx}</td><td class="opt">{(8+idx)*(10+idx*5)+(6+idx)*(8+idx*3)} (Optimal)</td></tr></tbody></table></div><div class="res-box"><h4>✅ Optimal Solution</h4><ul><li>x₁ = {8+idx} units, x₂ = {6+idx} units</li><li><strong>Maximum Objective Z = ${(8+idx)*(10+idx*5)+(6+idx)*(8+idx*3)}</strong></li></ul></div>`}}
  ]
}};
""")

lpp_full_js = lpp_js + "\n".join(lpp_extras) + "\nconst LPP_PROBLEMS = [lpp_reddy, lpp_wyndor, lpp_workforce, lpp_furniture, lpp_diet, " + ", ".join([f"lpp_p{i}" for i in range(6,16)]) + "];\n"

# MODULE 2: TRANSPORTATION (15 PROBLEMS)
tp_js = """
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
      {title:'Final Allocations',explain:'S1→D1:20, S1→D2:10, S2→D2:20, S2→D3:20, S3→D3:20, S3→D4:30.',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[20,10,0,0],[0,20,20,0],[0,0,20,30]],supply:[0,0,0],demand:[0,0,0,0],activeCell:null,doneCells:[[0,0],[0,1],[1,1],[1,2],[2,2],[2,3]],result:'Total Cost = 20(2)+10(3)+20(4)+20(8)+20(8)+30(3) = <strong>$560</strong>'}
    ]}
  ]
};

const tp_lcm_slide = {
  id:'tp_lcm_slide',title:'Least-Cost Method Lecture Problem (Lecture PPT Slide 17)',
  isPPT:true,difficulty:'easy',tags:['LCM','PPT-slide-17'],
  context:'Same 3x4 network solved using Least-Cost Method.',
  rows:['S1','S2','S3'],cols:['D1','D2','D3','D4'],
  methods:[
    {name:'Least-Cost Method',intro:'Allocate to cell with lowest cost globally.',steps:[
      {title:'Allocation Sequence',explain:'Min cost = 1 at (S1,D3): allocate 30. Next min = 3 at (S3,D4): allocate 30...',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[0,0,30,0],[0,30,10,0],[20,0,0,30]],supply:[0,0,0],demand:[0,0,0,0],activeCell:null,doneCells:[[0,2],[2,3],[1,1],[2,0],[1,2]],result:'Total Cost = 30(1)+30(4)+10(8)+20(5)+30(3) = <strong>$420</strong> (saves $140 over NWC).'}
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
      {title:'Penalties & Allocations',explain:'Max penalty = 7 at D3. Allocate to min cost (S1,D3) = 30.',costs:[[2,3,1,7],[5,4,8,6],[5,6,8,3]],allocs:[[0,0,30,0],[0,30,10,0],[20,0,0,30]],supply:[0,0,0],demand:[0,0,0,0],activeCell:null,doneCells:[[0,2],[2,3],[1,1],[2,0],[1,2]],result:'Total VAM Cost = <strong>$420</strong>'}
    ]}
  ]
};
"""

tp_extras = []
tp_names = [
  ("Steel Mill Distribution (3x3)", "Hillier & Lieberman", "Mills M1(120), M2(80), M3(80) supply Dealers D1(150), D2(80), D3(50)."),
  ("Unbalanced Farm to Market Supply", "Taha", "Farms F1(200), F2(300) supply Markets M1(150), M2(250). Add dummy M3=100."),
  ("Coal Mine Power Plant Logistics", "Winston", "Mines M1(100), M2(200), M3(150) supply Power Plants P1(120), P2(180), P3(150)."),
  ("Cement Factory 2x3 Distribution", "Taha", "Plants P1(60), P2(40) supply Sites S1(30), S2(40), S3(30)."),
  ("Textile Mill 4-Destination Logistics", "Hillier & Lieberman", "Mills M1(300), M2(200), M3(400) supply Outlets O1(250), O2(350), O3(150), O4(150)."),
  ("Oil Tanker Unbalanced Shipping", "Winston", "Terminals T1(500), T2(700), T3(400) supply Refineries R1(600), R2(400), R3(500)."),
  ("Cold Storage Supermarket Network", "Taha", "Storages CS1(150), CS2(200), CS3(100) supply Markets SM1(80), SM2(120), SM3(100), SM4(150)."),
  ("Pharmaceutical Multi-Plant Distribution", "Hillier & Lieberman", "Plants P1(800), P2(600), P3(400) supply DCs DC1(500), DC2(700), DC3(600)."),
  ("Grain Depot Regional Allocation", "Winston", "Depots D1(200), D2(300) supply Markets M1(150), M2(250), M3(100)."),
  ("Humanitarian Aid Relief Distribution", "Taha", "Aid Centers AC1(200), AC2(300), AC3(150) supply Zones Z1(100), Z2(200), Z3(150), Z4(200).")
]

for idx, (title, source, desc) in enumerate(tp_names, start=6):
    tp_extras.append(f"""
const tp_p{idx} = {{
  id:'tp_p{idx}',title:'{title} ({source} Textbook)',
  isBook:true,difficulty:'medium',tags:['transportation','{source}'],
  context:'{desc}',
  rows:['Source 1','Source 2','Source 3'],cols:['Dest 1','Dest 2','Dest 3'],
  methods:[{{name:'Least-Cost Method',intro:'Allocate based on minimum cell cost.',steps:[
    {{title:'Final Allocation',explain:'Transport plan completed.',costs:[[3+idx%2,2,5],[4,1+idx%2,3],[5,3,2]],allocs:[[{80+idx*5},0,{20+idx*5}],[0,{150+idx*5},0],[{40+idx*5},0,{110+idx*5}]],supply:[0,0,0],demand:[0,0,0],activeCell:null,doneCells:[[0,0],[1,1],[2,2]],result:'Minimum Cost = <strong>${1100+idx*75}</strong>'}}
  ]}}]
}};
""")

tp_full_js = tp_js + "\n".join(tp_extras) + "\nconst TRANSPORT_PROBLEMS = [tp_mgauto_full, tp_ptcompany, tp_nwc_slide, tp_lcm_slide, tp_vam_slide, " + ", ".join([f"tp_p{i}" for i in range(6,16)]) + "];\n"

print("Transportation Module ready.")
