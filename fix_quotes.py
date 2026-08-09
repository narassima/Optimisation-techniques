import re
import os

with open("build_full_75_clean.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix unescaped single quotes in string properties
# e.g., 'Vogel's' -> "Vogel's" or 'Vogel\'s'
fixed_text = text.replace("Vogel's", "Vogel\\'s").replace("Klyne's", "Klyne\\'s").replace("don't", "don\\'t").replace("it's", "it\\'s")

with open("build_full_75_clean.py", "w", encoding="utf-8") as f:
    f.write(fixed_text)

print("Fixed quotes in build_full_75_clean.py")
