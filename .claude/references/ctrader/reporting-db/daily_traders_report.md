# `daily_traders_report`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `report_timestamp` | timestamp without time zone | NO |  |  |
| `login` | bigint | NO |  |  |
| `balance` | bigint | NO | 0 |  |
| `gross_unrealized_pnl_a` | bigint | NO | 0 |  |
| `net_unrealized_pnl_a` | bigint | NO | 0 |  |
| `gross_unrealized_pnl_b` | bigint | NO | 0 |  |
| `net_unrealized_pnl_b` | bigint | NO | 0 |  |
| `equity` | bigint | NO | 0 |  |
| `margin` | bigint | NO | 0 |  |
| `free_margin` | bigint | NO | 0 |  |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |
| `non_withdrawable_bonus` | bigint | NO | 0 |  |

## Sample Data

| `report_timestamp` | `login` | `balance` | `gross_unrealized_pnl_a` | `net_unrealized_pnl_a` | `gross_unrealized_pnl_b` | `net_unrealized_pnl_b` | `equity` | `margin` | `free_margin` | `is_precise_money` | `non_withdrawable_bonus` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2023-08-02 20:55:00.002000 | [REDACTED] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | False | 0 |
| 2023-08-03 20:55:00.005000 | [REDACTED] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | False | 0 |
| 2023-08-04 20:55:00.001000 | [REDACTED] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | False | 0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
