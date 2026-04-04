# `trader`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trader_id` | bigint | NO |  |  |
| `trader_group_id` | bigint | NO |  |  |
| `login` | bigint | NO |  |  |
| `deleted` | boolean | NO |  |  |
| `phone_password` | character varying | YES |  |  |
| `name` | character varying | YES |  |  |
| `country_id` | bigint | YES |  |  |
| `city` | character varying | YES |  |  |
| `state` | character varying | YES |  |  |
| `zip_code` | character varying | YES |  |  |
| `address` | character varying | YES |  |  |
| `phone` | character varying | YES |  |  |
| `email` | character varying | YES |  |  |
| `description` | character varying | YES |  |  |
| `document_id` | character varying | YES |  |  |
| `status` | character varying | YES |  | Any string from client protobuf message |
| `registration_timestamp` | timestamp without time zone | NO |  |  |
| `last_connection_timestamp` | timestamp without time zone | YES |  |  |
| `leverage` | integer | NO |  | Default symbol leverage in cents |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `is_system` | boolean | NO |  |  |
| `introducing_broker1` | character varying | YES |  |  |
| `introducing_broker2` | character varying | YES |  |  |
| `account_type` | integer | NO |  | HEDGED(0), NETTED(1), SPREAD_BETTING(2); |
| `deposit_asset_id` | bigint | NO |  |  |
| `introducing_broker` | boolean | NO | false |  |
| `parent_ib_id` | bigint | YES |  |  |
| `ib_commission_rate` | integer | NO | 0 |  |
| `pocket_commission_rate` | integer | NO | 0 |  |
| `pocket_markup_rate` | integer | NO | 0 |  |
| `default_ib_commission_rate` | integer | NO | 0 |  |
| `default_pocket_commission_rate` | integer | NO | 0 |  |
| `default_pocket_markup_rate` | integer | NO | 0 |  |
| `logout_timestamp` | timestamp without time zone | YES |  |  |
| `default_split_revenue` | boolean | NO | false |  |
| `last_name` | character varying | YES |  |  |
| `split_revenue` | boolean | NO | false |  |
| `rank_id` | integer | YES |  |  |
| `show_personal_data` | boolean | NO | false |  |
| `manager_bonus` | bigint | YES |  |  |
| `ib_bonus` | bigint | YES |  |  |
| `ib_becoming_requested` | boolean | NO | false |  |
| `ib_becoming_request_timestamp` | timestamp without time zone | NO | timezone('UTC'::text, now()) |  |
| `access_rights` | numeric | NO | 0 | FULL_ACCESS(0), CLOSE_ONLY(1), NO_TRADING(2), NO_LOGIN(3); |
| `send_own_statement` | boolean | NO | false |  |
| `swap_free` | boolean | NO | false |  |
| `move_to_ib_group` | boolean | NO | false |  |
| `broker_name` | character varying | YES |  |  |
| `total_margin_calculation_type` | integer | NO | 0 | 0=MAX, 1=SUM, 2=NET |
| `investment` | bigint | YES | 0 |  |
| `max_leverage` | integer | YES |  |  |
| `free_trades` | boolean | NO | false | trading with/without commissions |
| `rebate_rate` | integer | NO | 0 |  |
| `default_rebate_rate` | integer | NO | 0 |  |
| `version` | bigint | NO | 0 |  |
| `sub_account_of` | bigint | YES |  |  |
| `disable_password_login` | boolean | NO | false |  |
| `is_limited_risk` | boolean | NO | false |  |
| `limited_risk_margin_calculation_strategy` | USER-DEFINED | YES |  |  |
| `max_nop` | integer | YES |  | value = 1 equal to 0.01% |
| `send_statement_to_broker` | boolean | YES |  |  |
| `default_ib_commission_type` | smallint | NO | 1 |  |
| `ib_commission_type` | smallint | NO | 1 |  |
| `fair_stop_out` | boolean | YES |  |  |
| `strategy_provider_name` | character varying | YES |  |  |
| `strategy_provider_id` | bigint | YES |  |  |
| `stop_out_strategy` | integer | YES |  | MOST_MARGIN_USED_FIRST(0), MOST_LOSING_FIRST(1) |
| `account_lifetime_type` | smallint | YES |  | UNLIMITED(1), LIMITED_INACTIVITY(2), LIMITED_CREATION(3), LIMITED_CREATION_FREE(4) |
| `comment` | character varying | YES |  |  |

## Sample Data

| `trader_id` | `trader_group_id` | `login` | `deleted` | `phone_password` | `name` | `country_id` | `city` | `state` | `zip_code` | `address` | `phone` | `email` | `description` | `document_id` | `status` | `registration_timestamp` | `last_connection_timestamp` | `leverage` | `utc_last_update_timestamp` | `is_system` | `introducing_broker1` | `introducing_broker2` | `account_type` | `deposit_asset_id` | `introducing_broker` | `parent_ib_id` | `ib_commission_rate` | `pocket_commission_rate` | `pocket_markup_rate` | `default_ib_commission_rate` | `default_pocket_commission_rate` | `default_pocket_markup_rate` | `logout_timestamp` | `default_split_revenue` | `last_name` | `split_revenue` | `rank_id` | `show_personal_data` | `manager_bonus` | `ib_bonus` | `ib_becoming_requested` | `ib_becoming_request_timestamp` | `access_rights` | `send_own_statement` | `swap_free` | `move_to_ib_group` | `broker_name` | `total_margin_calculation_type` | `investment` | `max_leverage` | `free_trades` | `rebate_rate` | `default_rebate_rate` | `version` | `sub_account_of` | `disable_password_login` | `is_limited_risk` | `limited_risk_margin_calculation_strategy` | `max_nop` | `send_statement_to_broker` | `default_ib_commission_type` | `ib_commission_type` | `fair_stop_out` | `strategy_provider_name` | `strategy_provider_id` | `stop_out_strategy` | `account_lifetime_type` | `comment` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6311 | 1102 | [REDACTED] | False | [REDACTED] | [REDACTED] | 752 | Valluntena | NULL | NULL | NULL | [REDACTED] | [REDACTED] | NULL | NULL | NULL | 2026-04-02 21:04:49.971000 | NULL | 50000 | [REDACTED] | False | NULL | NULL | 0 | 15 | False | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | True | [REDACTED] | False | NULL | False | NULL | NULL | False | 2026-04-02 21:04:49.951000 | 2 | True | False | False | [REDACTED] | 0 | 0 | 50000 | False | 0 | 0 | 1 | NULL | [REDACTED] | False | NULL | NULL | False | 1 | 1 | NULL | NULL | NULL | NULL | NULL | NULL |
| 5606 | 1058 | [REDACTED] | False | [REDACTED] | [REDACTED] | NULL | NULL | NULL | NULL | NULL | [REDACTED] | [REDACTED] | NULL | NULL | NULL | 2025-12-08 20:49:40.520000 | NULL | 10000 | [REDACTED] | False | NULL | NULL | 0 | 15 | False | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | True | [REDACTED] | False | NULL | False | NULL | NULL | False | 2025-12-08 20:49:40.502000 | 2 | True | False | False | [REDACTED] | 0 | 0 | 50000 | False | 0 | 0 | 1 | NULL | [REDACTED] | False | NULL | NULL | False | 1 | 1 | NULL | NULL | NULL | NULL | NULL | NULL |
| 6052 | 1058 | [REDACTED] | False | NULL | [REDACTED] | NULL | Khodabandeh | NULL | NULL | NULL | [REDACTED] | [REDACTED] | NULL | NULL | NULL | 2026-02-06 18:49:04.610000 | NULL | 50000 | [REDACTED] | False | NULL | NULL | 0 | 15 | False | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | True | [REDACTED] | False | NULL | False | NULL | NULL | False | 2026-02-06 18:49:04.590000 | 2 | True | False | False | [REDACTED] | 0 | 0 | 50000 | False | 0 | 0 | 2 | NULL | [REDACTED] | False | NULL | NULL | False | 1 | 1 | NULL | NULL | NULL | NULL | NULL | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
