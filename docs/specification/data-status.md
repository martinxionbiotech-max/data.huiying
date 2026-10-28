# Data Status Labels

Every data point on this site carries one status label. They tell the reader exactly
how confident we are in the value.

## Fitment / OE relationship — three states

For vehicle-fitment and OE-relationship data (the 592-row fitment matrix and the
SKU–OE–Vehicle association), three states apply:

| Label | Meaning | Used for |
|---|---|---|
| `reference` | Common-application or framework-level guidance, **not** a verified match | The 592-row vehicle-fitment matrix (74 vehicles × 8 filter types); vehicle model/year attached to any SKU |
| `catalog-confirmed` | Value is published by the source catalog; the OE↔brand attribution is a fact | The OE↔brand relationship for congben-sourced SKUs (e.g. `17220-5R0-008` → Honda) |
| `factory-verified` | A **complete** factory drawing / measurement record | Only when a SKU's specification is backed by factory drawings or measured tests. **None exist today (0 rows).** |

## SKU identity / specification — four labels

For SKU identity and specification fields on the product pages:

| Label | Meaning | Used for |
|---|---|---|
| `verified` | Present in the canonical dataset / source site; no interpretation applied | SKU identity fields (model, category, name, slug, source ID) |
| `catalog-confirmed` | Value is published by the source catalog (congbenfilter.com) | OE number(s), cross-reference, material, and the OE↔brand relationship where stated |
| `reference` | Framework-level guidance, not a verified match | Vehicle-fitment framework, media typical ranges, vehicle model/year |
| `pending` | Field is expected but not yet verified (source data does not supply it, or no factory test) — leave blank, do not quote | SKU dimensions, thread, seal, bypass, efficiency, packing, HS Code, year/engine code |

## Rules

1. **No invented values.** A field absent from the source is rendered blank (`pending`),
   never as a plausible-sounding guess.
2. **OE↔brand is `catalog-confirmed`, vehicle model/year is `reference`.** The source
   catalog states the OE number and (usually) its brand — that attribution is a fact.
   The specific vehicle model, year and engine a part fits is **not** verified and stays
   `reference` (or `pending` when absent).
3. **`factory-verified` is a high bar.** It requires a factory drawing or measured test
   record. Nothing on this site currently meets it.
4. **Fitment is never an exact-fitment tool.** Every fitment page is labelled
   "reference material — not an exact-fitment tool".

## How to upgrade a field

To move a field from `pending` / `reference` to `catalog-confirmed` or
`factory-verified`, the value must be added to the canonical dataset `data/products.json`
on the main site and re-synced here (byte-identical copy), then the pages are regenerated:

- `python3 scripts/build-fitment-pages.py`
- `python3 scripts/build-sku-oe-vehicle.py`

See [Field Schema](field-schema.md) and [Sources & disclaimer](sources.md).
