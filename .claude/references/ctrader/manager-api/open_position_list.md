# Open Position List

**Category:** positions &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns open positions opened within the given time window.

---

## Request — `ProtoPositionListReq` (payloadType `407`)

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `traderId` | `int64` | optional | Filter by trader — omit for all |
| `fromTimestamp` | `int64` | required | Window start — Unix ms |
| `toTimestamp` | `int64` | required | Window end — Unix ms |


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
    PT["POSITION_LIST_REQ"],
    PT["POSITION_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoPositionListRes` (payloadType `408`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `traderId` | `int64` | Echoed from request (if filtered) |
| `position` | `ProtoPosition[]` | Open position objects |
| `hasMore` | `bool` | Paginate by advancing fromTimestamp |


### Live Response Sample

```json
{
  "3": [
    {
      "1": 767289,
      "3": {
        "1": 41,
        "2": 800,
        "3": 1,
        "4": 6279,
        "7": 1774939921813,
        "13": "Strategy Provider: Welfare",
        "14": "cTrader Copy",
        "15": "Oz",
        "16": 10000,
        "20": 0
      },
      "4": 1,
      "5": 0,
      "6": "ec51b81ec5cdb140",
      "10": 1774939921813,
      "11": 2,
      "13": 0,
      "14": {
        "9": 15713
      },
      "16": 0,
      "17": 0,
      "18": 0,
      "20": 0,
      "21": 0,
      "23": 36461,
      "30": 2,
      "31": 0
    },
    {
      "1": 767227,
      "3": {
        "1": 41,
        "2": 300,
        "3": 1,
        "4": 4822,
        "7": 1774932849268,
        "14": "cTrader 2 iOS",
        "15": "Oz",
        "16": 10000,
        "20": 0,
        "21": 1
      },
      "4": 1,
      "5": 0,
      "6": "85eb51b89ed4b140",
      "10": 1774932849268,
      "11": 2,
      "13": 18446744073709551610,
      "14": {
        "487": 2212353045893
      },
      "16": 0,
      "17": 0,
      "18": 0,
      "20": 0,
      "21": 0,
      "23": 6847,
      "30": 2,
      "31": 0
    }
  ],
  "4": 0
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
        PT["POSITION_LIST_REQ"],
        PT["POSITION_LIST_RES"],
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

Only returns currently open positions. For closed positions use ManagerClosedPositionList.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
