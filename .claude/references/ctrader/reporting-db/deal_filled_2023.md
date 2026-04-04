# `deal_filled_2023`

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
| 2 | 2 | 100000 | 109130 | 1 | 1 | 2023-08-16 11:41:06.354000 | 1.0913 | 2 | 1 | 2 | 100000 | 109128 | 109128 | 2023-08-16 11:41:06.592000 | NULL | 2 | True | 0 | 0 | [REDACTED] | 66 | 2 | NULL | 109128 | 0 | 0 | 0 | NULL | 0 | 0 | 10000000 | True | 218410 | False | NULL | 0 | 0 | 0 | NULL | False | NULL | 1.0913 | 1021 | 100000 | 85655 | False |
| 1 | 1 | 100000 | NULL | 2 | 1 | 2023-08-16 09:30:19.510000 | 1.0928 | 2 | 1 | 2 | 100000 | 109280 | 109280 | 2023-08-16 09:30:19.745000 | NULL | 1 | True | 0 | 0 | [REDACTED] | 66 | 1 | NULL | 109280 | 0 | 0 | 0 | NULL | 0 | 0 | 10000000 | True | 109280 | False | NULL | 109280 | 0 | 0 | NULL | False | NULL | 1.0928 | 1021 | 100000 | 85642 | False |
| 5 | 5 | 100000 | NULL | 2 | 1 | 2023-08-18 11:37:38.717000 | 1.08616 | 2 | 3 | 2 | 100000 | 108616 | 108616 | 2023-08-18 11:37:38.955000 | NULL | 1 | True | 2 | 0 | [REDACTED] | 66 | 5 | NULL | 108616 | 0 | 0 | 0 | NULL | 0 | 0 | 10000000 | True | 217232 | False | NULL | 108616 | 0 | 0 | NULL | False | NULL | 1.08616 | 1022 | 100000 | 85477 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
