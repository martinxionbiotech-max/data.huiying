# SKU–OE–Vehicle Association

Every **congben-sourced SKU** with an OE number, mapped to the OE number(s) published by the source catalog. The **OE↔brand** relationship is `catalog-confirmed` where the source states a brand (the OE number's brand attribution is a fact); specific **vehicle model/year** application is `reference`-only.

> ⚠️ **This is a separate partition from the [fitment reference matrix](../fitment/index.md).** The 74-vehicle reference matrix is a common-application framework; this page records only the *real* SKU↔OE relationships present in the canonical dataset.

> **Auto-generated** by `scripts/build-sku-oe-vehicle.py` from `data/products.json` v0.3.0 (2026-10-28). Do not edit values by hand — edit the dataset, then rebuild.


**33 OE-bearing SKUs · 26 with catalog-confirmed OE↔brand · 7 OE-only (brand not stated) · 0 factory-verified.**

| SKU | Category | OE number(s) | Brand | OE↔brand status | Vehicle (reference) |

|---|---|---|---|---|---|
| `03-42776-010` | Air Filter | `03-42776-010` · `0342776010` | Freightliner | `catalog-confirmed` | Cascadia, Detroit Diesel |
| `04E129620` | Air Filter | `04E129620` · `L04E129620D` | Volkswagen | `catalog-confirmed` | VW |
| `13717811026` | Air Filter | `13717811026` | BMW | `catalog-confirmed` | X3, X5, X6 |
| `1500A098` | Air Filter | `1500A098` | Mitsubishi | `catalog-confirmed` | 1500a098, 1500a358 |
| `16546-ED000` | Air Filter | `16546-ED000` | Nissan | `catalog-confirmed` | Tiida, NV200, March |
| `17220-5R0-008` | Air Filter | `17220-5R0-008` | Honda | `catalog-confirmed` | Quality |
| `17801-21050` | Air Filter | `17801-21050` | Toyota | `catalog-confirmed` | Corolla, Avensis, Auris |
| `17801-30070` | Air Filter | `17801-30070` | Toyota | `catalog-confirmed` | `—` |
| `28113-2S000` | Air Filter | `28113-2S000` | Kia | `catalog-confirmed` | HYUNDAI |
| `A2700940004` | Air Filter | `A2700940004` | Mercedes-Benz | `catalog-confirmed` | A, B, CLA, GLA Class |
| `LR011593` | Air Filter | `LR011593` | Land Rover | `catalog-confirmed` | Discovery 4, RR Sport, RR |
| `RE596317` | Air Filter | `RE596317` · `RE596318` | John Deere | `catalog-confirmed` | E- |
| `04465-04030` | Brake Pads | `04465-04030` · `04465-0K020` | Toyota | `catalog-confirmed` | `—` |
| `04465-0K020` | Brake Pads | `04465-0K020` · `04465-04030` · `04465-0K070` | Toyota | `catalog-confirmed` | 04465, 0k020, 04030, 0k070 |
| `87139-0N010` | Cabin Filter | `87139-0N010` · `87139-30040` | Toyota | `catalog-confirmed` | `—` |
| `1000FH` | Fuel Filter | `1000FH` · `1000FG` | `—` | `reference` | `—` |
| `23390-0L070` | Fuel Filter | `23390-0L070` · `23390-0L090` | Toyota | `catalog-confirmed` | `—` |
| `500FH` | Fuel Filter | `500FH` · `500FG` | `—` | `reference` | `—` |
| `900FG` | Fuel Filter | `900FG` · `900FH` | `—` | `reference` | `—` |
| `FF5507` | Fuel Filter | `FF5507` | `—` | `reference` | `—` |
| `04152-31080` | Oil Filter | `04152-31080` | Toyota / Lexus | `catalog-confirmed` | `—` |
| `04152-31090` | Oil Filter | `04152-31090` · `04152-YZZA1` | `—` | `reference` | `—` |
| `04152-37010` | Oil Filter | `04152-37010` · `04152-YZZA6` | Toyota | `catalog-confirmed` | Corolla |
| `15208-65F00` | Oil Filter | `15208-65F00` | `—` | `reference` | `—` |
| `15400-PLC` | Oil Filter | `15400-PLC` | Honda | `catalog-confirmed` | `—` |
| `15400-PLC-004` | Oil Filter | `15400-PLC-004` · `15400-PLC-003` | Honda | `catalog-confirmed` | `—` |
| `35330-08010` | Oil Filter | `35330-08010` · `58010` | Toyota | `catalog-confirmed` | Lexus |
| `90915-YZZE1` | Oil Filter | `90915-YZZE1` · `90915-YZZJ1` | Toyota | `catalog-confirmed` | RAV4, Camry, Corolla, Prius |
| `90915-YZZE2` | Oil Filter | `90915-YZZE2` · `90915-YZZJ2` | Toyota | `catalog-confirmed` | Camry, Corolla, RAV4, Highlander, Yaris, Prius, Matrix, Lexus CT200h, ES240, ES350 |
| `A0001802309` | Oil Filter | `A0001802309` · `A0001802609` | Mercedes-Benz | `catalog-confirmed` | `—` |
| `A2701800009` | Oil Filter | `A2701800009` · `A2701800109` · `A2701840025` · `A2701840125` | Mercedes-Benz | `catalog-confirmed` | M270 & M274 |
| `LF14000NN` | Oil Filter | `LF14000NN` | `—` | `reference` | `—` |
| `17127525023` | Rubber Hoses | `17127525023` | BMW | `catalog-confirmed` | `—` |

## Status labels

- **`reference`** — framework / common-application guidance; not a verified match
- **`catalog-confirmed`** — source-catalog field; OE↔brand is a fact
- **`factory-verified`** — factory drawings / measurements (complete record)

> ⚠️ **catalog-confirmed / reference, not exact-fitment** — OE numbers and their brand attribution are drawn from the source catalog (congbenfilter.com). Vehicle model/year application is reference-only — always confirm against the buyer's OE / cross-reference table before ordering.
