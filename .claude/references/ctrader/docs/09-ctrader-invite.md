# cTrader Invite — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/en/cTrader_Invite
>   - https://docs.spotware.com/en/cTrader_Invite/
>   - https://docs.spotware.com/cTrader_Invite/Integration
>   - https://docs.spotware.com/en/cTrader_Invite/Integration
>   - https://docs.spotware.com/en/cTrader_Invite/Glossary
>   - https://docs.spotware.com/en/cTrader_Invite/API_Calls

---

## Page: Introduction
*Source: https://docs.spotware.com/en/cTrader_Invite*

# ¶ Introduction


## ¶ Purpose of the Documentation


This documentation explains how to integrate cTrader Invite with a broker’s partner programme, describing the technical details and relevant API calls.


## ¶ Introduction


IBs are the primary source of trader traffic in the forex industry. cTrader Invite already serves as a dedicated and powerful toolkit for partners within the trading application. However, without a seamless connection between cTrader Invite and the broker’s partner programme, all parties may face significant challenges.


  - IBs have to take extra steps to register in the broker’s partner programme, obtain a BRL and set it correctly in the trading application.

  - Traditional BRLs seem to be an outdated mechanism, offering little value to traders beyond attribution.

  - Redirecting traders from the trading platform to the broker’s website for registration and attribution can be confusing for traders and may lead to drop-offs.

  - IBs often face delayed referral statistics and struggle to monitor their attribution progress in one place.

  - The broker CRM may miss information about clients coming from the trading platform.


As a consequence, IB efficiency declines, and brokers lose clients at every stage of the onboarding funnel.


## ¶ Spotware’s Solution


When cTrader Invite is integrated with a broker’s partner programme, attribution data is transmitted via webhooks from the cTrader application directly to the broker CRM to register and attribute users. All redundant steps for IBs, such as obtaining a BRL and setting it in the application, are eliminated. Partners only need to focus on sharing engaging invite links that lead to trading products; the rest is done automatically for them.

*
  Figure 1: Integrated Invite in cTrader Mobile*


As a result, traders remain within the trading application without confusing redirects. Partners can monitor their real-time referral statistics in cTrader, fully synchronised with the broker CRM. The solution notifies the broker CRM of all newly registered users whose journey began with cTrader, even if no further attribution occurred.


## ¶ Benefits for Brokers


  - IB access simplified. The integration lowers the entry barrier to the broker’s partner programme by making the IB registration process effortless, without the need for a BRL.

  - Increased trader engagement. Unlike BRLs, product-related invite links offer powerful calls to action, stimulate trading activity and boost trader retention.

  - Improved CRM accuracy. Client data is automatically captured and transmitted from the trading platform to the broker CRM, eliminating the risk of missing records.

  - Higher conversion rates. By increasing the efficiency of the partner programme, brokers can expect higher conversion rates from leads to active traders.


## ¶ Structure of the Documentation


The documentation for cTrader Invite consists of the following sections:


  - Glossary. The glossary explains the key terms used in the documentation.

  - Integration. This section outlines the rules, requirements and flow steps of the integration.

  - API Calls. This section outlines the API calls for the integration.

---

## Page: Integration
*Source: https://docs.spotware.com/cTrader_Invite/Integration*

# ¶ Integration


## ¶ Invite Flows


When not integrated with the broker’s partner programme, cTrader Invite involves extra steps for both IBs and traders, and synchronisation of referral statistics becomes challenging.


*Figure 1: cTrader Invite before integration*


The integration allows brokers to streamline IB and trader flows while automating the data exchange between the cTrader application and the broker CRM.


*Figure 2: cTrader Invite after integration*


Specifically, the integrated Invite involves the following steps:


1. An IB shares an invite link from their broker-branded cTrader application with a trader.

> Invite links stimulate trader engagement by directing traders to specific trading products, such as algorithms, copy strategies, signal links and more.


2. Upon clicking the partner’s invite link, the trader opens cTrader, registers if new, and attribution occurs within the application.


3. The broker CRM receives a webhook with attribution information containing the user IDs of the invited trader and partner, broker name and partner ID.


4. The broker CRM registers the new user and attributes them to the corresponding IB in their system. If the IB is new, they undergo registration in the CRM under the broker’s conditions.


- If the IB is receiving attribution for the first time, the broker CRM generates a new partner ID, which is sent to the cTrader backend and automatically set in cTrader Invite.

- If the IB received attribution in the past (meaning they already have a partner ID), the broker CRM should recognise them, as the webhook sent by the cTrader backend contains known identifiers.


This process keeps the broker CRM in synchronisation with cTrader, allowing real-time referral statistics to be displayed within the application


## ¶ Integration Process


1. To receive webhooks, a broker must notify the Spotware Support Team ([**support@spotware.com**](mailto:support@spotware.com)) of the unique URL in their backend that is prepared to receive attribution information.


2. Support receiving callbacks with attribution information containing `invitedUserId`, `partnerUserId`, `brokerName` and `brokerPartnerId` from the cTrader backend.


- `invitedUserId` - unique user ID of the invited trader.

- `partnerUserId` - unique user ID of the partner.

- `brokerName` - name of the broker or white label the user registers with.

- `brokerPartnerId` - unique ID of the IB in the broker CRM or partner programme.


3. Support sending responses containing `brokerPartnerId` and `brokerResult` to the cTrader backend.


- `partnerUserId`0 - status of the attribution process. See the response body in this API call for more information on this key.


### ¶ Optional Steps


4. Support sending requests and then receiving history of attributions from the cTrader backend via this [**API call**](/cTrader_Invite/API_Calls#get-list-of-invited-users-attributions).


5. Support receiving callback notifications from the cTrader backend about the registration of a new user via this [**API call**](/cTrader_Invite/API_Calls#get-callback-with-notification-about-a-new-user) and notify Spotware about the URL in the broker’s backend prepared for this purpose. This enables brokers to learn about new users who register directly in a cTrader application, as the cTrader backend does not automatically return such users’ `partnerUserId`1 to the broker CRM.


6. Support sending requests via this [**API call**](/cTrader_Invite/API_Calls#get-list-of-registered-users) and receiving responses containing all registered users or users registered within a specified timeframe.


**Note**: The Invite functionality described in this document can be used independently from the WebServices [**API call 8.6**](/WebServices_API/Use_Cases#h-86-attributing-a-trader-to-a-partner) and the Broker SSO [**API call 3.6**](/Broker_SSO_OAuth/API_Calling_Backend#h-36-set-a-new-partner-identifier).

---

## Page: Glossary
*Source: https://docs.spotware.com/en/cTrader_Invite/Glossary*

# ¶ Glossary


**cTrader Invite**. An all-in-one toolkit designed to help partners attract traders with appealing cTrader products and seamlessly convert them into referrals. Once integrated, cTrader Invite functions as an extension of a broker’s partner programme, requiring no setup efforts from partners while providing them with real-time attribution statistics directly within the cTrader application.


**Partner**. An individual or entity that collaborates with a broker on the cTrader platform to promote their services and attract new trading clients. In broker-branded cTrader apps, partners initiate inviting traders, attribute them and may offer trading support upon request.


**Introducing broker (IB)**. An individual or entity that refers clients to a broker in exchange for a commission. Registered in the broker’s partner programme, IBs act as intermediaries, focusing on marketing, education, support and other trader engagement services.


**Invited trader**. A trader attributed to a partner within cTrader. Invited traders stay with their partner for a guaranteed period before they can be reattributed to another partner.


**Referral**. A trader who registers with a broker through an IB in the partner programme. IB commissions are typically determined by the broker’s conditions, the trading activity of referrals and other criteria.


**Partner ID**. A unique identifier assigned to a partner by the broker’s backend upon registration in the partner programme. It is automatically filled in cTrader Invite after the first attribution.


**Broker referral link (BRL)**. A unique referral link issued by the broker for an IB, which redirects new clients to the broker’s website for registration and participation in the partner programme.


**Invite link**. Any cTrader link with a special (u) parameter carrying the partner’s username. Once traders click an invite link, they are attributed to the corresponding partner within cTrader and further in the broker’s partner programme on condition they are synchronised with each other.

---

## Page: API Calls
*Source: https://docs.spotware.com/en/cTrader_Invite/API_Calls*

# ¶ API Calls


## ¶ Get Callback with Notification About Attribution


The cTrader backend sends this request to the broker CRM, which then provides the response.

| Method | URL |
| --- | --- |
| `POST` | provided by the broker |


**Headers**

| Header | Description | Required? |
| --- | --- | --- |
| Authorisation header | Authorisation header containing API token provided by the broker. E.g. `Basic ab45da2g34hdb6` | Yes |


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `invitedUserId` | Yes | integer | Unique user ID of the invited trader. |
| `partnerUserId` | Yes | integer | Unique user ID of the partner. |
| `brokerPartnerId` | No | string | Unique ID of the IB in the broker CRM or partner programme. |
| `brokerName` | Yes | string | Unique name denoting a specific broker or white label with whom the user registered. |


**Output**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `brokerPartnerId` | No | string | Unique ID of the IB in the broker CRM or partner programme. |
| `brokerResult` | No | enum | Status of the attribution process. Possible values and their meanings: - `ATTRIBUTED_NEW` The broker successfully attributed a new user to a partner receiving their first attribution with them. A new brokerPartnerId has been generated.  - `ATTRIBUTED` The broker successfully attributed a new user to a partner known to them. An existing brokerPartnerId has been returned. - `Basic ab45da2g34hdb6`0 The attribution process has started but is not yet finished. - `Basic ab45da2g34hdb6`1 The broker successfully reattributed a user already attributed to one partner to a different partner. |


**Request Example**


```curl
curl -X POST 'attributionWebhookUrl'  -H 'Authorization: Basic ab45da2g34hdb6'  -H 'Content-Type: application/json'  -d '{"invitedUserId ": 4216, "partnerUserId ": 28042, "brokerPartnerId ": "I2333PIOIII", "brokerName ": "BESTBROKER"}'

```

**Expected Response Status Code**


`Basic ab45da2g34hdb6`2


**Response Example**


```json
{
    "brokerPartnerId ": "I2333PIOIII",
    "brokerResult": "ATTRIBUTED_NEW"
}

```


## ¶ Get List of Invited Users (Attributions)

The broker CRM sends this request to the cTrader backend, which then provides the response.

| Method | URL |
| --- | --- |
| `Basic ab45da2g34hdb6`3 | `Basic ab45da2g34hdb6`4 |


Generates the one-time code required for the SSO.


**Headers**

| Header | Description | Required? |
| --- | --- | --- |
| Authorisation Bearer | Authorisation header containing the authentication token of the manager. E.g. `Basic ab45da2g34hdb6`5 | Yes |


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `Basic ab45da2g34hdb6`6 | path | No | integer | Unix epoch timestamp (inclusive) in UTC milliseconds for the start of the search interval. |
| `Basic ab45da2g34hdb6`7 | path | No | integer | Number of records to return. `Basic ab45da2g34hdb6`8 is the default value. |
| `Basic ab45da2g34hdb6`9 | path | No | integer | Number of records to skip. `invitedUserId`0 is the default value. |


**Request Body**


No request body.


**Output**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `invitedUserId`1 | Yes | array | List containing invited users and their details as JSON objects. |
| `invitedUserId`2 | Yes | integer | Unique user ID of the invited trader. |
| `invitedUserId`3 | Yes | integer | Unique user ID of the partner. |
| `invitedUserId`4 | No | string | Unique ID of the IB in the broker CRM or partner programme. Filled if it was previously received from the broker. |
| `invitedUserId`5 | No | string | Unique name denoting a specific broker or white label for the invitation. |
| `invitedUserId`6 | Yes | integer | Unix epoch timestamp in UTC milliseconds of the attribution event. |


**Request Example**


```curl
curl -X GET 'https://HOST:PORT/v1/social/invitedUsers?createdFrom =1735560962458&limit=100&skip=0' -H 'Authorization: Bearer 2f68dbbf-519d-4f01-9636-e2421b68f379'

```

**Expected Response Status Code**


`invitedUserId`7


**Response Example**


```json
{
    "invitedUsers": [
        {
            "invitedUserId ": 53324216,
            "partnerUserId ": 27951042,
            "brokerPartnerId ": "I2333PIOIII",
            "brokerName ": "BESTBROKER",
            "createTimestamp": 1735560962458
        },
      	{
            "invitedUserId ": 42213105,
            "partnerUserId ": 38062153,
            "brokerPartnerId ": "J122QJ1JJJ",
            "brokerName ": "TOPBROKER",
            "createTimestamp": 1735560963562
        }
    ]
}

```


## ¶ Get Callback with Notification about a New User

The cTrader backend sends this request to the broker CRM.

| Method | URL |
| --- | --- |
| `invitedUserId`8 | provided by the broker |


**Headers**

| Header | Description | Required? |
| --- | --- | --- |
| Authorisation header | Authorisation header containing API token provided by the broker. | Yes |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `invitedUserId`9 | Yes | integer | Unique user ID of the registered trader in cTrader. |
| `partnerUserId`0 | Yes | string | Unique name denoting a specific broker or white label with whom the user registered. |
| `partnerUserId`1 | Yes | string | Email address of the registered user. |
| `partnerUserId`2 | Yes | integer | Unique user ID of the partner. |


**Request Example**


```curl
curl -X POST 'userRegistrationWebhookBrokerUrl' -H 'Authorization: Basic ab45da2g34hdb6' -H 'Content-Type: application/json' -d '{"userId": 123, "brokerName": "bestbroker", "email": "test@test.com", "partnerUserId": 345}'

```


## ¶ Get List of Registered Users

The broker CRM sends this request to the cTrader backend, which then provides the response.

| Method | URL |
| --- | --- |
| `partnerUserId`3 | `partnerUserId`4 |


**Headers**

| Header | Description | Required? | Notes |
| --- | --- | --- | --- |
| Authorisation bearer | Authorisation header containing the authentication token of the manager. E.g. `partnerUserId`5 | Yes | The manager whose token is used to send the request must have permission to authenticate users. |


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `partnerUserId`6 | path | No | integer | Unix epoch timestamp (inclusive) in UTC milliseconds for the start of the search interval. |
| `partnerUserId`7 | path | No | integer | Number of records to return. `partnerUserId`8 is the default value. |
| `partnerUserId`9 | path | No | integer | Number of records to skip. `brokerPartnerId`0 is the default value. |


**Request Body**


No request body.


**Output**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `brokerPartnerId`1 | Yes | array | List containing registered users and their details as JSON objects. |
| `brokerPartnerId`2 | Yes | integer | Unique user ID of the registered trader in cTrader. |
| `brokerPartnerId`3 | Yes | string | Email of the registered user in cTrader. |
| `brokerPartnerId`4 | Yes | string | Unique name denoting a specific broker or white label with whom the user registered. |
| `brokerPartnerId`5 | Yes | integer | Unix epoch timestamp in UTC milliseconds for the user registration event. |


**Request Example**


```curl
curl -X GET 'https://HOST:PORT/v1/users?createdFrom=1735560962458&limit=1000&skip=0'  -H 'Authorization: Bearer 2f68dbbf-519d-4f01-9636-e2421b68f379'

```

**Expected Response Status Code**


`brokerPartnerId`6


**Response Example**


```json
{
    "users": [
        {
            "userId": 27424389,
            "email": "test@test.com",
            "brokerName": "BESTBROKER",
            "utcCreateTimestamp": 1735560962458
        },
      	{
            "userId": 16875243,
            "email": "user@email.com",
            "brokerName": "TOPBROKER",
            "utcCreateTimestamp": 1735560981692
        }
    ]
}

```

---
