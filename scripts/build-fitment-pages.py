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
  - docs/fitment/{type}.md               x3 vehicle-fitment reference tables

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
    text += "Full index of every SKU in the canonical dataset. Identification fields "
    "are `verified` (from `data/products.json`); all specification fields (dimensions, "
    "material, efficiency, OE, packing) are `NEEDS_VERIFICATION`.\n\n"
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
    text += "Identification fields are `verified`; specification fields are `NEEDS_VERIFICATION`. "
    "See [Data status labels](../specification/data-status.md) for the label definitions.\n"
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
    text += "Reference-level vehicle-fitment framework for the three core filter types. "
    "These are **common-application references**, not precise OE cross-references.\n\n"
    text += autogen_note(
        f"Fitment framework `data/fitment.json` v{FIT_META.get('version','0.1.0')} "
        f"({FIT_META.get('generated','')}) — `{FIT_META.get('nature','reference-only')}`."
    )
    text += f"\n**{len(brands)} brands · {len(VEHICLES)} vehicle models · "
    f"{total_rows} fitment rows ({len(FILTERS)} filter types).**\n\n"
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
                label,
                typical,
                path,
            ]) + " |"
        )
    table = "\n".join([
        "| Vehicle model | Brand (region) | Era (reference) | Filter type | Typical size range (reference) | Matching path |",
        "|---|---|---|---|---|---|",
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
    text += f"**Matching path:** {path}\n\n"
    text += f"**{len(VEHICLES)} vehicle references:**\n\n"
    text += table + "\n"
    write(f"fitment/{flt['type']}.md", text)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

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
    print("\nDone.")


if __name__ == "__main__":
    main()
