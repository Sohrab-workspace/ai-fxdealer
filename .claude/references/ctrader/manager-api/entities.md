# Core Entity Structures

## ProtoTrader (Account)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | traderId | int64 | Internal unique ID |
| 2 | login | int64 | Login number shown in cTrader |
| 3 | groupId | int64 | Group assignment |
| 8 | balance | int64 | Balance in cents |
| 9 | accountType | ProtoAccountType | HEDGED or NETTED |
| 10 | name | string | First name |
| 56 | lastName | string | Last name |
| 11 | passwordHash | string | MD5 hex |
| 12 | description | string | Internal note |
| 14 | countryId | int64 | Country reference |
| 16 | city | string | |
| 17 | address | string | |
| 18 | zipCode | string | |
| 19 | phone | string | |
| 21 | email | string | |
| 22 | documentId | string | KYC document number |
| 25 | registrationTimestamp | int64 | Unix ms |
| 26 | lastConnectTimestamp | int64 | Unix ms |
| 27 | online | bool | Currently connected |
| 28 | utcLastUpdateTimestamp | int64 | Unix ms |
| 29 | deleted | bool | Soft-deleted |
| 30 | balanceVersion | int64 | Optimistic lock |
| 47 | managerBonus | int64 | Manager bonus cents |
| 48 | ibBonus | int64 | IB bonus cents |
| 59 | accessRights | ProtoAccessRights | Trading permissions |
| 61 | depositAssetId | int64 | Deposit currency asset ID |
| 64 | swapFree | bool | Islamic account |
| 65 | nonWithdrawableBonus | int64 | Cents |
| 66 | leverageInCents | uint32 | e.g. 5000 = 50x |
| 74 | version | int64 | Entity version |
| 75 | subAccountOf | int64 | Parent account ID |
| 78 | isLimitedRisk | bool | No negative balance |
| 80 | moneyDigits | uint32 | Precision exponent |
| 85 | fairStopOut | bool | |

## ProtoDeal (Execution Record)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | dealId | int64 | |
| 2 | orderId | int64 | |
| 3 | positionId | int64 | |
| 4 | traderId | int64 | |
| 5 | volume | int64 | Ordered volume (cents of lot) |
| 6 | filledVolume | int64 | Actual filled (cents of lot) |
| 7 | symbolId | int64 | |
| 8 | createTimestamp | int64 | Unix ms — use for pagination |
| 9 | executionTimestamp | int64 | Unix ms |
| 10 | utcLastUpdateTimestamp | int64 | Unix ms |
| 11 | executionPrice | double | With markup |
| 12 | limitPrice | double | Requested price (if limit) |
| 13 | tradeSide | ProtoTradeSide | BUY or SELL |
| 14 | dealStatus | ProtoDealStatus | |
| 15 | dealType | ProtoDealType | |
| 16 | marginRate | double | Base-to-deposit conversion rate |
| 17 | commission | int64 | Cents |
| 19 | bookType | ProtoBookType | A or B |
| 20 | lpExecutionPrice | double | Without markup |
| 22 | label | string | Strategy label |
| 23 | channel | string | Execution channel |
| 24 | comment | string | |
| 32 | closePositionDetail | ProtoClosePositionDetail | Closing deals only |
| 35 | introducingBrokerCommission | int64 | Cents |
| 43 | markup | int64 | USD |
| 52 | manual | bool | Manually executed |
| 57 | equity | int64 | Account equity at deal time, cents |
| 58 | moneyDigits | uint32 | |

## ProtoPosition (Open/Closed Position)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | positionId | int64 | |
| 3 | tradeData | ProtoTradeData | Embedded — symbolId, volume, side, timestamps |
| 4 | positionStatus | ProtoPositionStatus | OPEN / CLOSED |
| 5 | swap | int64 | Accumulated swap cents |
| 6 | price | double | VWAP open price |
| 7 | stopLoss | double | 0 = none |
| 8 | takeProfit | double | 0 = none |
| 10 | utcLastUpdateTimestamp | int64 | Unix ms |
| 11 | bookType | ProtoBookType | |
| 13 | commission | int64 | Cents |
| 23 | usedMargin | uint64 | Cents |
| 24 | trailingStopLoss | bool | |
| 25 | stopLossTriggerMethod | ProtoOrderTriggerMethod | |
| 30 | moneyDigits | uint32 | |

## ProtoTradeData (embedded in Position and Order)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | symbolId | int64 | |
| 2 | volume | int64 | Cents of lot size |
| 3 | tradeSide | ProtoTradeSide | BUY or SELL |
| 4 | traderId | int64 | |
| 7 | openTimestamp | int64 | Unix ms |
| 8 | closeTimestamp | int64 | Unix ms (closed positions) |
| 12 | label | string | |
| 13 | comment | string | |
| 14 | channel | string | |
| 16 | lotSize | int64 | |

## ProtoOrder (Order)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | orderId | int64 | |
| 2 | tradeData | ProtoTradeData | |
| 3 | orderType | ProtoOrderType | |
| 4 | orderStatus | ProtoOrderStatus | |
| 6 | expirationTimestamp | int64 | Unix ms |
| 9 | executionPrice | double | |
| 10 | executedVolume | int64 | Cents |
| 11 | stopLoss | double | |
| 12 | takeProfit | double | |
| 13 | utcLastUpdateTimestamp | int64 | Unix ms |
| 14 | bookType | ProtoBookType | |
| 20 | closingOrder | bool | Closes a position |
| 21 | limitPrice | double | |
| 22 | stopPrice | double | |
| 23 | clientOrderId | string | Max 50 chars |
| 24 | commission | int64 | Cents |
| 26 | timeInForce | ProtoTimeInForce | |
| 30 | positionId | int64 | |
| 45 | isStopOut | bool | Triggered by stop-out |
| 46 | trailingStopLoss | bool | |
| 54 | moneyDigits | uint32 | |

## ProtoDepositWithdraw (Balance Operation)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | operationType | ProtoChangeBalanceType | |
| 2 | balanceHistoryId | int64 | |
| 3 | traderId | int64 | |
| 4 | balance | int64 | Balance after operation (cents) |
| 5 | delta | int64 | Operation amount (cents, + or -) |
| 6 | changeBalanceTimestamp | int64 | Unix ms |
| 7 | comment | string | Manager-only |
| 8 | externalNote | string | Visible to trader |
| 9 | balanceVersion | int64 | |
| 10 | equity | int64 | Account equity at time, cents |
| 14 | source | string | e.g. "VISA", "WIRE" |
| 15 | externalId | string | Reconciliation / CRM reference ID |
| 16 | moneyDigits | uint32 | |

## ProtoClosePositionDetail (inside ProtoDeal for closing deals)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 2 | entryPrice | double | Original open price |
| 3 | swap | int64 | Realized swap at close (cents) |
| 4 | commission | int64 | Closing commission (cents) |
| 7 | profit | int64 | Gross profit (cents) |
| 8 | balance | int64 | Balance after close (cents) |
| 16 | closedVolume | int64 | |
| 18 | balanceVersion | int64 | |
| 23 | equity | int64 | Cents |
| 25 | netProfit | int64 | Cents |
| 43 | moneyDigits | uint32 | |
| 44 | pnlConversionFee | int64 | Cents |

## Money / Volume Encoding

All monetary values are stored as **integers in cents**:

```python
# Amount in currency units → cents
amount_cents = int(amount_float * 10 ** money_digits)

# Cents → currency units
amount_float = amount_cents / 10 ** money_digits

# moneyDigits=2 (USD, EUR): 123456 = $1,234.56
# moneyDigits=5 (BTC):      12345678 = 0.12345678 BTC
```

Volume is stored as **cents of the lot size**:
```python
# 1.00 lot, lotSize=100000 → volume = 100000 * 100 = 10000000
```
