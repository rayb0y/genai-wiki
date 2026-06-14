#!/usr/bin/env python3
"""Build wiki/catalog.md, a static page index that renders on GitHub.

Reads YAML frontmatter (title, type, updated) from every page under wiki/ and writes a
sorted markdown table. Stdlib only, so it runs in CI with no dependencies.
"""
import os, re, glob, datetime

WIKI = "wiki"
OUT = os.path.join(WIKI, "catalog.md")
EXCLUDE = {"catalog.md", "dashboard.md"}


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].strip("\n").split("\n"):
                m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
                if m:
                    fm[m.group(1)] = m.group(2).strip()
    return fm


def clean(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v.replace("|", r"\|")


rows = []
for p in sorted(glob.glob(os.path.join(WIKI, "**", "*.md"), recursive=True)):
    if os.path.basename(p) in EXCLUDE:
        continue
    fm = parse_frontmatter(p)
    title = clean(fm.get("title", os.path.basename(p)[:-3]))
    typ = clean(fm.get("type", "")) or "—"
    updated = clean(fm.get("updated", ""))
    rel = os.path.relpath(p, WIKI)  # link is relative to catalog.md (lives in wiki/)
    rows.append((updated, title, typ, rel))

rows.sort(key=lambda r: (r[0], r[1]), reverse=True)

lines = [
    "---",
    "title: Catalog",
    "type: dashboard",
    "updated: " + datetime.date.today().isoformat(),
    "tags: [meta, catalog]",
    "---",
    "",
    "# Catalog",
    "",
    "Auto-generated index of every page, rendered on GitHub (unlike [dashboard](dashboard.md), which",
    "needs the Obsidian Dataview plugin). Do not edit by hand; it is rebuilt by",
    "`scripts/build_catalog.py` and the `build-catalog` GitHub Action.",
    "",
    f"{len(rows)} pages.",
    "",
    "| Page | Type | Updated |",
    "| --- | --- | --- |",
]
for updated, title, typ, rel in rows:
    lines.append(f"| [{title}]({rel}) | {typ} | {updated} |")
lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print(f"wrote {OUT} with {len(rows)} rows")
