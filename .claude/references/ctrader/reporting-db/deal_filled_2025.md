# `deal_filled_2025`

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
| 158210 | 193551 | 10 | NULL | 2 | 115 | 2025-07-11 00:56:01.363000 | 22685.0 | 2 | 86383 | 2 | 10 | 2268299000 | 2268300000 | 2025-07-11 00:56:01.626000 | NULL | 1 | True | 2 | 0 | [REDACTED] | 66 | 145316 | NULL | 2268300000 | 0 | 0 | 0 | NULL | 0 | 0 | 1000 | True | 2484309307 | False | NULL | 0 | 0 | 0 | NULL | False | NULL | 22685.0 | 3180 | 194422 | 167438 | False |
| 102268 | 126932 | 200000 | NULL | 1 | 1 | 2025-01-02 00:12:30.169000 | 1.03505 | 2 | 54127 | 2 | 200000 | 103509 | 103505 | 2025-01-02 00:12:30.438000 | NULL | 1 | True | 6 | 0 | [REDACTED] | 66 | 92476 | NULL | 103505 | 0 | 0 | 0 | NULL | 0 | 8 | 10000000 | True | 43238435 | False | NULL | 103509 | 0 | 0 | NULL | False | NULL | 1.03505 | 2798 | 200000 | 165424 | False |
| 102273 | 126927 | 100 | NULL | 2 | 115 | 2025-01-02 00:16:52.537000 | 20956.03 | 2 | 54139 | 2 | 100 | 2095727000 | 2095778000 | 2025-01-02 00:16:52.738000 | NULL | 1 | True | 30 | 0 | [REDACTED] | 66 | 92481 | NULL | 2095778000 | 0 | 0 | 0 | NULL | 0 | 51 | 1000 | True | 6075913944 | False | NULL | 2095759000 | 0 | 0 | NULL | False | NULL | 20956.03 | 2034 | 2024796 | 1674714 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
