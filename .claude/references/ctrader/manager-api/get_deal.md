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
    "1": 326138,
    "2": 407178,
    "3": 767055,
    "4": 6297,
    "5": 300,
    "6": 300,
    "7": 41,
    "8": 1774888939654,
    "9": 1774888939872,
    "10": 1774888939654,
    "11": {
      "1964": "14aec7c2b140"
    },
    "12": "ae47e17ad4c2b140",
    "13": 2,
    "14": 2,
    "15": 2,
    "16": "ae47e17ad4c2b140",
    "17": 18446744073709551607,
    "19": 2,
    "20": "ae47e17ad4c2b140",
    "22": "FTB_Pro_Ultra",
    "23": "cBot Cloud",
    "25": 305539,
    "26": "ae47e17ad4c2b140",
    "31": 66,
    "32": {
      "2": "ffff\u6d31@",
      "3": 0,
      "4": 18446744073709551598,
      "7": 4164,
      "8": 34146,
      "11": {
        "14": 111
      },
      "12": "66666666a6abb140",
      "13": {
        "1964": "14aec7c2b140"
      },
      "15": "000000000000f03f",
      "16": 300,
      "18": 3,
      "19": 0,
      "20": 0,
      "21": 0,
      "23": 34146,
      "25": 4146,
      "26": 0,
      "27": {
        "0": [
          0,
          0,
          0,
          0
        ]
      },
      "28": 29898,
      "29": 34155,
      "30": 0,
      "32": 30,
      "33": {
        "10": 82
      },
      "34": 0,
      "40": 1774888225860,
      "43": 2,
      "44": 0
    },
    "35": 0,
    "36": 0,
    "37": 0,
    "40": 0,
    "41": "Oz",
    "42": 10000,
    "43": 15,
    "44": 1,
    "45": 2723892,
    "46": 0,
    "58": 2,
    "59": [
      1,
      5
    ]
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

*Captured: 2026-03-30 16:42 UTC — OpoFinance live environment*
