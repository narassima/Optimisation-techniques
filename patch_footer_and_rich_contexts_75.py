import re

print("Patching build_clean_75_direct_perfect.py with Academic Citations Footer & Rich 2-3 Sentence Contexts...")

# Rich 2-3 sentence contexts for all 75 problems
contexts_map = {
    # ── LPP ──
    "lpp_1": "Reddy Mikks produces exterior and interior paints from two raw materials M1 and M2 with daily capacities of 24 tons and 6 tons respectively. Exterior paint yields $5,000/ton profit while interior paint yields $4,000/ton. A market survey restricts daily interior paint production to at most 1 ton more than exterior paint and caps total interior demand at 2 tons per day.",
    "lpp_2": "Wyndor Glass Co. plans to launch two innovative product lines: glass doors with aluminum frames (Product 1, $3,000 profit/batch) and wood-framed windows (Product 2, $5,000 profit/batch). Production requires processing across three specialized plants with limited weekly working capacities of 4 hours at Plant 1, 12 hours at Plant 2, and 18 hours at Plant 3. Management needs an optimal product mix to maximize weekly operating profits while honoring plant limits.",
    "lpp_3": "A 24/7 industrial manufacturing facility operates continuously across all seven days of the week with varying daily staffing demands ranging from 11 workers on Sunday to 19 workers on Thursday. Each full-time employee works 5 consecutive days followed by 2 mandatory days off to ensure fatigue compliance. The plant manager must formulate an integer linear programming schedule to minimize total headcount while fulfilling daily shift coverage.",
    "lpp_4": "A custom furniture workshop manufactures dining tables (yielding $6 profit each) and ergonomic chairs (yielding $8 profit each) using shared carpentry and painting workshops. Available monthly shop capacities are strictly capped at 48 hours for carpentry and 20 hours for painting. The plant supervisor needs to determine the exact monthly production quantities of tables and chairs to maximize net workshop returns.",
    "lpp_5": "A commercial livestock feed manufacturer blends natural grain ($2 per bag) and processed soybean meal ($3 per bag) to formulate a daily cattle diet. The nutritional blend must contain at least 90 units of crude protein and 30 units of dietary fat per batch to maintain livestock health. The operations nutritionist needs to determine the minimum-cost blending ratio that fully satisfies all dietary constraints.",
    "lpp_6": "An outdoor apparel manufacturer produces premium leather parkas (profit $30/unit) and insulated overcoats (profit $50/unit) from high-grade leather stock. Total raw leather availability is constrained to 40 square feet per batch, with parkas requiring 1 sq ft and overcoats requiring 2 sq ft. Seasonal market demand caps maximum production at 20 parkas and 15 overcoats, requiring an optimal batch decision.",
    "lpp_7": "A regional logistics company manages 2 central distribution hubs supplying 3 major retail markets with varying unit freight rates. Total warehouse inventories and customer demand quotas must be balanced under transport capacity bounds. The logistics director needs an LP formulation to minimize total regional distribution costs across all supply channels.",
    "lpp_8": "A petroleum refinery processes Crude Oil A (profit $4/barrel) and Crude Oil B (profit $5/barrel) into commercial gasoline blends. Operational safety guidelines require that Crude A cannot exceed Crude B in the blend ratio, while overall refinery distillation capacity is capped at 50 barrels per hour. The chemical engineer must optimize crude throughput to maximize hourly refinery margins.",
    "lpp_9": "An asset management firm allocates institutional funds across high-yield stocks (12% expected return), corporate bonds (8% return), and liquid cash (4% return). Risk management policy dictates that stock holdings cannot exceed 60% of total capital, while bond allocations must comprise at least 20%. The portfolio manager aims to maximize overall portfolio yield under strict capital allocation rules.",
    "lpp_10": "An apparel manufacturing facility produces formal shirts ($5 profit per unit) and tailored trousers ($7 profit per unit) across cutting and sewing departments. Shirts require 2 hours of cutting and 1 hour of sewing, whereas trousers require 1 hour of cutting and 3 hours of sewing. With total available shop time capped at 40 cutting hours and 45 sewing hours per week, management seeks the profit-maximizing unit output.",
    "lpp_11": "An electronics firm manufactures smart televisions (profit $12/unit) and digital radios (profit $7/unit) using automated assembly and quality testing lines. Producing a television requires 3 assembly hours and 1 testing hour, while a radio requires 2 assembly hours and 2 testing hours. Total weekly resource availability is limited to 60 assembly hours and 40 testing hours, requiring an optimal production plan.",
    "lpp_12": "A chemical processing plant blends Compound A ($8 profit per unit) and Compound B ($5 profit per unit) in a pressurized reactor. Total batch volume cannot exceed 200 units, while thermal stability requires the combined reaction rate index 3A + B to remain within 360 units. The chemical supervisor needs to maximize financial yield without triggering reactor instability.",
    "lpp_13": "A corporate marketing manager distributes an advertising budget between prime-time television broadcasts ($5,000 per ad, reaching 200,000 viewers) and daily newspaper features ($2,000 per ad, reaching 80,000 viewers). Total available campaign budget is $20,000, with contracts limiting television ads to at most 3 and newspaper placements to at most 7. The campaign goal is to maximize total audience reach.",
    "lpp_14": "A commercial bakery produces artisanal cakes ($10 profit per unit) and specialty pastries ($6 profit per unit) requiring baking and icing processes. Each cake requires 2 hours of baking and 1 hour of icing, while each pastry batch requires 1 hour of baking and 2 hours of icing. Available shift capacities are 16 hours for baking and 16 hours for icing, requiring an optimal product mix.",
    "lpp_15": "A steel manufacturing mill produces hot-rolled sheets ($15 profit/ton) and cold-rolled coils ($12 profit/ton) using rolling and finishing mills. Hot-rolled steel requires 4 hours of rolling mill time, whereas cold-rolled steel requires 2 hours of rolling and 2 hours of finishing mill time. Weekly capacities are 80 hours for the rolling mill and 40 hours for the finishing mill, requiring an optimal production schedule.",

    # ── TRANSPORTATION ──
    "tp_1": "MG Auto operates three assembly plants in Los Angeles, Detroit, and New Orleans with monthly capacities of 1,000, 1,500, and 1,200 vehicles. Vehicles are shipped to two main distribution centers in Denver and Miami with demands of 2,300 and 1,400 vehicles respectively. The logistics planner must minimize total transshipment costs while fully satisfying regional vehicle demand.",
    "tp_2": "P&T Foods distributes canned peas from 3 cannery plants with output capacities of 75, 125, and 100 truckloads to 4 regional distribution warehouses with demands of 80, 65, 70, and 85 truckloads. Per-truckload transport costs vary significantly based on geographic distance and carrier rates. Management requires an optimal shipping allocation to minimize total freight expenditure.",
    "tp_3": "A regional agricultural cooperative collects produce from 3 rural collection hubs (supplying 30, 40, and 50 tons) and distributes to 4 urban markets (demanding 20, 30, 40, and 30 tons). Freight tariffs vary across routes depending on road conditions and transit times. The supply chain manager needs an optimal distribution schedule minimizing overall logistics cost.",
    "tp_4": "A steel manufacturing company operates 3 primary rolling mills with monthly outputs of 120, 80, and 80 thousand tons. Steel shipments supply 3 industrial equipment manufacturers requiring 150, 80, and 50 thousand tons respectively. Freight costs depend on rail transport tariffs, requiring an optimal distribution matrix to minimize total freight charges.",
    "tp_5": "An agricultural distribution network coordinates fresh produce delivery from 3 regional farm clusters (supplying 200, 300, and 100 crates) to 3 wholesale markets (demanding 150, 250, and 200 crates). Replicated transport pricing reflects refrigerated trucking costs per crate. The distribution lead must schedule shipments to minimize total cold-chain logistics expense.",
    "tp_6": "A national energy conglomerate extracts coal from 3 regional mining sites with monthly production capabilities of 100, 200, and 150 kilotons. Coal is shipped by rail to 3 thermal power generation plants requiring 120, 180, and 150 kilotons respectively. Transport tariffs per kiloton vary according to rail corridor distance, requiring a minimum-cost supply plan.",
    "tp_7": "A building materials supplier distributes bagged cement from 2 manufacturing plants (capacities 60 and 40 tons) to 3 active infrastructure construction sites (demands 30, 40, and 30 tons). Local trucking tariffs depend on urban traffic congestion and haulage distance. The logistics coordinator needs to balance supply and demand at minimum total haulage cost.",
    "tp_8": "A textile conglomerate ships finished fabric rolls from 3 manufacturing mills (producing 300, 200, and 400 rolls) to 4 retail distribution outlets (requiring 250, 350, 150, and 150 rolls). Shipping tariffs reflect interstate trucking rates per roll across corridors. The distribution manager seeks an optimal allocation matrix minimizing total freight expenses.",
    "tp_9": "A grain distribution enterprise transports harvested wheat from 3 regional grain elevators (capacities 500, 700, and 400 bushels) to 3 commercial flour mills (demands 400, 600, and 600 bushels). Rail transport charges vary based on distance and bulk loading fees. Management requires a minimum-cost freight schedule.",
    "tp_10": "A healthcare supplier distributes temperature-sensitive vaccines from 3 central cold-storage hubs (supplying 150, 250, and 200 cases) to 3 regional hospital networks (demanding 100, 300, and 200 cases). Specialized refrigerated transit rates vary per route. The operations team needs to minimize total cold-chain shipping costs while fulfilling all hospital quotas.",
    "tp_11": "An energy supplier delivers refined fuel from 3 coastal petroleum storage depots (supplying 800, 600, and 1,000 kiloliters) to 3 inland gas station networks (demanding 700, 900, and 800 kiloliters). Tanker truck transport tariffs per kiloliter reflect highway distance and toll charges. The dispatch supervisor requires an optimal fuel routing plan.",
    "tp_12": "A paper manufacturing enterprise delivers newsprint paper reels from 3 paper mills (capacities 400, 300, and 500 reels) to 3 major newspaper printing plants (demands 350, 450, and 400 reels). Freight rates per reel vary according to transport mode and carrier contracts. Management seeks to minimize overall distribution expenditure.",
    "tp_13": "An automotive manufacturer supplies replacement parts from 3 central spare-part warehouses (stocks of 600, 400, and 500 units) to 3 regional dealership hubs (demands of 500, 500, and 500 units). Express delivery rates depend on distance and package dimensions. The logistics planner must minimize total distribution expense.",
    "tp_14": "A beverage company ships bottled beverages from 3 bottling facilities (supplying 1,000, 800, and 1,200 crates) to 3 retail distribution centers (demanding 900, 1,100, and 1,000 crates). Trucking tariffs per crate vary across delivery routes. The operations manager requires an optimal allocation matrix minimizing total shipping cost.",
    "tp_15": "A consumer electronics manufacturer distributes laptops from 3 assembly plants (supplying 600, 400, and 500 units) to 3 retail electronics store chains (demanding 500, 500, and 500 units). Air and road freight tariffs vary per route. Management needs a minimum-cost shipping plan that completely balances plant supply with store demand.",

    # ── ASSIGNMENT ──
    "asgn_1": "Klyne's household needs to assign 4 children to 4 weekly household chores based on secret bid prices submitted by each child in dollars. To prevent conflict, each child must be assigned to exactly one unique chore while minimizing overall household allowance expenditure. After standard row and column reductions, minimum lines test fails (3 lines < n=4), requiring Hungarian matrix adjustment.",
    "asgn_2": "A manufacturing plant needs to assign 3 heavy industrial machines to 4 newly built shop-floor locations to minimize material handling costs. A dummy machine with zero cost everywhere is added to balance the 3x4 non-square matrix into a 4x4 Hungarian formulation. Direct assignment becomes possible immediately following row reduction.",
    "asgn_3": "An IT consulting firm needs to assign 4 senior consultants (Alex, Ben, Cara, Dev) to 4 client software projects (P1 through P4) based on estimated cost bids in thousands of dollars. Initial row and column reduction produces a matrix where three consultants share zeros in only two project columns. Applying the Hungarian coverage test forces a matrix adjustment with k=2 to achieve a valid 1-to-1 matching.",
    "asgn_4": "A corporate marketing department assigns 4 creative marketing teams to 4 product promotion campaigns (TV, Radio, Print, Online) to minimize total budget requirements in thousands of dollars. Three teams exhibit identical low-cost structures for TV and Radio, creating a 3-vs-2 zero conflict. The Hungarian algorithm adjusts the matrix with k=2 to break the bottleneck and form an optimal matching.",
    "asgn_5": "A hospital nursing supervisor needs to assign 4 specialized nurses to 4 hospital wards (ICU, ER, Pediatric, Geriatric) based on shift difficulty scores. Three nurses share identical low difficulty ratings for ICU and ER, violating Hall's condition after initial reduction. Subtracting k=1 from uncovered cells creates a new zero at the Pediatric ward, enabling a complete unique assignment.",
    "asgn_6": "An academic journal editor assigns 4 research scholars to review 4 submitted research manuscripts based on estimated review turnaround times in hours. Three junior scholars require equal review times for Papers 1 and 2, causing 3 rows to compete for 2 zero-columns. The Hungarian method applies matrix adjustment with k=4 hours to allocate all manuscripts optimally.",
    "asgn_7": "A commercial sales director assigns 4 senior sales representatives to 4 new product lines to minimize total transition and training costs in dollars. Three representatives possess identical proficiency for Product Lines 1 and 2, preventing direct assignment after reduction. Performing Hungarian matrix adjustment with k=6 resolves the conflict and minimizes total training expenditure.",
    "asgn_8": "A university athletics department assigns 4 track coaches to 4 event categories (100m, 200m, 400m, Relay) based on coaching effort index scores. Three sprint coaches have identical high aptitude for 100m and 200m events, creating a 3-coach conflict for 2 event slots. Matrix adjustment with k=3 expands zero coverage into the 400m event to achieve an optimal assignment.",
    "asgn_9": "A urban logistics manager assigns 4 delivery vans to 4 delivery routes based on estimated round-trip travel times in minutes. Three vans exhibit identical efficiency on Routes 1 and 2, requiring line coverage adjustment after initial reduction. Subtracting k=7 minutes from uncovered cells generates new zero entries on Route 3, achieving a total time minimization.",
    "asgn_10": "An Agile scrum master assigns 4 developers (Alice, Bob, Carol, Tech Lead) to 4 sprint modules (Frontend, Backend, Database, Testing) based on estimated story-point effort. Alice, Bob, and Carol are equally skilled in Frontend and Backend, producing a 3-vs-2 zero constraint after reduction. Applying Hungarian adjustment with k=4 story points unlocks optimal task distribution.",
    "asgn_11": "A university department head assigns 4 faculty members to 4 teaching time slots (8 AM, 10 AM, 12 PM, 2 PM) to minimize total faculty inconvenience scores. Three professors express equal preference for early morning slots, creating zero overlap in 8 AM and 10 AM columns. Matrix adjustment with k=3 inconvenience points resolves the schedule overlap.",
    "asgn_12": "A construction site manager assigns 4 skilled workers to 4 specialized tasks (Excavation, Concreting, Carpentry, Electrical) based on task completion hours. Three workers have identical productivity in Excavation and Concreting, preventing direct assignment. Executing Hungarian matrix adjustment with k=4 hours enables a complete task allocation at minimum total labor time.",
    "asgn_13": "A university examination board assigns 4 faculty invigilators to 4 exam halls based on travel and setup time in minutes. Three invigilators have equal proximity to Halls A and B, requiring line coverage matrix modification. Subtracting k=5 minutes from uncovered cells opens Hall C for assignment, minimizing total setup time.",
    "asgn_14": "A investment bank assigns 4 financial analysts to 4 asset portfolios (Equity, Debt, Hybrid, Gold) based on risk-adjusted management cost scores. Three analysts possess identical competence in Equity and Debt portfolios, violating Hall's condition. Performing Hungarian adjustment with k=5 risk points yields a unique portfolio matching.",
    "asgn_15": "A supply chain director assigns 4 regional field agents to 4 sales territories (North, South, East, West) based on total travel logistics costs in dollars. Three agents demonstrate identical efficiency in North and South territories, requiring matrix adjustment. Subtracting k=6 dollars from uncovered cells generates a new zero in the East territory for an optimal assignment.",

    # ── SHORTEST PATH ──
    "sp_1": "Seervada Park management needs to determine the shortest path from the park entrance (Node O) to remote scenic station T for daily tram operations. The sightseeing trail network includes multiple intermediate junction stops (A, B, C, D, E) connected by scenic roads with known mileages. Using Dijkstra's algorithm step-by-step, the park supervisor computes the shortest path of 13 miles.",
    "sp_2": "A urban traffic authority needs to optimize the emergency vehicle route from central station S to peripheral industrial park T across 5 intermediate highway junctions. Road segments have varying speed limits and distance bottlenecks. Dijkstra's algorithm evaluates candidate paths step-by-step to establish the shortest distance route of 16 miles.",
    "sp_3": "A logistics enterprise coordinates cargo shipments from central manufacturing hub S to retail distribution terminal T through 5 regional transit hubs. Transit times and toll fees are evaluated across all connecting corridors. The supply chain planner applies Dijkstra's algorithm to determine the minimum-cost routing of 12 units.",
    "sp_4": "An emergency response center calculates the fastest route for an ambulance traveling from accident site S to trauma hospital T through 5 city intersections. Traffic congestion indexes dictate transit times across all intermediate street links. Dijkstra's algorithm evaluates real-time network states to establish the minimum response path of 11 minutes.",
    "sp_5": "A university facilities management department designs a pedestrian walkway guide connecting the main campus entrance S to the library complex T across 5 campus plazas. Distance measurements in meters are evaluated along paved pathways. Dijkstra's algorithm identifies the shortest walking route of 12 units.",
    "sp_6": "A cloud infrastructure provider routes high-frequency data packets from origin server S to destination server T through 5 intermediate router nodes. Network latency and transmission delay in milliseconds are evaluated across all fiber connections. Dijkstra's algorithm calculates the minimum-latency network path of 13 ms.",
    "sp_7": "An energy corporation transports crude oil from extraction well S to coastal refinery T through 5 intermediate pumping stations. Energy consumption per barrel varies across pipeline terrain segments. Dijkstra's algorithm determines the minimum pumping energy path of 11 units.",
    "sp_8": "A railway authority optimizes the express passenger train route connecting terminal station S to regional destination T through 5 intermediate junction cities. Track distance in kilometers is evaluated across all connecting rail segments. Dijkstra's algorithm computes the shortest rail route of 23 units.",
    "sp_9": "An e-commerce logistics firm plans the delivery van route from central distribution hub S to customer parcel locker T through 5 urban neighborhood checkpoints. Transit delays in minutes are calculated for each road link. Dijkstra's algorithm identifies the fastest delivery path of 12 minutes.",
    "sp_10": "An airport operations group determines the fastest passenger transit path between arrival gate S and departure gate T across 5 terminal concourse junctions. Pedestrian walkway travel times in minutes are evaluated for all connecting corridors. Dijkstra's algorithm establishes the minimum layover travel path of 14 minutes.",
    "sp_11": "A telecommunications engineer routes a microwave communications signal from broadcasting tower S to receiver tower T through 5 relay repeater towers. Signal attenuation in decibels is evaluated across all line-of-sight links. Dijkstra's algorithm computes the minimum signal loss path of 15 dB.",
    "sp_12": "A municipal water authority plans a high-pressure main supply pipe from reservoir S to district storage tank T through 5 distribution junctions. Hydraulic friction loss is calculated for all pipe segments. Dijkstra's algorithm determines the path of minimum total pressure loss (15 units).",
    "sp_13": "A travel agency compiles the lowest-cost flight itinerary connecting departure airport S to vacation destination T across 5 layover airport hubs. Airfare prices in hundreds of dollars are evaluated across all connecting flight legs. Dijkstra's algorithm calculates the cheapest flight path of 12 units.",
    "sp_14": "A port authority optimizes container drayage truck movements from receiving gate S to berth terminal T through 5 port yard intersections. Transit times in minutes are calculated across all internal port roadways. Dijkstra's algorithm establishes the minimum drayage route of 17 minutes.",
    "sp_15": "An electric utility company routes a high-voltage power transmission line from power plant S to regional substation T across 5 grid node towers. Electrical resistance and line loss are evaluated for all candidate transmission corridors. Dijkstra's algorithm computes the path of minimum line resistance (15 units).",

    # ── MST ──
    "mst_1": "Seervada Park management needs to install a permanent telephone communications network connecting all 7 stations (O, A, B, C, D, E, T) with minimum total cable length. The park terrain contains 11 candidate underground cable routes forming multiple closed loops. Prim's algorithm builds the minimum spanning tree step-by-step, achieving a total cable requirement of 14 miles.",
    "mst_2": "Midwest TV Cable Company provides cable television service to 5 residential housing developments connected to a central headend station. A total of 8 candidate cable corridors connect adjacent developments, forming 3 closed loops. Prim's algorithm connects all housing developments into a minimum spanning tree with a total cable length of 17 miles.",
    "mst_3": "An enterprise IT department needs to interconnect 7 departmental office clusters (Hub, A, B, C, D, E, Gateway) into a unified fiber optic network. The building floorplan features 12 candidate conduit paths forming 5 distinct structural cycles. Prim's algorithm selects the optimal non-cyclic links to construct a minimum spanning tree of 17 units.",
    "mst_4": "A rural water development agency plans a clean water distribution grid connecting 7 village residential sectors. The planned layout includes 13 candidate pipeline routes forming 6 closed hydraulic loops. Prim's algorithm identifies the minimum total pipe length (16 units) required to supply all sectors without redundant looping.",
    "mst_5": "A university IT team installs high-speed fiber optic cabling to connect 7 academic building clusters to the campus network core. The campus layout offers 12 candidate duct paths with 5 structural cycles. Prim's algorithm connects all buildings into a minimum spanning tree requiring 16 units of fiber.",
    "mst_6": "A regional rail network connects 8 passenger stations and freight yards across 14 candidate track corridors forming 6 closed loops. Rail engineers apply Prim's algorithm to determine the minimum total track construction distance (19 units) that ensures full network connectivity.",
    "mst_7": "A power utility company designs an interconnected electrical grid linking 7 regional substations and power plants. The network includes 12 high-voltage transmission lines forming 5 closed grid loops. Prim's algorithm constructs a minimum spanning tree requiring 19 units of transmission line.",
    "mst_8": "An agricultural irrigation authority connects a river headworks to 6 farming canal sectors through 12 candidate canal channels forming 5 closed loops. Prim's algorithm determines the minimum total canal excavation length (16 units) that guarantees water flow to all sectors.",
    "mst_9": "A municipal smart-city initiative connects 8 urban data collection nodes with fiber optic broadband across 15 candidate duct pathways forming 7 structural loops. Prim's algorithm builds a minimum spanning network requiring 18 units of fiber cabling.",
    "mst_10": "A natural gas distributor connects a central compressor station to 6 regional distribution points across 12 candidate pipeline corridors forming 5 closed loops. Prim's algorithm identifies the minimum pipeline construction length of 19 units.",
    "mst_11": "A medical center installs high-speed data cabling to link 7 critical care units (ER, ICU, OR, Lab, Radiology, Main Server, Switch) across 12 candidate conduit paths forming 5 loops. Prim's algorithm connects all medical units into a minimum spanning tree with a total latency length of 13 ms.",
    "mst_12": "An industrial chemical plant connects 7 hazardous material sensors and alarm units to the central control room across 12 candidate wiring channels forming 5 closed loops. Prim's algorithm calculates the minimum total wiring length of 15 units.",
    "mst_13": "A telecommunications ISP connects 8 regional internet exchange POPs across 14 candidate fiber trunk routes forming 6 closed loops. Prim's algorithm establishes a minimum spanning backbone requiring 19 units of fiber cabling.",
    "mst_14": "A university physical plant department connects 7 academic complexes across 12 candidate utility trenches forming 5 closed loops. Prim's algorithm determines the minimum trenching distance of 16 units required to connect all buildings.",
    "mst_15": "An automated e-commerce fulfillment center connects 8 sorting, packing, and dispatch zones across 14 candidate conveyor tracks forming 6 closed loops. Prim's algorithm calculates the minimum total conveyor track length (16 units) to link all warehouse zones."
}

# 1. Update build_clean_75_direct_perfect.py contexts
with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    code = f.read()

# Update contexts across all 75 problem dictionaries in python code
count = 0
for prob_id, rich_context in contexts_map.items():
    # Match "id": "prob_id", ... "context": "..."
    pattern = rf'("id":\s*"{prob_id}".*?"context":\s*")[^"]+(")'
    if re.search(pattern, code, re.DOTALL):
        code = re.sub(pattern, rf'\g<1>{rich_context}\g<2>', code, count=1, flags=re.DOTALL)
        count += 1

print(f"Updated {count} problem contexts to rich 2-3 sentence real-world scenarios!")

# 2. Add Academic References Footer to renderHome()
old_home_func = """function renderHome() {
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
}"""

new_home_func = """function renderHome() {
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
}"""

if old_home_func in code:
    code = code.replace(old_home_func, new_home_func)
    print("Added Academic Citations Footer to renderHome()!")
else:
    pattern = r'function renderHome\(\)\s*\{\s*return `.*?\`;\s*\}'
    code = re.sub(pattern, new_home_func, code, flags=re.DOTALL)
    print("Added Academic Citations Footer via regex!")

with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Patching complete!")
