# Server-Pushed Events

Events arrive without a `clientMsgId`. They must be handled by a dispatch loop
separate from request/response correlation.

## Dispatch Pattern

```python
import threading

def event_loop(client):
    while client.connected:
        try:
            data = client._recv_frame()
            pt, payload, cid = proto_message_unwrap(data)
            if cid:
                client._pending[cid] = (pt, payload)  # response to a request
            else:
                dispatch_event(pt, payload)            # unsolicited event
        except Exception as e:
            handle_error(e)

def dispatch_event(payload_type, payload):
    handler = EVENT_HANDLERS.get(payload_type)
    if handler:
        handler(parse_message(payload))
    elif payload_type == PT['HEARTBEAT_EVENT']:
        pass  # ignore or echo back
    else:
        log.debug("unknown_event", pt=payload_type)
```

## All Events

| payloadType | Name | Trigger | Key Fields |
|-------------|------|---------|------------|
| 990 | `ProtoHelloEvent` | Sent immediately on connect | — |
| 51 | `ProtoHeartbeatEvent` | Every 25s if no other traffic | — |
| 300 | `ProtoExecutionEvent` | Any order/position/balance change | `executionType`, `position`, `order`, `deal`, `depositWithdraw` |
| 335 | `ProtoPositionMarginChangedEvent` | Position margin recalculated | `positionId`, `usedMargin`, `traderId` |
| 503 | `ProtoTraderChangedEvent` | Trader created/updated/deleted | `trader` (ProtoTrader) |
| 506 | `ProtoGroupChangedEvent` | Group created/updated/deleted | `group` (ProtoGroup) |
| 558 | `ProtoManagerSymbolChangedEvent` | Symbol created/updated/deleted | `symbol` (ProtoManagerSymbol) |
| 512 | `ProtoManagerChangedEvent` | Manager created/updated/deleted | `manager` (ProtoManager) |
| 518 | `ProtoServerSettingsChangedEvent` | Server settings updated | `settings` |
| 533 | `ProtoPriceStreamChangedEvent` | Price stream updated | `priceStream` |
| 561 | `ProtoDynamicLeverageChangedEvent` | Dynamic leverage profile updated | `dynamicLeverage` |
| 565 | `ProtoGSLScheduleChangedEvent` | GSL schedule updated | `gslSchedule` |
| 562 | `ProtoTraderPermissionLoseEvent` | Manager lost access to trader | `traderId` |
| 540 | `ProtoAssetChangedEvent` | Asset created/updated/deleted | `asset` |
| 547 | `ProtoLiquidityFeedSymbolChangedEvent` | LP feed-symbol link changed | `liquidityFeedSymbol` |
| 515 | `ProtoSwapAndDividendProfileChangedEvent` | Swap profile changed | profile ID |
| 730 | `ProtoTraderLogonEvent` | Trader logged in | `traderId`, `login`, timestamp |
| 731 | `ProtoTraderLogoutEvent` | Trader logged out | `traderId`, `login`, timestamp |
| 843 | `ProtoDealingSettingsUpdatedEvent` | Dealing config changed | full settings |
| 820 | `ProtoNewManualDealEvent` | New order queued for manual dealing | deal details |
| 825 | `ProtoManualDealClaimedEvent` | Manual deal claimed by manager | `dealId`, `managerId` |
| 828 | `ProtoManualDealUnclaimedEvent` | Manual deal released | `dealId` |
| 835 | `ProtoManualDealProcessedEvent` | Manual deal executed or rejected | `dealId`, result |
| 885 | `ProtoMaxAutoExecutionSizeProfileChangedEvent` | Max auto exec profile changed | profile data |
| 846 | `ProtoAssetClassChangedEvent` | Asset class created/updated | `assetClass` |
| 847 | `ProtoAssetClassDeletedEvent` | Asset class deleted | `assetClassId` |
| 848 | `ProtoSymbolCategoryChangedEvent` | Symbol category changed | `symbolCategory` |
| 849 | `ProtoSymbolCategoryDeletedEvent` | Symbol category deleted | `symbolCategoryId` |
| 575 | `ProtoSymbolArchivedEvent` | Symbol archived | `symbolId` |
| 580 | `ProtoSymbolRestoredEvent` | Symbol restored from archive | `symbolId` |
| 583 | `ProtoCrudTradeNotificationProfileChangedEvent` | Trade notification profile changed | profile data |

## ProtoExecutionEvent — Key Fields

```
field 2 (executionType)     — ProtoExecutionType enum
field 4 (position)          — ProtoPosition (optional)
field 5 (order)             — ProtoOrder (optional)
field 6 (errorCode)         — string, ProtoCSErrorCode name (optional)
field 7 (depositWithdraw)   — ProtoDepositWithdraw (optional, for balance ops)
field 8 (deal)              — ProtoDeal (optional)
field 9 (eventId)           — uint64 (optional)
field 11 (isServerEvent)    — bool
field 12 (depositToUsdRate) — double
```

## ProtoExecutionType Enum

| Value | Name |
|-------|------|
| 2 | ORDER_ACCEPTED |
| 3 | ORDER_FILLED |
| 4 | ORDER_CANCELLED |
| 5 | ORDER_EXPIRED |
| 6 | ORDER_AMENDED |
| 7 | ORDER_REJECTED |
| 8 | TRADE_OPENED |
| 9 | TRADE_CLOSED |
| 11 | BALANCE_DEPOSIT |
| 12 | BALANCE_WITHDRAW |
| 14 | STOP_OUT |
| 15 | CLOSE_POSITION |
| 16 | SWAP |
| 17 | ROLLOVER |
