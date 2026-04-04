# `holiday`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `holiday_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `schedule_timezone` | character varying | NO |  |  |
| `holiday_date` | date | NO |  |  |
| `recurring` | boolean | NO |  |  |
| `start_second` | integer | YES |  |  |
| `end_second` | integer | YES |  |  |

## Sample Data

| `holiday_id` | `name` | `description` | `schedule_timezone` | `holiday_date` | `recurring` | `start_second` | `end_second` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | [REDACTED] | Tuesday 24th December | Europe/Bucharest | 2024-12-24 | False | 19800 | 86340 |
| 2 | [REDACTED] | Tuesday 24th December | Europe/Bucharest | 2024-12-24 | False | 72900 | 86340 |
| 4 | [REDACTED] | Tuesday 24th December | Europe/Bucharest | 2024-12-24 | False | 21600 | 86340 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
