# Manager's API — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/Managers_API
>   - https://docs.spotware.com/en/Managers_API/CRUDs
>   - https://docs.spotware.com/Managers_API/Trading_and_Pricing
>   - https://docs.spotware.com/Managers_API/Lists
>   - https://docs.spotware.com/en/Managers_API/Events

---

## Page: Manager's API
*Source: https://docs.spotware.com/Managers_API*

# ¶ Introduction to Manager’s API


The **Manager’s API** is a powerful tool that allows for creating custom systems of communication with the cTrader backend. In essence, it enables you to perform nearly all major operations on server entities in a manner that is most convenient to you.


The **Manager’s** **API** uses Protocol Buffers (or Protobufs), a language and architecture-neutral solution originally developed by Google. Protobufs offer a lightweight and easy-to-use means for serializing structured data which makes them the ideal choice for transferring information between the cTrader backend and any custom control systems you may create.


Each Protobuf message consists of structured name-value pairs. Consider the following example.


```
message SampleSymbolUpdateReq {

        required string symbolName = 1;

    required int32 symbolID = 2;

    required string baseAssetName = 3;

    required string quoteAssetName = 4;

    required UpdateOperation operation = 5;

}

```

The structure of Protobuf message is essentially a sequence of numbered fields. Each field may belong to a variety of types including `string`, `int32`, or even custom value types.


When sent between different solutions/applications, Protobuf messages are used to create objects of certain types directly from raw bytes. As a result, you can use a wide variety of programming languages and approaches when performing server-side integration using the **Manager’s API**.


# ¶ Working with the Manager’s API


As the **Manager’s API** is a powerful tool for integration purposes, using it improperly may have a detrimental effect on your cServer instances, potentially impacting the performance or even causing an outage. We therefore advise that you proceed with caution.


## ¶ Working With Protocol Buffers


Protobufs constitute a lightweight tool for data serialization. Identifying the correct library to use for serializing and/or deserializing objects to and from Protobut messages will obviously vary according to the language you are using for integration, and in some cases several may exist. Many libraries also include some implementation of the protogen tool which allows you to automatically generate the appropriate classes and objects based on the `.proto` files supplied by our support team.

> This API uses syntax version 2 (Proto2), so please ensure that whichever library you select supports this version.

> The examples below use C# syntax and the `protobuf-net` library.


## ¶ Establishing a Connection


All connections for the **Manager’s API** are handled by our proxy cloud, and are encrypted . You can obtain specific connection details from our support team. Establishing a connection is as simple as opening a TCP connection to port 5011 of the desired proxy, and then performing any necessary validation of the SSL certificate.


```

    TcpClient client = new TcpClient();

    client.Connect(proxyHost, proxyPort);

    SslStream stream = new SslStream(client.GetStream(), false);

    stream.AuthenticateAsClient(proxyHost);


```

Once you have successfully established connection to the proxy you will immediately receive the [`HelloEvent` message](/Managers_API/Events/). To ensure that the connection stays open you shoud send a [`HeartbeatEvent`](/Managers_API/Events/) message every 25 seconds. The proxy will send its own [`HeartbeatEvent`](/Managers_API/Events/) message if no other data is being sent.


## ¶ Receiving Data


When reading messages from the stream, the first 4 bytes indiciate the length of the actual data. The message which follows is always wrapped within the `ProtoMessage` structure, which is described below.


```java
message ProtoMessage {

    /*
     * Contains the unsigned-integer representation of the payload type, which can be found from ProtoPayloadType
     * or ProtoCSPayloadType enums.
     */

    required uint32 payloadType = 1;

    /*
     * Contains the actual payload, which can be deserialized to the type identified by payloadType.
     */

    optional bytes payload = 2;

    /*
     * A user-defined string which can be specified in requests sent to the proxy, and will be included in the
     * corresponding response in order to allow matching it to the corresponding request.
     */

    optional string clientMsgId = 3;
}

```

The process for working with received data can be broken down into four steps.


- Determine the message length.

- Deserialize the received `ProtoMessage`.

- Identify the type of message contained within `ProtoMessage.payload`.

- Deserialize `int32`0 to the appropriate type.


## ¶ Determining the Message Length


To extract the length of the payload you must first reverse the 4-byte array, and then convert it to an integer value.


```c

    // where bytes is the 4-byte array

    Span<byte> lengthSpan = bytes.AsApan();

    lengthSpan.Reverse();

    int length = BitConverter.ToInt32(lengthSpan);


```

From this you can determine that the next `int32`1 bytes of the stream contain the actual message.


## ¶ Deserializing the ProtoMessage


After the message has been read from the stream, you can then proceed to deserialize this data to the `int32`2 structure.


```c

    // assuming `buffer` is the byte array read from the stream

    ProtoMessage message = Serializer.Deserialize<ProtoMessage>(new MemoryStream(buffer));


```


## ¶ Identify the Payload Type

Once the `int32`3 has been deserialized, you can then use the `int32`4 property to identify the type of `int32`5, and then proceed to deserializing of the contents.


## ¶ Deserializing the Payload


With the appropriate type identified, you can now proceed to deserialize `int32`6 to this type.


```c

    // assuming that `payloadType` represents the Type that you wish to deserialize to.
    var payload = Serializer.Deserialize(payloadType, new MemoryStream(message.Payload));


```


## ¶ Sending Data

Sending messages to the proxy follows the same basic principals as receiving, in that the payload should be wrapped within the `int32`7 structure, and a 4-byte array indicating the length prepended to the generated byte array.


```c

    ProtoHeartbeatEvent payload = new ProtoHeartbeatEvent();
    MemoryStream payloadStream = new MemoryStream();
    Serializer.Serialize(payloadStream, payload);

    ProtoMessage message = new ProtoMessage()
    {
        PayloadType = ProtoPayloadType.PROTO_HEARTBEAT_EVENT,
        Payload = payloadStream.ToArray()
    };

    MemoryStream messageStream = new MemoryStream();
    Serializer.Serialize(messageStream, message);

    byte[] bytes = messageStream.ToArray();
    // calculate the length of bytes, reverse it, and append the `bytes` array to the result
    byte[] data = BitConverter.GetBytes(bytes.Length).Reverse().Concat(bytes).ToArray();


```

The resulting `int32`8 array can then be written to the established stream.

> Specifying `int32`9 is optional, but recommended when you need to match a specific response to the request.


# ¶ The Reporting API vs the Manager’s API


Both the **Reporting API** and the **Manager’s API** are powerful tools that could be used for receiving statistics from the cTrader backend.


Compared to the **Manager’s API**, the **Reporting API** has several characteristics that limit its functionality to just reporting. The following table summarizes the main differences between the APIs.

| Characteristic | Manager’s API | Reporting API |
| --- | --- | --- |
| Authorization/authentication mechanism | Each participant has to be authorized using a special manager’s token which can only be received after gaining access to the cBroker back office. | There are no additional authorization/authentication mechanisms. The full functionality can be accessed by any manager from any business entity that has access to your server and knows the API connection details. |
| Access rights | Each participant can only perform actions that they have specifically been granted permissions to perform in the cBroker back office. | Each participant can always perform all actions that are permitted by the API. |
| Possible actions | Participants can receive statistics, manage trading conditions, oversee accounts, etc. | Participants can only receive statistics. |


As a result, integration with the **Manager’s API** is preferable in the following cases.


- You have a server with several small-scale White Labels (WLs) and you want to minimise risks by separating the access rights of their managers.

- You want to not only receive statistics but also to create a custom system for controlling accounts, symbols, assets, liquidity feeds, and other major server entities.


In any other case, integration with the **Reporting API** may be a valid alternative.


# ¶ Manager’s API Guide


This guide is not intended as a full-scale documentation for the **Manager’s API**, nor does it contain links to the Protobuf files that include the full API structure.


Instead, the guide lists the key types of messages included in the **Manager’s API** and their definitions. You can consult it to attain a general idea of what you can do when using the **Manager’s API**. To request access to the `.proto`0 files containing the fields included in each message as well as model messages (custom value types used in the API), please contact Spotware’s service assurance team.


The guide is separated into four sub-sections.


- CRUD Operations

- Events

- Lists

- Trading and Pricing

---

## Page: CRUD Operations
*Source: https://docs.spotware.com/en/Managers_API/CRUDs*

# ¶ CRUD Operations


This page lists all CRUD requests included in the current version of the **Manager's API**.


The requests are grouped by the types of server entities that they are supposed to create/update/delete.


## ¶ Assets, Symbols, and Feed Symbol Settings

| Request | Definition |
| --- | --- |
| `CrudAssetReq` | The request to create/update/delete an asset. |
| `CrudSymbolReq` | The request to update/delete a symbol. |
| `CrudLiquidityFeedSymbolReq` | The request to create/update/delete a feed symbol setting. |


## ¶ Accounts, and Groups

| Request | Definition |
| --- | --- |
| `CrudGroupReq` | The request to create/update/delete an group. |
| `CrudTraderReq` | The request to create/update/delete an account. |


## ¶ Group Profiles and Related Items

| Request | Definition |
| --- | --- |
| `CrudCommissionProfileReq` | The request to create/update/delete a commission profile. |
| `CrudExecutionProfileReq` | The request to create/update/delete an execution profile. |
| `CrudGSLScheduleReq` | The request to create/update/delete Guaranteed Stop Loss (GSL) schedule items. |
| `CrudDynamicLeverageReq` | The request to create/update/delete dynamic leverage settings. |
| `CrudProtectionProfileReq` | The request to create/update/delete a protection profile. |
| `CrudSymbolReq`0 | The request to create/update/delete a swap free profile. |
| `CrudSymbolReq`1 | The request to create/update/delete a trade notification profile. |
| `CrudSymbolReq`2 | The request to create/update/delete a volume profile. |


## ¶ Swaps and Dividends Profiles and Price Streams

| Request | Definition |
| --- | --- |
| `CrudSymbolReq`3 | The request to create/update/delete a swaps and dividends profile. |


## ¶ Session Profiles, Holiday Profiles, and Holidays

| Request | Definition |
| --- | --- |
| `CrudSymbolReq`4 | The request to create/update/delete a holiday profile. |
| `CrudSymbolReq`5 | The request to create/update/delete a holiday. |


## ¶ Managers

| Request | Definition |
| --- | --- |
| `CrudSymbolReq`6 | The request to create/update/delete a manager. |

---

## Page: Trading and Pricing
*Source: https://docs.spotware.com/Managers_API/Trading_and_Pricing*

# ¶ Trading and Pricing


This page lists all trading-oriented requests you can perform when using the **Manager’s API**. It also contains the requests for subscibing/unsubscribing to and from spot events.


Trading-oriented requests are typically used in the following cases.


- Trading on behalf of your retail clients. E.g., this can be done in emergency situations where a trader wants to open/close a position without having to access the trading terminal.

- Supporting the creation of a custom copy trading solution integrated with your systems.


The requests are grouped according to the server entities that they operate on.


## ¶ Orders

| Request | Definition |
| --- | --- |
| `ManagerNewOrderReq` | The request to create and place a new order. |
| `ManagerAmendOrderReq` | The request to amend an existing order. |
| `ManagerCancelOrderReq` | The request to cancel an order. |


## ¶ Positions

| Request | Definition |
| --- | --- |
| `ManagerAmendPositionReq` | The request to amend the protection mechanisms of an existing position. |
| `ManagerClosePositionReq` | The request to close an existing position. |


## ¶ Spot Events

| Request | Definition |
| --- | --- |
| `SubscribeSpotQuotesReq` | The request to subscribe to spot events for a particular symbol. |
| `UnsubscribeSpotQuotesReq` | The request to unsubscribe from spot events for a particular symbol. |

---

## Page: Lists
*Source: https://docs.spotware.com/Managers_API/Lists*

# ¶ Lists


This page all lists included in the current version of the **Manager’s API**.


The requests are grouped by the types of server entities that they are supposed to attain information for.


## ¶ Assets, Symbols, and Feed Symbol Settings

| List | Definition |
| --- | --- |
| `AssetListReq` | The request to get a list of assets. |
| `AssetClassListReq` | The request to get a list of asset classes. |
| `ManagerSymbolListReq` | The request to get a list of symbols. |
| `SymbolCategoryListReq` | The request to get a list of symbol categories. |
| `LiquidityFeedListReq` | The request to get a list of liquidity feeds. |
| `LiquidityFeedSymbolListReq` | The request to get a list of feed symbol settings. |
| `ExposureSymbolListReq` | The request to get exposure per symbol. |


## ¶ Users, Accounts, and Groups

| List | Definition |
| --- | --- |
| `TraderListReq` | The request to get a list of accounts filtered by account registration timestamp; this list is given in the descending order (the account that was created last is mentioned first). |
| `ManagerLightTraderListReq` | The request to get a list of accounts with a limited number of fields. |
| `BalanceHistoryListReq` | The request to get a history of balance changes (deposits and withdrawals only) filtered by deposit/withdrawal timestamp. |
| `AssetClassListReq`0 | The request to get a history of bonus changes (deposits and withdrawals only) filtered by deposit/withdrawal timestamp. |
| `AssetClassListReq`1 | The request to get a list of groups with a limited number of fields. |


## ¶ Orders, Deals, and Positions

| List | Definition |
| --- | --- |
| `AssetClassListReq`2 | The request to get a list of orders related to a certain position. |
| `AssetClassListReq`3 | The request to get a list of orders filtered by the order creation timestamp. |
| `AssetClassListReq`4 | The request to get a list of pending orders filtered by the order creation timestamp. |
| `AssetClassListReq`5 | The request to get a list of deals related to a certain position filtered by deal creation timestamp. |
| `AssetClassListReq`6 | The request to get a list of deals filtered by deal creation timestamp. |
| `AssetClassListReq`7 | The request to get a list of open positions filtered by the position open timestamp. |
| `AssetClassListReq`8 | The request to get closed positions. |


## ¶ Group Profiles and Related Items

| List | Definition |
| --- | --- |
| `AssetClassListReq`9 | The request to get a list of commission profiles. |
| `ManagerSymbolListReq`0 | The request to get a list of all execution profiles. |
| `ManagerSymbolListReq`1 | The request to get a list of GSL schedule items. |
| `ManagerSymbolListReq`2 | The request to get a list of dynamic leverage entities. |
| `ManagerSymbolListReq`3 | The request to get a list of protection profiles. |
| `ManagerSymbolListReq`4 | The request to get a list of swap free profiles. |
| `ManagerSymbolListReq`5 | The request to get a list of trade notification profiles. |
| `ManagerSymbolListReq`6 | The request to get a list of volume profiles. |


## ¶ Swaps and Dividends Profiles and Price Streams

| List | Definition |
| --- | --- |
| `ManagerSymbolListReq`7 | The request to get a list of price streams. |
| `ManagerSymbolListReq`8 | The request to get a list of swap and dividends profiles with a limited number of fields. |


## ¶ Session Profiles, Holiday Profiles, and Holidays

| List | Definition |
| --- | --- |
| `ManagerSymbolListReq`9 | The request to get a list of session profiles. |
| `SymbolCategoryListReq`0 | The request to get a list of holidays. |
| `SymbolCategoryListReq`1 | The request to get a list of holiday profiles. |


## ¶ Managers

| List | Definition |
| --- | --- |
| `SymbolCategoryListReq`2 | The request to get a list of managers. |


## ¶ Miscellaneous

| List | Definition |
| --- | --- |
| `SymbolCategoryListReq`3 | The request to get a list of countries. |
| `SymbolCategoryListReq`4 | The request to get historic trend bars. |

---

## Page: Events
*Source: https://docs.spotware.com/en/Managers_API/Events*

# ¶ Events


This page lists all events included in the current version of the **Manager’s API**.


The events are grouped by the types of server entities that they are supposed to be triggered for.


## ¶ Assets, Symbols, and Feed Symbol Settings

| Event | Definition |
| --- | --- |
| `AssetChangedEvent` | The event sent when an asset is created/updated/deleted. |
| `AssetClassChangedEvent` | The event sent when an asset class is created/updated. |
| `AssetClassDeletedEvent` | The event sent when an asset class is deleted. |
| `LiquidityFeedSymbolChangedEvent` | The event sent when a feed symbol setting is created/updated/deleted. |
| `ManagerSymbolChangedEvent` | The event sent when a symbol is created/updated/deleted. |
| `SymbolArchivedEvent` | The event sent when a symbol is archived. |
| `SymbolRestoredEvent` | The event sent when an archived symbol is restored. |
| `SymbolCategoryChangedEvent` | The event sent when a symbol category is created/updated. |
| `SymbolCategoryDeletedEvent` | The event sent when a symbol category is deleted. |


## ¶ Users, Accounts, and Groups

| Event | Definition |
| --- | --- |
| `TraderChangedEvent` | The event sent when an account is created/updated/deleted. |
| `AssetClassChangedEvent`0 | The event sent when an account log in occurs. |
| `AssetClassChangedEvent`1 | The event sent when an account logout occurs. |
| `AssetClassChangedEvent`2 | The event sent when a group is created/updated/deleted. |


## ¶ Orders, Deals, and Positions

| Event | Definition |
| --- | --- |
| `AssetClassChangedEvent`3 | The event sent following cServer successfully accepting or executing an order.The event is also sent when a deposit/withdrawal is performed. |
| `AssetClassChangedEvent`4 | The event that is sent when errors occur during order-related requests. |
| `AssetClassChangedEvent`5 | The event sent when the amount of margin allocated to a specific position is changed. |


## ¶ Group Profiles and Related Items

| Event | Definition |
| --- | --- |
| `AssetClassChangedEvent`6 | The event sent when a commission profile is created/updated/deleted. |
| `AssetClassChangedEvent`7 | The event sent when dynamic leverage settings are created/updated/deleted. |
| `AssetClassChangedEvent`8 | The event sent when an execution profile is created/updated/deleted. |
| `AssetClassChangedEvent`9 | The event sent when a GSL schedule profile item is created/updated/deleted. |
| `AssetClassDeletedEvent`0 | The event sent when a protection profile is created/updated/deleted. |
| `AssetClassDeletedEvent`1 | The event sent when a swap free profile is created/updated/deleted. |
| `AssetClassDeletedEvent`2 | The event sent when a trade notification profile is created/updated/deleted. |
| `AssetClassDeletedEvent`3 | The event sent when a volume profile is created/updated/deleted. |


## ¶ Swaps and Dividends Profiles and Price Streams

| Event | Definition |
| --- | --- |
| `AssetClassDeletedEvent`4 | The event sent when a swap and dividends profile is created/updated/deleted. |
| `AssetClassDeletedEvent`5 | The event sent when a price stream is created/updated/deleted. |


## ¶ Session Profiles, Holiday Profiles, and Holidays

| Event | Definition |
| --- | --- |
| `AssetClassDeletedEvent`6 | The event sent when a session profile is created/updated/deleted. |
| `AssetClassDeletedEvent`7 | The event sent when a holiday is created/updated/deleted. |
| `AssetClassDeletedEvent`8 | The event sent when a holiday profile is created/updated/deleted. |


## ¶ Managers

| Event | Definition |
| --- | --- |
| `AssetClassDeletedEvent`9 | The event sent when a manager is created/updated/deleted. |
| `LiquidityFeedSymbolChangedEvent`0 | The event sent when a manager loses access to an account due to a change in the manager’s access rights. |


## ¶ Miscellaneous

| Event | Definition |
| --- | --- |
| `LiquidityFeedSymbolChangedEvent`1 | The event sent when connection is first established. |
| `LiquidityFeedSymbolChangedEvent`2 | The event used for keeping the connection alive. |
| `LiquidityFeedSymbolChangedEvent`3 | The event sent when server settings are updated. |
| `LiquidityFeedSymbolChangedEvent`4 | The event sent when a new spot event is generated on the side of the server.  Spot events (received after subscribing to them via a separate request) always contain the latest prices even if markets are closed. |

---
