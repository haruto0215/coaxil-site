"""/tools/ のページに、業種ごとの10本（tools-app の業種の型）を埋め込む。
使い方：cd ~/dev/ai-support/tools-app && node scripts/packs-json.mjs > /tmp/packs.json
        python3 ~/dev/coaxil-site/scripts/tools_page_data.py /tmp/packs.json
ページの中の `var PACKS = [...];` の1行だけを書き直す。
"""
import json, re, sys, os
src = sys.argv[1]
page = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "tools", "index.html")
packs = json.load(open(src, encoding="utf-8"))
kind = lambda t: "PDF" if "PDF" in t["output"] and "Excel" not in t["output"] else ("Excel" if "Excel" in t["output"] else ("表" if t["mode"] == "file" else "文章"))
data = [{"id": p["id"], "name": p["name"], "tools": [{"n": t["name"], "s": t["short"], "o": t["output"]} for t in p["tools"]]} for p in packs]
line = "  var PACKS = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";"
s = open(page, encoding="utf-8").read()
s2, n = re.subn(r"^  var PACKS = .*;$", lambda m: line, s, flags=re.M)
if n != 1:
    sys.exit("var PACKS の行が見つからない")
open(page, "w", encoding="utf-8").write(s2)
print(f"{len(data)}業種・{sum(len(p['tools']) for p in data)}本を入れました")
