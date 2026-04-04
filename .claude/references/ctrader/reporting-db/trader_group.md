# `trader_group`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trader_group_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `deleted` | boolean | NO |  |  |
| `enabled` | boolean | NO |  |  |
| `swap_enabled` | boolean | NO |  |  |
| `margin_call_level` | numeric | NO |  |  |
| `stop_out_level` | numeric | NO |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `is_default` | boolean | NO |  |  |
| `price_stream_id` | bigint | NO |  |  |
| `minimal_paid_commission` | bigint | NO |  |  |
| `bonus_convert_lots` | boolean | NO | true |  |
| `bonus_conversion_rate_lots` | bigint | NO | 100 |  |
| `bonus_conversion_rate` | bigint | NO | 0 |  |
| `is_dealing_desk` | boolean | NO | false |  |
| `blocked_channels` | character varying | YES |  |  |
| `max_auto_execution_size_profile_id` | bigint | YES |  |  |
| `fair_stop_out` | boolean | NO | false |  |
| `region_id` | bigint | YES |  | CS-10591 Support Region in groups |
| `copy_disabled` | boolean | NO | false | If TRUE then trader's of the Group are unable to create sub-accounts |
| `stopout_disabled` | boolean | NO | false | If TRUE then account is not checked for breaching Stop-Out level |
| `inactivity_grace_period` | integer | NO | 0 | Grace period in days during which an inactivity fee is not charged for a account since last filled deal. |
| `inactivity_charge_period` | integer | NO | 0 | Period in days after which an inactivity fee is charged. |
| `inactivity_fee_amount` | integer | NO | 0 | Inactivity fee amount in cents, specified in USD and converted to Deposit CCY of an account |
| `copy_providing_disabled` | boolean | NO | false | If TRUE then traders of the group are unable to become copy provider. Logic is on JM side |
| `legal_entity_id` | bigint | YES |  |  |
| `disable_password_login` | boolean | NO | false |  |
| `allow_worse_gsl` | boolean | NO | true |  |
| `fake_spread_betting` | boolean | NO | false |  |
| `swap_and_dividend_profile_id` | bigint | YES |  |  |
| `negative_balance_protection` | boolean | NO | false |  |
| `allow_trader_change_so` | boolean | NO | false | If FALSE trader can not change their Stop Out strategy |
| `shared_access_enabled` | boolean | NO | true |  |
| `stop_out_strategy` | integer | NO | 0 | MOST_MARGIN_USED_FIRST(0), MOST_LOSING_FIRST(1) |
| `negative_balance_protection_limit_usd` | integer | YES |  |  |

## Sample Data

| `trader_group_id` | `name` | `description` | `deleted` | `enabled` | `swap_enabled` | `margin_call_level` | `stop_out_level` | `utc_last_update_timestamp` | `is_default` | `price_stream_id` | `minimal_paid_commission` | `bonus_convert_lots` | `bonus_conversion_rate_lots` | `bonus_conversion_rate` | `is_dealing_desk` | `blocked_channels` | `max_auto_execution_size_profile_id` | `fair_stop_out` | `region_id` | `copy_disabled` | `stopout_disabled` | `inactivity_grace_period` | `inactivity_charge_period` | `inactivity_fee_amount` | `copy_providing_disabled` | `legal_entity_id` | `disable_password_login` | `allow_worse_gsl` | `fake_spread_betting` | `swap_and_dividend_profile_id` | `negative_balance_protection` | `allow_trader_change_so` | `shared_access_enabled` | `stop_out_strategy` | `negative_balance_protection_limit_usd` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1057 | [REDACTED] |  | False | True | True | 0.00000 | 0.20000 | [REDACTED] | False | 1 | 0 | False | 100 | 0 | False |  | NULL | True | NULL | False | False | 0 | 0 | 0 | False | NULL | [REDACTED] | True | False | 2 | True | False | True | 0 | NULL |
| 1041 | [REDACTED] |  | False | True | True | 0.00000 | 0.20000 | [REDACTED] | False | 5 | 0 | False | 100 | 0 | False |  | NULL | True | NULL | True | False | 0 | 0 | 0 | False | NULL | [REDACTED] | True | False | 2 | True | False | True | 0 | NULL |
| 1050 | [REDACTED] |  | False | True | True | 0.00000 | 0.20000 | [REDACTED] | False | 8 | 0 | False | 100 | 0 | False |  | NULL | True | NULL | True | False | 0 | 0 | 0 | False | NULL | [REDACTED] | True | False | 2 | True | False | True | 0 | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
