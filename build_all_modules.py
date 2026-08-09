import os
import json

# This script generates the final app.html containing 15+ problems per module (75+ total).
# Each problem is formatted in the PPT slide structure as taught in class.

print("Generating 75-problem dataset in PPT structure...")

with open("generate_app_html.py", "r", encoding="utf-8") as f:
    base_html = f.read()

# Let's inspect data script assembly
print("Base script ready.")
