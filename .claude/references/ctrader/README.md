# cTrader Reporting DB — Reference

Source: OpoFinance cTrader Integration PDF (Appendix B + live schema capture)

## Connection

All connections route through stunnel (HTTP CONNECT proxy to `dbapi.ctrader.com:15220`).
Stunnel config: `C:\Program Files (x86)\stunnel\config\stunnel.conf`

| Environment | Host      | Port | Database          | User                    |
|-------------|-----------|------|-------------------|-------------------------|
| Demo        | localhost | 5432 | ctrader_spotware  | opofinance_demo_repo    |
| Live        | localhost | 5433 | ctrader_spotware  | opofinance_live_repo    |

> Access requires IP whitelisting — email `support@spotware.com` to add your static IP.

---

## Entity → Table Mapping

| Domain Entity      | Reporting DB Table        | Description                                               |
|--------------------|---------------------------|-----------------------------------------------------------|
| Accounts           | `trader`                  | Trading accounts; entity that places orders               |
| Assets             | `asset`                   | Tradable securities or other tangible/intangible resources |
| Deals              | `deal`                    | Execution attempts for orders; closing deals include P&L   |
| Orders             | `trade_order`             | Order details; references the associated position          |
| Positions          | `position`                | Open/closed position information                           |
| Groups             | `trader_group`            | Server groups aggregating accounts by custom criteria      |
| Symbols            | `symbol`                  | Symbol definitions and default configurations              |
| Transactions       | `balance_history`         | Balance operations: deposits, withdrawals, realized P&L    |
| Swaps              | `swap_calculation_event`  | Swap amounts attributed to open positions                  |
| EOD Open Positions | `daily_open_positions`    | End-of-day snapshot of open positions                      |
| EOD Spot Snapshot  | `daily_spot_snapshot`     | End-of-day spot price snapshot                             |
| EOD Trader Report  | `daily_traders_report`    | End-of-day financial snapshot per trader                   |

---

## Table Reference Files

> Schema files below are populated after live DB introspection.
> Run the capture script once IP whitelisting is confirmed.

| Table | File |
|-------|------|
| `trader` | [trader.md](reporting-db/trader.md) |
| `asset` | [asset.md](reporting-db/asset.md) |
| `deal` | [deal.md](reporting-db/deal.md) |
| `trade_order` | [trade_order.md](reporting-db/trade_order.md) |
| `position` | [position.md](reporting-db/position.md) |
| `trader_group` | [trader_group.md](reporting-db/trader_group.md) |
| `symbol` | [symbol.md](reporting-db/symbol.md) |
| `balance_history` | [balance_history.md](reporting-db/balance_history.md) |
| `swap_calculation_event` | [swap_calculation_event.md](reporting-db/swap_calculation_event.md) |
| `daily_open_positions` | [daily_open_positions.md](reporting-db/daily_open_positions.md) |
| `daily_spot_snapshot` | [daily_spot_snapshot.md](reporting-db/daily_spot_snapshot.md) |
| `daily_traders_report` | [daily_traders_report.md](reporting-db/daily_traders_report.md) |

---

## Notes

- Read-only replica of the primary cServer PostgreSQL database (near real-time)
- Data encoded as standard SQL types; no Protobuf encoding at DB level
- RabbitMQ real-time events available separately on ports 5672/5673 via same stunnel tunnel
- Reporting API (HTTP snapshots + events) available at `demo/live-opofinance.webapi.ctrader.com:8086`
