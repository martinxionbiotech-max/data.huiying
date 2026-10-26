# data.huiying — Expansion Report (v0.2.0)

**Date:** 2026-10-26 · **Repo:** `data.huiying` · **Brand:** huiying ·
**Main site:** huiyingfilter.com · **Deploy domain:** data.huiying.com

Data-content expansion for the huiying bottom-layer data sub-site. Builds on the v0.1.0
scaffold and grows the reference layer while keeping the canonical `data/products.json`
byte-identical with the main site.

## 1. Vehicle-fitment matrix expansion

| Dimension | Before | After | Δ |
|---|---|---|---|
| Brands | 10 | **22** | +12 |
| Vehicle models | 13 | **66** | +53 |
| Filter types | 3 | **5** | +2 |
| Fitment rows | 39 | **330** | +291 |

- **New brands (12):** Audi, Mazda, Kia, Subaru, Chevrolet, Renault, Peugeot, Skoda,
  BYD, Roewe, Chery, Changan.
- **New filter types (2):** fuel filter + wiper → all five categories covered
  (air / oil / cabin / fuel / wiper).
- Each fitment row now carries: vehicle model / brand (region) / era / typical size
  range / material suggestion / replacement interval / status (all `reference`).

## 2. OE prefix-pattern reference framework

New dataset `data/oe-patterns.json` → `reference/oe-patterns.md`.

- **4 filter types** covered (air / oil / cabin / fuel), **23 brand-pattern entries**
  (Toyota `17801-…`, Honda `17220-…`, VW `06A/06J 115 …`, BMW `11 42 …`,
  Mercedes-Benz `A 651/271/272 180 …`, and more).
- Every entry labelled **`prefix pattern reference — verify full OE number`**; no full
  OE number is written.
- Includes a **cross-reference lookup path** (5 steps) and a **coverage note** for
  brands without a stable public prefix pattern (Ford air, GM/Chevrolet, Chinese
  domestic brands).

## 3. Size reference-range library

New dataset `data/size-ranges.json` → `reference/size-ranges.md`.

- **Air-filter L×W×H by vehicle class** — 4 classes (compact / mid-size / SUV / pickup).
- **Oil-filter thread specs** — 5 entries (3/4-16 UNF, M20 × 1.5, M22 × 1.5, M18 × 1.5,
  M26 × 1.5 / M27 × 2).
- Cabin + fuel typical ranges included; all `reference`.

## 4. Filter-media data expansion

`docs/materials/media-comparison.md` expanded from 4 → **7 media types**:

- **+3 new:** activated-carbon cabin (adsorption), glass fibre (high-temperature),
  electrostatic electret synthetic.
- Added a second **cabin & specialty media** matrix, three micro-characteristic
  sections, and a **material × vehicle-class pairing** table (5 scenarios).

## 5. Replacement-interval reference data

New dataset `data/replacement-intervals.json` → `reference/replacement-intervals.md`.

- **5 filter types** with km / months reference intervals.
- **6 factors** affecting replacement interval.
- **3 localised suggestions** (`小筑 ✍️`): China north-west dust (air filter 5,000–10,000 km),
  south humid (cabin filter before rainy season), diesel fleet (fuel filter 20,000 km).

## 6. Procurement data expansion

New dataset `data/procurement.json` → `reference/procurement.md`.

- **HS-code reference** — 5 entries (8421.31, 8421.23, 8421.39, 8421.99, 8512.40/8512.90),
  all `reference — verify with customs`.
- **MOQ / packing framework** — framework-level only (no fixed numbers asserted),
  consistent with the main site (private-label/OEM, mixed-container multi-SKU).

## 7. Page inventory

| Section | Pages | Notes |
|---|---|---|
| Home | 1 | updated stats |
| SKU Index | 1 | 10 SKUs |
| Category pages | 5 | air / cabin / oil / fuel / wiper |
| SKU parameter pages | 10 | identity `verified` + specs `NEEDS_VERIFICATION` |
| Fitment reference | 6 | index + 5 filter types |
| Reference data | 4 | OE patterns · size ranges · intervals · procurement |
| Filter media | 1 | 7 media types |
| Data specification | 4 | field schema · status · sources · changelog |
| **Total content pages** | **32** | + 1 404.html = 33 HTML files |

## 8. Verification checklist

- [x] `diff data/products.json ../Huiying/src/data/products.json` = IDENTICAL (6065 bytes, 0 diff)
- [x] Generator idempotent (re-run → identical md5 of all generated `.md`)
- [x] `mkdocs build` — 0 warnings; 33 HTML pages (32 content + 1 404); 32 sitemap URLs
- [x] `llms.txt` updated (new fitment + reference pages, 32 links + Notes)
- [x] Fitment matrix: 22 brands · 66 models · 5 types · 330 rows (all `reference`)
- [x] OE framework: prefix-pattern only, no full OE numbers
- [x] `mkdocs.yml` nav updated; report files excluded via `exclude_docs`

## 9. Honesty discipline retained

- No per-SKU dimension / material / efficiency / OE / packing value was invented —
  all remain `NEEDS_VERIFICATION` on SKU pages.
- Fitment, size ranges, intervals, HS codes and MOQ are all `reference` /
  common-knowledge with standing disclaimers.
- OE data is prefix-pattern level only; no exact OE number is asserted anywhere.
