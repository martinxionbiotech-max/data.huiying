#!/usr/bin/env python3
"""
gen-nav.py — regenerate the data.huiying mkdocs.yml `nav` from the canonical
datasets (products.json categories + products, fitment.json filters).

Preserves the static config (theme, plugins, extra, hooks) and only rewrites the
`nav` tree so new categories/SKUs flow into the sidebar automatically.

Run from repo root:  python3 scripts/gen-nav.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTS_PATH = os.path.join(ROOT, "data", "products.json")
FITMENT_PATH = os.path.join(ROOT, "data", "fitment.json")
MKDOCS_PATH = os.path.join(ROOT, "mkdocs.yml")

with open(PRODUCTS_PATH, "r", encoding="utf-8") as f:
    DS = json.load(f)
with open(FITMENT_PATH, "r", encoding="utf-8") as f:
    FIT = json.load(f)

CATS = DS["categories"]
PRODUCTS = DS["products"]
FILTERS = FIT["filters"]

# Category order from the dataset (categories array order)
cat_order = [c["slug"] for c in CATS]
cat_name = {c["slug"]: c["name"] for c in CATS}

def natural_key(s):
    import re
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s or "")]

# group products by category, sort by model
by_cat = {}
for p in PRODUCTS:
    by_cat.setdefault(p["category"], []).append(p)
for k in by_cat:
    by_cat[k].sort(key=lambda p: natural_key(p["model"]))

# --- build nav lines ---
lines = []
lines.append("nav:")
lines.append("  - Home: index.md")
lines.append("  - SKU Index: products/index.md")
lines.append("  - Categories:")
for slug in cat_order:
    lines.append(f"      - {cat_name[slug]}: products/{slug}.md")
lines.append("  - SKU Details:")
for slug in cat_order:
    if slug not in by_cat:
        continue
    lines.append(f"      - {cat_name[slug]}:")
    for p in by_cat[slug]:
        lines.append(f"          - {p['model']}: products/{p['model']}.md")
lines.append("  - Fitment Reference:")
lines.append("      - Fitment Index: fitment/index.md")
for f in FILTERS:
    lines.append(f"      - {f['label']}: fitment/{f['type']}.md")
# static reference/spec nav (unchanged)
lines.append("  - Filter Media: materials/media-comparison.md")
lines.append("  - Reference Data:")
lines.append("      - OE Prefix Patterns: reference/oe-patterns.md")
lines.append("      - Size Ranges: reference/size-ranges.md")
lines.append("      - Replacement Intervals: reference/replacement-intervals.md")
lines.append("      - Procurement: reference/procurement.md")
lines.append("  - Data Specification:")
lines.append("      - Field Schema: specification/field-schema.md")
lines.append("      - Data Status Labels: specification/data-status.md")
lines.append("      - Sources & Disclaimer: specification/sources.md")
lines.append("      - Changelog: specification/changelog.md")

nav_block = "\n".join(lines) + "\n"

# --- read existing mkdocs.yml, replace the nav section ---
with open(MKDOCS_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# The nav section runs from the "nav:" line to the "hooks:" line (or EOF).
# We rebuild everything from "nav:" onward with our generated nav + hooks.
import re
# find where "nav:" begins
idx = content.find("\nnav:")
if idx == -1:
    idx = content.find("nav:")
head = content[:idx].rstrip() + "\n\n"
# extract the hooks: block (everything from "hooks:" onward)
hooks_idx = content.find("hooks:")
hooks_block = content[hooks_idx:].rstrip() + "\n" if hooks_idx != -1 else ""

new_content = head + nav_block + "\n" + hooks_block
with open(MKDOCS_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"nav regenerated: {len(CATS)} categories, {len(PRODUCTS)} SKUs, {len(FILTERS)} fitment pages")
print("category SKU counts:", {c['slug']: len(by_cat.get(c['slug'], [])) for c in CATS})
