# `schedule_profile`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `schedule_profile_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `schedule_timezone` | character varying | NO | 'UTC'::character varying |  |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |
| `deleted` | boolean | NO | false |  |

## Sample Data

| `schedule_profile_id` | `name` | `description` | `schedule_timezone` | `utc_last_update_timestamp` | `deleted` |
| --- | --- | --- | --- | --- | --- |
| 26 | [REDACTED] | NULL | Australia/Canberra | [REDACTED] | False |
| 3 | [REDACTED] | NULL | UTC | [REDACTED] | False |
| 4 | [REDACTED] | NULL | UTC | [REDACTED] | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
