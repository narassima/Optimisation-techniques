import json
import os

print("Building clean 75-problem Vanilla JS app.html...")

# Read data definitions from build_full_75_clean.py
with open("build_full_75_clean.py", "r", encoding="utf-8") as f:
    clean_js = f.read()

data_and_modules = clean_js.split("const MODULES=")[0]
modules_def = "const MODULES=" + clean_js.split("const MODULES=")[1].split("// ====================================================================")[0]

# Read Vanilla renderer from build_vanilla_75_complete.py
with open("build_vanilla_75_complete.py", "r", encoding="utf-8") as f:
    vanilla_renderer = f.read().split("const vanilla_renderer_js = \"\"\"")[1].split('"""')[0]

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

print("Full 75-problem Vanilla JS app.html compiled successfully!")
