# `deal_offset`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `deal_offset_id` | bigint | NO |  |  |
| `open_deal_id` | bigint | NO |  |  |
| `closing_deal_id` | bigint | NO |  |  |
| `volume` | bigint | NO |  |  |
| `not_offsetted_deal_id` | bigint | YES |  |  |
| `stake` | bigint | NO | 0 |  |
| `swap` | bigint | NO | 0 |  |

## Sample Data

| `deal_offset_id` | `open_deal_id` | `closing_deal_id` | `volume` | `not_offsetted_deal_id` | `stake` | `swap` |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 2 | 100000 | 2 | 0 | 0 |
| 2 | 4 | 5 | 100000 | 5 | 0 | 0 |
| 3 | 6 | 7 | 100000 | 7 | 0 | 0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
