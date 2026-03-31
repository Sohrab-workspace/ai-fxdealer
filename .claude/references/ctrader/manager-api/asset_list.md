# Asset List

**Category:** assets &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns all assets (currencies, commodities, indices) configured on the server.

---

## Request — `ProtoAssetListReq` (payloadType `465`)

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
    PT["ASSET_LIST_REQ"],
    PT["ASSET_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoAssetListRes` (payloadType `466`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `asset` | `ProtoAsset[]` | Asset ID, name, digits, display name |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 1024,
      "2": "DOT",
      "3": "DOT",
      "4": 6,
      "5": 0,
      "6": 0,
      "7": "DOT",
      "8": 0,
      "9": 8,
      "10": "",
      "12": 1,
      "13": 1757147505313
    },
    {
      "1": 1025,
      "2": "DSH",
      "3": "DSH",
      "4": 6,
      "5": 0,
      "6": 0,
      "7": "DSH",
      "8": 0,
      "9": 8,
      "10": "",
      "12": 1,
      "13": 1757147505313
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
        PT["ASSET_LIST_REQ"],
        PT["ASSET_LIST_RES"],
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

Assets are referenced by symbolId in deals and positions via depositAssetId.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
