# Symbol List

**Category:** symbols &nbsp;|&nbsp; **Status:** ✅ Live

## Description

Returns all symbols configured on the trading server.

---

## Request — `ProtoManagerSymbolListReq` (payloadType `467`)

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
    PT["SYMBOL_LIST_REQ"],
    PT["SYMBOL_LIST_RES"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```

---

## Response — `ProtoManagerSymbolListRes` (payloadType `468`)

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `symbol` | `ProtoManagerSymbol[]` | All symbols with full configuration |


### Live Response Sample

```json
{
  "2": [
    {
      "1": 1,
      "2": {
        "8": {
          "10": "RUS"
        }
      },
      "4": 5,
      "5": 4,
      "7": 1,
      "8": 1,
      "9": 3,
      "10": "000000000000e03f",
      "11": "9a9999999999b93f",
      "12": 0,
      "13": 0,
      "14": 3,
      "15": {
        "8": {
          "14": "ro "
        }
      },
      "16": 1749579408105,
      "17": 100000000,
      "18": 100000,
      "19": [
        {
          "3": 61255,
          "4": 147545,
          "5": 1,
          "6": 1
        },
        {
          "3": 147600,
          "4": 233945,
          "5": 1,
          "6": 1
        },
        {
          "3": 234000,
          "4": 320345,
          "5": 1,
          "6": 1
        },
        {
          "3": 320400,
          "4": 406745,
          "5": 1,
          "6": 1
        },
        {
          "3": 406800,
          "4": 493145,
          "5": 1,
          "6": 1
        }
      ],
      "23": {
        "0": [
          0,
          0,
          0,
          0
        ]
      },
      "24": {
        "8": "UR"
      },
      "27": 300,
      "30": {
        "1": 0,
        "2": 0,
        "3": 1
      },
      "31": 2,
      "32": 10000000,
      "33": 1,
      "34": {
        "8": {
          "10": "RUS"
        }
      },
      "35": 8,
      "37": 0,
      "38": 0,
      "39": 1,
      "40": 10000000,
      "49": "",
      "53": 5,
      "54": 15,
      "56": 1011,
      "57": {
        "8": {
          "13": "eric",
          "12": "/N"
        },
        "12": "w_Yo",
        "14": ""
      },
      "58": 0,
      "59": 66,
      "60": 66,
      "61": 1689811200000,
      "63": {
        "8": {
          "10": "RUS"
        }
      },
      "64": {
        "8": {
          "10": "RUS"
        }
      },
      "65": 0,
      "66": 43,
      "67": 1,
      "68": 1,
      "69": 1,
      "72": 1,
      "73": 1,
      "74": 1,
      "75": 3,
      "78": 1000,
      "79": 1259,
      "80": 24,
      "81": 0,
      "82": 0
    },
    {
      "1": 3,
      "2": {
        "8": {
          "10": "RJP"
        },
        "11": ""
      },
      "4": 3,
      "5": 2,
      "7": 1,
      "8": 1,
      "9": 3,
      "10": "000000000000e03f",
      "11": "9a9999999999b93f",
      "12": 0,
      "13": 0,
      "14": 3,
      "15": {
        "8": {
          "14": "ro "
        }
      },
      "16": 1749579408138,
      "17": 100000000,
      "18": 100000,
      "19": [
        {
          "3": 61255,
          "4": 147545,
          "5": 1,
          "6": 1
        },
        {
          "3": 147600,
          "4": 233945,
          "5": 1,
          "6": 1
        },
        {
          "3": 234000,
          "4": 320345,
          "5": 1,
          "6": 1
        },
        {
          "3": 320400,
          "4": 406745,
          "5": 1,
          "6": 1
        },
        {
          "3": 406800,
          "4": 493145,
          "5": 1,
          "6": 1
        }
      ],
      "23": {
        "0": [
          0,
          0,
          0,
          0
        ]
      },
      "24": {
        "8": "UR"
      },
      "27": 300,
      "30": {
        "1": 0,
        "2": 0,
        "3": 1
      },
      "31": 2,
      "32": 10000000,
      "33": 1,
      "34": {
        "8": {
          "10": "RJP"
        },
        "11": ""
      },
      "35": 9,
      "37": 1,
      "38": 0,
      "39": 1,
      "40": 10000000,
      "49": "",
      "53": 5,
      "54": 8,
      "56": 1011,
      "57": {
        "8": {
          "13": "eric",
          "12": "/N"
        },
        "12": "w_Yo",
        "14": ""
      },
      "58": 0,
      "59": 66,
      "60": 66,
      "61": 1689811200000,
      "63": {
        "8": {
          "10": "RJP"
        },
        "11": ""
      },
      "64": {
        "8": {
          "10": "RJP"
        },
        "11": ""
      },
      "65": 0,
      "66": 43,
      "67": 1,
      "68": 1,
      "69": 1,
      "72": 1,
      "73": 1,
      "74": 1,
      "75": 3,
      "78": 1000,
      "79": 1259,
      "80": 24,
      "81": 0,
      "82": 0
    }
  ],
  "3": [
    {
      "1": 65,
      "2": {
        "8": {
          "10": "DZAR"
        }
      },
      "3": 1692612258667,
      "4": {
        "8": {
          "14": "stra"
        }
      },
      "5": 4,
      "6": 4,
      "7": 10000000,
      "8": {
        "8": "UD"
      },
      "9": 1
    },
    {
      "1": 66,
      "2": "CADDKK",
      "3": 1692612263200,
      "4": "Canadian Dollar vs Danish Krone",
      "5": 5,
      "6": 4,
      "7": 10000000,
      "8": "CAD",
      "9": 2
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
        PT["SYMBOL_LIST_REQ"],
        PT["SYMBOL_LIST_RES"],
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

Includes all fields: spread, swaps, commissions, margins, trading hours, LP routing.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
