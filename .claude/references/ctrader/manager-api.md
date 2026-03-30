# cTrader Manager API — Complete Reference

Source: https://docs.spotware.com/en/Managers_API
Proto source: https://github.com/ivmazurenko/ctrader-managerapi-connect (community implementation)
Proto files: `CSMessages_External.proto`, `CSModelMessages_External.proto`, `CommonMessages_External.proto`, `CommonModelMessages_External.proto`

---

## 1. Connection and Authentication

### Transport

- Protocol: **Protobuf over TCP with TLS (SSL)**
- Port: **5011**
- Host: Broker-specific proxy host (obtain from Spotware support)
- Connection type: Persistent TCP, SSL-authenticated

### Establishing a Connection

```
1. Open TCP connection to <proxy_host>:5011
2. Perform TLS handshake (AuthenticateAsClient with server hostname)
3. Receive ProtoHelloEvent immediately from server (payload type = PROTO_HELLO_EVENT = 1 in CSMessages, or 990 in model numbering)
4. Send ProtoManagerAuthReq with credentials
5. Receive ProtoManagerAuthRes with permission list
6. Connection is ready for requests
```

### Heartbeat

- Send `ProtoHeartbeatEvent` (payload type = `HEARTBEAT_EVENT` = 51) every **25 seconds** to keep connection alive
- Server will also send `ProtoHeartbeatEvent` if no data is being sent in the other direction
- If heartbeat is missed, the proxy will close the connection

### Wire Format

All messages are framed with a 4-byte big-endian length prefix:

```
[4 bytes big-endian: message length] [N bytes: serialized ProtoMessage]
```

**Reading:**
1. Read 4 bytes (big-endian) → message length N
2. Read N bytes → deserialize as `ProtoMessage`
3. Read `ProtoMessage.payloadType` (uint32) to identify message type
4. Deserialize `ProtoMessage.payload` (bytes) to the appropriate message type
5. Match `ProtoMessage.clientMsgId` to correlate responses to requests

**Writing:**
1. Serialize target message (e.g., `ProtoManagerAuthReq`) to bytes
2. Wrap in `ProtoMessage`:
   - `payloadType` = message's enum value
   - `payload` = serialized bytes
   - `clientMsgId` = unique string (e.g., UUID) for request-response correlation
3. Serialize `ProtoMessage` to bytes
4. Prepend 4-byte big-endian length
5. Write to SSL stream

---

## 2. ProtoMessage Wrapper (CommonMessages_External.proto)

```proto
message ProtoMessage {
  required uint32 payloadType = 1;   // identifies payload category
  optional bytes  payload = 2;        // serialized message content
  optional string clientMsgId = 3;    // correlates responses to requests
}
```

### Common Messages

| Message | payloadType | Direction | Description |
|---------|------------|-----------|-------------|
| `ProtoErrorRes` | `ERROR_RES` = 50 | Server → Client | Error response |
| `ProtoHeartbeatEvent` | `HEARTBEAT_EVENT` = 51 | Both | Keep-alive |
| `ProtoPingReq` | `PING_REQ` = 52 | Client → Server | Latency check |
| `ProtoPingRes` | `PING_RES` = 53 | Server → Client | Latency response |
| `ProtoAvailableServicesEvent` | `AVAILABLE_SERVICES_EVENT` = 66 | Server → Client | Service availability |

#### ProtoErrorRes Fields
- `payloadType` (ProtoPayloadType, optional, default=ERROR_RES)
- `errorCode` (string, required): Error identifier string
- `description` (string, optional): Human-readable error details
- `maintenanceEndTimestamp` (uint64, optional): Unix ms when maintenance ends

#### ProtoAvailableServicesEvent Fields
- `socialAvailable` (bool, optional)
- `copyAvailable` (bool, optional)
- `datastoreAvailable` (bool, optional)
- `blotterAvailable` (bool, optional)

### Common Error Codes (ProtoErrorCode)

| Value | Code | Meaning |
|-------|------|---------|
| 1 | UNKNOWN_ERROR | Unknown error |
| 2 | UNSUPPORTED_MESSAGE | Message type not supported |
| 3 | INVALID_REQUEST | Malformed request |
| 4 | WRONG_PASSWORD | Authentication failure |
| 5 | TIMEOUT_ERROR | Request timed out |
| 6 | ENTITY_NOT_FOUND | Entity does not exist |
| 7 | CANT_ROUTE_REQUEST | Routing failure |
| 8 | FRAME_TOO_LONG | Message frame too large |
| 9 | MARKET_CLOSED | Market is closed |
| 10 | CONCURRENT_MODIFICATION | Concurrent edit conflict |
| 11 | BLOCKED_PAYLOAD_TYPE | Payload type blocked |
| 12 | DATASTORE_IS_NOT_AVAILABLE | Datastore unavailable |

---

## 3. Authentication Messages

### ProtoManagerAuthReq (payloadType = PROTO_MANAGER_AUTH_REQ = 2)

**Request:**
- `payloadType` (ProtoCSPayloadType, optional, default: PROTO_MANAGER_AUTH_REQ)
- `plantId` (string, **required**): Plant identifier (provided by Spotware)
- `environmentName` (string, **required**): Environment name (e.g., "live", "demo")
- `login` (int64, **required**): Manager login number
- `passwordHash` (string, **required**): MD5 hash of password (lowercase hex)

**Password hashing:**
```python
import hashlib
password_hash = hashlib.md5(password.encode('ascii')).hexdigest()
```

### ProtoManagerAuthRes (payloadType = PROTO_MANAGER_AUTH_RES = 3)

**Response:**
- `payloadType` (ProtoCSPayloadType, optional)
- `permission` (ProtoManagerPermission, **repeated**): List of granted permissions

### ProtoManagerGetAuthTokenReq (payloadType = PROTO_MANAGER_GET_AUTH_TOKEN_REQ = 4)

Request a token for cID authentication (no additional fields required beyond payloadType).

### ProtoManagerGetAuthTokenRes (payloadType = PROTO_MANAGER_GET_AUTH_TOKEN_RES = 5)

- `token` (string, **required**): Authentication token

### ProtoHelloEvent (payloadType = PROTO_HELLO_EVENT = 1)

Sent by server immediately on connection. No payload fields beyond payloadType.

---

## 4. All Available API Methods

### 4.1 Authentication & Session

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoManagerAuthReq | 2 | 3 | Authenticate manager |
| ProtoManagerGetAuthTokenReq | 4 | 5 | Get cID auth token |
| ProtoServerTimeReq | 16 | 17 | Get server UNIX timestamp |
| ProtoVersionReq | 106 | 107 | Get cServer version |

### 4.2 Password Management

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoChangeTraderPasswordReq | 6 | 7 | Change trader account password |
| ProtoCheckTraderPasswordReq | 8 | 9 | Check trader password |
| ProtoChangeManagerPasswordReq | 10 | 11 | Change manager password |
| ProtoCheckManagerPasswordReq | 12 | 13 | Check manager password |

### 4.3 Trader (Account) Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoTraderListReq | 26 | 27 | Get list of traders filtered by registrationTimestamp |
| ProtoTraderByIdReq | 100 | 101 | Get trader(s) by ID |
| ProtoCrudTraderReq | 60 | 61 | Create/update/delete trader |

### 4.4 Position Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoPositionListReq | 32 | 33 | Get open positions filtered by open timestamp |
| ProtoManagerClosedPositionListReq | 114 | 115 | Get closed positions |
| ProtoPositionDetailsLiteReq | 116 | 117 | Get position info by ID (includes SL/TP changes, swap records) |
| ProtoManagerAmendPositionReq | 121 | — | Amend position SL/TP |
| ProtoManagerClosePositionReq | 122 | — | Close position |
| ProtoForceClosePositionReq | 166 | — | Force close position (bypasses normal checks) |
| ProtoForceOpenPositionReq | 167 | — | Force open position (bypasses normal checks) |

### 4.5 Order Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoPendingOrderListReq | 34 | 35 | Get pending orders filtered by timestamp |
| ProtoOrderManagerListReq | 110 | 111 | Get orders filtered by utcLastUpdateTimestamp |
| ProtoManagerOrderListByPositionIdReq | 54 | 55 | Get orders for a specific position |
| ProtoOrderDetailsReq | 18 | 19 | Get order details plus related deals and actions |
| ProtoManagerNewOrderReq | 118 | — | Create and send new order |
| ProtoManagerAmendOrderReq | 119 | — | Amend existing order |
| ProtoManagerCancelOrderReq | 120 | — | Cancel order |

### 4.6 Deal Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoManagerDealListReq | 50 | 51 | Get deals filtered by creation timestamp |
| ProtoManagerDealListByPositionIdReq | 52 | 53 | Get deals related to a position |
| ProtoManagerGetDealReq | 112 | 113 | Get single deal by ID |

### 4.7 Balance & Bonus Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoChangeBalanceReq | 74 | 75 | Deposit/withdraw from trader balance |
| ProtoBalanceHistoryListReq | 36 | 37 | Get balance history (deposits/withdrawals) |
| ProtoManagerChangeBonusReq | 126 | 127 | Credit/debit trader bonus |
| ProtoBonusHistoryListReq | 38 | 39 | Get bonus history |
| ProtoManagerBalanceTransferReq | 168 | 169 | Transfer funds between traders |

### 4.8 Group Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoLightGroupListReq | 24 | 25 | Get groups with limited fields |
| ProtoGroupByIdReq | 102 | 103 | Get group by ID |
| ProtoCrudGroupReq | 64 | 65 | Create/update/delete group |

### 4.9 Manager Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoManagerListReq | 30 | 31 | Get list of managers |
| ProtoCrudManagerReq | 66 | 67 | Create/update/delete manager |

### 4.10 Symbol Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoManagerSymbolListReq | 28 | 29 | Get all symbols |
| ProtoCreateSymbolReq | 212 | 213 | Create new symbol |
| ProtoCrudSymbolReq | 62 | 63 | Update/delete symbol |
| ProtoSymbolCategoryListReq | 128 | 129 | Get symbol categories |
| ProtoGetSymbolsForConversionReq | 130 | 131 | Get conversion chain between two assets |

### 4.11 Asset Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoAssetListReq | 44 | 45 | Get all assets |
| ProtoCrudAssetReq | 68 | 69 | Create/update/delete asset |
| ProtoAssetClassListReq | 108 | 109 | Get asset classes |

### 4.12 Liquidity Feed Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoLiquidityFeedListReq | 48 | 49 | Get liquidity feeds |
| ProtoLiquidityFeedSymbolListReq | 210 | 211 | Get feed-symbol mappings |
| ProtoCrudLiquidityFeedSymbolReq | 70 | 71 | Create/update/delete feed-symbol link |

### 4.13 Price Stream Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoPriceStreamListReq | 46 | 47 | Get price streams |
| ProtoCreatePriceStreamReq | 78 | 79 | Create price stream |
| ProtoDeletePriceStreamReq | 80 | 81 | Delete price stream |
| ProtoUpdatePriceStreamReq | 82 | 83 | Update price stream |

### 4.14 Exposure

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoExposureSymbolListReq | 40 | 41 | Get exposure per symbol |

### 4.15 Server Settings

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoServerSettingsReq | 42 | 43 | Get server settings |
| ProtoUpdateServerSettingsReq | 76 | 77 | Update server settings |

### 4.16 Margin Operations

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoRecalculateAccountMarginReq | 20 | 21 | Recalculate trader margin |
| ProtoRecalculateSymbolMarginReq | 22 | 23 | Recalculate margin for symbol margin settings change |
| ProtoRecalculateDynamicLeverageMarginReq | 220 | 221 | Recalculate margins for dynamic leverage change |

### 4.17 Profile CRUD Operations

| Profile Type | List Req | List Res | CRUD Req | CRUD Res | Description |
|---|---|---|---|---|---|
| Dynamic Leverage | 56 | 57 | 84 | 85 | Tiered leverage |
| GSL Schedule | 58 | 59 | 86 | 87 | Guaranteed SL schedule |
| Swap & Dividend | 216 | 217 | 72 | 73 | Swap profiles |
| Commission | 178 | 179 | 175 | 176 | Commission rates |
| Execution | 188 | 189 | 185 | 186 | Execution policies |
| Protection | 193 | 194 | 190 | 191 | Risk protection |
| Volume | 183 | 184 | 180 | 181 | Volume limits |
| Schedule | 173 | 174 | 170 | 171 | Trading schedules |
| Swap Free | 198 | 199 | 195 | 196 | Islamic accounts |
| Holiday | 203 | 204 | 200 | 201 | Holiday dates |
| Holiday Profile | 208 | 209 | 205 | 206 | Holiday profiles |
| Max AutoExec Size | 155 | 156 | 152 | 153 | Auto execution sizing |

### 4.18 Dealing (Manual Execution)

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoDealingSettingsReq | 132 | 133 | Get dealing settings |
| ProtoUpdateDealingSettingsReq | 134 | 135 | Update dealing settings |
| ProtoManualDealListReq | 136 | 137 | Get pending manual deals |
| ProtoManualDealClaimReq | 139 | 140 | Claim manual deal for processing |
| ProtoManualDealUnclaimReq | 142 | 143 | Release claimed deal |
| ProtoManualDealResetReq | 145 | 146 | Reset deal to unclaimed state |
| ProtoManualDealRejectReq | 147 | 148 | Reject manual deal |
| ProtoManualDealExecuteReq | 149 | 150 | Execute manual deal at price |

### 4.19 Dealer Order Operations (bypass normal validation)

| Request Message | Req Type | Description |
|-----------------|----------|-------------|
| ProtoDealerNewOrderReq | 157 | Create order (dealer mode, ignoreValidation available) |
| ProtoDealerAmendOrderReq | 158 | Amend order (dealer mode) |
| ProtoDealerCancelOrderReq | 159 | Cancel order (dealer mode) |
| ProtoDealerAmendPositionReq | 160 | Amend position (dealer mode) |
| ProtoDealerClosePositionReq | 161 | Close position (dealer mode) |

### 4.20 Country

| Request Message | Req Type | Res Type | Description |
|-----------------|----------|----------|-------------|
| ProtoCountryListReq | 104 | 105 | Get list of countries |

---

## 5. Request and Response Message Structures

### ProtoTraderListReq (payloadType = 26)

```proto
message ProtoTraderListReq {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_TRADER_LIST_REQ];
  required int64 fromTimestamp = 2;   // Filter by registrationTimestamp >= fromTimestamp (Unix ms)
  required int64 toTimestamp = 3;     // Filter by registrationTimestamp <= toTimestamp (Unix ms)
  optional int64 groupId = 4;         // Filter by group
  optional bool hideIbParameters = 5; // Hide IB-specific fields
  optional bool onlySubAccounts = 6;  // Return only sub-accounts
}
```

### ProtoTraderListRes (payloadType = 27)

```proto
message ProtoTraderListRes {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_TRADER_LIST_RES];
  repeated ProtoTrader trader = 2;   // List of traders
  required bool hasMore = 3;          // True if result was truncated
}
```

**Note:** If `hasMore = true`, repeat the request with a new `fromTimestamp` set to the `registrationTimestamp` of the last returned trader.

### ProtoTraderByIdReq (payloadType = 100)

```proto
message ProtoTraderByIdReq {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_TRADER_BY_ID_REQ];
  repeated int64 traderId = 2;  // One or more trader IDs
}
```

### ProtoManagerDealListReq (payloadType = 50)

```proto
message ProtoManagerDealListReq {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_MANAGER_DEAL_LIST_REQ];
  repeated int64 traderId = 2;                 // Filter by specific traders (empty = all)
  required int64 fromTimestamp = 3;            // Filter by createTimestamp >= (Unix ms)
  required int64 toTimestamp = 4;              // Filter by createTimestamp <= (Unix ms)
  optional int32 maxRows = 5;                   // Limit result count
  optional bool closingDealsOnly = 6 [default = false];
  optional bool includeAdditionalVolumes = 7 [default = false];
  optional bool withFilledVolumeOnly = 8 [default = false];
  repeated int64 groupId = 9;                   // Filter by group IDs
}
```

### ProtoManagerDealListRes (payloadType = 51)

```proto
message ProtoManagerDealListRes {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_MANAGER_DEAL_LIST_RES];
  repeated ProtoDeal deal = 2;
  required bool hasMore = 3;  // True if result was truncated - paginate by advancing fromTimestamp
}
```

### ProtoPositionListReq (payloadType = 32)

```proto
message ProtoPositionListReq {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_POSITION_LIST_REQ];
  optional int64 traderId = 2;         // Filter by trader (empty = all)
  required int64 fromTimestamp = 3;    // Filter by openTimestamp >=
  required int64 toTimestamp = 4;      // Filter by openTimestamp <=
}
```

### ProtoPositionListRes (payloadType = 33)

```proto
message ProtoPositionListRes {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_POSITION_LIST_RES];
  optional int64 traderId = 2;
  repeated ProtoPosition position = 3;
  required bool hasMore = 4;
}
```

### ProtoChangeBalanceReq (payloadType = 74)

```proto
message ProtoChangeBalanceReq {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_CHANGE_BALANCE_REQ];
  required int64 traderId = 2;
  required int64 amount = 3;           // Amount in cents (e.g., 10000 = $100.00)
  optional string comment = 4;          // Visible to managers only
  required ProtoChangeBalanceType type = 5;  // See ProtoChangeBalanceType enum
  optional int64 managerId = 6;
  optional string externalNote = 7;     // Visible to trader and managers
  optional string source = 8;           // Payment source (e.g., "VISA")
  optional string externalId = 9;       // Third-party reconciliation ID
  optional bool newWay = 10;
}
```

### ProtoChangeBalanceRes (payloadType = 75)

```proto
message ProtoChangeBalanceRes {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_CHANGE_BALANCE_RES];
  required int64 traderId = 2;
  required int64 balanceHistoryId = 3;  // ID for audit trail
}
```

### ProtoManagerNewOrderReq (payloadType = 118)

```proto
message ProtoManagerNewOrderReq {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_MANAGER_NEW_ORDER_REQ];
  required uint64 traderId = 2;
  required int64 symbolId = 3;
  required ProtoOrderType orderType = 4;
  required ProtoTradeSide tradeSide = 5;
  required int64 volume = 6;              // Volume in cents
  optional double limitPrice = 7;
  optional double stopPrice = 8;
  optional ProtoTimeInForce timeInForce = 9 [default = GOOD_TILL_CANCEL];
  optional int64 expirationTimestamp = 10;
  optional double stopLoss = 12;
  optional double takeProfit = 13;
  optional string comment = 16;
  optional string method = 17;
  optional double baseSlippagePrice = 19;
  optional string label = 21;
  optional string channel = 22;
  optional int64 positionId = 23;         // For closing orders
  optional string clientOrderId = 24;     // Max 50 chars
  optional string clientToken = 25;
  optional int64 relativeStopLoss = 26;   // In points
  optional int64 relativeTakeProfit = 27; // In points
  optional bool trailingStopLoss = 30;
  optional ProtoOrderTriggerMethod stopTriggerMethod = 31 [default = TRADE];
  optional ProtoOrderTriggerMethod stopLossTriggerMethod = 32 [default = TRADE];
  optional int32 slippageInPoints = 33;
  optional int64 desiredOpenTimestamp = 34; // For MARKET_ON_OPEN orders
}
```

Order response is a `ProtoExecutionEvent` (not a direct Res), sent asynchronously on the `MessageWithoutIdReceived` event.

### ProtoManagerClosePositionReq (payloadType = 122)

```proto
message ProtoManagerClosePositionReq {
  optional ProtoCSPayloadType payloadType = 1 [default = PROTO_MANAGER_CLOSE_POSITION_REQ];
  required uint64 traderId = 2;
  required int64 positionId = 3;
  required int64 volume = 4;       // Partial close if < position volume (cents)
  optional string channel = 7;
}
```

---

## 6. Core Entity Structures

### ProtoTrader (Account)

| Field | Type | Description |
|-------|------|-------------|
| traderId | int64 | Internal trader ID |
| login | int64 | Login number |
| groupId | int64 | Group ID |
| balance | int64 | Balance in cents |
| accountType | ProtoAccountType | HEDGED / NETTED / SPREAD_BETTING |
| name | string | First name |
| lastName | string | Last name |
| email | string | Email address |
| passwordHash | string | MD5 password hash |
| countryId | int64 | Country ID |
| phone | string | Phone number |
| registrationTimestamp | int64 | Registration time (Unix ms) |
| lastConnectTimestamp | int64 | Last login time (Unix ms) |
| online | bool | Currently online |
| utcLastUpdateTimestamp | int64 | Last update (Unix ms) |
| deleted | bool | Deletion flag |
| accessRights | ProtoAccessRights | FULL_ACCESS / CLOSE_ONLY / NO_TRADING / NO_LOGIN |
| swapFree | bool | Islamic account |
| leverageInCents | uint32 | Account leverage (e.g., 5000 = 50x) |
| depositAssetId | int64 | Deposit currency asset ID |
| nonWithdrawableBonus | int64 | Non-withdrawable bonus in cents |
| managerBonus | int64 | Broker bonus in cents |
| ibBonus | int64 | IB bonus in cents |
| balanceVersion | int64 | Balance version for optimistic locking |
| moneyDigits | uint32 | Monetary precision exponent |
| version | int64 | Entity version |
| maxLeverage | uint32 | Maximum leverage cap |
| isLimitedRisk | bool | Limited risk account (no negative balance) |
| subAccountOf | int64 | Parent account ID for subaccounts |

### ProtoDeal (Execution Record)

| Field | Type | Description |
|-------|------|-------------|
| dealId | int64 | Deal ID |
| orderId | int64 | Related order ID |
| positionId | int64 | Related position ID |
| traderId | int64 | Trader ID |
| volume | int64 | Requested volume in cents |
| filledVolume | int64 | Filled volume in cents |
| symbolId | int64 | Symbol ID |
| createTimestamp | int64 | Creation time (Unix ms) |
| executionTimestamp | int64 | Execution time (Unix ms) |
| utcLastUpdateTimestamp | int64 | Last update (Unix ms) |
| executionPrice | double | Execution price (with markups) |
| limitPrice | double | Limit price (for market orders) |
| tradeSide | ProtoTradeSide | BUY or SELL |
| dealStatus | ProtoDealStatus | FILLED / PARTIALLY_FILLED / REJECTED / ERROR |
| dealType | ProtoDealType | MARKET_DEAL / LIMIT_DEAL |
| marginRate | double | Base-to-deposit conversion rate |
| commission | int64 | Trading commission in cents |
| bookType | ProtoBookType | BOOK_A or BOOK_B |
| lpExecutionPrice | double | LP execution price (without markups) |
| closePositionDetail | ProtoClosePositionDetail | Populated for closing deals |
| introducingBrokerCommission | int64 | IB commission in cents |
| equity | int64 | Trader equity at deal time |
| moneyDigits | uint32 | Monetary precision exponent |
| markup | int64 | Deal markup in USD |
| label | string | Order label |
| channel | string | Order channel |
| comment | string | Order comment |
| manual | bool | True if manually executed |

### ProtoPosition (Open Position)

| Field | Type | Description |
|-------|------|-------------|
| positionId | int64 | Position ID |
| tradeData | ProtoTradeData | Symbol, volume, side, trader, timestamps |
| positionStatus | ProtoPositionStatus | OPEN / CLOSED / CREATED / ERROR |
| swap | int64 | Accumulated swap in cents |
| price | double | VWAP open price |
| stopLoss | double | Stop loss price |
| takeProfit | double | Take profit price |
| utcLastUpdateTimestamp | int64 | Last update (Unix ms) |
| bookType | ProtoBookType | BOOK_A or BOOK_B |
| commission | int64 | Unrealized commission in cents |
| usedMargin | uint64 | Margin used in cents |
| trailingStopLoss | bool | Trailing SL active |
| moneyDigits | uint32 | Monetary precision exponent |

### ProtoOrder (Order)

| Field | Type | Description |
|-------|------|-------------|
| orderId | int64 | Order ID |
| tradeData | ProtoTradeData | Trading details |
| orderType | ProtoOrderType | MARKET / LIMIT / STOP / STOP_LIMIT |
| orderStatus | ProtoOrderStatus | ACCEPTED / FILLED / REJECTED / EXPIRED / CANCELLED |
| executionPrice | double | Filled price |
| executedVolume | int64 | Filled volume in cents |
| stopLoss | double | Stop loss price |
| takeProfit | double | Take profit price |
| limitPrice | double | Limit price |
| stopPrice | double | Stop price |
| utcLastUpdateTimestamp | int64 | Last update (Unix ms) |
| commission | int64 | Trading commission in cents |
| timeInForce | ProtoTimeInForce | GTC / GTD / IOC / FOK / MOO |
| positionId | int64 | Related position ID |
| clientOrderId | string | Client-supplied ID (max 50 chars) |
| closingOrder | bool | True if closing position |
| isStopOut | bool | True if triggered by stop-out |
| moneyDigits | uint32 | Monetary precision exponent |

### ProtoDepositWithdraw (Balance Operation)

| Field | Type | Description |
|-------|------|-------------|
| operationType | ProtoChangeBalanceType | Balance operation type |
| balanceHistoryId | int64 | Unique history record ID |
| traderId | int64 | Trader ID |
| balance | int64 | Balance after operation (cents) |
| delta | int64 | Operation amount (cents) |
| changeBalanceTimestamp | int64 | Operation timestamp (Unix ms) |
| comment | string | Manager-only comment |
| externalNote | string | Visible to trader and managers |
| balanceVersion | int64 | Balance version |
| equity | int64 | Equity after operation (cents) |
| nonWithdrawableBonus | int64 | Non-withdrawable bonus |
| source | string | Payment source (e.g., "VISA") |
| externalId | string | Third-party reconciliation ID |
| moneyDigits | uint32 | Monetary precision exponent |

### ProtoClosePositionDetail (Closing Deal Financials)

| Field | Type | Description |
|-------|------|-------------|
| entryPrice | double | Position entry price |
| profit | int64 | Realized gross profit (cents) |
| swap | int64 | Realized swap (cents) |
| commission | int64 | Realized commission (cents) |
| balance | int64 | Account balance after (cents) |
| equity | int64 | Account equity after (cents) |
| netProfit | int64 | Net realized profit (cents) |
| closedVolume | int64 | Closed volume (cents) |
| balanceVersion | int64 | Balance version |
| quoteToDepositConversionRate | double | Currency conversion rate |
| moneyDigits | uint32 | Monetary precision exponent |

### ProtoTradeData (Trading Details, embedded in Position/Order)

| Field | Type | Description |
|-------|------|-------------|
| symbolId | int64 | Symbol ID |
| volume | int64 | Volume in cents |
| tradeSide | ProtoTradeSide | BUY or SELL |
| traderId | int64 | Trader ID |
| openTimestamp | int64 | Open time (Unix ms) |
| closeTimestamp | int64 | Close time (Unix ms) |
| label | string | Text label |
| comment | string | Order comment |
| channel | string | Channel identifier |
| lotSize | int64 | Lot size in cents |

### ProtoGroup (Trader Group)

| Field | Type | Description |
|-------|------|-------------|
| groupId | int64 | Group ID |
| name | string | Group name |
| enabled | bool | Active flag |
| marginStopout | double | Stop-out margin level (%) |
| priceStreamId | int64 | Price stream ID |
| swapAndDividendProfileId | int64 | Swap profile |
| isDealingDesk | bool | Manual dealing desk |
| utcLastUpdateTimestamp | int64 | Last update (Unix ms) |
| deleted | bool | Deletion flag |
| symbol | repeated ProtoGroupSymbol | Per-symbol settings |

### ProtoManagerSymbol (Symbol)

| Field | Type | Description |
|-------|------|-------------|
| symbolId | int64 | Symbol ID |
| name | string | Symbol name |
| digits | int32 | Price precision |
| pipPosition | int32 | Pip position |
| enabled | bool | Visibility flag |
| tradingMode | ProtoTradingMode | ENABLED / DISABLED / CLOSE_ONLY |
| lotSize | int64 | Lot size in cents |
| baseAssetId | int64 | Base asset ID |
| quoteAssetId | int64 | Quote asset ID |
| utcLastUpdateTimestamp | int64 | Last update (Unix ms) |

---

## 7. Event Messages (Server-Pushed, No clientMsgId)

Events arrive on the connection without a `clientMsgId`. Handle them in a separate message handler.

### Trading Events

| Event Message | Type | Description |
|---------------|------|-------------|
| ProtoExecutionEvent | 14 | Order accepted/filled/rejected, position opened/closed, balance change |
| ProtoMarginChangedEvent | 15 | Position margin updated |
| ProtoOrderErrorEvent | 123 | Error during order processing |
| ProtoTraderLogonEvent | 124 | Trader logged in |
| ProtoTraderLogoutEvent | 125 | Trader logged out |
| ProtoNewManualDealEvent | 138 | New manual deal created (dealing desk) |
| ProtoManualDealClaimedEvent | 141 | Manual deal claimed by a manager |
| ProtoManualDealUnclaimedEvent | 144 | Manual deal released |
| ProtoManualDealProcessedEvent | 151 | Manual deal processing finished |

### ProtoExecutionEvent Fields

| Field | Type | Description |
|-------|------|-------------|
| executionType | ProtoExecutionType | Type of execution event |
| position | ProtoPosition | Position (if applicable) |
| order | ProtoOrder | Order (if applicable) |
| errorCode | string | Error code (if rejected) |
| depositWithdraw | ProtoDepositWithdraw | Balance operation (if applicable) |
| deal | ProtoDeal | Deal (if filled) |
| eventId | uint64 | Event sequence ID |
| bonusDepositWithdraw | ProtoBonusDepositWithdraw | Bonus operation (if applicable) |
| depositToUsdRate | double | Deposit to USD conversion rate |

### ProtoExecutionType Values

| Value | Name | Meaning |
|-------|------|---------|
| 0 | ORDER_ACCEPTED | Order accepted by server |
| 1 | ORDER_FILLED | Order fully or partially filled |
| 2 | ORDER_REJECTED | Order rejected |
| 3 | POSITION_OPENED | New position opened |
| 4 | POSITION_CLOSED | Position closed |
| 5 | POSITION_PARTIALLY_CLOSED | Partial close |
| 6 | DEPOSIT_PERFORMED | Balance deposit |
| 7 | WITHDRAWAL_PERFORMED | Balance withdrawal |

### Entity Change Events

| Event Message | Type | Description |
|---------------|------|-------------|
| ProtoTraderChangedEvent | 88 | Trader created/updated/deleted |
| ProtoGroupChangedEvent | 89 | Group created/updated/deleted |
| ProtoManagerSymbolChangedEvent | 90 | Symbol created/updated/deleted |
| ProtoManagerChangedEvent | 91 | Manager created/updated/deleted |
| ProtoServerSettingsChangedEvent | 92 | Server settings changed |
| ProtoAssetChangedEvent | 97 | Asset created/updated/deleted |
| ProtoTraderPermissionLoseEvent | 96 | Manager lost access to a trader |
| ProtoDealingSettingsUpdatedEvent | 219 | Dealing settings changed |

---

## 8. Error Codes

### ProtoCSErrorCode (from CSModelMessages)

| Code | Name | Meaning |
|------|------|---------|
| 1 | NOT_ENOUGH_MONEY | Insufficient balance |
| 2 | NOT_ENOUGH_RIGHTS | Permission denied |
| 3 | AUTHENTICATION_FAILED | Wrong credentials |
| 4 | POSITION_NOT_FOUND | Position ID invalid |
| 5 | POSITION_LOCKED | Position being modified |
| 6 | CHANGE_BALANCE_BAD_AMOUNT | Invalid balance amount |
| 7 | NO_QUOTES | No market data |
| 8 | TRADING_DISABLED | Trading not enabled |
| 9 | TRADING_NOT_ALLOWED | Trading permission denied |
| 10 | TRADING_BAD_VOLUME | Invalid order volume |
| 11 | TRADER_NOT_FOUND | Trader ID invalid |
| 12 | TRADER_GROUP_NOT_FOUND | Group ID invalid |
| 13 | RECONCILIATION_IN_PROGRESS | System reconciling |
| 14 | ALREADY_LOGGED_IN | Already connected |
| 16 | TOO_MANY_POSITIONS | Position limit exceeded |
| 17 | ORDER_NOT_FOUND | Order ID invalid |
| 18 | TRADING_BAD_STOPS | Invalid SL/TP |
| 19 | ALREADY_DELETED | Entity already deleted |
| 20 | WRONG_LEVERAGE | Leverage invalid |
| 21 | TRADING_BAD_EXPIRATION_DATE | Invalid expiration |
| 22 | ALREADY_SUBSCRIBED | Already subscribed |
| 23 | REQUEST_FREQUENCY_EXCEEDED | Rate limit exceeded |
| 24 | POSITION_NOT_OPEN | Position already closed |
| 25 | WRONG_TIME_SEQUENCE | Timestamp sequence error |
| 26 | FORBID_WITH_TRADING_ENABLED | Forbidden while trading active |
| 27 | INCORRECT_POSITION_ID | Position ID format error |
| 28 | TRADER_HAS_POSITIONS | Trader has open positions |
| 29 | UNKNOWN_LIQIDITY_FEED | Liquidity feed invalid |
| 32 | TRADING_BAD_PRICES | Price out of range |
| 34 | UNKNOWN_SYMBOL | Symbol ID invalid |
| 36 | SYMBOL_NOT_FOUND | Symbol not found |
| 37 | DEAL_NOT_FOUND | Deal ID invalid |
| 41 | UNABLE_TO_CANCEL_ORDER | Cancel failed |
| 42 | UNABLE_TO_AMEND_ORDER | Amend failed |
| 45 | SHORT_SELLING_NOT_ALLOWED | Short selling disabled |
| 47 | SERVER_IS_UNDER_MAINTENANCE | Maintenance in progress |
| 52 | INVALID_DATA | Invalid data format |
| 53 | NO_SUCH_LOGIN | Login does not exist |
| 54 | MAX_EXPOSURE_REACHED | Exposure limit exceeded |
| 60 | SYMBOL_NAME_ALREADY_EXIST | Duplicate symbol name |
| 62 | OPERATION_NOT_ALLOWED | Operation not permitted |
| 63 | CHANNEL_IS_BLOCKED | Trading channel blocked |
| 67 | CONNECTIONS_LIMIT_EXCEEDED | Too many connections |
| 69 | SYMBOL_HAS_HOLIDAY | Symbol on holiday |

### ProtoResultCode

| Code | Status | Meaning |
|------|--------|---------|
| 0 | RET_OK | Success |
| 1 | RET_OK_NONE | Success but no data |
| 2 | RET_ERROR | General error |
| 3 | RET_INVALID_DATA | Invalid request |
| 4 | RET_TECH_PROBLEM | Technical issue |
| 5 | RET_OLD_VERSION | Protocol outdated |
| 6 | RET_NO_CONNECT | Connection lost |
| 7 | RET_NOT_ENOUGH_RIGHTS | Insufficient permissions |
| 8 | RET_TOO_FREQUENT | Rate limit exceeded |
| 128 | RET_TRADE_TIMEOUT | Trade timeout |
| 130 | RET_TRADE_BAD_STOPS | Invalid SL/TP |
| 131 | RET_TRADE_BAD_VOLUME | Invalid volume |
| 132 | RET_TRADE_MARKET_CLOSED | Market closed |
| 133 | RET_TRADE_DISABLE | Trading disabled |
| 134 | RET_TRADE_NO_MONEY | Insufficient balance |
| 137 | RET_TRADE_REQUOTE | Requote required |

---

## 9. Key Enumerations

### ProtoOrderType

| Value | Name | Description |
|-------|------|-------------|
| 0 | MARKET | Immediate market execution |
| 1 | LIMIT | Execute at limit price or better |
| 2 | STOP | Execute at stop price or worse |
| 3 | MARKET_RANGE | Market order with price range |
| 4 | STOP_LIMIT | Stop order that becomes a limit |

### ProtoTradeSide

| Value | Name |
|-------|------|
| 0 | BUY |
| 1 | SELL |

### ProtoTimeInForce

| Value | Name | Description |
|-------|------|-------------|
| 0 | GOOD_TILL_CANCEL | Valid until cancelled |
| 1 | GOOD_TILL_DATE | Valid until specified date |
| 2 | IMMEDIATE_OR_CANCEL | Fill immediately or cancel |
| 3 | FILL_OR_KILL | Fill all or cancel |
| 4 | MARKET_ON_OPEN | Execute at next market open |

### ProtoPositionStatus

| Value | Name |
|-------|------|
| 1 | POSITION_STATUS_OPEN |
| 2 | POSITION_STATUS_CLOSED |
| 3 | POSITION_STATUS_CREATED |
| 4 | POSITION_STATUS_ERROR |

### ProtoOrderStatus

| Value | Name |
|-------|------|
| 1 | ORDER_STATUS_ACCEPTED |
| 2 | ORDER_STATUS_FILLED |
| 3 | ORDER_STATUS_REJECTED |
| 4 | ORDER_STATUS_EXPIRED |
| 5 | ORDER_STATUS_CANCELLED |

### ProtoDealStatus

| Value | Name |
|-------|------|
| 2 | FILLED |
| 3 | PARTIALLY_FILLED |
| 4 | REJECTED |
| 5 | INTERNALLY_REJECTED |
| 6 | ERROR |
| 7 | MISSED |

### ProtoAccountType

| Value | Name | Description |
|-------|------|-------------|
| 0 | HEDGED | Multiple positions per symbol |
| 1 | NETTED | Single position per symbol |
| 2 | SPREAD_BETTING | Spread betting |

### ProtoAccessRights

| Value | Name | Description |
|-------|------|-------------|
| 0 | FULL_ACCESS | Full trading allowed |
| 1 | CLOSE_ONLY | Can only close positions |
| 2 | NO_TRADING | No trading allowed |
| 3 | NO_LOGIN | Cannot login |

### ProtoBookType

| Value | Name | Description |
|-------|------|-------------|
| 0 | BOOK_A | A-book (LP/bank liquidity) |
| 1 | BOOK_B | B-book (market maker) |

### ProtoCrudOperation

| Value | Name | Description |
|-------|------|-------------|
| 0 | CREATE | Create entity (ID must be 0) |
| 1 | UPDATE | Full update (nulls clear fields) |
| 2 | UPDATE_DIFF | Partial update (only specified fields) |
| 3 | DELETE | Delete entity |

### ProtoChangeBalanceType (key values)

| Value | Name | Description |
|-------|------|-------------|
| 0 | BALANCE_DEPOSIT | Client deposit |
| 1 | BALANCE_WITHDRAW | Client withdrawal |
| 2 | BALANCE_CLOSE_POSITION | Position P&L |
| 5 | BALANCE_DEPOSIT_IB_COMMISSIONS | IB commission credit |
| 9 | BALANCE_DEPOSIT_REBATE | Rebate credit |
| 10 | BALANCE_WITHDRAW_REBATE | Rebate debit |
| 15 | BALANCE_DEPOSIT_DIVIDENDS | Dividend credit |
| 17 | BALANCE_WITHDRAW_GSL_CHARGE | GSL fee |
| 18 | BALANCE_WITHDRAW_ROLLOVER | Rollover/swap charge |
| 19 | BALANCE_DEPOSIT_NONWITHDRAWABLE_BONUS | Non-withdrawable bonus |
| 20 | BALANCE_WITHDRAW_NONWITHDRAWABLE_BONUS | Non-withdrawable bonus debit |
| 21 | BALANCE_DEPOSIT_SWAP | Swap credit |
| 22 | BALANCE_WITHDRAW_SWAP | Swap charge |
| 35 | BALANCE_WITHDRAW_INACTIVITY_FEE | Inactivity fee |
| 36 | BALANCE_DEPOSIT_TRANSFER | Transfer in |
| 37 | BALANCE_WITHDRAW_TRANSFER | Transfer out |

### ProtoTradingMode

| Value | Name | Description |
|-------|------|-------------|
| 0 | ENABLED | Full trading |
| 1 | DISABLED_WITHOUT_PENDINGS_EXECUTION | Disabled, pending orders don't execute |
| 2 | DISABLED_WITH_PENDINGS_EXECUTION | Disabled, pending orders execute |
| 3 | CLOSE_ONLY_MODE | Close orders only |

---

## 10. Pagination

Many list requests return `hasMore = true` when results are truncated. Pagination strategy:

- For **dealer/position/order** lists: use the `utcLastUpdateTimestamp` of the last returned record as the new `fromTimestamp`
- For **trader lists**: use the `registrationTimestamp` of the last returned trader
- For **deal lists**: use the `createTimestamp` of the last returned deal
- Continue paginating until `hasMore = false`

---

## 11. Important Notes

### Monetary Values

- All monetary values are in **cents** (integer): `balance = 10000` = $100.00
- Use `moneyDigits` field to determine the actual precision exponent (e.g., `moneyDigits = 2` means divide by 100)
- Volume is in **cents** of the base currency's lot size

### Timestamps

- All timestamps are **Unix milliseconds** (int64)
- Server time reference: use `ProtoServerTimeReq`

### Proto File Acquisition

The Manager API `.proto` files are **not publicly distributed**. Contact `support@spotware.com` to request them. The community implementation at https://github.com/ivmazurenko/ctrader-managerapi-connect contains the `CSMessages_External.proto` and `CSModelMessages_External.proto` files which reflect the current schema.

### Rate Limits

- Error code `REQUEST_FREQUENCY_EXCEEDED` (23) / `RET_TOO_FREQUENT` (8) is returned when limits are hit
- No specific rate limit numbers are published — implement exponential backoff

### Connection Details

- Connection details (proxy host) are broker-specific — obtain from Spotware support
- IP whitelisting may be required — contact `support@spotware.com`
- The proxy handles TLS — no additional application-level encryption needed

### Manager Permissions (ProtoManagerPermission)

Returned in `ProtoManagerAuthRes.permission[]`. These control what operations the authenticated manager can perform. Exact permission enum values are defined in the proto file but require the actual file from Spotware.

---

## 12. Python Integration Notes

```python
import socket
import ssl
import struct
import hashlib
# pip install protobuf

# Password hashing
password_hash = hashlib.md5(password.encode('ascii')).hexdigest()

# Frame reading
def read_message(sock):
    length_bytes = recv_all(sock, 4)
    length = struct.unpack('>I', length_bytes)[0]  # big-endian uint32
    data = recv_all(sock, length)
    proto_msg = ProtoMessage()
    proto_msg.ParseFromString(data)
    return proto_msg

# Frame writing
def send_message(sock, proto_msg, client_msg_id=None):
    if client_msg_id:
        proto_msg.clientMsgId = client_msg_id
    data = proto_msg.SerializeToString()
    length = struct.pack('>I', len(data))  # big-endian uint32
    sock.sendall(length + data)

# SSL connection
context = ssl.create_default_context()
raw_sock = socket.create_connection((host, 5011))
ssl_sock = context.wrap_socket(raw_sock, server_hostname=host)
```

### Recommended Python Libraries

- `protobuf` — Google's official Python protobuf library
- `grpcio` — only needed if using gRPC transport (not required for raw TCP)
- No gRPC required — this is raw TCP with Protobuf serialization, not gRPC

---

## 13. Proto File Acquisition

To obtain the official `.proto` files:
1. Contact Spotware support: `support@spotware.com`
2. Request Manager API access and proto file package
3. Files needed: `CSMessages.proto`, `CSModelMessages.proto`, `CommonMessages.proto`, `CommonModelMessages.proto`

Community reference implementation (C#): https://github.com/ivmazurenko/ctrader-managerapi-connect

---

Sources:
- https://docs.spotware.com/Managers_API
- https://docs.spotware.com/en/Managers_API/Trading_and_Pricing
- https://docs.spotware.com/en/Managers_API/CRUDs
- https://docs.spotware.com/Managers_API/Lists
- https://github.com/ivmazurenko/ctrader-managerapi-connect
