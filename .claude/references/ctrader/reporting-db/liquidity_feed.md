# `liquidity_feed`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `liquidity_feed_id` | bigint | NO |  |  |
| `liquidity_feed_type` | character varying | NO |  |  |
| `liquidity_feed_name` | character varying | NO |  |  |
| `is_enabled` | boolean | NO |  |  |
| `support_email` | character varying | YES |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | YES | timezone('UTC'::text, now()) |  |
| `configuration_suffix` | USER-DEFINED | NO | 'DEFAULT'::lp_suffix |  |
| `deal_expiration_timeout` | bigint | NO | 15000 |  |
| `trade_enabled` | boolean | NO | true |  |
| `network_delay_threshold_ms` | bigint | NO | 3000 |  |
| `network_delay_threshold_count` | bigint | NO | 10 |  |
| `monitor_price_connect` | boolean | NO | true |  |
| `monitor_trade_connect` | boolean | NO | true |  |

## Sample Data

| `liquidity_feed_id` | `liquidity_feed_type` | `liquidity_feed_name` | `is_enabled` | `support_email` | `utc_last_update_timestamp` | `configuration_suffix` | `deal_expiration_timeout` | `trade_enabled` | `network_delay_threshold_ms` | `network_delay_threshold_count` | `monitor_price_connect` | `monitor_trade_connect` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | CURRENEX | [REDACTED] | False | NULL | [REDACTED] | DEFAULT | 15000 | False | 3000 | 10 | True | True |
| 12 | FDRVT | [REDACTED] | False | NULL | [REDACTED] | DEFAULT | 15000 | False | 3000 | 10 | True | True |
| 13 | FXCM | [REDACTED] | False | NULL | [REDACTED] | DEFAULT | 15000 | False | 3000 | 10 | True | True |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
