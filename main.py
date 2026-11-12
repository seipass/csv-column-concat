from __future__ import annotations
def run(rows,columns,separator=" "):
 return [separator.join(r.get(c,"") for c in columns) for r in rows]
