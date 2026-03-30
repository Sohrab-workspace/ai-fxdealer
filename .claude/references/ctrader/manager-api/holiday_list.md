# Holiday List

**Category:** profiles &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns all configured market holidays.

---

## Request — `ProtoHolidayListReq` (payloadType `398`)

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
    PT["HOLIDAY_LIST_REQ"],
    PT["HOLIDAY_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoHolidayListRes` (payloadType `399`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `holiday` | `ProtoHoliday[]` | Date, name, affected symbols/profiles |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 2,
      "2": {
        "8": {
          "12": "rly"
        },
        "4": 99
      },
      "3": "Tuesday 24th December",
      "4": {
        "8": {
          "14": "rop"
        },
        "12": "/Buc",
        "13": 97,
        "14": "st"
      },
      "5": 20081,
      "6": 0,
      "7": 72900,
      "8": 86340
    },
    {
      "1": 3,
      "2": {
        "8": {
          "12": "rly"
        },
        "4": 99
      },
      "3": "Tuesday 24th December",
      "4": {
        "8": {
          "14": "rop"
        },
        "12": "/Buc",
        "13": 97,
        "14": "st"
      },
      "5": 20081,
      "6": 0,
      "7": 19800,
      "8": 86340
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
        PT["HOLIDAY_LIST_REQ"],
        PT["HOLIDAY_LIST_RES"],
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

Holidays override trading schedules. Referenced by ProtoScheduleProfile.

---

*Captured: 2026-03-30 16:42 UTC — OpoFinance live environment*
