# `asset_class`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `sorting_number` | double precision | NO |  |  |
| `default_lots` | boolean | NO | true |  |

## Sample Data

| `id` | `name` | `sorting_number` | `default_lots` |
| --- | --- | --- | --- |
| 8 | [REDACTED] | 0.0 | True |
| 9 | [REDACTED] | 1.0 | True |
| 10 | [REDACTED] | 2.0 | True |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
