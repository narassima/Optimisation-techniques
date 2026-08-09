import re

with open("app.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

script_start = 0
for i, l in enumerate(lines):
    if '<script type="text/babel">' in l:
        script_start = i + 1
        break

print(f"Script starts at line {script_start}")

parens = 0
for idx, line in enumerate(lines[script_start:], start=script_start+1):
    if '</script>' in line:
        break
    
    # Strip string literals and comments roughly
    clean_line = re.sub(r'//.*', '', line)
    clean_line = re.sub(r'`.*?`', '``', clean_line)
    clean_line = re.sub(r"'.*?'", "''", clean_line)
    
    for ch in clean_line:
        if ch == '(': parens += 1
        elif ch == ')': parens -= 1
    
    if parens < 0:
        print(f"Negative parens at line {idx}: {line.strip()}")
        break

print(f"Final parens count: {parens}")
