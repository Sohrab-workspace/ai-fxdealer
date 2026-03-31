# Get Deal By ID

**Category:** deals &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Fetches a single deal by its ID.

---

## Request — `ProtoManagerGetDealReq` (payloadType `709`)

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `dealId` | `uint64` | required | Deal internal ID |


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
    PT["GET_DEAL_REQ"],
    PT["GET_DEAL_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoManagerGetDealRes` (payloadType `711`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `deal` | `ProtoDeal` | The deal object |


### Live Response Sample

```json
{
  "2": {
    "1": 326443,
    "2": 407543,
    "3": 767310,
    "4": 6307,
    "5": 100,
    "6": 100,
    "7": 41,
    "8": 1774941729565,
    "9": 1774941729779,
    "10": 1774941729565,
    "11": {
      "9": 15713
    },
    "13": 2,
    "14": 2,
    "15": 1,
    "16": "ec51b81e05c9b140",
    "17": 0,
    "19": 2,
    "20": "ec51b81e05c9b140",
    "23": "cTrader Copy",
    "24": "Strategy Provider: Saturn",
    "25": 305793,
    "26": "ec51b81e05c9b140",
    "31": 66,
    "32": {
      "2": {
        "14": "3d0ad763c7b140"
      },
      "3": 0,
      "4": 0,
      "7": 154,
      "8": 43058,
      "11": {
        "14": 111
      },
      "15": "000000000000f03f",
      "16": 100,
      "18": 18,
      "19": 0,
      "20": 0,
      "21": 0,
      "23": 43056,
      "25": 154,
      "26": 0,
      "27": {
        "0": [
          0,
          0,
          0,
          0
        ]
      },
      "28": 42110,
      "29": 43204,
      "30": 0,
      "32": 18,
      "33": {
        "4": 22,
        "13": "f38eb33f"
      },
      "34": 0,
      "40": 1774941249039,
      "43": 2,
      "44": 0
    },
    "35": 0,
    "36": 0,
    "37": 0,
    "40": 0,
    "41": "Oz",
    "42": 10000,
    "43": 9,
    "44": 0,
    "45": 14692475,
    "46": 0,
    "58": 2
  }
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
        PT["GET_DEAL_REQ"],
        PT["GET_DEAL_RES"],
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

Fast single-deal lookup. Prefer this over DealList when you have the dealId.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
