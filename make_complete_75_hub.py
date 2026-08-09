import os

# Build the complete app.html file

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>OR Learning Hub – OTDM (PGDM)</title>
<script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:#f4f6f9;color:#1a202c;min-height:100vh;line-height:1.6}

/* HEADER */
#app-header{background:linear-gradient(135deg,#1b365d 0%,#2563eb 60%,#0f2b5c 100%);color:#fff;padding:0;position:sticky;top:0;z-index:100;box-shadow:0 3px 14px rgba(0,0,0,.2)}
.header-inner{max-width:1320px;margin:0 auto;padding:18px 24px 12px;display:flex;align-items:center;justify-content:space-between;gap:14px}
.header-left{display:flex;align-items:center;gap:14px}
.header-logo{font-size:2.2rem}
.header-text h1{font-size:1.45rem;font-weight:700;letter-spacing:-.3px}
.header-text p{font-size:.83rem;opacity:.88;margin-top:2px}
.nav-strip{background:rgba(0,0,0,.25);overflow-x:auto;white-space:nowrap}
.nav-strip-inner{max-width:1320px;margin:0 auto;display:flex}
.ntab{padding:11px 20px;font-size:.84rem;font-weight:600;color:rgba(255,255,255,.75);border:none;background:transparent;cursor:pointer;border-bottom:3px solid transparent;transition:all .18s;flex-shrink:0}
.ntab:hover{color:#fff;background:rgba(255,255,255,.08)}
.ntab.active{color:#fff;border-bottom-color:#60a5fa;background:rgba(255,255,255,.12)}

/* MAIN LAYOUT */
.main{max-width:1320px;margin:0 auto;padding:26px 20px}

/* BADGES & TAGS */
.ppt-badge{display:inline-flex;align-items:center;gap:5px;background:#fff7ed;color:#c2410c;border:1px solid #ffedd5;border-radius:4px;font-size:.73rem;font-weight:700;padding:3px 9px;margin-bottom:8px}
.book-badge{display:inline-flex;align-items:center;gap:5px;background:#f0fdf4;color:#166534;border:1px solid #bbf7d0;border-radius:4px;font-size:.73rem;font-weight:700;padding:3px 9px;margin-bottom:8px}
.tag{display:inline-block;padding:3px 8px;border-radius:4px;font-size:.72rem;font-weight:700;background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe}

/* CARDS GRID */
.mod-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-top:10px}
.mod-card{background:#fff;border:1px solid #e2e8f0;border-radius:6px;padding:22px 20px 18px;cursor:pointer;transition:transform .18s,box-shadow .18s,border-color .18s;position:relative;overflow:hidden}
.mod-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--c,#2563eb)}
.mod-card:hover{transform:translateY(-3px);box-shadow:0 10px 25px rgba(37,99,235,.15);border-color:#93c5fd}
.mod-card h3{font-size:1.05rem;font-weight:700;margin:10px 0 6px;color:#1b365d}
.mod-card p{font-size:.83rem;color:#64748b;margin-bottom:12px;line-height:1.5}
.mod-badge{display:inline-block;background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe;border-radius:4px;font-size:.72rem;font-weight:700;padding:3px 9px}

/* LIST VIEW */
.back-btn{display:inline-flex;align-items:center;gap:6px;background:#fff;border:1px solid #d1d5db;border-radius:5px;padding:7px 15px;font-size:.84rem;font-weight:600;color:#374151;cursor:pointer;margin-bottom:18px;transition:all .15s}
.back-btn:hover{background:#f3f4f6;border-color:#9ca3af}
.sec-title{font-size:1.35rem;font-weight:700;color:#1b365d;margin-bottom:4px}
.sec-desc{font-size:.86rem;color:#64748b;margin-bottom:20px}
.prob-list{display:flex;flex-direction:column;gap:10px}
.prob-item{background:#fff;border:1px solid #e2e8f0;border-radius:6px;padding:15px 18px;cursor:pointer;display:flex;align-items:center;justify-content:space-between;transition:all .15s}
.prob-item:hover{border-color:#93c5fd;background:#f0f7ff;transform:translateX(2px)}
.prob-item h4{font-size:.92rem;font-weight:600;color:#1b365d;display:flex;align-items:center;gap:8px}
.prob-item p{font-size:.8rem;color:#64748b;margin-top:3px}
.diff{font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:4px}
.d-easy{background:#dcfce7;color:#166534}
.d-med{background:#fef3c7;color:#92400e}
.d-hard{background:#fee2e2;color:#991b1b}

/* DETAIL CONTAINER */
.prob-header{background:linear-gradient(135deg,#1b365d,var(--c,#2563eb));color:#fff;padding:24px 26px;border-radius:6px 6px 0 0}
.prob-header h2{font-size:1.25rem;font-weight:700}
.prob-header p{font-size:.86rem;opacity:.9;margin-top:6px;line-height:1.5}
.prob-body{background:#fff;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 6px 6px;padding:24px}

/* PPT-STYLE STEP CARDS */
.step-card{border:1px solid #e2e8f0;border-radius:6px;margin-bottom:14px;overflow:hidden;background:#fff}
.step-hd{background:#f8fafc;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;transition:background .15s;border-bottom:1px solid transparent}
.step-hd:hover,.step-hd.open{background:#eff6ff;border-bottom-color:#bfdbfe}
.step-hd h3{font-size:.9rem;font-weight:700;color:#1b365d;display:flex;align-items:center;gap:9px}
.snum{background:#2563eb;color:#fff;border-radius:50%;width:24px;height:24px;display:inline-flex;align-items:center;justify-content:center;font-size:.73rem;font-weight:800;flex-shrink:0}
.step-bd{padding:18px;display:none;background:#fff}
.step-bd.show{display:block}

/* PPT FORMULATION BOX */
.ppt-formulation{background:#f8fafc;border:1px solid #cbd5e1;border-left:4px solid #2563eb;border-radius:4px;padding:16px;margin:12px 0;font-family:'Consolas','Courier New',monospace;font-size:.85rem;line-height:1.8;color:#1e293b}
.ppt-formulation .lbl{color:#2563eb;font-weight:700}
.ppt-formulation .var{color:#059669;font-weight:700}
.ppt-formulation .const{color:#d97706;font-weight:700}

/* PPT EXPLANATION BOX */
.ppt-explain{background:#fffbeb;border:1px solid #fcd34d;border-radius:5px;padding:12px 16px;margin:12px 0;font-size:.85rem;color:#78350f;line-height:1.6}
.ppt-explain strong{color:#92400e}

/* TABLES IN PPT FORMAT */
.table-wrap{overflow-x:auto;margin:12px 0}
table.ppt-table{border-collapse:collapse;width:100%;font-size:.83rem;min-width:450px}
table.ppt-table th,table.ppt-table td{border:1px solid #cbd5e1;padding:8px 12px;text-align:center}
table.ppt-table th{background:#1b365d;color:#fff;font-weight:700;font-size:.82rem}
table.ppt-table tr:nth-child(even) td{background:#f8fafc}
table.ppt-table .hl{background:#fef9c3;font-weight:700;color:#92400e}
table.ppt-table .opt{background:#dcfce7;font-weight:700;color:#166534}

/* TRANSPORTATION TABLEAU (PPT STYLE) */
.tp-wrap{overflow-x:auto;margin:14px 0}
.tp-table{border-collapse:collapse;width:100%;font-size:.83rem;min-width:480px}
.tp-table th,.tp-table td{border:2px solid #94a3b8;padding:0;text-align:center;min-width:85px;position:relative}
.tp-table th{background:#1b365d;color:#fff;font-weight:700;padding:9px 10px;font-size:.83rem}
.tp-table .src-lbl{background:#334155;color:#fff;font-weight:700;padding:9px 12px;font-size:.83rem}
.tp-table .dem-lbl{background:#475569;color:#fff;font-weight:700;padding:8px 12px;font-size:.8rem}
.tp-cell{position:relative;height:65px;min-width:85px;background:#fff}
.cost-box{position:absolute;top:2px;right:3px;font-size:.7rem;color:#475569;font-weight:700;border:1px solid #cbd5e1;padding:1px 5px;background:#f8fafc;border-radius:2px}
.alloc-box{position:absolute;bottom:5px;left:0;right:0;text-anchor:middle;font-size:1.05rem;font-weight:800;color:#1b365d}
.cell-active{background:#fef9c3 !important;border:3px solid #f59e0b !important}
.cell-done{background:#dbeafe !important}
.cell-exhaust{background:#f1f5f9;opacity:.7}
.supply-val{background:#f0fdf4;color:#166534;font-weight:700;padding:9px;font-size:.86rem;border:2px solid #94a3b8}
.demand-val{background:#f0fdf4;color:#166534;font-weight:700;padding:8px;font-size:.86rem;border:2px solid #94a3b8}

/* ASSIGNMENT MATRIX (PPT HUNGARIAN STYLE) */
.asgn-table{border-collapse:collapse;font-size:.86rem;margin:12px auto;min-width:400px}
.asgn-table th,.asgn-table td{border:2px solid #94a3b8;padding:10px 16px;text-align:center;min-width:65px;font-weight:600;position:relative}
.asgn-table th{background:#1b365d;color:#fff}
.asgn-table .row-lbl{background:#334155;color:#fff;font-weight:700}
.az-zero{color:#2563eb;font-weight:800;background:#eff6ff}
.az-assigned{color:#fff;background:#16a34a !important;font-weight:800}
.line-row{border-top:3px solid #ef4444 !important;border-bottom:3px solid #ef4444 !important;background:#fee2e2}
.line-col{border-left:3px solid #ef4444 !important;border-right:3px solid #ef4444 !important;background:#fee2e2}

/* SHORTEST PATH TABLE (PPT SLIDE 36 EXACT MATCH) */
table.sp-ppt-table{border-collapse:collapse;width:100%;font-size:.82rem;margin:12px 0}
table.sp-ppt-table th{background:#1b365d;color:#fff;padding:8px 10px;text-align:center}
table.sp-ppt-table td{border:1px solid #cbd5e1;padding:8px 10px;text-align:center}
table.sp-ppt-table tr:nth-child(even){background:#f8fafc}
table.sp-ppt-table .active-row{background:#fef9c3;font-weight:700}

/* STEP NAVIGATION BAR */
.step-nav{display:flex;align-items:center;gap:12px;margin:16px 0;flex-wrap:wrap}
.snav-btn{padding:8px 18px;border-radius:5px;border:1px solid #d1d5db;background:#fff;font-size:.84rem;font-weight:600;cursor:pointer;transition:all .15s;color:#374151}
.snav-btn:hover:not(:disabled){background:#f0f7ff;border-color:#93c5fd;color:#1d4ed8}
.snav-btn:disabled{opacity:.4;cursor:not-allowed}
.snav-count{font-size:.85rem;color:#64748b;font-weight:600;margin:0 4px}

/* RESULT BOX */
.res-box{background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:14px 18px;margin-top:14px}
.res-box h4{font-size:.9rem;font-weight:700;color:#166534;margin-bottom:6px}
.res-box ul{font-size:.84rem;color:#166534;padding-left:18px}
.res-box li{margin-bottom:4px}

/* ANIMATIONS & UTILS */
.fade-in{animation:fadeIn .22s ease both}
@keyframes fadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.pill-row{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.sep{height:1px;background:#e2e8f0;margin:16px 0}
.btn{padding:9px 20px;border-radius:5px;border:none;font-size:.86rem;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:6px;transition:all .15s}
.btn-primary{background:#2563eb;color:#fff}
.btn-primary:hover{background:#1d4ed8}
.btn-sec{background:#fff;color:#374151;border:1px solid #d1d5db}
.btn-sec:hover{background:#f9fafb}
</style>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const {useState,useEffect,useRef}=React;

function HTML({h}){return <div dangerouslySetInnerHTML={{__html:h}}/>}

// ====================================================================
// STEP ACCORDION (For LPP & General Problems)
// ====================================================================
function StepCard({step,index,forceOpen}){
  const [open,setOpen]=useState(index===0);
  useEffect(()=>{if(forceOpen!==undefined) setOpen(forceOpen);},[forceOpen]);
  return(
    <div className="step-card fade-in" style={{animationDelay:`${index*.05}s`}}>
      <div className={`step-hd ${open?'open':''}`} onClick={()=>setOpen(o=>!o)}>
        <h3><span className="snum">{index+1}</span>{step.title}</h3>
        <span style={{color:'#64748b'}}>{open?'▲':'▼'}</span>
      </div>
      <div className={`step-bd ${open?'show':''}`}>
        {step.explain&&<div className="ppt-explain"><HTML h={step.explain}/></div>}
        {step.formulation&&<div className="ppt-formulation"><HTML h={step.formulation}/></div>}
        {step.body&&<HTML h={step.body}/>}
      </div>
    </div>
  );
}

// ====================================================================
// TRANSPORTATION VIEWER (PPT TABLEAU FORMAT)
// ====================================================================
function TransportTable({step,rows,cols}){
  const {costs,allocs,supply,demand,activeCell,doneCells=[]}=step;
  const isDone=(r,c)=>doneCells.some(([dr,dc])=>dr===r&&dc===c);
  const isActive=(r,c)=>activeCell&&activeCell[0]===r&&activeCell[1]===c;
  return(
    <div className="tp-wrap">
      <table className="tp-table">
        <thead>
          <tr>
            <th style={{background:'#1b365d'}}>Plant / Warehouse \ DC</th>
            {cols.map((c,i)=><th key={i}>{c}</th>)}
            <th style={{background:'#334155'}}>Supply</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r,ri)=>(
            <tr key={ri}>
              <td className="src-lbl">{r}</td>
              {cols.map((_,ci)=>(
                <td key={ci} className={`tp-cell ${isActive(ri,ci)?'cell-active':isDone(ri,ci)?'cell-done':supply[ri]===0&&!isActive(ri,ci)?'cell-exhaust':''}`}>
                  <span className="cost-box">{costs[ri][ci]}</span>
                  {allocs[ri][ci]>0&&<span className="alloc-box">{allocs[ri][ci]}</span>}
                </td>
              ))}
              <td className="supply-val">{supply[ri]}</td>
            </tr>
          ))}
          <tr>
            <td className="dem-lbl">Demand</td>
            {cols.map((_,ci)=><td key={ci} className="demand-val">{demand[ci]}</td>)}
            <td style={{background:'#f8fafc'}}></td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

function TransportViewer({problem}){
  const {rows,cols,methods}=problem;
  const [methodIdx,setMethodIdx]=useState(0);
  const [stepIdx,setStepIdx]=useState(0);
  const method=methods[methodIdx];
  const steps=method.steps;
  const step=steps[stepIdx];
  return(
    <div>
      <div className="pill-row">
        {methods.map((m,i)=>(
          <button key={i} onClick={()=>{setMethodIdx(i);setStepIdx(0);}}
            style={{padding:'6px 16px',borderRadius:'4px',border:'1px solid',cursor:'pointer',fontSize:'.82rem',fontWeight:600,
              background:methodIdx===i?'#2563eb':'#fff',color:methodIdx===i?'#fff':'#374151',borderColor:methodIdx===i?'#2563eb':'#d1d5db'}}>
            {m.name}
          </button>
        ))}
      </div>
      <div className="ppt-explain"><HTML h={method.intro}/></div>
      <TransportTable step={step} rows={rows} cols={cols}/>
      {step.penalties&&(
        <div style={{margin:'10px 0',fontSize:'.82rem'}}>
          <strong>Penalties: </strong>
          {step.penalties.row&&step.penalties.row.map((p,i)=><span key={i} className="tag" style={{marginRight:'6px'}}>Row {i+1}: {p}</span>)}
          {step.penalties.col&&step.penalties.col.map((p,i)=><span key={i} className="tag" style={{background:'#f0fdf4',color:'#166534',borderColor:'#86efac',marginRight:'6px'}}>Col {i+1}: {p}</span>)}
        </div>
      )}
      <div className="ppt-explain"><strong>{step.title}</strong><br/><HTML h={step.explain}/></div>
      <div className="step-nav">
        <button className="snav-btn" onClick={()=>setStepIdx(i=>i-1)} disabled={stepIdx===0}>◀ Previous Step</button>
        <span className="snav-count">Step {stepIdx+1} of {steps.length}</span>
        <button className="snav-btn" onClick={()=>setStepIdx(i=>i+1)} disabled={stepIdx===steps.length-1}>Next Step ▶</button>
      </div>
      {stepIdx===steps.length-1&&step.result&&(
        <div className="res-box"><h4>✅ {method.name} – Final Result</h4><HTML h={step.result}/></div>
      )}
    </div>
  );
}

// ====================================================================
// ASSIGNMENT VIEWER (PPT HUNGARIAN STEPS)
// ====================================================================
function AssignmentViewer({problem}){
  const {rowLabels,colLabels,steps}=problem;
  const [idx,setIdx]=useState(0);
  const step=steps[idx];
  return(
    <div>
      <div className="ppt-explain"><strong>{step.title}</strong><br/><HTML h={step.explain}/></div>
      <div className="table-wrap">
        <table className="asgn-table">
          <thead>
            <tr>
              <th style={{background:'#1b365d'}}>Child / Machine \ Chore / Location</th>
              {colLabels.map((c,i)=><th key={i}>{c}</th>)}
              {step.showRowMin&&<th style={{background:'#475569'}}>Row Min ($p_i$)</th>}
            </tr>
          </thead>
          <tbody>
            {step.matrix.map((row,ri)=>(
              <tr key={ri}>
                <td className="row-lbl">{rowLabels[ri]}</td>
                {row.map((val,ci)=>{
                  const isZero=val===0;
                  const isAssigned=step.assignment&&step.assignment.some(([r,c])=>r===ri&&c===ci);
                  const linedRow=step.lineRows&&step.lineRows.includes(ri);
                  const linedCol=step.lineCols&&step.lineCols.includes(ci);
                  let cls=isAssigned?'az-assigned':isZero?'az-zero':'';
                  if(linedRow) cls+=' line-row';
                  if(linedCol) cls+=' line-col';
                  return <td key={ci} className={cls}>{val===999?'M':val}</td>;
                })}
                {step.showRowMin&&<td style={{background:'#fef9c3',fontWeight:700,color:'#92400e'}}>{step.rowMins[ri]}</td>}
              </tr>
            ))}
            {step.showColMin&&(
              <tr>
                <td style={{background:'#475569',color:'#fff',fontWeight:700}}>Col Min ($q_j$)</td>
                {step.colMins.map((v,i)=><td key={i} style={{background:'#fffbeb',fontWeight:700,color:'#92400e'}}>{v}</td>)}
                <td></td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      <div className="step-nav">
        <button className="snav-btn" onClick={()=>setIdx(i=>i-1)} disabled={idx===0}>◀ Previous Step</button>
        <span className="snav-count">Step {idx+1} of {steps.length}</span>
        <button className="snav-btn" onClick={()=>setIdx(i=>i+1)} disabled={idx===steps.length-1}>Next Step ▶</button>
      </div>
      {idx===steps.length-1&&step.result&&(
        <div className="res-box"><h4>✅ Final Optimal Assignment</h4><HTML h={step.result}/></div>
      )}
    </div>
  );
}

// ====================================================================
// SHORTEST PATH VIEWER (EXACT SEERVADA PARK SLIDE 36 TABLE)
// ====================================================================
function ShortestPathViewer({problem}){
  const {steps,result,traceback}=problem;
  const [idx,setIdx]=useState(steps.length-1);
  return(
    <div>
      <div className="ppt-explain"><strong>Shortest Path Algorithm Table (PPT Slide 36 Format)</strong><br/>Determine $n$-th nearest node to origin $O$ until destination $T$ is reached.</div>
      <div className="table-wrap">
        <table className="sp-ppt-table">
          <thead>
            <tr>
              <th>n</th>
              <th>Solved Nodes Directly Connected to Unsolved Nodes</th>
              <th>Closest Connected Unsolved Node</th>
              <th>Total Distance Involved</th>
              <th>nth Nearest Node</th>
              <th>Minimum Distance</th>
              <th>Last Connection</th>
            </tr>
          </thead>
          <tbody>
            {steps.map((s,i)=>(
              <tr key={i} className={i===idx?'active-row':''}>
                <td><strong>{s.n}</strong></td>
                <td>{s.solvedNodes}</td>
                <td>{s.closestUnsolved}</td>
                <td>{s.totalDist}</td>
                <td><strong style={{color:'#1d4ed8'}}>{s.nthNode}</strong></td>
                <td><strong style={{color:'#166534'}}>{s.minDist}</strong></td>
                <td><strong>{s.lastConn}</strong></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="ppt-explain">
        <strong>Trace Shortest Path from Destination to Origin:</strong><br/>
        <span style={{fontSize:'1.05rem',fontFamily:'monospace',color:'#1d4ed8'}}>{traceback}</span>
      </div>
      <div className="res-box"><h4>✅ Optimal Route & Distance</h4><HTML h={result}/></div>
    </div>
  );
}

// ====================================================================
// MST VIEWER (EXACT SEERVADA PARK PPT STEPS)
// ====================================================================
function MSTViewer({problem}){
  const {steps,result}=problem;
  const [idx,setStepIdx]=useState(0);
  const step=steps[idx];
  return(
    <div>
      <div className="ppt-explain"><strong>Minimum Spanning Tree Algorithm (PPT Slides 39–47 Format)</strong><br/>Iteratively connect the unconnected node closest to any currently connected node.</div>
      <div className="step-card" style={{margin:'14px 0'}}>
        <div className="step-hd open">
          <h3><span className="snum">{idx+1}</span>{step.title}</h3>
        </div>
        <div className="step-bd show">
          <div className="ppt-explain"><HTML h={step.explain}/></div>
          <div className="tp-wrap">
            <table className="ppt-table">
              <thead><tr><th>Step</th><th>Connected Nodes Set</th><th>Unconnected Node Added</th><th>Link Used</th><th>Link Length</th><th>Total Cable Length</th></tr></thead>
              <tbody>
                {steps.slice(0,idx+1).map((s,i)=>(
                  <tr key={i} className={i===idx?'hl':''}>
                    <td>{s.stepNum}</td>
                    <td>{s.connectedSet}</td>
                    <td><strong style={{color:'#1d4ed8'}}>{s.addedNode}</strong></td>
                    <td><strong>{s.linkUsed}</strong></td>
                    <td>{s.linkLen}</td>
                    <td><strong style={{color:'#166534'}}>{s.totalLength}</strong></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div className="step-nav">
        <button className="snav-btn" onClick={()=>setStepIdx(i=>i-1)} disabled={idx===0}>◀ Previous Step</button>
        <span className="snav-count">Step {idx+1} of {steps.length}</span>
        <button className="snav-btn" onClick={()=>setStepIdx(i=>i+1)} disabled={idx===steps.length-1}>Next Step ▶</button>
      </div>
      {idx===steps.length-1&&<div className="res-box"><h4>✅ Minimum Spanning Tree Complete</h4><HTML h={result}/></div>}
    </div>
  );
}

// ====================================================================
// ROUTER FOR PROBLEM TYPES
// ====================================================================
function ProblemDetail({problem,onBack,moduleColor}){
  const [allOpen,setAllOpen]=useState(false);
  const renderContent=()=>{
    switch(problem.type){
      case 'transport': return <TransportViewer problem={problem}/>;
      case 'assignment': return <AssignmentViewer problem={problem}/>;
      case 'shortest_ppt': return <ShortestPathViewer problem={problem}/>;
      case 'mst_ppt': return <MSTViewer problem={problem}/>;
      default: return(
        <div>
          <div style={{display:'flex',justifyContent:'flex-end',marginBottom:'12px'}}>
            <button className="btn btn-sec" style={{fontSize:'.78rem',padding:'5px 12px'}} onClick={()=>setAllOpen(o=>!o)}>
              {allOpen?'▲ Collapse All':'▼ Expand All'}
            </button>
          </div>
          {(problem.steps||[]).map((s,i)=><StepCard key={i} step={s} index={i} forceOpen={allOpen?true:i===0?true:undefined}/>)}
        </div>
      );
    }
  };
  return(
    <div>
      <button className="back-btn" onClick={onBack}>← Back to Problems</button>
      <div className="fade-in">
        {problem.isPPT&&<div className="ppt-badge">📌 Official PPT Lecture Example (Day 1 / Day 2)</div>}
        {problem.isBook&&<div className="book-badge">📖 Textbook Classic (Hillier & Lieberman / Taha / Winston)</div>}
        <div className="prob-header" style={{'--c':moduleColor}}>
          <h2>{problem.title}</h2>
          <p>{problem.context}</p>
        </div>
        <div className="prob-body">
          <div className="pill-row">
            {(problem.tags||[]).map(t=><span key={t} className="tag">{t}</span>)}
            <span className={`diff ${problem.difficulty==='easy'?'d-easy':problem.difficulty==='hard'?'d-hard':'d-med'}`}>{problem.difficulty}</span>
          </div>
          <div className="sep"/>
          {renderContent()}
        </div>
      </div>
    </div>
  );
}

// ====================================================================
// PROBLEM LIST
// ====================================================================
function ProblemList({module,onSelect,onBack}){
  const [filter,setFilter]=useState('all');
  const filtered=filter==='all'?module.problems:module.problems.filter(p=>p.difficulty===filter);
  return(
    <div>
      <button className="back-btn" onClick={onBack}>← Back to Modules</button>
      <div className="sec-title">{module.icon} {module.title}</div>
      <p className="sec-desc">{module.desc}</p>
      <div style={{display:'flex',gap:'8px',marginBottom:'16px',flexWrap:'wrap',alignItems:'center'}}>
        {['all','easy','medium','hard'].map(d=>(
          <button key={d} onClick={()=>setFilter(d)} style={{padding:'5px 14px',borderRadius:'4px',border:'1px solid',cursor:'pointer',fontSize:'.8rem',fontWeight:600,background:filter===d?module.color:'#fff',color:filter===d?'#fff':'#374151',borderColor:filter===d?module.color:'#d1d5db'}}>
            {d.charAt(0).toUpperCase()+d.slice(1)}
          </button>
        ))}
        <span style={{marginLeft:'auto',fontSize:'.82rem',color:'#64748b'}}>{filtered.length} problems</span>
      </div>
      <div className="prob-list">
        {filtered.map((p,i)=>(
          <div key={p.id} className="prob-item fade-in" style={{animationDelay:`${i*.03}s`}} onClick={()=>onSelect(p)}>
            <div>
              <h4>
                {p.isPPT&&<span style={{color:'#c2410c'}}>📌 [PPT] </span>}
                {p.isBook&&<span style={{color:'#166534'}}>📖 [Book] </span>}
                {i+1}. {p.title}
              </h4>
              <p>{p.context.slice(0,98)}…</p>
            </div>
            <div style={{display:'flex',alignItems:'center',gap:'10px',flexShrink:0}}>
              <span className={`diff ${p.difficulty==='easy'?'d-easy':p.difficulty==='hard'?'d-hard':'d-med'}`}>{p.difficulty}</span>
              <span style={{color:'#94a3b8',fontSize:'1.1rem'}}>›</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// ====================================================================
// MODULE HOME
// ====================================================================
function ModuleHome({modules,onSelect}){
  return(
    <div>
      <h2 style={{fontSize:'1.15rem',fontWeight:700,color:'#1b365d',marginBottom:'4px'}}>Select a Topic to Explore</h2>
      <p style={{fontSize:'.86rem',color:'#64748b',marginBottom:'20px'}}>Includes 15+ step-by-step problems per module from Day 1 & Day 2 PPTs and Hillier & Lieberman, Taha, Winston textbooks.</p>
      <div className="mod-grid">
        {modules.map((m,i)=>(
          <div key={m.id} className="mod-card fade-in" style={{'--c':m.color,animationDelay:`${i*.07}s`}} onClick={()=>onSelect(m)}>
            <div style={{fontSize:'1.8rem'}}>{m.icon}</div>
            <h3>{m.title}</h3>
            <p>{m.desc}</p>
            <span className="mod-badge">{m.problems.length} Problems</span>
          </div>
        ))}
      </div>
    </div>
  );
}
"""

print("Helper template ready.")
