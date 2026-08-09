import re

print("Patching build_clean_75_direct_perfect.py with full 15 assignment problems...")

with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace from asgn_problems = [ to # ─── 4. SHORTEST PATH PROBLEMS
asgn_section = """asgn_problems = [
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
            {"title": "Step 4: Matrix Adjustment (k=1) & Final Assignment", "explain": "Smallest uncovered element k=1. Subtract k from all uncovered cells; add k to double-covered intersection cells. Now lines = n=4. Assign unique zeros.", "matrix": [[0,2,1,1],[3,0,0,2],[0,0,3,2],[4,2,0,0]], "assignment": [[0,0],[1,2],[2,1],[3,3]], "result": "Child 1 \u2192 Chore 1 ($1)<br/>Child 2 \u2192 Chore 3 ($10)<br/>Child 3 \u2192 Chore 2 ($5)<br/>Child 4 \u2192 Chore 4 ($5)<br/><strong>Minimum Total Cost = $21</strong>"}
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
            {"title": "Column Reduction & Assignment", "explain": "Column minimums are all 0 - no column reduction needed. Unique zeros can be matched directly.", "matrix": [[3,0,6,1],[0,6,1,0],[3,0,5,3],[0,0,0,0]], "assignment": [[0,1],[1,0],[2,3],[3,2]], "result": "M1\u2192Loc 2 ($10), M2\u2192Loc 1 ($9), M3\u2192Loc 4 ($12), Dummy\u2192Loc 3 ($0)<br/><strong>Minimum Handling Cost = $31</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "New zero at (Alex,P3). Now 4 lines cover all zeros (Col P1 + Col P2 + Col P3 + Row Dev). Assign: Dev must take P3 or P4 - assign Dev\u2192P4. Alex gets P3. Ben & Cara share P1 & P2.", "matrix": [[0,0,0,2],[0,0,1,3],[0,0,2,4],[5,4,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Alex \u2192 Project 3 ($7K)<br/>Ben \u2192 Project 1 ($4K)<br/>Cara \u2192 Project 2 ($6K)<br/>Dev \u2192 Project 4 ($3K)<br/><strong>Minimum Total Cost = $20,000</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "New zeros: A(TV,Radio,Print), B(TV,Radio,Print), C(TV,Radio). Team D has zeros at Print,Online. TeamD must go Online (Print needed for A/B). Teams A,B,C share TV, Radio, Print.", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,2,6],[9,7,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Team A \u2192 Print ($10L)<br/>Team B \u2192 TV ($6L)<br/>Team C \u2192 Radio ($9L)<br/>Team D \u2192 Online ($5L)<br/><strong>Minimum Total Budget = $30L</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "New zero at (N1,Pediatric) breaks the tie. 4 lines now cover all zeros. Assign N4\u2192Geriatric, N1\u2192Pediatric, and N2,N3 distribute between ICU and ER.", "matrix": [[0,0,0,2],[0,0,1,3],[0,0,2,4],[5,3,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Nurse 1 \u2192 Pediatric (8)<br/>Nurse 2 \u2192 ICU (5)<br/>Nurse 3 \u2192 ER (9)<br/>Nurse 4 \u2192 Geriatric (3)<br/><strong>Minimum Total Difficulty Score = 25</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "Junior scholars now have zeros in P1, P2, and P3. Senior has zeros in P3 and P4. Since Senior must NOT take a paper juniors exclusively need: assign Senior\u2192P4, and juniors share P1,P2,P3.", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,0,4],[13,11,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Scholar 1 \u2192 Paper 3 (14 hrs)<br/>Scholar 2 \u2192 Paper 1 (8 hrs)<br/>Scholar 3 \u2192 Paper 2 (12 hrs)<br/>Senior Scholar \u2192 Paper 4 (7 hrs)<br/><strong>Minimum Total Time = 41 hours</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "Sarah,Mike have zeros in PL1,PL2,PL3. Priya has zeros in PL1,PL2. Tom has zeros in PL3,PL4. Assign Tom\u2192PL4, Sarah\u2192PL3, and Mike,Priya share PL1,PL2.", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,2,10],[19,17,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Sarah \u2192 Prod Line 3 ($31)<br/>Mike \u2192 Prod Line 1 ($21)<br/>Priya \u2192 Prod Line 2 ($28)<br/>Tom \u2192 Prod Line 4 ($19)<br/><strong>Minimum Total Cost = $99</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "Coaches A,B,C have zeros in 100m, 200m, 400m. Head Coach has zeros in 400m, Relay. Head must cover Relay (400m needed for juniors). A,B,C freely cover 100m,200m,400m.", "matrix": [[0,0,0,5],[0,0,0,5],[0,0,0,5],[12,10,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Coach A \u2192 400m (17)<br/>Coach B \u2192 100m (11)<br/>Coach C \u2192 200m (17)<br/>Head Coach \u2192 Relay (10)<br/><strong>Minimum Total Effort = 55</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "Vans 1,2,3 now have zeros in R1,R2,R3. Van 4 has zeros in R3,R4. Assign V4\u2192R4, and distribute V1,V2,V3 over R1,R2,R3.", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,0,8],[27,22,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Van 1 \u2192 Route 3 (52 min)<br/>Van 2 \u2192 Route 1 (38 min)<br/>Van 3 \u2192 Route 2 (50 min)<br/>Van 4 \u2192 Route 4 (35 min)<br/><strong>Minimum Total Time = 175 minutes</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "Developers have zeros in FE, BE, DB. Tech Lead has zeros in DB, Testing. Lead must take Testing (DB needed for developers). Alice, Bob, Carol share FE, BE, DB.", "matrix": [[0,0,0,4],[0,0,0,4],[0,0,0,4],[12,10,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Alice \u2192 Database (12 pts)<br/>Bob \u2192 Frontend (6 pts)<br/>Carol \u2192 Backend (10 pts)<br/>Tech Lead \u2192 Testing (7 pts)<br/><strong>Minimum Total Story Points = 35</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "P,Q,R have zeros in 8AM, 10AM, 12PM. Prof.S has zeros in 12PM and 2PM. Assign S\u21922PM (to free 12PM for P/Q/R). Faculty share the three morning/midday slots.", "matrix": [[0,0,0,5],[0,0,0,5],[0,0,0,5],[13,11,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Prof. P \u2192 12 PM (14)<br/>Prof. Q \u2192 8 AM (9)<br/>Prof. R \u2192 10 AM (13)<br/>Prof. S \u2192 2 PM (8)<br/><strong>Minimum Total Inconvenience = 44</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "Workers 1,2,3 have zeros in Exc, Con, Carpentry. Foreman has zeros in Carpentry and Electrical. Assign Foreman\u2192Electrical (freeing Carpentry for workers). Workers share Exc, Con, Carp.", "matrix": [[0,0,0,6],[0,0,0,6],[0,0,0,6],[17,15,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Worker 1 \u2192 Carpentry (20 hrs)<br/>Worker 2 \u2192 Excavation (12 hrs)<br/>Worker 3 \u2192 Concreting (20 hrs)<br/>Foreman \u2192 Electrical (11 hrs)<br/><strong>Minimum Total Time = 63 hours</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "W,X,Y now have zeros in A, B, C. Chief has zeros in C and D. Chief must take D (to free C for junior invigilators). W,X,Y share Halls A, B, C.", "matrix": [[0,0,0,7],[0,0,0,7],[0,0,0,7],[21,18,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Inv. W \u2192 Hall C (23 min)<br/>Inv. X \u2192 Hall A (15 min)<br/>Inv. Y \u2192 Hall B (21 min)<br/>Chief Inv. \u2192 Hall D (12 min)<br/><strong>Minimum Total Time = 71 minutes</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "P,Q,R have zeros in Equity, Debt, Hybrid. Senior has zeros in Hybrid and Gold. Senior must take Gold (Hybrid reserved for P/Q/R rotation). Analysts P,Q,R share Equity, Debt, Hybrid.", "matrix": [[0,0,0,7],[0,0,0,7],[0,0,0,7],[20,17,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Analyst P \u2192 Hybrid (25)<br/>Analyst Q \u2192 Equity (16)<br/>Analyst R \u2192 Debt (24)<br/>Senior Analyst \u2192 Gold (15)<br/><strong>Minimum Total Risk-Cost = 80</strong>"}
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
            {"title": "Step 5: Final Optimal Assignment", "explain": "Agents 1,2,3 have zeros in North, South, East. Regional Head has zeros in East and West. Head takes West (East freed for agents). Agents share North, South, East.", "matrix": [[0,0,0,8],[0,0,0,8],[0,0,0,8],[24,20,0,0]], "assignment": [[0,2],[1,0],[2,1],[3,3]], "result": "Agent 1 \u2192 East ($28)<br/>Agent 2 \u2192 North ($18)<br/>Agent 3 \u2192 South ($26)<br/>Regional Head \u2192 West ($18)<br/><strong>Minimum Total Logistics Cost = $90</strong>"}
        ]
    }
]
"""

# Replace in code: find start of asgn_problems = [ and end before # ─── 4. SHORTEST PATH PROBLEMS
start_idx = code.find("asgn_problems = [")
end_idx = code.find("sp_problems = [")
# back up to find comment before sp_problems
comment_idx = code.rfind("#", 0, end_idx)
if comment_idx != -1:
    end_idx = comment_idx

if start_idx != -1 and end_idx != -1:
    new_code = code[:start_idx] + asgn_section + "\n\n" + code[end_idx:]
    with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
        f.write(new_code)
    print("Successfully replaced assignment problems section!")
else:
    print(f"Error finding markers! start_idx={start_idx}, end_idx={end_idx}")
