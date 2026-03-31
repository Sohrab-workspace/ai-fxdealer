# Deal List By Position ID

**Category:** deals &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns all deals associated with a specific position.

---

## Request — `ProtoManagerDealListByPositionIdReq` (payloadType `459`)

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `positionId` | `int64` | required | Position internal ID |
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
    PT["DEAL_LIST_BY_POSITION_ID_REQ"],
    PT["DEAL_LIST_BY_POSITION_ID_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoManagerDealListByPositionIdRes` (payloadType `460`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `deal` | `ProtoDeal[]` | Deals linked to this position |
| `hasMore` | `bool` | Paginate if true |


### Live Response Sample

```json
{
  "2": {
    "1": 326430,
    "2": 407529,
    "3": 767289,
    "4": 6279,
    "5": 800,
    "6": 800,
    "7": 41,
    "8": 1774939921583,
    "9": 1774939921813,
    "10": 1774939921583,
    "11": "ec51b81ec5cdb140",
    "13": 1,
    "14": 2,
    "15": 1,
    "16": {
      "9": 15713
    },
    "17": 0,
    "19": 2,
    "20": {
      "9": 15713
    },
    "23": "cTrader Copy",
    "24": "Strategy Provider: Welfare",
    "25": 305784,
    "26": {
      "9": 15713
    },
    "31": 66,
    "35": 0,
    "36": 0,
    "37": 0,
    "40": 0,
    "41": "Oz",
    "42": 10000,
    "43": 72,
    "44": 0,
    "45": 210883760,
    "46": 0,
    "58": 2
  },
  "3": 0
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
        PT["DEAL_LIST_BY_POSITION_ID_REQ"],
        PT["DEAL_LIST_BY_POSITION_ID_RES"],
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

Includes opening deal, partial closes, and the final closing deal.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
