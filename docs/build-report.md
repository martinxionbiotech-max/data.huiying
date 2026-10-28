# data.huiying — Build Report

**Date:** 2026-10-26 · **Repo:** `data.huiying` (empty-repo scaffold) · **Brand:** huiying ·
**Main site:** carfilterspro.com · **Deploy domain:** data.carfilterspro.com

## 1. Scope

Built the huiying bottom-layer data sub-site (MkDocs Material) as the machine-readable
data layer backing the commercial main site.

| Item | Result |
|---|---|
| Framework | MkDocs 1.6.1 · Material 9.7.7 (navy `#0F2A43` primary · orange `#E8622C` accent, matching main site) |
| Canonical sync | `data/products.json` byte-identical with `../Huiying/src/data/products.json` (6065 bytes, `diff` = 0) |
| Generator | `scripts/build-fitment-pages.py` — renders all data pages from the two JSON datasets (idempotent) |
| Build | `mkdocs build` — **0 warnings**, 27 HTML pages (26 content + 1 404) |
| Git | committed + pushed to `origin/main` (empty repo → first push) |

## 2. Page inventory

| Section | Pages | Notes |
|---|---|---|
| Home | 1 | data-site positioning + entry points |
| SKU Index | 1 | all 10 SKUs, spec status = `NEEDS_VERIFICATION` |
| Category pages | 5 | air / cabin / oil / fuel / wiper (fuel & wiper = 0 SKU, placeholder) |
| SKU parameter pages | 10 | identity `verified` + all specs `NEEDS_VERIFICATION` |
| Fitment reference | 4 | index + air / oil / cabin (3 filter types) |
| Filter media | 1 | cellulose vs blended vs synthetic vs nano-fibre comparison |
| Data specification | 4 | field schema · data status · sources · changelog |
| **Total content pages** | **26** | + 1 404.html = 27 HTML files |

## 3. Fitment matrix size

- **10 brands** (Toyota, Honda, Volkswagen, BMW, Mercedes-Benz, Ford, Hyundai, Nissan, Geely, Great Wall).
- **13 vehicle models** (Corolla, Camry, Civic, Accord, Lavida, Passat, 3 Series, C-Class, Focus, Elantra, Sylphy, Emgrand, Haval).
- **3 filter types** (engine air / oil / cabin) → **39 fitment rows** (13 × 3).
- All rows are `reference` — common-application only, no OE numbers asserted.

## 4. Data-status label distribution

| Label | Count (field-level) | Where |
|---|---|---|
| `verified` | 6 per SKU (×10 = 60) | SKU identity fields (model, brand, category, name, slug, source ID) |
| `reference` | 39 rows + media typical ranges + fitment framework | fitment tables, media comparison |
| `NEEDS_VERIFICATION` | 7 per SKU (×10 = 70) | dimensions, material, efficiency, OE, cross-ref, packing, HS Code |

**Honesty discipline:** the source catalogue publishes no per-SKU specs, so every missing
field is `NEEDS_VERIFICATION` — none were invented. Fitment is reference-only.

## 5. SEO & machine-readable

| Artifact | Status |
|---|---|
| `llms.txt` | llmstxt.org spec, 22 links + Notes (honest posture) |
| `sitemap.xml` | 26 URLs, generated via `site_url` |
| `robots.txt` | allow-all + sitemap reference |
| Organization JSON-LD | in `overrides/main.html` (`extrahead`) — huiying legal entity |
| Per-page title | Material auto `{page} - Huiying Filter Data` |

## 6. Main-site integration

- Added **"Product Data ↗"** footer link (`data.carfilterspro.com`, dofollow, `target=_blank`)
  in the main site `src/components/Footer.astro` Products column.
- Main site `npm run build` → 38 pages, clean; link rendered in `dist/index.html`.
- Main site committed + pushed (`data: link footer to data.carfilterspro.com`).

## 7. Verification checklist

- [x] `diff data/products.json ../Huiying/src/data/products.json` = IDENTICAL (0 bytes diff)
- [x] `mkdocs build` 0 warnings; 27 HTML pages
- [x] announce bar renders backlink to carfilterspro.com
- [x] Organization JSON-LD present in `site/index.html`
- [x] `sitemap.xml` (26 URLs) + `llms.txt` + `robots.txt` emitted to `site/`
- [x] Generator idempotent (re-run produces identical output)
- [x] Main-site footer link committed + pushed
- [x] `data.huiying` committed + pushed, sync `0/0`
