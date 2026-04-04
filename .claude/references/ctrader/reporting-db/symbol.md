# `symbol`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `symbol_id` | integer | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `digits` | integer | NO |  |  |
| `pip_position` | integer | NO |  |  |
| `lp_enabled` | boolean | NO |  |  |
| `enabled` | boolean | NO |  |  |
| `default_swap_long` | numeric | NO |  |  |
| `default_swap_short` | numeric | NO |  |  |
| `default_swap_rollover_3days` | integer | NO |  | NONE(0), MONDAY(1), TUESDAY(2), WEDNESDAY(3), THURSDAY(4), FRIDAY(5), SATURDAY(6), SUNDAY(7) |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `bid_markup` | integer | NO | 0 |  |
| `ask_markup` | integer | NO | 0 |  |
| `sorting_number` | double precision | NO |  |  |
| `measurement_units` | character varying | YES |  |  |
| `base_asset_id` | bigint | NO |  |  |
| `quote_asset_id` | bigint | NO |  |  |
| `quote_expiration_timeout` | integer | NO |  |  |
| `min_spread_enabled` | boolean | NO | false |  |
| `min_spread` | integer | NO | 0 |  |
| `min_spread_bias` | integer | NO | 0 |  |
| `internal_alias` | character varying | NO |  |  |
| `lot_size` | bigint | NO |  |  |
| `enable_short_selling` | boolean | NO | true |  |
| `symbol_category_id` | bigint | YES |  |  |
| `favorite` | boolean | NO | false |  |
| `always_manual` | boolean | NO | false |  |
| `tags` | character varying | YES |  |  |
| `default_leverage_id` | bigint | NO | 0 |  |
| `price_liquidity_feed_id` | integer | NO | 0 |  |
| `trade_liquidity_feed_id` | integer | NO | 0 |  |
| `trading_mode` | integer | NO | 0 | ENABLED(0), DISABLED_WITHOUT_PENDINGS_EXECUTION(1), DISABLED_WITH_PENDINGS_EXECUTION(2), CLOSE_ONLY_MODE(3) |
| `dividend_time` | timestamp without time zone | NO | now() |  |
| `unified_symbol_id` | integer | YES |  |  |
| `schedule_profile_id` | bigint | NO |  |  |
| `default_commission_profile_id` | bigint | NO |  |  |
| `default_volume_profile_id` | bigint | NO |  |  |
| `default_execution_profile_id` | bigint | NO |  |  |
| `autochartist_alias` | character varying | YES |  |  |
| `trading_central_alias` | character varying | YES |  |  |
| `default_protection_profile_id` | bigint | NO |  |  |
| `default_swap_free_profile_id` | bigint | NO |  |  |
| `default_gsl_schedule_id` | bigint | NO |  |  |
| `holiday_profile_id` | bigint | NO |  |  |
| `archived` | boolean | NO | false |  |
| `bbsp_alias` | character varying | YES |  |  |
| `default_trade_notification_profile_id` | bigint | NO |  |  |
| `default_swap_time` | integer | NO |  |  |
| `default_swap_period` | integer | NO |  |  |
| `default_skip_swap_periods` | integer | NO | 0 |  |
| `default_charge_swap_at_weekends` | boolean | NO | false |  |
| `last_split_timestamp` | timestamp without time zone | YES |  |  |
| `last_manual_chart_invalidate_timestamp` | timestamp without time zone | YES |  |  |
| `tv_alias` | character varying | YES |  |  |

## Sample Data

| `symbol_id` | `name` | `description` | `digits` | `pip_position` | `lp_enabled` | `enabled` | `default_swap_long` | `default_swap_short` | `default_swap_rollover_3days` | `utc_last_update_timestamp` | `bid_markup` | `ask_markup` | `sorting_number` | `measurement_units` | `base_asset_id` | `quote_asset_id` | `quote_expiration_timeout` | `min_spread_enabled` | `min_spread` | `min_spread_bias` | `internal_alias` | `lot_size` | `enable_short_selling` | `symbol_category_id` | `favorite` | `always_manual` | `tags` | `default_leverage_id` | `price_liquidity_feed_id` | `trade_liquidity_feed_id` | `trading_mode` | `dividend_time` | `unified_symbol_id` | `schedule_profile_id` | `default_commission_profile_id` | `default_volume_profile_id` | `default_execution_profile_id` | `autochartist_alias` | `trading_central_alias` | `default_protection_profile_id` | `default_swap_free_profile_id` | `default_gsl_schedule_id` | `holiday_profile_id` | `archived` | `bbsp_alias` | `default_trade_notification_profile_id` | `default_swap_time` | `default_swap_period` | `default_skip_swap_periods` | `default_charge_swap_at_weekends` | `last_split_timestamp` | `last_manual_chart_invalidate_timestamp` | `tv_alias` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 374 | [REDACTED] | Euro vs Swedish Krona | 5 | 4 | True | True | 0.00000 | 0.00000 | 3 | [REDACTED] | 925 | 925 | 0.0 | EUR | 1352 | 13 | 300 | False | 0 | 0 | EURSEK | 10000000 | True | 17 | False | False | NULL | 1019 | 66 | 66 | 0 | 1970-01-01 00:00:00 | NULL | 43 | 1 | 1 | 1 | NULL | NULL | 1 | 1 | 1 | 3 | False | NULL | 1000 | 1259 | 24 | 0 | False | NULL | NULL | NULL |
| 375 | [REDACTED] | US Dollar vs Swedish Krona | 5 | 4 | True | True | 0.00000 | 0.00000 | 3 | [REDACTED] | 925 | 925 | 1.0 | USD | 1384 | 13 | 300 | False | 0 | 0 | USDSEK | 10000000 | True | 17 | False | False | NULL | 1019 | 66 | 66 | 0 | 1970-01-01 00:00:00 | NULL | 43 | 1 | 1 | 1 | NULL | NULL | 1 | 1 | 1 | 3 | False | NULL | 1000 | 1259 | 24 | 0 | False | NULL | NULL | NULL |
| 376 | [REDACTED] | Euro vs Norwegian Krone | 4 | 3 | True | True | 0.00000 | 0.00000 | 3 | [REDACTED] | 90 | 90 | 2.0 | EUR | 1352 | 10 | 300 | False | 0 | 0 | EURNOK | 10000000 | True | 17 | False | False | NULL | 1019 | 66 | 66 | 0 | 1970-01-01 00:00:00 | NULL | 43 | 1 | 1 | 1 | NULL | NULL | 1 | 1 | 1 | 3 | False | NULL | 1000 | 1259 | 24 | 0 | False | NULL | NULL | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
