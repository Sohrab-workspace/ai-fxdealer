# Execution Profile List

**Category:** profiles &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns all execution profiles defining how orders are filled.

---

## Request — `ProtoExecutionProfileListReq` (payloadType `383`)

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
    PT["EXECUTION_PROFILE_LIST_REQ"],
    PT["EXECUTION_PROFILE_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoExecutionProfileListRes` (payloadType `384`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `executionProfile` | `ProtoExecutionProfile[]` | Profile ID, name, slippage, requote policy |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 1,
      "2": {
        "8": {
          "8": "ok"
        }
      },
      "3": "",
      "4": 200,
      "5": 300,
      "6": 2,
      "7": 0,
      "8": 1692352334337,
      "10": 0
    },
    {
      "1": 2,
      "2": {
        "8": {
          "5": "Book"
        }
      },
      "4": 200,
      "5": 300,
      "6": 1,
      "7": 0,
      "8": 1692352363500,
      "10": 0
    }
  ],
  "4": 0,
  "5": 1704806696509
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
        PT["EXECUTION_PROFILE_LIST_REQ"],
        PT["EXECUTION_PROFILE_LIST_RES"],
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

Execution mode (instant/market), max deviation, and partial fill policy.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
