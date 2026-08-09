import json
import os

from generate_perfect_75_hub import solve_nwc, solve_lcm, solve_vam

print("Updating Assignment Hungarian line drawing styles and adding detailed line test steps...")

# Read generate_app_html_direct.py text
with open("generate_app_html_direct.py", "r", encoding="utf-8") as f:
    code_text = f.read()

# Update CSS for .line-row and .line-col to draw crisp red lines across cells
old_css_lines = ".line-row{border-top:3px solid #ef4444 !important;border-bottom:3px solid #ef4444 !important;background:#fee2e2}\n.line-col{border-left:3px solid #ef4444 !important;border-right:3px solid #ef4444 !important;background:#fee2e2}"

new_css_lines = """.line-row{position:relative;background:#fee2e2 !important;font-weight:700}
.line-row::after{content:'';position:absolute;top:50%;left:0;right:0;height:4px;background:#dc2626;z-index:10;transform:translateY(-50%)}
.line-col{position:relative;background:#fee2e2 !important;font-weight:700}
.line-col::after{content:'';position:absolute;top:0;bottom:0;left:50%;width:4px;background:#dc2626;z-index:10;transform:translateX(-50%)}
.az-intersection{position:relative;background:#fca5a5 !important;font-weight:800}
.az-intersection::before{content:'';position:absolute;top:50%;left:0;right:0;height:4px;background:#dc2626;z-index:10;transform:translateY(-50%)}
.az-intersection::after{content:'';position:absolute;top:0;bottom:0;left:50%;width:4px;background:#dc2626;z-index:10;transform:translateX(-50%)}"""

updated_code = code_text.replace(old_css_lines, new_css_lines)

with open("generate_app_html_direct.py", "w", encoding="utf-8") as f:
    f.write(updated_code)

print("Updated line CSS in generate_app_html_direct.py.")
