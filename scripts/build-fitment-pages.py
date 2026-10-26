#!/usr/bin/env python3
"""
build-fitment-pages.py — huiying data sub-site page generator.

Reads two datasets and renders every data-derived MkDocs page under `docs/`:

  1. `data/products.json` — the canonical product dataset, kept byte-identical
     with the main site's `src/data/products.json` (authoritative copy).
  2. `data/fitment.json`  — the fitment REFERENCE framework (common-application
     vehicle matrix, explicitly reference-only; no verified OE numbers).

Generated pages (zero manual transcription of values):

  - docs/products/index.md               SKU full index
  - docs/products/{slug}.md              x5 category pages (incl. empty ones)
  - docs/products/{model}.md             x10 SKU parameter pages
  - docs/fitment/index.md                fitment reference index + stats
  - docs/fitment/{type}.md               x5 vehicle-fitment reference tables
  - docs/reference/oe-patterns.md        OE prefix-pattern reference framework
  - docs/reference/size-ranges.md        filter size reference ranges
  - docs/reference/replacement-intervals.md  replacement-interval reference
  - docs/reference/procurement.md        HS-code + MOQ/packing reference

Honesty discipline: the source product pages contain no per-SKU dimensions,
material, efficiency, OE or packing data. Every such field is rendered as
`NEEDS_VERIFICATION` — never invented. Only identification fields present in
`products.json` carry `verified` status.

Run from repo root:  python3 scripts/build-fitment-pages.py
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTS_PATH = os.path.join(ROOT, "data", "products.json")
FITMENT_PATH = os.path.join(ROOT, "data", "fitment.json")
OE_PATH = os.path.join(ROOT, "data", "oe-patterns.json")
SIZE_PATH = os.path.join(ROOT, "data", "size-ranges.json")
INTERVALS_PATH = os.path.join(ROOT, "data", "replacement-intervals.json")
PROCUREMENT_PATH = os.path.join(ROOT, "data", "procurement.json")
DOCS = os.path.join(ROOT, "docs")

SITE_URL = "https://data.huiying.com"
MAIN_URL = "https://huiyingfilter.com"

with open(PRODUCTS_PATH, "r", encoding="utf-8") as f:
    DS = json.load(f)
with open(FITMENT_PATH, "r", encoding="utf-8") as f:
    FIT = json.load(f)

META = DS.get("_meta", {})
CATS = DS["categories"]
PRODUCTS = DS["products"]
VERSION = META.get("version", "0.1.0")
GENERATED = META.get("generated", "")

FIT_META = FIT.get("_meta", {})
VEHICLES = FIT["vehicles"]
FILTERS = FIT["filters"]

with open(OE_PATH, "r", encoding="utf-8") as f:
    OE = json.load(f)
with open(SIZE_PATH, "r", encoding="utf-8") as f:
    SIZES = json.load(f)
with open(INTERVALS_PATH, "r", encoding="utf-8") as f:
    INTERVALS = json.load(f)
with open(PROCUREMENT_PATH, "r", encoding="utf-8") as f:
    PROC = json.load(f)

OE_META = OE.get("_meta", {})
SIZE_META = SIZES.get("_meta", {})
INTERVALS_META = INTERVALS.get("_meta", {})
PROC_META = PROC.get("_meta", {})

# Map category slug -> category object; category code -> slug
CAT_BY_SLUG = {c["slug"]: c for c in CATS}
CAT_BY_CODE = {c["code"]: c for c in CATS}


def write(path, text):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  wrote {path}")


def autogen_note(extra=""):
    s = (
        "> **Auto-generated** by `scripts/build-fitment-pages.py`. "
        f"Canonical dataset `data/products.json` v{VERSION} ({GENERATED}). "
        "Do not edit values by hand — edit the dataset, then rebuild."
    )
    if extra:
        s += " " + extra
    return s + "\n"


def cat_of(p):
    return CAT_BY_SLUG[p["category"]]


def cat_products(slug):
    return [p for p in PRODUCTS if p["category"] == slug]


# ---------------------------------------------------------------------------
# 1. SKU full index
# ---------------------------------------------------------------------------

def gen_index():
    rows = []
    for p in PRODUCTS:
        c = cat_of(p)
        link = f"[`{p['model']}`]({p['model']}.md)"
        rows.append(
            "| " + " | ".join([
                link,
                f"{c['name']} (`{c['code']}`)",
                p["name"],
                f"`{p['sourceId']}`",
                "`NEEDS_VERIFICATION`",
            ]) + " |"
        )
    table = "\n".join([
        "| Model | Category | Name | Source ID | Spec status |",
        "|---|---|---|---|---|",
    ] + rows)
    text = "# SKU Index\n\n"
    text += (
        "Full index of every SKU in the canonical dataset. Identification fields "
        "are `verified` (from `data/products.json`); all specification fields (dimensions, "
        "material, efficiency, OE, packing) are `NEEDS_VERIFICATION`.\n\n"
    )
    text += autogen_note()
    text += f"\n**{len(PRODUCTS)} SKUs across {len(CATS)} categories.**\n\n"
    text += f"> **Commercial catalog** — [View all products &amp; request a quote on huiyingfilter.com →]({MAIN_URL}/products/)\n\n"
    text += table + "\n"
    write("products/index.md", text)


# ---------------------------------------------------------------------------
# 2. Category pages
# ---------------------------------------------------------------------------

def gen_category(slug):
    c = CAT_BY_SLUG[slug]
    skus = cat_products(slug)
    if skus:
        rows = []
        for p in skus:
            link = f"[`{p['model']}`]({p['model']}.md)"
            rows.append(
                "| " + " | ".join([
                    link,
                    p["name"],
                    f"`{p['sourceId']}`",
                    "`NEEDS_VERIFICATION`",
                ]) + " |"
            )
        table = "\n".join([
            "| Model | Name | Source ID | Spec status |",
            "|---|---|---|---|",
        ] + rows)
        sku_block = f"## SKUs ({len(skus)})\n\n{table}\n\n"
    else:
        sku_block = (
            "## SKUs (0)\n\n"
            "> This category is declared in the canonical dataset but currently has "
            "**no SKUs** in `data/products.json`. Treat the category as placeholder "
            "until SKUs are added.\n\n"
        )

    text = f"# {c['name']}\n\n"
    text += f"Category code `{c['code']}` · slug `{c['slug']}` · "
    text += f"{len(skus)} SKU(s).\n\n"
    text += autogen_note()
    text += "\n" + c["desc"] + "\n\n"
    text += f"> **Commercial listing** — [View this category &amp; request a quote on huiyingfilter.com →]({MAIN_URL}/products/{c['slug']}/)\n\n"
    text += sku_block
    text += "## Data status\n\n"
    text += (
        "Identification fields are `verified`; specification fields are `NEEDS_VERIFICATION`. "
        "See [Data status labels](../specification/data-status.md) for the label definitions.\n"
    )
    write(f"products/{slug}.md", text)


# ---------------------------------------------------------------------------
# 3. SKU parameter pages
# ---------------------------------------------------------------------------

def gen_sku(p):
    c = cat_of(p)
    desc = p.get("desc", "").strip()

    ident = "\n".join([
        "| Field | Value | Status |",
        "|---|---|---|",
        f"| Model | `{p['model']}` | `verified` |",
        f"| Brand | {META.get('brand', 'huiying')} | `verified` |",
        f"| Category | {c['name']} (`{c['code']}`) | `verified` |",
        f"| Name | {p['name']} | `verified` |",
        f"| Slug | `{p['slug']}` | `verified` |",
        f"| Source ID | `{p['sourceId']}` | `verified` |",
    ])

    spec = "\n".join([
        "| Field | Value | Status |",
        "|---|---|---|",
        "| Dimensions (L×W×H / OD×ID×H) | `—` | `NEEDS_VERIFICATION` |",
        "| Filter media material | `—` | `NEEDS_VERIFICATION` |",
        "| Filtration efficiency | `—` | `NEEDS_VERIFICATION` |",
        "| OE number(s) | `—` | `NEEDS_VERIFICATION` |",
        "| Cross-reference (competitor) | `—` | `NEEDS_VERIFICATION` |",
        "| Packing / carton qty | `—` | `NEEDS_VERIFICATION` |",
        "| HS Code | `—` | `NEEDS_VERIFICATION` |",
    ])

    # Reference fitment link resolved to the fitment page for this category
    fit_type = {
        "air-filter": "air-filter",
        "oil-filter": "oil-filter",
        "cabin-filter": "cabin-filter",
    }.get(p["category"])

    fit_block = ""
    if fit_type:
        fit_block = (
            "\n## Reference fitment\n\n"
            "No precise OE fitment is asserted. This SKU belongs to the "
            f"[{c['name']} reference framework](../fitment/{fit_type}.md), which lists "
            "common-application vehicles only.\n\n"
            "| Field | Value | Status |\n"
            "|---|---|---|\n"
            f"| Reference fitment | [{c['name']} — common applications](../fitment/{fit_type}.md) | `reference` |\n"
        )

    text = f"# {p['name']}\n\n"
    text += f"`{p['model']}`\n\n"
    text += autogen_note()
    text += f"\n> Category: **{c['name']}** — [category page]({c['slug']}.md) · [SKU index](index.md)\n"
    text += f"> **Commercial listing** — [View product &amp; request quote on huiyingfilter.com →]({MAIN_URL}/products/{p['category']}/)\n\n"
    text += "## Description (source site)\n\n"
    text += (desc if desc else "`—`") + "\n\n"
    text += "## Identification\n\n" + ident + "\n"
    text += "## Parameters\n\n"
    text += "The source product pages do not publish per-SKU dimensions, material, "
    "efficiency, OE or packing data. Every specification below is therefore "
    "`NEEDS_VERIFICATION` — request the value from Huiying before quoting.\n\n"
    text += spec + "\n"
    text += fit_block
    write(f"products/{p['model']}.md", text)


# ---------------------------------------------------------------------------
# 4. Fitment reference pages
# ---------------------------------------------------------------------------

def gen_fitment_index():
    total_rows = len(VEHICLES) * len(FILTERS)
    brands = sorted({v["brand"] for v in VEHICLES})
    regions = sorted({v["region"] for v in VEHICLES})

    rows = []
    for flt in FILTERS:
        rows.append(
            f"| [{flt['label']}]({flt['type']}.md) | `{flt['type']}` | "
            f"{len(VEHICLES)} vehicles × 1 row = {len(VEHICLES)} rows | `{flt['data_status']}` |"
        )
    table = "\n".join([
        "| Page | Type | Matrix size | Data status |",
        "|---|---|---|---|",
    ] + rows)

    text = "# Fitment Reference Index\n\n"
    text += (
        "Reference-level vehicle-fitment framework for the five core filter types. "
        "These are **common-application references**, not precise OE cross-references.\n\n"
    )
    text += autogen_note(
        f"Fitment framework `data/fitment.json` v{FIT_META.get('version','0.1.0')} "
        f"({FIT_META.get('generated','')}) — `{FIT_META.get('nature','reference-only')}`."
    )
    text += (
        f"\n**{len(brands)} brands · {len(VEHICLES)} vehicle models · "
        f"{total_rows} fitment rows ({len(FILTERS)} filter types).**\n\n"
    )
    text += "| Attribute | Value |\n|---|---|\n"
    text += f"| Brands | {', '.join(brands)} |\n"
    text += f"| Regions | {', '.join(regions)} |\n"
    text += f"| Filter types | {', '.join(f['label'] for f in FILTERS)} |\n"
    text += f"| Matrix rows | {total_rows} |\n"
    text += f"| Data status | `reference` (all entries) |\n\n"
    text += table + "\n\n"
    text += f"> ⚠️ **{FIT_META.get('nature','reference-only')}** — {FIT_META.get('disclaimer','')}\n"
    write("fitment/index.md", text)


def gen_fitment(flt):
    label = flt["label"]
    typical = flt["typical_size_range"]
    path = flt["matching_path"]
    status = flt["data_status"]
    material = flt.get("material_suggestion", "`reference`")
    interval = flt.get("replacement_interval", "`reference`")

    rows = []
    for v in VEHICLES:
        name = f"{v['model']}"
        if v.get("zh"):
            name += f" · {v['zh']}"
        rows.append(
            "| " + " | ".join([
                name,
                f"{v['brand']} ({v['region']})",
                v["era"],
                typical,
                material,
                interval,
                "`reference`",
            ]) + " |"
        )
    table = "\n".join([
        "| Vehicle model | Brand (region) | Era (reference) | Typical size range (reference) | Material suggestion (reference) | Replacement interval (reference) | Status |",
        "|---|---|---|---|---|---|---|",
    ] + rows)

    text = f"# {label} — Fitment Reference\n\n"
    text += flt["intro"] + "\n\n"
    text += autogen_note(
        f"Fitment framework `data/fitment.json` v{FIT_META.get('version','0.1.0')} — "
        f"`{FIT_META.get('nature','reference-only')}`."
    )
    text += "\n"
    text += f"> ⚠️ **Data status: `{status}`.** {FIT_META.get('disclaimer','')}\n\n"
    text += f"**Filter type:** {label}\n\n"
    text += f"**Typical size range (reference):** {typical}\n\n"
    text += f"**Material suggestion (reference):** {material}\n\n"
    text += f"**Replacement interval (reference):** {interval}\n\n"
    text += f"**Matching path:** {path}\n\n"
    text += f"**{len(VEHICLES)} vehicle references:**\n\n"
    text += table + "\n"
    write(f"fitment/{flt['type']}.md", text)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 5. OE prefix-pattern reference
# ---------------------------------------------------------------------------

def gen_oe_patterns():
    text = "# OE Number Prefix-Pattern Reference\n\n"
    text += (
        "Directional OE-number prefix patterns for mainstream vehicle brands. "
        "Prefixes are **public common knowledge** and are shown at pattern level only — "
        "a prefix alone is never a valid part match.\n\n"
    )
    text += autogen_note(
        f"OE-pattern dataset `data/oe-patterns.json` v{OE_META.get('version','0.1.0')} — "
        f"`{OE_META.get('nature','prefix-pattern-reference')}`."
    )
    text += "\n"
    text += f"> ⚠️ **{OE_META.get('nature','prefix-pattern-reference')}** — {OE_META.get('disclaimer','')}\n\n"
    for flt in OE["filters"]:
        text += f"## {flt['label']}\n\n"
        rows = []
        for p in flt["patterns"]:
            rows.append(
                f"| {p['brand']} | `{p['prefix']}` | {p['note']} | "
                f"`{OE.get('status_label','prefix pattern reference')}` |"
            )
        text += "\n".join([
            "| Brand | Prefix pattern | Note | Status |",
            "|---|---|---|---|",
        ] + rows) + "\n\n"
    text += "## Cross-reference lookup path\n\n"
    for i, step in enumerate(OE["cross_reference_path"], 1):
        text += f"{i}. {step}\n"
    text += "\n## Coverage note\n\n"
    text += OE["coverage_note"] + "\n\n"
    write("reference/oe-patterns.md", text)


# ---------------------------------------------------------------------------
# 6. Size reference ranges
# ---------------------------------------------------------------------------

def gen_size_ranges():
    text = "# Filter Size Reference Ranges\n\n"
    text += (
        "Typical dimensional ranges by vehicle class, plus common oil-filter thread "
        "specifications. Public common-knowledge ranges for estimation only.\n\n"
    )
    text += autogen_note(
        f"Size dataset `data/size-ranges.json` v{SIZE_META.get('version','0.1.0')} — `reference-only`."
    )
    text += "\n"
    text += f"> ⚠️ **reference-only** — {SIZE_META.get('disclaimer','')}\n\n"
    text += "## Engine air filter — typical L×W×H by vehicle class\n\n"
    rows = []
    for c in SIZES["air_filter_by_class"]:
        rows.append(
            f"| {c['label']} (`{c['class']}`) · {c['zh']} | {c['length_mm']} | "
            f"{c['width_mm']} | {c['height_mm']} | {c['example_vehicles']} | `reference` |"
        )
    text += "\n".join([
        "| Vehicle class | Length (mm) | Width (mm) | Height (mm) | Example vehicles | Status |",
        "|---|---|---|---|---|---|",
    ] + rows) + "\n\n"
    text += "## Oil filter — typical thread specifications\n\n"
    rows = []
    for t in SIZES["oil_filter_threads"]:
        rows.append(f"| `{t['thread']}` | {t['typical']} | `{t['status']}` |")
    text += "\n".join([
        "| Thread | Typical applications | Status |",
        "|---|---|---|",
    ] + rows) + "\n\n"
    text += "## Other filter types (typical ranges)\n\n"
    text += f"- **Cabin filter:** {SIZES['cabin_filter_range']}\n"
    text += f"- **Fuel filter:** {SIZES['fuel_filter_range']}\n\n"
    text += "## Notes\n\n"
    for n in SIZES["notes"]:
        text += f"- {n}\n"
    text += "\n"
    write("reference/size-ranges.md", text)


# ---------------------------------------------------------------------------
# 7. Replacement-interval reference
# ---------------------------------------------------------------------------

def gen_replacement_intervals():
    text = "# Filter Replacement-Interval Reference\n\n"
    text += (
        "Industry-common replacement intervals for the five filter categories. "
        "Reference guidance only — always follow the vehicle/engine manufacturer's schedule first.\n\n"
    )
    text += autogen_note(
        f"Intervals dataset `data/replacement-intervals.json` v{INTERVALS_META.get('version','0.1.0')} — `reference-only`."
    )
    text += "\n"
    text += f"> ⚠️ **reference-only** — {INTERVALS_META.get('disclaimer','')}\n\n"
    text += "## Reference intervals by filter type\n\n"
    rows = []
    for i in INTERVALS["intervals"]:
        rows.append(
            f"| {i['label']} (`{i['type']}`) | {i['km']} | {i['months']} | {i['note']} | `{i['status']}` |"
        )
    text += "\n".join([
        "| Filter type | Kilometres (reference) | Months (reference) | Note | Status |",
        "|---|---|---|---|---|",
    ] + rows) + "\n\n"
    text += "## Factors affecting replacement interval\n\n"
    rows = []
    for f in INTERVALS["factors"]:
        rows.append(f"| {f['factor']} | {f['effect']} |")
    text += "\n".join([
        "| Factor | Effect |",
        "|---|---|",
    ] + rows) + "\n\n"
    text += "## Localised suggestions `小筑 ✍️`\n\n"
    for s in INTERVALS["suggestions"]:
        text += f"- **{s['region']}:** {s['text']} _(signed: {s['author']})_\n"
    text += "\n"
    write("reference/replacement-intervals.md", text)


# ---------------------------------------------------------------------------
# 8. Procurement reference
# ---------------------------------------------------------------------------

def gen_procurement():
    text = "# Procurement Reference\n\n"
    text += (
        "HS-code reference and MOQ / packing framework for huiying filters. "
        "Public common-knowledge HS codes for estimation; MOQ/packing described at framework level.\n\n"
    )
    text += autogen_note(
        f"Procurement dataset `data/procurement.json` v{PROC_META.get('version','0.1.0')} — `reference-only`."
    )
    text += "\n"
    text += f"> ⚠️ **reference-only** — {PROC_META.get('disclaimer','')}\n\n"
    text += "## HS-code reference\n\n"
    rows = []
    for h in PROC["hs_codes"]:
        rows.append(f"| `{h['code']}` | {h['label']} | {h['applies_to']} | `{h['status']}` |")
    text += "\n".join([
        "| HS Code | Description | Applies to | Status |",
        "|---|---|---|---|",
    ] + rows) + "\n\n"
    text += "## MOQ & packing framework\n\n"
    rows = []
    for m in PROC["moq_packing"]:
        rows.append(f"| {m['topic']} | {m['framework']} |")
    text += "\n".join([
        "| Topic | Framework |",
        "|---|---|",
    ] + rows) + "\n\n"
    text += f"**Export markets:** {PROC['export_markets']}\n\n"
    text += f"{PROC['contact']}\n"
    write("reference/procurement.md", text)


def main():
    print(f"Dataset: v{VERSION} ({GENERATED}) — {len(PRODUCTS)} SKUs, {len(CATS)} categories")
    print(f"Fitment: v{FIT_META.get('version','0.1.0')} — {len(VEHICLES)} vehicles, {len(FILTERS)} filter types\n")
    gen_index()
    for c in CATS:
        gen_category(c["slug"])
    for p in PRODUCTS:
        gen_sku(p)
    gen_fitment_index()
    for flt in FILTERS:
        gen_fitment(flt)
    gen_oe_patterns()
    gen_size_ranges()
    gen_replacement_intervals()
    gen_procurement()
    print("\nDone.")


if __name__ == "__main__":
    main()
