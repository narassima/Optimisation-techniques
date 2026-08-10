import re

print("Patching renderGeneral return bug and dynamic graph axis expansion...")

with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Fix renderGeneral missing return statement
old_render_gen = """function renderGeneral(p) {
  const graphHtml = p.graph ? drawLppGraph(p.graph) : '';
  const stepsHtml = (p.steps||[]).map((s,i) => {
    const id = `info-g-${i}`;
    const hidden = state.hiddenInfoMap[id];
    return `
      <div class="step-card">
        <div class="step-hd"><h3><span class="snum">${i+1}</span>${s.title}<button class="info-btn" onclick="toggleInfo('${id}')">i</button></h3></div>
        <div class="step-bd">
          ${s.explain?`<div id="${id}" class="ppt-explain" style="display:${hidden?'none':'block'};"><strong>ℹ️</strong> ${s.explain}</div>`:''}
          ${s.formulation?`<div class="ppt-formulation">${s.formulation}</div>`:''}
          ${s.body?`<div>${s.body}</div>`:''}
        </div>
      </div>`;
  }).join('') + graphHtml;
}"""

new_render_gen = """function renderGeneral(p) {
  const graphHtml = p.graph ? drawLppGraph(p.graph) : '';
  const stepsHtml = (p.steps||[]).map((s,i) => {
    const id = `info-g-${i}`;
    const hidden = state.hiddenInfoMap[id];
    return `
      <div class="step-card">
        <div class="step-hd"><h3><span class="snum">${i+1}</span>${s.title}<button class="info-btn" onclick="toggleInfo('${id}')">i</button></h3></div>
        <div class="step-bd">
          ${s.explain?`<div id="${id}" class="ppt-explain" style="display:${hidden?'none':'block'};"><strong>ℹ️</strong> ${s.explain}</div>`:''}
          ${s.formulation?`<div class="ppt-formulation">${s.formulation}</div>`:''}
          ${s.body?`<div>${s.body}</div>`:''}
        </div>
      </div>`;
  }).join('');
  return stepsHtml + graphHtml;
}"""

if old_render_gen in code:
    code = code.replace(old_render_gen, new_render_gen)
    print("Fixed renderGeneral return statement!")
else:
    # Use regex replace if whitespace differs
    pattern = r'function renderGeneral\(p\)\s*\{\s*const graphHtml = p\.graph \? drawLppGraph\(p\.graph\) : \'\';.*?\n\}'
    code = re.sub(pattern, new_render_gen, code, flags=re.DOTALL)
    print("Fixed renderGeneral return statement via regex!")

# 2. Upgrade drawLppGraph and solveBuilderLpp for Dynamic Axis Expansion
old_draw_lpp = r"""// ─── LPP SVG GRAPH RENDERER ──────────────────────────────────────────────────
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
}"""

new_draw_lpp = r"""// ─── LPP SVG GRAPH RENDERER (DYNAMIC EXPANDING AXES) ───────────────────────
function drawLppGraph(g, customZ, activePoint) {
  if (!g) return '';
  const W = 480, H = 340, pad = 45;
  
  // Calculate dynamic axis bounds so graph automatically expands when values/sliders change!
  let maxValX1 = g.maxX1 || 10;
  let maxValX2 = g.maxX2 || 10;
  
  // Expand bounds based on constraint intercepts
  (g.constraints || []).forEach(c => {
    if (c.a1 > 0) { const x1Int = c.b / c.a1; if (x1Int > 0 && x1Int < 1000) maxValX1 = Math.max(maxValX1, x1Int * 1.15); }
    if (c.a2 > 0) { const x2Int = c.b / c.a2; if (x2Int > 0 && x2Int < 1000) maxValX2 = Math.max(maxValX2, x2Int * 1.15); }
  });
  
  // Expand bounds based on custom Z slider
  const optCorner = g.corners ? g.corners.find(c => c.isOpt) || g.corners[0] : null;
  const zVal = customZ !== undefined ? customZ : (optCorner ? optCorner.z : 0);
  if (g.c1 > 0) maxValX1 = Math.max(maxValX1, (zVal / g.c1) * 1.1);
  if (g.c2 > 0) maxValX2 = Math.max(maxValX2, (zVal / g.c2) * 1.1);
  
  // Round up bounds for clean ticks
  const maxX1 = Math.ceil(maxValX1 / 5) * 5 || 10;
  const maxX2 = Math.ceil(maxValX2 / 5) * 5 || 10;
  
  const toX = x => pad + (x / maxX1) * (W - pad - 25);
  const toY = y => (H - pad) - (y / maxX2) * (H - pad - 25);
  
  // 1. Grid & Axes
  let gridSvg = '';
  const xStep = maxX1 / 5, yStep = maxX2 / 5;
  for (let i = 0; i <= 5; i++) {
    const valX = (i * xStep).toFixed(1).replace(/\.0$/, '');
    const valY = (i * yStep).toFixed(1).replace(/\.0$/, '');
    const px = toX(i * xStep), py = toY(i * yStep);
    
    gridSvg += `<line x1="${px}" y1="${pad-10}" x2="${px}" y2="${H-pad}" stroke="#e2e8f0" stroke-dasharray="2,2"/>`;
    gridSvg += `<text x="${px}" y="${H-pad+15}" text-anchor="middle" font-size="10" fill="#64748b" font-weight="600">${valX}</text>`;
    
    gridSvg += `<line x1="${pad}" y1="${py}" x2="${W-15}" y2="${py}" stroke="#e2e8f0" stroke-dasharray="2,2"/>`;
    gridSvg += `<text x="${pad-8}" y="${py+3}" text-anchor="end" font-size="10" fill="#64748b" font-weight="600">${valY}</text>`;
  }
  
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
    polygonSvg = `<polygon points="${pointsStr}" fill="rgba(34, 197, 94, 0.25)" stroke="#16a34a" stroke-width="2.2" stroke-dasharray="4,2"/>`;
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
    const color = c.color || ['#ef4444','#3b82f6','#10b981','#8b5cf6','#f59e0b'][idx % 5];
    linesSvg += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${color}" stroke-width="2.2"/>`;
  });

  // 4. Objective Isoprofit Line
  let isoSvg = '';
  if (g.c1 !== undefined && g.c2 !== undefined && g.c2 !== 0) {
    const yAt0 = zVal / g.c2;
    const yAtMaxX = (zVal - g.c1 * maxX1) / g.c2;
    const ix1 = toX(0), iy1 = toY(yAt0);
    const ix2 = toX(maxX1), iy2 = toY(yAtMaxX);
    isoSvg += `<line x1="${ix1}" y1="${iy1}" x2="${ix2}" y2="${iy2}" stroke="#eab308" stroke-width="3.5" stroke-dasharray="6,4"/>`;
  }

  // 5. Corner Points
  let cornersSvg = '';
  (g.corners || []).forEach(c => {
    const cx = toX(c.x1), cy = toY(c.x2);
    const r = c.isOpt ? 7.5 : 5.5;
    const fill = c.isOpt ? '#16a34a' : '#2563eb';
    const stroke = c.isOpt ? '#fff' : '#1d4ed8';
    
    cornersSvg += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="2"/>`;
    const labelZ = c.z !== undefined ? ` (Z=${c.z.toFixed(1).replace(/\.0$/, '')})` : '';
    cornersSvg += `<text x="${cx+8}" y="${cy-6}" font-size="11" font-weight="800" fill="${c.isOpt?'#15803d':'#1e293b'}">${c.label}${labelZ}</text>`;
  });

  return `
    <div class="lpp-graph-container" style="background:#fff;border:1px solid #cbd5e1;border-radius:8px;padding:14px;margin:14px 0;">
      <div style="font-size:.88rem;font-weight:700;color:#1b365d;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
        📈 Parallel Graphical Solution View (Auto-Scaling Axes: 0 to ${maxX1} x₁)
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
        <span style="display:inline-flex;align-items:center;gap:4px;"><span style="width:16px;height:3px;background:#eab308;display:inline-block;"></span> Objective Line Z (${zVal.toFixed(1)})</span>
      </div>
    </div>
  `;
}"""

if old_draw_lpp in code:
    code = code.replace(old_draw_lpp, new_draw_lpp)
    print("Replaced drawLppGraph with dynamic axis auto-scaling version!")
else:
    # Replace via pattern
    pattern = r'// ─── LPP SVG GRAPH RENDERER ───.*?return `\s*<div class="lpp-graph-container".*?</div>\s*`;\s*\}'
    code = re.sub(pattern, new_draw_lpp, code, flags=re.DOTALL)
    print("Replaced drawLppGraph via regex!")

with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Patch applied successfully!")
