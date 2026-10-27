# Field Schema

Schema for the canonical datasets that drive this site: `data/products.json`
(the authoritative product dataset, byte-identical with the main site) and
`data/fitment.json` (the reference-only fitment framework).

## `products.json`

### `_meta`

| Field | Type | Meaning |
|---|---|---|
| `title` | string | Dataset title |
| `version` | string | Semantic version (`0.1.0`) |
| `generated` | string | Generation date (`YYYY-MM-DD`) |
| `brand` | string | Canonical brand (`huiying`) |
| `source` | string | Source-site note |
| `purpose` | string | Single-source-of-truth statement |

### `categories[]`

| Field | Type | Meaning |
|---|---|---|
| `slug` | string | URL slug (`air-filter`) |
| `name` | string | Display name (`Air Filter`) |
| `code` | string | Short category code (`af`) |
| `icon` | string | Icon path (main-site asset) |
| `desc` | string | Category description |

### `products[]`

| Field | Type | Meaning | Status in this build |
|---|---|---|---|
| `slug` | string | SKU slug (`of-690`) | `verified` |
| `name` | string | Display name (`Oil Filter`) | `verified` |
| `category` | string | Category slug | `verified` |
| `sourceId` | integer | Source-site product ID | `verified` |
| `model` | string | Canonical model (`HY-OF-690`) | `verified` |
| `desc` | string | Source-site generic description | `verified` (as text) |
| `image` | string | Product image path | `verified` |
| `gallery[]` | string[] | Image gallery paths | `verified` |

!!! warning "Fields NOT present in the source data"
    Dimensions, filter media material, filtration efficiency, OE numbers,
    cross-references, packing and HS Code **do not exist** in the source product
    catalogue. Every such field is rendered as `NEEDS_VERIFICATION` — they are listed
    here for completeness but must be supplied by Huiying before quoting.

## `fitment.json`

### `_meta`

| Field | Type | Meaning |
|---|---|---|
| `nature` | string | `reference-only` (not verified OE data) |
| `disclaimer` | string | Standing disclaimer applied to every entry |

### `vehicles[]`

| Field | Type | Meaning |
|---|---|---|
| `brand` | string | Vehicle brand |
| `region` | string | Brand home region |
| `model` | string | Vehicle model (English) |
| `zh` | string | Vehicle model (Chinese) |
| `era` | string | Broad service era (`reference`) |
| `class` | string | Vehicle class (compact / mid-size / suv / pickup) |

### `filters[]`

| Field | Type | Meaning |
|---|---|---|
| `type` | string | Filter type slug |
| `label` | string | Display label |
| `intro` | string | Framework intro |
| `typical_size_range` | string | Typical size range (`reference`) |
| `material_suggestion` | string | Media suggestion per filter type (`reference`) |
| `replacement_interval` | string | Replacement interval (`reference`) |
| `matching_path` | string | OE → cross-reference matching path |
| `data_status` | string | Always `reference` |

## Reference datasets (v0.2.0)

Four additional reference datasets drive the `reference/` pages. All are `reference-only`.

### `oe-patterns.json`

| Field | Type | Meaning |
|---|---|---|
| `status_label` | string | Standing label (`prefix pattern reference — verify full OE number`) |
| `filters[].type` | string | Filter type slug |
| `filters[].patterns[].brand` | string | Brand (or brand group) |
| `filters[].patterns[].prefix` | string | OE prefix **pattern** (never a full number) |
| `cross_reference_path[]` | string[] | Ordered cross-reference lookup steps |
| `coverage_note` | string | Brands without a stable public prefix pattern |

### `size-ranges.json`

| Field | Type | Meaning |
|---|---|---|
| `air_filter_by_class[]` | object[] | Length/width/height ranges by vehicle class (`reference`) |
| `oil_filter_threads[]` | object[] | Common oil-filter thread specs (`reference`) |
| `cabin_filter_range` / `fuel_filter_range` | string | Typical ranges for the other filter types |

### `replacement-intervals.json`

| Field | Type | Meaning |
|---|---|---|
| `intervals[]` | object[] | km / months / note per filter type (`reference`) |
| `factors[]` | object[] | Factors affecting replacement interval |
| `suggestions[]` | object[] | Localised subjective suggestions (signed ` ✍️`) |

### `procurement.json`

| Field | Type | Meaning |
|---|---|---|
| `hs_codes[]` | object[] | HS-code reference (`reference — verify with customs`) |
| `moq_packing[]` | object[] | MOQ / packing framework (no fixed numbers asserted) |
| `export_markets` | string | Export markets (consistent with main site) |

See [Data status labels](data-status.md) and [Sources & disclaimer](sources.md).
