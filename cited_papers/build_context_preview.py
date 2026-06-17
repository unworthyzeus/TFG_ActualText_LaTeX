import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
contexts = json.loads((ROOT / "citation_contexts_full.json").read_text(encoding="utf-8"))
audit = json.loads((ROOT / "citation_audit_rows.json").read_text(encoding="utf-8"))
titles = {row["_key"]: row["Name of citation"] for row in audit}

lines = []
for row in contexts:
    lines.append(f"## {row['number']} {row['key']} | {titles.get(row['key'], '')}")
    for ctx in row["contexts"][:4]:
        paragraph = ctx["paragraph"].replace("\n", " ")
        lines.append(f"[{ctx['file']} / {ctx['section']}] {paragraph[:1200]}")
    lines.append("")

out = ROOT / "citation_contexts_preview.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(out)
