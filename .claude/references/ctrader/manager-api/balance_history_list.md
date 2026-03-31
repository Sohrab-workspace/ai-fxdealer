# Balance History List

**Category:** balance &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns deposit, withdrawal, and balance adjustment records.

---

## Request — `ProtoBalanceHistoryListReq` (payloadType `417`)

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
    PT["BALANCE_HISTORY_LIST_REQ"],
    PT["BALANCE_HISTORY_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoBalanceHistoryListRes` (payloadType `418`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `traderId` | `int64` | Echoed from request |
| `depositWithdraw` | `ProtoDepositWithdraw[]` | Balance operation records |
| `hasMore` | `bool` | Paginate if true |


### Live Response Sample

```json
{
  "3": [
    {
      "1": 0,
      "2": 160882,
      "3": 6293,
      "4": 719202,
      "5": 200000,
      "6": 1774918024050,
      "7": "",
      "9": 38,
      "10": 719202,
      "11": 519202,
      "12": 719202,
      "13": 0,
      "15": {
        "6": "05850"
      },
      "16": 2
    },
    {
      "1": 1,
      "2": 160855,
      "3": 5580,
      "4": 0,
      "5": 18446744073709541816,
      "6": 1774909053984,
      "7": "",
      "9": 3,
      "10": 0,
      "11": 0,
      "12": 9800,
      "13": 0,
      "15": {
        "6": {
          "6": 53
        }
      },
      "16": 2
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
        PT["BALANCE_HISTORY_LIST_REQ"],
        PT["BALANCE_HISTORY_LIST_RES"],
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

Includes deposits, withdrawals, manual balance adjustments, and realized P&L from closed positions.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
