# `dynamic_leverage`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `leverage_id` | bigint | NO |  |  |
| `leverage_name` | character varying | NO |  |  |
| `leverage_description` | character varying | YES |  |  |
| `deleted` | boolean | NO | false |  |
| `readonly` | boolean | NO | false |  |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |

## Sample Data

| `leverage_id` | `leverage_name` | `leverage_description` | `deleted` | `readonly` | `utc_last_update_timestamp` |
| --- | --- | --- | --- | --- | --- |
| 1009 | [REDACTED] | Default leverage for Strategy Symbols | False | True | [REDACTED] |
| 1010 | [REDACTED] | Test | True | False | [REDACTED] |
| 1013 | [REDACTED] | Leverage 1:100 | False | False | [REDACTED] |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
