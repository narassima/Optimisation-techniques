import json
import os

print("Writing make_vanilla_75_direct.py...")

# Read data definitions from build_full_75_clean.py
with open("build_full_75_clean.py", "r", encoding="utf-8") as f:
    clean_js = f.read()

data_and_modules = clean_js.split("const MODULES=")[0]
modules_def = "const MODULES=" + clean_js.split("const MODULES=")[1].split("// ====================================================================")[0]

vanilla_renderer = """
// ====================================================================
// VANILLA JS ZERO-DEPENDENCY APP RENDERER
// ====================================================================

const state = {
  currentTab: 'home',
  selectedModule: null,
  selectedProblem: null,
  difficultyFilter: 'all',
  tpMethodIndex: 0,
  tpStepIndex: 0,
  asgnStepIndex: 0,
  spStepIndex: 0,
  mstStepIndex: 0
};

function renderApp() {
  const root = document.getElementById('root');
  if (!root) return;

  const tabs = [
    { id: 'home', label: '🏠 Home' },
    ...MODULES.map(m => ({ id: m.id, label: `${m.icon} ${m.title.split('(')[0].trim()}` }))
  ];

  let mainHtml = '';

  if (state.currentTab === 'home') {
    mainHtml = renderHome();
  } else {
    const mod = state.selectedModule || MODULES.find(m => m.id === state.currentTab);
    if (!mod) {
      mainHtml = '<div>Module not found</div>';
    } else if (state.selectedProblem) {
      mainHtml = renderProblemDetail(state.selectedProblem, mod);
    } else {
      mainHtml = renderProblemList(mod);
    }
  }

  root.innerHTML = `
    <div id="app-header">
      <div class="header-inner" style="max-width:1320px;margin:0 auto;padding:18px 24px 12px;display:flex;align-items:center;justify-content:space-between;">
        <div style="display:flex;align-items:center;gap:14px;">
          <div style="font-size:2.2rem;">📐</div>
          <div>
            <h1 style="font-size:1.45rem;font-weight:700;">OR Learning Hub – OTDM</h1>
            <p style="font-size:.83rem;opacity:.88;margin-top:2px;">PGDM 2024-2026 · Great Lakes Institute of Management</p>
          </div>
        </div>
      </div>
      <div class="nav-strip">
        <div class="nav-strip-inner">
          ${tabs.map(t => `<button class="ntab ${state.currentTab === t.id ? 'active' : ''}" onclick="gotoTab('${t.id}')">${t.label}</button>`).join('')}
        </div>
      </div>
    </div>
    <main class="main">${mainHtml}</main>
  `;
}

function gotoTab(tabId) {
  state.currentTab = tabId;
  state.selectedProblem = null;
  state.tpStepIndex = 0;
  state.asgnStepIndex = 0;
  state.mstStepIndex = 0;
  if (tabId === 'home') state.selectedModule = null;
  else state.selectedModule = MODULES.find(m => m.id === tabId) || null;
  renderApp();
}

function selectModule(modId) {
  const mod = MODULES.find(m => m.id === modId);
  if (mod) {
    state.selectedModule = mod;
    state.currentTab = modId;
    state.selectedProblem = null;
    renderApp();
  }
}

function selectProblem(probId) {
  const mod = state.selectedModule || MODULES.find(m => m.id === state.currentTab);
  if (mod) {
    const prob = mod.problems.find(p => p.id === probId);
    if (prob) {
      state.selectedProblem = prob;
      state.tpStepIndex = 0;
      state.asgnStepIndex = 0;
      state.mstStepIndex = 0;
      renderApp();
    }
  }
}

function backToList() {
  state.selectedProblem = null;
  renderApp();
}

function filterDifficulty(diff) {
  state.difficultyFilter = diff;
  renderApp();
}

function setTpMethod(idx) {
  state.tpMethodIndex = idx;
  state.tpStepIndex = 0;
  renderApp();
}

function navTpStep(delta) {
  state.tpStepIndex += delta;
  renderApp();
}

function navAsgnStep(delta) {
  state.asgnStepIndex += delta;
  renderApp();
}

function navMstStep(delta) {
  state.mstStepIndex += delta;
  renderApp();
}

// HOME VIEW
function renderHome() {
  return `
    <h2 style="font-size:1.15rem;font-weight:700;color:#1b365d;margin-bottom:4px;">Select a Topic to Explore</h2>
    <p style="font-size:.86rem;color:#64748b;margin-bottom:20px;">Includes 15+ step-by-step problems per module from Day 1 & Day 2 PPTs and Hillier & Lieberman, Taha, Winston textbooks.</p>
    <div class="mod-grid">
      ${MODULES.map(m => `
        <div class="mod-card" style="--c:${m.color};" onclick="selectModule('${m.id}')">
          <div style="font-size:1.8rem;">${m.icon}</div>
          <h3>${m.title}</h3>
          <p>${m.desc}</p>
          <span class="mod-badge">${m.problems.length} Problems</span>
        </div>
      `).join('')}
    </div>
  `;
}

// LIST VIEW
function renderProblemList(module) {
  const filtered = state.difficultyFilter === 'all' ? module.problems : module.problems.filter(p => p.difficulty === state.difficultyFilter);
  return `
    <button class="back-btn" onclick="gotoTab('home')">← Back to Modules</button>
    <div class="sec-title">${module.icon} ${module.title}</div>
    <p class="sec-desc">${module.desc}</p>
    <div style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap;align-items:center;">
      ${['all','easy','medium','hard'].map(d => `
        <button onclick="filterDifficulty('${d}')" style="padding:5px 14px;border-radius:4px;border:1px solid;cursor:pointer;font-size:.8rem;font-weight:600;background:${state.difficultyFilter === d ? module.color : '#fff'};color:${state.difficultyFilter === d ? '#fff' : '#374151'};border-color:${state.difficultyFilter === d ? module.color : '#d1d5db'};">
          ${d.charAt(0).toUpperCase() + d.slice(1)}
        </button>
      `).join('')}
      <span style="margin-left:auto;font-size:.82rem;color:#64748b;">${filtered.length} problems</span>
    </div>
    <div class="prob-list">
      ${filtered.map((p, i) => `
        <div class="prob-item" onclick="selectProblem('${p.id}')">
          <div>
            <h4>
              ${p.isPPT ? '<span style="color:#c2410c;">📌 [PPT] </span>' : ''}
              ${p.isBook ? '<span style="color:#166534;">📖 [Book] </span>' : ''}
              ${i+1}. ${p.title}
            </h4>
            <p>${p.context.slice(0, 98)}…</p>
          </div>
          <div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
            <span class="diff ${p.difficulty === 'easy' ? 'd-easy' : p.difficulty === 'hard' ? 'd-hard' : 'd-med'}">${p.difficulty}</span>
            <span style="color:#94a3b8;font-size:1.1rem;">›</span>
          </div>
        </div>
      `).join('')}
    </div>
  `;
}

// DETAIL VIEW
function renderProblemDetail(problem, module) {
  let contentHtml = '';

  if (problem.type === 'transport') {
    contentHtml = renderTransportDetail(problem);
  } else if (problem.type === 'assignment') {
    contentHtml = renderAssignmentDetail(problem);
  } else if (problem.type === 'shortest_ppt') {
    contentHtml = renderShortestDetail(problem);
  } else if (problem.type === 'mst_ppt') {
    contentHtml = renderMstDetail(problem);
  } else {
    contentHtml = renderGeneralStepsDetail(problem);
  }

  return `
    <button class="back-btn" onclick="backToList()">← Back to Problems</button>
    <div>
      ${problem.isPPT ? '<div class="ppt-badge">📌 Official PPT Lecture Example (Day 1 / Day 2)</div>' : ''}
      ${problem.isBook ? '<div class="book-badge">📖 Textbook Classic (Hillier & Lieberman / Taha / Winston)</div>' : ''}
      <div class="prob-header" style="--c:${module.color};">
        <h2>${problem.title}</h2>
        <p>${problem.context}</p>
      </div>
      <div class="prob-body">
        <div class="pill-row">
          ${(problem.tags || []).map(t => `<span class="tag">${t}</span>`).join('')}
          <span class="diff ${problem.difficulty === 'easy' ? 'd-easy' : problem.difficulty === 'hard' ? 'd-hard' : 'd-med'}">${problem.difficulty}</span>
        </div>
        <div class="sep"></div>
        ${contentHtml}
      </div>
    </div>
  `;
}

// LPP / GENERAL STEPS RENDERER
function renderGeneralStepsDetail(problem) {
  return (problem.steps || []).map((s, i) => `
    <div class="step-card">
      <div class="step-hd open">
        <h3><span class="snum">${i+1}</span>${s.title}</h3>
      </div>
      <div class="step-bd show">
        ${s.explain ? `<div class="ppt-explain">${s.explain}</div>` : ''}
        ${s.formulation ? `<div class="ppt-formulation">${s.formulation}</div>` : ''}
        ${s.body ? `<div>${s.body}</div>` : ''}
      </div>
    </div>
  `).join('');
}

// TRANSPORT RENDERER
function renderTransportDetail(problem) {
  const method = problem.methods[state.tpMethodIndex];
  const steps = method.steps;
  const step = steps[state.tpStepIndex];

  const isDone = (r, c) => (step.doneCells || []).some(([dr, dc]) => dr === r && dc === c);
  const isActive = (r, c) => step.activeCell && step.activeCell[0] === r && step.activeCell[1] === c;

  return `
    <div class="pill-row">
      ${problem.methods.map((m, i) => `
        <button onclick="setTpMethod(${i})" style="padding:6px 16px;border-radius:4px;border:1px solid;cursor:pointer;font-size:.82rem;font-weight:600;background:${state.tpMethodIndex === i ? '#2563eb' : '#fff'};color:${state.tpMethodIndex === i ? '#fff' : '#374151'};border-color:${state.tpMethodIndex === i ? '#2563eb' : '#d1d5db'};">
          ${m.name}
        </button>
      `).join('')}
    </div>
    <div class="ppt-explain">${method.intro}</div>
    <div class="tp-wrap">
      <table class="tp-table">
        <thead>
          <tr>
            <th style="background:#1b365d;">Plant / Warehouse \\ DC</th>
            ${problem.cols.map(c => `<th>${c}</th>`).join('')}
            <th style="background:#334155;">Supply</th>
          </tr>
        </thead>
        <tbody>
          ${problem.rows.map((r, ri) => `
            <tr>
              <td class="src-lbl">${r}</td>
              ${problem.cols.map((_, ci) => {
                const active = isActive(ri, ci);
                const done = isDone(ri, ci);
                const exhaust = step.supply[ri] === 0 && !active;
                const cls = active ? 'cell-active' : done ? 'cell-done' : exhaust ? 'cell-exhaust' : '';
                const alloc = step.allocs[ri][ci];
                return `
                  <td class="tp-cell ${cls}">
                    <span class="cost-box">${step.costs[ri][ci]}</span>
                    ${alloc > 0 ? `<span class="alloc-box">${alloc}</span>` : ''}
                  </td>
                `;
              }).join('')}
              <td class="supply-val">${step.supply[ri]}</td>
            </tr>
          `).join('')}
          <tr>
            <td class="dem-lbl">Demand</td>
            ${problem.cols.map((_, ci) => `<td class="demand-val">${step.demand[ci]}</td>`).join('')}
            <td style="background:#f8fafc;"></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="ppt-explain"><strong>${step.title}</strong><br/>${step.explain}</div>
    <div class="step-nav">
      <button class="snav-btn" onclick="navTpStep(-1)" ${state.tpStepIndex === 0 ? 'disabled' : ''}>◀ Previous Step</button>
      <span class="snav-count">Step ${state.tpStepIndex + 1} of ${steps.length}</span>
      <button class="snav-btn" onclick="navTpStep(1)" ${state.tpStepIndex === steps.length - 1 ? 'disabled' : ''}>Next Step ▶</button>
    </div>
    ${state.tpStepIndex === steps.length - 1 && step.result ? `<div class="res-box"><h4>✅ ${method.name} – Final Result</h4>${step.result}</div>` : ''}
  `;
}

// ASSIGNMENT RENDERER
function renderAssignmentDetail(problem) {
  const steps = problem.steps;
  const step = steps[state.asgnStepIndex];

  return `
    <div class="ppt-explain"><strong>${step.title}</strong><br/>${step.explain}</div>
    <div class="table-wrap">
      <table class="asgn-table">
        <thead>
          <tr>
            <th style="background:#1b365d;">Child / Machine \\ Chore / Location</th>
            ${problem.colLabels.map(c => `<th>${c}</th>`).join('')}
            ${step.showRowMin ? '<th style="background:#475569;">Row Min ($p_i$)</th>' : ''}
          </tr>
        </thead>
        <tbody>
          ${step.matrix.map((row, ri) => `
            <tr>
              <td class="row-lbl">${problem.rowLabels[ri]}</td>
              ${row.map((val, ci) => {
                const isZero = val === 0;
                const isAssigned = step.assignment && step.assignment.some(([r, c]) => r === ri && c === ci);
                const linedRow = step.lineRows && step.lineRows.includes(ri);
                const linedCol = step.lineCols && step.lineCols.includes(ci);
                let cls = isAssigned ? 'az-assigned' : isZero ? 'az-zero' : '';
                if (linedRow) cls += ' line-row';
                if (linedCol) cls += ' line-col';
                return `<td class="${cls}">${val === 999 ? 'M' : val}</td>`;
              }).join('')}
              ${step.showRowMin ? `<td style="background:#fef9c3;font-weight:700;color:#92400e;">${step.rowMins[ri]}</td>` : ''}
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>
    <div class="step-nav">
      <button class="snav-btn" onclick="navAsgnStep(-1)" ${state.asgnStepIndex === 0 ? 'disabled' : ''}>◀ Previous Step</button>
      <span class="snav-count">Step ${state.asgnStepIndex + 1} of ${steps.length}</span>
      <button class="snav-btn" onclick="navAsgnStep(1)" ${state.asgnStepIndex === steps.length - 1 ? 'disabled' : ''}>Next Step ▶</button>
    </div>
    ${state.asgnStepIndex === steps.length - 1 && step.result ? `<div class="res-box"><h4>✅ Final Optimal Assignment</h4>${step.result}</div>` : ''}
  `;
}

// SHORTEST PATH RENDERER
function renderShortestDetail(problem) {
  return `
    <div class="ppt-explain"><strong>Shortest Path Algorithm Table (PPT Slide 36 Format)</strong><br/>Determine n-th nearest node to origin O until destination T is reached.</div>
    <div class="table-wrap">
      <table class="sp-ppt-table">
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
          ${problem.steps.map((s, i) => `
            <tr class="${i === problem.steps.length - 1 ? 'active-row' : ''}">
              <td><strong>${s.n}</strong></td>
              <td>${s.solvedNodes}</td>
              <td>${s.closestUnsolved}</td>
              <td>${s.totalDist}</td>
              <td><strong style="color:#1d4ed8;">${s.nthNode}</strong></td>
              <td><strong style="color:#166534;">${s.minDist}</strong></td>
              <td><strong>${s.lastConn}</strong></td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>
    <div class="ppt-explain">
      <strong>Trace Shortest Path from Destination to Origin:</strong><br/>
      <span style="font-size:1.05rem;font-family:monospace;color:#1d4ed8;">${problem.traceback}</span>
    </div>
    <div class="res-box"><h4>✅ Optimal Route & Distance</h4>${problem.result}</div>
  `;
}

// MST RENDERER
function renderMstDetail(problem) {
  const steps = problem.steps;
  const step = steps[state.mstStepIndex];

  return `
    <div class="ppt-explain"><strong>Minimum Spanning Tree Algorithm (PPT Slides 39–47 Format)</strong><br/>Iteratively connect the unconnected node closest to any currently connected node.</div>
    <div class="step-card" style="margin:14px 0;">
      <div class="step-hd open">
        <h3><span class="snum">${state.mstStepIndex + 1}</span>${step.title}</h3>
      </div>
      <div class="step-bd show">
        <div class="ppt-explain">${step.explain}</div>
        <div class="tp-wrap">
          <table class="ppt-table">
            <thead>
              <tr><th>Step</th><th>Connected Nodes Set</th><th>Unconnected Node Added</th><th>Link Used</th><th>Link Length</th><th>Total Cable Length</th></tr>
            </thead>
            <tbody>
              ${steps.slice(0, state.mstStepIndex + 1).map((s, i) => `
                <tr class="${i === state.mstStepIndex ? 'hl' : ''}">
                  <td>${s.stepNum}</td>
                  <td>${s.connectedSet}</td>
                  <td><strong style="color:#1d4ed8;">${s.addedNode}</strong></td>
                  <td><strong>${s.linkUsed}</strong></td>
                  <td>${s.linkLen}</td>
                  <td><strong style="color:#166534;">${s.totalLength}</strong></td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="step-nav">
      <button class="snav-btn" onclick="navMstStep(-1)" ${state.mstStepIndex === 0 ? 'disabled' : ''}>◀ Previous Step</button>
      <span class="snav-count">Step ${state.mstStepIndex + 1} of ${steps.length}</span>
      <button class="snav-btn" onclick="navMstStep(1)" ${state.mstStepIndex === steps.length - 1 ? 'disabled' : ''}>Next Step ▶</button>
    </div>
    ${state.mstStepIndex === steps.length - 1 ? `<div class="res-box"><h4>✅ Minimum Spanning Tree Complete</h4>${problem.result}</div>` : ''}
  `;
}

// INITIALIZE ON DOM LOAD
document.addEventListener('DOMContentLoaded', renderApp);
"""

# Construct full standalone HTML
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>OR Learning Hub – OTDM (PGDM)</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:#f4f6f9;color:#1a202c;min-height:100vh;line-height:1.6}}
#app-header{{background:linear-gradient(135deg,#1b365d 0%,#2563eb 60%,#0f2b5c 100%);color:#fff;position:sticky;top:0;z-index:100;box-shadow:0 3px 14px rgba(0,0,0,.2)}}
.nav-strip{{background:rgba(0,0,0,.25);overflow-x:auto;white-space:nowrap}}
.nav-strip-inner{{max-width:1320px;margin:0 auto;display:flex}}
.ntab{{padding:11px 20px;font-size:.84rem;font-weight:600;color:rgba(255,255,255,.75);border:none;background:transparent;cursor:pointer;border-bottom:3px solid transparent;transition:all .18s;flex-shrink:0}}
.ntab:hover{{color:#fff;background:rgba(255,255,255,.08)}}
.ntab.active{{color:#fff;border-bottom-color:#60a5fa;background:rgba(255,255,255,.12)}}
.main{{max-width:1320px;margin:0 auto;padding:26px 20px}}
.mod-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-top:10px}}
.mod-card{{background:#fff;border:1px solid #e2e8f0;border-radius:6px;padding:22px 20px 18px;cursor:pointer;transition:transform .18s,box-shadow .18s;position:relative;overflow:hidden}}
.mod-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:var(--c,#2563eb)}}
.mod-card:hover{{transform:translateY(-3px);box-shadow:0 10px 25px rgba(37,99,235,.15)}}
.mod-card h3{{font-size:1.05rem;font-weight:700;margin:10px 0 6px;color:#1b365d}}
.mod-card p{{font-size:.83rem;color:#64748b;margin-bottom:12px}}
.mod-badge{{display:inline-block;background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe;border-radius:4px;font-size:.72rem;font-weight:700;padding:3px 9px}}
.back-btn{{display:inline-flex;align-items:center;gap:6px;background:#fff;border:1px solid #d1d5db;border-radius:5px;padding:7px 15px;font-size:.84rem;font-weight:600;color:#374151;cursor:pointer;margin-bottom:18px}}
.back-btn:hover{{background:#f3f4f6}}
.sec-title{{font-size:1.35rem;font-weight:700;color:#1b365d;margin-bottom:4px}}
.sec-desc{{font-size:.86rem;color:#64748b;margin-bottom:20px}}
.prob-list{{display:flex;flex-direction:column;gap:10px}}
.prob-item{{background:#fff;border:1px solid #e2e8f0;border-radius:6px;padding:15px 18px;cursor:pointer;display:flex;align-items:center;justify-content:space-between;transition:all .15s}}
.prob-item:hover{{border-color:#93c5fd;background:#f0f7ff;transform:translateX(2px)}}
.prob-item h4{{font-size:.92rem;font-weight:600;color:#1b365d;display:flex;align-items:center;gap:8px}}
.prob-item p{{font-size:.8rem;color:#64748b;margin-top:3px}}
.diff{{font-size:.72rem;font-weight:700;padding:2px 8px;border-radius:4px}}
.d-easy{{background:#dcfce7;color:#166534}}
.d-med{{background:#fef3c7;color:#92400e}}
.d-hard{{background:#fee2e2;color:#991b1b}}
.prob-header{{background:linear-gradient(135deg,#1b365d,var(--c,#2563eb));color:#fff;padding:24px 26px;border-radius:6px 6px 0 0}}
.prob-header h2{{font-size:1.25rem;font-weight:700}}
.prob-header p{{font-size:.86rem;opacity:.9;margin-top:6px}}
.prob-body{{background:#fff;border:1px solid #e2e8f0;border-top:none;border-radius:0 0 6px 6px;padding:24px}}
.step-card{{border:1px solid #e2e8f0;border-radius:6px;margin-bottom:14px;overflow:hidden;background:#fff}}
.step-hd{{background:#f8fafc;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;font-weight:700;color:#1b365d}}
.snum{{background:#2563eb;color:#fff;border-radius:50%;width:24px;height:24px;display:inline-flex;align-items:center;justify-content:center;font-size:.73rem;font-weight:800;font-family:monospace;margin-right:8px}}
.step-bd{{padding:18px;background:#fff}}
.ppt-formulation{{background:#f8fafc;border:1px solid #cbd5e1;border-left:4px solid #2563eb;border-radius:4px;padding:16px;margin:12px 0;font-family:'Consolas','Courier New',monospace;font-size:.85rem;line-height:1.8;color:#1e293b;white-space:pre-wrap}}
.ppt-formulation .lbl{{color:#2563eb;font-weight:700}}
.ppt-formulation .var{{color:#059669;font-weight:700}}
.ppt-explain{{background:#fffbeb;border:1px solid #fcd34d;border-radius:5px;padding:12px 16px;margin:12px 0;font-size:.85rem;color:#78350f;line-height:1.6}}
.ppt-explain strong{{color:#92400e}}
.table-wrap{{overflow-x:auto;margin:12px 0}}
table.ppt-table{{border-collapse:collapse;width:100%;font-size:.83rem;min-width:450px}}
table.ppt-table th,table.ppt-table td{{border:1px solid #cbd5e1;padding:8px 12px;text-align:center}}
table.ppt-table th{{background:#1b365d;color:#fff;font-weight:700}}
table.ppt-table tr:nth-child(even) td{{background:#f8fafc}}
table.ppt-table .opt{{background:#dcfce7;font-weight:700;color:#166534}}
.tp-table{{border-collapse:collapse;width:100%;font-size:.83rem;min-width:480px}}
.tp-table th,.tp-table td{{border:2px solid #94a3b8;padding:0;text-align:center;min-width:85px;position:relative}}
.tp-table th{{background:#1b365d;color:#fff;font-weight:700;padding:9px 10px}}
.tp-table .src-lbl{{background:#334155;color:#fff;font-weight:700;padding:9px 12px}}
.tp-table .dem-lbl{{background:#475569;color:#fff;font-weight:700;padding:8px 12px}}
.tp-cell{{position:relative;height:65px;min-width:85px;background:#fff}}
.cost-box{{position:absolute;top:2px;right:3px;font-size:.7rem;color:#475569;font-weight:700;border:1px solid #cbd5e1;padding:1px 5px;background:#f8fafc;border-radius:2px}}
.alloc-box{{position:absolute;bottom:5px;left:0;right:0;text-anchor:middle;font-size:1.05rem;font-weight:800;color:#1b365d}}
.cell-active{{background:#fef9c3 !important;border:3px solid #f59e0b !important}}
.cell-done{{background:#dbeafe !important}}
.cell-exhaust{{background:#f1f5f9;opacity:.7}}
.supply-val{{background:#f0fdf4;color:#166534;font-weight:700;padding:9px;border:2px solid #94a3b8}}
.demand-val{{background:#f0fdf4;color:#166534;font-weight:700;padding:8px;border:2px solid #94a3b8}}
.asgn-table{{border-collapse:collapse;font-size:.86rem;margin:12px auto;min-width:400px}}
.asgn-table th,.asgn-table td{{border:2px solid #94a3b8;padding:10px 16px;text-align:center;min-width:65px;font-weight:600;position:relative}}
.asgn-table th{{background:#1b365d;color:#fff}}
.asgn-table .row-lbl{{background:#334155;color:#fff;font-weight:700}}
.az-zero{{color:#2563eb;font-weight:800;background:#eff6ff}}
.az-assigned{{color:#fff;background:#16a34a !important;font-weight:800}}
.line-row{{border-top:3px solid #ef4444 !important;border-bottom:3px solid #ef4444 !important;background:#fee2e2}}
.line-col{{border-left:3px solid #ef4444 !important;border-right:3px solid #ef4444 !important;background:#fee2e2}}
table.sp-ppt-table{{border-collapse:collapse;width:100%;font-size:.82rem;margin:12px 0}}
table.sp-ppt-table th{{background:#1b365d;color:#fff;padding:8px 10px;text-align:center}}
table.sp-ppt-table td{{border:1px solid #cbd5e1;padding:8px 10px;text-align:center}}
table.sp-ppt-table tr:nth-child(even){{background:#f8fafc}}
table.sp-ppt-table .active-row{{background:#fef9c3;font-weight:700}}
.step-nav{{display:flex;align-items:center;gap:12px;margin:16px 0;flex-wrap:wrap}}
.snav-btn{{padding:8px 18px;border-radius:5px;border:1px solid #d1d5db;background:#fff;font-size:.84rem;font-weight:600;cursor:pointer;color:#374151}}
.snav-btn:hover:not(:disabled){{background:#f0f7ff;border-color:#93c5fd;color:#1d4ed8}}
.snav-btn:disabled{{opacity:.4;cursor:not-allowed}}
.snav-count{{font-size:.85rem;color:#64748b;font-weight:600;margin:0 4px}}
.res-box{{background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:14px 18px;margin-top:14px}}
.res-box h4{{font-size:.9rem;font-weight:700;color:#166534;margin-bottom:6px}}
.res-box ul{{font-size:.84rem;color:#166534;padding-left:18px}}
.res-box li{{margin-bottom:4px}}
.pill-row{{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}}
.sep{{height:1px;background:#e2e8f0;margin:16px 0}}
.ppt-badge{{display:inline-flex;align-items:center;gap:5px;background:#fff7ed;color:#c2410c;border:1px solid #ffedd5;border-radius:4px;font-size:.73rem;font-weight:700;padding:3px 9px;margin-bottom:8px}}
.book-badge{{display:inline-flex;align-items:center;gap:5px;background:#f0fdf4;color:#166534;border:1px solid #bbf7d0;border-radius:4px;font-size:.73rem;font-weight:700;padding:3px 9px;margin-bottom:8px}}
.tag{{display:inline-block;padding:3px 8px;border-radius:4px;font-size:.72rem;font-weight:700;background:#eff6ff;color:#1d4ed8;border:1px solid #bfdbfe}}
</style>
</head>
<body>
<div id="root"></div>
<script>
{data_and_modules}
{modules_def}
{vanilla_renderer}
</script>
</body>
</html>
"""

with open("app.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("make_vanilla_75_direct.py completed successfully!")
