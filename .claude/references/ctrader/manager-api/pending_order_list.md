# Pending Order List

**Category:** orders &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns all pending (limit/stop) orders within the time window.

---

## Request — `ProtoPendingOrderListReq` (payloadType `409`)

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `traderId` | `int64` | optional | Filter by trader |
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
    PT["PENDING_ORDER_LIST_REQ"],
    PT["PENDING_ORDER_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoPendingOrderListRes` (payloadType `410`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `traderId` | `int64` | Echoed from request |
| `order` | `ProtoOrder[]` | Pending orders |
| `hasMore` | `bool` | Paginate if true |


### Live Response Sample

```json
{
  "3": [
    {
      "1": 407546,
      "2": {
        "1": 41,
        "2": 100,
        "3": 1,
        "4": 6295,
        "7": 1774942470284,
        "14": "cTrader 2 iOS",
        "15": "Oz",
        "16": 10000,
        "17": 0,
        "19": "c3f5285c4fa9b140",
        "20": 0,
        "21": 1
      },
      "3": 2,
      "4": 1,
      "10": 0,
      "13": 1774942491336,
      "14": 2,
      "20": 0,
      "21": "7b14ae47a1aab140",
      "23": "ctm-d2952cbb6dc94e7a9ba770555cf39b2a",
      "24": 0,
      "26": 2,
      "30": 767317,
      "33": 9683000,
      "34": 0,
      "35": 0,
      "36": 0,
      "39": 0,
      "41": 0,
      "42": 6005276,
      "43": "Safiullah",
      "44": "Faqiri",
      "54": 2
    },
    {
      "1": 407545,
      "2": {
        "1": 41,
        "2": 100,
        "3": 1,
        "4": 6295,
        "7": 1774942467106,
        "14": "cTrader 2 iOS",
        "15": "Oz",
        "16": 10000,
        "17": 0,
        "19": "f6285c8f82b4b140",
        "20": 0,
        "21": 1
      },
      "3": 2,
      "4": 1,
      "10": 0,
      "13": 1774942485915,
      "14": 2,
      "20": 0,
      "21": "f6285c8f82b4b140",
      "23": "ctm-8bc34cab208f4feeaa096aa9dd273ee1",
      "24": 0,
      "26": 2,
      "30": 767316,
      "33": 8677000,
      "34": 0,
      "35": 0,
      "36": 0,
      "39": 0,
      "41": 0,
      "42": 6005276,
      "43": "Safiullah",
      "44": "Faqiri",
      "54": 2
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
        PT["PENDING_ORDER_LIST_REQ"],
        PT["PENDING_ORDER_LIST_RES"],
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

Only returns PENDING orders (LIMIT, STOP, STOP_LIMIT). Use OrderManagerList for executed orders.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
