import re

with open("app.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract script text
script_match = re.search(r'<script type="text/babel">(.*?)</script>', html, re.DOTALL)
if not script_match:
    print("ERROR: Could not find <script type=\"text/babel\">")
    exit(1)

js_code = script_match.group(1)

# Check brackets balance
parens = 0
curlys = 0
brackets = 0

for i, ch in enumerate(js_code):
    if ch == '(': parens += 1
    elif ch == ')': parens -= 1
    elif ch == '{': curlys += 1
    elif ch == '}': curlys -= 1
    elif ch == '[': brackets += 1
    elif ch == ']': brackets -= 1

print(f"Brackets check: parens={parens}, curlys={curlys}, brackets={brackets}")

if parens != 0 or curlys != 0 or brackets != 0:
    print("MISMATCH DETECTED IN BRACKETS!")
else:
    print("Brackets are perfectly balanced!")

# Check React 18 render
if "createRoot" in js_code:
    print("React 18 createRoot present")
else:
    print("Warning: using legacy ReactDOM.render instead of createRoot")
