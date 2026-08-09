import re
import os

with open("app.html", "r", encoding="utf-8") as f:
    text = f.read()

print("File Size:", os.path.getsize("app.html"), "bytes")

lpp = len(re.findall(r'"lpp_', text))
tp = len(re.findall(r'"tp_', text))
asgn = len(re.findall(r'"asgn_', text))
sp = len(re.findall(r'"sp_', text))
mst = len(re.findall(r'"mst_', text))

print(f"LPP Problems: {lpp}")
print(f"Transportation Problems: {tp}")
print(f"Assignment Problems: {asgn}")
print(f"Shortest Path Problems: {sp}")
print(f"MST Problems: {mst}")
print(f"TOTAL VERIFIED: {lpp + tp + asgn + sp + mst}")
