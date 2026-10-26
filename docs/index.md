# Huiying Filter Data

Canonical product database for **huiying** — the structured, machine-readable layer that
backs the commercial site [huiyingfilter.com](https://huiyingfilter.com/).

This is a **data sub-site, not a marketing site**: it holds SKU records, a reference-level
vehicle-fitment framework and a filter-media comparison. Every value here is either drawn
from the canonical dataset or explicitly marked `NEEDS_VERIFICATION` / `reference`.

## What's here

| Section | What it contains | Data status |
|---|---|---|
| [SKU Index](products/index.md) | All 10 SKUs in the canonical dataset | `verified` (identity) + `NEEDS_VERIFICATION` (specs) |
| [Categories](products/air-filter.md) | 5 product categories (air / cabin / oil / fuel / wiper) | `verified` |
| [SKU Details](products/HY-AF-692.md) | Per-SKU parameter tables | `verified` (identity) + `NEEDS_VERIFICATION` (specs) |
| [Fitment Reference](fitment/index.md) | Vehicle-fitment framework for air / oil / cabin filters | `reference` |
| [Filter Media](materials/media-comparison.md) | Cellulose vs synthetic vs blended vs nano-fiber | `framework reference` + `editorial` |
| [Data Specification](specification/field-schema.md) | Field schema, status labels, sources & disclaimer | `verified` |

## Quick facts

- **10 SKUs** across **5 categories** (air filter: 8 · cabin filter: 1 · oil filter: 1 · fuel: 0 · wiper: 0).
- **13 vehicle models** across **10 brands** in the fitment reference framework (3 filter types × 13 vehicles = 39 rows).
- Canonical dataset version: `0.1.0` (generated 2026-10-26).

## Honest data posture

The source product catalogue does **not** publish per-SKU dimensions, filter media,
efficiency, OE numbers or packing data. Rather than invent those values, this site marks
them `NEEDS_VERIFICATION` and directs buyers to confirm them with Huiying before quoting.
The fitment framework is **reference-only** — no exact OE number is asserted.

Start with the [SKU Index](products/index.md), or go to the
[commercial catalog](https://huiyingfilter.com/products/) to request a quote.
