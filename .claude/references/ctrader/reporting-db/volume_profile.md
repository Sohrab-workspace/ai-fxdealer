# `volume_profile`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `volume_profile_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `min_volume` | bigint | NO |  |  |
| `max_volume` | bigint | NO |  |  |
| `min_stake` | bigint | NO | 1 |  |
| `max_stake` | bigint | NO | 10000000 |  |
| `step_volume` | bigint | NO | 1 |  |
| `step_stake` | bigint | NO | 1 |  |
| `max_exposure` | bigint | NO | '10000000000000'::bigint |  |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |
| `deleted` | boolean | NO | false |  |
| `exposure_calc_type` | integer | NO | 3 | 0-EXP_MAX, 1-EXP_SUM, 2-EXP_NET, 3-EXP_NET_ALLOW_CLOSE (default) |

## Sample Data

| `volume_profile_id` | `name` | `description` | `min_volume` | `max_volume` | `min_stake` | `max_stake` | `step_volume` | `step_stake` | `max_exposure` | `utc_last_update_timestamp` | `deleted` | `exposure_calc_type` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [REDACTED] | NULL | 100000 | 100000000 | 1 | 10000000 | 100000 | 1 | 10000000000000 | [REDACTED] | False | 3 |
| 3 | [REDACTED] | NULL | 100000 | 10000000000 | 1 | 10000000 | 100000 | 1 | 10000000000000 | [REDACTED] | False | 3 |
| 4 | [REDACTED] | NULL | 100 | 1000000 | 100 | 10000000 | 100 | 100 | 10000000000000 | [REDACTED] | False | 3 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
