import json
import os

# Complete script to build zero-dependency app.html

with open("build_entire_75_hub.py", "r", encoding="utf-8") as f:
    full_js = f.read()

# Extract LPP, Transport, Assignment, Shortest, MST JS definitions
# We will convert the React components to clean Vanilla JS DOM renderers!

vanilla_renderer_js = """
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
      <div className="header-inner" style="max-width:1320px;margin:0 auto;padding:18px 24px 12px;display:flex;align-items:center;justify-content:space-between;">
        <div style="display:flex;align-items:center;gap:14px;">
          <div style="font-size:2.2rem;">📐</div>
          <div>
            <h1 style="font-size:1.45rem;font-weight:700;">OR Learning Hub – OTDM</h1>
            <p style="font-size:.83rem;opacity:.88;margin-top:2px;">PGDM 2024-2026 · Great Lakes Institute of Management</p>
          </div>
        </div>
      </div>
      <div className="nav-strip">
        <div className="nav-strip-inner">
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

print("Vanilla renderer ready.")
