# Order Details

**Category:** orders &nbsp;|&nbsp; **Status:** ✅ Live

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

```json
{
  "2": {
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
    "16": "chartQTpending#dark#f535c656-f602-43c6-ba1a-8e89cf8aa3ba#9058251#Live",
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
  "4": [
    {
      "1": 779838,
      "3": 5,
      "4": 2,
      "6": 100,
      "7": 452131000,
      "10": {
        "6": [
          {
            "7": 55
          },
          ""
        ]
      },
      "11": "ctm-d2952cbb6dc94e7a9ba770555cf39b2a",
      "14": "cTrader 2 iOS",
      "17": 1774942470284
    },
    {
      "1": 779841,
      "3": 7,
      "4": 3,
      "6": 100,
      "7": 452263000,
      "10": {
        "6": [
          {
            "7": 55
          },
          ""
        ]
      },
      "11": "ctm-6047cb9d60224118b308700a3e74c28f",
      "14": "cTrader 2 iOS",
      "17": 1774942478816
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

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
