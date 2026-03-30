# Liquidity Feed Symbol List

**Category:** configuration &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns the symbol-to-LP-feed mapping for execution routing.

---

## Request — `ProtoLiquidityFeedSymbolListReq` (payloadType `489`)

### Request Fields

_No request fields — send empty payload._

### Python Example

```python
import ssl, socket, struct, hashlib, time
from capture_manager_api import (
    ManagerAPIClient, encode_int64, encode_string,
    PT, parse_message, fields_to_dict
)

c = ManagerAPIClient()
c.connect()  # authenticates automatically

now_ms = int(time.time() * 1000)
from_ms = now_ms - 7 * 86400 * 1000  # 7 days ago

inner = (
    b""  # add fields here, e.g. encode_int64(2, from_ms) + encode_int64(3, now_ms)
)

fields = c.request(
    PT["LIQUIDITY_FEED_SYMBOL_LIST_REQ"],
    PT["LIQUIDITY_FEED_SYMBOL_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoLiquidityFeedSymbolListRes` (payloadType `490`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `liquidityFeedSymbol` | `ProtoLiquidityFeedSymbol[]` | Symbol ID + feed ID + routing config |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 32,
      "2": "GBPSGD",
      "3": "GBPSGD",
      "4": 1024,
      "5": 66,
      "6": 0,
      "7": 15000,
      "8": 12000,
      "9": 0
    },
    {
      "1": 637,
      "2": "GBPSGD.",
      "3": "GBPSGD.",
      "4": 1025,
      "5": 66,
      "6": 0,
      "7": 15000,
      "8": 12000,
      "9": 0
    }
  ]
}
```

---

## Error Handling

| Scenario | Error | Action |
|----------|-------|--------|
| Invalid credentials | `AUTHENTICATION_FAILED (3)` | Re-authenticate |
| Wrong traderId / ID | `TRADER_NOT_FOUND (11)` or `ENTITY_NOT_FOUND (6)` | Validate ID exists first |
| Rate limit hit | `REQUEST_FREQUENCY_EXCEEDED (23)` | Back off and retry with jitter |
| Permissions denied | `NOT_ENOUGH_RIGHTS (2)` | Check manager permission list |
| Connection dropped | `ConnectionError` / socket timeout | Reconnect with exponential backoff |
| Frame too large | `FRAME_TOO_LONG (8)` | Reduce time window / add `maxRows` |

```python
try:
    fields = c.request(
        PT["LIQUIDITY_FEED_SYMBOL_LIST_REQ"],
        PT["LIQUIDITY_FEED_SYMBOL_LIST_RES"],
        inner
    )
except RuntimeError as e:
    if "AUTHENTICATION_FAILED" in str(e):
        c.connect()   # re-authenticate
    elif "REQUEST_FREQUENCY_EXCEEDED" in str(e):
        time.sleep(1)
    else:
        raise
except TimeoutError:
    # reconnect
    c.close()
    c.connect()
```

---

## Notes

Used to understand B-book / A-book routing per symbol.

---

*Captured: 2026-03-30 16:42 UTC — OpoFinance live environment*
