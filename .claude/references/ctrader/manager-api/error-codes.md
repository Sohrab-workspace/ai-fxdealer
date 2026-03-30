# Error Codes

## ProtoErrorCode (Transport-level — from ErrorRes payloadType=50)

| Code | Name | Description |
|------|------|-------------|
| 1 | UNKNOWN_ERROR | Unknown error |
| 2 | UNSUPPORTED_MESSAGE | Message type not supported by this server |
| 3 | INVALID_REQUEST | Malformed or missing required fields |
| 4 | WRONG_PASSWORD | Authentication failure |
| 5 | TIMEOUT_ERROR | Server-side timeout |
| 6 | ENTITY_NOT_FOUND | Referenced entity does not exist |
| 7 | CANT_ROUTE_REQUEST | Internal routing failure |
| 8 | FRAME_TOO_LONG | Message frame exceeds server limit — reduce time window |
| 9 | MARKET_CLOSED | Trading not available |
| 10 | CONCURRENT_MODIFICATION | Optimistic lock conflict — retry |
| 11 | BLOCKED_PAYLOAD_TYPE | This payload type is not permitted |
| 12 | DATASTORE_IS_NOT_AVAILABLE | Server datastore unavailable |

## ProtoCSErrorCode (Business-level — from ProtoExecutionEvent.errorCode)

| Code | Name | Description |
|------|------|-------------|
| 1 | NOT_ENOUGH_MONEY | Insufficient balance |
| 2 | NOT_ENOUGH_RIGHTS | Permission denied |
| 3 | AUTHENTICATION_FAILED | Wrong credentials or expired session |
| 4 | POSITION_NOT_FOUND | Invalid position ID |
| 5 | POSITION_LOCKED | Position being modified by another process |
| 6 | CHANGE_BALANCE_BAD_AMOUNT | Invalid balance operation amount |
| 7 | NO_QUOTES | No market data available |
| 8 | TRADING_DISABLED | Trading disabled on symbol or server |
| 9 | TRADING_NOT_ALLOWED | Trader does not have trading permission |
| 10 | TRADING_BAD_VOLUME | Volume outside allowed min/max/step |
| 11 | TRADER_NOT_FOUND | Invalid trader ID |
| 12 | TRADER_GROUP_NOT_FOUND | Invalid group ID |
| 13 | RECONCILIATION_IN_PROGRESS | System undergoing reconciliation |
| 14 | ALREADY_LOGGED_IN | Connection already established |
| 16 | TOO_MANY_POSITIONS | Position limit reached |
| 17 | ORDER_NOT_FOUND | Invalid order ID |
| 18 | TRADING_BAD_STOPS | SL/TP outside allowed distance |
| 19 | ALREADY_DELETED | Entity already deleted |
| 20 | WRONG_LEVERAGE | Leverage value not allowed |
| 21 | TRADING_BAD_EXPIRATION_DATE | Expiration time invalid |
| 22 | ALREADY_SUBSCRIBED | Already subscribed to this feed |
| 23 | REQUEST_FREQUENCY_EXCEEDED | **Rate limit** — back off and retry |
| 24 | POSITION_NOT_OPEN | Position already closed |
| 25 | WRONG_TIME_SEQUENCE | Timestamp out of order |
| 26 | FORBID_WITH_TRADING_ENABLED | Operation not allowed while trading active |
| 27 | INCORRECT_POSITION_ID | Position ID format error |
| 28 | TRADER_HAS_POSITIONS | Cannot delete trader with open positions |
| 29 | UNKNOWN_LIQIDITY_FEED | Invalid liquidity feed ID |
| 30 | ASSET_CLASS_ALREADY_EXIST | Duplicate asset class name |
| 31 | ASSET_CLASS_IS_NOT_EMPTY | Asset class has symbols assigned |
| 32 | TRADING_BAD_PRICES | Price outside valid range |
| 33 | UNABLE_TO_FORWARD_COMMAND | Internal routing failure |
| 34 | UNKNOWN_SYMBOL | Invalid symbol ID |
| 35 | INCORRECT_BOUNDARIES | Boundary validation failed |
| 36 | SYMBOL_NOT_FOUND | Symbol not found |
| 37 | DEAL_NOT_FOUND | Invalid deal ID |
| 38 | POSITION_CONCURRENT_CHANGE | Concurrent position modification |
| 39 | NOT_INTRODUCING_BROKER | Account is not an IB |
| 40 | INTRODUCING_BROKER_CYCLE | IB relationship cycle detected |
| 41 | UNABLE_TO_CANCEL_ORDER | Order cannot be cancelled in current state |
| 42 | UNABLE_TO_AMEND_ORDER | Order cannot be amended in current state |
| 43 | UNKNOWN_DEPOSIT_CURRENCY | Deposit currency not recognized |
| 44 | DEPOSIT_CURRENCY_NOT_ALLOWED | Currency not allowed for this account |
| 45 | SHORT_SELLING_NOT_ALLOWED | Short selling disabled for this symbol/account |
| 46 | CHANGE_BONUS_BAD_AMOUNT | Invalid bonus amount |
| 47 | SERVER_IS_UNDER_MAINTENANCE | Server in maintenance mode |
| 48 | TRADING_BAD_STAKE | Invalid stake (spread betting) |
| 50 | PROTECTION_IS_TOO_CLOSE_TO_MARKET | GSL protection too close to current price |
| 51 | ORDER_TYPE_NOT_ALLOWED | Order type not permitted on this symbol |
| 52 | INVALID_DATA | Generic invalid data error |
| 53 | NO_SUCH_LOGIN | Login number does not exist |
| 54 | MAX_EXPOSURE_REACHED | Broker exposure limit reached |
| 55 | PENDING_EXECUTION | Execution pending — await ExeCution event |
| 63 | CHANNEL_IS_BLOCKED | Trading channel (e.g. API) is blocked |
| 67 | CONNECTIONS_LIMIT_EXCEEDED | Too many simultaneous manager connections |
| 68 | WORSE_GSL_NOT_ALLOWED | Cannot move GSL to a worse price |
| 69 | SYMBOL_HAS_HOLIDAY | Symbol is on a configured holiday |

## Error Handling Pattern

```python
try:
    fields = c.request(req_pt, res_pt, inner)
except RuntimeError as e:
    msg = str(e)
    if "AUTHENTICATION_FAILED" in msg or "WRONG_PASSWORD" in msg:
        # Re-authenticate
        c.close()
        c.connect()
    elif "REQUEST_FREQUENCY_EXCEEDED" in msg:
        # Rate limited — exponential backoff
        time.sleep(random.uniform(1, 3))
    elif "TRADER_NOT_FOUND" in msg or "ENTITY_NOT_FOUND" in msg:
        # Bad ID — skip this record
        log.warning("entity_not_found", id=requested_id)
    elif "FRAME_TOO_LONG" in msg:
        # Shrink time window
        window = window // 2
    else:
        raise
except TimeoutError:
    c.close()
    c.connect()
except ConnectionError:
    c.close()
    time.sleep(5)
    c.connect()
```
