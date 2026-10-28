#!/usr/bin/env python3
"""
build-sku-oe-vehicle.py — emit the SKU-OE-vehicle association dataset and its
rendered page from the canonical products.json.

Three-state data status (audit3 / P0-2):
  reference        — framework / common-application guidance; NOT a verified match
  source-verified  — the value is published by the source catalog (congbenfilter.com);
                     for the OE↔brand relationship this means the OE number's brand
                     attribution is a fact (e.g. 17220-5R0-008 → Honda)
  fitment-verified — only for a complete SKU-OE-vehicle-source-verification-date
                     record; NONE exist today, so this bucket is empty (0 rows)

The association only records REAL relationships present in products.json:
  - OE number(s)               → `source-verified` (published by source)
  - OE ↔ brand (fitment.brand) → `source-verified` where the source states a brand;
                                  `reference` where the source gives an OE number but
                                  no brand (we do NOT invent a brand)
  - vehicle model / year        → always `reference` (never a precise fitment claim)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTS_PATH = os.path.join(ROOT, "data", "products.json")
OUT_JSON = os.path.join(ROOT, "data", "sku-oe-vehicle.json")
DOCS = os.path.join(ROOT, "docs")
OUT_MD = os.path.join(DOCS, "reference", "sku-oe-vehicle.md")

with open(PRODUCTS_PATH, "r", encoding="utf-8") as f:
    DS = json.load(f)

META = DS.get("_meta", {})
CATS = {c["slug"]: c for c in DS["categories"]}
PRODUCTS = DS["products"]

entries = []
for p in PRODUCTS:
    src = p.get("source") or {}
    if "congben" not in (src.get("name") or ""):
        continue
    oe = p.get("oeNumbers") or []
    if not oe:
        continue
    fit = p.get("fitment") or {}
    brand = fit.get("brand") if isinstance(fit, dict) else None
    models = (fit.get("models") or []) if isinstance(fit, dict) else []
    entries.append({
        "model": p["model"],
        "slug": p["slug"],
        "category": p["category"],
        "category_name": CATS.get(p["category"], {}).get("name", p["category"]),
        "oe_numbers": oe,
        "cross_reference": p.get("crossReference"),
        "brand": brand,
        # OE↔brand: source-verified when the source catalog states the brand; otherwise reference.
        "oe_brand_status": "source-verified" if brand else "reference",
        "vehicle_models": models,
        "vehicle_status": "reference",
        "source": src.get("name"),
        "source_url": src.get("url"),
        "source_retrieved": src.get("retrieved"),
    })

# stable order: category then model
entries.sort(key=lambda e: (e["category"], e["model"]))

n_oe = len(entries)
n_brand = sum(1 for e in entries if e["oe_brand_status"] == "source-verified")
n_brand_ref = n_oe - n_brand

out = {
    "_meta": {
        "title": "SKU–OE–Vehicle Association",
        "version": "0.1.0",
        "generated": "2026-10-28",
        "brand": META.get("brand", "huiying"),
        "nature": "source-verified OE↔brand + reference vehicle application",
        "purpose": (
            "Associates each congben-sourced SKU to the OE number(s) published by the "
            "source catalog. The OE number's brand attribution is a fact (source-verified); "
            "specific vehicle model/year fitment remains reference-level and is never "
            "asserted as a precise fitment."
        ),
        "disclaimer": (
            "OE numbers and their brand attribution are drawn from the source catalog "
            "(congbenfilter.com). Vehicle model/year application is reference-only — always "
            "confirm against the buyer's OE / cross-reference table before ordering."
        ),
        "status_schema": {
            "reference": "framework / common-application guidance; not a verified match",
            "source-verified": "value published by the source catalog; OE↔brand is a fact",
            "fitment-verified": "complete SKU-OE-vehicle-source-verification-date record",
        },
        "counts": {
            "oe_skus": n_oe,
            "source_verified_oe_brand": n_brand,
            "oe_without_stated_brand": n_brand_ref,
            "fitment_verified": 0,
        },
    },
    "entries": entries,
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")

# ---------------------------------------------------------------------------
# Rendered page
# ---------------------------------------------------------------------------

def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")

lines = []
lines.append("# SKU–OE–Vehicle Association\n")
lines.append(
    "Every **congben-sourced SKU** with an OE number, mapped to the OE number(s) "
    "published by the source catalog. The **OE↔brand** relationship is `source-verified` "
    "where the source states a brand (the OE number's brand attribution is a fact); "
    "specific **vehicle model/year** application is `reference`-only.\n"
)
lines.append(
    "> **Auto-generated** by `scripts/build-sku-oe-vehicle.py` from `data/products.json` "
    f"v{META.get('version','0.1.0')} ({META.get('generated','')}). "
    "Do not edit values by hand — edit the dataset, then rebuild.\n"
)
lines.append(
    f"\n**{n_oe} OE-bearing SKUs · {n_brand} with source-verified OE↔brand · "
    f"{n_brand_ref} OE-only (brand not stated) · {0} fitment-verified.**\n"
)
lines.append("| SKU | Category | OE number(s) | Brand | OE↔brand status | Vehicle (reference) |\n")
lines.append("|---|---|---|---|---|---|")
for e in entries:
    brand = esc(e["brand"]) if e["brand"] else "`—`"
    oe = " · ".join(f"`{o}`" for o in e["oe_numbers"])
    models = esc(", ".join(e["vehicle_models"])) if e["vehicle_models"] else "`—`"
    lines.append(
        f"| `{e['model']}` | {esc(e['category_name'])} | {oe} | {brand} | "
        f"`{e['oe_brand_status']}` | {models} |"
    )
lines.append("")
lines.append("## Status labels\n")
for k, v in out["_meta"]["status_schema"].items():
    lines.append(f"- **`{k}`** — {v}")
lines.append("")
lines.append(f"> ⚠️ **reference / source-verified, not exact-fitment** — {out['_meta']['disclaimer']}\n")

os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"wrote {os.path.relpath(OUT_JSON, ROOT)} ({n_oe} SKUs)")
print(f"wrote {os.path.relpath(OUT_MD, ROOT)}")
print(f"  source-verified OE↔brand: {n_brand}")
print(f"  OE-only (brand not stated): {n_brand_ref}")
print(f"  fitment-verified: 0")
