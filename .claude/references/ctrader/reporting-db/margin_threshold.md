# `margin_threshold`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `margin_threshold_id` | bigint | NO |  |  |
| `trader_id` | bigint | NO |  |  |
| `margin_level_threshold` | double precision | YES | 0 |  |
| `threshold_id` | character varying | NO |  |  |

## Sample Data

| `margin_threshold_id` | `trader_id` | `margin_level_threshold` | `threshold_id` |
| --- | --- | --- | --- |
| 1 | 666 | 1.5 | 29646241MC_1 |
| 2 | 666 | 0.8 | 29646241MC_3 |
| 78 | 1047 | 1.5 | 33044527MC_1 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
