---
name: mt4-integration
description: MT4 Manager API integration for AI FXDealer collector service.
  Use when building or modifying the MT4 collector, connecting to MT4 server
  via the Manager API DLL, fetching MT4 entities (trades, orders, accounts,
  users, symbols, groups, ticks, server logs, balance operations, margin events,
  online sessions), implementing ctypes DLL wrapper, handling MT4 return codes,
  defining ctypes structures from MT4 C++ structs, designing raw_mt4_* database
  schemas, or writing any code that talks to a MetaTrader 4 server.
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

## ⚠️ Sections to IGNORE in the docs

These are for end-users, MQL4 scripting, or admin UI — NOT for your collector:
```
.claude/references/mql4/Terminal/        ← trading terminal user guide
.claude/references/mql4/metaeditor/      ← MQL4 scripting IDE
.claude/references/mql4/multiterminal/   ← multi-terminal user guide
.claude/references/mql4/Administrator/   ← server admin UI
.claude/references/mql4/manager/         ← manager desktop application UI
```

**Only read from `.claude/references/mql4/API/`**

---

## Documentation map — what to read for each task

### Connection and initialization

| Task | File |
|---|---|
| Overview of Manager API | .claude/references/mql4/API/ManagerAPI.md |
| Development guide / getting started | .claude/references/mql4/API/ManagerAPI/manager_api_dev.md |
| Common API patterns | .claude/references/mql4/API/ManagerAPI/manager_api_common.md |
| DLL factory / CreateManager function | .claude/references/mql4/API/ManagerAPI/manager_api_exported_factory.md |
| Connect / disconnect methods | .claude/references/mql4/API/ManagerAPI/manager_api_connect.md |
| Server info methods | .claude/references/mql4/API/ManagerAPI/manager_api_server.md |

### Users / Accounts

| Task | File |
|---|---|
| User methods (get, add, update) | .claude/references/mql4/API/ManagerAPI/manager_api_user.md |
| UserRecord C++ struct fields | .claude/references/mql4/API/reference_structures/structure_user.md |

### Trades / Orders / Deals

| Task | File |
|---|---|
| Trade methods (history, open) | .claude/references/mql4/API/ManagerAPI/manager_api_trade.md |
| TradeRecord C++ struct fields | .claude/references/mql4/API/reference_structures/structure_trade.md |

Note: In MT4, "deals" = closed trades (TradeRecord with state=closed).
Open orders = TradeRecord with state=open. Raw table is still named
`raw_mt4_deals` for consistency with MT5 naming.

### Symbols

| Task | File |
|---|---|
| Symbol methods | .claude/references/mql4/API/ManagerAPI/manager_api_symbol.md |
| SymbolInfo C++ struct fields | .claude/references/mql4/API/reference_structures/structure_symbol.md |

### Groups / Config

| Task | File |
|---|---|
| Config methods (groups, managers) | .claude/references/mql4/API/ManagerAPI/manager_api_config.md |
| ConGroup C++ struct fields | .claude/references/mql4/API/reference_structures/structure_config.md |

### Ticks / Price feed

| Task | File |
|---|---|
| Tick / feeder methods | .claude/references/mql4/API/ManagerAPI/manager_api_feeder.md |
| TickInfo C++ struct fields | .claude/references/mql4/API/reference_structures/structure_price.md |

### Online sessions / login activity

| Task | File |
|---|---|
| Online user methods | .claude/references/mql4/API/ManagerAPI/manager_api_online.md |

### Exposure / margin

| Task | File |
|---|---|
| Exposure methods | .claude/references/mql4/API/ManagerAPI/manager_api_exposure.md |

### Reports / summary

| Task | File |
|---|---|
| Summary methods | .claude/references/mql4/API/ManagerAPI/manager_api_summary.md |
| Report methods | .claude/references/mql4/API/ManagerAPI/manager_api_report.md |
| DailyReport C++ struct | .claude/references/mql4/API/reference_structures/structure_report.md |

### Server logs / journal

| Task | File |
|---|---|
| Server methods (logs, info) | .claude/references/mql4/API/ManagerAPI/manager_api_server.md |
| LogRecord C++ struct | .claude/references/mql4/API/reference_structures/structure_journal.md |

### Dealer operations (for future action layer)

| Task | File |
|---|---|
| Dealer methods | .claude/references/mql4/API/ManagerAPI/manager_api_dealer.md |
| Backup methods | .claude/references/mql4/API/ManagerAPI/manager_api_backup.md |

### Return codes / error handling

| Task | File |
|---|---|
| Common return codes | .claude/references/mql4/API/reference_retcodes/retcodes_common.md |
| Successful return codes | .claude/references/mql4/API/reference_retcodes/retcodes_successful.md |
| Trade request codes | .claude/references/mql4/API/reference_retcodes/retcodes_trade_request.md |
| Account codes | .claude/references/mql4/API/reference_retcodes/retcodes_account.md |
| All return codes overview | .claude/references/mql4/API/reference_retcodes.md |

### All C++ data structures

| Structure | File |
|---|---|
| TradeRecord | .claude/references/mql4/API/reference_structures/structure_trade.md |
| UserRecord | .claude/references/mql4/API/reference_structures/structure_user.md |
| SymbolInfo | .claude/references/mql4/API/reference_structures/structure_symbol.md |
| TickInfo / price | .claude/references/mql4/API/reference_structures/structure_price.md |
| ConGroup / config | .claude/references/mql4/API/reference_structures/structure_config.md |
| DailyReport | .claude/references/mql4/API/reference_structures/structure_report.md |
| LogRecord | .claude/references/mql4/API/reference_structures/structure_journal.md |
| Feed structures | .claude/references/mql4/API/reference_structures/structure_feed.md |
| Plugin structures | .claude/references/mql4/API/reference_structures/structure_plugin.md |
| News / mail structures | .claude/references/mql4/API/reference_structures/structure_news_mail.md |
| Auxiliary structures | .claude/references/mql4/API/reference_structures/structure_auxiliary.md |
| All structures overview | .claude/references/mql4/API/reference_structures.md |

---

## MT4 vs MT5 — key difference

```
MT5 → pip install MT5Manager → import MT5Manager → call Python methods
MT4 → load DLL via ctypes   → call C functions   → parse C structs in Python
```

---

## DLL loading pattern

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
        self.dll_path = dll_path      # loaded from AWS Secrets Manager
        self.host = host
        self.port = port
        self.login = login
        self.password = password
        self.lib = None
        self.manager = None
        self.status = "disconnected"

    def connect(self) -> None:
        # Read before implementing:
        # .claude/references/mql4/API/ManagerAPI/manager_api_exported_factory.md
        # .claude/references/mql4/API/ManagerAPI/manager_api_connect.md

        # Load the DLL
        self.lib = ctypes.WinDLL(self.dll_path)

        # Get factory function — exact name in manager_api_exported_factory.md
        create_manager = self.lib.CreateManager
        create_manager.restype = ctypes.c_void_p
        self.manager = create_manager()

        # Connect — exact method and params in manager_api_connect.md
        # result = self.manager.Connect(...)
        ...

        self.status = "connected"
        log.info("mt4.connected",
            broker_id=str(self.broker_id),
            server_id=str(self.server_id),
            host=self.host)
```

---

## ctypes structure pattern

**Read the structure doc BEFORE defining any ctypes struct.**

```python
import ctypes

# Before writing this — read:
# .claude/references/mql4/API/reference_structures/structure_trade.md
class TradeRecord(ctypes.Structure):
    _fields_ = [
        # Copy exact field names and C++ types from the structure doc
        # Never guess field names or sizes
    ]
```

### C++ to ctypes type mapping

```
int           → ctypes.c_int
unsigned int  → ctypes.c_uint
long          → ctypes.c_long
double        → ctypes.c_double
float         → ctypes.c_float
char[N]       → ctypes.c_char * N
wchar_t[N]    → ctypes.c_wchar * N
__int64       → ctypes.c_int64
DWORD         → ctypes.c_uint32
WORD          → ctypes.c_uint16
BYTE          → ctypes.c_uint8
time_t        → ctypes.c_int64
bool          → ctypes.c_bool
void*         → ctypes.c_void_p
```

### ctypes struct to dict helper

```python
def struct_to_dict(struct_instance) -> dict:
    """Convert ctypes Structure to plain Python dict for storage."""
    result = {}
    for field_name, field_type in struct_instance._fields_:
        value = getattr(struct_instance, field_name)
        if isinstance(value, bytes):
            value = value.decode('utf-8', errors='replace').rstrip('\x00')
        result[field_name] = value
    return result
```

---

## Entities to collect and their raw tables

| Entity | Raw table | Sync mode | Key doc |
|---|---|---|---|
| Users / Accounts | raw_mt4_accounts | Bootstrap + incremental | manager_api_user.md |
| Open orders | raw_mt4_orders | Bootstrap + incremental | manager_api_trade.md |
| Trade history (closed) | raw_mt4_deals | Bootstrap + incremental | manager_api_trade.md |
| Symbols | raw_mt4_symbols | Bootstrap + daily refresh | manager_api_symbol.md |
| Groups | raw_mt4_groups | Bootstrap + daily refresh | manager_api_config.md |
| Ticks | raw_mt4_ticks | Incremental real-time | manager_api_feeder.md |
| Server logs | raw_mt4_server_logs | Incremental | manager_api_server.md |

Note: MT4 "deals" = closed TradeRecords. MT4 "orders" = open TradeRecords.
Stored separately for consistency with MT5 naming convention.

---

## Raw schema design rule

**Do not design raw_mt4_* schemas without reading the C++ struct docs first.**

Process:
```
1. Read the structure doc for the entity
2. Connect to MT4 test server
3. Call fetch method and inspect actual returned struct
4. Use struct_to_dict() to convert to Python dict
5. Print all fields
6. Save sample to tests/fixtures/mt4/{entity}.json
7. Design table columns from REAL returned fields
8. Always keep payload_json with full raw record
```

Structure files to read before designing each table:
- raw_mt4_deals / raw_mt4_orders → .claude/references/mql4/API/reference_structures/structure_trade.md
- raw_mt4_accounts → .claude/references/mql4/API/reference_structures/structure_user.md
- raw_mt4_symbols → .claude/references/mql4/API/reference_structures/structure_symbol.md
- raw_mt4_groups → .claude/references/mql4/API/reference_structures/structure_config.md
- raw_mt4_ticks → .claude/references/mql4/API/reference_structures/structure_price.md
- raw_mt4_server_logs → .claude/references/mql4/API/reference_structures/structure_journal.md

---

## Error handling

Return code files:
```
.claude/references/mql4/API/reference_retcodes/retcodes_common.md
.claude/references/mql4/API/reference_retcodes/retcodes_successful.md
.claude/references/mql4/API/reference_retcodes/retcodes_trade_request.md
.claude/references/mql4/API/reference_retcodes/retcodes_account.md
```

Retry policy:
```
Attempt 1: immediate
Attempt 2: wait 5 seconds
Attempt 3: wait 30 seconds
After 3 failures: circuit_open, alert Sentry, stop for 10 minutes
```

Never log or expose credentials. Never crash on single entity failure.

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
    # Returns: { "dll_path": "...", "host": "...", "port": 443,
    #            "login": 1234, "password": "..." }
```

Never hardcode DLL paths. The DLL version must match the broker's MT4 Server version.
Each broker provides their own DLL — they are not interchangeable.

---

## Windows deployment

The MT4 Manager API DLL is Windows-only.
collector-mt4 runs on Windows EC2. Do not attempt on Linux without Wine.

---

## What NOT to do

```
- Never call the MT4 DLL from the frontend or API service
- Never hardcode DLL paths or credentials in code
- Never transform data before saving to raw tables
- Never design schemas without reading the C++ structure docs
- Never guess ctypes struct field sizes or types
- Never advance cursor past failed records
- Never commit credentials or DLL files to git
- Never mix MT4 and MT5 collector code
- Never read from folders outside .claude/references/mql4/API/
```

---

## Reference implementations (fill as built)

```
services/collector-mt4/collector.py   ← main collector class
services/collector-mt4/structs.py     ← all ctypes structure definitions
services/collector-mt4/ingestion.py   ← raw save logic
services/collector-mt4/tests/         ← unit tests with mocked DLL
tests/fixtures/mt4/                   ← real captured MT4 payloads per entity
```
