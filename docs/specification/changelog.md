# Changelog

## v0.3.0 — 2026-10-28 (audit4 remediation)

- **Three-state data status model unified** across the main site and this data site:
  `catalog-confirmed` (source-catalog field; OE↔brand is a fact) · `factory-verified`
  (factory drawing / measurement; 0 rows today) · `pending` (year / engine / thread /
  seal / bypass parameters not yet verified). Previous labels renamed: `source-verified`
  → `catalog-confirmed`, `fitment-verified` → `factory-verified`, `NEEDS_VERIFICATION` → `pending`.
- **Case-A fix** (`17801-30070`): brand field set to `Toyota` (OE-number brand attribution
  is a source-catalog fact = `catalog-confirmed`); description wording downgraded to
  "Toyota OE-pattern (catalog-confirmed)".
- **Case-B fix** (`04152-31080`): 2.5L–3.5L displacement band downgraded to a catalog
  reference annotation (not a verified fitment); cross-reference numbers annotated as
  source catalog; false "thread/seal/bypass confirmed per engine" removed.
- **Fitment matrix redesign**: 592 rows frozen; each row now carries `Fitment status`
  (three-state, all `reference`) + `Evidence source` (blank) + `Verification date`
  (blank) + `Model year / engine (evidence)` (blank). No evidence source or verification
  date is ever auto-generated.
- **Fitment index** now states plainly that the 74 vehicle models are a *reference model
  list* (≠ every model has a SKU / verified fitment), and that the SKU–OE association is
  a separate partition from the reference matrix.
- **SKU parameter pages** now distinguish brand fitment (OE↔brand = `catalog-confirmed`)
  from vehicle models / engine (`reference` / `pending`), and add a "Quality verification
  & documents" section ("No published test data for this SKU").

## v0.2.0 — 2026-10-26 (data expansion)

- **Fitment matrix expansion**: 10 → **28 brands**, 13 → **74 vehicle models**, 3 → **5 filter types** (added fuel filter + wiper), 39 → **370 fitment rows**.
  - Overseas-market models prioritised (**56 overseas** + 18 Chinese domestic).
  - New overseas brands: Audi, Mazda, Kia, Subaru, Chevrolet, Renault, Peugeot, Skoda, Dodge, Jeep, GMC, Volvo, Land Rover, Mitsubishi.
  - Each row now carries: vehicle model / brand / era / typical size range / material suggestion / replacement interval / status (all `reference`).
- **OE prefix-pattern framework** (`data/oe-patterns.json` → `reference/oe-patterns.md`): prefix-pattern reference across 4 filter types + cross-reference lookup path + coverage note. Prefixes only; full OE numbers are never asserted.
- **Size reference ranges** (`data/size-ranges.json` → `reference/size-ranges.md`): air-filter L×W×H by vehicle class (compact / mid-size / SUV / pickup) + oil-filter thread specs (3/4-16 UNF, M18/M20/M22, M26/M27).
- **Replacement-interval reference** (`data/replacement-intervals.json` → `reference/replacement-intervals.md`): 5 filter types (km / months) + factors + localised suggestions (` ✍️`, China north-west dust / south humid / diesel fleet).
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
