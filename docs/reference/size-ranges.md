# Filter Size Reference Ranges

Typical dimensional ranges by vehicle class, plus common oil-filter thread specifications. Public common-knowledge ranges for estimation only.

> **Auto-generated** by `scripts/build-fitment-pages.py`. Canonical dataset `data/products.json` v0.1.0 (2026-10-26). Do not edit values by hand — edit the dataset, then rebuild. Size dataset `data/size-ranges.json` v0.2.0 — `reference-only`.

> ⚠️ **reference-only** — These are typical REFERENCE ranges, not measurements of any specific SKU. They are for planning and estimation only; never use them to confirm a part. Always match the exact part by OE / cross-reference number.

## Engine air filter — typical L×W×H by vehicle class

| Vehicle class | Length (mm) | Width (mm) | Height (mm) | Example vehicles | Status |
|---|---|---|---|---|---|
| Compact / C-segment (`compact`) · 紧凑型 | 230–280 | 140–180 | 25–45 | Corolla, Civic, Lavida, Focus, Elantra, Sylphy, Emgrand | `reference` |
| Mid-size / D-segment (`mid-size`) · 中型 | 250–310 | 160–200 | 30–50 | Camry, Accord, Passat, 3 Series, C-Class, A4, Malibu | `reference` |
| SUV / Crossover (`suv`) · SUV / 跨界 | 250–330 | 170–220 | 35–60 | RAV4, CR-V, Tiguan, X3, GLC, Q5, Haval H6 | `reference` |
| Pickup / Light truck (`pickup`) · 皮卡 / 轻卡 | 270–350 | 180–230 | 40–70 | F-150, Ranger, Poer | `reference` |

## Oil filter — typical thread specifications

| Thread | Typical applications | Status |
|---|---|---|
| `3/4-16 UNF` | Most common spin-on thread (Toyota, Honda, Ford, GM and many aftermarket) | `reference` |
| `M20 × 1.5` | Volkswagen Group, Mercedes-Benz and many European engines | `reference` |
| `M22 × 1.5` | BMW, Mercedes-Benz and Volvo (some applications) | `reference` |
| `M18 × 1.5` | Nissan, Subaru and some Japanese applications | `reference` |
| `M26 × 1.5 / M27 × 2` | Heavy-duty / cartridge applications | `reference` |

## Other filter types (typical ranges)

- **Cabin filter:** Panel type: L 200–320 × W 150–260 × H 15–40 mm (reference; carbon variants share footprint).
- **Fuel filter:** In-line / cartridge: OD 50–90 × H 80–160 mm (reference).

## Notes

- Air-filter panel dimensions scale with engine displacement and vehicle class, not with brand.
- Oil-filter thread is engine-specific; the same vehicle name can use different threads across model years and engines.
- Never order on dimensional ranges alone — confirm the OE / cross-reference number first.

