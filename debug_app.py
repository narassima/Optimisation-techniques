import re

with open("app.html", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Total lines: {len(text.splitlines())}")
print(f"Total size: {len(text)} bytes")

# Extract the script inside <script type="text/babel">
match = re.search(r'<script type="text/babel">(.*?)</script>', text, re.DOTALL)
if not match:
    print("NOT FOUND <script type=\"text/babel\"> tag NOT found or not closed!")
else:
    code = match.group(1)
    print("OK Babel script tag found. Script length:", len(code), "bytes")
    
    # Check for basic JS syntax markers
    print("MODULES defined:", "const MODULES=" in code)
    print("ReactDOM.render present:", "ReactDOM.render" in code)
