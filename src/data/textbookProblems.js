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
