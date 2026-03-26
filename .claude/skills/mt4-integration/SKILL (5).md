---
name: mt4-integration
description: MT4 Manager API integration for AI FXDealer collector service.
  Use when building or modifying the MT4 collector, connecting to MT4 server
  via the Manager API DLL, fetching MT4 entities (trades, orders, accounts,
  users, symbols, groups, ticks, server logs, balance operations, margin events,
  online sessions, pumping mode), implementing ctypes DLL wrapper, handling MT4
  return codes, defining ctypes structures, designing raw_mt4_* database schemas,
  or writing any code that talks to a MetaTrader 4 server via the Manager API DLL.
allowed-tools: [Read, Write, Edit, Bash, Grep]
---

# MT4 Integration Skill

## Critical context — read this first

AI FXDealer connects to MT4 servers using the **MT4 Manager API DLL**
via a Python `ctypes` wrapper. There is no pip package for MT4.

The DLL is a C++ library provided by MetaQuotes to licensed brokers.
Each broker provides their own DLL from their MT4 Server installation.
The DLL path is loaded from AWS Secrets Manager per broker — never hardcoded.

This is a collector service. Its only job:
1. Load the broker-provided DLL via ctypes
2. Connect to MT4 server with manager credentials
3. Fetch raw entity data exactly as returned by the DLL
4. Store in raw_mt4_* tables with payload_json preserved
5. Never transform, normalize, or interpret data

Runs on a **Windows EC2 instance** — the MT4 DLL is Windows-only.
One collector instance per broker per MT4 server.

---

## ⚠️ Primary reference — use these FIRST

These are real API calls made against a live MT4 server with actual response
fields, example code, and error handling already documented. Always read the
relevant file here BEFORE writing any collector code or designing any schema.

```
.claude/references/mt4-endpoint/README.md              ← start here
.claude/references/mt4-endpoint/_connection_setup.md   ← connection setup
```

### Entity → real response file mapping

| Entity / Task | Real response file |
|---|---|
| Server time | .claude/references/mt4-endpoint/00_server_time.md |
| Connection overview | .claude/references/mt4-endpoint/01_connection.md |
| Connect + login | .claude/references/mt4-endpoint/01_connect_login.md |
| Users — bulk request | .claude/references/mt4-endpoint/02_users_request.md |
| User record — structure | .claude/references/mt4-endpoint/02_user_record.md |
| User record — live response | .claude/references/mt4-endpoint/02_user_record_live.md |
| Trades (open orders) | .claude/references/mt4-endpoint/03_trades_open.md |
| Trade record — structure | .claude/references/mt4-endpoint/03_trade_record.md |
| Trade record — live response | .claude/references/mt4-endpoint/03_trade_record_live.md |
| Margin level | .claude/references/mt4-endpoint/04_margin_level.md |
| Margin level — live response | .claude/references/mt4-endpoint/04_margin_level_live.md |
| Trades history (closed) | .claude/references/mt4-endpoint/04_trades_history.md |
| Online record — structure | .claude/references/mt4-endpoint/05_online_record.md |
| Online record — live response | .claude/references/mt4-endpoint/05_online_record_live.md |
| Symbols list | .claude/references/mt4-endpoint/05_symbols.md |
| Groups list | .claude/references/mt4-endpoint/06_groups.md |
| Symbol info — structure | .claude/references/mt4-endpoint/06_symbol_info.md |
| Symbol info — live response | .claude/references/mt4-endpoint/06_symbol_info_live.md |
| Server logs / journal | .claude/references/mt4-endpoint/07_server_logs.md |
| Summary + exposure overview | .claude/references/mt4-endpoint/07_summary_exposure.md |
| Summary — live response | .claude/references/mt4-endpoint/07_summary_live.md |
| Chart request — live | .claude/references/mt4-endpoint/08_chart_request_live.md |
| Chart + ticks overview | .claude/references/mt4-endpoint/08_chart_ticks.md |
| Online sessions | .claude/references/mt4-endpoint/08_online_sessions.md |
| Ticks — live request | .claude/references/mt4-endpoint/08b_ticks_request_live.md |
| Daily reports | .claude/references/mt4-endpoint/09_daily_reports.md |
| Exposure | .claude/references/mt4-endpoint/09_exposure.md |
| Reports — live request | .claude/references/mt4-endpoint/09_reports_request_live.md |
| Margin | .claude/references/mt4-endpoint/10_margin.md |
| News + mail | .claude/references/mt4-endpoint/10_news_mail.md |
| Groups config | .claude/references/mt4-endpoint/11_groups_config.md |
| Summary | .claude/references/mt4-endpoint/11_summary.md |
| Journal — live request | .claude/references/mt4-endpoint/12_journal_request_live.md |
| Reports | .claude/references/mt4-endpoint/12_reports.md |
| Server journal | .claude/references/mt4-endpoint/12_server_journal.md |
| Ticks | .claude/references/mt4-endpoint/13_ticks.md |
| Trade transaction | .claude/references/mt4-endpoint/13_trade_transaction.md |
| Pumping mode (real-time events) | .claude/references/mt4-endpoint/14_pumping_mode.md |
| Backup | .claude/references/mt4-endpoint/15_backup.md |

---

## Secondary reference — MT4 API docs

Use these only if the real response file above doesn't answer your question.

```
.claude/references/mql4/API/ManagerAPI.md
.claude/references/mql4/API/ManagerAPI/manager_api_dev.md
.claude/references/mql4/API/ManagerAPI/manager_api_connect.md
.claude/references/mql4/API/ManagerAPI/manager_api_exported_factory.md
.claude/references/mql4/API/ManagerAPI/manager_api_user.md
.claude/references/mql4/API/ManagerAPI/manager_api_trade.md
.claude/references/mql4/API/ManagerAPI/manager_api_symbol.md
.claude/references/mql4/API/ManagerAPI/manager_api_config.md
.claude/references/mql4/API/ManagerAPI/manager_api_feeder.md
.claude/references/mql4/API/ManagerAPI/manager_api_online.md
.claude/references/mql4/API/ManagerAPI/manager_api_server.md
.claude/references/mql4/API/reference_structures/structure_trade.md
.claude/references/mql4/API/reference_structures/structure_user.md
.claude/references/mql4/API/reference_structures/structure_symbol.md
.claude/references/mql4/API/reference_structures/structure_price.md
.claude/references/mql4/API/reference_structures/structure_config.md
.claude/references/mql4/API/reference_structures/structure_report.md
.claude/references/mql4/API/reference_structures/structure_journal.md
.claude/references/mql4/API/reference_retcodes/retcodes_common.md
.claude/references/mql4/API/reference_retcodes/retcodes_successful.md
.claude/references/mql4/API/reference_retcodes/retcodes_trade_request.md
```

## ⚠️ Sections to IGNORE in mql4 docs

```
.claude/references/mql4/Terminal/        ← trading terminal user guide
.claude/references/mql4/metaeditor/      ← MQL4 scripting IDE
.claude/references/mql4/multiterminal/   ← multi-terminal user guide
.claude/references/mql4/Administrator/   ← server admin UI
.claude/references/mql4/manager/         ← manager desktop UI
```

---

## Raw schema design rule — CRITICAL

**Always design raw_mt4_* table columns from the real response files, not from
the API docs or imagination.**

```
1. Read the real response file for the entity (live response version)
2. Note every field in the actual response
3. Extract top-level fields as indexed columns
4. Keep full response in payload_json
5. Save a sample to tests/fixtures/mt4/{entity}.json
```

### Which file to read per table

| Raw table | Read this real response file first |
|---|---|
| raw_mt4_accounts | 02_user_record_live.md |
| raw_mt4_orders (open) | 03_trades_open.md + 03_trade_record_live.md |
| raw_mt4_deals (closed) | 04_trades_history.md + 03_trade_record_live.md |
| raw_mt4_symbols | 06_symbol_info_live.md |
| raw_mt4_groups | 06_groups.md + 11_groups_config.md |
| raw_mt4_ticks | 08b_ticks_request_live.md |
| raw_mt4_server_logs | 12_journal_request_live.md |
| raw_mt4_online | 05_online_record_live.md |
| raw_mt4_margin | 04_margin_level_live.md |
| raw_mt4_summary | 07_summary_live.md |

### Raw table minimum columns

```sql
id               UUID PRIMARY KEY DEFAULT gen_random_uuid()
broker_id        UUID NOT NULL
server_id        UUID NOT NULL
external_id      VARCHAR          -- MT4's own ID (login, ticket, etc.)
payload_json     JSONB NOT NULL   -- full raw response, never modified
collected_at     TIMESTAMPTZ NOT NULL
source_timestamp TIMESTAMPTZ      -- MT4's own timestamp if available
ingestion_hash   VARCHAR          -- SHA256 for deduplication
status           VARCHAR NOT NULL DEFAULT 'active'
created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW()
```

---

## Entities → raw tables → sync mode

| Entity | Raw table | Sync mode |
|---|---|---|
| Users / Accounts | raw_mt4_accounts | Bootstrap + incremental |
| Open orders | raw_mt4_orders | Bootstrap + incremental |
| Trade history (closed) | raw_mt4_deals | Bootstrap + incremental |
| Symbols | raw_mt4_symbols | Bootstrap + daily refresh |
| Groups | raw_mt4_groups | Bootstrap + daily refresh |
| Ticks | raw_mt4_ticks | Incremental real-time |
| Server logs | raw_mt4_server_logs | Incremental |
| Online sessions | raw_mt4_server_logs | Incremental |

Note: In MT4, "deals" = closed TradeRecords, "orders" = open TradeRecords.
Stored separately for consistency with MT5 naming.

---

## MT4 vs MT5 — key difference

```
MT5 → pip install MT5Manager → Python methods directly
MT4 → load DLL via ctypes   → call C functions → parse C structs
```

---

## DLL loading + connection pattern

```python
import ctypes
import structlog
from packages.shared.base_collector import BaseCollector

log = structlog.get_logger()

class MT4Collector(BaseCollector):

    def __init__(self, broker_id, server_id, connection_id,
                 dll_path, host, port, login, password):
        self.broker_id = broker_id
        self.server_id = server_id
        self.connection_id = connection_id
        self.dll_path = dll_path  # from AWS Secrets Manager
        self.host = host
        self.port = port
        self.login = login
        self.password = password
        self.lib = None
        self.manager = None
        self.status = "disconnected"

    def connect(self) -> None:
        # Read before implementing:
        # .claude/references/mt4-endpoint/01_connect_login.md
        # .claude/references/mt4-endpoint/_connection_setup.md
        # .claude/references/mql4/API/ManagerAPI/manager_api_exported_factory.md
        self.lib = ctypes.WinDLL(self.dll_path)
        create_manager = self.lib.CreateManager
        create_manager.restype = ctypes.c_void_p
        self.manager = create_manager()
        # Connect — exact method in 01_connect_login.md
        ...
        self.status = "connected"
        log.info("mt4.connected",
            broker_id=str(self.broker_id),
            server_id=str(self.server_id),
            host=self.host)
```

---

## ctypes struct to dict helper

```python
def struct_to_dict(struct_instance) -> dict:
    result = {}
    for field_name, field_type in struct_instance._fields_:
        value = getattr(struct_instance, field_name)
        if isinstance(value, bytes):
            value = value.decode('utf-8', errors='replace').rstrip('\x00')
        result[field_name] = value
    return result
```

## C++ to ctypes type mapping

```
int       → c_int        double    → c_double
char[N]   → c_char * N   __int64   → c_int64
DWORD     → c_uint32     WORD      → c_uint16
time_t    → c_int64      bool      → c_bool
void*     → c_void_p
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

Never log or expose credentials. Never crash on single entity failure.
Always log to raw_collector_errors on any fetch failure.

---

## DLL path configuration

```python
import boto3, json

def get_mt4_config(broker_id: str) -> dict:
    client = boto3.client('secretsmanager')
    secret = client.get_secret_value(
        SecretId=f"fxdealer/broker/{broker_id}/mt4"
    )
    return json.loads(secret['SecretString'])
    # { "dll_path": "...", "host": "...", "port": 443,
    #   "login": 1234, "password": "..." }
```

---

## What NOT to do

```
- Never call the MT4 DLL from frontend or API service
- Never hardcode DLL paths or credentials
- Never design schemas without reading the live response files first
- Never guess ctypes struct field sizes or types
- Never transform data before saving to raw tables
- Never advance cursor past failed records
- Never commit DLL files or credentials to git
- Never mix MT4 and MT5 collector code
- Never read from mql4/Terminal/, mql4/manager/, or other non-API folders
```

---

## Reference implementations (fill as built)

```
services/collector-mt4/collector.py   ← main collector class
services/collector-mt4/structs.py     ← ctypes structure definitions
services/collector-mt4/ingestion.py   ← raw save logic
services/collector-mt4/tests/         ← unit tests with mocked DLL
tests/fixtures/mt4/                   ← real captured MT4 payloads per entity
```
