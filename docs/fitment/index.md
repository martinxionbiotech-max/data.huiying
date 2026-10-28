# Fitment Reference Index

> ⚠️ **Reference material — not an exact-fitment tool.** This is a common-application reference framework, **not** a precise OE cross-reference table. Always confirm the exact part against your OE / cross-reference number before ordering.

Reference-level vehicle-fitment framework for the core filter types. These are **common-application references**, not precise OE cross-references.

> **Auto-generated** by `scripts/build-fitment-pages.py`. Canonical dataset `data/products.json` v0.3.0 (2026-10-28). Do not edit values by hand — edit the dataset, then rebuild. Fitment framework `data/fitment.json` v0.3.0 (2026-10-27) — `reference-only`.

**28 brands · 74 vehicle models · 592 fitment rows (8 filter types).**

| Attribute | Value |
|---|---|
| Brands | Audi, BMW, BYD, Changan, Chery, Chevrolet, Dodge, Ford, GMC, Geely, Great Wall, Honda, Hyundai, Jeep, Kia, Land Rover, Mazda, Mercedes-Benz, Mitsubishi, Nissan, Peugeot, Renault, Roewe, Skoda, Subaru, Toyota, Volkswagen, Volvo |
| Regions | China, Czech Republic, France, Germany, Japan, South Korea, Sweden, USA, United Kingdom |
| Filter types | Engine Air Filter, Engine Oil Filter, Cabin Air Filter, Fuel Filter, Wiper, Brake Pads, Spark Plugs, Rubber Hoses |
| Matrix rows | 592 |
| Data status | `reference` (all matrix rows) |

### Three-state data status

| State | Meaning | Count here |
|---|---|---|
| `reference` | common-application guidance, not a verified match | 592 matrix rows |
| `source-verified` | OE↔brand attribution is a fact (source catalog) | see [SKU–OE–Vehicle association](../reference/sku-oe-vehicle.md) |
| `fitment-verified` | complete SKU-OE-vehicle-source-date record | 0 |

| Page | Type | Matrix size | Data status |
|---|---|---|---|
| [Engine Air Filter](air-filter.md) | `air-filter` | 74 vehicles × 1 row = 74 rows | `reference` |
| [Engine Oil Filter](oil-filter.md) | `oil-filter` | 74 vehicles × 1 row = 74 rows | `reference` |
| [Cabin Air Filter](cabin-filter.md) | `cabin-filter` | 74 vehicles × 1 row = 74 rows | `reference` |
| [Fuel Filter](fuel-filter.md) | `fuel-filter` | 74 vehicles × 1 row = 74 rows | `reference` |
| [Wiper](wiper.md) | `wiper` | 74 vehicles × 1 row = 74 rows | `reference` |
| [Brake Pads](brake-pads.md) | `brake-pads` | 74 vehicles × 1 row = 74 rows | `reference` |
| [Spark Plugs](spark-plugs.md) | `spark-plugs` | 74 vehicles × 1 row = 74 rows | `reference` |
| [Rubber Hoses](rubber-hoses.md) | `rubber-hoses` | 74 vehicles × 1 row = 74 rows | `reference` |

> ⚠️ **reference-only** — Every entry is a common-application reference. No exact OE number, exact dimension, or precise year range is asserted. Always confirm the exact part against the buyer's OE number, cross-reference number, or Huiying's fitment table before ordering.
