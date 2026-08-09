import re
import os

with open("app.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace Vogel's and Klyne's with escaped single quotes
fixed_text = text.replace("Vogel's", "Vogel\\'s").replace("Klyne's", "Klyne\\'s")

with open("app.html", "w", encoding="utf-8") as f:
    f.write(fixed_text)

print("Fixed app.html directly.")
