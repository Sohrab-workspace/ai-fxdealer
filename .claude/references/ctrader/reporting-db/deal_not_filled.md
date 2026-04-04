# `deal_not_filled`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `deal_id` | bigint | NO |  |  |
| `trade_order_id` | bigint | NO |  |  |
| `volume` | bigint | NO |  |  |
| `limit_price` | bigint | YES |  |  |
| `trade_side` | integer | NO |  |  |
| `symbol_id` | integer | NO |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `margin_rate` | double precision | NO |  |  |
| `book_type` | integer | NO |  |  |
| `position_id` | bigint | NO |  |  |
| `deal_status` | integer | NO |  |  |
| `filled_volume` | bigint | NO |  |  |
| `execution_price` | bigint | YES |  |  |
| `lp_execution_price` | bigint | YES |  |  |
| `execution_timestamp` | timestamp without time zone | NO |  |  |
| `lp_order_id` | character varying | YES |  |  |
| `deal_type` | integer | NO |  |  |
| `offsetted` | boolean | NO | false |  |
| `commission` | bigint | NO | 0 |  |
| `unrealized_swap` | bigint | NO | 0 |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `liquidity_feed_id` | bigint | YES |  |  |
| `price_snapshot_id` | bigint | YES |  |  |
| `server_order_id` | character varying | YES |  |  |
| `symbol_markup_execution_price` | bigint | YES |  |  |
| `ib_commission` | bigint | NO | 0 |  |
| `pocket_commission` | bigint | NO | 0 |  |
| `pocket_markup` | bigint | NO | 0 |  |
| `parent_ib_id` | bigint | YES |  |  |
| `mirroring_commission` | bigint | NO | 0 |  |
| `markup` | bigint | NO | 0 |  |
| `lot_size` | bigint | NO |  |  |
| `inner_mirroring_fee` | boolean | NO | true |  |
| `total_volume_in_usd` | bigint | NO | 0 |  |
| `split_revenue` | boolean | NO | false |  |
| `stake` | bigint | YES |  |  |
| `desired_vwap` | bigint | NO | 0 |  |
| `market_vwap` | bigint | NO | 0 |  |
| `tolerance` | integer | NO | 0 |  |
| `reject_reason` | character varying | YES |  |  |
| `manual` | boolean | NO | false |  |
| `spot_price` | bigint | YES |  |  |
| `base_to_usd_conversion_rate` | double precision | NO | (0)::double precision |  |
| `trader_id` | bigint | YES |  |  |
| `filled_eur_volume` | bigint | YES |  |  |
| `filled_gbp_volume` | bigint | YES |  |  |
| `is_precise_money` | boolean | NO | false |  |

## Sample Data

| `deal_id` | `trade_order_id` | `volume` | `limit_price` | `trade_side` | `symbol_id` | `create_timestamp` | `margin_rate` | `book_type` | `position_id` | `deal_status` | `filled_volume` | `execution_price` | `lp_execution_price` | `execution_timestamp` | `lp_order_id` | `deal_type` | `offsetted` | `commission` | `unrealized_swap` | `utc_last_update_timestamp` | `liquidity_feed_id` | `price_snapshot_id` | `server_order_id` | `symbol_markup_execution_price` | `ib_commission` | `pocket_commission` | `pocket_markup` | `parent_ib_id` | `mirroring_commission` | `markup` | `lot_size` | `inner_mirroring_fee` | `total_volume_in_usd` | `split_revenue` | `stake` | `desired_vwap` | `market_vwap` | `tolerance` | `reject_reason` | `manual` | `spot_price` | `base_to_usd_conversion_rate` | `trader_id` | `filled_eur_volume` | `filled_gbp_volume` | `is_precise_money` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 3 | 10000000 | NULL | 1 | 1 | 2023-08-18 11:36:40.607000 | 1.08613 | 2 | 2 | 5 | 0 | NULL | NULL | 2023-08-18 11:36:40.607000 | NULL | 1 | False | 0 | 0 | [REDACTED] | 66 | 3 | NULL | NULL | 0 | 0 | 0 | NULL | 0 | 0 | 10000000 | True | 0 | False | NULL | 108613 | 0 | 0 | Not enough funds | False | NULL | 1.08613 | 1022 | 0 | 0 | False |
| 18 | 18 | 100000 | NULL | 1 | 108 | 2023-08-18 11:46:59.740000 | 16867.258626 | 1 | 10 | 5 | 0 | NULL | NULL | 2023-08-18 11:46:59.740000 | NULL | 1 | False | 0 | 0 | [REDACTED] | 66 | 18 | NULL | NULL | 0 | 0 | 0 | NULL | 0 | 0 | 1000 | True | 23188938 | False | NULL | 1551828000 | 0 | 0 | Not enough funds | False | NULL | 16867.258626 | 1022 | 0 | 0 | False |
| 19 | 19 | 100000 | NULL | 1 | 104 | 2023-08-18 11:48:28.005000 | 83.26 | 1 | 11 | 5 | 0 | NULL | NULL | 2023-08-18 11:48:28.005000 | NULL | 1 | False | 0 | 0 | [REDACTED] | 66 | 19 | NULL | NULL | 0 | 0 | 0 | NULL | 0 | 0 | 100000 | True | 23188938 | False | NULL | 8327000 | 0 | 0 | Not enough funds | False | NULL | 83.26 | 1022 | 0 | 0 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
