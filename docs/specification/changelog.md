# Changelog

## v0.2.0 — 2026-10-26 (data expansion)

- **Fitment matrix expansion**: 10 → **22 brands**, 13 → **66 vehicle models**, 3 → **5 filter types** (added fuel filter + wiper), 39 → **330 fitment rows**.
  - New brands: Audi, Mazda, Kia, Subaru, Chevrolet, Renault, Peugeot, Skoda, BYD, Roewe, Chery, Changan.
  - Each row now carries: vehicle model / brand / era / typical size range / material suggestion / replacement interval / status (all `reference`).
- **OE prefix-pattern framework** (`data/oe-patterns.json` → `reference/oe-patterns.md`): prefix-pattern reference across 4 filter types + cross-reference lookup path + coverage note. Prefixes only; full OE numbers are never asserted.
- **Size reference ranges** (`data/size-ranges.json` → `reference/size-ranges.md`): air-filter L×W×H by vehicle class (compact / mid-size / SUV / pickup) + oil-filter thread specs (3/4-16 UNF, M18/M20/M22, M26/M27).
- **Replacement-interval reference** (`data/replacement-intervals.json` → `reference/replacement-intervals.md`): 5 filter types (km / months) + factors + localised suggestions (`小筑 ✍️`, China north-west dust / south humid / diesel fleet).
- **Procurement reference** (`data/procurement.json` → `reference/procurement.md`): HS-code reference (8421.31 / 8421.23 / 8421.39 / 8421.99 / 8512.40 / 8512.90) + MOQ/packing framework (consistent with main site).
- **Filter-media comparison** expanded: +3 media (activated-carbon cabin, glass fibre, electrostatic electret), a second cabin/specialty matrix, and material × vehicle-class pairing guidance.
- Generator `scripts/build-fitment-pages.py` extended to render the 4 new reference pages + 5 fitment pages; fixed the multi-line string-concatenation bug in intro paragraphs.

## v0.1.0 — 2026-10-26

- Initial data sub-site scaffold (`data.huiying`, MkDocs Material).
- Synced canonical `data/products.json` byte-identical with the main site
  (`10 SKUs · 5 categories`).
- Added `data/fitment.json` reference framework (13 vehicles · 10 brands · 3 filter types).
- Added `scripts/build-fitment-pages.py` generator: SKU index, 5 category pages,
  10 SKU parameter pages, fitment index + 3 fitment reference tables.
- Added handwritten pages: home, filter-media comparison, field schema, data-status
  labels, sources & disclaimer.
- Added SEO: `llms.txt`, `robots.txt`, sitemap (via `site_url`), Organization JSON-LD,
  per-page `title`/`description`.

> Field-level data changes are recorded by editing the canonical dataset, then regenerating
> this site. See the repository `README.md` (at repo root) for the sync procedure.
