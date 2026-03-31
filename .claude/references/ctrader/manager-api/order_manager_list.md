# Order Manager List (All Orders)

**Category:** orders &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns all orders (pending + executed + cancelled) within the time window.

---

## Request — `ProtoOrderManagerListReq` (payloadType `443`)

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fromTimestamp` | `int64` | required | Window start — Unix ms |
| `toTimestamp` | `int64` | required | Window end — Unix ms |
| `traderId` | `int64` | optional | Filter by trader |


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
    PT["ORDER_MANAGER_LIST_REQ"],
    PT["ORDER_MANAGER_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoOrderManagerListRes` (payloadType `444`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `order` | `ProtoOrder[]` | All order objects |
| `hasMore` | `bool` | Paginate if true |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 407544,
      "2": {
        "1": 41,
        "2": 200,
        "3": 1,
        "4": 6295,
        "7": 1774941984222,
        "14": "cTrader 2 iOS",
        "15": "Oz",
        "16": 10000,
        "17": 0,
        "19": "1f85eb51f8c2b140",
        "20": 0,
        "21": 1
      },
      "3": 2,
      "4": 5,
      "10": 0,
      "13": 1774941992312,
      "14": 2,
      "16": "chartQTpending#dark#a177d492-2f52-4df5-9fbe-0eca3041a440#9058251#Live",
      "20": 0,
      "21": "1f85eb51f8c2b140",
      "23": "ctm-9ef8caac2fed4b69809f48230c7f02cd",
      "24": 0,
      "26": 2,
      "30": 767315,
      "32": 830000,
      "34": 0,
      "35": 0,
      "36": 0,
      "39": 0,
      "41": 0,
      "42": 6005276,
      "43": "Safiullah",
      "44": "Faqiri",
      "46": 0,
      "49": 1,
      "54": 2
    },
    {
      "1": 407543,
      "2": {
        "1": 41,
        "2": 100,
        "3": 2,
        "4": 6307,
        "7": 1774941729565,
        "8": 1774941729779,
        "13": "Strategy Provider: Saturn",
        "14": "cTrader Copy",
        "15": "Oz",
        "16": 10000,
        "17": 0,
        "20": 0
      },
      "3": 1,
      "4": 2,
      "9": {
        "9": 15713
      },
      "10": 100,
      "13": 1774941729779,
      "14": 2,
      "20": 1,
      "23": "CH:2e9c7a59-a043-463c-a3da-6070f695c3ad",
      "24": 0,
      "26": 3,
      "30": 767310,
      "34": 0,
      "35": 0,
      "36": 0,
      "39": 0,
      "41": 0,
      "42": 6005288,
      "43": {
        "9": "oham",
        "13": [
          {
            "12": "dme"
          },
          "sam"
        ]
      },
      "44": "Tafazzolinasr",
      "54": 2
    }
  ],
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
        PT["ORDER_MANAGER_LIST_REQ"],
        PT["ORDER_MANAGER_LIST_RES"],
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

Broadest order query. Useful for full activity audit.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
