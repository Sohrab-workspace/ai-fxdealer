# `holiday_profile`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `holiday_profile_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |
| `deleted` | boolean | NO | false |  |

## Sample Data

| `holiday_profile_id` | `name` | `description` | `utc_last_update_timestamp` | `deleted` |
| --- | --- | --- | --- | --- |
| 1 | [REDACTED] | Default profile without any holidays | [REDACTED] | False |
| 31 | [REDACTED] |  | [REDACTED] | False |
| 15 | [REDACTED] |  | [REDACTED] | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
