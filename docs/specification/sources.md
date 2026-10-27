# Sources & Disclaimer

## Where the data comes from

| Source | What it provides | Reliability |
|---|---|---|
| Main-site `src/data/products.json` (canonical) | SKU identity: model, category, name, slug, source ID, description, images | `verified` — copied byte-identical into `data/products.json` |
| Source-site product pages (tianrui crawl) | Category names and company boilerplate only — **no per-SKU specs** | Used only to confirm the catalogue is spec-sparse |
| Main-site `vehicleFitment.ts` | Reference-level brand/model framework the fitment matrix is based on | `reference` |
| Editorial (this site) | Filter-media comparison and buying guidance | `framework reference` + signed `editorial` |

## Honest disclosures

- **No per-SKU specifications are available** in the source data. Dimensions, filter
  media, efficiency, OE numbers, cross-references, packing and HS Code are marked
  `NEEDS_VERIFICATION` throughout.
- **Fitment is reference-only.** Vehicle-model listings are common-application examples,
  not verified OE cross-references. No exact OE number, exact dimension or precise year
  range is asserted.
- **Typical media figures are framework references** (`[]`), not measured
  performance of any specific SKU. They are intended for comparison only.
- **No certification is claimed.** Standards mentioned (ISO / SAE / GB) are test-method
  frameworks, not certificates held by any product.

## Contact

For verified specifications, OE cross-references or quotes, contact the manufacturer
through [huiyingfilter.com](https://huiyingfilter.com/) — do not rely on this reference
site as a purchasing specification.

See also [Data status labels](data-status.md) and [Field schema](field-schema.md).
