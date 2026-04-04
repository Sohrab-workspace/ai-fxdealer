# `balance_history`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `balance_history_id` | bigint | NO |  |  |
| `trader_id` | bigint | NO |  |  |
| `delta` | bigint | NO |  |  |
| `balance` | bigint | NO |  |  |
| `operation_type` | integer | NO |  | DEPOSIT(0), WITHDRAW(1), CLOSE_POSITION(2), DEPOSIT_STRATEGY_COMMISSION_INNER(3),
            WITHDRAW_STRATEGY_COMMISSION_INNER(4), DEPOSIT_IB_COMMISSIONS(5), WITHDRAW_IB_SHARED_PERCENTAGE(6), DEPOSIT_IB_SHARED_PERCENTAGE_FROM_SUB_IB(7),
            DEPOSIT_IB_SHARED_PERCENTAGE_FROM_BROKER(8), DEPOSIT_REBATE(9), WITHDRAW_REBATE(10), DEPOSIT_STRATEGY_COMMISSION_OUTER(11),
            WITHDRAW_STRATEGY_COMMISSION_OUTER(12), WITHDRAW_BONUS_COMPENSATION(13), WITHDRAW_IB_SHARED_PERCENTAGE_TO_BROKER(14),
            DEPOSIT_DIVIDENDS(15), WITHDRAW_DIVIDENDS(16), WITHDRAW_GSL_CHARGE(17), WITHDRAW_ROLLOVER(18), DEPOSIT_NONWITHDRAWABLE_BONUS(19),
            WITHDRAW_NONWITHDRAWABLE_BONUS(20), BALANCE_DEPOSIT_SWAP(21), BALANCE_WITHDRAW_SWAP(22), BALANCE_WITHDRAW_INVESTMENT_TO_STRATEGY(23),
            BALANCE_DEPOSIT_FROM_INVESTOR(24), BALANCE_DEPOSIT_RETURNED_INVESTMENT(25), BALANCE_WITHDRAW_BY_INVESTOR(26),
            BALANCE_DEPOSIT_MANAGEMENT_FEE(27), BALANCE_WITHDRAW_MANAGEMENT_FEE(28), BALANCE_DEPOSIT_PERFORMANCE_FEE(29),
            BALANCE_WITHDRAW_FOR_SUBACCOUNT(30), BALANCE_DEPOSIT_TO_SUBACCOUNT(31),
            BALANCE_WITHDRAW_FROM_SUBACCOUNT(32), BALANCE_DEPOSIT_FROM_SUBACCOUNT(33), BALANCE_WITHDRAW_COPY_FEE(34),
            BALANCE_WITHDRAW_INACTIVITY_FEE(35), BALANCE_DEPOSIT_TRANSFER(36), BALANCE_WITHDRAW_TRANSFER(37), BALANCE_DEPOSIT_CONVERTED_BONUS(38),
            BALANCE_DEPOSIT_NEGATIVE_BALANCE_PROTECTION(39), RESERVED_1(40), RESERVED_2(41), RESERVED_3(42) |
| `description` | character varying | YES |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `utc_last_update_datetime` | timestamp without time zone | NO | timezone('utc'::text, now()) |  |
| `external_note` | character varying | YES |  |  |
| `balance_version` | bigint | NO |  |  |
| `equity` | bigint | NO | 0 |  |
| `min_equity` | bigint | NO | 0 |  |
| `max_equity` | bigint | NO | 0 |  |
| `nonwithdrawable_bonus` | bigint | NO | 0 |  |
| `source` | character varying | YES |  |  |
| `external_id` | character varying | YES |  |  |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |
| `asset_to_usd_rate` | double precision | YES |  |  |

## Sample Data

| `balance_history_id` | `trader_id` | `delta` | `balance` | `operation_type` | `description` | `create_timestamp` | `utc_last_update_datetime` | `external_note` | `balance_version` | `equity` | `min_equity` | `max_equity` | `nonwithdrawable_bonus` | `source` | `external_id` | `is_precise_money` | `asset_to_usd_rate` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1021 | 152 | 100152 | 2 | positionEntity id 1 | 2023-08-16 11:41:06.668000 | [REDACTED] | NULL | 3 | 100152 | 99972 | 100152 | 0 | NULL | NULL | False | 1.0 |
| 4 | 1022 | -5 | 999995 | 2 | positionEntity id 3 | 2023-08-18 11:37:38.980000 | [REDACTED] | NULL | 3 | 999995 | 999989 | 1000000 | 0 | NULL | NULL | False | 1.0 |
| 5 | 1022 | -7 | 999988 | 2 | positionEntity id 4 | 2023-08-18 11:38:34.037000 | [REDACTED] | NULL | 4 | 999988 | 999986 | 999995 | 0 | NULL | NULL | False | 1.0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
