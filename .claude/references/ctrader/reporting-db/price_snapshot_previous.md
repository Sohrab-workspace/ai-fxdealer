# `price_snapshot_previous`

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

_No rows returned or table is empty._

## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
