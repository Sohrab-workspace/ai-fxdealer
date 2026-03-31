# Trader List (Accounts)

**Category:** accounts &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns a paginated list of trader accounts registered within the given timestamp window.

---

## Request — `ProtoTraderListReq` (payloadType `403`)

### Request Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fromTimestamp` | `int64` | required | Start of window — Unix ms |
| `toTimestamp` | `int64` | required | End of window — Unix ms |
| `groupId` | `int64` | optional | Filter by group ID |
| `hideIbParameters` | `bool` | optional | Exclude IB-specific fields |
| `onlySubAccounts` | `bool` | optional | Return sub-accounts only |


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
    PT["TRADER_LIST_REQ"],
    PT["TRADER_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoTraderListRes` (payloadType `404`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `trader` | `ProtoTrader[]` | List of trader objects |
| `hasMore` | `bool` | true = more pages exist; advance fromTimestamp |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 6307,
      "2": 6005288,
      "3": 1031,
      "7": 100,
      "8": 43058,
      "9": 0,
      "10": {
        "9": "oham",
        "13": [
          {
            "12": "dme"
          },
          "sam"
        ]
      },
      "12": {
        "9": "nvestmen"
      },
      "16": {
        "9": {
          "12": "zan"
        }
      },
      "19": "+989121111299",
      "21": {
        "13": {
          "13": "taf"
        },
        "12": [
          {
            "15": "oli@gm"
          },
          {
            "13": "l.com"
          }
        ]
      },
      "25": 1774887429358,
      "27": 0,
      "28": 1774941729801,
      "29": 0,
      "30": 18,
      "32": 0,
      "34": 0,
      "35": 0,
      "36": 0,
      "37": 0,
      "38": 0,
      "39": 0,
      "43": 0,
      "44": 1,
      "45": 1,
      "49": 0,
      "50": 0,
      "51": 1,
      "53": 1,
      "55": 1,
      "56": "Tafazzolinasr",
      "57": 1,
      "58": 0,
      "59": 0,
      "60": 1,
      "61": 15,
      "64": 0,
      "65": 0,
      "66": 10000,
      "67": 0,
      "68": 0,
      "69": "opofinance",
      "70": 50000,
      "71": 0,
      "72": 111449,
      "73": 0,
      "74": 3,
      "75": 6271,
      "77": 0,
      "78": 0,
      "80": 2,
      "86": "Saturn"
    },
    {
      "1": 6306,
      "2": 6005287,
      "3": 1036,
      "7": 500,
      "8": 0,
      "9": 0,
      "10": {
        "8": {
          "13": [
            "iral",
            ""
          ]
        }
      },
      "14": 792,
      "16": {
        "9": "stanbul"
      },
      "19": "+905010164902",
      "20": {
        "7": {
          "6": 99
        }
      },
      "21": {
        "12": {
          "13": "rhm2",
          "6": 48
        },
        "8": 103,
        "13": {
          "12": "il."
        }
      },
      "25": 1774879467894,
      "27": 0,
      "28": 1774879469588,
      "29": 0,
      "30": 1,
      "32": 0,
      "34": 0,
      "35": 0,
      "36": 0,
      "37": 0,
      "38": 0,
      "39": 0,
      "43": 0,
      "44": 1,
      "45": 1,
      "49": 0,
      "50": 0,
      "51": 1,
      "53": 1,
      "55": 1,
      "56": {
        "10": {
          "13": [
            105,
            "i"
          ]
        }
      },
      "57": 1,
      "58": 0,
      "59": 2,
      "60": 1,
      "61": 15,
      "64": 0,
      "65": 0,
      "66": 50000,
      "67": 0,
      "68": 0,
      "69": "opofinance",
      "70": 50000,
      "71": 0,
      "73": 0,
      "74": 1,
      "77": 0,
      "78": 0,
      "80": 2
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
        PT["TRADER_LIST_REQ"],
        PT["TRADER_LIST_RES"],
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

Paginate by advancing `fromTimestamp` to the last record's `registrationTimestamp`. Keep looping while `hasMore == true`.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
