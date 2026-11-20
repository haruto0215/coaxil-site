"""/tools/ のページを型（tools_page.tpl.html）から作る。業種の10本のデータ（var PACKS の1行）は今のページから引き継ぐ。
使い方：python3 scripts/build_tools_page.py
業種のデータを新しくする時は、そのあとで tools_page_data.py を流す（var PACKS の1行だけを書き直す）。
"""
import os, re, sys
d = os.path.dirname(os.path.abspath(__file__))
page = os.path.join(d, "..", "docs", "tools", "index.html")
tpl = open(os.path.join(d, "tools_page.tpl.html"), encoding="utf-8").read()
cur = open(page, encoding="utf-8").read()
m = re.search(r"^  var PACKS = .*;$", cur, re.M)
if not m:
    sys.exit("今のページに var PACKS の行が無い")
out = tpl.replace("__PACKS_LINE__", m.group(0))
assert "__PACKS_LINE__" not in out
open(page, "w", encoding="utf-8").write(out)
print("built", len(out))
