# cTrader Manager API — Complete Reference

Captured live from the OpoFinance environment on 2026-03-30.

## Connection

| Parameter | Value |
|-----------|-------|
| Host | `live-managerapi.p.ctrader.com` |
| Port | `5011` |
| Protocol | Protobuf over TCP + TLS |
| Auth | MD5 password hash + plantId + environmentName |
| Heartbeat | Every 25 seconds (payloadType=51) |

## Quick Start

```python
from capture_manager_api import ManagerAPIClient, PT, encode_int64, fields_to_dict
import time

c = ManagerAPIClient()
c.connect()

now_ms = int(time.time() * 1000)
fields = c.request(
    PT['SERVER_TIME_REQ'],
    PT['SERVER_TIME_RES']
)
print(fields_to_dict(fields))
c.close()
```

## All Endpoints

| Status | Endpoint | Request Message | Category |
|--------|----------|-----------------|----------|
| ✅ | [Trader List (Accounts)](trader_list.md) | `ProtoTraderListReq` | accounts |
| ✅ | [Trader By ID](trader_by_id.md) | `ProtoTraderByIdReq` | accounts |
| ✅ | [Asset List](asset_list.md) | `ProtoAssetListReq` | assets |
| ✅ | [Asset Class List](asset_class_list.md) | `ProtoAssetClassListReq` | assets |
| ✅ | [Balance History List](balance_history_list.md) | `ProtoBalanceHistoryListReq` | balance |
| ✅ | [Bonus History List](bonus_history_list.md) | `ProtoBonusHistoryListReq` | balance |
| ✅ | [Server Settings](server_settings.md) | `ProtoServerSettingsReq` | configuration |
| ⚠️ | [Dealing Settings](dealing_settings.md) | `ProtoDealingSettingsReq` | configuration |
| ✅ | [Liquidity Feed List](liquidity_feeds.md) | `ProtoLiquidityFeedListReq` | configuration |
| ✅ | [Liquidity Feed Symbol List](liquidity_feed_symbols.md) | `ProtoLiquidityFeedSymbolListReq` | configuration |
| ✅ | [Price Stream List](price_stream_list.md) | `ProtoPriceStreamListReq` | configuration |
| ⚠️ | [Manual Deal List (Dealer Queue)](manual_deal_list.md) | `ProtoManualDealListReq` | dealing |
| ⚠️ | [Deal List By Position ID](deal_list_by_position.md) | `ProtoManagerDealListByPositionIdReq` | deals |
| ✅ | [Deal List](deal_list.md) | `ProtoManagerDealListReq` | deals |
| ✅ | [Get Deal By ID](get_deal.md) | `ProtoManagerGetDealReq` | deals |
| ✅ | [Group List (Light)](group_list.md) | `ProtoLightGroupListReq` | groups |
| ✅ | [Group By ID (Full)](group_by_id.md) | `ProtoGroupByIdReq` | groups |
| ⚠️ | [Manager List](manager_list.md) | `ProtoManagerListReq` | managers |
| ⚠️ | [Pending Order List](pending_order_list.md) | `ProtoPendingOrderListReq` | orders |
| ⚠️ | [Order Manager List (All Orders)](order_manager_list.md) | `ProtoOrderManagerListReq` | orders |
| ⚠️ | [Order Details](order_details.md) | `ProtoOrderDetailsReq` | orders |
| ⚠️ | [Open Position List](open_position_list.md) | `ProtoPositionListReq` | positions |
| ⚠️ | [Closed Position List](closed_position_list.md) | `ProtoManagerClosedPositionListReq` | positions |
| ⚠️ | [Position Details Lite](position_details_lite.md) | `ProtoPositionDetailsLiteReq` | positions |
| ✅ | [Schedule Profile List](schedule_profiles.md) | `ProtoScheduleProfileListReq` | profiles |
| ✅ | [Commission Profile List](commission_profiles.md) | `ProtoCommissionProfileListReq` | profiles |
| ✅ | [Volume Profile List](volume_profiles.md) | `ProtoVolumeProfileListReq` | profiles |
| ✅ | [Execution Profile List](execution_profiles.md) | `ProtoExecutionProfileListReq` | profiles |
| ✅ | [Protection Profile List](protection_profiles.md) | `ProtoProtectionProfileListReq` | profiles |
| ✅ | [Swap-Free Profile List](swap_free_profiles.md) | `ProtoSwapFreeProfileListReq` | profiles |
| ✅ | [Holiday List](holiday_list.md) | `ProtoHolidayListReq` | profiles |
| ✅ | [Holiday Profile List](holiday_profiles.md) | `ProtoHolidayProfileListReq` | profiles |
| ✅ | [Dynamic Leverage List](dynamic_leverage_list.md) | `ProtoDynamicLeverageListReq` | profiles |
| ✅ | [GSL Schedule List](gsl_schedule_list.md) | `ProtoGslScheduleListReq` | profiles |
| ✅ | [Swap & Dividend Profile List (Light)](light_swap_profiles.md) | `ProtoLightSwapAndDividendProfileListReq` | profiles |
| ✅ | [Country List](country_list.md) | `ProtoCountryListReq` | reference |
| ⚠️ | [Exposure Symbol List](exposure_symbols.md) | `ProtoExposureSymbolListReq` | risk |
| ⚠️ | [Recalculate Account Margin](recalc_account_margin.md) | `ProtoRecalculateAccountMarginReq` | risk |
| ✅ | [Server Time](server_time.md) | `ProtoServerTimeReq` | session |
| ✅ | [Get Auth Token](auth_token.md) | `ProtoManagerGetAuthTokenReq` | session |
| ✅ | [Symbol List](symbol_list.md) | `ProtoManagerSymbolListReq` | symbols |
| ✅ | [Symbol Category List](symbol_category_list.md) | `ProtoSymbolCategoryListReq` | symbols |


## Wire Format

```
[4 bytes big-endian length N][N bytes: serialized ProtoMessage]

ProtoMessage {
  field 1 (uint32):  payloadType   ← identifies inner message
  field 2 (bytes):   payload       ← serialized inner message
  field 3 (string):  clientMsgId   ← optional, for req/res matching
}
```

## Pagination Pattern

All list endpoints that return `hasMore=true` must be paginated:

```python
from_ts = 30_days_ago_ms
while True:
    inner = encode_int64(2, from_ts) + encode_int64(3, now_ms)
    fields = c.request(PT['DEAL_LIST_REQ'], PT['DEAL_LIST_RES'], inner)
    process(fields)
    has_more = fields.get(3, [False])[0]
    if not has_more:
        break
    # Advance cursor to last record's timestamp
    last_deal = parse_message(fields[2][-1])
    from_ts = last_deal[8][0]  # createTimestamp
```

## Key Entity Cross-Reference

| Entity | Request | payloadType | Key ID field |
|--------|---------|-------------|--------------|
| Trader (Account) | `ProtoTraderListReq` | 403 | `traderId` |
| Group | `ProtoLightGroupListReq` | 473 | `groupId` |
| Symbol | `ProtoManagerSymbolListReq` | 467 | `symbolId` |
| Asset | `ProtoAssetListReq` | 465 | `assetId` |
| Position | `ProtoPositionListReq` | 407 | `positionId` |
| Deal | `ProtoManagerDealListReq` | 431 | `dealId` |
| Order | `ProtoOrderManagerListReq` | 443 | `orderId` |
| Balance Op | `ProtoBalanceHistoryListReq` | 417 | `balanceHistoryId` |

See [error-codes.md](../error-codes.md) for full error reference.
See [events.md](events.md) for all server-pushed events.
