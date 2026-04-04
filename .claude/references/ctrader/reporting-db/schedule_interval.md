# `schedule_interval`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `schedule_profile_id` | bigint | NO |  |  |
| `start_second` | integer | NO |  |  |
| `end_second` | integer | NO |  |  |
| `is_global_session_start` | boolean | NO | false |  |
| `is_global_session_end` | boolean | NO | false |  |

## Sample Data

| `schedule_profile_id` | `start_second` | `end_second` | `is_global_session_start` | `is_global_session_end` |
| --- | --- | --- | --- | --- |
| 3 | 79205 | 161995 | True | True |
| 3 | 165605 | 248395 | True | True |
| 3 | 252005 | 334795 | True | True |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
