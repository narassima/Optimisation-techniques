import os
import sys

print("Assembling final app.html file...")

# Load generate_app_html base
with open("generate_app_html.py", "r", encoding="utf-8") as f:
    base = f.read().split('print("Loading data definitions...")')[0]

# Load master_builder LPP code
with open("master_builder.py", "r", encoding="utf-8") as f:
    lpp_code = f.read().split("# --- MODULE 1: LPP (15 PROBLEMS) ---")[1]

# Load compile_hub Transport code
with open("compile_hub.py", "r", encoding="utf-8") as f:
    tp_code = f.read().split("// --------------------------------------------------------------------")[1]

# Load build_entire_75_hub Assignment, Shortest Path, MST & App code
with open("build_entire_75_hub.py", "r", encoding="utf-8") as f:
    rest_code = f.read().split("Appending Shortest Path and MST modules to build_entire_75_hub.py...")[0]

print("Parts loaded. Assembling HTML...")
