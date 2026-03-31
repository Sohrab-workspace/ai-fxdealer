# Reporting API — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/Reporting_API
>   - https://docs.spotware.com/Reporting_API/Establishing_a_Connection
>   - https://docs.spotware.com/en/Reporting_API/Receiving_Events
>   - https://docs.spotware.com/en/Reporting_API/Making_Snapshots
>   - https://docs.spotware.com/en/Reporting_API/Historical_Tick_Data

---

## Page: Reporting API
*Source: https://docs.spotware.com/Reporting_API*

# ¶ Introduction to Reporting API


The **Reporting API** is a versatile and easy-to-use solution that allows for integrating your reporting systems with the cTrader backend. You can also use it as a basis for developing a custom reporting suite. The Reporting API provides you with data about key server entities (e.g., traders, orders, and positions) that you can process using any suitable logics.

> If you are a non-broker entity, you cannot work with white labels through the Reporting API. Please use other APIs or contact us at partners@spotware.com for clarifications.


# ¶ Google Protobufs and RabbitMQ


Similarly to the [**Manager’s API**](/Managers_API), the Reporting API uses Google Protocol Buffers (Protobufs) as a means of transferring information between services.

> The Reporting API uses syntax version 2 (Proto2). When selecting a language/library for integration, make sure that it supports this version.


A detailed guide to working with with Protobufs can be found in our introduction to the [**Manager’s API**](/Managers_API). Additional information can also be found on the following resources.


- Official Protobuf documentation

- Official GitHub repo


For sending real-time data, the **Reporting API** uses [**RabbitMQ**](https://www.rabbitmq.com/), a well-known message broker.


# ¶ Key Components and Use Cases


Integration with the **Reporting API** is recommended in case you need to achieve any of the following goals.


- Creating a custom in-house reporting system displaying statistics originating from cTrader accounts.

- Making sure an existing reporting solution can receive and process information from the cTrader backend.


To attain these goals, the **Reporting API** consists of two key components.


- Snapshots. These are received by performing web requests to certain endpoints.

- Events. As stated previously, events are received after establishing a connection with RabbitMQ.


A snapshot provides information about the state of certain server entities during the specified period. Depending on the request you make, a snapshot may either contain a list of entities and their attributes, or data about just one entity.


In contrast, events act as notifications about the creation/modification/deletion of server entities. Each event is preceded by a sequence number allowing you to detect cases where reconciliation with the cTrader backend may be required. Finally, spot events represent changes in bid/ask prices.

> Snapshots are time and resource-consuming to take. In most cases, it is necessary to only take snapshots at the initial stages of integration so that you can receive information about the entire structure of the database. Snapshots should also be taken for reconciliation in case you detect that you have not received or processed any real-time events. Ideally, snapshots should be taken during weekends.

> When generating sequence numbers for real-time events, each server restart produces a new sequence starting from `1`. As a result, please follow the below rules when deciding whether reconciliation is needed.
> 1. If you receive events whose sequence numbers are incremented by `1` with each consecutive event (e.g., `23456`, `23457`, `23458`), no reconciliation is needed.
> 2. If you receive events whose sequence numbers are incremented by `1` and then receive an event whose sequence number is `1`, a server restart has occurred and reconciliation is needed.
> 3. If you receive events whose sequence numbers are incremented by a number larger than `1` (e.g., `23456`, `23458`, `1`0), some events have been missed and reconciliation is needed.


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


In any other case, integration with the **Reporting API** is a valid alternative.


# ¶ Structure of the Documentation


Apart from this introduction, the documentation is divided into the following sections.


- Establishing a connection

- Receiving events

- Making snapshots

- Requesting historical tick data


# ¶ Protobuf Files


You can access the latest verion of the **Reporting API** Protobuf files [**here**](/reporting-api/reportingmessages.proto).

---

## Page: Establishing a Connection
*Source: https://docs.spotware.com/Reporting_API/Establishing_a_Connection*

# ¶ Establishing a Connection


For receiving events, the **Reporting API** requires a connection to [**RabbitMQ**](https://www.rabbitmq.com/), a well-known message broker suite.

> Connections to our RabbitMQ node are only possible from whitelisted IPs. To whitelist your IPs, please provide them to Spotware’s service assurance team.


To connect to **RabbitMQ**, all you have to do is perform these actions.


- Run Stunnel on your machine and route your connection through it.

- Connect to the correct host and create a channel.


> All C# examples below use the `RabbitMQ.Client` Nuget package, which you can install using any suitable Nuget package management service.

> All Java examples below use the RabbitMQ Java client that you can install using any suitable dependency management system or build tool such as Maven or Gradle.


## ¶ Routing Your Connection Via Stunnel


[**Stunnel**](https://www.stunnel.org/) is an application that you can use to provide TSL/SSL encryption functionality to a connection.


To connect to the **RabbitMQ** node, **Stunnel** should be successfully deployed and accessible from your client. **Stunnel** should also be configured properly; this configuration is provided by Spotware’s service assurance team.


## ¶ Connecting to the Host


After routing your connection via **Stunnel** and whitelisting your IPs, you will have to connect to the correct host via your application or service. This can be done as follows.

> The values of `hostName`, `password`, `portNumber`, and `userName` are provided by Spotware’s service assurance team upon request.

> Connections are meant to handle many operations and, therefore, should stay open for long periods of time. It would be inefficient to establish a new connection for every new action you need to perform.

- C#
- Java

---

## Page: Receiving Events
*Source: https://docs.spotware.com/en/Reporting_API/Receiving_Events*

# ¶ Receiving Events


This guide covers how you can correctly receive and interpret events as part of integrating with the **Reporting API**.

> The C# examples in this tutorial use the `protobuf-net` Nuget package.


## ¶ Event Queues


**RabbitMQ** supplies events via two queues.


- `rabbit.spot_queue` is used for receiving spot events (and only spot events).

- `rabbit.queue` is used for receiving all other types of events.


> Note that `rabbit.spot_queue` is not available by default. You can enable it by contacting Spotware’s service assurance team.


## ¶ Structure of Events


Each event contains the following information.

| Name | Definition |
| --- | --- |
| `Payload` | The contents of the Protobuf message as a byte array |
| `Properties` | The properties of the object representing the delivered message. `Properties` contain the following information.  `content_type`. The type of content that the message represents. The value of this property always equals `application/x-protobuf`.`content_length`. The size of the message in bytes.`rabbit.spot_queue`0. The property containing message headers. The following headers are supported.`rabbit.spot_queue`1. The message type from among those supported by the Reporting API (e.g., `rabbit.spot_queue`2, `rabbit.spot_queue`3, etc.).`rabbit.spot_queue`4. The sequence number assigned to the event. You can use it to determine whether reconciliation is needed. |


In brief, accessing the contents of an event requires the following.


- Determining the `rabbit.spot_queue`5 of the newly received message via the `rabbit.spot_queue`6 property.

- Converting the message payload into a suitable class representing the `rabbit.spot_queue`7 received during Step 1.


If you already know the `rabbit.spot_queue`8 of an event, you can access its contents as follows (the examples below use `rabbit.spot_queue`9).

- C#
- Java

---

## Page: Making Snapshots
*Source: https://docs.spotware.com/en/Reporting_API/Making_Snapshots*

# ¶ Making Snapshots


In contrast to events, making snapshots is done by performing HTTP requests to various endpoints. You can send these requests using any HTTP client of your choice.

> All endpoints listed below are relative to `https://HOST:PORT/repo`. The value of `HOST:PORT` is provided by Spotware's service assurance team upon request.

> Note that all requests listed below return arrays of bytes that you can serialise into the required entities. For example, in Java this can be done by calling the `parseFrom()` method from a suitable static class.

> It is only possible to send a maximum of two concurrent requests per server when making shapshots. When requesting a snapshot, make sure to set a timeout of no less than 20 seconds.


It is possible to make snapshots for the following types of entities.

- Assets and Symbols
- Traders, Balance, and Bonus
- Orders, Deals, and Positions
- Authentications and Actions
- Reports
- Prices, Price Streams, and Swaps
- Profiles and Holidays
- Countries

---

## Page: Historical Tick Data
*Source: https://docs.spotware.com/en/Reporting_API/Historical_Tick_Data*

# ¶ Historical Tick Data


Similarly to making snapshots, you can request historical tick data by performing an HTTP request.

> All endpoints listed below are relative to `https://HOST:PORT/repo`. The value of `HOST:PORT` is provided by Spotware’s service assurance team upon request.

> Note that all requests listed below return arrays of bytes that you can serialise into the required entities. For example, in Java this can be done by calling the `parseFrom()` method from a suitable static class.


## ¶ Request Historical Tick Data

| HTTP Method | URL |
| --- | --- |
| `GET` | `/tickData` |


Gets historical tick data for a symbol for a certain time period. The maximum period for which it is possible to request tick data via one request is 24 hours.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `symbolId` | query | Yes | integer | The ID of the symbol for which you would like to request historical tick data. |
| `type` | query | Yes | string | The type of historical tick data you would like to request. This parameter can only take two possible values.`BID`. The tick data for bid prices is requested.`ASK`. The tick data for ask prices is requested. |
| `fromTimestamp` | query | Yes | integer | The Unix timestamp of the start of the period for which you would like to request tick data (including milliseconds). |
| `HOST:PORT`0 | query | Yes | integer | The Unix timestamp of the end of the period for which you would like to request tick data (including milliseconds). |
| `HOST:PORT`1 | query | No | integer | The total number of ticks to return; this parameter can only take values ranging from `HOST:PORT`2 to `HOST:PORT`3. Defaults to `HOST:PORT`4. |


**Request Body**


No request body.


**Output**


An array of bytes representing the requested entity(-ies).


**Request Examples**


Requesting the first 100 `HOST:PORT`5 ticks for symbol whose ID equals `HOST:PORT`6 starting from 22/06/2019, 11:12:31.681 until 22/06/2019, 12:32:30.231.


```curl
curl -X GET "https://HOST:PORT/repo/tickData?symbolId=1&type=ASK&fromTimestamp=1563793951681&toTimestamp=1563798750231&size=100"

```

**Response Example**


As the response contains only an array of bytes, no specific example can be provided.

---
