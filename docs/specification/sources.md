# Sources & Disclaimer

## Where the data comes from

| Source | What it provides | Reliability |
|---|---|---|
| Main-site `src/data/products.json` (canonical) | SKU identity: model, category, name, slug, source ID, description, images | `verified` — copied byte-identical into `data/products.json` |
| Source-site product pages (congbenfilter.com) | OE numbers, cross-references, material, and the OE↔brand attribution | `catalog-confirmed` — the source catalog states these fields; the OE number's brand attribution is a fact |
| Source-site product pages (tianrui crawl) | Category names and company boilerplate only — **no per-SKU specs** | Used only to confirm the catalogue is spec-sparse |
| Main-site `vehicleFitment.ts` | Reference-level brand/model framework the fitment matrix is based on | `reference` |
| Editorial (this site) | Filter-media comparison and buying guidance | `framework reference` + signed `editorial` |

## Honest disclosures

- **OE numbers, cross-references, material and OE↔brand are `catalog-confirmed`** — drawn
  from the source catalog (congbenfilter.com), not independently verified against a vehicle.
- **No per-SKU specifications beyond the catalog fields.** Dimensions, thread, seal, bypass,
  filtration efficiency, packing and HS Code are marked `pending` throughout.
- **Fitment is reference-only.** Vehicle-model listings are common-application examples,
  not verified OE cross-references. No exact OE number, exact dimension or precise year
  range is asserted. The 74-vehicle matrix is a *reference model list* — it does not mean
  every model has a corresponding SKU, and it is not a verified fitment.
- **`factory-verified` is empty (0 rows).** No SKU is backed by a factory drawing or
  measured test record on this site. Verification dates are left blank rather than
  auto-generated.
- **Typical media figures are framework references** (`[]`), not measured performance of
  any specific SKU. They are intended for comparison only.
- **No certification is claimed.** Standards mentioned (ISO / SAE / GB) are test-method
  frameworks, not certificates held by any product.

## Contact

For verified specifications, OE cross-references or quotes, contact the manufacturer
through [carfilterspro.com](https://carfilterspro.com/) — do not rely on this reference
site as a purchasing specification.

See also [Data status labels](data-status.md) and [Field schema](field-schema.md).
