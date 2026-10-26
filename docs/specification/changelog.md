# Changelog

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
