# Filter Replacement-Interval Reference

Industry-common replacement intervals for the five filter categories. Reference guidance only — always follow the vehicle/engine manufacturer's schedule first.

> **Auto-generated** by `scripts/build-fitment-pages.py`. Canonical dataset `data/products.json` v0.3.0 (2026-10-28). Do not edit values by hand — edit the dataset, then rebuild. Intervals dataset `data/replacement-intervals.json` v0.2.0 — `reference-only`.

> ⚠️ **reference-only** — Intervals are industry-common REFERENCE values (kilometres / months), not Huiying product specifications and not a substitute for the OEM service schedule. Adjust for local conditions and confirm per application.

## Reference intervals by filter type

| Filter type | Kilometres (reference) | Months (reference) | Note | Status |
|---|---|---|---|---|
| Engine Air Filter (`air-filter`) | 10,000–20,000 km | 12 months | Shorten to 5,000–10,000 km in heavy-dust / sand regions | `reference` |
| Engine Oil Filter (`oil-filter`) | 5,000–10,000 km | 6 months | Replace with every oil change; synthetic oil may extend the oil-change interval | `reference` |
| Cabin Air Filter (`cabin-filter`) | 10,000–20,000 km | 12 months | Replace before the humid / rainy season to avoid musty smell | `reference` |
| Fuel Filter (`fuel-filter`) | 20,000–40,000 km | 24 months | Diesel and commercial applications shorten toward the lower bound | `reference` |
| Wiper (`wiper`) | — (on condition) | 6–12 months | Replace on streaking, chatter or reduced clarity | `reference` |

## Factors affecting replacement interval

| Factor | Effect |
|---|---|
| Dust / road conditions | Shortens engine-air, cabin and oil intervals (desert, unpaved, construction) |
| Climate humidity | Cabin filter replaced more often; watch for mould and fogging |
| Driving style | Stop-and-go / short trips shorten oil and fuel intervals |
| Fuel quality | Poor or contaminated fuel shortens fuel-filter life |
| Oil quality | Lower-grade oil loads the oil filter faster |
| OEM service schedule | Always the primary authority — this table is a secondary reference |

## Localised suggestions `小筑 ✍️`

- **中国华北 / 西北沙尘地区:** 空气滤清器建议缩短至 5,000–10,000 km 或按需更换；沙尘较大时推荐同时检查空调滤。 _(signed: 小筑 ✍️)_
- **中国南方潮湿地区:** 空调滤建议每年雨季前更换，避免霉味与出风減弱；优先选择活性炭层款。 _(signed: 小筑 ✍️)_
- **柴油商用车队:** 燃油滤建议按 20,000 km 或压差指示更换，对油水系统的保护价值高于件价本身。 _(signed: 小筑 ✍️)_

