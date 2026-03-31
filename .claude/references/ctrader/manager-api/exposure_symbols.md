# Exposure Symbol List

**Category:** risk &nbsp;|&nbsp; **Status:** ✅ Live captured

## Description

Returns the current net exposure per symbol across all open positions, for every symbol on both BUY and SELL sides.

---

## Request — `ProtoExposureSymbolListReq` (payloadType `419`)

### Request Fields

> Sending an empty payload returns `INVALID_REQUEST`. Pass `field2 = 1` to retrieve the full server-wide exposure list.

| Field | Wire # | Type | Required | Description |
|-------|--------|------|----------|-------------|
| *(mode flag)* | `2` | `int64` | required | Set to `1` — returns all symbol exposures |

### Python Example

```python
import ssl, socket, struct, hashlib, time
from capture_manager_api import (
    ManagerAPIClient, encode_int64,
    PT, fields_to_dict, parse_message
)

c = ManagerAPIClient()
c.connect()  # authenticates automatically

# field 2 = 1 is required; empty payload returns INVALID_REQUEST
inner = encode_int64(2, 1)

fields = c.request(
    PT["EXPOSURE_SYMBOL_LIST_REQ"],
    PT["EXPOSURE_SYMBOL_LIST_RES"],
    inner,
    reconnect_on_fail=True  # this endpoint drops the connection on error
)

# Response is a list of ProtoExposureSymbol in field 2
raw_exposures = c.raw_captures.get("exposure_symbols", {}).get(2, [])
for raw in raw_exposures:
    rec = parse_message(raw)
    symbol_id = rec.get(1, [None])[0]
    side      = rec.get(2, [None])[0]   # 1=BUY, 2=SELL
    vol       = rec.get(3, [0])[0]
    exposure  = rec.get(6, [0])[0]      # in account currency cents
    print(f"  symbolId={symbol_id} side={side} vol={vol} exposure={exposure}")

c.close()
```

---

## Response — `ProtoExposureSymbolListRes` (payloadType `420`)

### Response Fields

| Field | Wire # | Type | Description |
|-------|--------|------|-------------|
| `exposureSymbol` | `2` | `ProtoExposureSymbol[]` | One record per symbol per side |

### ProtoExposureSymbol fields

| Field | Wire # | Type | Description |
|-------|--------|------|-------------|
| `symbolId`   | `1` | `int64`  | cTrader symbol ID |
| `tradeSide`  | `2` | `int32`  | `1`=BUY, `2`=SELL |
| `volume`     | `3` | `int64`  | Net volume (units × 100) |
| `price`      | `4` | `int64`  | Weighted average price (× 100000) |
| `contracts`  | `5` | `int64`  | Number of open contracts |
| `grossPnl`   | `6` | `int64`  | Gross P&L in account currency cents |
| `usedMargin` | `7` | `int64`  | Margin used in account currency cents |

### Live Response Sample

```json
{
  "exposureSymbol": [
    { "symbolId": 374, "tradeSide": 1, "volume": 0, "price": 0, "contracts": 0, "grossPnl": 0, "usedMargin": 0 },
    { "symbolId": 374, "tradeSide": 2, "volume": 0, "price": 0, "contracts": 0, "grossPnl": 0, "usedMargin": 0 },
    { "symbolId": 375, "tradeSide": 1, "volume": 0, ... },
    ...
  ]
}
```

> The list includes all configured symbols with both BUY and SELL rows, even when exposure is zero.
> Zero values indicate no open positions on that symbol/side at capture time.

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
        PT["EXPOSURE_SYMBOL_LIST_REQ"],
        PT["EXPOSURE_SYMBOL_LIST_RES"],
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

Critical for risk monitoring. Updated in near real-time. Use ProtoExecutionEvent to maintain live state.

---

*Captured: 2026-03-31 07:40 UTC — OpoFinance live environment*
