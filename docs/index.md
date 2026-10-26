# Huiying Filter Data

Canonical product database for **huiying** — the structured, machine-readable layer that
backs the commercial site [huiyingfilter.com](https://huiyingfilter.com/).

This is a **data sub-site, not a marketing site**: it holds SKU records, a reference-level
vehicle-fitment framework and filter reference data (media, OE prefix patterns, size
ranges, replacement intervals, procurement). Every value here is either drawn from the
canonical dataset or explicitly marked `NEEDS_VERIFICATION` / `reference`.

## What's here

| Section | What it contains | Data status |
|---|---|---|
| [SKU Index](products/index.md) | All 10 SKUs in the canonical dataset | `verified` (identity) + `NEEDS_VERIFICATION` (specs) |
| [Categories](products/air-filter.md) | 5 product categories (air / cabin / oil / fuel / wiper) | `verified` |
| [SKU Details](products/HY-AF-692.md) | Per-SKU parameter tables | `verified` (identity) + `NEEDS_VERIFICATION` (specs) |
| [Fitment Reference](fitment/index.md) | Vehicle-fitment framework for 5 filter types | `reference` |
| [OE Prefix Patterns](reference/oe-patterns.md) | OE-number prefix-pattern framework | `prefix pattern reference` |
| [Size Ranges](reference/size-ranges.md) | Typical dimensions by vehicle class + oil-filter threads | `reference` |
| [Replacement Intervals](reference/replacement-intervals.md) | Reference replacement cycles for 5 filter types | `reference` |
| [Procurement](reference/procurement.md) | HS-code reference + MOQ/packing framework | `reference` |
| [Filter Media](materials/media-comparison.md) | Seven media types compared (core + cabin/specialty) | `framework reference` + `editorial` |
| [Data Specification](specification/field-schema.md) | Field schema, status labels, sources & disclaimer | `verified` |

## Quick facts

- **10 SKUs** across **5 categories** (air filter: 8 · cabin filter: 1 · oil filter: 1 · fuel: 0 · wiper: 0).
- **74 vehicle models** across **28 brands** in the fitment reference framework (5 filter types × 74 vehicles = 370 rows), prioritising **overseas-market models** (56 overseas + 18 Chinese domestic).
- **OE prefix-pattern framework** across 4 filter types (prefix patterns only — full OE numbers are never asserted).
- Canonical dataset version: `0.1.0` (generated 2026-10-26); fitment framework `0.2.0`.

## Honest data posture

The source product catalogue does **not** publish per-SKU dimensions, filter media,
efficiency, OE numbers or packing data. Rather than invent those values, this site marks
them `NEEDS_VERIFICATION` and directs buyers to confirm them with Huiying before quoting.
The fitment framework and all reference datasets are **reference-only** — no exact OE
number or exact dimension is asserted.

Start with the [SKU Index](products/index.md), or go to the
[commercial catalog](https://huiyingfilter.com/products/) to request a quote.
