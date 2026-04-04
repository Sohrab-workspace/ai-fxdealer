# `symbol_category`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `id` | bigint | NO |  |  |
| `asset_class_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `color` | character varying | NO |  |  |
| `sorting_number` | double precision | NO |  |  |
| `expanded` | boolean | NO |  |  |
| `is_default` | boolean | NO |  |  |
| `is_dom_enabled` | boolean | NO | true |  |

## Sample Data

| `id` | `asset_class_id` | `name` | `color` | `sorting_number` | `expanded` | `is_default` | `is_dom_enabled` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 10 | [REDACTED] | 33C1F3 | 0.0 | True | True | True |
| 2 | 2 | [REDACTED] | FFC000 | 500.0 | True | True | True |
| 3 | 3 | [REDACTED] | B3B3B3 | 2000.0 | True | True | True |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
