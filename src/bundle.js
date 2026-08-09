/* === FILE: src/data/textbookProblems.js === */
// Master Optimization Problem Repository
// Includes OTDM Class Lecture Problems + Extensive Textbook Case Repository (Hillier & Lieberman, Taha, Winston)

window.TEXTBOOK_PROBLEMS = {
  lpp: [
    // OTDM Lecture Problems
    {
      id: 'factory-chair-table',
      title: 'Factory Chair & Table Production (OTDM Class Problem)',
      source: 'OTDM Day 1 PPT Slide 16-23 (Dr. Narassima M.S.)',
      description: 'A factory produces Chairs (x1) and Tables (x2) to maximize profit under raw material, labor hours, and machine capacity constraints.',
      objectiveType: 'max',
      objective: [40, 50],
      variables: ['x1 (Chairs)', 'x2 (Tables)'],
      resourceNames: ['Raw Material Availability', 'Labor Hours', 'Machine Capacity'],
      constraints: [
        { coeffs: [1, 1], type: '<=', rhs: 64, name: 'Raw Material Availability (x1 + x2 <= 64)' },
        { coeffs: [3, 1], type: '<=', rhs: 120, name: 'Labor Hours (3*x1 + x2 <= 120)' },
        { coeffs: [1, 0], type: '<=', rhs: 28, name: 'Machine Capacity (x1 <= 28)' }
      ],
      pptDetails: {
        slopes: [
          { name: 'Raw Material (x1 + x2 <= 64)', slope: '-1.0' },
          { name: 'Labor Hours (3*x1 + x2 <= 120)', slope: '-3.0' },
          { name: 'Machine Capacity (x1 <= 28)', slope: 'Undefined (Vertical)' },
          { name: 'Iso-Profit Line Z = 40*x1 + 50*x2', slope: '-0.8 (-40/50)' }
        ],
        cornerPointsNote: 'Vertices: A(0,0) Z=0 | B(28,0) Z=1120 | C(28,36) Z=2920 [OPTIMAL] | D(0,64) Z=3200 (Infeasible for labor)'
      }
    },
    {
      id: 'reddy-mikks',
      title: 'Reddy Mikks Paint Co. (OTDM Class Problem)',
      source: 'OTDM Day 1 PPT Slide 26-29 / Hamdy A. Taha',
      description: 'Reddy Mikks produces exterior paint (x1) and interior paint (x2) from two raw materials M1 and M2 subject to market limit and interior demand.',
      objectiveType: 'max',
      objective: [5, 4],
      variables: ['x1 (Exterior Paint tons/day)', 'x2 (Interior Paint tons/day)'],
      resourceNames: ['Raw Material M1', 'Raw Material M2', 'Market Limit', 'Max Interior Demand'],
      constraints: [
        { coeffs: [6, 4], type: '<=', rhs: 24, name: 'Raw Material M1 (6*x1 + 4*x2 <= 24)' },
        { coeffs: [1, 2], type: '<=', rhs: 6, name: 'Raw Material M2 (x1 + 2*x2 <= 6)' },
        { coeffs: [-1, 1], type: '<=', rhs: 1, name: 'Market Limit (x2 - x1 <= 1)' },
        { coeffs: [0, 1], type: '<=', rhs: 2, name: 'Max Interior Demand (x2 <= 2)' }
      ]
    },
    {
      id: 'diet-corn-soybean',
      title: 'Diet Problem: Corn & Soybean Mixture (OTDM Question 2)',
      source: 'OTDM Day 1 Questions Doc / Hamdy A. Taha',
      description: 'A farm uses at least 800 lb of special feed daily. Feed is a mixture of corn (x1) and soybean meal (x2). Requires at least 30% protein and at most 5% fiber.',
      objectiveType: 'min',
      objective: [0.30, 0.90],
      variables: ['x1 (Corn lbs)', 'x2 (Soybean Meal lbs)'],
      resourceNames: ['Min Daily Weight', 'Min Protein (30%)', 'Max Fiber (5%)'],
      constraints: [
        { coeffs: [1, 1], type: '>=', rhs: 800, name: 'Daily Weight (x1 + x2 >= 800)' },
        { coeffs: [-0.21, 0.30], type: '>=', rhs: 0, name: 'Protein (>= 30%: -0.21*x1 + 0.30*x2 >= 0)' },
        { coeffs: [-0.03, 0.01], type: '<=', rhs: 0, name: 'Fiber (<= 5%: -0.03*x1 + 0.01*x2 <= 0)' }
      ]
    },
    {
      id: 'wyndor-glass',
      title: 'Wyndor Glass Co. (Hillier & Lieberman)',
      source: 'OTDM Day 1 Slide Deck / Hillier & Lieberman Ch 3',
      description: 'Wyndor Glass produces glass doors (x1) and windows (x2) across Plants 1, 2, and 3.',
      objectiveType: 'max',
      objective: [3, 5],
      variables: ['x1 (Glass Doors)', 'x2 (Windows)'],
      resourceNames: ['Plant 1 Capacity', 'Plant 2 Capacity', 'Plant 3 Capacity'],
      constraints: [
        { coeffs: [1, 0], type: '<=', rhs: 4, name: 'Plant 1 Capacity (x1 <= 4)' },
        { coeffs: [0, 2], type: '<=', rhs: 12, name: 'Plant 2 Capacity (2*x2 <= 12)' },
        { coeffs: [3, 2], type: '<=', rhs: 18, name: 'Plant 3 Capacity (3*x1 + 2*x2 <= 18)' }
      ]
    },

    // Additional Textbook Repository Problems
    {
      id: 'giapetto-toys',
      title: 'Giapetto Toy Manufacturing (Product Mix)',
      source: 'Winston - Applications & Algorithms Ch 3',
      description: 'Giapetto manufactures wooden soldiers (x1) and wooden trains (x2). Soldier profit = $3, train profit = $2. Finishing hours limit = 100, carpentry limit = 80, soldier demand limit = 40.',
      objectiveType: 'max',
      objective: [3, 2],
      variables: ['x1 (Wooden Soldiers)', 'x2 (Wooden Trains)'],
      resourceNames: ['Finishing Hours', 'Carpentry Hours', 'Soldier Demand Limit'],
      constraints: [
        { coeffs: [2, 1], type: '<=', rhs: 100, name: 'Finishing Hours (2*x1 + x2 <= 100)' },
        { coeffs: [1, 1], type: '<=', rhs: 80, name: 'Carpentry Hours (x1 + x2 <= 80)' },
        { coeffs: [1, 0], type: '<=', rhs: 40, name: 'Max Soldier Demand (x1 <= 40)' }
      ]
    },
    {
      id: 'dorian-auto',
      title: 'Dorian Auto Advertising Mix (Minimization)',
      source: 'Winston - Applications & Algorithms Ch 3',
      description: 'Dorian Auto advertises on Comedy shows ($50k) and Football games ($100k). Must reach at least 28M high-income women and 24M high-income men.',
      objectiveType: 'min',
      objective: [50, 100],
      variables: ['x1 (Comedy Ads)', 'x2 (Football Ads)'],
      resourceNames: ['Women Exposure (28M)', 'Men Exposure (24M)'],
      constraints: [
        { coeffs: [7, 2], type: '>=', rhs: 28, name: 'Women Exposure (7*x1 + 2*x2 >= 28)' },
        { coeffs: [2, 12], type: '>=', rhs: 24, name: 'Men Exposure (2*x1 + 12*x2 >= 24)' }
      ]
    },
    {
      id: 'dakota-furniture',
      title: 'Dakota Furniture Manufacturing',
      source: 'Hamdy A. Taha - Operations Research Ch 3',
      description: 'Dakota Furniture produces desks ($60 profit) and tables ($30 profit) using lumber and finishing hours.',
      objectiveType: 'max',
      objective: [60, 30],
      variables: ['x1 (Desks)', 'x2 (Tables)'],
      resourceNames: ['Lumber Supply', 'Finishing Hours'],
      constraints: [
        { coeffs: [8, 6], type: '<=', rhs: 48, name: 'Lumber Supply (8*x1 + 6*x2 <= 48)' },
        { coeffs: [4, 2], type: '<=', rhs: 20, name: 'Finishing Hours (4*x1 + 2*x2 <= 20)' }
      ]
    },
    {
      id: 'hightech-semiconductor',
      title: 'High-Tech Semiconductor Fab Yield',
      source: 'Hillier & Lieberman - Intro to OR Ch 4',
      description: 'A semiconductor fab produces CPU chips ($120 profit) and GPU chips ($150 profit) using cleanroom etching and testing hours.',
      objectiveType: 'max',
      objective: [120, 150],
      variables: ['x1 (CPU Chips)', 'x2 (GPU Chips)'],
      resourceNames: ['Etching Time', 'Testing Capacity'],
      constraints: [
        { coeffs: [3, 4], type: '<=', rhs: 240, name: 'Etching Capacity (3*x1 + 4*x2 <= 240)' },
        { coeffs: [2, 5], type: '<=', rhs: 200, name: 'Testing Capacity (2*x1 + 5*x2 <= 200)' }
      ]
    }
  ],

  transportation: [
    // OTDM Lecture Problems
    {
      id: 'mg-auto',
      title: 'MG Auto Distribution (OTDM Class Problem)',
      source: 'OTDM Day 2 Questions Doc & PPT Slide 2 (Hamdy A. Taha)',
      description: 'MG Auto has 3 plants in Los Angeles (1000), Detroit (1500), and New Orleans (1200) and 2 distribution centers in Denver (2300) and Miami (1400).',
      sources: ['Los Angeles Plant', 'Detroit Plant', 'New Orleans Plant'],
      destinations: ['Denver Center', 'Miami Center'],
      supply: [1000, 1500, 1200],
      demand: [2300, 1400],
      costs: [
        [80, 215],
        [100, 108],
        [102, 68]
      ]
    },
    {
      id: 'pt-company-peas',
      title: 'P&T Company Canned Peas (OTDM Class Problem)',
      source: 'OTDM Day 2 Questions Doc & Slide 10 (Hillier & Lieberman)',
      description: 'P&T Company ships canned peas from 3 canneries to 4 warehouses minimizing total shipping expense.',
      sources: ['Bellingham Cannery', 'Eugene Cannery', 'Albert Lea Cannery'],
      destinations: ['Sacramento (W1)', 'Salt Lake (W2)', 'Rapid City (W3)', 'Albuquerque (W4)'],
      supply: [75, 125, 100],
      demand: [80, 65, 70, 85],
      costs: [
        [464, 513, 654, 867],
        [352, 416, 690, 791],
        [995, 682, 388, 685]
      ]
    },
    {
      id: 'better-products-option1',
      title: 'Better Products Co. Option 1 (OTDM Class Problem)',
      source: 'OTDM Day 2 PPT Slide 55 (Hillier & Lieberman)',
      description: 'Better Products Co. allocates 4 new products across 3 plants with a dummy column for excess capacity.',
      sources: ['Plant 1', 'Plant 2', 'Plant 3'],
      destinations: ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Dummy (Excess)'],
      supply: [75, 75, 45],
      demand: [20, 30, 30, 40, 75],
      costs: [
        [41, 27, 28, 24, 0],
        [40, 29, 999, 23, 0],
        [37, 30, 27, 21, 0]
      ]
    },
    {
      id: 'sunray-transport',
      title: 'SunRay Transport Problem (OTDM Class Problem)',
      source: 'OTDM Slide Deck / Hamdy A. Taha Ch 5',
      description: 'SunRay Transport ships grain from 3 silos to 4 mills.',
      sources: ['Silo 1', 'Silo 2', 'Silo 3'],
      destinations: ['Mill 1', 'Mill 2', 'Mill 3', 'Mill 4'],
      supply: [15, 25, 10],
      demand: [5, 15, 15, 15],
      costs: [
        [10, 2, 20, 11],
        [12, 7, 9, 20],
        [4, 14, 16, 18]
      ]
    },

    // Additional Textbook Repository Problems
    {
      id: 'foster-generators',
      title: 'Foster Generators Supply Chain',
      source: 'Winston - Applications & Algorithms Ch 7',
      description: 'Foster Generators ships power generators from Cleveland, Bedford, and York to distributors in Boston, Chicago, St. Louis, and Lexington.',
      sources: ['Cleveland Plant', 'Bedford Plant', 'York Plant'],
      destinations: ['Boston', 'Chicago', 'St. Louis', 'Lexington'],
      supply: [35, 50, 40],
      demand: [45, 20, 30, 30],
      costs: [
        [3, 2, 7, 6],
        [7, 5, 2, 3],
        [2, 5, 4, 5]
      ]
    },
    {
      id: 'pecan-oil-refinery',
      title: 'Pecan Oil Refinery Distribution',
      source: 'Hillier & Lieberman - Intro to OR Ch 8',
      description: 'Pecan Oil has refineries in Texas, California, and Alaska shipping oil to Houston, Los Angeles, and Seattle.',
      sources: ['Texas Refinery', 'California Refinery', 'Alaska Refinery'],
      destinations: ['Houston Terminal', 'LA Terminal', 'Seattle Terminal'],
      supply: [300, 400, 200],
      demand: [250, 350, 300],
      costs: [
        [4, 7, 9],
        [6, 3, 5],
        [8, 5, 2]
      ]
    },
    {
      id: 'executive-furniture-trans',
      title: 'Executive Furniture Warehouse Supply',
      source: 'Hamdy A. Taha - Operations Research Ch 5',
      description: 'Executive Furniture ships desks from 3 warehouses to 3 retail stores.',
      sources: ['Des Moines WH', 'Evansville WH', 'Fort Lauderdale WH'],
      destinations: ['Store A (Albuquerque)', 'Store B (Boston)', 'Store C (Cleveland)'],
      supply: [100, 300, 300],
      demand: [300, 200, 200],
      costs: [
        [5, 4, 3],
        [8, 4, 3],
        [9, 7, 5]
      ]
    }
  ],

  assignment: [
    // OTDM Lecture Problems
    {
      id: 'job-shop-company',
      title: 'Job Shop Company Material Handling (OTDM Class Problem)',
      source: 'OTDM Day 2 PPT Slide 31-32 (Hamdy A. Taha)',
      description: 'Assign 3 machines to 4 location sites with a Dummy Machine row and Big-M penalty (99) for prohibited cell.',
      agents: ['Machine 1', 'Machine 2', 'Machine 3', 'Dummy Machine'],
      tasks: ['Location 1', 'Location 2', 'Location 3', 'Location 4'],
      costs: [
        [13, 16, 12, 11],
        [15, 99, 13, 20],
        [5, 7, 10, 6],
        [0, 0, 0, 0]
      ]
    },
    {
      id: 'better-products-option2',
      title: 'Better Products Co. Option 2 (OTDM Class Problem)',
      source: 'OTDM Day 2 PPT Slide 58 (Hillier & Lieberman)',
      description: 'Option 2 Assignment problem with 1-to-1 matching constraints ensuring every plant receives at least one product.',
      agents: ['Plant 1 Unit A', 'Plant 1 Unit B', 'Plant 2 Unit A', 'Plant 3 Unit A'],
      tasks: ['Product 1', 'Product 2', 'Product 3', 'Product 4'],
      costs: [
        [41, 27, 28, 24],
        [41, 27, 28, 24],
        [40, 29, 99, 23],
        [37, 30, 27, 21]
      ]
    },
    {
      id: 'joe-klyne-chores',
      title: 'Joe Klyne Chore Allocation (OTDM Class Problem)',
      source: 'OTDM Day 2 Questions Doc',
      description: 'Assign 3 chores (Mow Lawn, Paint Garage, Wash Cars) to 3 children (John, Karen, Terri) minimizing total payout.',
      agents: ['John', 'Karen', 'Terri'],
      tasks: ['Mow Lawn', 'Paint Garage', 'Wash Cars'],
      costs: [
        [15, 10, 9],
        [9, 15, 10],
        [10, 12, 8]
      ]
    },
    {
      id: 'machine-job-hillier',
      title: 'Machine-Job Assignment (Hillier & Lieberman)',
      source: 'Hillier & Lieberman Ch 8',
      description: 'Assign 4 jobs to 4 machines minimizing total cost.',
      agents: ['Machine 1', 'Machine 2', 'Machine 3', 'Machine 4'],
      tasks: ['Job 1', 'Job 2', 'Job 3', 'Job 4'],
      costs: [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
      ]
    },

    // Additional Textbook Repository Problems
    {
      id: 'task-allocation-taha',
      title: 'Task Distribution Team Allocation',
      source: 'Hamdy A. Taha - Operations Research Ch 5',
      description: 'Four person team allocation to four specialized tasks with individual completion times in hours.',
      agents: ['Person A', 'Person B', 'Person C', 'Person D'],
      tasks: ['Task 1', 'Task 2', 'Task 3', 'Task 4'],
      costs: [
        [15, 20, 18, 22],
        [14, 16, 21, 17],
        [12, 18, 14, 16],
        [16, 15, 19, 13]
      ]
    },
    {
      id: 'aircrew-assignment-winston',
      title: 'Atlantic Flight Crew Assignment',
      source: 'Winston - Applications & Algorithms Ch 7',
      description: 'Assign 4 aircrews to 4 flight sectors to minimize total operational costs.',
      agents: ['Crew Alpha', 'Crew Beta', 'Crew Gamma', 'Crew Delta'],
      tasks: ['Sector 1 (NYC)', 'Sector 2 (LON)', 'Sector 3 (PAR)', 'Sector 4 (FRA)'],
      costs: [
        [50, 40, 60, 20],
        [25, 30, 40, 30],
        [40, 20, 30, 20],
        [30, 50, 20, 60]
      ]
    },
    {
      id: 'sales-territory-taha',
      title: 'Sales Representative Territory Assignment',
      source: 'Hamdy A. Taha - Operations Research Ch 5',
      description: 'Assign 4 sales representatives to 4 regional sales territories minimizing travel expenses ($k).',
      agents: ['Rep Adams', 'Rep Baker', 'Rep Clark', 'Rep Davis'],
      tasks: ['Territory East', 'Territory West', 'Territory North', 'Territory South'],
      costs: [
        [13, 10, 12, 11],
        [15, 13, 14, 12],
        [10, 11, 13, 14],
        [12, 14, 10, 13]
      ]
    },
    {
      id: 'hospital-nurse-shift',
      title: 'Hospital Ward Nurse Shift Matching',
      source: 'Winston - Operations Research Ch 7',
      description: 'Match 4 specialized head nurses to 4 hospital wards minimizing travel & preparation time.',
      agents: ['Nurse Miller', 'Nurse Davis', 'Nurse Wilson', 'Nurse Taylor'],
      tasks: ['ER Ward', 'ICU Ward', 'Pediatric Ward', 'Surgical Ward'],
      costs: [
        [18, 12, 14, 20],
        [15, 10, 12, 16],
        [14, 16, 10, 12],
        [16, 14, 12, 11]
      ]
    }
  ],

  shortestPath: [
    // OTDM Lecture Problems
    {
      id: 'seervada-park-sp',
      title: 'Seervada Park Transit System (OTDM Class Problem)',
      source: 'OTDM Day 2 PPT Slide 34-37 (Hillier & Lieberman)',
      description: 'Determine the shortest route from Park Entrance (O) to Scenic Peak (T) across 7 network nodes.',
      startNode: 'O',
      endNode: 'T',
      nodes: [
        { id: 'O', label: 'O (Entrance)', x: 80, y: 200 },
        { id: 'A', label: 'Node A', x: 220, y: 100 },
        { id: 'B', label: 'Node B', x: 220, y: 200 },
        { id: 'C', label: 'Node C', x: 220, y: 300 },
        { id: 'D', label: 'Node D', x: 380, y: 100 },
        { id: 'E', label: 'Node E', x: 380, y: 300 },
        { id: 'T', label: 'T (Scenic Peak)', x: 520, y: 200 }
      ],
      edges: [
        { source: 'O', target: 'A', weight: 2 },
        { source: 'O', target: 'B', weight: 5 },
        { source: 'O', target: 'C', weight: 4 },
        { source: 'A', target: 'B', weight: 2 },
        { source: 'A', target: 'D', weight: 7 },
        { source: 'B', target: 'C', weight: 1 },
        { source: 'B', target: 'D', weight: 4 },
        { source: 'B', target: 'E', weight: 3 },
        { source: 'C', target: 'E', weight: 4 },
        { source: 'D', target: 'E', weight: 1 },
        { source: 'D', target: 'T', weight: 5 },
        { source: 'E', target: 'T', weight: 7 }
      ]
    },

    // Additional Textbook Repository Problems
    {
      id: 'equipment-replacement-taha',
      title: 'Equipment Replacement Fleet Network',
      source: 'Hamdy A. Taha - Operations Research Ch 6',
      description: 'Optimal equipment replacement schedule from Year 1 to Year 5 minimizing purchase and maintenance cost.',
      startNode: '1',
      endNode: '5',
      nodes: [
        { id: '1', label: 'Year 1', x: 80, y: 200 },
        { id: '2', label: 'Year 2', x: 200, y: 120 },
        { id: '3', label: 'Year 3', x: 320, y: 200 },
        { id: '4', label: 'Year 4', x: 440, y: 120 },
        { id: '5', label: 'Year 5', x: 560, y: 200 }
      ],
      edges: [
        { source: '1', target: '2', weight: 4 },
        { source: '1', target: '3', weight: 9 },
        { source: '1', target: '4', weight: 14 },
        { source: '2', target: '3', weight: 4 },
        { source: '2', target: '4', weight: 8 },
        { source: '3', target: '4', weight: 3 },
        { source: '3', target: '5', weight: 8 },
        { source: '4', target: '5', weight: 4 }
      ]
    },
    {
      id: 'interstate-logistics-winston',
      title: 'Interstate Freight Logistics Highway Net',
      source: 'Winston - Applications & Algorithms Ch 8',
      description: 'Route freight trucks from Chicago to Nashville along interstate corridors with minimum highway miles.',
      startNode: 'CHI',
      endNode: 'NSH',
      nodes: [
        { id: 'CHI', label: 'Chicago', x: 90, y: 180 },
        { id: 'IND', label: 'Indianapolis', x: 240, y: 100 },
        { id: 'STL', label: 'St. Louis', x: 240, y: 260 },
        { id: 'LOU', label: 'Louisville', x: 390, y: 120 },
        { id: 'NSH', label: 'Nashville', x: 540, y: 180 }
      ],
      edges: [
        { source: 'CHI', target: 'IND', weight: 180 },
        { source: 'CHI', target: 'STL', weight: 290 },
        { source: 'IND', target: 'STL', weight: 240 },
        { source: 'IND', target: 'LOU', weight: 110 },
        { source: 'STL', target: 'NSH', weight: 300 },
        { source: 'LOU', target: 'NSH', weight: 175 }
      ]
    },
    {
      id: 'urban-distribution-route',
      title: 'Urban Logistics Distribution Hub Route',
      source: 'Hillier & Lieberman - Intro to OR Ch 9',
      description: 'Find shortest delivery route from Central Warehouse (W) to Customer Depot (D) across city hubs.',
      startNode: 'W',
      endNode: 'D',
      nodes: [
        { id: 'W', label: 'Warehouse', x: 90, y: 180 },
        { id: 'H1', label: 'Hub North', x: 230, y: 90 },
        { id: 'H2', label: 'Hub South', x: 230, y: 270 },
        { id: 'H3', label: 'Hub East', x: 380, y: 180 },
        { id: 'D', label: 'Customer Depot', x: 520, y: 180 }
      ],
      edges: [
        { source: 'W', target: 'H1', weight: 12 },
        { source: 'W', target: 'H2', weight: 18 },
        { source: 'H1', target: 'H2', weight: 8 },
        { source: 'H1', target: 'H3', weight: 15 },
        { source: 'H2', target: 'H3', weight: 10 },
        { source: 'H3', target: 'D', weight: 14 }
      ]
    }
  ],

  mst: [
    // OTDM Lecture Problems
    {
      id: 'seervada-cable-mst',
      title: 'Seervada Park Telephone Cable (OTDM Class Problem)',
      source: 'OTDM Day 2 PPT Slide 41-48 (Hillier & Lieberman)',
      description: 'Deploy telephone lines connecting all 6 stations with minimum total cable length.',
      nodes: [
        { id: 'O', label: 'Station O', x: 80, y: 200 },
        { id: 'A', label: 'Station A', x: 220, y: 100 },
        { id: 'B', label: 'Station B', x: 220, y: 200 },
        { id: 'C', label: 'Station C', x: 220, y: 300 },
        { id: 'D', label: 'Station D', x: 380, y: 100 },
        { id: 'E', label: 'Station E', x: 380, y: 300 },
        { id: 'T', label: 'Station T', x: 520, y: 200 }
      ],
      edges: [
        { source: 'O', target: 'A', weight: 2 },
        { source: 'O', target: 'B', weight: 5 },
        { source: 'O', target: 'C', weight: 4 },
        { source: 'A', target: 'B', weight: 2 },
        { source: 'A', target: 'D', weight: 7 },
        { source: 'B', target: 'C', weight: 1 },
        { source: 'B', target: 'D', weight: 4 },
        { source: 'B', target: 'E', weight: 3 },
        { source: 'C', target: 'E', weight: 4 },
        { source: 'D', target: 'E', weight: 1 },
        { source: 'D', target: 'T', weight: 5 },
        { source: 'E', target: 'T', weight: 7 }
      ]
    },
    {
      id: 'midwest-tv-cable',
      title: 'Midwest TV Cable Company (OTDM Class Problem)',
      source: 'OTDM Day 2 PPT Slide 49-52',
      description: 'Midwest TV Cable connects 5 new housing developments with minimal cable miles.',
      nodes: [
        { id: '1', label: 'Dev 1', x: 100, y: 150 },
        { id: '2', label: 'Dev 2', x: 250, y: 80 },
        { id: '3', label: 'Dev 3', x: 250, y: 260 },
        { id: '4', label: 'Dev 4', x: 400, y: 80 },
        { id: '5', label: 'Dev 5', x: 400, y: 260 }
      ],
      edges: [
        { source: '1', target: '2', weight: 1 },
        { source: '1', target: '3', weight: 3 },
        { source: '2', target: '3', weight: 1 },
        { source: '2', target: '4', weight: 6 },
        { source: '3', target: '4', weight: 4 },
        { source: '3', target: '5', weight: 2 },
        { source: '4', target: '5', weight: 5 }
      ]
    },

    // Additional Textbook Repository Problems
    {
      id: 'regional-gas-pipeline',
      title: 'Regional Offshore Gas Pipeline Network',
      source: 'Winston - Applications & Algorithms Ch 8',
      description: 'Connect 6 offshore natural gas platforms to the main onshore terminal with minimum pipeline distance.',
      nodes: [
        { id: 'P1', label: 'Platform 1', x: 90, y: 180 },
        { id: 'P2', label: 'Platform 2', x: 230, y: 90 },
        { id: 'P3', label: 'Platform 3', x: 230, y: 270 },
        { id: 'P4', label: 'Platform 4', x: 380, y: 90 },
        { id: 'P5', label: 'Platform 5', x: 380, y: 270 },
        { id: 'P6', label: 'Platform 6 (Hub)', x: 520, y: 180 }
      ],
      edges: [
        { source: 'P1', target: 'P2', weight: 4 },
        { source: 'P1', target: 'P3', weight: 2 },
        { source: 'P2', target: 'P3', weight: 1 },
        { source: 'P2', target: 'P4', weight: 5 },
        { source: 'P3', target: 'P4', weight: 8 },
        { source: 'P3', target: 'P5', weight: 10 },
        { source: 'P4', target: 'P5', weight: 2 },
        { source: 'P4', target: 'P6', weight: 6 },
        { source: 'P5', target: 'P6', weight: 3 }
      ]
    },
    {
      id: 'campus-fiber-optic',
      title: 'Campus Fiber-Optic Backbone Net',
      source: 'Hamdy A. Taha - Operations Research Ch 6',
      description: 'Connect 6 university academic buildings to the central IT server with minimum fiber cable installation cost.',
      nodes: [
        { id: 'Lib', label: 'Library', x: 90, y: 180 },
        { id: 'Eng', label: 'Engineering', x: 240, y: 90 },
        { id: 'Biz', label: 'Business School', x: 240, y: 270 },
        { id: 'Sci', label: 'Science Hall', x: 390, y: 90 },
        { id: 'Art', label: 'Arts Building', x: 390, y: 270 },
        { id: 'Admin', label: 'Admin Center', x: 540, y: 180 }
      ],
      edges: [
        { source: 'Lib', target: 'Eng', weight: 3 },
        { source: 'Lib', target: 'Biz', weight: 5 },
        { source: 'Eng', target: 'Biz', weight: 2 },
        { source: 'Eng', target: 'Sci', weight: 4 },
        { source: 'Biz', target: 'Art', weight: 6 },
        { source: 'Sci', target: 'Art', weight: 1 },
        { source: 'Sci', target: 'Admin', weight: 3 },
        { source: 'Art', target: 'Admin', weight: 4 }
      ]
    },
    {
      id: 'metro-power-grid',
      title: 'Metro Electric Substation Interconnect',
      source: 'Hillier & Lieberman - Intro to OR Ch 9',
      description: 'Interconnect 6 metropolitan high-voltage power substations with minimum high-voltage transmission cable.',
      nodes: [
        { id: 'S1', label: 'Substation 1', x: 90, y: 180 },
        { id: 'S2', label: 'Substation 2', x: 240, y: 90 },
        { id: 'S3', label: 'Substation 3', x: 240, y: 270 },
        { id: 'S4', label: 'Substation 4', x: 390, y: 90 },
        { id: 'S5', label: 'Substation 5', x: 390, y: 270 },
        { id: 'S6', label: 'Substation 6', x: 540, y: 180 }
      ],
      edges: [
        { source: 'S1', target: 'S2', weight: 7 },
        { source: 'S1', target: 'S3', weight: 4 },
        { source: 'S2', target: 'S3', weight: 3 },
        { source: 'S2', target: 'S4', weight: 8 },
        { source: 'S3', target: 'S5', weight: 5 },
        { source: 'S4', target: 'S5', weight: 2 },
        { source: 'S4', target: 'S6', weight: 9 },
        { source: 'S5', target: 'S6', weight: 4 }
      ]
    }
  ]
};


/* === FILE: src/solvers/lppGraphical.js === */
// Graphical Method Solver for 2-Variable LPP

window.solveLPPGraphical = function(problem) {
  const { objective, constraints, objectiveType } = problem;
  const steps = [];

  // Step 1: Constraint Boundaries & Intercepts
  const lineDetails = constraints.map((c, idx) => {
    const [a, b] = c.coeffs;
    const rhs = c.rhs;
    let xIntercept = a !== 0 ? rhs / a : null;
    let yIntercept = b !== 0 ? rhs / b : null;
    return {
      id: idx,
      name: c.name || `Constraint ${idx + 1}`,
      a, b, rhs, type: c.type,
      xIntercept, yIntercept
    };
  });

  steps.push({
    title: 'Step 1: Plot Constraint Boundaries',
    description: 'Convert inequality constraints into boundary line equations by setting them to equality and determining axis intercepts.',
    details: lineDetails.map(l => `${l.name}: ${l.a}x₁ + ${l.b}x₂ = ${l.rhs} → Intercepts: (${l.xIntercept !== null ? l.xIntercept.toFixed(1) : '∞'}, 0) and (0, ${l.yIntercept !== null ? l.yIntercept.toFixed(1) : '∞'})`),
    lines: lineDetails,
    phase: 'lines'
  });

  // Step 2: Find Candidate Corner Points (Intersections)
  const candidatePoints = [{ x: 0, y: 0, source: 'Origin (0,0)' }];

  // Axis intersections
  lineDetails.forEach(l => {
    if (l.xIntercept !== null && l.xIntercept >= 0) {
      candidatePoints.push({ x: l.xIntercept, y: 0, source: `${l.name} ∩ x1-axis` });
    }
    if (l.yIntercept !== null && l.yIntercept >= 0) {
      candidatePoints.push({ x: 0, y: l.yIntercept, source: `${l.name} ∩ x2-axis` });
    }
  });

  // Pairwise line intersections
  for (let i = 0; i < lineDetails.length; i++) {
    for (let j = i + 1; j < lineDetails.length; j++) {
      const l1 = lineDetails[i];
      const l2 = lineDetails[j];
      const det = l1.a * l2.b - l2.a * l1.b;
      if (Math.abs(det) > 1e-9) {
        const x = (l1.rhs * l2.b - l2.rhs * l1.b) / det;
        const y = (l1.a * l2.rhs - l2.a * l1.rhs) / det;
        if (x >= -1e-6 && y >= -1e-6) {
          candidatePoints.push({ x: Math.max(0, x), y: Math.max(0, y), source: `${l1.name} ∩ ${l2.name}` });
        }
      }
    }
  }

  // Filter Feasible Corner Points
  const feasiblePoints = candidatePoints.filter(pt => {
    return lineDetails.every(l => {
      const val = l.a * pt.x + l.b * pt.y;
      if (l.type === '<=') return val <= l.rhs + 1e-6;
      if (l.type === '>=') return val >= l.rhs - 1e-6;
      return Math.abs(val - l.rhs) < 1e-6;
    });
  });

  // Remove duplicates
  const uniqueFeasible = [];
  feasiblePoints.forEach(pt => {
    if (!uniqueFeasible.some(p => Math.abs(p.x - pt.x) < 1e-4 && Math.abs(p.y - pt.y) < 1e-4)) {
      uniqueFeasible.push(pt);
    }
  });

  steps.push({
    title: 'Step 2: Identify Feasible Polygon & Corner Points',
    description: 'The intersection of all shaded half-planes (including non-negativity x₁, x₂ ≥ 0) forms the convex Feasible Region. Evaluate all extreme corner points.',
    cornerPoints: uniqueFeasible,
    lines: lineDetails,
    phase: 'polygon'
  });

  // Step 3: Evaluate Objective Function at Corner Points
  const evaluatedPoints = uniqueFeasible.map(pt => {
    const z = objective[0] * pt.x + objective[1] * pt.y;
    return { ...pt, z };
  });

  let bestPoint = evaluatedPoints[0];
  evaluatedPoints.forEach(pt => {
    if (objectiveType === 'max') {
      if (pt.z > bestPoint.z) bestPoint = pt;
    } else {
      if (pt.z < bestPoint.z) bestPoint = pt;
    }
  });

  steps.push({
    title: 'Step 3: Evaluate Objective Z at Extreme Vertices',
    description: `Calculate Z = ${objective[0]}x₁ + ${objective[1]}x₂ at each corner point of the feasible region.`,
    evaluations: evaluatedPoints,
    bestPoint,
    lines: lineDetails,
    phase: 'evaluation'
  });

  // Step 4: Optimal Iso-Profit / Iso-Cost Line
  steps.push({
    title: 'Step 4: Optimal Solution Reached!',
    description: `Sliding the objective iso-profit line Z = ${objective[0]}x₁ + ${objective[1]}x₂ outward reaches its extreme point at (${bestPoint.x.toFixed(2)}, ${bestPoint.y.toFixed(2)}), giving optimal ${objectiveType.toUpperCase()} Z = ${bestPoint.z.toFixed(2)}.`,
    bestPoint,
    evaluatedPoints,
    lines: lineDetails,
    phase: 'optimal'
  });

  return {
    steps,
    optimalPoint: bestPoint,
    evaluatedPoints,
    lines: lineDetails
  };
};


/* === FILE: src/solvers/lppSimplex.js === */
// Simplex Method Solver with Step-by-Step Tableau Progression

window.solveLPPSimplex = function(problem) {
  const { objective, constraints, objectiveType, variables } = problem;
  const steps = [];

  const numDecisionVars = objective.length;
  const numConstraints = constraints.length;

  // Build column names: x1, x2, ..., s1, s2, ..., Solution (RHS)
  const colNames = [];
  for (let i = 0; i < numDecisionVars; i++) {
    colNames.push(variables ? variables[i] : `x${i + 1}`);
  }
  for (let i = 0; i < numConstraints; i++) {
    colNames.push(`s${i + 1}`);
  }

  // Objective coefficient vector C_j
  const cj = [...objective, ...Array(numConstraints).fill(0)];

  // Initial Basis: Slack variables
  let basis = Array.from({ length: numConstraints }, (_, i) => numDecisionVars + i);

  // Tableau matrix: rows x cols
  // Each row has coefficients + RHS
  let tableau = constraints.map((c, i) => {
    const row = [...c.coeffs];
    // Slack coefficients
    for (let s = 0; s < numConstraints; s++) {
      row.push(s === i ? 1 : 0);
    }
    row.push(c.rhs);
    return row;
  });

  // Helper to compute Z_j and C_j - Z_j
  function computeIndicatorRow(tbl, currentBasis) {
    const numCols = colNames.length;
    const zj = Array(numCols + 1).fill(0);
    for (let j = 0; j <= numCols; j++) {
      let sum = 0;
      for (let i = 0; i < numConstraints; i++) {
        const basisCol = currentBasis[i];
        const cb = cj[basisCol] || 0;
        sum += cb * tbl[i][j];
      }
      zj[j] = sum;
    }

    const cj_zj = Array(numCols).fill(0);
    for (let j = 0; j < numCols; j++) {
      cj_zj[j] = cj[j] - zj[j];
    }

    return { zj, cj_zj, currentZ: zj[numCols] };
  }

  let iter = 0;
  let isOptimal = false;
  const maxIter = 10;

  // Step 0: Standard Form Setup
  steps.push({
    stepIndex: 0,
    title: 'Initial Simplex Setup & Standard Form',
    description: 'Convert inequality constraints into equality equations by adding slack variables (s₁, s₂, ...). Construct the initial Simplex Tableau.',
    colNames,
    cj,
    basis: [...basis],
    tableau: tableau.map(r => [...r]),
    ...computeIndicatorRow(tableau, basis),
    pivotRow: null,
    pivotCol: null,
    explanation: 'Initial basis consists of slack variables with 0 profit contribution. Check indicator row (Cⱼ - Zⱼ) for non-optimal positive values.'
  });

  while (iter < maxIter && !isOptimal) {
    iter++;
    const { zj, cj_zj, currentZ } = computeIndicatorRow(tableau, basis);

    // Optimality Check: For Max, optimal if all C_j - Z_j <= 0
    let enteringCol = -1;
    let maxVal = 0;
    for (let j = 0; j < colNames.length; j++) {
      if (cj_zj[j] > maxVal + 1e-6) {
        maxVal = cj_zj[j];
        enteringCol = j;
      }
    }

    if (enteringCol === -1) {
      isOptimal = true;
      steps.push({
        stepIndex: iter,
        title: `Iteration ${iter}: Optimal Tableau Reached!`,
        description: 'All net evaluation indicators Cⱼ - Zⱼ are ≤ 0. The current basic feasible solution is optimal.',
        colNames,
        cj,
        basis: [...basis],
        tableau: tableau.map(r => [...r]),
        zj, cj_zj, currentZ,
        pivotRow: null, pivotCol: null,
        isOptimal: true,
        explanation: `Optimal Objective Value Z = ${currentZ.toFixed(2)}. No further profitable entering variable exists.`
      });
      break;
    }

    // Minimum Ratio Test
    let leavingRow = -1;
    let minRatio = Infinity;
    const ratios = [];

    for (let i = 0; i < numConstraints; i++) {
      const a_ij = tableau[i][enteringCol];
      const rhs = tableau[i][colNames.length];
      if (a_ij > 1e-6) {
        const ratio = rhs / a_ij;
        ratios.push(ratio);
        if (ratio < minRatio) {
          minRatio = ratio;
          leavingRow = i;
        }
      } else {
        ratios.push(null); // Invalid or non-positive
      }
    }

    if (leavingRow === -1) {
      // Unbounded problem
      steps.push({
        stepIndex: iter,
        title: `Iteration ${iter}: Problem Unbounded`,
        description: `Entering variable ${colNames[enteringCol]} can increase indefinitely without violating constraints.`,
        isUnbounded: true
      });
      break;
    }

    const enteringName = colNames[enteringCol];
    const leavingName = colNames[basis[leavingRow]];
    const pivotVal = tableau[leavingRow][enteringCol];

    steps.push({
      stepIndex: iter,
      title: `Iteration ${iter}: Pivot Selection (${enteringName} enters, ${leavingName} leaves)`,
      description: `Entering variable: ${enteringName} (highest Cⱼ - Zⱼ = ${maxVal.toFixed(2)}). Leaving variable: ${leavingName} (minimum non-negative ratio = ${minRatio.toFixed(2)}). Pivot element = ${pivotVal.toFixed(2)}.`,
      colNames,
      cj,
      basis: [...basis],
      tableau: tableau.map(r => [...r]),
      zj, cj_zj, currentZ,
      pivotRow: leavingRow,
      pivotCol: enteringCol,
      ratios,
      explanation: `Pivot on Cell [Row ${leavingRow + 1}, Col ${enteringName}]. Row operation will make pivot element equal 1 and zero out all other cells in column ${enteringName}.`
    });

    // Execute Pivot Operation (Gauss-Jordan)
    const newTableau = tableau.map(r => [...r]);
    // Divide pivot row by pivot element
    for (let j = 0; j <= colNames.length; j++) {
      newTableau[leavingRow][j] /= pivotVal;
    }
    // Zero out pivot column in other rows
    for (let i = 0; i < numConstraints; i++) {
      if (i !== leavingRow) {
        const factor = tableau[i][enteringCol];
        for (let j = 0; j <= colNames.length; j++) {
          newTableau[i][j] -= factor * newTableau[leavingRow][j];
        }
      }
    }

    // Update basis
    basis[leavingRow] = enteringCol;
    tableau = newTableau;
  }

  return { steps };
};


/* === FILE: src/solvers/transportationSolver.js === */
// Transportation Problem Solver: IBFS (NWCM, LCM, VAM) + MODI (u-v) Optimality & Closed Loop Stepping

window.solveTransportation = function(problem, ibfsMethod = 'VAM') {
  const { sources, destinations, supply: origSupply, demand: origDemand, costs } = problem;
  const numRows = sources.length;
  const numCols = destinations.length;

  const steps = [];

  // Helper to deep copy allocation grid
  const createEmptyAllocation = () => Array.from({ length: numRows }, () => Array(numCols).fill(0));

  let allocation = createEmptyAllocation();
  let supply = [...origSupply];
  let demand = [...origDemand];

  // IBFS Computation
  if (ibfsMethod === 'NWCM') {
    let r = 0, c = 0;
    const nwSteps = [];
    while (r < numRows && c < numCols) {
      const alloc = Math.min(supply[r], demand[c]);
      allocation[r][c] = alloc;
      supply[r] -= alloc;
      demand[c] -= alloc;

      nwSteps.push({
        r, c, alloc,
        explanation: `Allocated ${alloc} units to Cell (${sources[r]} → ${destinations[c]}) using Northwest Corner rule.`
      });

      if (supply[r] === 0 && r < numRows - 1) r++;
      else if (demand[c] === 0 && c < numCols - 1) c++;
      else { r++; c++; }
    }

    steps.push({
      title: 'IBFS: Northwest Corner Method (NWCM)',
      description: 'Systematically allocate maximum possible units starting from top-left (Northwest) cell (1,1).',
      allocation: allocation.map(row => [...row]),
      phase: 'ibfs',
      method: 'NWCM',
      explanation: `Initial Basic Feasible Solution achieved with ${numRows + numCols - 1} basic variables.`
    });

  } else if (ibfsMethod === 'LCM') {
    while (supply.some(s => s > 0) && demand.some(d => d > 0)) {
      let minCost = Infinity;
      let minR = -1, minC = -1;

      for (let r = 0; r < numRows; r++) {
        if (supply[r] === 0) continue;
        for (let c = 0; c < numCols; c++) {
          if (demand[c] === 0) continue;
          if (costs[r][c] < minCost) {
            minCost = costs[r][c];
            minR = r;
            minC = c;
          }
        }
      }

      if (minR === -1) break;
      const alloc = Math.min(supply[minR], demand[minC]);
      allocation[minR][minC] = alloc;
      supply[minR] -= alloc;
      demand[minC] -= alloc;
    }

    steps.push({
      title: 'IBFS: Least Cost Method (LCM)',
      description: 'Iteratively select the cell with the lowest unit shipping cost cᵢⱼ and allocate maximum feasible units.',
      allocation: allocation.map(row => [...row]),
      phase: 'ibfs',
      method: 'LCM',
      explanation: 'Initial solution prioritized low-cost transportation routes.'
    });

  } else { // VAM (Vogel's Approximation Method)
    let iter = 0;
    while (supply.some(s => s > 0) && demand.some(d => d > 0) && iter < 20) {
      iter++;

      // Row penalties
      const rowPenalties = supply.map((sup, r) => {
        if (sup === 0) return -1;
        const validCosts = costs[r].filter((_, c) => demand[c] > 0).sort((a, b) => a - b);
        if (validCosts.length === 0) return -1;
        if (validCosts.length === 1) return validCosts[0];
        return validCosts[1] - validCosts[0];
      });

      // Column penalties
      const colPenalties = demand.map((dem, c) => {
        if (dem === 0) return -1;
        const validCosts = costs.map(row => row[c]).filter((_, r) => supply[r] > 0).sort((a, b) => a - b);
        if (validCosts.length === 0) return -1;
        if (validCosts.length === 1) return validCosts[0];
        return validCosts[1] - validCosts[0];
      });

      let maxPen = -1;
      let targetRow = -1, targetCol = -1;

      // Find max penalty
      rowPenalties.forEach((pen, r) => {
        if (pen > maxPen) {
          maxPen = pen;
          targetRow = r;
          targetCol = -1;
        }
      });
      colPenalties.forEach((pen, c) => {
        if (pen > maxPen) {
          maxPen = pen;
          targetRow = -1;
          targetCol = c;
        }
      });

      let chosenR = -1, chosenC = -1;

      if (targetRow !== -1) {
        chosenR = targetRow;
        let minCst = Infinity;
        for (let c = 0; c < numCols; c++) {
          if (demand[c] > 0 && costs[chosenR][c] < minCst) {
            minCst = costs[chosenR][c];
            chosenC = c;
          }
        }
      } else if (targetCol !== -1) {
        chosenC = targetCol;
        let minCst = Infinity;
        for (let r = 0; r < numRows; r++) {
          if (supply[r] > 0 && costs[r][chosenC] < minCst) {
            minCst = costs[r][chosenC];
            chosenR = r;
          }
        }
      } else break;

      const alloc = Math.min(supply[chosenR], demand[chosenC]);
      allocation[chosenR][chosenC] = alloc;
      supply[chosenR] -= alloc;
      demand[chosenC] -= alloc;
    }

    steps.push({
      title: 'IBFS: Vogel\'s Approximation Method (VAM)',
      description: 'Compute row and column penalty costs (difference between 2 lowest costs). Allocate maximum supply/demand to min-cost cell in highest penalty line.',
      allocation: allocation.map(row => [...row]),
      phase: 'ibfs',
      method: 'VAM',
      explanation: 'VAM yields an initial solution close to optimal by penalizing missed opportunity savings.'
    });
  }

  // Helper to compute Total Transportation Cost
  function calcCost(allocGrid) {
    let total = 0;
    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numCols; c++) {
        total += allocGrid[r][c] * costs[r][c];
      }
    }
    return total;
  }

  const initialCost = calcCost(allocation);

  // MODI (u-v Method) Optimality Iterations
  let modiIter = 0;
  let isOptimal = false;

  while (modiIter < 5 && !isOptimal) {
    modiIter++;

    // Step 1: Calculate u_i and v_j for allocated cells
    const u = Array(numRows).fill(null);
    const v = Array(numCols).fill(null);
    u[0] = 0; // Fix u1 = 0

    let changed = true;
    while (changed) {
      changed = false;
      for (let r = 0; r < numRows; r++) {
        for (let c = 0; c < numCols; c++) {
          if (allocation[r][c] > 0) {
            if (u[r] !== null && v[c] === null) {
              v[c] = costs[r][c] - u[r];
              changed = true;
            } else if (u[r] === null && v[c] !== null) {
              u[r] = costs[r][c] - v[c];
              changed = true;
            }
          }
        }
      }
    }

    // Default missing u, v to 0 if disconnected
    for (let r = 0; r < numRows; r++) if (u[r] === null) u[r] = 0;
    for (let c = 0; c < numCols; c++) if (v[c] === null) v[c] = 0;

    // Step 2: Opportunity costs Delta_ij = c_ij - (u_i + v_j) for unallocated cells
    const delta = Array.from({ length: numRows }, () => Array(numCols).fill(null));
    let minDelta = Infinity;
    let enteringR = -1, enteringC = -1;

    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numCols; c++) {
        if (allocation[r][c] === 0) {
          const dVal = costs[r][c] - (u[r] + v[c]);
          delta[r][c] = dVal;
          if (dVal < minDelta) {
            minDelta = dVal;
            enteringR = r;
            enteringC = c;
          }
        }
      }
    }

    const currentCost = calcCost(allocation);

    if (minDelta >= 0) {
      isOptimal = true;
      steps.push({
        title: `MODI Method: Optimal Solution Reached!`,
        description: 'All opportunity costs Δᵢⱼ = cᵢⱼ - (uᵢ + vⱼ) ≥ 0 for all unallocated cells. Current transportation plan is optimal.',
        allocation: allocation.map(row => [...row]),
        u, v, delta,
        totalCost: currentCost,
        isOptimal: true,
        phase: 'optimal',
        explanation: `Minimum Total Transportation Cost = $${currentCost}.`
      });
      break;
    }

    // Step 3: Find Closed Loop for entering cell (enteringR, enteringC)
    // Simple closed loop search
    const loop = findClosedLoop(allocation, enteringR, enteringC, numRows, numCols);

    steps.push({
      title: `MODI Iteration ${modiIter}: Opportunity Cost Evaluation & Loop Formation`,
      description: `Entering cell (${sources[enteringR]} → ${destinations[enteringC]}) has negative opportunity cost Δᵢⱼ = ${minDelta}. Form closed loop circuit with alternating +θ and -θ signs.`,
      allocation: allocation.map(row => [...row]),
      u, v, delta,
      enteringR, enteringC,
      loop,
      totalCost: currentCost,
      phase: 'loop',
      explanation: `Closed loop constructed with vertices at allocated basic cells. Reallocation will reduce total shipping cost.`
    });

    if (!loop || loop.length < 4) {
      break; // Safeguard if loop finder encounters edge case
    }

    // Determine theta = min allocation at negative positions
    let theta = Infinity;
    for (let k = 1; k < loop.length; k += 2) {
      const [lr, lc] = loop[k];
      if (allocation[lr][lc] < theta) theta = allocation[lr][lc];
    }

    // Adjust allocations along loop
    const newAlloc = allocation.map(row => [...row]);
    for (let k = 0; k < loop.length; k++) {
      const [lr, lc] = loop[k];
      if (k % 2 === 0) {
        newAlloc[lr][lc] += theta;
      } else {
        newAlloc[lr][lc] -= theta;
      }
    }

    allocation = newAlloc;
  }

  return { steps, finalCost: calcCost(allocation) };
};

// Helper: DFS to find closed orthogonal loop
function findClosedLoop(alloc, startR, startC, numRows, numCols) {
  const path = [[startR, startC]];

  function search(r, c, horizontalOnly) {
    if (horizontalOnly) {
      for (let nextC = 0; nextC < numCols; nextC++) {
        if (nextC === c) continue;
        if (nextC === startC && r === startR && path.length >= 4) {
          return true;
        }
        if (alloc[r][nextC] > 0 || (r === startR && nextC === startC)) {
          if (!path.some(([pr, pc]) => pr === r && pc === nextC)) {
            path.push([r, nextC]);
            if (search(r, nextC, false)) return true;
            path.pop();
          }
        }
      }
    } else {
      for (let nextR = 0; nextR < numRows; nextR++) {
        if (nextR === r) continue;
        if (nextR === startR && c === startC && path.length >= 4) {
          return true;
        }
        if (alloc[nextR][c] > 0 || (nextR === startR && c === startC)) {
          if (!path.some(([pr, pc]) => pr === nextR && pc === c)) {
            path.push([nextR, c]);
            if (search(nextR, c, true)) return true;
            path.pop();
          }
        }
      }
    }
    return false;
  }

  if (search(startR, startC, true) || search(startR, startC, false)) {
    return path;
  }
  return [[startR, startC]];
}


/* === FILE: src/solvers/assignmentSolver.js === */
// Assignment Problem Solver: Hungarian Method Step-by-Step

window.solveAssignment = function(problem) {
  const { agents, tasks, costs: origCosts } = problem;
  const N = agents.length;
  const steps = [];

  let matrix = origCosts.map(row => [...row]);

  // Step 0: Original Cost Matrix
  steps.push({
    stepIndex: 0,
    title: 'Initial Assignment Cost Matrix',
    description: `Original ${N}×${N} cost matrix representing cost of assigning agent i to task j.`,
    matrix: matrix.map(row => [...row]),
    phase: 'initial',
    explanation: 'Goal: Find a 1-to-1 assignment matching that minimizes overall total cost.'
  });

  // Step 1: Row Reduction
  const rowMins = matrix.map(row => Math.min(...row));
  const rowReduced = matrix.map((row, r) => row.map(val => val - rowMins[r]));
  matrix = rowReduced;

  steps.push({
    stepIndex: 1,
    title: 'Step 1: Row Minimum Reduction',
    description: 'Subtract the minimum value of each row from every element in that row. Ensures at least one zero per row.',
    matrix: matrix.map(row => [...row]),
    rowMins,
    phase: 'row-reduction',
    explanation: `Row minimums subtracted: [${rowMins.join(', ')}]. Creates opportunity zeros in each row.`
  });

  // Step 2: Column Reduction
  const colMins = [];
  for (let c = 0; c < N; c++) {
    let min = Infinity;
    for (let r = 0; r < N; r++) {
      if (matrix[r][c] < min) min = matrix[r][c];
    }
    colMins.push(min);
  }

  const colReduced = matrix.map((row) => row.map((val, c) => val - colMins[c]));
  matrix = colReduced;

  steps.push({
    stepIndex: 2,
    title: 'Step 2: Column Minimum Reduction',
    description: 'Subtract the minimum value of each column from every element in that column. Ensures at least one zero per column.',
    matrix: matrix.map(row => [...row]),
    colMins,
    phase: 'col-reduction',
    explanation: `Column minimums subtracted: [${colMins.join(', ')}]. Creates opportunity zeros in each column.`
  });

  // Step 3 & 4: Minimum Lines & Matrix Modifications
  let iter = 0;
  let linesCovered = false;

  while (iter < 4 && !linesCovered) {
    iter++;

    // Helper to compute min lines covering all zeros
    const coverage = computeMinLineCoverage(matrix, N);

    if (coverage.numLines >= N) {
      linesCovered = true;
      break;
    }

    // Uncovered minimum element k
    let minUncovered = Infinity;
    for (let r = 0; r < N; r++) {
      for (let c = 0; c < N; c++) {
        if (!coverage.coveredRows.includes(r) && !coverage.coveredCols.includes(c)) {
          if (matrix[r][c] < minUncovered) {
            minUncovered = matrix[r][c];
          }
        }
      }
    }

    // Modify Matrix: Subtract k from uncovered, add k to double-covered (intersections)
    const newMatrix = matrix.map((row, r) => row.map((val, c) => {
      const isRowCovered = coverage.coveredRows.includes(r);
      const isColCovered = coverage.coveredCols.includes(c);

      if (!isRowCovered && !isColCovered) return val - minUncovered;
      if (isRowCovered && isColCovered) return val + minUncovered;
      return val;
    }));

    steps.push({
      stepIndex: 2 + iter,
      title: `Step 3 (Iteration ${iter}): Minimum Line Coverage & Matrix Adjustment`,
      description: `Cover all zeros with minimum lines (${coverage.numLines} lines drawn < ${N} matrix size). Minimum uncovered element k = ${minUncovered}. Subtract k from uncovered cells, add k to line intersections.`,
      matrix: matrix.map(row => [...row]),
      coveredRows: coverage.coveredRows,
      coveredCols: coverage.coveredCols,
      minUncovered,
      phase: 'line-coverage',
      explanation: `Drawn ${coverage.numLines} lines (Rows: ${coverage.coveredRows.map(r=>r+1).join(',')||'None'}, Cols: ${coverage.coveredCols.map(c=>c+1).join(',')||'None'}). Adjusted matrix to generate additional zero options.`
    });

    matrix = newMatrix;
  }

  // Step 5: Final Zero Assignment Matching
  const assignments = findOptimalAssignments(matrix, N);
  let totalCost = 0;
  assignments.forEach(({ r, c }) => {
    totalCost += origCosts[r][c];
  });

  steps.push({
    stepIndex: steps.length,
    title: 'Step 4: Optimal Assignment Matching Reached!',
    description: `Identify independent zeros to establish optimal 1-to-1 matching. Total Minimum Cost = ${totalCost}.`,
    matrix: matrix.map(row => [...row]),
    assignments,
    origCosts,
    totalCost,
    phase: 'optimal',
    explanation: assignments.map(({ r, c }) => `${agents[r]} → ${tasks[c]} (Cost = ${origCosts[r][c]})`).join(' | ')
  });

  return { steps, assignments, totalCost };
};

// Helper: Line coverage heuristic
function computeMinLineCoverage(matrix, N) {
  const coveredRows = [];
  const coveredCols = [];

  // Simple heuristic: count zeros per row/col and cover line with highest zeros
  const rowZeros = matrix.map(row => row.filter(v => v === 0).length);
  const colZeros = Array(N).fill(0);
  for (let c = 0; c < N; c++) {
    for (let r = 0; r < N; r++) if (matrix[r][c] === 0) colZeros[c]++;
  }

  // Cover rows/cols
  rowZeros.forEach((cnt, r) => {
    if (cnt >= 2) coveredRows.push(r);
  });
  colZeros.forEach((cnt, c) => {
    if (cnt >= 1) {
      // Check if any uncovered zero remains in col c
      let uncoveredZero = false;
      for (let r = 0; r < N; r++) {
        if (matrix[r][c] === 0 && !coveredRows.includes(r)) uncoveredZero = true;
      }
      if (uncoveredZero) coveredCols.push(c);
    }
  });

  return {
    numLines: coveredRows.length + coveredCols.length,
    coveredRows,
    coveredCols
  };
}

// Helper: Zero assignment matcher
function findOptimalAssignments(matrix, N) {
  const assignments = [];
  const assignedRows = new Set();
  const assignedCols = new Set();

  // Greedy match rows with single zero
  for (let iter = 0; iter < N; iter++) {
    for (let r = 0; r < N; r++) {
      if (assignedRows.has(r)) continue;
      const zeroCols = [];
      for (let c = 0; c < N; c++) {
        if (matrix[r][c] === 0 && !assignedCols.has(c)) {
          zeroCols.push(c);
        }
      }
      if (zeroCols.length === 1) {
        const c = zeroCols[0];
        assignments.push({ r, c });
        assignedRows.add(r);
        assignedCols.add(c);
      }
    }
  }

  // Pick remaining zeros
  for (let r = 0; r < N; r++) {
    if (assignedRows.has(r)) continue;
    for (let c = 0; c < N; c++) {
      if (matrix[r][c] === 0 && !assignedCols.has(c)) {
        assignments.push({ r, c });
        assignedRows.add(r);
        assignedCols.add(c);
        break;
      }
    }
  }

  return assignments;
}


/* === FILE: src/solvers/shortestPathSolver.js === */
// Shortest Path Solver: Dijkstra's Algorithm with Step-by-Step Distance & Edge Relaxation

window.solveShortestPath = function(problem) {
  const { startNode, endNode, nodes, edges } = problem;
  const steps = [];

  // Initialize distance and predecessor maps
  const dist = {};
  const prev = {};
  const visited = new Set();

  nodes.forEach(n => {
    dist[n.id] = Infinity;
    prev[n.id] = null;
  });

  dist[startNode] = 0;

  steps.push({
    stepIndex: 0,
    title: 'Initialization: Set Initial Distances',
    description: `Set distance to Start Node (${startNode}) d(${startNode}) = 0. Set all other nodes d(v) = ∞. All nodes unvisited.`,
    currentNode: startNode,
    dist: { ...dist },
    prev: { ...prev },
    visited: Array.from(visited),
    activeEdge: null,
    phase: 'init',
    explanation: 'Dijkstra algorithm starting state.'
  });

  let current = startNode;

  while (current && visited.size < nodes.length) {
    visited.add(current);

    steps.push({
      stepIndex: steps.length,
      title: `Select Node (${current}) with Min Distance d(${current}) = ${dist[current]}`,
      description: `Mark node (${current}) as Visited. Explore all outgoing/adjacent edges from node (${current}).`,
      currentNode: current,
      dist: { ...dist },
      prev: { ...prev },
      visited: Array.from(visited),
      activeEdge: null,
      phase: 'select-node',
      explanation: `Permanent label assigned to node (${current}).`
    });

    if (current === endNode) {
      break; // Reached target
    }

    // Find outgoing edges from current
    const neighborEdges = edges.filter(e => e.source === current || e.target === current);

    neighborEdges.forEach(edge => {
      const neighbor = edge.source === current ? edge.target : edge.source;
      if (!visited.has(neighbor)) {
        const alt = dist[current] + edge.weight;

        const isRelaxed = alt < dist[neighbor];
        if (isRelaxed) {
          dist[neighbor] = alt;
          prev[neighbor] = current;
        }

        steps.push({
          stepIndex: steps.length,
          title: `Relax Edge (${current} → ${neighbor}, weight = ${edge.weight})`,
          description: isRelaxed
            ? `New path distance d(${current}) + ${edge.weight} = ${alt} < current d(${neighbor}) = ${dist[neighbor] !== Infinity ? dist[neighbor] : '∞'}. Update d(${neighbor}) = ${alt}, Predecessor π(${neighbor}) = ${current}.`
            : `Path via ${current} (d=${alt}) is not shorter than existing d(${neighbor}) = ${dist[neighbor]}. No update.`,
          currentNode: current,
          dist: { ...dist },
          prev: { ...prev },
          visited: Array.from(visited),
          activeEdge: edge,
          phase: 'relax-edge',
          explanation: `Triangle inequality check: d(v) = min(d(v), d(u) + w(u,v))`
        });
      }
    });

    // Select next unvisited node with min distance
    let nextNode = null;
    let minD = Infinity;

    nodes.forEach(n => {
      if (!visited.has(n.id) && dist[n.id] < minD) {
        minD = dist[n.id];
        nextNode = n.id;
      }
    });

    current = nextNode;
  }

  // Reconstruct Shortest Path
  const path = [];
  let curr = endNode;
  while (curr) {
    path.unshift(curr);
    curr = prev[curr];
  }

  const pathEdges = [];
  for (let i = 0; i < path.length - 1; i++) {
    const u = path[i];
    const v = path[i + 1];
    const e = edges.find(ed => (ed.source === u && ed.target === v) || (ed.source === v && ed.target === u));
    if (e) pathEdges.push(e);
  }

  steps.push({
    stepIndex: steps.length,
    title: 'Shortest Path Reached!',
    description: `Optimal Shortest Path from (${startNode}) to (${endNode}): ${path.join(' → ')}. Total Path Distance = ${dist[endNode]}.`,
    currentNode: endNode,
    dist: { ...dist },
    prev: { ...prev },
    visited: Array.from(visited),
    activeEdge: null,
    path,
    pathEdges,
    totalDistance: dist[endNode],
    phase: 'optimal',
    explanation: `Trace predecessors backwards from destination (${endNode}) to origin (${startNode}).`
  });

  return { steps, shortestPath: path, pathEdges, distance: dist[endNode] };
};


/* === FILE: src/solvers/mstSolver.js === */
// Minimum Spanning Tree (MST) Solver: Kruskal's & Prim's Algorithms

window.solveMST = function(problem, algorithm = 'Kruskal') {
  const { nodes, edges } = problem;
  const numNodes = nodes.length;
  const steps = [];

  if (algorithm === 'Kruskal') {
    // Step 1: Sort edges by weight
    const sortedEdges = [...edges].sort((a, b) => a.weight - b.weight);

    steps.push({
      stepIndex: 0,
      title: 'Kruskal Step 1: Sort All Edges by Weight',
      description: `Sort all ${edges.length} edges in non-decreasing order of their weights.`,
      sortedEdges,
      mstEdges: [],
      activeEdge: null,
      phase: 'init',
      explanation: 'Kruskal algorithm prioritizes lowest-cost edges regardless of location.'
    });

    // Union-Find Disjoint Set
    const parent = {};
    nodes.forEach(n => { parent[n.id] = n.id; });

    function find(i) {
      if (parent[i] === i) return i;
      return parent[i] = find(parent[i]);
    }

    function union(i, j) {
      const rootI = find(i);
      const rootJ = find(j);
      if (rootI !== rootJ) {
        parent[rootI] = rootJ;
        return true;
      }
      return false; // Cycle detected
    }

    const mstEdges = [];
    let totalWeight = 0;

    for (let i = 0; i < sortedEdges.length; i++) {
      const edge = sortedEdges[i];
      const rootSrc = find(edge.source);
      const rootTgt = find(edge.target);

      const canAdd = rootSrc !== rootTgt;

      if (canAdd) {
        union(edge.source, edge.target);
        mstEdges.push(edge);
        totalWeight += edge.weight;

        steps.push({
          stepIndex: steps.length,
          title: `Consider Edge (${edge.source} - ${edge.target}, weight = ${edge.weight})`,
          description: `Add edge (${edge.source} - ${edge.target}) to MST. Disjoint sets connected without creating a cycle. Total MST weight = ${totalWeight}.`,
          sortedEdges,
          mstEdges: [...mstEdges],
          activeEdge: edge,
          accepted: true,
          phase: 'add-edge',
          explanation: `Node ${edge.source} (Root: ${rootSrc}) and Node ${edge.target} (Root: ${rootTgt}) belong to different components. Safe to join.`
        });
      } else {
        steps.push({
          stepIndex: steps.length,
          title: `Consider Edge (${edge.source} - ${edge.target}, weight = ${edge.weight})`,
          description: `Reject edge (${edge.source} - ${edge.target}). Adding this edge would form a closed cycle in the tree.`,
          sortedEdges,
          mstEdges: [...mstEdges],
          activeEdge: edge,
          accepted: false,
          phase: 'reject-edge',
          explanation: `Both Node ${edge.source} and Node ${edge.target} already share Root: ${rootSrc}. Cycle detected!`
        });
      }

      if (mstEdges.length === numNodes - 1) break;
    }

    steps.push({
      stepIndex: steps.length,
      title: 'Kruskal MST Complete!',
      description: `Minimum Spanning Tree successfully built with ${mstEdges.length} edges connecting all ${numNodes} stations. Minimum Total Cable Length = ${totalWeight}.`,
      sortedEdges,
      mstEdges: [...mstEdges],
      activeEdge: null,
      totalWeight,
      phase: 'optimal',
      explanation: 'All nodes connected with minimum total edge weight.'
    });

    return { steps, mstEdges, totalWeight };
  } else {
    // Prim's Algorithm
    const inTree = new Set([nodes[0].id]);
    const mstEdges = [];
    let totalWeight = 0;

    steps.push({
      stepIndex: 0,
      title: `Prim Step 1: Start at Node (${nodes[0].id})`,
      description: `Initialize MST tree set with start node (${nodes[0].id}). Grow tree node by node.`,
      mstEdges: [],
      inTree: Array.from(inTree),
      activeEdge: null,
      phase: 'init',
      explanation: 'Prim algorithm expands outward from an initial root node.'
    });

    while (inTree.size < numNodes) {
      let minEdge = null;
      let minW = Infinity;

      // Find min cost edge crossing tree boundary
      edges.forEach(e => {
        const uIn = inTree.has(e.source);
        const vIn = inTree.has(e.target);
        if ((uIn && !vIn) || (!uIn && vIn)) {
          if (e.weight < minW) {
            minW = e.weight;
            minEdge = e;
          }
        }
      });

      if (!minEdge) break;

      const newVertex = inTree.has(minEdge.source) ? minEdge.target : minEdge.source;
      inTree.add(newVertex);
      mstEdges.push(minEdge);
      totalWeight += minEdge.weight;

      steps.push({
        stepIndex: steps.length,
        title: `Add Min Boundary Edge (${minEdge.source} - ${minEdge.target}, weight = ${minEdge.weight})`,
        description: `Connect Node (${newVertex}) to the growing tree using lowest weight boundary edge. Total MST weight = ${totalWeight}.`,
        mstEdges: [...mstEdges],
        inTree: Array.from(inTree),
        activeEdge: minEdge,
        phase: 'add-edge',
        explanation: `Edge (${minEdge.source}-${minEdge.target}) is the cheapest edge connecting tree set S to unvisited V-S.`
      });
    }

    steps.push({
      stepIndex: steps.length,
      title: 'Prim MST Complete!',
      description: `Minimum Spanning Tree complete with ${mstEdges.length} edges. Total MST Weight = ${totalWeight}.`,
      mstEdges: [...mstEdges],
      inTree: Array.from(inTree),
      activeEdge: null,
      totalWeight,
      phase: 'optimal',
      explanation: 'Tree spanning all nodes completed.'
    });

    return { steps, mstEdges, totalWeight };
  }
};


/* === FILE: src/components/Header.js === */
// Header Component: Navigation, Textbook Problem Switcher, Custom Input, Quiz Mode & Theme Toggle

window.Header = function({ activeTopic, setActiveTopic, selectedProblem, setSelectedProblem, onOpenCustomInput, isQuizMode, setIsQuizMode, theme, toggleTheme }) {
  const topics = [
    { id: 'lpp', label: 'Linear Programming (LPP)', icon: 'bar-chart-3', color: 'var(--color-lpp)' },
    { id: 'transportation', label: 'Transportation Problem', icon: 'truck', color: 'var(--color-transport)' },
    { id: 'assignment', label: 'Assignment Problem', icon: 'users', color: 'var(--color-assign)' },
    { id: 'shortestPath', label: 'Shortest Path', icon: 'navigation', color: 'var(--color-shortest)' },
    { id: 'mst', label: 'Minimum Spanning Tree', icon: 'git-merge', color: 'var(--color-mst)' }
  ];

  const currentProblems = window.TEXTBOOK_PROBLEMS[activeTopic] || [];

  return (
    <header className="main-header">
      <div className="brand-section">
        <div className="brand-icon">OR</div>
        <div className="brand-title">
          <h1>Optimization Learning Hub</h1>
          <p>Great Lakes PGDM / MBA Interactive Guide</p>
        </div>
      </div>

      <nav className="nav-tabs">
        {topics.map(t => (
          <button
            key={t.id}
            className={`nav-tab-btn ${activeTopic === t.id && !isQuizMode ? 'active' : ''}`}
            onClick={() => {
              setActiveTopic(t.id);
              setIsQuizMode(false);
              if (window.TEXTBOOK_PROBLEMS[t.id]) {
                setSelectedProblem(window.TEXTBOOK_PROBLEMS[t.id][0]);
              }
            }}
          >
            <span>{t.label}</span>
          </button>
        ))}
      </nav>

      <div className="header-actions">
        <button
          className={`action-btn ${isQuizMode ? 'primary' : ''}`}
          onClick={() => setIsQuizMode(!isQuizMode)}
          title="Self-Assessment Quiz Mode"
        >
          <span>🎯 Practice Quiz</span>
        </button>

        <button
          className="action-btn"
          onClick={onOpenCustomInput}
          title="Create Custom Problem"
        >
          <span>➕ Custom Input</span>
        </button>

        <button
          className="action-btn"
          onClick={toggleTheme}
          title="Toggle Light/Dark Theme"
        >
          <span>{theme === 'dark' ? '☀️ Light' : '🌙 Dark'}</span>
        </button>
      </div>
    </header>
  );
};


/* === FILE: src/components/StepControls.js === */
// StepControls Component: Interactive Step-by-Step Playback Controls

window.StepControls = function({ currentStepIndex, totalSteps, onStepChange, isPlaying, onTogglePlay, playSpeed, setPlaySpeed }) {
  const isFirst = currentStepIndex === 0;
  const isLast = currentStepIndex === totalSteps - 1;

  return (
    <div className="step-control-bar">
      <div className="step-buttons">
        <button
          className="step-btn"
          onClick={() => onStepChange(0)}
          disabled={isFirst}
          title="First Step"
        >
          ⏮
        </button>
        <button
          className="step-btn"
          onClick={() => onStepChange(currentStepIndex - 1)}
          disabled={isFirst}
          title="Previous Step"
        >
          ◀
        </button>

        <button
          className="step-btn"
          style={{ background: isPlaying ? 'var(--accent-rose)' : 'var(--accent-blue)', color: '#0b0f19', fontWeight: 700 }}
          onClick={onTogglePlay}
          title={isPlaying ? 'Pause Animation' : 'Auto Play Steps'}
        >
          {isPlaying ? '⏸' : '▶'}
        </button>

        <button
          className="step-btn"
          onClick={() => onStepChange(currentStepIndex + 1)}
          disabled={isLast}
          title="Next Step"
        >
          ▶
        </button>
        <button
          className="step-btn"
          onClick={() => onStepChange(totalSteps - 1)}
          disabled={isLast}
          title="Final Solution"
        >
          ⏭
        </button>
      </div>

      <div className="step-progress-info">
        <div className="step-counter">
          <span>Step {currentStepIndex + 1} of {totalSteps}</span>
          <span style={{ color: 'var(--text-muted)' }}>
            {Math.round(((currentStepIndex + 1) / totalSteps) * 100)}% Completed
          </span>
        </div>
        <div className="progress-bar-track">
          <div
            className="progress-bar-fill"
            style={{ width: `${((currentStepIndex + 1) / totalSteps) * 100}%` }}
          />
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
        <span>Speed:</span>
        <select
          value={playSpeed}
          onChange={(e) => setPlaySpeed(Number(e.target.value))}
          style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--bg-card-border)',
            color: 'var(--text-primary)',
            padding: '0.25rem 0.5rem',
            borderRadius: '6px',
            cursor: 'pointer'
          }}
        >
          <option value={2000}>0.5x (2s)</option>
          <option value={1000}>1.0x (1s)</option>
          <option value={500}>2.0x (0.5s)</option>
        </select>
      </div>
    </div>
  );
};


/* === FILE: src/components/InspectionModal.js === */
// InspectionModal Component: Click-to-Explain Detailed Educational Modal

window.InspectionModal = function({ isOpen, onClose, data }) {
  if (!isOpen || !data) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3 style={{ color: 'var(--accent-blue)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>💡</span> {data.title || 'Interactive Step Explanation'}
          </h3>
          <button className="modal-close-btn" onClick={onClose}>✕</button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
          {data.formula && (
            <div className="formula-box">
              <strong>Formula / Rule:</strong>
              <div>{data.formula}</div>
            </div>
          )}

          <div style={{ fontSize: '0.95rem', color: 'var(--text-primary)', lineHeight: 1.6 }}>
            {data.description}
          </div>

          {data.calculation && (
            <div style={{ background: 'rgba(255,255,255,0.04)', padding: '0.75rem', borderRadius: '8px', border: '1px solid var(--bg-card-border)', fontFamily: 'var(--font-family-mono)', fontSize: '0.85rem' }}>
              <div style={{ color: 'var(--accent-amber)', fontWeight: 600, marginBottom: '0.3rem' }}>Step-by-Step Math Derivation:</div>
              <div>{data.calculation}</div>
            </div>
          )}

          {data.textbookNote && (
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontStyle: 'italic', borderTop: '1px dashed var(--bg-card-border)', paddingTop: '0.5rem' }}>
              📚 <strong>Textbook Context:</strong> {data.textbookNote}
            </div>
          )}
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '0.5rem' }}>
          <button className="action-btn primary" onClick={onClose}>
            Got it!
          </button>
        </div>
      </div>
    </div>
  );
};


/* === FILE: src/components/CustomInputModal.js === */
// CustomInputModal Component: Ultra-Easy Student Problem Builder with Visual Grid & Templates

window.CustomInputModal = function({ isOpen, onClose, activeTopic, onSaveCustomProblem }) {
  if (!isOpen) return null;

  const [title, setTitle] = React.useState('Student Custom Problem');
  const [template, setTemplate] = React.useState('custom');

  // LPP visual state
  const [lppObjType, setLppObjType] = React.useState('max');
  const [c1, setC1] = React.useState(40);
  const [c2, setC2] = React.useState(50);
  const [var1Name, setVar1Name] = React.useState('x1 (Chairs)');
  const [var2Name, setVar2Name] = React.useState('x2 (Tables)');

  const [rows, setRows] = React.useState([
    { name: 'Raw Material', a: 1, b: 1, type: '<=', rhs: 64 },
    { name: 'Labor Hours', a: 3, b: 1, type: '<=', rhs: 120 },
    { name: 'Machine Capacity', a: 1, b: 0, type: '<=', rhs: 28 }
  ]);

  // Transportation state
  const [transSupply, setTransSupply] = React.useState('1000, 1500, 1200');
  const [transDemand, setTransDemand] = React.useState('2300, 1400');
  const [transCosts, setTransCosts] = React.useState('80, 215\n100, 108\n102, 68');

  // Assignment state
  const [assignCosts, setAssignCosts] = React.useState('13, 16, 12, 11\n15, 99, 13, 20\n5, 7, 10, 6\n0, 0, 0, 0');

  // Load Preset Templates
  const handleTemplateChange = (tplKey) => {
    setTemplate(tplKey);
    if (tplKey === 'chair-table') {
      setTitle('Product Mix: Chairs & Tables');
      setLppObjType('max');
      setC1(40); setC2(50);
      setVar1Name('x1 (Chairs)'); setVar2Name('x2 (Tables)');
      setRows([
        { name: 'Raw Material Availability', a: 1, b: 1, type: '<=', rhs: 64 },
        { name: 'Labor Hours', a: 3, b: 1, type: '<=', rhs: 120 },
        { name: 'Machine Capacity', a: 1, b: 0, type: '<=', rhs: 28 }
      ]);
    } else if (tplKey === 'diet') {
      setTitle('Diet Mix: Corn & Soybean');
      setLppObjType('min');
      setC1(0.30); setC2(0.90);
      setVar1Name('x1 (Corn lbs)'); setVar2Name('x2 (Soybean Meal lbs)');
      setRows([
        { name: 'Min Weight', a: 1, b: 1, type: '>=', rhs: 800 },
        { name: 'Min Protein (30%)', a: -0.21, b: 0.30, type: '>=', rhs: 0 },
        { name: 'Max Fiber (5%)', a: -0.03, b: 0.01, type: '<=', rhs: 0 }
      ]);
    }
  };

  const handleAddRow = () => {
    setRows([...rows, { name: `Constraint ${rows.length + 1}`, a: 1, b: 1, type: '<=', rhs: 50 }]);
  };

  const handleRemoveRow = (idx) => {
    setRows(rows.filter((_, i) => i !== idx));
  };

  const handleRowChange = (idx, field, val) => {
    const nextRows = [...rows];
    nextRows[idx][field] = val;
    setRows(nextRows);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (activeTopic === 'lpp') {
      const parsedConstraints = rows.map(r => ({
        coeffs: [parseFloat(r.a) || 0, parseFloat(r.b) || 0],
        type: r.type,
        rhs: parseFloat(r.rhs) || 0,
        name: `${r.name} (${r.a}*x1 + ${r.b}*x2 ${r.type} ${r.rhs})`
      }));

      onSaveCustomProblem({
        id: `custom-lpp-${Date.now()}`,
        title: title || 'Student Custom LPP',
        source: 'Interactive Student Builder',
        description: 'Student-formulated Linear Programming Model',
        objectiveType: lppObjType,
        objective: [parseFloat(c1) || 0, parseFloat(c2) || 0],
        variables: [var1Name, var2Name],
        constraints: parsedConstraints
      });
    } else if (activeTopic === 'transportation') {
      const supply = transSupply.split(',').map(v => parseFloat(v.trim()) || 0);
      const demand = transDemand.split(',').map(v => parseFloat(v.trim()) || 0);
      const costs = transCosts.split('\n').filter(l => l.trim()).map(l => l.split(',').map(v => parseFloat(v.trim()) || 0));

      onSaveCustomProblem({
        id: `custom-trans-${Date.now()}`,
        title: title || 'Custom Transportation Problem',
        source: 'Interactive Student Builder',
        description: 'Student-formulated Transportation Problem',
        sources: supply.map((_, i) => `Plant / Source ${i + 1}`),
        destinations: demand.map((_, i) => `Dest / Center ${i + 1}`),
        supply,
        demand,
        costs
      });
    } else if (activeTopic === 'assignment') {
      const costs = assignCosts.split('\n').filter(l => l.trim()).map(l => l.split(',').map(v => parseFloat(v.trim()) || 0));
      const N = costs.length;

      onSaveCustomProblem({
        id: `custom-assign-${Date.now()}`,
        title: title || 'Custom Assignment Problem',
        source: 'Interactive Student Builder',
        description: 'Student-formulated Assignment Problem',
        agents: Array.from({ length: N }, (_, i) => `Agent / Machine ${i + 1}`),
        tasks: Array.from({ length: N }, (_, i) => `Task / Location ${i + 1}`),
        costs
      });
    }

    onClose();
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" style={{ maxWidth: '780px' }} onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3 style={{ color: 'var(--accent-blue)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>✏️</span> Interactive Student Problem Builder ({activeTopic.toUpperCase()})
          </h3>
          <button className="modal-close-btn" onClick={onClose}>✕</button>
        </div>

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {/* Quick Preset Selector */}
          {activeTopic === 'lpp' && (
            <div style={{ background: 'rgba(2, 132, 199, 0.06)', padding: '0.75rem', borderRadius: '8px', border: '1px solid rgba(2, 132, 199, 0.2)' }}>
              <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--accent-blue)', display: 'block', marginBottom: '0.3rem' }}>
                🚀 Load Class Template (Quick Start):
              </label>
              <select
                value={template}
                onChange={(e) => handleTemplateChange(e.target.value)}
                style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', cursor: 'pointer' }}
              >
                <option value="custom">Blank Custom Problem</option>
                <option value="chair-table">Factory Chair & Table (OTDM Class Example)</option>
                <option value="diet">Diet Mix Problem (Corn & Soybean)</option>
              </select>
            </div>
          )}

          <div>
            <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', display: 'block', marginBottom: '0.2rem' }}>
              Problem Title:
            </label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
            />
          </div>

          {activeTopic === 'lpp' && (
            <>
              {/* Objective Function Row */}
              <div style={{ background: 'rgba(15,23,42,0.03)', padding: '0.8rem', borderRadius: '8px', border: '1px solid var(--bg-card-border)' }}>
                <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-primary)', display: 'block', marginBottom: '0.4rem' }}>
                  Objective Function:
                </label>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                  <select
                    value={lppObjType}
                    onChange={(e) => setLppObjType(e.target.value)}
                    style={{ padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', fontWeight: 700 }}
                  >
                    <option value="max">Maximize Z =</option>
                    <option value="min">Minimize Z =</option>
                  </select>
                  <input
                    type="number" step="any"
                    value={c1} onChange={(e) => setC1(e.target.value)}
                    style={{ width: '70px', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', textAlign: 'center' }}
                  />
                  <span>x₁ +</span>
                  <input
                    type="number" step="any"
                    value={c2} onChange={(e) => setC2(e.target.value)}
                    style={{ width: '70px', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', textAlign: 'center' }}
                  />
                  <span>x₂</span>
                </div>
              </div>

              {/* Variable Names */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem' }}>
                <div>
                  <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Variable x₁ Name:</label>
                  <input
                    type="text" value={var1Name} onChange={(e) => setVar1Name(e.target.value)}
                    style={{ width: '100%', padding: '0.4rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                  />
                </div>
                <div>
                  <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Variable x₂ Name:</label>
                  <input
                    type="text" value={var2Name} onChange={(e) => setVar2Name(e.target.value)}
                    style={{ width: '100%', padding: '0.4rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                  />
                </div>
              </div>

              {/* Interactive Resource Constraints Grid */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.4rem' }}>
                  <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-primary)' }}>
                    Resource Constraints Table:
                  </label>
                  <button type="button" className="action-btn" onClick={handleAddRow} style={{ fontSize: '0.75rem', padding: '0.2rem 0.5rem' }}>
                    + Add Constraint Row
                  </button>
                </div>

                <div className="matrix-container">
                  <table className="custom-table" style={{ fontSize: '0.85rem' }}>
                    <thead>
                      <tr>
                        <th>Resource Name</th>
                        <th>x₁ Coeff (a)</th>
                        <th>x₂ Coeff (b)</th>
                        <th>Type</th>
                        <th>RHS (b_i)</th>
                        <th>Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {rows.map((r, idx) => (
                        <tr key={idx}>
                          <td>
                            <input
                              type="text" value={r.name} onChange={(e) => handleRowChange(idx, 'name', e.target.value)}
                              style={{ width: '100%', padding: '0.3rem', background: 'transparent', border: 'none', color: 'var(--text-primary)', fontWeight: 600 }}
                            />
                          </td>
                          <td>
                            <input
                              type="number" step="any" value={r.a} onChange={(e) => handleRowChange(idx, 'a', e.target.value)}
                              style={{ width: '60px', padding: '0.3rem', background: 'transparent', border: 'none', textAlign: 'center', color: 'var(--text-primary)' }}
                            />
                          </td>
                          <td>
                            <input
                              type="number" step="any" value={r.b} onChange={(e) => handleRowChange(idx, 'b', e.target.value)}
                              style={{ width: '60px', padding: '0.3rem', background: 'transparent', border: 'none', textAlign: 'center', color: 'var(--text-primary)' }}
                            />
                          </td>
                          <td>
                            <select
                              value={r.type} onChange={(e) => handleRowChange(idx, 'type', e.target.value)}
                              style={{ padding: '0.2rem', background: 'transparent', border: 'none', color: 'var(--text-primary)', fontWeight: 700 }}
                            >
                              <option value="<=">&le; (<=)</option>
                              <option value=">=">&ge; (>=)</option>
                              <option value="=">= (=)</option>
                            </select>
                          </td>
                          <td>
                            <input
                              type="number" step="any" value={r.rhs} onChange={(e) => handleRowChange(idx, 'rhs', e.target.value)}
                              style={{ width: '70px', padding: '0.3rem', background: 'transparent', border: 'none', textAlign: 'center', color: 'var(--accent-amber)', fontWeight: 700 }}
                            />
                          </td>
                          <td>
                            {rows.length > 1 && (
                              <button type="button" onClick={() => handleRemoveRow(idx)} style={{ background: 'transparent', border: 'none', color: 'var(--accent-rose)', cursor: 'pointer', fontWeight: 800 }}>
                                ✕
                              </button>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </>
          )}

          {activeTopic === 'transportation' && (
            <>
              <div>
                <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Plant Capacities / Supply (Comma-separated):</label>
                <input
                  type="text" value={transSupply} onChange={(e) => setTransSupply(e.target.value)}
                  style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Distribution Demands (Comma-separated):</label>
                <input
                  type="text" value={transDemand} onChange={(e) => setTransDemand(e.target.value)}
                  style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px' }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Transportation Costs Matrix (Rows by line, comma-separated):</label>
                <textarea
                  rows={3} value={transCosts} onChange={(e) => setTransCosts(e.target.value)}
                  style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', fontFamily: 'var(--font-family-mono)' }}
                />
              </div>
            </>
          )}

          {activeTopic === 'assignment' && (
            <div>
              <label style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Assignment Cost Matrix N×N (Rows by line, comma-separated):</label>
              <textarea
                rows={4} value={assignCosts} onChange={(e) => setAssignCosts(e.target.value)}
                style={{ width: '100%', padding: '0.5rem', background: 'var(--bg-surface)', border: '1px solid var(--bg-card-border)', color: 'var(--text-primary)', borderRadius: '6px', fontFamily: 'var(--font-family-mono)' }}
              />
            </div>
          )}

          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.5rem', marginTop: '0.5rem' }}>
            <button type="button" className="action-btn" onClick={onClose}>Cancel</button>
            <button type="submit" className="action-btn primary">✨ Generate Interactive Solution</button>
          </div>
        </form>
      </div>
    </div>
  );
};


/* === FILE: src/components/QuizModeView.js === */
// QuizModeView Component: Interactive Self-Assessment Quiz for MBA/PGDM Students

window.QuizModeView = function() {
  const quizQuestions = [
    {
      id: 1,
      topic: 'Linear Programming (LPP)',
      question: 'In the Simplex Method for a Maximization problem, when is the current basic feasible solution optimal?',
      options: [
        'A) All Cj - Zj indicators are positive (> 0)',
        'B) All Cj - Zj indicators are non-positive (≤ 0)',
        'C) When slack variables equal zero',
        'D) When artificial variables enter the basis'
      ],
      correctAnswer: 1,
      explanation: 'Optimality Criterion: For a maximization problem, if all net evaluations Cj - Zj ≤ 0, no non-basic variable can enter the basis to increase Z further.'
    },
    {
      id: 2,
      topic: 'Transportation Problem',
      question: 'In Vogel\'s Approximation Method (VAM), how is the row/column penalty calculated?',
      options: [
        'A) Maximum cost minus minimum cost in that line',
        'B) Difference between the two lowest costs in that row or column',
        'C) Average of all costs in that row or column',
        'D) Total supply minus total demand'
      ],
      correctAnswer: 1,
      explanation: 'VAM penalties represent opportunity loss: the difference between the lowest unit cost and the next lowest unit cost in a line.'
    },
    {
      id: 3,
      topic: 'Transportation Problem (MODI)',
      question: 'In the u-v (MODI) method, an unallocated cell has opportunity cost Δij = cij - (ui + vj). If Δij < 0 for a cell in a minimization problem, what does it signify?',
      options: [
        'A) The current solution is optimal',
        'B) Allocating units to this cell will INCREASE total shipping cost',
        'C) Allocating units to this cell will DECREASE total shipping cost',
        'D) The problem is degenerate'
      ],
      correctAnswer: 2,
      explanation: 'In MODI, a negative opportunity cost Δij < 0 indicates that introducing this route will reduce total transportation cost.'
    },
    {
      id: 4,
      topic: 'Assignment Problem',
      question: 'In the Hungarian Method for an N×N cost matrix, when is the current matrix optimal?',
      options: [
        'A) When every row has at least two zeros',
        'B) When minimum lines needed to cover all zeros equals N',
        'C) When all entries in the matrix are non-negative',
        'D) When all diagonal elements equal zero'
      ],
      correctAnswer: 1,
      explanation: 'König\'s theorem: Maximum number of independent zero assignments equals the minimum number of lines covering all zeros. When lines = N, a complete 1-to-1 optimal assignment exists.'
    },
    {
      id: 5,
      topic: 'Network Models (MST vs Shortest Path)',
      question: 'What is the primary distinction between a Minimum Spanning Tree (MST) and a Shortest Path between two nodes?',
      options: [
        'A) MST minimizes total edge weight connecting ALL nodes; Shortest Path minimizes weight along a path between a specific SOURCE and TARGET',
        'B) MST allows cycles; Shortest Path is strictly acyclic',
        'C) Dijkstra algorithm solves MST; Kruskal solves Shortest Path',
        'D) MST requires directed graphs; Shortest Path requires undirected graphs'
      ],
      correctAnswer: 0,
      explanation: 'MST spans the entire graph with minimum total weight. Shortest path optimizes distance between a specific pair of nodes.'
    }
  ];

  const [currentQ, setCurrentQ] = React.useState(0);
  const [selectedOpt, setSelectedOpt] = React.useState(null);
  const [score, setScore] = React.useState(0);
  const [showResult, setShowResult] = React.useState(false);

  const q = quizQuestions[currentQ];

  const handleSelectOption = (idx) => {
    if (selectedOpt !== null) return; // Prevent re-click
    setSelectedOpt(idx);
    if (idx === q.correctAnswer) {
      setScore(score + 1);
    }
  };

  const handleNext = () => {
    if (currentQ < quizQuestions.length - 1) {
      setCurrentQ(currentQ + 1);
      setSelectedOpt(null);
    } else {
      setShowResult(true);
    }
  };

  const handleRestart = () => {
    setCurrentQ(0);
    setSelectedOpt(null);
    setScore(0);
    setShowResult(false);
  };

  if (showResult) {
    return (
      <div className="card" style={{ maxWidth: '700px', margin: '2rem auto', textAlign: 'center' }}>
        <h2 style={{ color: 'var(--accent-blue)', marginBottom: '1rem' }}>🎉 Quiz Completed!</h2>
        <div style={{ fontSize: '2.5rem', fontWeight: 800, color: 'var(--accent-emerald)', margin: '1rem 0' }}>
          {score} / {quizQuestions.length}
        </div>
        <p style={{ color: 'var(--text-secondary)', marginBottom: '1.5rem' }}>
          {score === quizQuestions.length
            ? '🏆 Outstanding! Perfect score in Operations Research concepts.'
            : score >= 3
            ? '👍 Great effort! Review step-by-step solver explanations to master remaining concepts.'
            : '📚 Keep practicing! Use the step-by-step guide to review algorithms.'}
        </p>
        <button className="action-btn primary" style={{ margin: '0 auto' }} onClick={handleRestart}>
          Try Quiz Again
        </button>
      </div>
    );
  }

  return (
    <div className="card" style={{ maxWidth: '800px', margin: '1rem auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <span className="source-badge">Concept Quiz {currentQ + 1} of {quizQuestions.length}</span>
        <span style={{ fontSize: '0.85rem', color: 'var(--accent-indigo)', fontWeight: 600 }}>{q.topic}</span>
      </div>

      <h3 style={{ fontSize: '1.1rem', marginBottom: '1.25rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
        {q.question}
      </h3>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.6rem', marginBottom: '1.25rem' }}>
        {q.options.map((opt, idx) => {
          let stateClass = '';
          if (selectedOpt !== null) {
            if (idx === q.correctAnswer) stateClass = 'correct';
            else if (idx === selectedOpt) stateClass = 'wrong';
          }
          return (
            <button
              key={idx}
              className={`quiz-option-btn ${stateClass}`}
              onClick={() => handleSelectOption(idx)}
            >
              {opt}
            </button>
          );
        })}
      </div>

      {selectedOpt !== null && (
        <div style={{ background: 'rgba(56, 189, 248, 0.1)', border: '1px solid var(--accent-blue)', borderRadius: '8px', padding: '0.9rem', marginBottom: '1rem' }}>
          <div style={{ fontWeight: 700, color: selectedOpt === q.correctAnswer ? 'var(--accent-emerald)' : 'var(--accent-rose)', marginBottom: '0.3rem' }}>
            {selectedOpt === q.correctAnswer ? '✅ Correct Answer!' : '❌ Incorrect'}
          </div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)' }}>
            {q.explanation}
          </div>
        </div>
      )}

      {selectedOpt !== null && (
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
          <button className="action-btn primary" onClick={handleNext}>
            {currentQ < quizQuestions.length - 1 ? 'Next Question ▶' : 'See Results 🏆'}
          </button>
        </div>
      )}
    </div>
  );
};


/* === FILE: src/components/LPPView.js === */
// LPPView Component: PPT-Style Formulation Table, 2D Vector Plotter & Simplex Visualizer

window.LPPView = function({ problem, currentStepIndex, onCellClick }) {
  const [method, setMethod] = React.useState('ppt-formulation'); // 'ppt-formulation', 'simplex', 'graphical'

  const simplexRes = React.useMemo(() => {
    return window.solveLPPSimplex(problem);
  }, [problem]);

  const graphicalRes = React.useMemo(() => {
    return window.solveLPPGraphical(problem);
  }, [problem]);

  const simplexStep = simplexRes.steps[Math.min(currentStepIndex, simplexRes.steps.length - 1)] || simplexRes.steps[0];
  const graphicalStep = graphicalRes.steps[Math.min(currentStepIndex, graphicalRes.steps.length - 1)] || graphicalRes.steps[0];

  const obj = problem.objective || [0, 0];
  const vars = problem.variables || ['x₁', 'x₂'];
  const objType = problem.objectiveType ? problem.objectiveType.toUpperCase() : 'MAX';

  // Iso-profit slope calculation
  const isoSlope = obj[1] !== 0 ? (-obj[0] / obj[1]).toFixed(2) : 'Undefined';

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {/* View Method Switcher */}
      <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <button
          className={`action-btn ${method === 'ppt-formulation' ? 'primary' : ''}`}
          onClick={() => setMethod('ppt-formulation')}
        >
          📋 Course PPT Model Formulation
        </button>
        <button
          className={`action-btn ${method === 'simplex' ? 'primary' : ''}`}
          onClick={() => setMethod('simplex')}
        >
          📊 Simplex Method (Tableau)
        </button>
        <button
          className={`action-btn ${method === 'graphical' ? 'primary' : ''}`}
          onClick={() => setMethod('graphical')}
        >
          📈 Graphical Method (2D Plane)
        </button>
      </div>

      {method === 'ppt-formulation' && (
        <div className="card">
          <div className="explanation-title">
            <h3>📖 Structured LPP Model Formulation (Course PPT Standard)</h3>
            <span className="source-badge">{problem.source}</span>
          </div>

          {/* Decision Variable Definition Box */}
          <div style={{ background: 'rgba(2, 132, 199, 0.05)', border: '1px solid rgba(2, 132, 199, 0.2)', padding: '1rem', borderRadius: '8px', margin: '0.8rem 0' }}>
            <h4 style={{ color: 'var(--accent-blue)', marginBottom: '0.4rem' }}>1. Decision Variables Definition:</h4>
            <div style={{ display: 'flex', gap: '1.5rem', fontSize: '0.9rem' }}>
              <div><strong>x₁:</strong> {vars[0]}</div>
              <div><strong>x₂:</strong> {vars[1]}</div>
            </div>
          </div>

          {/* Slide 24/25 PPT Parameter Grid Table */}
          <h4 style={{ color: 'var(--text-primary)', marginTop: '1rem', marginBottom: '0.4rem' }}>2. Resource Usage & Profit Matrix (PPT Slide 24/25 Table):</h4>
          <div className="matrix-container">
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Resource i</th>
                  <th>Activity 1 ({vars[0]})</th>
                  <th>Activity 2 ({vars[1]})</th>
                  <th>Resource Available (b_i)</th>
                  <th>Constraint Equation</th>
                </tr>
              </thead>
              <tbody>
                {problem.constraints.map((c, idx) => (
                  <tr key={idx}>
                    <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>
                      {c.name ? c.name.split('(')[0] : `Resource ${idx + 1}`}
                    </td>
                    <td style={{ fontWeight: 600 }}>{c.coeffs[0]}</td>
                    <td style={{ fontWeight: 600 }}>{c.coeffs[1]}</td>
                    <td style={{ fontWeight: 700, color: 'var(--accent-amber)' }}>{c.type} {c.rhs}</td>
                    <td style={{ fontFamily: 'var(--font-family-mono)', color: 'var(--text-secondary)' }}>
                      {c.coeffs[0]}x₁ + {c.coeffs[1]}x₂ {c.type} {c.rhs}
                    </td>
                  </tr>
                ))}
                <tr style={{ background: 'rgba(5, 150, 105, 0.1)', fontWeight: 700 }}>
                  <td style={{ color: 'var(--accent-emerald)' }}>Unit Contribution (c_j)</td>
                  <td style={{ color: 'var(--accent-emerald)' }}>${obj[0]}</td>
                  <td style={{ color: 'var(--accent-emerald)' }}>${obj[1]}</td>
                  <td colSpan={2} style={{ color: 'var(--accent-emerald)', textAlign: 'left', paddingLeft: '1rem' }}>
                    <strong>Objective:</strong> {objType} Z = ${obj[0]}x₁ + ${obj[1]}x₂
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          {/* Iso-Profit Slope & Constraint Slope Analysis Box */}
          <div style={{ background: 'rgba(217, 119, 6, 0.08)', border: '1px solid var(--accent-amber)', borderRadius: '8px', padding: '1rem', marginTop: '1rem' }}>
            <h4 style={{ color: 'var(--accent-amber)', marginBottom: '0.4rem' }}>3. Slope Analysis & Solvability (Course PPT Standard):</h4>
            <div style={{ fontSize: '0.85rem', lineHeight: 1.6 }}>
              <div>• <strong>Objective Iso-Profit Line Equation:</strong> {obj[0]}x₁ + {obj[1]}x₂ = Z ➔ Slope m_Z = -c₁/c₂ = <strong>{isoSlope}</strong></div>
              {problem.pptDetails && problem.pptDetails.slopes && (
                <div style={{ marginTop: '0.4rem' }}>
                  <strong>Constraint Slopes (m = -a₁/a₂):</strong>
                  <ul style={{ paddingLeft: '1.2rem', marginTop: '0.2rem' }}>
                    {problem.pptDetails.slopes.map((s, i) => (
                      <li key={i}>{s.name}: <strong>Slope m = {s.slope}</strong></li>
                    ))}
                  </ul>
                </div>
              )}
              {problem.pptDetails && problem.pptDetails.cornerPointsNote && (
                <div style={{ marginTop: '0.5rem', color: 'var(--accent-emerald)', fontWeight: 600 }}>
                  💡 {problem.pptDetails.cornerPointsNote}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {method === 'simplex' && (
        <div className="card">
          <div className="explanation-title">
            <h3>{simplexStep.title}</h3>
            <span className="click-hint-badge">💡 Click cell to inspect formula</span>
          </div>
          <p className="explanation-text">{simplexStep.description}</p>

          {/* Simplex Tableau */}
          {simplexStep.tableau && (
            <div className="matrix-container">
              <table className="custom-table">
                <thead>
                  <tr>
                    <th>Basis</th>
                    <th>C_b</th>
                    {simplexStep.colNames.map((name, j) => (
                      <th key={j} style={{ color: j === simplexStep.pivotCol ? 'var(--accent-emerald)' : 'inherit' }}>
                        {name} {j === simplexStep.pivotCol ? '⤓' : ''}
                      </th>
                    ))}
                    <th>Solution (RHS)</th>
                    {simplexStep.ratios && <th>Ratio Test (b_i / a_ij)</th>}
                  </tr>
                </thead>
                <tbody>
                  {simplexStep.tableau.map((row, r) => {
                    const basisVarIndex = simplexStep.basis[r];
                    const basisName = simplexStep.colNames[basisVarIndex];
                    const cb = simplexStep.cj[basisVarIndex] || 0;
                    const isPivotRow = r === simplexStep.pivotRow;

                    return (
                      <tr key={r} style={{ background: isPivotRow ? 'rgba(225, 29, 72, 0.08)' : 'transparent' }}>
                        <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>{basisName}</td>
                        <td>{cb}</td>
                        {row.slice(0, simplexStep.colNames.length).map((val, c) => {
                          const isPivotCell = r === simplexStep.pivotRow && c === simplexStep.pivotCol;
                          const isEnteringCol = c === simplexStep.pivotCol;
                          const isLeavingRow = r === simplexStep.pivotRow;

                          let cellClass = '';
                          if (isPivotCell) cellClass = 'cell-pivot';
                          else if (isEnteringCol) cellClass = 'cell-entering';
                          else if (isLeavingRow) cellClass = 'cell-leaving';

                          return (
                            <td
                              key={c}
                              className={cellClass}
                              onClick={() => onCellClick({
                                title: `Tableau Cell [${basisName}, ${simplexStep.colNames[c]}]`,
                                formula: `Value = ${val.toFixed(2)}`,
                                description: isPivotCell
                                  ? `PIVOT ELEMENT = ${val.toFixed(2)}. This element will be normalized to 1 in the next tableau.`
                                  : `Current tableau coefficient for variable ${simplexStep.colNames[c]} in row ${basisName}.`,
                                calculation: `CB = ${cb}, Variable = ${simplexStep.colNames[c]}`
                              })}
                            >
                              {val.toFixed(2)}
                            </td>
                          );
                        })}
                        <td style={{ fontWeight: 700 }}>{row[simplexStep.colNames.length].toFixed(2)}</td>
                        {simplexStep.ratios && (
                          <td style={{ color: isPivotRow ? 'var(--accent-amber)' : 'var(--text-muted)', fontWeight: isPivotRow ? 700 : 400 }}>
                            {simplexStep.ratios[r] !== null ? simplexStep.ratios[r].toFixed(2) : '— (N/A)'}
                          </td>
                        )}
                      </tr>
                    );
                  })}

                  {/* Indicator Rows */}
                  {simplexStep.zj && (
                    <tr style={{ background: 'rgba(15,23,42,0.04)', fontWeight: 600 }}>
                      <td colSpan={2}>Z_j</td>
                      {simplexStep.zj.slice(0, simplexStep.colNames.length).map((val, c) => (
                        <td key={c}>{val.toFixed(2)}</td>
                      ))}
                      <td style={{ color: 'var(--accent-emerald)', fontSize: '1rem' }}>{simplexStep.currentZ.toFixed(2)}</td>
                      {simplexStep.ratios && <td>—</td>}
                    </tr>
                  )}
                  {simplexStep.cj_zj && (
                    <tr style={{ background: 'rgba(2, 132, 199, 0.08)', fontWeight: 700 }}>
                      <td colSpan={2} style={{ color: 'var(--accent-blue)' }}>C_j - Z_j</td>
                      {simplexStep.cj_zj.map((val, c) => (
                        <td key={c} style={{ color: c === simplexStep.pivotCol ? 'var(--accent-emerald)' : 'inherit' }}>
                          {val.toFixed(2)}
                        </td>
                      ))}
                      <td>—</td>
                      {simplexStep.ratios && <td>—</td>}
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}

      {method === 'graphical' && (
        <div className="card">
          <div className="explanation-title">
            <h3>{graphicalStep.title}</h3>
          </div>
          <p className="explanation-text">{graphicalStep.description}</p>

          <div className="network-canvas-wrapper" style={{ marginTop: '1rem' }}>
            <svg viewBox="-20 -20 440 340" className="network-svg">
              <line x1="0" y1="300" x2="400" y2="300" stroke="var(--text-muted)" strokeWidth="2" />
              <line x1="0" y1="0" x2="0" y2="300" stroke="var(--text-muted)" strokeWidth="2" />

              <text x="390" y="290" fill="var(--text-secondary)" fontSize="12" fontWeight="700">x₁</text>
              <text x="10" y="15" fill="var(--text-secondary)" fontSize="12" fontWeight="700">x₂</text>

              {[1, 2, 3, 4, 5, 6, 7, 8].map(tick => (
                <g key={tick}>
                  <line x1={tick * 45} y1="295" x2={tick * 45} y2="305" stroke="var(--text-muted)" />
                  <text x={tick * 45} y="318" fill="var(--text-muted)" fontSize="10" textAnchor="middle">{tick * 5}</text>
                  <line x1="-5" y1={300 - tick * 35} x2="5" y2={300 - tick * 35} stroke="var(--text-muted)" />
                  <text x="-12" y={300 - tick * 35 + 4} fill="var(--text-muted)" fontSize="10" textAnchor="end">{tick * 5}</text>
                </g>
              ))}

              {graphicalRes.lines.map((line, idx) => {
                const x1 = 0;
                const y1 = line.yIntercept !== null ? 300 - (line.yIntercept / 5) * 35 : 0;
                const x2 = line.xIntercept !== null ? (line.xIntercept / 5) * 45 : 400;
                const y2 = 300;

                const colors = ['#0284c7', '#d97706', '#9333ea', '#059669'];
                const col = colors[idx % colors.length];

                return (
                  <g key={idx}>
                    <line x1={x1} y1={y1} x2={x2} y2={y2} stroke={col} strokeWidth="3" strokeDasharray="4 2" />
                    <text x={x2 > 350 ? 320 : x2 + 5} y={y1 + 15} fill={col} fontSize="11" fontWeight="600">
                      {line.name}
                    </text>
                  </g>
                );
              })}

              {graphicalRes.evaluatedPoints.length > 0 && (
                <polygon
                  points={graphicalRes.evaluatedPoints.map(pt => `${(pt.x / 5) * 45},${300 - (pt.y / 5) * 35}`).join(' ')}
                  fill="rgba(2, 132, 199, 0.2)"
                  stroke="var(--accent-blue)"
                  strokeWidth="2"
                />
              )}

              {graphicalRes.evaluatedPoints.map((pt, idx) => {
                const cx = (pt.x / 5) * 45;
                const cy = 300 - (pt.y / 5) * 35;
                const isBest = graphicalRes.optimalPoint && Math.abs(pt.x - graphicalRes.optimalPoint.x) < 1e-4 && Math.abs(pt.y - graphicalRes.optimalPoint.y) < 1e-4;

                return (
                  <g key={idx} cursor="pointer" onClick={() => onCellClick({
                    title: `Corner Point (${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`,
                    formula: `Z = ${problem.objective[0]}×(${pt.x.toFixed(2)}) + ${problem.objective[1]}×(${pt.y.toFixed(2)}) = ${pt.z.toFixed(2)}`,
                    description: isBest ? 'OPTIMAL VERTEX! Yields maximum objective value.' : 'Feasible corner vertex point.',
                    calculation: `Source: ${pt.source}`
                  })}>
                    <circle cx={cx} cy={cy} r={isBest ? 7 : 5} fill={isBest ? 'var(--accent-amber)' : 'var(--accent-emerald)'} stroke="#fff" strokeWidth="2" />
                    <text x={cx + 10} y={cy - 5} fill="var(--text-primary)" fontSize="11" fontWeight="700">
                      ({pt.x.toFixed(1)}, {pt.y.toFixed(1)}) Z={pt.z.toFixed(1)}
                    </text>
                  </g>
                );
              })}
            </svg>
          </div>
        </div>
      )}
    </div>
  );
};


/* === FILE: src/components/TransportationView.js === */
// TransportationView Component: IBFS Solvers & MODI u-v Closed Loop Visualizer

window.TransportationView = function({ problem, currentStepIndex, onCellClick }) {
  const [ibfsMethod, setIbfsMethod] = React.useState('VAM');

  const solverRes = React.useMemo(() => {
    return window.solveTransportation(problem, ibfsMethod);
  }, [problem, ibfsMethod]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { sources, destinations, supply, demand, costs } = problem;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {/* IBFS Method Switcher */}
      <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <button
          className={`action-btn ${ibfsMethod === 'VAM' ? 'primary' : ''}`}
          onClick={() => setIbfsMethod('VAM')}
        >
          ⭐ Vogel's Approx Method (VAM)
        </button>
        <button
          className={`action-btn ${ibfsMethod === 'LCM' ? 'primary' : ''}`}
          onClick={() => setIbfsMethod('LCM')}
        >
          🏷️ Least Cost Method (LCM)
        </button>
        <button
          className={`action-btn ${ibfsMethod === 'NWCM' ? 'primary' : ''}`}
          onClick={() => setIbfsMethod('NWCM')}
        >
          ↖️ Northwest Corner Method (NWCM)
        </button>
      </div>

      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click cell to view u-v math</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* Transportation Matrix Grid */}
        <div className="matrix-container" style={{ marginTop: '1rem' }}>
          <table className="custom-table">
            <thead>
              <tr>
                <th>Sources \ Dests</th>
                {destinations.map((d, c) => (
                  <th key={c}>
                    {d}
                    {currentStep.v && (
                      <div style={{ fontSize: '0.75rem', color: 'var(--accent-emerald)', fontWeight: 600 }}>
                        v_{c+1} = {currentStep.v[c]}
                      </div>
                    )}
                  </th>
                ))}
                <th>Supply</th>
                {currentStep.u && <th>u_i</th>}
              </tr>
            </thead>
            <tbody>
              {sources.map((src, r) => (
                <tr key={r}>
                  <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>{src}</td>
                  {destinations.map((_, c) => {
                    const costVal = costs[r][c];
                    const allocVal = currentStep.allocation ? currentStep.allocation[r][c] : 0;
                    const deltaVal = currentStep.delta ? currentStep.delta[r][c] : null;

                    const isEntering = currentStep.enteringR === r && currentStep.enteringC === c;
                    const isInLoop = currentStep.loop && currentStep.loop.some(([lr, lc]) => lr === r && lc === c);

                    let cellClass = '';
                    if (isEntering) cellClass = 'cell-pivot';
                    else if (allocVal > 0) cellClass = 'cell-allocated';

                    return (
                      <td
                        key={c}
                        className={cellClass}
                        style={{ position: 'relative', height: '65px' }}
                        onClick={() => onCellClick({
                          title: `Cell [${src} → ${destinations[c]}]`,
                          formula: `Cost c_{${r+1}${c+1}} = $${costVal}`,
                          description: allocVal > 0
                            ? `ALLOCATED: ${allocVal} units shipped on this route. Total route cost = $${allocVal * costVal}.`
                            : deltaVal !== null
                            ? `UNALLOCATED: Opportunity cost Δ_{${r+1}${c+1}} = c_{${r+1}${c+1}} - (u_${r+1} + v_${c+1}) = ${costVal} - (${currentStep.u[r]} + ${currentStep.v[c]}) = ${deltaVal.toFixed(1)}.`
                            : `Unallocated route with unit shipping cost $${costVal}.`,
                          calculation: `Supply = ${supply[r]}, Demand = ${demand[c]}`
                        })}
                      >
                        {/* Unit cost badge */}
                        <div style={{ position: 'absolute', top: 4, right: 6, fontSize: '0.7rem', color: 'var(--accent-amber)', background: 'rgba(0,0,0,0.3)', padding: '1px 4px', borderRadius: '4px' }}>
                          ${costVal}
                        </div>

                        {/* Allocated Units */}
                        {allocVal > 0 ? (
                          <div style={{ fontSize: '1.1rem', fontWeight: 800, color: 'var(--accent-blue)', marginTop: '8px' }}>
                            [{allocVal}]
                          </div>
                        ) : deltaVal !== null ? (
                          <div style={{ fontSize: '0.8rem', color: deltaVal < 0 ? 'var(--accent-rose)' : 'var(--text-muted)', marginTop: '12px' }}>
                            Δ = {deltaVal.toFixed(1)}
                          </div>
                        ) : null}

                        {/* Loop Sign Indicator */}
                        {isInLoop && (
                          <div style={{ position: 'absolute', bottom: 2, left: 6, fontSize: '0.75rem', fontWeight: 800, color: 'var(--accent-amber)' }}>
                            {currentStep.loop.findIndex(([lr, lc]) => lr === r && lc === c) % 2 === 0 ? '+θ' : '-θ'}
                          </div>
                        )}
                      </td>
                    );
                  })}
                  <td style={{ fontWeight: 700 }}>{supply[r]}</td>
                  {currentStep.u && (
                    <td style={{ color: 'var(--accent-emerald)', fontWeight: 600 }}>u_{r+1} = {currentStep.u[r]}</td>
                  )}
                </tr>
              ))}

              {/* Demand Row */}
              <tr style={{ background: 'rgba(0,0,0,0.3)', fontWeight: 700 }}>
                <td style={{ color: 'var(--text-secondary)' }}>Demand</td>
                {demand.map((d, c) => (
                  <td key={c}>{d}</td>
                ))}
                <td style={{ color: 'var(--accent-emerald)' }}>
                  {supply.reduce((a, b) => a + b, 0)} (Total)
                </td>
                {currentStep.u && <td>—</td>}
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};


/* === FILE: src/components/AssignmentView.js === */
// AssignmentView Component: Hungarian Method Interactive Matrix & Zero Matching Visualizer

window.AssignmentView = function({ problem, currentStepIndex, onCellClick }) {
  const solverRes = React.useMemo(() => {
    return window.solveAssignment(problem);
  }, [problem]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { agents, tasks, costs: origCosts } = problem;
  const N = agents.length;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click cell to inspect Hungarian reduction</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* Matrix Grid */}
        <div className="matrix-container" style={{ marginTop: '1rem' }}>
          <table className="custom-table">
            <thead>
              <tr>
                <th>Agents \ Tasks</th>
                {tasks.map((t, c) => (
                  <th key={c}>
                    {t}
                    {currentStep.colMins && (
                      <div style={{ fontSize: '0.75rem', color: 'var(--accent-purple)', fontWeight: 600 }}>
                        Min = {currentStep.colMins[c]}
                      </div>
                    )}
                  </th>
                ))}
                {currentStep.rowMins && <th>Row Min</th>}
              </tr>
            </thead>
            <tbody>
              {agents.map((agent, r) => (
                <tr key={r}>
                  <td style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>{agent}</td>
                  {tasks.map((task, c) => {
                    const val = currentStep.matrix ? currentStep.matrix[r][c] : origCosts[r][c];

                    const isRowCovered = currentStep.coveredRows && currentStep.coveredRows.includes(r);
                    const isColCovered = currentStep.coveredCols && currentStep.coveredCols.includes(c);
                    const isAssigned = currentStep.assignments && currentStep.assignments.some(a => a.r === r && a.c === c);

                    let cellClass = '';
                    if (isAssigned) cellClass = 'cell-zero-match';
                    else if (isRowCovered || isColCovered) cellClass = 'cell-covered-line';

                    return (
                      <td
                        key={c}
                        className={cellClass}
                        style={{ position: 'relative' }}
                        onClick={() => onCellClick({
                          title: `Cell [${agent} → ${task}]`,
                          formula: `Current Value = ${val}`,
                          description: isAssigned
                            ? `MATCHED ASSIGNMENT! Agent ${agent} is assigned to ${task} with original cost = $${origCosts[r][c]}.`
                            : val === 0
                            ? `OPPORTUNITY ZERO: Candidate assignment option.`
                            : `Reduced cost cell value after row/column transformations.`,
                          calculation: `Original Cost = $${origCosts[r][c]}, Current Reduced Value = ${val}`
                        })}
                      >
                        {val}
                        {isAssigned && (
                          <div style={{ fontSize: '0.7rem', color: 'var(--accent-purple)', fontWeight: 800 }}>
                            ★ MATCH
                          </div>
                        )}
                      </td>
                    );
                  })}
                  {currentStep.rowMins && (
                    <td style={{ color: 'var(--accent-purple)', fontWeight: 600 }}>
                      {currentStep.rowMins[r]}
                    </td>
                  )}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Final Optimal Assignment Summary */}
        {currentStep.assignments && (
          <div style={{ marginTop: '1rem', background: 'rgba(192, 132, 252, 0.1)', border: '1px solid var(--accent-purple)', borderRadius: '8px', padding: '1rem' }}>
            <h4 style={{ color: 'var(--accent-purple)', marginBottom: '0.5rem' }}>🎯 Optimal Job-Machine Assignment Pairs:</h4>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.5rem' }}>
              {currentStep.assignments.map(({ r, c }, idx) => (
                <div key={idx} style={{ background: 'var(--bg-surface)', padding: '0.5rem 0.8rem', borderRadius: '6px', border: '1px solid var(--bg-card-border)', fontSize: '0.85rem' }}>
                  <strong>{agents[r]}</strong> ➔ <span>{tasks[c]}</span> <span style={{ color: 'var(--accent-amber)', fontWeight: 700 }}>(Cost: ${origCosts[r][c]})</span>
                </div>
              ))}
            </div>
            <div style={{ marginTop: '0.8rem', textAlign: 'right', fontSize: '1.1rem', fontWeight: 800, color: 'var(--accent-purple)' }}>
              Total Minimum Cost = ${currentStep.totalCost}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};


/* === FILE: src/components/ShortestPathView.js === */
// ShortestPathView Component: SVG Network Graph Visualizer for Dijkstra Shortest Path

window.ShortestPathView = function({ problem, currentStepIndex, onCellClick }) {
  const solverRes = React.useMemo(() => {
    return window.solveShortestPath(problem);
  }, [problem]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { nodes, edges, startNode, endNode } = problem;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click node/edge to inspect distance</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* Interactive SVG Canvas */}
        <div className="network-canvas-wrapper" style={{ marginTop: '1rem' }}>
          <svg viewBox="0 0 650 380" className="network-svg">
            {/* Render Edges */}
            {edges.map((edge, idx) => {
              const srcNode = nodes.find(n => n.id === edge.source);
              const tgtNode = nodes.find(n => n.id === edge.target);
              if (!srcNode || !tgtNode) return null;

              const isActive = currentStep.activeEdge &&
                ((currentStep.activeEdge.source === edge.source && currentStep.activeEdge.target === edge.target) ||
                 (currentStep.activeEdge.source === edge.target && currentStep.activeEdge.target === edge.source));

              const isShortestPath = currentStep.pathEdges &&
                currentStep.pathEdges.some(e => (e.source === edge.source && e.target === edge.target) || (e.source === edge.target && e.target === edge.source));

              let lineClass = 'edge-line';
              if (isShortestPath) lineClass += ' shortest-path';
              else if (isActive) lineClass += ' active';

              const midX = (srcNode.x + tgtNode.x) / 2;
              const midY = (srcNode.y + tgtNode.y) / 2;

              return (
                <g key={idx} cursor="pointer" onClick={() => onCellClick({
                  title: `Edge (${edge.source} ↔ ${edge.target})`,
                  formula: `Weight w(${edge.source}, ${edge.target}) = ${edge.weight}`,
                  description: isShortestPath
                    ? 'CRITICAL PATH EDGE: Included in final optimal shortest route!'
                    : isActive
                    ? 'ACTIVE RELAXATION: Currently checking triangle inequality d(v) <= d(u) + w(u,v).'
                    : `Road link connecting ${edge.source} and ${edge.target} with length ${edge.weight}.`,
                  calculation: `Weight = ${edge.weight}`
                })}>
                  <line
                    x1={srcNode.x}
                    y1={srcNode.y}
                    x2={tgtNode.x}
                    y2={tgtNode.y}
                    className={lineClass}
                  />

                  {/* Weight badge */}
                  <rect
                    x={midX - 14}
                    y={midY - 10}
                    width="28"
                    height="20"
                    rx="4"
                    className="edge-weight-badge"
                  />
                  <text
                    x={midX}
                    y={midY + 1}
                    className="edge-weight-text"
                  >
                    {edge.weight}
                  </text>
                </g>
              );
            })}

            {/* Render Nodes */}
            {nodes.map((node) => {
              const isVisited = currentStep.visited && currentStep.visited.includes(node.id);
              const isCurrent = currentStep.currentNode === node.id;
              const distVal = currentStep.dist ? currentStep.dist[node.id] : Infinity;
              const prevVal = currentStep.prev ? currentStep.prev[node.id] : null;

              let nodeClass = 'node-circle';
              if (isCurrent) nodeClass += ' current';
              else if (isVisited) nodeClass += ' visited';

              return (
                <g key={node.id} cursor="pointer" onClick={() => onCellClick({
                  title: `Node (${node.label || node.id})`,
                  formula: `d(${node.id}) = ${distVal !== Infinity ? distVal : '∞'}, π(${node.id}) = ${prevVal || 'None'}`,
                  description: isVisited
                    ? `VISITED NODE: Shortest path to ${node.id} is permanently determined as ${distVal}.`
                    : `UNVISITED NODE: Current tentative distance d(${node.id}) = ${distVal !== Infinity ? distVal : '∞'}.`,
                  calculation: `Predecessor = ${prevVal || 'None'}`
                })}>
                  <circle
                    cx={node.x}
                    cy={node.y}
                    r="22"
                    className={nodeClass}
                  />
                  <text
                    x={node.x}
                    y={node.y}
                    className="node-text"
                  >
                    {node.id}
                  </text>

                  {/* Distance & Predecessor Badge */}
                  <text
                    x={node.x}
                    y={node.y + 35}
                    fill={isVisited ? 'var(--accent-emerald)' : 'var(--text-secondary)'}
                    fontSize="11"
                    fontWeight="700"
                    textAnchor="middle"
                  >
                    d={distVal !== Infinity ? distVal : '∞'} {prevVal ? `(π=${prevVal})` : ''}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>

        {/* Distance Vector Table */}
        {currentStep.dist && (
          <div className="matrix-container" style={{ marginTop: '1rem' }}>
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Node</th>
                  {nodes.map(n => (
                    <th key={n.id} style={{ color: n.id === currentStep.currentNode ? 'var(--accent-amber)' : 'inherit' }}>
                      {n.id} {n.id === startNode ? '(Start)' : n.id === endNode ? '(End)' : ''}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style={{ fontWeight: 700 }}>Distance d(v)</td>
                  {nodes.map(n => {
                    const dVal = currentStep.dist[n.id];
                    return (
                      <td key={n.id} style={{ fontWeight: 700, color: dVal !== Infinity ? 'var(--accent-emerald)' : 'var(--text-muted)' }}>
                        {dVal !== Infinity ? dVal : '∞'}
                      </td>
                    );
                  })}
                </tr>
                <tr>
                  <td style={{ fontWeight: 700 }}>Predecessor π(v)</td>
                  {nodes.map(n => (
                    <td key={n.id} style={{ color: 'var(--accent-blue)' }}>
                      {currentStep.prev[n.id] || '—'}
                    </td>
                  ))}
                </tr>
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};


/* === FILE: src/components/MSTView.js === */
// MSTView Component: Kruskal & Prim Minimum Spanning Tree SVG Network Visualizer

window.MSTView = function({ problem, currentStepIndex, onCellClick }) {
  const [algorithm, setAlgorithm] = React.useState('Kruskal');

  const solverRes = React.useMemo(() => {
    return window.solveMST(problem, algorithm);
  }, [problem, algorithm]);

  const currentStep = solverRes.steps[Math.min(currentStepIndex, solverRes.steps.length - 1)] || solverRes.steps[0];
  const { nodes, edges } = problem;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
      {/* Algorithm Switcher */}
      <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid var(--bg-card-border)', paddingBottom: '0.5rem' }}>
        <button
          className={`action-btn ${algorithm === 'Kruskal' ? 'primary' : ''}`}
          onClick={() => setAlgorithm('Kruskal')}
        >
          🌲 Kruskal's Algorithm (Sorted Edges + Union-Find)
        </button>
        <button
          className={`action-btn ${algorithm === 'Prim' ? 'primary' : ''}`}
          onClick={() => setAlgorithm('Prim')}
        >
          🌿 Prim's Algorithm (Growing Tree Set)
        </button>
      </div>

      <div className="card">
        <div className="explanation-title">
          <h3>{currentStep.title}</h3>
          <span className="click-hint-badge">💡 Click edge to view MST status</span>
        </div>
        <p className="explanation-text">{currentStep.description}</p>

        {/* SVG Canvas */}
        <div className="network-canvas-wrapper" style={{ marginTop: '1rem' }}>
          <svg viewBox="0 0 650 360" className="network-svg">
            {/* Render Edges */}
            {edges.map((edge, idx) => {
              const srcNode = nodes.find(n => n.id === edge.source);
              const tgtNode = nodes.find(n => n.id === edge.target);
              if (!srcNode || !tgtNode) return null;

              const isInMST = currentStep.mstEdges &&
                currentStep.mstEdges.some(e => (e.source === edge.source && e.target === edge.target) || (e.source === edge.target && e.target === edge.source));

              const isActive = currentStep.activeEdge &&
                ((currentStep.activeEdge.source === edge.source && currentStep.activeEdge.target === edge.target) ||
                 (currentStep.activeEdge.source === edge.target && currentStep.activeEdge.target === edge.source));

              let lineClass = 'edge-line';
              if (isInMST) lineClass += ' in-mst';
              else if (isActive) lineClass += ' active';

              const midX = (srcNode.x + tgtNode.x) / 2;
              const midY = (srcNode.y + tgtNode.y) / 2;

              return (
                <g key={idx} cursor="pointer" onClick={() => onCellClick({
                  title: `Cable Link (${edge.source} ↔ ${edge.target})`,
                  formula: `Length / Cost = ${edge.weight}`,
                  description: isInMST
                    ? 'ACCEPTED MST EDGE: Included in the minimum spanning cable network!'
                    : isActive
                    ? currentStep.accepted === false
                      ? 'REJECTED EDGE: Creating closed cycle!'
                      : 'EVALUATING EDGE: Testing cycle condition.'
                    : `Network link with weight ${edge.weight}.`,
                  calculation: `Weight = ${edge.weight}`
                })}>
                  <line
                    x1={srcNode.x}
                    y1={srcNode.y}
                    x2={tgtNode.x}
                    y2={tgtNode.y}
                    className={lineClass}
                  />

                  {/* Weight badge */}
                  <rect
                    x={midX - 14}
                    y={midY - 10}
                    width="28"
                    height="20"
                    rx="4"
                    className="edge-weight-badge"
                  />
                  <text
                    x={midX}
                    y={midY + 1}
                    className="edge-weight-text"
                  >
                    {edge.weight}
                  </text>
                </g>
              );
            })}

            {/* Render Nodes */}
            {nodes.map((node) => {
              const isInTree = currentStep.inTree
                ? currentStep.inTree.includes(node.id)
                : currentStep.mstEdges && currentStep.mstEdges.some(e => e.source === node.id || e.target === node.id);

              return (
                <g key={node.id}>
                  <circle
                    cx={node.x}
                    cy={node.y}
                    r="20"
                    className={`node-circle ${isInTree ? 'visited' : ''}`}
                  />
                  <text
                    x={node.x}
                    y={node.y}
                    className="node-text"
                  >
                    {node.id}
                  </text>
                </g>
              );
            })}
          </svg>
        </div>

        {/* Kruskal Sorted Edge Table */}
        {algorithm === 'Kruskal' && currentStep.sortedEdges && (
          <div className="matrix-container" style={{ marginTop: '1rem' }}>
            <h4 style={{ color: 'var(--accent-rose)', marginBottom: '0.5rem' }}>📋 Edge List (Sorted by Weight):</h4>
            <table className="custom-table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Edge (u - v)</th>
                  <th>Weight w</th>
                  <th>MST Action Status</th>
                </tr>
              </thead>
              <tbody>
                {currentStep.sortedEdges.map((e, idx) => {
                  const isMST = currentStep.mstEdges.some(m => (m.source === e.source && m.target === e.target) || (m.source === e.target && m.target === e.source));
                  const isActive = currentStep.activeEdge &&
                    ((currentStep.activeEdge.source === e.source && currentStep.activeEdge.target === e.target) ||
                     (currentStep.activeEdge.source === e.target && currentStep.activeEdge.target === e.source));

                  return (
                    <tr key={idx} style={{ background: isActive ? 'rgba(251, 191, 36, 0.15)' : 'transparent' }}>
                      <td>#{idx + 1}</td>
                      <td style={{ fontWeight: 700 }}>{e.source} ↔ {e.target}</td>
                      <td style={{ color: 'var(--accent-blue)', fontWeight: 700 }}>{e.weight}</td>
                      <td>
                        {isMST ? (
                          <span style={{ color: 'var(--accent-emerald)', fontWeight: 700 }}>✅ Included in MST</span>
                        ) : isActive && currentStep.accepted === false ? (
                          <span style={{ color: 'var(--accent-rose)', fontWeight: 700 }}>❌ Rejected (Cycle)</span>
                        ) : (
                          <span style={{ color: 'var(--text-muted)' }}>— Pending</span>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};


/* === FILE: src/app.js === */
// Main Application Engine & Root React Component

function App() {
  const [activeTopic, setActiveTopic] = React.useState('lpp');
  const [selectedProblem, setSelectedProblem] = React.useState(() => {
    return window.TEXTBOOK_PROBLEMS.lpp[0];
  });

  const [currentStepIndex, setCurrentStepIndex] = React.useState(0);
  const [isPlaying, setIsPlaying] = React.useState(false);
  const [playSpeed, setPlaySpeed] = React.useState(1000);

  const [isQuizMode, setIsQuizMode] = React.useState(false);
  const [theme, setTheme] = React.useState('light');

  const [modalData, setModalData] = React.useState(null);
  const [isModalOpen, setIsModalOpen] = React.useState(false);
  const [isCustomModalOpen, setIsCustomModalOpen] = React.useState(false);

  const [customProblems, setCustomProblems] = React.useState([]);

  // Ensure default HTML data-theme attribute is light
  React.useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  // Compute Total Steps for current active module solver
  const totalSteps = React.useMemo(() => {
    if (!selectedProblem) return 1;
    let stepsCount = 1;
    if (activeTopic === 'lpp') {
      const res = window.solveLPPSimplex(selectedProblem);
      stepsCount = res.steps.length;
    } else if (activeTopic === 'transportation') {
      const res = window.solveTransportation(selectedProblem, 'VAM');
      stepsCount = res.steps.length;
    } else if (activeTopic === 'assignment') {
      const res = window.solveAssignment(selectedProblem);
      stepsCount = res.steps.length;
    } else if (activeTopic === 'shortestPath') {
      const res = window.solveShortestPath(selectedProblem);
      stepsCount = res.steps.length;
    } else if (activeTopic === 'mst') {
      const res = window.solveMST(selectedProblem, 'Kruskal');
      stepsCount = res.steps.length;
    }
    return Math.max(1, stepsCount);
  }, [activeTopic, selectedProblem]);

  // Handle Step Auto-Play Animation Interval
  React.useEffect(() => {
    let timer = null;
    if (isPlaying) {
      timer = setInterval(() => {
        setCurrentStepIndex(prev => {
          if (prev >= totalSteps - 1) {
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, playSpeed);
    }
    return () => { if (timer) clearInterval(timer); };
  }, [isPlaying, totalSteps, playSpeed]);

  // Reset Step Index when problem or topic changes
  const handleSelectProblem = (prob) => {
    setSelectedProblem(prob);
    setCurrentStepIndex(0);
    setIsPlaying(false);
  };

  const handleCellClick = (data) => {
    setModalData(data);
    setIsModalOpen(true);
  };

  const toggleTheme = () => {
    const nextTheme = theme === 'dark' ? 'light' : 'dark';
    setTheme(nextTheme);
    document.documentElement.setAttribute('data-theme', nextTheme);
  };

  const availableProblems = [
    ...(window.TEXTBOOK_PROBLEMS[activeTopic] || []),
    ...customProblems.filter(p => p.id.includes(activeTopic))
  ];

  return (
    <div className="app-container">
      <window.Header
        activeTopic={activeTopic}
        setActiveTopic={(t) => {
          setActiveTopic(t);
          setCurrentStepIndex(0);
          setIsPlaying(false);
          const probs = [
            ...(window.TEXTBOOK_PROBLEMS[t] || []),
            ...customProblems.filter(p => p.id.includes(t))
          ];
          if (probs.length > 0) setSelectedProblem(probs[0]);
        }}
        selectedProblem={selectedProblem}
        setSelectedProblem={handleSelectProblem}
        onOpenCustomInput={() => setIsCustomModalOpen(true)}
        isQuizMode={isQuizMode}
        setIsQuizMode={setIsQuizMode}
        theme={theme}
        toggleTheme={toggleTheme}
      />

      {isQuizMode ? (
        <div style={{ padding: '1.5rem', flex: 1 }}>
          <window.QuizModeView />
        </div>
      ) : (
        <main className="workspace">
          {/* Sidebar Problem Repository Panel */}
          <aside className="sidebar-panel">
            <div className="card">
              <h3 className="card-title">
                <span>📚</span> Problem Repository ({availableProblems.length})
              </h3>
              <div className="problem-selector-list">
                {availableProblems.map(prob => (
                  <div
                    key={prob.id}
                    className={`problem-card ${selectedProblem && selectedProblem.id === prob.id ? 'active' : ''}`}
                    onClick={() => handleSelectProblem(prob)}
                  >
                    <h4>{prob.title}</h4>
                    <p>{prob.description}</p>
                    <span className="source-badge">{prob.source}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Problem Overview Card */}
            {selectedProblem && (
              <div className="card">
                <h3 className="card-title">
                  <span>⚙️</span> Problem Formulation
                </h3>
                <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)', lineHeight: 1.5 }}>
                  <p style={{ marginBottom: '0.5rem' }}>{selectedProblem.description}</p>
                  {selectedProblem.objective && (
                    <div style={{ background: 'rgba(2, 132, 199, 0.06)', padding: '0.5rem', borderRadius: '6px', fontFamily: 'var(--font-family-mono)', color: 'var(--accent-blue)', marginTop: '0.4rem', border: '1px solid rgba(2, 132, 199, 0.2)' }}>
                      <strong>{selectedProblem.objectiveType ? selectedProblem.objectiveType.toUpperCase() : 'MAX'} Z:</strong> {selectedProblem.objective[0]}x₁ + {selectedProblem.objective[1]}x₂
                    </div>
                  )}
                  {selectedProblem.supply && (
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginTop: '0.4rem' }}>
                      Supply: [{selectedProblem.supply.join(', ')}] | Demand: [{selectedProblem.demand.join(', ')}]
                    </div>
                  )}
                </div>
              </div>
            )}
          </aside>

          {/* Visualization Workspace Panel */}
          <section className="visualizer-panel">
            <window.StepControls
              currentStepIndex={currentStepIndex}
              totalSteps={totalSteps}
              onStepChange={setCurrentStepIndex}
              isPlaying={isPlaying}
              onTogglePlay={() => setIsPlaying(!isPlaying)}
              playSpeed={playSpeed}
              setPlaySpeed={setPlaySpeed}
            />

            {/* Active Topic View Rendering */}
            {activeTopic === 'lpp' && selectedProblem && (
              <window.LPPView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'transportation' && selectedProblem && (
              <window.TransportationView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'assignment' && selectedProblem && (
              <window.AssignmentView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'shortestPath' && selectedProblem && (
              <window.ShortestPathView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}

            {activeTopic === 'mst' && selectedProblem && (
              <window.MSTView
                problem={selectedProblem}
                currentStepIndex={currentStepIndex}
                onCellClick={handleCellClick}
              />
            )}
          </section>
        </main>
      )}

      {/* Inspection Modal Overlay */}
      <window.InspectionModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        data={modalData}
      />

      {/* Custom Problem Input Modal */}
      <window.CustomInputModal
        isOpen={isCustomModalOpen}
        onClose={() => setIsCustomModalOpen(false)}
        activeTopic={activeTopic}
        onSaveCustomProblem={(newProb) => {
          setCustomProblems([...customProblems, newProb]);
          setSelectedProblem(newProb);
          setCurrentStepIndex(0);
        }}
      />
    </div>
  );
}

// Render Root
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

