# SKU–OE–Vehicle Association

Every **congben-sourced SKU** with an OE number, mapped to the OE number(s) published by the source catalog. The **OE↔brand** relationship is `source-verified` where the source states a brand (the OE number's brand attribution is a fact); specific **vehicle model/year** application is `reference`-only.

> **Auto-generated** by `scripts/build-sku-oe-vehicle.py` from `data/products.json` v0.3.0 (2026-10-28). Do not edit values by hand — edit the dataset, then rebuild.


**33 OE-bearing SKUs · 25 with source-verified OE↔brand · 8 OE-only (brand not stated) · 0 fitment-verified.**

| SKU | Category | OE number(s) | Brand | OE↔brand status | Vehicle (reference) |

|---|---|---|---|---|---|
| `03-42776-010` | Air Filter | `03-42776-010` · `0342776010` | Freightliner | `source-verified` | Cascadia, Detroit Diesel |
| `04E129620` | Air Filter | `04E129620` · `L04E129620D` | Volkswagen | `source-verified` | VW |
| `13717811026` | Air Filter | `13717811026` | BMW | `source-verified` | X3, X5, X6 |
| `1500A098` | Air Filter | `1500A098` | Mitsubishi | `source-verified` | 1500a098, 1500a358 |
| `16546-ED000` | Air Filter | `16546-ED000` | Nissan | `source-verified` | Tiida, NV200, March |
| `17220-5R0-008` | Air Filter | `17220-5R0-008` | Honda | `source-verified` | Quality |
| `17801-21050` | Air Filter | `17801-21050` | Toyota | `source-verified` | Corolla, Avensis, Auris |
| `17801-30070` | Air Filter | `17801-30070` | `—` | `reference` | `—` |
| `28113-2S000` | Air Filter | `28113-2S000` | Kia | `source-verified` | HYUNDAI |
| `A2700940004` | Air Filter | `A2700940004` | Mercedes-Benz | `source-verified` | A, B, CLA, GLA Class |
| `LR011593` | Air Filter | `LR011593` | Land Rover | `source-verified` | Discovery 4, RR Sport, RR |
| `RE596317` | Air Filter | `RE596317` · `RE596318` | John Deere | `source-verified` | E- |
| `04465-04030` | Brake Pads | `04465-04030` · `04465-0K020` | Toyota | `source-verified` | `—` |
| `04465-0K020` | Brake Pads | `04465-0K020` · `04465-04030` · `04465-0K070` | Toyota | `source-verified` | 04465, 0k020, 04030, 0k070 |
| `87139-0N010` | Cabin Filter | `87139-0N010` · `87139-30040` | Toyota | `source-verified` | `—` |
| `1000FH` | Fuel Filter | `1000FH` · `1000FG` | `—` | `reference` | `—` |
| `23390-0L070` | Fuel Filter | `23390-0L070` · `23390-0L090` | Toyota | `source-verified` | `—` |
| `500FH` | Fuel Filter | `500FH` · `500FG` | `—` | `reference` | `—` |
| `900FG` | Fuel Filter | `900FG` · `900FH` | `—` | `reference` | `—` |
| `FF5507` | Fuel Filter | `FF5507` | `—` | `reference` | `—` |
| `04152-31080` | Oil Filter | `04152-31080` | Toyota | `source-verified` | & Lexus |
| `04152-31090` | Oil Filter | `04152-31090` · `04152-YZZA1` | `—` | `reference` | `—` |
| `04152-37010` | Oil Filter | `04152-37010` · `04152-YZZA6` | Toyota | `source-verified` | Corolla |
| `15208-65F00` | Oil Filter | `15208-65F00` | `—` | `reference` | `—` |
| `15400-PLC` | Oil Filter | `15400-PLC` | Honda | `source-verified` | `—` |
| `15400-PLC-004` | Oil Filter | `15400-PLC-004` · `15400-PLC-003` | Honda | `source-verified` | `—` |
| `35330-08010` | Oil Filter | `35330-08010` · `58010` | Toyota | `source-verified` | Lexus |
| `90915-YZZE1` | Oil Filter | `90915-YZZE1` · `90915-YZZJ1` | Toyota | `source-verified` | RAV4, Camry, Corolla, Prius |
| `90915-YZZE2` | Oil Filter | `90915-YZZE2` · `90915-YZZJ2` | Toyota | `source-verified` | Camry, Corolla, RAV4, Highlander, Yaris, Prius, Matrix, Lexus CT200h, ES240, ES350 |
| `A0001802309` | Oil Filter | `A0001802309` · `A0001802609` | Mercedes-Benz | `source-verified` | `—` |
| `A2701800009` | Oil Filter | `A2701800009` · `A2701800109` · `A2701840025` · `A2701840125` | Mercedes-Benz | `source-verified` | M270 & M274 |
| `LF14000NN` | Oil Filter | `LF14000NN` | `—` | `reference` | `—` |
| `17127525023` | Rubber Hoses | `17127525023` | BMW | `source-verified` | `—` |

## Status labels

- **`reference`** — framework / common-application guidance; not a verified match
- **`source-verified`** — value published by the source catalog; OE↔brand is a fact
- **`fitment-verified`** — complete SKU-OE-vehicle-source-verification-date record

> ⚠️ **reference / source-verified, not exact-fitment** — OE numbers and their brand attribution are drawn from the source catalog (congbenfilter.com). Vehicle model/year application is reference-only — always confirm against the buyer's OE / cross-reference table before ordering.
