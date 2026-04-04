# `gsl_schedule`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `gsl_schedule_id` | bigint | NO |  |  |
| `schedule_name` | character varying | NO |  |  |
| `deleted` | boolean | NO | false |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO | timezone('UTC'::text, now()) |  |

## Sample Data

| `gsl_schedule_id` | `schedule_name` | `deleted` | `utc_last_update_timestamp` |
| --- | --- | --- | --- |
| 1 | [REDACTED] | False | [REDACTED] |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
