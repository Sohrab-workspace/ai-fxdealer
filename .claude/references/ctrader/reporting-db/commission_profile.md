# `commission_profile`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `commission_profile_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `trading_commission_rate` | bigint | NO |  |  |
| `commission_type` | integer | NO | 1 | USD_PER_MILLION_USD(1), USD_PER_LOT(2), PERCENTAGE_OF_VALUE(3), QUOTE_CCY_PER_LOT(4) |
| `min_commission` | bigint | NO | 0 |  |
| `min_commission_type` | integer | NO | 1 | CURRENCY(1), QUOTE_CURRENCY(2) |
| `min_commission_asset_id` | bigint | YES |  |  |
| `avoid_min_commission_on_stopout` | boolean | NO | false |  |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |
| `pnl_conversion_fee_rate` | integer | NO | 0 |  |
| `deleted` | boolean | NO | false |  |

## Sample Data

| `commission_profile_id` | `name` | `description` | `trading_commission_rate` | `commission_type` | `min_commission` | `min_commission_type` | `min_commission_asset_id` | `avoid_min_commission_on_stopout` | `utc_last_update_timestamp` | `pnl_conversion_fee_rate` | `deleted` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [REDACTED] | NULL | 0 | 1 | 0 | 1 | 15 | False | [REDACTED] | 0 | False |
| 2 | [REDACTED] | $4 commission per lot | 200000000 | 2 | 1000000 | 1 | 15 | False | [REDACTED] | 0 | False |
| 4 | [REDACTED] | $6 commission per lot | 300000000 | 2 | 1000000 | 1 | 15 | False | [REDACTED] | 0 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
