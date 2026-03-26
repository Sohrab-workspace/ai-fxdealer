---
name: mt5-integration
description: MT5 Manager API integration for AI FXDealer collector service.
  Use when building or modifying the MT5 collector, connecting to MT5 server,
  fetching MT5 entities (deals, orders, positions, accounts, users, symbols,
  groups, ticks, server logs, balance operations, margin events, online sessions),
  implementing MT5Manager Python methods, handling MT5 connection or return codes,
  designing raw_mt5_* database schemas, or writing any code that interacts with
  a MetaTrader 5 server via the Manager API.
allowed-tools: [Read, Write, Edit, Bash, Grep]
---

# MT5 Integration Skill

## Critical context — read this first

AI FXDealer uses the **MT5Manager pip package** (official MetaQuotes Python SDK)
to connect to MT5 servers as a manager — NOT as a trading account.

Install: `pip install MT5Manager`
PyPI: https://pypi.org/project/mt5manager/

This is a collector service. Its only job:
1. Connect to MT5 server with manager credentials
2. Fetch raw entity data exactly as returned
3. Store in raw_mt5_* tables with payload_json preserved
4. Never transform, normalize, or interpret data in the collector

Runs on a **Windows EC2 instance** — MT5Manager is Windows-only (win_amd64 wheel).
One collector instance per broker per MT5 server.

---

## ⚠️ Primary reference — use these FIRST

These are real API calls made against a live MT5 server with actual response
fields, example code, and error handling already documented. Always read the
relevant file here BEFORE writing any collector code or designing any schema.

```
.claude/references/mt5-endpoint/README.md          ← start here for overview
```

### Entity → real response file mapping

| Entity / Task | Real response file |
|---|---|
| Users / accounts — get single | .claude/references/mt5-endpoint/01_user_get.md |
| Users — get by group | .claude/references/mt5-endpoint/02_user_get_by_group.md |
| Users — bulk request | .claude/references/mt5-endpoint/03_user_request.md |
| User account (balance/margin) — get | .claude/references/mt5-endpoint/03b_user_account_get.md |
| User account — request | .claude/references/mt5-endpoint/03c_user_account_request.md |
| Deals — request | .claude/references/mt5-endpoint/04_deal_request.md |
| Deals — request by group | .claude/references/mt5-endpoint/04b_deal_request_by_group.md |
| Deals — balance operations | .claude/references/mt5-endpoint/04d_dealer_balance.md |
| Positions — get by group | .claude/references/mt5-endpoint/05_position_get_by_group.md |
| Positions — get by logins | .claude/references/mt5-endpoint/05b_position_get_by_logins.md |
| Positions — request | .claude/references/mt5-endpoint/05c_position_request.md |
| Positions — request by group | .claude/references/mt5-endpoint/05d_position_request_by_group.md |
| Orders (open) — get by group | .claude/references/mt5-endpoint/06_order_get_by_group.md |
| Orders — get by logins | .claude/references/mt5-endpoint/06b_order_get_by_logins.md |
| Orders — request open | .claude/references/mt5-endpoint/06c_order_request_open.md |
| History (closed orders) — request | .claude/references/mt5-endpoint/07_history_request.md |
| History — request by group | .claude/references/mt5-endpoint/07b_history_request_by_group.md |
| Symbols — get array | .claude/references/mt5-endpoint/08_symbol_get_array.md |
| Symbols — get single | .claude/references/mt5-endpoint/08b_symbol_get.md |
| Symbols — request | .claude/references/mt5-endpoint/08c_symbol_request.md |
| Symbols — request array | .claude/references/mt5-endpoint/08d_symbol_request_array.md |
| Groups — request array | .claude/references/mt5-endpoint/09_group_request_array.md |
| Groups — request | .claude/references/mt5-endpoint/09b_group_request.md |
| Ticks — last tick | .claude/references/mt5-endpoint/10_tick_last.md |
| Ticks — tick stat | .claude/references/mt5-endpoint/10b_tick_stat.md |
| Ticks — history request | .claude/references/mt5-endpoint/10c_tick_history_request.md |
| Summary — get all | .claude/references/mt5-endpoint/11_summary_get_all.md |
| Exposure — get all | .claude/references/mt5-endpoint/12_exposure_get_all.md |
| Daily reports — request | .claude/references/mt5-endpoint/13_daily_request.md |
| Daily reports — by group | .claude/references/mt5-endpoint/13b_daily_request_by_group.md |
| Online sessions — get array | .claude/references/mt5-endpoint/14_online_get_array.md |
| News | .claude/references/mt5-endpoint/15_news.md |
| Clients — request by group | .claude/references/mt5-endpoint/16_client_request_by_group.md |
| Book (DOM) — get | .claude/references/mt5-endpoint/17_book_get.md |
| Trade profit calculation | .claude/references/mt5-endpoint/18b_trade_profit.md |
| Trade margin check | .claude/references/mt5-endpoint/18_trade_margin_check.md |
| User add / update | .claude/references/mt5-endpoint/19_user_add_update.md |
| User password change | .claude/references/mt5-endpoint/20_user_password_change.md |
| Request get | .claude/references/mt5-endpoint/21_request_get.md |
| Leverage get | .claude/references/mt5-endpoint/22_leverage_get.md |
| Spread | .claude/references/mt5-endpoint/23_spread.md |
| Holiday | .claude/references/mt5-endpoint/24_holiday.md |
| Server time | .claude/references/mt5-endpoint/25_time_server.md |

---

## Secondary reference — MT5 API docs

Use these only if the real response file above doesn't answer your question.

```
.claude/references/mql5/API/managerapi_python.md     ← Python SDK overview
.claude/references/mql5/API/ManagerAPI.md            ← Manager API overview
.claude/references/mql5/API/managerapi_best_practice.md
.claude/references/mql5/API/getting_started.md
.claude/references/mql5/API/reference_retcodes.md    ← all return codes
.claude/references/mql5/API/retcodes_common.md
.claude/references/mql5/API/retcodes_successful.md
.claude/references/mql5/API/retcodes_trades.md
.claude/references/mql5/API/retcodes_authentication.md
```

## ⚠️ Sections to IGNORE in mql5 docs

```
.claude/references/mql5/client/        ← trading terminal user guide
.claude/references/mql5/android/       ← mobile app
.claude/references/mql5/iphone/        ← mobile app
.claude/references/mql5/metaeditor/    ← MQL5 scripting IDE
.claude/references/mql5/platform/      ← server admin/installation
.claude/references/mql5/manager/       ← manager desktop UI
.claude/references/mql5/Administrator/ ← administrator desktop UI
.claude/references/mql5/Gateway/       ← gateway component
```

---

## Raw schema design rule — CRITICAL

**Always design raw_mt5_* table columns from the real response files, not from
the API docs or imagination.**

```
1. Read the real response file for the entity
2. Note every field returned in the actual response
3. Extract top-level fields as indexed columns
4. Keep full response in payload_json
5. Save a sample to tests/fixtures/mt5/{entity}.json
```

### Raw table minimum columns

```sql
id               UUID PRIMARY KEY DEFAULT gen_random_uuid()
broker_id        UUID NOT NULL
server_id        UUID NOT NULL
external_id      VARCHAR          -- MT5's own ID for the record
payload_json     JSONB NOT NULL   -- full raw response, never modified
collected_at     TIMESTAMPTZ NOT NULL
source_timestamp TIMESTAMPTZ      -- MT5's own timestamp if available
ingestion_hash   VARCHAR          -- SHA256 for deduplication
status           VARCHAR NOT NULL DEFAULT 'active'
created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
```

---

## Entities → raw tables → sync mode

| Entity | Raw table | Sync mode |
|---|---|---|
| Users / Accounts | raw_mt5_accounts | Bootstrap + incremental |
| Deals | raw_mt5_deals | Bootstrap + incremental (timestamp cursor) |
| Orders (open) | raw_mt5_orders | Bootstrap + incremental |
| Positions | raw_mt5_positions | Incremental snapshot |
| Symbols | raw_mt5_symbols | Bootstrap + daily refresh |
| Groups | raw_mt5_groups | Bootstrap + daily refresh |
| Ticks | raw_mt5_ticks | Incremental real-time |
| Server logs / journal | raw_mt5_server_logs | Incremental |
| Online sessions | raw_mt5_server_logs | Incremental |
| Daily reports | raw_mt5_server_logs | Daily |

---

## BaseCollector implementation pattern

```python
import MT5Manager
import structlog
from packages.shared.base_collector import BaseCollector

log = structlog.get_logger()

class MT5Collector(BaseCollector):

    def __init__(self, broker_id, server_id, connection_id,
                 host, login, password):
        self.broker_id = broker_id
        self.server_id = server_id
        self.connection_id = connection_id
        self.host = host
        self.login = login
        self.password = password
        self.manager = None
        self.status = "disconnected"
        self.cursor = None
        self.last_success_at = None

    def connect(self) -> None:
        # Read before implementing:
        # .claude/references/mql5/API/managerapi_python.md
        self.manager = MT5Manager.ManagerAPI()
        result = self.manager.Connect(self.host, self.login, self.password)
        if result != MT5Manager.MTRetCode.MT_RET_OK:
            raise ConnectionError(f"MT5 connect failed: {result}")
        self.status = "connected"
        log.info("mt5.connected",
            broker_id=str(self.broker_id),
            server_id=str(self.server_id),
            host=self.host)
```

---

## Error handling

Retry policy:
```
Attempt 1: immediate
Attempt 2: wait 5 seconds
Attempt 3: wait 30 seconds
After 3 failures: circuit_open, alert Sentry, stop for 10 minutes
```

Never log or expose credentials. Never crash on a single entity failure.
Always log to raw_collector_errors on any fetch failure.

---

## Windows deployment

MT5Manager is Windows-only. collector-mt5 runs on Windows EC2.
Credentials loaded from AWS Secrets Manager at startup — never hardcoded.

---

## What NOT to do

```
- Never use MetaTrader5 pip package — that is the terminal client
- Never design schemas without reading the real response files first
- Never transform or normalize data before saving raw
- Never advance cursor past failed records
- Never call MT5Manager from frontend or API service
- Never hardcode credentials
- Never read from mql5/client/, mql5/manager/, or other non-API folders
```

---

## Reference implementations (fill as built)

```
services/collector-mt5/collector.py   ← main collector class
services/collector-mt5/ingestion.py   ← raw save logic
services/collector-mt5/tests/         ← unit tests with mocked MT5Manager
tests/fixtures/mt5/                   ← real captured MT5 payloads per entity
```
