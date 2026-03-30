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
      "1": 31,
      "2": 160824,
      "3": 6279,
      "4": 158263,
      "5": 89700,
      "6": 1774887897243,
      "7": "From account 6005252",
      "8": "From account 6005252",
      "9": 134,
      "10": 158276,
      "11": 68571,
      "12": 158276,
      "13": 0,
      "16": 2
    },
    {
      "1": 30,
      "2": 160823,
      "3": 6271,
      "4": 0,
      "5": 18446744073709461916,
      "6": 1774887897242,
      "7": {
        "9": "nvestmen"
      },
      "8": {
        "9": "nvestmen"
      },
      "9": 21,
      "10": 0,
      "11": 0,
      "12": 89700,
      "13": 0,
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

*Captured: 2026-03-30 16:42 UTC — OpoFinance live environment*
