# `country`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `country_id` | bigint | NO |  |  |
| `country_name` | character varying | NO |  |  |
| `country_alpha2_code` | character varying | YES |  | ISO 3166-1 Alpha-2 code |

## Sample Data

| `country_id` | `country_name` | `country_alpha2_code` |
| --- | --- | --- |
| 4 | [REDACTED] | AF |
| 8 | [REDACTED] | AL |
| 10 | [REDACTED] | AQ |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
