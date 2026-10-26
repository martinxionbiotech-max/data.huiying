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

### `filters[]`

| Field | Type | Meaning |
|---|---|---|
| `type` | string | Filter type slug |
| `label` | string | Display label |
| `intro` | string | Framework intro |
| `typical_size_range` | string | Typical size range (`reference`) |
| `matching_path` | string | OE → cross-reference matching path |
| `data_status` | string | Always `reference` |

See [Data status labels](data-status.md) and [Sources & disclaimer](sources.md).
