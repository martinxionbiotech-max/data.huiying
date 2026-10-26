# Data Status Labels

Every data point on this site carries one of three status labels. They tell the reader
exactly how confident we are in the value.

| Label | Meaning | Used for |
|---|---|---|
| `verified` | Present in the canonical dataset / source site; no interpretation applied | SKU identity fields (model, category, name, slug, source ID) |
| `reference` | Common-application or framework-level guidance, **not** a verified match | Vehicle-fitment framework, media typical ranges |
| `NEEDS_VERIFICATION` | Field is expected but the source data does not supply it — do not quote without confirming | SKU dimensions, material, efficiency, OE, packing, HS Code |

## Rules

1. **No invented values.** A field that is absent from the source is rendered as
   `NEEDS_VERIFICATION`, never as a plausible-sounding guess.
2. **No precise OE numbers.** The source catalogue publishes no per-SKU OE numbers, so
   none are asserted anywhere on this site.
3. **Fitment is always `reference`.** Vehicle fitment is common-application guidance;
   confirm against the buyer's OE / cross-reference table before ordering.

## How to upgrade a field

To move a field from `NEEDS_VERIFICATION` to `verified`, the value must be added to the
canonical dataset `data/products.json` on the main site and re-synced here (byte-identical
copy), then the pages are regenerated with `python3 scripts/build-fitment-pages.py`.

See [Field Schema](field-schema.md) and [Sources & disclaimer](sources.md).
