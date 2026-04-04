# `daily_asset_to_usd`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `report_timestamp` | timestamp without time zone | NO |  |  |
| `asset_id` | bigint | NO |  |  |
| `rate` | double precision | NO |  |  |

## Sample Data

| `report_timestamp` | `asset_id` | `rate` |
| --- | --- | --- |
| 2023-08-02 20:55:00.002000 | 32 | 1843.08 |
| 2023-08-02 20:55:00.002000 | 3 | 1.1393414606357526 |
| 2023-08-02 20:55:00.002000 | 5 | 1.09378 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
