# Data Status Labels

Every data point on this site carries one status label. They tell the reader exactly
how confident we are in the value.

## Fitment / OE relationship — three states

For vehicle-fitment and OE-relationship data (the 592-row fitment matrix and the
SKU–OE–Vehicle association), three states apply:

| Label | Meaning | Used for |
|---|---|---|
| `reference` | Common-application or framework-level guidance, **not** a verified match | The 592-row vehicle-fitment matrix (74 vehicles × 8 filter types); vehicle model/year attached to any SKU |
| `source-verified` | Value is published by the source catalog; the OE↔brand attribution is a fact | The OE↔brand relationship for congben-sourced SKUs (e.g. `17220-5R0-008` → Honda) |
| `fitment-verified` | A **complete** SKU-OE-vehicle-source-verification-date record | Only when all of SKU + OE + exact vehicle + source + verification date are recorded. **None exist today (0 rows).** |

## SKU identity / specification — four labels

For SKU identity and specification fields on the product pages:

| Label | Meaning | Used for |
|---|---|---|
| `verified` | Present in the canonical dataset / source site; no interpretation applied | SKU identity fields (model, category, name, slug, source ID) |
| `source-verified` | Value is published by the source catalog (congbenfilter.com) | OE number(s), cross-reference, material, and the OE↔brand relationship where stated |
| `reference` | Framework-level guidance, not a verified match | Vehicle-fitment framework, media typical ranges, vehicle model/year |
| `NEEDS_VERIFICATION` | Field is expected but the source data does not supply it — leave blank, do not quote without confirming | SKU dimensions, efficiency, packing, HS Code (when absent) |

## Rules

1. **No invented values.** A field absent from the source is rendered blank (or
   `NEEDS_VERIFICATION`), never as a plausible-sounding guess.
2. **OE↔brand is `source-verified`, vehicle model/year is `reference`.** The source
   catalog states the OE number and (usually) its brand — that attribution is a fact.
   The specific vehicle model and year a part fits is **not** verified and stays `reference`.
3. **`fitment-verified` is a high bar.** It requires a complete
   SKU-OE-vehicle-source-verification-date record. Nothing on this site currently meets it.
4. **Fitment is never an exact-fitment tool.** Every fitment page is labelled
   "reference material — not an exact-fitment tool".

## How to upgrade a field

To move a field from `NEEDS_VERIFICATION` / `reference` to `source-verified` or
`fitment-verified`, the value must be added to the canonical dataset `data/products.json`
on the main site and re-synced here (byte-identical copy), then the pages are regenerated:

- `python3 scripts/build-fitment-pages.py`
- `python3 scripts/build-sku-oe-vehicle.py`

See [Field Schema](field-schema.md) and [Sources & disclaimer](sources.md).
