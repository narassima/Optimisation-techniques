import re

with open("app.html", "r", encoding="utf-8") as f:
    text = f.read()

script = text.split('<script type="text/babel">')[1].split('</script>')[0]

curlys_stack = []
brackets_stack = []
backtick_start = None

lines = script.split('\n')
for line_idx, line in enumerate(lines, start=160):
    i = 0
    n = len(line)
    in_squote = False
    in_dquote = False
    
    while i < n:
        ch = line[i]
        is_escaped = (i > 0 and line[i-1] == '\\')
        
        # Check single line comment
        if not backtick_start and not in_squote and not in_dquote and i + 1 < n and line[i:i+2] == '//':
            break
            
        if ch == '`' and not in_squote and not in_dquote and not is_escaped:
            if backtick_start is None:
                backtick_start = (line_idx, i)
            else:
                backtick_start = None
        elif ch == "'" and not backtick_start and not in_dquote and not is_escaped:
            in_squote = not in_squote
        elif ch == '"' and not backtick_start and not in_squote and not is_escaped:
            in_dquote = not in_dquote
            
        if not backtick_start and not in_squote and not in_dquote:
            if ch == '{': curlys_stack.append((line_idx, line.strip()))
            elif ch == '}':
                if curlys_stack: curlys_stack.pop()
                else: print(f"Extra closing curly '}}' at line {line_idx}: {line.strip()}")
            elif ch == '[': brackets_stack.append((line_idx, line.strip()))
            elif ch == ']':
                if brackets_stack: brackets_stack.pop()
                else: print(f"Extra closing bracket ']' at line {line_idx}: {line.strip()}")
        i += 1

print(f"Unclosed backticks: {backtick_start}")
print(f"Unclosed curlys '{{': count = {len(curlys_stack)}")
print(f"Unclosed brackets '[': count = {len(brackets_stack)}")
