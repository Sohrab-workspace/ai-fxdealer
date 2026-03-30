# Group List (Light)

**Category:** groups &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns a lightweight list of all trader groups (no symbol configuration).

---

## Request — `ProtoLightGroupListReq` (payloadType `473`)

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
    PT["LIGHT_GROUP_LIST_REQ"],
    PT["LIGHT_GROUP_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoLightGroupListRes` (payloadType `474`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `group` | `ProtoLightGroup[]` | Group ID, name, and basic metadata |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 1024,
      "2": {
        "8": "CNPR"
      },
      "3": 1,
      "4": 1,
      "9": "9a9999999999c93f",
      "11": "",
      "13": 1,
      "14": 0,
      "15": 1,
      "23": 0,
      "26": 1,
      "27": 0,
      "28": 0,
      "29": 1,
      "30": 1
    },
    {
      "1": 1025,
      "2": {
        "8": "CNPR"
      },
      "3": 1,
      "4": 1,
      "9": "9a9999999999c93f",
      "11": "",
      "13": 1,
      "14": 0,
      "15": 1,
      "23": 0,
      "26": 1,
      "27": 0,
      "28": 0,
      "29": 1,
      "30": 1
    }
  ],
  "3": 1770722153945
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
        PT["LIGHT_GROUP_LIST_REQ"],
        PT["LIGHT_GROUP_LIST_RES"],
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

Use for lookups and dropdowns. For full group config including symbol overrides, use GroupById.

---

*Captured: 2026-03-30 16:42 UTC — OpoFinance live environment*
