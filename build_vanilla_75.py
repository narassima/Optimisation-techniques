import json
import os

print("Building pure Vanilla JS 75-problem hub script...")

# Load template CSS
with open("make_vanilla_app.py", "r", encoding="utf-8") as f:
    css_text = f.read().split('css_code = """')[1].split('"""')[0]

print("CSS template loaded.")
