# `close_position_detail`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `close_position_detail_id` | bigint | NO |  |  |
| `entry_price` | double precision | NO |  |  |
| `stop_loss` | bigint | YES |  |  |
| `take_profit` | bigint | YES |  |  |
| `balance_history_id` | bigint | NO |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `deal_id` | bigint | NO |  |  |
| `quote_to_deposit_conv_rate` | double precision | YES |  |  |
| `closed_volume` | bigint | NO |  |  |
| `swap` | bigint | NO | 0 |  |
| `commission` | bigint | NO | 0 |  |
| `ib_commission` | bigint | NO | 0 |  |
| `pocket_commission` | bigint | NO | 0 |  |
| `pocket_markup` | bigint | NO | 0 |  |
| `mirroring_commission` | bigint | NO | 0 |  |
| `deposit_to_ib_deposit_rate` | double precision | NO | 0 |  |
| `usd_to_ib_deposit_rate` | double precision | NO | 0 |  |
| `ib_commissions_paid` | boolean | YES |  |  |
| `rebate` | bigint | NO | 0 |  |
| `markup` | bigint | NO | 0 |  |
| `rebates_paid` | boolean | NO | false |  |
| `closed_stake` | bigint | NO | 0 |  |
| `equity_based_roi` | double precision | NO | 0 |  |
| `offset_deal_timestamp` | timestamp without time zone | YES |  |  |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |
| `pnl_conversion_fee` | bigint | NO | 0 |  |
| `parent_ib_id` | bigint | YES |  |  |

## Sample Data

| `close_position_detail_id` | `entry_price` | `stop_loss` | `take_profit` | `balance_history_id` | `create_timestamp` | `deal_id` | `quote_to_deposit_conv_rate` | `closed_volume` | `swap` | `commission` | `ib_commission` | `pocket_commission` | `pocket_markup` | `mirroring_commission` | `deposit_to_ib_deposit_rate` | `usd_to_ib_deposit_rate` | `ib_commissions_paid` | `rebate` | `markup` | `rebates_paid` | `closed_stake` | `equity_based_roi` | `offset_deal_timestamp` | `is_precise_money` | `pnl_conversion_fee` | `parent_ib_id` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1.0928 | 109289 | 109130 | 2 | 2023-08-16 11:41:06.672000 | 2 | 1.0 | 100000 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | NULL | 0 | 0 | False | 0 | 0.0015199999999999658 | 2023-08-16 09:30:19.745000 | False | 0 | NULL |
| 2 | 1.08617 | NULL | NULL | 4 | 2023-08-18 11:37:38.982000 | 5 | 1.0 | 100000 | 0 | 4 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | NULL | 0 | 0 | False | 0 | -5.000000000032756e-06 | 2023-08-18 11:37:10.813000 | False | 0 | NULL |
| 3 | 1.08612 | NULL | NULL | 5 | 2023-08-18 11:38:34.039000 | 7 | 1.0 | 100000 | 0 | 4 | 0 | 0 | 0 | 0 | 0.0 | 0.0 | NULL | 0 | 0 | False | 0 | -1.2000000000012001e-05 | 2023-08-18 11:38:02.824000 | False | 0 | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
