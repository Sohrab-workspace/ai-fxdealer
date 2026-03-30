# Order Details

**Category:** orders &nbsp;|&nbsp; **Status:** ⚠️ Error captured

## Description

Returns the full snapshot, associated deals, and action history for a single order.

---

## Request — `ProtoOrderDetailsReq` (payloadType `321`)

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `orderId` | `int64` | required | Order internal ID |


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
    PT["ORDER_DETAILS_REQ"],
    PT["ORDER_DETAILS_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoOrderDetailsRes` (payloadType `322`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `orderSnapshot` | `ProtoOrder` | Order state snapshot |
| `deal` | `ProtoDeal[]` | Execution deals |
| `action` | `ProtoOrderAction[]` | Lifecycle action log |


### Live Response Sample

```
ERROR: Not captured
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
        PT["ORDER_DETAILS_REQ"],
        PT["ORDER_DETAILS_RES"],
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

The most complete single-order view. Use for audit and investigation.

---

*Captured: 2026-03-30 16:42 UTC — OpoFinance live environment*
