# `price_snapshot_default`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `price_snapshot_id` | bigint | NO |  |  |
| `symbol_id` | integer | YES |  |  |
| `price_volume_a` | ARRAY | YES |  |  |
| `price_volume_b` | ARRAY | YES |  |  |

## Sample Data

| `price_snapshot_id` | `symbol_id` | `price_volume_a` | `price_volume_b` |
| --- | --- | --- | --- |
| 1 | 1 | [[109283, 60000000], [109282, 208800000], [109285, 70000000], [109284, 60000000], [109286, 130000000]] | [[109280, 300000000], [109277, 100000000], [109276, 110000000], [109279, 50000000], [109278, 60000000]] |
| 2 | 1 | [[109139, 50000000], [109141, 50000000], [109140, 50000000], [109143, 90000000], [109142, 80000000], [109130, 270000000]] | [[109137, 50000000], [109136, 60000000], [109129, 150000000], [109130, 10000000], [109133, 180000000], [109135, 80000000], [109134, 110000000]] |
| 3 | 1 | [[108613, 370000000], [108615, 50000000], [108614, 60000000], [108617, 90000000], [108616, 50000000]] | [[108609, 60000000], [108608, 50000000], [108610, 50000000], [108612, 110000000], [108607, 60000000], [108606, 140000000]] |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
