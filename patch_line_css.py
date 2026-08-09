import json
import os

with open("build_clean_75_direct_perfect.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace CSS line definitions in final_html template
old_lines_css = ".line-row{border-top:3px solid #ef4444 !important;border-bottom:3px solid #ef4444 !important;background:#fee2e2}\n.line-col{border-left:3px solid #ef4444 !important;border-right:3px solid #ef4444 !important;background:#fee2e2}"

new_lines_css = """.line-row{position:relative;background:#fee2e2 !important;font-weight:700}
.line-row::after{content:'';position:absolute;top:50%;left:0;right:0;height:4px;background:#dc2626;z-index:10;transform:translateY(-50%)}
.line-col{position:relative;background:#fee2e2 !important;font-weight:700}
.line-col::after{content:'';position:absolute;top:0;bottom:0;left:50%;width:4px;background:#dc2626;z-index:10;transform:translateX(-50%)}
.az-intersection{position:relative;background:#fca5a5 !important;font-weight:800}
.az-intersection::before{content:'';position:absolute;top:50%;left:0;right:0;height:4px;background:#dc2626;z-index:10;transform:translateY(-50%)}
.az-intersection::after{content:'';position:absolute;top:0;bottom:0;left:50%;width:4px;background:#dc2626;z-index:10;transform:translateX(-50%)}"""

fixed_text = text.replace(old_lines_css, new_lines_css)

with open("build_clean_75_direct_perfect.py", "w", encoding="utf-8") as f:
    f.write(fixed_text)

print("Updated line CSS in build_clean_75_direct_perfect.py.")
