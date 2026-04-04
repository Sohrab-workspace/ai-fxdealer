# `protection_profile`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `protection_profile_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `gsl_charge` | bigint | NO | 0 |  |
| `sl_distance` | integer | NO | 0 |  |
| `tp_distance` | integer | NO | 0 |  |
| `gsl_distance` | integer | NO | 0 |  |
| `distance_type` | integer | NO | 1 | SYMBOL_DISTANCE_IN_POINTS(1), SYMBOL_DISTANCE_IN_PERCENTAGE(2) |
| `tolerance` | integer | NO | 0 |  |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |
| `deleted` | boolean | NO | false |  |

## Sample Data

| `protection_profile_id` | `name` | `description` | `gsl_charge` | `sl_distance` | `tp_distance` | `gsl_distance` | `distance_type` | `tolerance` | `utc_last_update_timestamp` | `deleted` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [REDACTED] | NULL | 0 | 0 | 0 | 0 | 1 | 0 | [REDACTED] | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
