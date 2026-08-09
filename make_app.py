import json
import re

# Read the HTML header template
with open("build_full_hub.py", "r", encoding="utf-8") as f:
    header_content = f.read().split('html_head = """')[1].split('"""')[0]

print("Building 75-problem PPT-aligned OR Learning Hub...")
