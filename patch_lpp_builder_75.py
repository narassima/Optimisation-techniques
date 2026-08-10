import re

print("Patching build_clean_75_direct_perfect.py with drawLppGraph, renderLppBuilder, and renderLppTheory...")

with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    code = f.read()

# Add drawLppGraph, renderLppTheory, and renderLppBuilder into vanilla_renderer JS code
js_lpp_components = r"""
// ─── LPP SVG GRAPH RENDERER ──────────────────────────────────────────────────
function drawLppGraph(g, customZ, activePoint) {
  if (!g) return '';
  const W = 480, H = 340, pad = 45;
  const maxX1 = g.maxX1 || 10, maxX2 = g.maxX2 || 10;
  
  const toX = x => pad + (x / maxX1) * (W - pad - 20);
  const toY = y => (H - pad) - (y / maxX2) * (H - pad - 20);
  
  // 1. Grid & Axes
  let gridSvg = '';
  const xStep = maxX1 / 5, yStep = maxX2 / 5;
  for (let i = 0; i <= 5; i++) {
    const valX = (i * xStep).toFixed(1).replace(/\.0$/, '');
    const valY = (i * yStep).toFixed(1).replace(/\.0$/, '');
    const px = toX(i * xStep), py = toY(i * yStep);
    
    // Vertical grid line
    gridSvg += `<line x1="${px}" y1="${pad-10}" x2="${px}" y2="${H-pad}" stroke="#e2e8f0" stroke-dasharray="2,2"/>`;
    gridSvg += `<text x="${px}" y="${H-pad+15}" text-anchor="middle" font-size="10" fill="#64748b" font-weight="600">${valX}</text>`;
    
    // Horizontal grid line
    gridSvg += `<line x1="${pad}" y1="${py}" x2="${W-15}" y2="${py}" stroke="#e2e8f0" stroke-dasharray="2,2"/>`;
    gridSvg += `<text x="${pad-8}" y="${py+3}" text-anchor="end" font-size="10" fill="#64748b" font-weight="600">${valY}</text>`;
  }
  
  // Axes lines
  gridSvg += `<line x1="${pad}" y1="${pad-15}" x2="${pad}" y2="${H-pad+5}" stroke="#334155" stroke-width="2.5"/>`;
  gridSvg += `<line x1="${pad-5}" y1="${H-pad}" x2="${W-10}" y2="${H-pad}" stroke="#334155" stroke-width="2.5"/>`;
  gridSvg += `<text x="${W-12}" y="${H-pad-6}" text-anchor="end" font-size="11" font-weight="800" fill="#1b365d">x₁</text>`;
  gridSvg += `<text x="${pad+8}" y="${pad-5}" font-size="11" font-weight="800" fill="#1b365d">x₂</text>`;

  // 2. Feasible Polygon (Shaded area)
  let polygonSvg = '';
  if (g.corners && g.corners.length >= 3) {
    const cx = g.corners.reduce((sum, c) => sum + c.x1, 0) / g.corners.length;
    const cy = g.corners.reduce((sum, c) => sum + c.x2, 0) / g.corners.length;
    const sorted = [...g.corners].sort((a, b) => Math.atan2(a.x2 - cy, a.x1 - cx) - Math.atan2(b.x2 - cy, b.x1 - cx));
    const pointsStr = sorted.map(c => `${toX(c.x1)},${toY(c.x2)}`).join(' ');
    polygonSvg = `<polygon points="${pointsStr}" fill="rgba(34, 197, 94, 0.22)" stroke="#16a34a" stroke-width="2" stroke-dasharray="4,2"/>`;
  }

  // 3. Constraint Lines
  let linesSvg = '';
  (g.constraints || []).forEach((c, idx) => {
    let p1, p2;
    if (c.a2 === 0) {
      const xVal = c.b / c.a1;
      p1 = { x: toX(xVal), y: toY(0) };
      p2 = { x: toX(xVal), y: toY(maxX2) };
    } else if (c.a1 === 0) {
      const yVal = c.b / c.a2;
      p1 = { x: toX(0), y: toY(yVal) };
      p2 = { x: toX(maxX1), y: toY(yVal) };
    } else {
      const xInt = c.b / c.a1, yInt = c.b / c.a2;
      p1 = { x: toX(0), y: toY(yInt) };
      p2 = { x: toX(xInt), y: toY(0) };
    }
    const color = c.color || '#3b82f6';
    linesSvg += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${color}" stroke-width="2"/>`;
  });

  // 4. Objective Isoprofit Line
  let isoSvg = '';
  const optCorner = g.corners ? g.corners.find(c => c.isOpt) || g.corners[0] : null;
  const zVal = customZ !== undefined ? customZ : (optCorner ? optCorner.z : 0);
  if (g.c1 !== undefined && g.c2 !== undefined && g.c2 !== 0) {
    const yAt0 = zVal / g.c2;
    const yAtMaxX = (zVal - g.c1 * maxX1) / g.c2;
    const ix1 = toX(0), iy1 = toY(yAt0);
    const ix2 = toX(maxX1), iy2 = toY(yAtMaxX);
    isoSvg += `<line x1="${ix1}" y1="${iy1}" x2="${ix2}" y2="${iy2}" stroke="#eab308" stroke-width="3" stroke-dasharray="6,4"/>`;
  }

  // 5. Corner Points
  let cornersSvg = '';
  (g.corners || []).forEach(c => {
    const cx = toX(c.x1), cy = toY(c.x2);
    const r = c.isOpt ? 7 : 5;
    const fill = c.isOpt ? '#16a34a' : '#2563eb';
    const stroke = c.isOpt ? '#fff' : '#1d4ed8';
    
    cornersSvg += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="2"/>`;
    const labelZ = c.z !== undefined ? ` (Z=${c.z.toFixed(1).replace(/\.0$/, '')})` : '';
    cornersSvg += `<text x="${cx+8}" y="${cy-6}" font-size="11" font-weight="800" fill="${c.isOpt?'#15803d':'#1e293b'}">${c.label}${labelZ}</text>`;
  });

  return `
    <div class="lpp-graph-container" style="background:#fff;border:1px solid #cbd5e1;border-radius:8px;padding:14px;margin:14px 0;">
      <div style="font-size:.88rem;font-weight:700;color:#1b365d;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
        📈 Parallel Graphical Solution View
        <span style="font-size:.75rem;font-weight:600;color:#16a34a;background:#dcfce7;padding:2px 8px;border-radius:4px;margin-left:auto;">Feasible Region & Isoprofit Sweep Line</span>
      </div>
      <svg viewBox="0 0 ${W} ${H}" width="100%" style="max-width:${W}px;display:block;margin:0 auto;background:#f8fafc;border-radius:6px;border:1px solid #e2e8f0;">
        ${gridSvg}
        ${polygonSvg}
        ${linesSvg}
        ${isoSvg}
        ${cornersSvg}
      </svg>
      <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:10px;font-size:.76rem;color:#475569;justify-content:center;">
        <span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:12px;height:12px;background:rgba(34,197,94,0.3);border:1px solid #16a34a;display:inline-block;border-radius:2px;"></span> Feasible Region</span>
        <span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:10px;height:10px;background:#16a34a;border-radius:50%;display:inline-block;"></span> Optimal Corner Vertex</span>
        <span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#eab308;display:inline-block;"></span> Objective Line Z</span>
      </div>
    </div>
  `;
}

// ─── LPP THEORY SECTION ──────────────────────────────────────────────────────
function renderLppTheory() {
  return `
    <div class="lpp-theory-box" style="background:linear-gradient(135deg,#f0f9ff 0%,#e0f2fe 100%);border:1px solid #7dd3fc;border-radius:8px;padding:18px 22px;margin:16px 0;">
      <h3 style="font-size:1.05rem;font-weight:700;color:#0369a1;margin-bottom:8px;display:flex;align-items:center;gap:8px;">
        🎓 Fundamental Theorem of LPP: Why Solutions MUST Lie on Boundary or Corner Points
      </h3>
      <p style="font-size:.86rem;color:#334155;line-height:1.65;margin-bottom:14px;">
        Students often ask: <em>"Why can't an optimal solution lie strictly inside the interior of the feasible region?"</em> Here is the exact mathematical and visual breakdown:
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;">
        <div style="background:#fff;padding:14px;border-radius:6px;border:1px solid #bae6fd;">
          <h4 style="font-size:.88rem;font-weight:700;color:#0284c7;margin-bottom:4px;">1. The Gradient / Push Intuition</h4>
          <p style="font-size:.82rem;color:#475569;line-height:1.55;">
            Inside an interior point, there is 360° open room in all directions. Moving in the direction of the objective gradient vector <strong>∇Z = (c₁, c₂)</strong> strictly increases Z. Because you can always step further in direction ∇Z without leaving the feasible region, no interior point can ever maximize Z! You keep pushing until you hit a constraint boundary wall.
          </p>
        </div>
        <div style="background:#fff;padding:14px;border-radius:6px;border:1px solid #bae6fd;">
          <h4 style="font-size:.88rem;font-weight:700;color:#0284c7;margin-bottom:4px;">2. Boundary to Corner Sliding</h4>
          <p style="font-size:.82rem;color:#475569;line-height:1.55;">
            Once pushed to a boundary constraint line, you can still slide along that line towards higher Z until you hit a second constraint line. Where two constraint lines intersect is a <strong>Corner Point (Vertex)</strong>. Here, no further feasible movement increases Z, establishing the corner point as optimal!
          </p>
        </div>
        <div style="background:#fff;padding:14px;border-radius:6px;border:1px solid #bae6fd;">
          <h4 style="font-size:.88rem;font-weight:700;color:#0284c7;margin-bottom:4px;">3. Convex Combination Proof</h4>
          <p style="font-size:.82rem;color:#475569;line-height:1.55;">
            Any interior point <strong>x</strong> is a weighted average (convex combination) of the vertices <strong>vᵢ</strong>: x = Σ λᵢ vᵢ. The linear objective Z(x) = Σ λᵢ Z(vᵢ) is a weighted average of vertex values. Since a weighted average can never strictly exceed the maximum component, <strong>max Z(vᵢ) ≥ Z(x)</strong>.
          </p>
        </div>
      </div>
    </div>
  `;
}

// ─── INTERACTIVE LPP BUILDER & PLAYGROUND ─────────────────────────────────────
const builderState = {
  type: 'max', c1: 5, c2: 4,
  constraints: [
    { a1: 6, a2: 4, b: 24, dir: '<=' },
    { a1: 1, a2: 2, b: 6, dir: '<=' }
  ],
  customZ: null
};

function renderLppBuilder() {
  const g = solveBuilderLpp();
  return `
    <div style="background:#fff;border:1px solid #cbd5e1;border-radius:8px;padding:20px;margin:20px 0;">
      <h3 style="font-size:1.15rem;font-weight:700;color:#1b365d;margin-bottom:6px;display:flex;align-items:center;gap:8px;">
        🛠️ Interactive Linear Programming Builder & Sensitivity Playground
      </h3>
      <p style="font-size:.85rem;color:#64748b;margin-bottom:16px;">
        Build custom 2D LPP problems by modifying decision variable coefficients ($c_1, c_2$) and constraints. Watch the feasible region, corner point intersections, and isoprofit sweep line adjust live!
      </p>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;">
        <!-- Controls Column -->
        <div>
          <div style="background:#f8fafc;padding:14px;border-radius:6px;border:1px solid #e2e8f0;margin-bottom:14px;">
            <h4 style="font-size:.9rem;font-weight:700;color:#1e293b;margin-bottom:8px;">1. Objective Function</h4>
            <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px;">
              <select onchange="updateBuilder('type', this.value)" style="padding:6px;border-radius:4px;border:1px solid #cbd5e1;font-weight:700;background:#fff;">
                <option value="max" ${builderState.type==='max'?'selected':''}>Maximize Z</option>
                <option value="min" ${builderState.type==='min'?'selected':''}>Minimize Z</option>
              </select>
              <span>=</span>
              <input type="number" value="${builderState.c1}" onchange="updateBuilder('c1', parseFloat(this.value)|0)" style="width:65px;padding:6px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;font-weight:700;"/>
              <span>x₁ +</span>
              <input type="number" value="${builderState.c2}" onchange="updateBuilder('c2', parseFloat(this.value)|0)" style="width:65px;padding:6px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;font-weight:700;"/>
              <span>x₂</span>
            </div>
          </div>

          <div style="background:#f8fafc;padding:14px;border-radius:6px;border:1px solid #e2e8f0;margin-bottom:14px;">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;">
              <h4 style="font-size:.9rem;font-weight:700;color:#1e293b;">2. Constraints (Subject to:)</h4>
              <button onclick="addBuilderConstraint()" style="background:#2563eb;color:#fff;border:none;border-radius:4px;padding:4px 10px;font-size:.78rem;font-weight:700;cursor:pointer;">+ Add Constraint</button>
            </div>
            ${builderState.constraints.map((c, i) => `
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px;flex-wrap:wrap;">
                <input type="number" value="${c.a1}" onchange="updateBuilderConstraint(${i}, 'a1', parseFloat(this.value)|0)" style="width:55px;padding:5px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;"/>
                <span style="font-size:.8rem;">x₁ +</span>
                <input type="number" value="${c.a2}" onchange="updateBuilderConstraint(${i}, 'a2', parseFloat(this.value)|0)" style="width:55px;padding:5px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;"/>
                <span style="font-size:.8rem;">x₂</span>
                <select onchange="updateBuilderConstraint(${i}, 'dir', this.value)" style="padding:5px;border-radius:4px;border:1px solid #cbd5e1;font-weight:700;background:#fff;">
                  <option value="<=" ${c.dir==='<='?'selected':''}>≤</option>
                  <option value=">=" ${c.dir==='>='?'selected':''}>≥</option>
                </select>
                <input type="number" value="${c.b}" onchange="updateBuilderConstraint(${i}, 'b', parseFloat(this.value)|0)" style="width:60px;padding:5px;border-radius:4px;border:1px solid #cbd5e1;text-align:center;font-weight:700;"/>
                ${builderState.constraints.length > 1 ? `<button onclick="removeBuilderConstraint(${i})" style="background:#ef4444;color:#fff;border:none;border-radius:4px;padding:4px 8px;font-size:.75rem;cursor:pointer;margin-left:auto;">✕</button>` : ''}
              </div>`).join('')}
            <div style="font-size:.76rem;color:#64748b;margin-top:6px;">Non-negativity: x₁, x₂ ≥ 0 (implicit)</div>
          </div>

          <!-- Sensitivity Slider -->
          <div style="background:#fef9c3;padding:14px;border-radius:6px;border:1px solid #fde047;">
            <h4 style="font-size:.86rem;font-weight:700;color:#854d0e;margin-bottom:6px;">🎚️ Interactive Isoprofit Line Slider</h4>
            <p style="font-size:.78rem;color:#713f12;margin-bottom:8px;">Drag Z value to sweep objective line across feasible region:</p>
            <input type="range" min="0" max="${(g.optZ*1.4)||50}" step="1" value="${builderState.customZ!==null?builderState.customZ:(g.optZ||0)}" oninput="updateBuilderCustomZ(parseFloat(this.value))" style="width:100%;cursor:pointer;"/>
            <div style="display:flex;justify-content:space-between;font-size:.8rem;font-weight:700;color:#854d0e;margin-top:4px;">
              <span>Current Z: ${builderState.customZ!==null?builderState.customZ:(g.optZ||0)}</span>
              <span>Optimal Z: ${(g.optZ||0).toFixed(1)}</span>
            </div>
          </div>
        </div>

        <!-- Output Graph Column -->
        <div>
          ${drawLppGraph(g, builderState.customZ !== null ? builderState.customZ : undefined)}
          <div style="background:#f0fdf4;border:1px solid #86efac;border-radius:6px;padding:12px;margin-top:10px;">
            <h4 style="font-size:.86rem;font-weight:700;color:#166534;margin-bottom:4px;">✅ Builder Solution</h4>
            <div style="font-size:.83rem;color:#166534;">
              ${g.optCorner ? `Optimal Point: <strong>${g.optCorner.label} (${g.optCorner.x1.toFixed(2)}, ${g.optCorner.x2.toFixed(2)})</strong><br/>Optimal Z = <strong>${g.optZ.toFixed(2)}</strong>` : 'No feasible solution found with current constraints.'}
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}

function updateBuilder(key, val) { builderState[key] = val; builderState.customZ = null; renderApp(); }
function updateBuilderConstraint(i, key, val) { builderState.constraints[i][key] = val; builderState.customZ = null; renderApp(); }
function addBuilderConstraint() { builderState.constraints.push({ a1: 1, a2: 1, b: 10, dir: '<=' }); builderState.customZ = null; renderApp(); }
function removeBuilderConstraint(i) { builderState.constraints.splice(i, 1); builderState.customZ = null; renderApp(); }
function updateBuilderCustomZ(val) { builderState.customZ = val; renderApp(); }

function solveBuilderLpp() {
  const lines = builderState.constraints.map((c, idx) => ({
    a1: c.a1, a2: c.a2, b: c.b, dir: c.dir, label: `${c.a1}x₁ + ${c.a2}x₂ ${c.dir==='<='?'≤':'≥'} ${c.b}`,
    color: ['#ef4444','#3b82f6','#10b981','#8b5cf6','#f59e0b'][idx % 5]
  }));
  
  // Find all pairwise line intersections + axes
  const pts = [{ x1: 0, x2: 0 }];
  const allLines = [...lines, { a1: 1, a2: 0, b: 0, dir: '>=' }, { a1: 0, a2: 1, b: 0, dir: '>=' }];
  
  for (let i = 0; i < allLines.length; i++) {
    for (let j = i + 1; j < allLines.length; j++) {
      const l1 = allLines[i], l2 = allLines[j];
      const det = l1.a1 * l2.a2 - l1.a2 * l2.a1;
      if (Math.abs(det) > 1e-6) {
        const x1 = (l1.b * l2.a2 - l1.a2 * l2.b) / det;
        const x2 = (l1.a1 * l2.b - l1.b * l2.a1) / det;
        if (x1 >= -1e-4 && x2 >= -1e-4) {
          pts.push({ x1: Math.max(0, x1), x2: Math.max(0, x2) });
        }
      }
    }
  }
  
  // Filter feasible points
  const feasible = pts.filter(p => {
    return lines.every(c => {
      const val = c.a1 * p.x1 + c.a2 * p.x2;
      return c.dir === '<=' ? val <= c.b + 1e-4 : val >= c.b - 1e-4;
    });
  });
  
  // Unique corners
  const corners = [];
  const labels = ['O','A','B','C','D','E','F','G'];
  let maxX1 = 5, maxX2 = 5;
  
  feasible.forEach((p) => {
    if (!corners.some(c => Math.abs(c.x1 - p.x1) < 1e-3 && Math.abs(c.x2 - p.x2) < 1e-3)) {
      const z = builderState.c1 * p.x1 + builderState.c2 * p.x2;
      corners.push({ label: labels[corners.length % labels.length], x1: p.x1, x2: p.x2, z: z, isOpt: false });
      if (p.x1 > maxX1) maxX1 = p.x1;
      if (p.x2 > maxX2) maxX2 = p.x2;
    }
  });
  
  // Determine optimal corner
  let optZ = builderState.type === 'max' ? -Infinity : Infinity;
  let optCorner = null;
  corners.forEach(c => {
    if (builderState.type === 'max' ? c.z > optZ : c.z < optZ) {
      optZ = c.z; optCorner = c;
    }
  });
  if (optCorner) optCorner.isOpt = true;
  
  return {
    type: builderState.type, c1: builderState.c1, c2: builderState.c2,
    constraints: lines, corners: corners, optCorner: optCorner, optZ: optZ || 0,
    maxX1: Math.ceil(maxX1 * 1.3), maxX2: Math.ceil(maxX2 * 1.3)
  };
}
"""

# Insert JS components into vanilla_renderer before renderProblemList
render_list_pos = code.find("// PROBLEM LIST")
if render_list_pos != -1:
    code = code[:render_list_pos] + js_lpp_components + "\n\n" + code[render_list_pos:]
    print("Inserted LPP JS components into build script!")

# Now update renderProblemList for 'lpp' module to show Theory + Builder above list!
old_prob_list = "return `\n    <button class=\"back-btn\" onclick=\"gotoTab('home')\">← Back to Modules</button>"
new_prob_list = """if (mod.id === 'lpp') {
    return `
      <button class="back-btn" onclick="gotoTab('home')">← Back to Modules</button>
      <div class="sec-title">${mod.icon} ${mod.title}</div>
      <p class="sec-desc">${mod.desc}</p>
      ${renderLppTheory()}
      ${renderLppBuilder()}
      <div style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap;align-items:center;">
        ${['all','easy','medium','hard'].map(d => `
          <button onclick="filterDifficulty('${d}')" style="padding:5px 14px;border-radius:4px;border:1px solid;cursor:pointer;font-size:.8rem;font-weight:600;background:${state.difficultyFilter===d?mod.color:'#fff'};color:${state.difficultyFilter===d?'#fff':'#374151'};border-color:${state.difficultyFilter===d?mod.color:'#d1d5db'};">
            ${d.charAt(0).toUpperCase()+d.slice(1)}
          </button>`).join('')}
        <span style="margin-left:auto;font-size:.82rem;color:#64748b;">${filtered.length} problems</span>
      </div>
      <div class="prob-list">
        ${filtered.map(p => `
          <div class="prob-item" onclick="selectProblem('${p.id}')">
            <div>
              <h4>${p.title}</h4>
              <p>${p.context.slice(0,100)}…</p>
            </div>
            <div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
              <span class="diff ${p.difficulty==='easy'?'d-easy':p.difficulty==='hard'?'d-hard':'d-med'}">${p.difficulty}</span>
              <span style="color:#94a3b8;font-size:1.1rem;">›</span>
            </div>
          </div>`).join('')}
      </div>`;
  }
  return `
    <button class="back-btn" onclick="gotoTab('home')">← Back to Modules</button>"""

code = code.replace(old_prob_list, new_prob_list)

# Now update renderGeneral to include parallel graph if p.graph is present!
old_render_gen = "function renderGeneral(p) {\n  return (p.steps||[]).map((s,i) => {"
new_render_gen = "function renderGeneral(p) {\n  const graphHtml = p.graph ? drawLppGraph(p.graph) : '';\n  const stepsHtml = (p.steps||[]).map((s,i) => {"

code = code.replace(old_render_gen, new_render_gen)

# Append graphHtml at the end of renderGeneral return
old_gen_return = "}).join('');\n}"
new_gen_return = "}).join('') + graphHtml;\n}"

code = code.replace(old_gen_return, new_gen_return)

with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Build script patched with LPP Builder & Playground + Theory + Parallel Graphs!")
