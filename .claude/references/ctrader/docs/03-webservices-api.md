# WebServices API — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/WebServices_API
>   - https://docs.spotware.com/en/WebServices_API
>   - https://docs.spotware.com/WebServices_API/Operations_With_Accounts
>   - https://docs.spotware.com/en/WebServices_API/Operations_With_Accounts
>   - https://docs.spotware.com/WebServices_API/Operations_With_cTID
>   - https://docs.spotware.com/WebServices_API/Domain_Model_and_Logic
>   - https://docs.spotware.com/WebServices_API/Best_Practices
>   - https://docs.spotware.com/WebServices_API/JSON_Schemas
>   - https://docs.spotware.com/en/WebServices_API/Error_Codes
>   - https://docs.spotware.com/WebServices_API/Country_List
>   - https://docs.spotware.com/en/WebServices_API/General_Provisions
>   - https://docs.spotware.com/en/WebServices_API/Operations_With_Assets_Symbols
>   - https://docs.spotware.com/en/WebServices_API/Use_Cases

---

## Page: WebServices API
*Source: https://docs.spotware.com/WebServices_API*

# ¶ 1. Introduction


## ¶ 1.1. WebServices API Definition


The **WebServices API** is a powerful API that allows for integrating the cTrader backend with one’s registration forms, traders room, and CRM systems.


This REST API includes all essential operations including (but not limited to) account creation, cTID creation, group assignment, performing deposits and withdrawals, requesting balance, and linking accounts to cTID.


This documentation includes detailed descriptions of all endpoints in the **WebServics API**; it also contains the JSON schemas for all major server entities.


## ¶ 1.2. Structure of the Documentation


The WebServices API documentation includes the following sections.


- Section 2 provides a general overview of the cTrader domain model and logic.

- Section 3 outlines the general provisions for working with the API.

- Section 4 details the API calls made when working with account entities (‘traders’).

- Section 5 defines the API calls made when working with cTID entities (‘users’).

- Section 6 outlines the API calls made when working with assets and symbols.

- Section 7 contains the JSON schemas for major server entities.

- Section 8 details what calls you should make when performing commonly made actions.

- Section 9 outlines the custom error codes and their descriptions.

- Section 10 provides some of the best practices that you should follow when integrating with the WebServices API.

- Section 11 contains the list of countries and their IDs that you can use when performing operations with accounts.

---

## Page: Operations With Accounts
*Source: https://docs.spotware.com/WebServices_API/Operations_With_Accounts*

# ¶ 4. Operations With Accounts


All API calls in this section concern operations with account entities (‘traders’) and related entities (e.g., orders).


All URLs for the API calls described on this page are relative to `https://HOST:PORT/v2`. The value of `HOST:PORT` is provided during the onboarding process by Spotware’s service assurance team.


## ¶ 4.1. Create a Trader

| HTTP Method | URL |
| --- | --- |
| `POST` | `/webserv/traders` |


Creates a new trader entity.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `accessRights` | Yes | enum | The access rights of the account. The following values are accepted. `"FULL_ACCESS"`. The account can perform all operations with no restrictions.`"CLOSE_ONLY"`. The account can only close existing positions.`"NO_TRADING"`. The account cannot perform any trading operations.`"NO_LOGIN"`. The account cannot log into cTrader. |
| `accountType` | Yes | enum | The type of the trading account. The following values are accepted.`HOST:PORT`0. The account can open positions in both directions for the same symbol simultaneously.`HOST:PORT`1. The account can only positions in one directions for a given symbol.`HOST:PORT`2. The account can perform spread betting operations. |
| `HOST:PORT`3 | Yes | long | The total balance of the new account. This parameter primarily exists for the creation of demo accounts with a non-zero balance. |
| `HOST:PORT`4 | Yes | string | A unique name denoting a specific broker (including White Labels). |
| `HOST:PORT`5 | Yes | string | The name of the currency that the account uses for making deposits and withdrawals. |
| `HOST:PORT`6 | Yes | string | The name of the group to which the account is assigned. |
| `HOST:PORT`7 | Yes | string | The MD5 of the account password. |
| `HOST:PORT`8 | Yes | integer | The total amount of leverage available to the account; is specified in 10^2. E.g., the 1:1 leverage is `HOST:PORT`9 while the 1:100 leverage is `POST`0. |
| `POST`1 | Yes | enum | The strategy via which the account margin is calculated. The following values are accepted.`POST`2. The total margin requirements per symbol are equal to the maximum margin requirements for all positions opened for this symbol.`POST`3. The total margin requirements per symbol are equal to the sum of all margin requirements of all positions opened for this symbol.`POST`4. The total margin requirements per symbol are equal to the difference between the margin requirements for all long positions and all short positions opened for this symbol. |
| `POST`5 | No | JSON object | A JSON object containing the trader’s address, phone number, and other details as shown below. |
| `POST`6 | No | string | The trader’s address of residence. |
| `POST`7 | No | string | The trader’s city of residence. |
| `POST`8 | No | integer | The identifier the trader’s country of residence. The full list of these identifiers can be accessed here. |
| `POST`9 | No | string | The trader’s unique document ID. |
| `/webserv/traders`0 | No | string | The trader’s email address. |
| `/webserv/traders`1 | No | string | The trader’s phone number. |
| `/webserv/traders`2 | No | string | The trader’s state of residence. |
| `/webserv/traders`3 | No | string | The zip code of the trader’s residence. |
| `/webserv/traders`4 | No | string | A custom identifier of the first-level partner that has introduced this trader. |
| `/webserv/traders`5 | No | string | A custom identifier of the second level-partner that has introduced this trader. |
| `/webserv/traders`6 | No | string | The description of the account. |
| `/webserv/traders`7 | No | boolean | The trader’s limited risk (LR) status. LR means the establishment of guaranteed stop losses. If `/webserv/traders`8, LR is enabled, and vice versa. |
| `/webserv/traders`9 | No | string | The last name of the account holder. |
| `accessRights`0 | No | enum | The margin calculation strategy used for the limited risk account. The following values are accepted.`accessRights`1. Margin requirements have to be calculated based on the account leverage.`accessRights`2. Margin requirements have to be calculated based on the distance between the position open price and the guaranteed stop loss.`accessRights`3. cServer calculates the leverage-based and GSL-based margin requirements, and chooses the larger of the two values. |
| `accessRights`4 | No | integer | The maximum amount of leverage (in the base currency units) available to the account. Specified in 10^2. |
| `accessRights`5 | No | string | The first name of the account holder. |
| `accessRights`6 | No | boolean | A flag determining whether a daily trading statement is sent to the trader. |
| `accessRights`7 | No | boolean | A flag determining whether a daily account trading statement is sent to the broker under which the account is registered. |
| `accessRights`8 | No | boolean | A flag determining whether the account is charged swaps (`accessRights`9) or administrative fees (`"FULL_ACCESS"`0). |


**Output**


For a JSON schema of the output, [**click here**](/WebServices_API/JSON_Schemas).


Several keys from the request body are repeated in the output, namely `"FULL_ACCESS"`1, `"FULL_ACCESS"`2, `"FULL_ACCESS"`3, `"FULL_ACCESS"`4, `"FULL_ACCESS"`5, `"FULL_ACCESS"`6, `"FULL_ACCESS"`7, `"FULL_ACCESS"`8, `"FULL_ACCESS"`9, `"CLOSE_ONLY"`0, `"CLOSE_ONLY"`1, `"CLOSE_ONLY"`2, `"CLOSE_ONLY"`3, `"CLOSE_ONLY"`4, `"CLOSE_ONLY"`5, `"CLOSE_ONLY"`6, and `"CLOSE_ONLY"`7.

| Key | Data Type | Description |
| --- | --- | --- |
| `"CLOSE_ONLY"`8 | integer | The total amount of bonus funds allocated to the account. Subject to `"CLOSE_ONLY"`9. |
| `"NO_TRADING"`0 | integer | The total amount of equity possessed by the account. Subject to `"NO_TRADING"`1. |
| `"NO_TRADING"`2 | integer | The amount of free margin available to the account. Subject to `"NO_TRADING"`3. |
| `"NO_TRADING"`4 | integer | The current amount of funds that the account can withdraw.It is calculated via the following formula: `"NO_TRADING"`5, where `"NO_TRADING"`6 are all management fees charged by the providers of strategies that the account owner has invested in. Subject to `"NO_TRADING"`7. |
| `"NO_TRADING"`8 | integer | A timestamp with the date and time of the latest account update. |
| `"NO_TRADING"`9 | integer | The number of a specific trading account. |
| `"NO_LOGIN"`0 | integer | The number that determines how finance-related values are defined for the account. E.g., if `"NO_LOGIN"`1 and `"NO_LOGIN"`2, the account balance is 12345.12 in the account deposit currency.Additional details are given in Section 3. |
| `"NO_LOGIN"`3 | integer | The total amount of the non-withdrawable bonus allocated to the account. Subject to `"NO_LOGIN"`4. |
| `"NO_LOGIN"`5 | integer | A timestamp with the date and time of account registration. |
| `"NO_LOGIN"`6 | boolean | If this parameter equals true, rollover commissions are applied to the account instead of swaps. The reverse applies if the parameter is false. This field is useful for ensuring compliance with Sharia law. |
| `"NO_LOGIN"`7 | integer | The total amount of margin in use by the account. Subject to `"NO_LOGIN"`8. |
| `"NO_LOGIN"`9 | integer | The minimum daily equity for the account. The day starts at 00:00 UTC. |
| `accountType`0 | integer | The maximum daily equity for the account. The day starts at 00:00 UTC. |


**Request Example**


```curl
curl -X POST ‘https://HOST:PORT/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": 0, "brokerName": "BESTBROKER", "contactDetails": {"address": "Moon", "city": "Lake", "countryId": 8, "documentId": "0123", "email": "president@bestbroker.com", "phone": "+50987654321", "state": "RE", "zipCode": "5500", "introducingBroker1": "CoolPartner", "introducingBroker2": "AnotherCoolPartner"},"depositCurrency": "EUR", "description": "coolDescription", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "isLimitedRisk": false, "lastName": "President", "leverageInCents": 1000, "maxLeverage": 100000, "name": "Best", "sendOwnStatement": true, "sendStatementToBroker": true, "totalMarginCalculationType": "MAX"}’

```

**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```

**Expected Status Code**


`accountType`1


## ¶ 4.2. Read a Trader’s Details

| HTTP Method | URL |
| --- | --- |
| `accountType`2 | `accountType`3 |


Reads the details of an existing trader entity.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `accountType`4 | path | Yes | integer | The number of a specific trading account. |


**Request Body**


No request body.


**Output**


For a JSON schema of the output, [**click here**](/WebServices_API/JSON_Schemas); also see the output for [**API call 4.1**](#h-41-create-a-trader).


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```

**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```

**Expected Status Code**


`accountType`5


## ¶ 4.3. Read Multiple Traders’ Details

| HTTP Method | URL |
| --- | --- |
| `accountType`6 | `accountType`7 |


Reads the details of multiple trader entities.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `accountType`8 | query | Yes | string | The account registration timestamp. Only accounts registered at or after the specified timestamp are shown in the results.This value is formatted as `accountType`9 in UTC (e.g., `HOST:PORT`00). |
| `HOST:PORT`01 | query | Yes | string | The account registration timestamp.  Only accounts registered before the specified timestamp are shown in the results.This value is formatted as `HOST:PORT`02 in UTC (e.g., `HOST:PORT`03). |
| `HOST:PORT`04 | query | No | string | The start time for deals. Only accounts whose last deals occurred at this start time or after are shown in the results. This value is formatted as `HOST:PORT`05 in UTC (e.g., `HOST:PORT`06). |
| `HOST:PORT`07 | query | No | string | The end time for deals. Only accounts whose last deals occurred before this end time are shown in the results.This value is formatted as `HOST:PORT`08 in UTC (e.g., `HOST:PORT`09). |
| `HOST:PORT`10 | query | No | string | The account details included in the response. The value is formatted as an array of strings (e.g., `HOST:PORT`11).If `HOST:PORT`12 is specified, the trader entity is returned only with the specified fields. Otherwise, it is returned with all fields. |
| `HOST:PORT`13 | query | No | boolean | If `HOST:PORT`14, the response will include only accounts that have open positions. If `HOST:PORT`15, the response will include only accounts that do not have open positions.If this parameter is not specified, the response will include accounts regardless of open positions. |
| `HOST:PORT`16 | query | No | integer | The identifier of an account group. Only accounts assigned to the group are shown in the results. |

> The `HOST:PORT`17 and `HOST:PORT`18 parameters must be both specified or unspecified.

> If both parameters are not specified, the response will include accounts regardless of the timestamps of their last deals.


**Request Body**


No request body.


**Output**


An array of JSON objects with each object having the structure of the output of [**API call 4.1**](#h-41-create-a-trader); for a JSON schema of the output, [**click here**](/WebServices_API/JSON_Schemas).


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/?from=2018-01-01T12:12:12.000&to=2018-03-01T12:12:12.000&groupId=15&token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```

**Response Example**


```json
{
  "trader": [
    {
      "login": 8044900,
      "balance": 0,
      "minEquityDaily": 0,
      "maxEquityDaily": 0
    },
    {
      "login": 8044899,
      "balance": 0,
      "minEquityDaily": 0,
      "maxEquityDaily": 0
    },
    {
      "login": 8044898,
      "balance": 0,
      "minEquityDaily": 0,
      "maxEquityDaily": 0
    }
  ],
  "hasMore": false
}

```

> The data chunk size in a response is limited to 100,000 by default. A response always includes the `HOST:PORT`19 parameter.
> When `HOST:PORT`20 is `HOST:PORT`21 in a response, then the `HOST:PORT`22 parameter in the next request should be changed to the earliest received `HOST:PORT`23 so that the new response provides the next chunk of data. The accounts included in any response are filtered based on `HOST:PORT`24 <= `HOST:PORT`25 < `HOST:PORT`26.

**Expected Status Code**


`HOST:PORT`27


## ¶ 4.4. Read the Details of a Sub-Account

| HTTP Method | URL |
| --- | --- |
| `HOST:PORT`28 | `HOST:PORT`29 |


Reads the details of all sub-accounts (special account entities for strategy following in cTrader Copy) belonging to a trader entity.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `HOST:PORT`30 | path | Yes | integer | The number of a specific trading account. |


**Request Body**


No request body.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `HOST:PORT`31 | object | The object containing an array of logins of the sub-accounts belonging to the specified trader. |
| `HOST:PORT`32 | array | The array of logins of the sub-accounts belonging to the specified trader. |
| `HOST:PORT`33 | integer | The total balance of all sub-accounts belonging to the specified trader. Subject to `HOST:PORT`34 of the trader with the specified `HOST:PORT`35. |
| `HOST:PORT`36 | integer | The total equity of all sub-accounts belonging to the specified trader. Subject to `HOST:PORT`37 of the trader with the specified `HOST:PORT`38. |


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800/subaccounts?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```

**Response Example**


```json
{
  "subAccountLogins":
  {
    "login":
    [
      9006731,
      9006762,
      9006765
    ]
  },
    "totalSubAccountsBalance":46016,
    "totalSubAccountsEquity":47324
}

```


## ¶ 4.5.1. Update a Trader (All Parameters)

| HTTP Method | URL |
| --- | --- |
| `HOST:PORT`39 | `HOST:PORT`40 |

Updates a trader entity.

> When making this API call, all parameters of the trader entity become mandatory in the request body. If you do not specify their values, these parameters will be set to `HOST:PORT`41 or their respective default values.

> Note that this call cannot be used to change a trader’s balance. Instead, use API call 4.7.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `HOST:PORT`42 | path | Yes | integer | The number of a specific trading account. |


**Request Body**


This API call has the same request body as [**API call 4.1**](#h-41-create-a-trader).


**Output**


No output.


**Request Example**


```curl
curl -X PUT 'https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc' -H 'Accept: application/json' -H 'Content-Type: application/json' -d '{"accessRights": "FULL_ACCESS", "brokerName": "BESTBROKER", "contactDetails": {"address": "Moon", "city": "Lake", "countryId": 8, "documentId": "0123", "email": "president@bestbroker.com", "phone": "+50987654321", "state": "RE ", "zipCode": "5500", "introducingBroker1": "CoolPartner", "introducingBroker2": "AnotherCoolPartner"}, "description": "coolDescription", "groupName": "Default", "isLimitedRisk": false, "lastName": "President ", "leverageInCents": 10000, "maxLeverage": 100000, "name": "Best", "sendOwnStatement": true, "sendStatementToBroker": true, "totalMarginCalculationType": "MAX"}'

```

**Response Example**


This API call does not produce an output.


**Expected Status Code**


`HOST:PORT`43


## ¶ 4.5.2. Update a Trader (Specific Parameters)

| HTTP Method | URL |
| --- | --- |
| `HOST:PORT`44 | `HOST:PORT`45 |


Updates a trader entity.

> In contrast to API call 4.5.1., you do not have to specify all parameters of the trader entity when performing this call.

> Note that this call cannot be used to change a trader’s balance. Instead, use API call 4.7.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `HOST:PORT`46 | path | Yes | integer | The number of a specific trading account. |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `HOST:PORT`47 | No | enum | The access rights of the account. The following values are accepted. `HOST:PORT`48. The account can perform all operations with no restrictions.`HOST:PORT`49. The account can only close existing positions.`HOST:PORT`50. The account cannot perform any trading operations.`HOST:PORT`51. The account cannot log into cTrader. |
| `HOST:PORT`52 | No | JSON object | A JSON object containing the trader’s address, phone number, and other details as shown below. |
| `HOST:PORT`53 | No | string | The trader’s address of residence. |
| `HOST:PORT`54 | No | string | The trader’s city of residence. |
| `HOST:PORT`55 | No | integer | The identifier the trader’s country of residence. The full list of these identifiers can be accessed here. |
| `HOST:PORT`56 | No | string | The trader’s unique document ID. |
| `HOST:PORT`57 | No | string | The trader’s email address. |
| `HOST:PORT`58 | No | string | The trader’s phone number. |
| `HOST:PORT`59 | No | string | The trader’s state of residence. |
| `HOST:PORT`60 | No | string | The zip code of the trader’s residence. |
| `HOST:PORT`61 | No | string | A custom identifier of the first-level partner that has introduced this trader. |
| `HOST:PORT`62 | No | string | A custom identifier of the second level-partner that has introduced this trader. |
| `HOST:PORT`63 | No | string | The description of the account. |
| `HOST:PORT`64 | No | string | The name of the group to which the account is assigned. |
| `HOST:PORT`65 | No | boolean | The trader’s limited risk (LR) status. LR means the establishment of guaranteed stop losses. If `HOST:PORT`66, LR is enabled, and vice versa. |
| `HOST:PORT`67 | No | string | The last name of the account holder. |
| `HOST:PORT`68 | No | integer | The total amount of leverage available to the account; is specified in 10^2. E.g., the 1:1 leverage is `HOST:PORT`69 while the 1:100 leverage is `HOST:PORT`70. |
| `HOST:PORT`71 | No | integer | The maximum amount of leverage (in the base currency units) available to the account. Specified in 10^2. |
| `HOST:PORT`72 | No | string | The first name of the account holder. |
| `HOST:PORT`73 | No | boolean | A flag determining whether a daily trading statement is sent to the trader. |
| `HOST:PORT`74 | No | boolean | A flag determining whether a daily account trading statement is sent to the broker under which the account is registered. |
| `HOST:PORT`75 | No | boolean | A flag determining whether the account is charged swaps (`HOST:PORT`76) or administrative fees (`HOST:PORT`77). |


**Output**


No output.


**Request Example**


```curl
curl -X PATCH 'https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc' -H 'Accept: application/json' -H 'Content-Type: application/json' -d '{"description": "updatedDescription", "groupName": "newGroup", "maxLeverage": 50000}'

```

**Response Example**


This API call does not produce an output.


**Expected Status Code**


`HOST:PORT`78


## ¶ 4.6. Delete a Trader

| HTTP Method | URL |
| --- | --- |
| `HOST:PORT`79 | `HOST:PORT`80 |


Deletes a trader entity.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `HOST:PORT`81 | path | Yes | integer | The number of a specific trading account. |


**Request Body**


No request body.


**Output**


No output.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
0
**Response Example**


This API call does not produce an output.


**Expected Status Code**


`HOST:PORT`82


## ¶ 4.7. Change a Trader’s Balance

| HTTP Method | URL |
| --- | --- |
| `HOST:PORT`83 | `HOST:PORT`84 |


Changes the balance of a trader entity (including allocating/removing credit).


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `HOST:PORT`85 | path | Yes | integer | The number of a specific trading account. |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `HOST:PORT`86 | No | string | A short note that can be attached to any balance change. This note is not shown to retail clients. |
| `HOST:PORT`87 | No | string | A number that matches an external identifier of the broker’s choosing. For instance, the value of `HOST:PORT`88 could be equal to the number of the bank transfer order through which the user chose to make a deposit. |
| `HOST:PORT`89 | No | string | A brief comment that can supplement a deposit or a withdrawal. In contrast to `HOST:PORT`90, this text is displayed to retail clients. |
| `HOST:PORT`91 | Yes | integer | The number of a specific trading account. |
| `HOST:PORT`92 | Yes | double | The precise amount of withdrawn or deposited funds/credit. Specified as a decimal number. For BTC and similar assets, the value of `HOST:PORT`93 can include as many as eight digits after the decimal point. |
| `HOST:PORT`94 | No | string | The designated source of the deposit/withdrawal. |
| `HOST:PORT`95 | Yes | string | The desired type of balance change. The following values are accepted.`HOST:PORT`96. Deposit funds to the trader.`HOST:PORT`97. Withdraw funds from the trader.  `HOST:PORT`98. Deposit credit to the trader. `HOST:PORT`99. Withdraw credit from the trader. |
| `POST`00 | No | boolean | If true, margin requirements will be skipped. This may result in Stop Out, negative balance or both. |

> Note that only positive values are accepted when specifying the `POST`01 parameter. The direction of the balance change is regulated entirely by the `POST`02 parameter.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `POST`03 | integer | The identifier of a balance history entity containing all balance-related transactions for the specified trader.Note that bonus and credit are not included in `POST`04. |


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
1
**Output Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
2
**Expected Status Code**


`POST`05


## ¶ 4.8. Change a Trader’s Password

| HTTP Method | URL |
| --- | --- |
| `POST`06 | `POST`07 |


Changes the password for authenticating a trader entity.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `POST`08 | path | Yes | integer | The number of a specific trading account. |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `POST`09 | Yes | string | The MD5 of the new password of the account |
| `POST`10 | Yes | integer | The number of a specific trading account. |


**Output**


No output.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
3
**Output Example**


This API call does not produce an output.


**Expected Status Code**


`POST`11


## ¶ 4.9. Check a Trader’s Password

| HTTP Method | URL |
| --- | --- |
| `POST`12 | `POST`13 |


Checks the password for authenticating a trader entity.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `POST`14 | path | Yes | integer | The number of a specific trading account. |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `POST`15 | Yes | string | The MD5 of the account password. |
| `POST`16 | Yes | integer | The number of a specific trading account. |


**Output**


No output.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
4
**Output Example**


This API call does not produce an output.


**Expected Status Code**


`POST`17


## ¶ 4.10. Change a Trader’s Bonus

| HTTP Method | URL |
| --- | --- |
| `POST`18 | `POST`19 |


Changes the amount of bonus allocated to a given trader.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `POST`20 | path | Yes | integer | The number of a specific trading account. |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `POST`21 | No | string | A short note that can be attached to the bonus change. This note is not shown to retail clients. |
| `POST`22 | No | string | A number that matches an external identifier of the broker’s choosing. For instance, the value of `POST`23 could be equal to the number of the bank transfer order through which the user chose to make a deposit. |
| `POST`24 | No | string | A brief comment that described the change. In contrast to `POST`25, this text is displayed to retail clients. |
| `POST`26 | Yes | integer | The number of a specific trading account. |
| `POST`27 | Yes | double | The precise amount of withdrawn or deposited bonus. Specified as a decimal number. For BTC and similar assets, the value of `POST`28 can include as many as eight digits after the decimal point. |
| `POST`29 | Yes | string | The desired type of change. The following values are accepted.`POST`30. Allocate bonus to the trader. `POST`31. Withdraw bonus from the trader. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `POST`32 | integer | The identifier of a bonus history entity containing all bonus-related transactions for the specified trader. |


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
5
**Output Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
6
**Expected Status Code**


`POST`33


## ¶ 4.11. Request a List of All Trader Groups

| HTTP Method | URL |
| --- | --- |
| `POST`34 | `POST`35 |


Gets a list of all trader groups.


**Parameters**


No parameters.


**Request Body**


No request body.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `POST`36 | array | An array containing JSON or XML objects representing account groups. |
| `POST`37 | integer | The identifier of an account group. |
| `POST`38 | string | The name of an account group. |
| `POST`39 | string | The description of an account group. |


For a JSON schema of the output, [**click here**](/WebServices_API/JSON_Schemas).


**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
7
**Output Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
8
**Expected Status Code**


`POST`40


## ¶ 4.12. Request a List of Open Positions

| HTTP Method | URL |
| --- | --- |
| `POST`41 | `POST`42 |


Gets either a list of all open positions or a list of open positions originated by a specific trader entity (if the `POST`43 parameter is specified).


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `POST`44 | query | No | integer | The number of a specific trading account. |


**Request Body**


No request body.


**Output**


This API call returns a comma-separated ‘grid’ containing information about position entities and their details.

| Column | Data Type | Description |
| --- | --- | --- |
| `POST`45 | integer | The number of a specific trading account. |
| `POST`46 | integer | The unique identifier of a position entity. |
| `POST`47 | string | The timestamp of the moment when the position was opened.This value is formatted as `POST`48 in UTC (e.g., `POST`49). |
| `POST`50 | decimal | The entry price for the position. |
| `POST`51 | string | The position direction. The following values are permitted. `POST`52. Denotes a long position.`POST`53. Denotes a short position. |
| `POST`54 | double | The traded volume denoted in units of the base asset. |
| `POST`55 | string | The symbol for which the position is opened. Permitted values include all valid symbol names that exist on the server. |
| `POST`56 | double | The commission paid for opening the position; denoted in USD. |
| `POST`57 | double | The SWAPs charged for holding the position open overnight; denoted in USD. |
| `POST`58 | string | The order execution book that was used for opening the position. The following values are permitted.`POST`59. Denotes Book A execution. `POST`60. Denotes Book B execution. |
| `POST`61 | double | The spread betting stake of the position; denoted in the account deposit currency. |
| `POST`62 | boolean | A flag that determines whether the position is of the spread betting type. |
| `POST`63 | double | The margin used by the position denoted in the account deposit currency. |


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 100000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
9
**Output Examples**


The following output is produced if the `POST`64 parameter is omitted.


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
0
The following output is produced if the `POST`65 parameter is specified.


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
1
**Expected Status Code**


`POST`66


## ¶ 4.13. Request a List of Closed Positions

| HTTP Method | URL |
| --- | --- |
| `POST`67 | `POST`68 |


Gets either a list of all closed positions or a list of closed positions originated by a specific trader entity (if the `POST`69 parameter is specified).

> Note that each row in the output represents one specific result of closing a position, be it wholly or partially. As a result, you may see cases where `POST`70 is repeated across several rows. This is intended behavior as it represents positions that were closed via multiple deals.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `POST`71 | query | Yes | string | The position creation timestamp; only positions that have been created at or after the specified timestamp will be shown in the results.This value is formatted as `POST`72 in UTC (e.g., `POST`73). |
| `POST`74 | query | Yes | string | The position creation timestamp; only positions that have been created before the specified timestamp will be shown in the results.This value is formatted as `POST`75 in UTC (e.g., `POST`76). |
| `POST`77 | query | No | integer | The number of a specific trading account. |

> The difference between the timestamps specified in the `POST`78 and `POST`79 parameters must be equal to two days or less.


**Request Body**


No request body.


**Output**


This API call returns a comma-separated ‘grid’ containing information about position entities and their details.

| Column | Data Type | Description |
| --- | --- | --- |
| `POST`80 | integer | The number of a specific trading account. |
| `POST`81 | integer | The unique identifier of a position entity. |
| `POST`82 | integer | The unique identifier of the deal entity that has closed the position with the given `POST`83.If multiple results are returned with the same `POST`84 but with different `POST`85s, the position was closed via several closing deals. |
| `POST`86 | string | The timestamp of the moment when the position was opened.This value is formatted as `POST`87 in UTC (e.g., `POST`88). |
| `POST`89 | string | The timestamp of the moment when position was closed. This value is formatted as `POST`90 in UTC (e.g., `POST`91). |
| `POST`92 | decimal | The VWAP of the volume that was used in the closing deal(s) of the position with the given `POST`93.E.g., the position was opened via two deals; the first one was executed for 50,000 units at 1.2, the second one was executed at 20,000 units at 1.3. There was only one closing deal for the full volume of 70,000. The `POST`94 was calcuated as `POST`95. |
| `POST`96 | decimal | The price at which the position was closed (wholly or partially). |
| `POST`97 | string | The position direction. The following values are permitted.`POST`98. Denotes a long position.`POST`99. Denotes a short position. |
| `/webserv/traders`00 | double | The traded volume denoted in units of the base asset. |
| `/webserv/traders`01 | string | The symbol for which the position is opened. Permitted values include all valid symbol names that exist on the server. |
| `/webserv/traders`02 | double | The commission paid for opening the position; denoted in USD. |
| `/webserv/traders`03 | double | The SWAPs charged for holding the position open overnight; denoted in USD. |
| `/webserv/traders`04 | double | The net realized PnL generated by the position. |
| `/webserv/traders`05 | decimal | The conversion rate between the base asset of the symbol for which the position was opened and the account deposit currency of the trader entity that has opened the position. |
| `/webserv/traders`06 | decimal | The conversion rate between the base asset of the symbol for which the position was opened and USD. |
| `/webserv/traders`07 | string | The order execution book that was used for opening the position. The following values are permitted.`/webserv/traders`08. Denotes Book A execution.`/webserv/traders`09. Denotes Book B execution. |
| `/webserv/traders`10 | double | The spread betting stake of the position; denoted in the account deposit currency. |
| `/webserv/traders`11 | boolean | A flag that determines whether the position is of the spread betting type. |


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
2
**Response Example**


The following output is produced if the `/webserv/traders`12 parameter is omitted.


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
3
The following output is produced if the `/webserv/traders`13 parameter is specified.


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
4
**Expected Status Code**


`/webserv/traders`14


## ¶ 4.14. List Trader Attributes

| HTTP Method | URL |
| --- | --- |
| `/webserv/traders`15 | `/webserv/traders`16 |


Fetches the current attributes for one or more traders.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/traders`17 | No | array | An array of trader IDs (1–10,000). When omitted or empty, all visible traders that own at least one attribute row are returned. |
| `/webserv/traders`18 | No | integer | The number of records to be returned per page (1–10,000, default 10,000). Only allowed when `/webserv/traders`19 is omitted. |
| `/webserv/traders`20 | No | integer | Cursor for the next page (≥0, default 0). Only allowed when `/webserv/traders`21 is omitted. |
| `/webserv/traders`22 | No | string | Case-insensitive substring filter on attribute name (0–64 characters). |
| `/webserv/traders`23 | No | integer | The epoch unix timestamp (in milliseconds) used to return only traders whose latest attribute row is greater than or equal to this value. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/webserv/traders`24 | array | An array containing one entry per authorised trader with at least one attribute row. |
| `/webserv/traders`25 | integer | The unique identifier of a trader. |
| `/webserv/traders`26 | array | An array of objects containing `/webserv/traders`27 pairs. |
| `/webserv/traders`28 | integer | The epoch unix timestamp (in milliseconds) of the latest attribute row for the trader. |
| `/webserv/traders`29 | integer or null | Cursor for the next call. Present only when more pages are available. |


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
5
**Response Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
6
**Expected Status Code**


`/webserv/traders`30


## ¶ 4.15. List Trader Group Attributes

| HTTP Method | URL |
| --- | --- |
| `/webserv/traders`31 | `/webserv/traders`32 |


Fetches the current attributes for one or more trader groups. Only groups that have at least one attribute row are returned.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/traders`33 | Yes | array | An array of trader group IDs (1–10,000). No “all” mode. No paging. |
| `/webserv/traders`34 | No | string | Case-insensitive substring on attribute name (0–64 characters). Field `/webserv/traders`35 must have length of 0–64. |
| `/webserv/traders`36 | No | integer | The epoch unix timestamp (in milliseconds). Only groups whose most recent attribute row is greater than or equal to this value are returned. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/webserv/traders`37 | array | One object per authorised trader group that has at least one attribute row. |
| `/webserv/traders`38 | integer | The unique identifier of a trader group. |
| `/webserv/traders`39 | array | An array of objects containing `/webserv/traders`40 pairs. |
| `/webserv/traders`41 | integer | The epoch unix timestamp (in milliseconds) of the most recent attribute row for this group. |


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
7
**Response Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
8
**Expected Status Code**


`/webserv/traders`42


## ¶ 4.16. List Manager Attributes

| HTTP Method | URL |
| --- | --- |
| `/webserv/traders`43 | `/webserv/traders`44 |


Fetches the current attributes for one or more managers. Only managers that have at least one attribute row are returned.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/traders`45 | Yes | array | An array of manager IDs (1–10,000). For a regular manager, only their own ID is allowed; for a super-admin, any ID is allowed. No paging is available. |
| `/webserv/traders`46 | No | string | Case-insensitive substring on attribute name (0–64 characters). |
| `/webserv/traders`47 | No | integer | The epoch unix timestamp (in milliseconds). Only managers whose most recent attribute row is greater than or equal to this value are returned. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/webserv/traders`48 | array | One object per authorised manager that has at least one attribute row. |
| `/webserv/traders`49 | integer | The unique identifier of a manager. |
| `/webserv/traders`50 | array | An array of objects containing `/webserv/traders`51 pairs. |
| `/webserv/traders`52 | integer | The epoch unix timestamp (in milliseconds) of the most recent attribute row for this manager. |


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/9017800?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
9
**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
0
**Expected Status Code**


`/webserv/traders`53


## ¶ 4.17. Update Trader Attributes

| HTTP Method | URL |
| --- | --- |
| `/webserv/traders`54 | `/webserv/traders`55 |


Creates or updates (upserts) multiple traders’ attribute sets in one call.

> The call succeeds for authorised trader IDs, while unauthorised ones are omitted from the response. When none of the supplied IDs pass access control, the call returns `/webserv/traders`56.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/traders`57 | Yes | array | An array (1–100 items) of objects, each containing the fields `/webserv/traders`58 and `/webserv/traders`59. Only authorised trader IDs are processed. |
| `/webserv/traders`60 | Yes | integer | The unique identifier of a trader to upsert or delete attributes for. |
| `/webserv/traders`61 | Yes | array | An array (1–100 items) of `/webserv/traders`62 pairs. `/webserv/traders`63 must be 1–64 UTF-8 characters, not empty. `/webserv/traders`64 must be 1–512 UTF-8 characters and not null. |


**Output**


An empty object `/webserv/traders`65 is returned upon success.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
1
**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
2
**Expected Status Code**


`/webserv/traders`66


## ¶ 4.18. Update Trader Group Attributes

| HTTP Method | URL |
| --- | --- |
| `/webserv/traders`67 | `/webserv/traders`68 |


Creates or upserts multiple trader groups’ attribute sets in one call.

> The call succeeds for authorised trader group IDs, while unauthorised ones are omitted from the response. When none of the supplied IDs pass access control, the call returns `/webserv/traders`69.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/traders`70 | Yes | array | An array (1–100 items) of objects, each containing the fields `/webserv/traders`71 and `/webserv/traders`72. Only authorised trader group IDs are processed. |
| `/webserv/traders`73 | Yes | integer | The unique identifier of a trader group to upsert or delete attributes for. |
| `/webserv/traders`74 | Yes | array | An array (1–100 items) of `/webserv/traders`75 pairs. `/webserv/traders`76 must be 1–64 UTF-8 characters, not empty. `/webserv/traders`77 must be 1–512 UTF-8 characters and not null. |


**Output**


An empty object `/webserv/traders`78 is returned upon success.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
3
**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
4
**Expected Status Code**


`/webserv/traders`79


## ¶ 4.19. Update Manager Attributes

| HTTP Method | URL |
| --- | --- |
| `/webserv/traders`80 | `/webserv/traders`81 |


Creates or updates (upserts) multiple managers’ attribute sets in one call.

> The call succeeds for authorised manager IDs, while unauthorised ones are omitted from the response. When none of the supplied IDs pass access control, the call returns `/webserv/traders`82.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/traders`83 | Yes | array | An array (1–100 items) of objects, each containing the fields `/webserv/traders`84 and `/webserv/traders`85. Only authorised manager IDs are processed. |
| `/webserv/traders`86 | Yes | integer | The unique identifier of a manager to upsert or delete attributes for. For a regular manager, only their own ID is allowed; for a super-admin, any ID is allowed. |
| `/webserv/traders`87 | Yes | array | An array (1–100 items) of `/webserv/traders`88 pairs. `/webserv/traders`89 must be 1–64 UTF-8 characters, not empty. `/webserv/traders`90 must be 1–512 UTF-8 characters and not null. |


**Output**


An empty object `/webserv/traders`91 is returned upon success.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
5
**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
6
**Expected Status Code**


`/webserv/traders`92


## ¶ 4.20. Delete Trader Attributes

| HTTP Method | URL |
| --- | --- |
| `/webserv/traders`93 | `/webserv/traders`94 |


Deletes one or more traders’ attributes in bulk.

> The call succeeds for authorised trader IDs, while unauthorised ones are omitted from the operation. A `/webserv/traders`95 status is returned only if none of the supplied IDs are authorised. If `/webserv/traders`96 is omitted or empty, all attributes for the specified traders are deleted.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/traders`97 | Yes | array | An array (1–10,000) of trader IDs whose attributes are to be deleted. |
| `/webserv/traders`98 | No | array | An array (0–100) of attribute names to delete. If omitted or empty, all attributes for the specified traders are deleted. Each name must be 1–64 UTF-8 characters, not empty. |


**Output**


An empty object `/webserv/traders`99 is returned upon success.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
7
**Response Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
8
**Expected Status Code**


`accessRights`00


## ¶ 4.21. Delete Trader Group Attributes

| HTTP Method | URL |
| --- | --- |
| `accessRights`01 | `accessRights`02 |


Deletes one or more trader groups’ attributes in bulk.

> The call succeeds for authorised trader group IDs, while unauthorised ones are omitted from the operation. A `accessRights`03 status is returned only if none of the supplied IDs are authorised. If `accessRights`04 is omitted or empty, all attributes for the specified trader groups are deleted.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `accessRights`05 | Yes | array | An array (1–10,000) of trader group IDs whose attributes are to be deleted. |
| `accessRights`06 | No | array | An array (0–100) of attribute names to delete. If omitted or empty, all attributes for the specified trader groups are deleted. Each name must be 1–64 UTF-8 characters, not empty. |


**Output**


An empty object `accessRights`07 is returned upon success.


**Request Example**


```json
{
  "accessRights": "FULL_ACCESS",
  "accountType": "HEDGED",
  "balance": 0,
  "bonus": 0,
  "cashEquity": 0,
  "brokerName": "BESTBROKER",
  "contactDetails": {
    "address": "Moon",
    "city": "Lake",
    "countryId": 8,
    "documentId": "0123",
    "email": "president@bestbroker.com",
    "phone": "+50987654321",
    "state": "RE",
    "zipCode": "5500",
    "introducingBroker1": "CoolPartner",
    "introducingBroker2": "AnotherCoolPartner"
  },
  "depositCurrency": "EUR",
  "description": "coolDescription",
  "equity": 0,
  "freeMargin": 0,
  "groupName": "Default",
  "isLimitedRisk": false,
  "lastConnectionTimestamp": 0,
  "lastName": "President",
  "lastUpdateTimestamp": 0,
  "leverageInCents": 1000,
  "limitedRiskMarginCalculationStrategy": "ACCORDING_TO_LEVERAGE",
  "login": 9017800,
  "maxLeverage": 1000,
  "moneyDigits": 0,
  "name": "Best",
  "nonWithdrawableBonus": 0,
  "registrationTimestamp": 0,
  "sendOwnStatement": true,
  "sendStatementToBroker": true,
  "swapFree": true,
  "totalMarginCalculationType": "MAX",
  "usedMargin": 0
}

```
9
**Response Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/?from=2018-01-01T12:12:12.000&to=2018-03-01T12:12:12.000&groupId=15&token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
0
**Expected Status Code**


`accessRights`08


## ¶ 4.22. Delete Manager Attributes

| HTTP Method | URL |
| --- | --- |
| `accessRights`09 | `accessRights`10 |


Deletes one or more managers’ attributes in bulk.

> The call succeeds for authorised manager IDs, while unauthorised ones are omitted from the operation. A `accessRights`11 status is returned only if none of the supplied IDs are authorised. If `accessRights`12 is omitted or empty, all attributes for the specified managers are deleted.

> Regular (non-super-admin) managers may only delete their own ID; super-admins may delete any.


**Parameters**


No parameters


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `accessRights`13 | Yes | array | An array (1–10,000) of manager IDs whose attributes are to be deleted. |
| `accessRights`14 | No | array | An array (0–100) of attribute names to delete. If omitted or empty, all attributes for the specified managers are deleted. Each name must be 1–64 UTF-8 characters, not empty. |


**Output**


An empty object `accessRights`15 is returned upon success.


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/?from=2018-01-01T12:12:12.000&to=2018-03-01T12:12:12.000&groupId=15&token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
1
**Response Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/traders/?from=2018-01-01T12:12:12.000&to=2018-03-01T12:12:12.000&groupId=15&token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```
2
**Expected Status Code**


`accessRights`16

---

## Page: Operations With cTID
*Source: https://docs.spotware.com/WebServices_API/Operations_With_cTID*

# ¶ 5. Operations With cTID


All API calls in this section concern operations with [**cTID entities (‘users’)**](/WebServices_API/Domain_Model_and_Logic/).


All URLs for the API calls described in this section are relative to `https://HOST:PORT/cid`. The value of `HOST:PORT` is provided during the onboarding process by Spotware’s service assurance team.


## ¶ 5.1. Create a cTID

| HTTP Method | URL |
| --- | --- |
| `POST` | `/ctid/create` |


Creates a new user entity.

> Note that this API call cannot be used for creating new cTIDs as part of our SSO (OAuth) solution. For more information, please refer to our SSO (OAuth) documentation.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `brokerName` | No | string | A unique name denoting a specific broker (including White Labels). |
| `email` | Yes | string | The email address assigned to the new user. |
| `preferredLanguage` | No | string | An Alpha-2 code denoting the preferred language of the new user. |


**Output**

> Note that there are two possible outputs depending on whether you specify a unique `email` in the request body (an email that is not used by any of the users registered on your server). If `email` is unique, the response will include all parameters from the below table. If the specified `email` is already assigned to an existing user, the output will only include the `HOST:PORT`0 parameter.

| Key | Data Type | Description |
| --- | --- | --- |
| `HOST:PORT`1 | integer | The unique identifier of the user entity. |
| `HOST:PORT`2 | string | The nickname of the user entity. By default, `HOST:PORT`3. |
| `HOST:PORT`4 | string | The email assigned to the user entity. |
| `HOST:PORT`5 | string | An Alpha-2 code denoting the preferred language of the user entity. |
| `HOST:PORT`6 | integer | The epoch unix timestamp of the creation of the user entity. |
| `HOST:PORT`7 | enum | The status of the new user entity. Possible values: - `HOST:PORT`8. The default status for any new user.- `HOST:PORT`9. The status denoting an existing active user who has confirmed their email address in the cTrader ecosystem. Note that only users with `POST`0 as their `POST`1 receive trading notifications in their email inbox.- `POST`2. The status denoting a deleted user entity.Note that receiving `POST`3 or `POST`4 in the response body would constitute unexpected behavior. |


For a JSON schema of the output, [**click here**](/WebServices_API/JSON_Schemas).


**Request Example**


```curl
curl -X POST 'https://HOST:PORT/cid/ctid/create?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc' -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"brokerName": "BESTBROKER", "email": "president@bestbroker.com", "preferredLanguage": "EN"}'

```

**Response Examples**

- If a Unique `POST`5 Is Specified
- If an Existing `POST`6 Is Specified

---

## Page: Domain Model and Logic
*Source: https://docs.spotware.com/WebServices_API/Domain_Model_and_Logic*

# ¶ 2. Domain Model and Logic


This page defines the key terms and entities forming the core cTrader infrastructure.


## ¶ 2.1. Defining Server Structure


cTrader servers are comprised of the following elements.


**Plant**. This term denotes a logical aggregation of several environments into a single ‘pack’. In the vast majority of cases, a plant combines all environments managed by a single broker. This aggregation is useful to quickly and clearly identify a specific trading server (as shown below by our naming convention) and to facilitate billing.


**Environment**. This term defines an actual server which is itself an instance of the backend solution provided by Spotware to a broker. Our generic setup allows two environments (namely `demo` or `live`) to exist on one plant. Brokers can request the creation of additional environments (e.g., `live2`) with any naming. A single broker may have an unlimited number of environments. However, the deployment of each new environment is billed separately and constitutes an additional charge. Please contact [sales@spotware.com](sales@spotware.com) to get more information on adding new environments.


**Broker (White Label)**. This designation applies to an entity that can be used to segregate trading accounts registered on one plant. This entity, therefore, may refer to different White Labels (WLs) and/or jurisdictions. By default, each plant contains one broker (which is denoted as `brokerName` in this API) with the name of this broker also used as the plant name. Note that a plant may support a potentially infinite number of broker/WL entities.


Given the terms defined above, our naming convention for a trading server is `{environment}.{plant}`. For example, a server could be designated as `demo.superbroker`.


The following examples graphically summarize the relationship between plants, environments, and brokers.

- Plant With Two Servers and Two Brokers
- Plant With Three Servers (Environments) and One Broker

---

## Page: Best Practices
*Source: https://docs.spotware.com/WebServices_API/Best_Practices*

# ¶ 10. Best Practices


This tutorial describes some of the common best practices that should be followed by CRM systems/client areas integrated with the **WebServices API**.


## ¶ 10.1. Supporting Essential Functionality


Successful **WebServices API** integration is only possible if your CRM/client area supports the following use cases (for a refresher on key terms, refer to [**the definition of our domain model**](/WebServices_API/Domain_Model_and_Logic)).


- Creating new users (new cTID entities) (API call 5.1)

- Creating new traders (API call 4.1)

- Linking a trader to a user (API call 5.2)

- Handling deposits and withdrawals (API call 4.7)


As such, you should prioritise the implementation of these use cases in your integration process. We recommend conducting extensive testing of your implementation as the functionality listed above is crucial for any effective CRM/client area linked to the cTrader backend.


## ¶ 10.2. Implementing Additional Analytics


The **WebServices API** exposes several endpoints that you can consume to display various analytics to your traders.

> Here are just some examples of the data you can show in your client area.
> a. Total realised P&L for all positions closed during a specific period.
> b. The asset classes, symbol categories, and/or symbols that the trader has frequently placed new orders for during the past month.
> c. The total volume of all positions currently opened by the trader.
> d. The balance and equity of all Copy sub-accounts created by the trader.
> e. The winning/losing trade ratio for a chosen period.


The API calls you can use to attain the relevant data are listed below.


- API call 4.12 returns a list of all currently open positions (and their details) that you can optionally narrow down by trader.

- API call 4.13 returns a list of all closed positions (and their details) during the specified period; this list can also be optionally narrowed down by trader.

- API call 6.1 returns a list of all symbols available on the server along with their categories and asset classes.

- API call 4.4 returns the details of all Copy sub-accounts for a particular trader.


> Note that the WebServices API does not allow for receiving real-time events, meaning that you would need to send separate requests each time you want to refresh the statistics shown in your CRM system/client area. In this case, make sure that such requests are sent at reasonable intervals (e.g., once when a trader opens the analytics page and then every minute until the trader leaves the page). We reserve the right to restrict access to the WebServices API if you send requests with excessive frequency (e.g., every second).

> If you want to react to new data arriving in real time, consider additionally integrating with the Reporting API.


## ¶ 10.3. Handling Trader and User Creation Correctly


To correctly handle the creation and linkage of all major server entities in the cTrader backend, you should send the following API calls in the order given below.


- API call 5.1 for user creation

- API call 4.1 for trader creation

- API call 5.2 for trader-user linkage


In our [**domain model**](/WebServices_API/Domain_Model_and_Logic), users are higher-order entities to which new traders are linked; as such, creating new users first is the recommended flow for any integration.


When someone new registers inside your CRM, the need to create a new user in the cTrader backend depends based on whether your CRM/client area is designed to accept registrants from different platforms.


This decision-making process can be explained via the following flow chart.

flowchart TD
    A(["Does the CRM/client area work with traders (accounts) from platforms other than cTrader?"])
  B([User creation can occur immediately after someone new registers inside the CRM])
  C([User creation can only occur after it is clear that the new registrant wants to use cTrader])
  A == No ==> B
  A == Yes ==> C


If your CRM/client area only takes new traders from cTrader, there is no need to determine the platform that a new registrant comes from. As a result, you can request the creation of a new cTrader user each time someone new completes the signup process in your CRM.


In contrast, if your CRM/client area can take new registrants from several different platforms, there may be no need to create a new user in the cTrader backend. As a result, you would need to design and implement a custom mechanism for determining the platform that a new registrant wants to use. If this mechanism identifies cTrader as the preferred platform, you would need to create a new user entity.

> As an example, your CRM/client area may show an interactable platform selector menu to all new registrants. You would need to create a new user only after cTrader is selected in this menu and the registrant confirms their choice.


## ¶ 10.4. Handling Withdrawals Correctly


It is essential to differentiate between the following types of withdrawals requests.


- Withdrawal requests received by a backoffice manager.

- Withdrawal requests sent to the cTrader backend via API call 4.7.


Withdrawal requests received by a backoffice manager can be handled and processed according to your internal business logic. However, when such a request is is received, it is imperative for its results to be reflected in the cTrader backend. To achieve this goal, you should send [**API call 4.7**](/WebServices_API/Operations_With_Accounts#h-47-change-a-traders-balance) with `"type": "WITHDRAW"` and `"preciseAmount": {withdrawalAmount}`in the request body.

> Sending API call 4.7 request (and receiving a successful response) has to occur earlier than processing the withdrawal request in your system (e.g., by returning the withdrawn funds to the trader via bank transfer). This is needed to avoid a case where a trader can place new orders using the money that they have technically already withdrawn.

---

## Page: JSON Schemas
*Source: https://docs.spotware.com/WebServices_API/JSON_Schemas*

# ¶ 7. JSON Schemas


This section provides the JSON schemas for all major server entities on which you can perform operations while using the WebServices API.


## ¶ 7.1. Trader (Account)


```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Trader",
    "description": "The entity responsible for performing trading operations",
    "type": "object",
    "properties": {
        "login": {
            "description": "The number of a specific trading account",
            "type": "long",
            "examples": [
                9017800
            ]
        },
        "groupName": {
            "description": "The name of the group to which the account is assigned",
            "type": "string",
            "examples": [
                "Default"
            ]
        },
        "depositCurrency": {
            "description": "The name of the currency that the account uses for making deposits and withdrawals",
            "type": "string",
            "examples": [
                "EUR",
                "USD",
                "CHF"
            ]
        },
        "name": {
            "description": "The first name of the account holder",
            "type": "string",
            "examples": [
                "John"
            ]
        },
        "lastName": {
            "description": "The last name of the account holder",
            "type": "string",
            "examples": [
                "Smith"
            ]
        },
        "description" : {
            "description": "The description of the account",
            "type": "string",
            "examples": [
                "John's account"
            ]
        },
        "accessRights": {
            "description": "The access rights of the account",
            "type": "enum",
            "oneOf": [
                {
                    "const": "FULL_ACCESS",
                    "description": "The account can perform all operations with no restrictions"
                },
                {
                    "const": "CLOSE_ONLY",
                    "description": "The account can only close existing positions"
                },
                {
                    "const": "NO_TRADING",
                    "description": "The account cannot perform any trading operations"
                },
                {
                    "const": "NO_LOGIN",
                    "description": "The account cannot log into cTrader"
                }
            ]
        },
        "balance": {
            "description": "The total balance of the new account",
            "type": "long",
            "examples": [
                1234512
            ]
        },
        "bonus": {
            "description": "The total amount of bonus funds allocated to the account",
            "type": "long",
            "examples": [
                1234512
            ]
        },
      	"cashEquity": {
          "description": "The total amount of funds that the account owner can withdraw",
      		"type": "long",
      		"examples": [
            		1234512
        	]
        },
        "nonWithdrawableBonus": {
            "description": "The total amount of credit allocated to the account",
            "type": "long",
            "examples": [
                1234512
            ]
        },
        "leverageInCents": {
            "description": "The total amount of leverage available to the account; is specified in 10^2",
            "type": "int",
            "examples": [
                100
            ]
        },
        "contactDetails": {
            "description": "An object containing the trader’s address, phone number, and other details",
            "type": "object",
            "properties": {
                "address": {
                    "description": "The trader’s address of residence",
                    "type": "string",
                    "examples": [
                        "Moon"
                    ]
                },
                "city": {
                    "description": "The trader’s city of residence",
                    "type": "string",
                    "examples": [
                        "Lake"
                    ]
                },
                "countryId": {
                    "description": "The identifier denoting the trader's country of residence",
                    "type": "integer",
                    "examples": [
                        8
                    ]
                },
                "documentId": {
                    "description": "The trader’s unique document ID",
                    "type": "string",
                    "examples": [
                        "01234"
                    ]
                },
                "email": {
                    "description": "The trader's email address",
                    "type": "string",
                    "examples": [
                        "president@bestbroker.com"
                    ]
                },
                "phone": {
                    "description": "The trader's phone number",
                    "type": "string",
                    "examples": [
                        "+50987654321"
                    ]
                },
                "state": {
                    "description": "The trader's state of residence",
                    "type": "string",
                    "examples": [
                        "RE"
                    ]
                },
                "zipCode": {
                    "description": "The zip code of the trader’s residence",
                    "type": "string",
                    "examples": [
                        "5500"
                    ]
                },
                "introducingBroker1": {
                    "description": "A custom designation of the first-level partner to which the trader is attributed",
                    "type": "string",
                    "examples": [
                        "CoolPartner"
                    ]
                },
                "introducingBroker2": {
                    "description": "A custom designation of the second-level partner to which the trader is attributed",
                    "type": "string",
                    "examples": [
                        "GreatPartner"
                    ]
                },
                "required": []
            }
        },
        "accountType": {
            "description": "The type of the trading account",
            "type": "enum",
            "oneOf": [
                {
                    "const": "HEDGED",
                    "description": "The account can open positions in both directions for the same symbol simultaneously"
                },
                {
                    "const": "NETTED",
                    "description": "The account can only positions in one direction for a given symbol"
                },
                {
                    "const": "SPREAD_BETTING",
                    "description": "The account can perform spread betting operations"
                }
            ]
        },
        "sendOwnStatement": {
            "description": "A flag determining whether a daily trading statement is sent to the trader",
            "type": "boolean",
            "examples": [
                true
            ]
        },
        "swapFree": {
            "description": "A flag determining whether the account is charged swaps or administrative fees",
            "type": "boolean",
            "examples": [
                false
            ]
        },
        "brokerName": {
            "description": "A unique name denoting a specific broker (including White Labels)",
            "type": "string",
            "examples": [
                "BESTBROKER"
            ]
        },
        "totalMarginCalculationType": {
            "description": "The strategy via which the account margin is calculated",
            "type": "enum",
            "oneOf": [
                {
                    "const": "MAX",
                    "description": "The total margin requirements per symbol are equal to the maximum margin requirements for all positions opened for this symbol"
                },
                {
                    "const": "SUM",
                    "description": "The total margin requirements per symbol are equal to the sum of all margin requirements of all positions opened for this symbol"
                },
                {
                    "const": "NET",
                    "description": "The total margin requirements per symbol are equal to the difference between the margin requirements for all long positions and all short positions opened for this symbol."
                }
            ]
        },
        "maxLeverage": {
            "description": "The maximum amount of leverage (in the base currency units) available to the account",
            "type": "integer",
            "examples": [
                10000
            ]
        },
        "isLimitedRisk": {
            "description": "The trader’s limited risk (LR) status",
            "type": "boolean"
        },
        "limitedRiskMarginCalculationStrategy": {
            "description": "The margin calculation strategy used for a limited risk account",
            "type": "enum",
            "oneOf": [
                {
                    "const": "ACCORDING_TO_LEVERAGE",
                    "description": "Margin requirements have to be calculated based on the account leverage"
                },
                {
                    "const": "ACCORDING_TO_GSL",
                    "description": "Margin requirements have to be calculated based on the distance between the position open price and the guaranteed stop loss"
                },
                {
                    "const": "ACCORDING_TO_GSL_AND_LEVERAGE",
                    "description": "cServer calculates the leverage-based and GSL-based margin requirements, and chooses the larger of the two values"
                }
            ]
        },
        "sendStatementToBroker": {
            "description": " A flag determining whether a daily account trading statement is sent to the broker",
            "type": "boolean",
            "examples": [
                false
            ]
        },
        "registrationTimestamp": {
            "description": " A timestamp with the date and time of account registration",
            "type": "long",
            "examples": [
                1680087970
            ]
        },
        "lastUpdateTimeStamp": {
            "description": "A timestamp with the date and time of the last account update",
            "type": "long",
            "examples": [
                1680087970
            ]
        },
        "lastConnectionTimestamp": {
            "description": "A timestamp with the date and time of the last connection to cTrader by the account",
            "type": "long",
            "examples": [
                1680087970
            ]
        }
    },
    "required": [
        "login", "groupName", "depositCurrency", "accessRights", "balance", "bonus", "nonWithdrawableBonus", "leverageInCents", "contactDetails", "registrationTimestamp", "lastUpdateTimestamp", "equity", "usedMargin", "freeMargin", "accountType"
    ]
}

```


## ¶ 7.2. Trader Group


```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Group",
    "description": "The entity that aggregates traders based on custom criteria",
    "type": "object",
    "properties": {
        "id": {
            "description": "The identifier of an account group",
            "type": "long",
            "examples": [
                51350
            ]
        },
        "name": {
            "description": "The name of an account group",
            "type": "string",
            "examples": [
                "Default Group"
            ]
        },
        "description": {
            "description": "The description of an account group",
            "type": "string",
            "examples": [
                "Default group for new traders"
            ]
        }
    },
  	"required": ["id", "name"]
}

```


## ¶ 7.3. cTID (User)


```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "User",
    "description": "The entity responsible for user authorization",
    "type": "object",
    "properties": {
        "userId": {
            "description": "The unique identifier of a user entity",
            "type": "string",
            "examples": [
                10333,
            ]
        },
        "nickname": {
            "description": "The nickname of a user entity",
            "type": "string",
            "examples": [
                "ctid10333"
            ]
        },
        "email": {
            "description": "The email assigned to the user entity",
            "type": "string",
            "examples": [
                "president@bestbroker.com"
            ]
        },
        "utcCreateTimestamp": {
            "description": "The epoch unix timestamp of the creation of the user entity",
            "type": "long",
            "examples": [
                1679898064783
            ]
        },
        "preferredLanguage": {
            "description": "An Alpha-2 code denoting the preferred language of the user entity",
            "type": "string",
            "examples": [
                "en"
            ]
        },
        "status": {
            "description": "The status of the user entity",
            "type": "enum",
            "oneOf": [
                {
                    "const": "CTID_NEW",
                    "description": "The default status for any new user"
                },
                {
                    "const": "CTID_ACTIVE",
                    "description": "The status denoting an existing active user"
                },
                {
                    "const": "CTID_DELETED",
                    "description": "The status denoting a deleted user entity"
                }
            ]
        },
    },
    "required": ["userId", "email", "nickname"]
}

```


## ¶ 7.4. Symbol


```json
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Symbol",
    "description": "The entity for which orders are placed, deals are executed, and positions are opened/closed",
    "type": "object",
    "properties": {
      	"name": {
          	"description": "The name of a symbol",
          	"type": "string",
           	"examples": [
              	"EURUSD",
              	"GBPJPY",
            ]
        },
        "id": {
            "description": "The identifier of a symbol",
            "type": "integer",
            "examples": [
                34,
      					98,
            ]
        },
        "description": {
            "description": "The description of a symbol",
            "type": "string",
            "examples": [
                "EUR to USD",
              	"GBP to JPY",
            ]
        },
        "assetClass": {
          	"description": "The name of the asset class to which a symbol belongs to",
          	"type": "string",
          	"examples": [
              	"Forex",
              	"Commodities",
            ]
        },
        "category": {
        		"description": "The name of the symbol category to which a symbol belongs to",
          	"type": "string",
          	"examples": [
            		"Majors",
              	"Metals",
            ]
        },
        "quotesEnabled": {
        		"description": "The flag that determines whether a symbol is currently receiving quotes",
          	"type": "boolean",
          	"examples": [
            		true,
              	false,
            ]
        },
        "showInCtrader": {
        		"description": "The flag that determines whether a symbol is currently shown in cTrader applications",
          	"type": "boolean",
          	"examples": [
              	true,
              	false,
            ]
        }
    },
    "required": ["name", "id", "assetClass", "category", "quotesEnabled", "showInCtrader"]
}

```

---

## Page: Error Codes
*Source: https://docs.spotware.com/en/WebServices_API/Error_Codes*

# ¶ 9. Error Codes and Descriptions


This section defines the error codes you may encounter when working with the WebServices API.


The table below defines the error codes that you may encounter when making any of the API calls described in [**Section 4**](/WebServices_API/Operations_With_Accounts) and [**Section 5**](/WebServices_API/Operations_With_cTID).

| Code | Definition |
| --- | --- |
| `UNKNOWN_ERROR` | An unknown server error has occured. |
| `INVALID_REQUEST` | A request validation failure has occured. The possible error descriptions are as following. |
| `NOT_ENOUGH_RIGHTS` | The manager who has made the request does not have sufficient rights to perform the requested operation. |
| `CH_BROKER_NOT_FOUND` | The cTrader backend cannot find the broker that the request concerns. |


The following table defines the error codes that can only be encountered when making certain calls described in [**Section 4**](/WebServices_API/Operations_With_Accounts) and [**Section 5**](/WebServices_API/Operations_With_cTID).

| Code | API Call(s) | Definition |
| --- | --- | --- |
| `REQUEST_FREQUENCY_EXCEEDED` | Any call with a non-`GET` method. | The client has exceeded the request rate limiter (only applies to non-`GET` requests). |
| `TRADER_NOT_FOUND` | Any API call with the `login` parameter and/or the `traderLogin`/`INVALID_REQUEST`0 keys in the request body. | The requested trader is not found. |
| `INVALID_REQUEST`1 | Any API calls with the `INVALID_REQUEST`2 key in the request body. | The cTrader backend cannot find a broker with `INVALID_REQUEST`3 at the plant to which the request is made. |


## ¶ 9.1. Error Codes for Operations With Accounts


The following errors can only be encountered when making certain API call(s) described in [**Section 4**](/WebServices_API/Operations_With_Accounts).


[https://wiki-public.devzone.kube.spotwa.re/WebServices_API/Operations_With_Accounts#h-47-change-a-traders-balance](/WebServices_API/Operations_With_Accounts#h-47-change-a-traders-balance)

| Code | API Call(s) | Definition |
| --- | --- | --- |
| `INVALID_REQUEST`4 | API calls 4.7 and 4.13. | A trader does not have sufficient funds to perform the requested operation or has open positions generating unrealized PnL. |
| `INVALID_REQUEST`5 | API call 4.7 | The requested balance change amount is invalid (e.g., if it is less than zero). |
| `INVALID_REQUEST`6 | API call 4.3 | The requested trader group is not found. |
| `INVALID_REQUEST`7 | API call 4.9 | The password submitted in the request body is incorrect. |


## ¶ 9.2. Error Codes for Operations With cTID


You may encounter the following error codes when making certain API calls described in [**Section 5**](/WebServices_API/Operations_With_cTID).

| Code | API Call(s) | Definition |
| --- | --- | --- |
| `INVALID_REQUEST`8 | API call 5.1 | The plant to which the request is made is lacking a default region in its configuration. |
| `INVALID_REQUEST`9 | API call 5.1 | The value of the `NOT_ENOUGH_RIGHTS`0 |
| `NOT_ENOUGH_RIGHTS`1 | API call 5.2 | The environment with the specified `NOT_ENOUGH_RIGHTS`2 is not found. |
| `NOT_ENOUGH_RIGHTS`3 | API call 5.2 | The broker with the specified `NOT_ENOUGH_RIGHTS`4 does not have access to the trader with the specified `NOT_ENOUGH_RIGHTS`5. |
| `NOT_ENOUGH_RIGHTS`6 | API call 5.2 | The trader with the specified `NOT_ENOUGH_RIGHTS`7 has already been linked. |
| `NOT_ENOUGH_RIGHTS`8 | API calls 5.2 and 5.3 | The trader with the specified `NOT_ENOUGH_RIGHTS`9 is not found. |
| `CH_BROKER_NOT_FOUND`0 | API call 5.3 | The trader with the specified `CH_BROKER_NOT_FOUND`1 is not found. |

---

## Page: Country List
*Source: https://docs.spotware.com/WebServices_API/Country_List*

# ¶ 11. Country List


The following table provides the list of all countries, `countryId`s, and related Alpha-2 codes that are part of the WebServices API.


To download the table as a JSON file, [**click here**](/webservices-api/countrylistnew.json).

> You can set the `contactDetails.countryId` parameter in any operation related to creating or updating traders.

| Country Name | Alpha-2 | `country_id` |
| --- | --- | --- |
| Afghanistan | AF | 4 |
| Albania | AL | 8 |
| Antarctica | AQ | 10 |
| Algeria | DZ | 12 |
| American Samoa | AS | 16 |
| Andorra | AD | 20 |
| Angola | AO | 24 |
| Antigua and Barbuda | AG | 28 |
| Azerbaijan | AZ | 31 |
| Argentina | AR | 32 |
| Australia | AU | 36 |
| Austria | AT | 40 |
| Bahamas (the) | BS | 44 |
| Bahrain | BH | 48 |
| Bangladesh | BD | 50 |
| Armenia | AM | 51 |
| Barbados | BB | 52 |
| Belgium | BE | 56 |
| Bermuda | BM | 60 |
| Bhutan | BT | 64 |
| Bolivia (Plurinational State of) | BO | 68 |
| Bosnia and Herzegovina | BA | 70 |
| Botswana | BW | 72 |
| Bouvet Island | BV | 74 |
| Brazil | BR | 76 |
| Belize | BZ | 84 |
| British Indian Ocean Territory (the) | IO | 86 |
| Solomon Islands | SB | 90 |
| Virgin Islands (British) | VG | 92 |
| Brunei Darussalam | BN | 96 |
| Bulgaria | BG | 100 |
| Myanmar | MM | 104 |
| Burundi | BI | 108 |
| Belarus | BY | 112 |
| Cambodia | KH | 116 |
| Cameroon | CM | 120 |
| Canada | CA | 124 |
| Cabo Verde | CV | 132 |
| Cayman Islands (the) | KY | 136 |
| Central African Republic (the) | CF | 140 |
| Sri Lanka | LK | 144 |
| Chad | TD | 148 |
| Chile | CL | 152 |
| China | CN | 156 |
| Taiwan (Province of China) | TW | 158 |
| Christmas Island | CX | 162 |
| Cocos (Keeling) Islands (the) | CC | 166 |
| Colombia | CO | 170 |
| Comoros (the) | KM | 174 |
| Mayotte | YT | 175 |
| Congo (the) | CG | 178 |
| Congo (the Democratic Republic of the) | CD | 180 |
| Cook Islands (the) | CK | 184 |
| Costa Rica | CR | 188 |
| Croatia | HR | 191 |
| Cuba | CU | 192 |
| Cyprus | CY | 196 |
| Czechia | CZ | 203 |
| Benin | BJ | 204 |
| Denmark | DK | 208 |
| Dominica | DM | 212 |
| Dominican Republic (the) | DO | 214 |
| Ecuador | EC | 218 |
| El Salvador | SV | 222 |
| Equatorial Guinea | GQ | 226 |
| Ethiopia | ET | 231 |
| Eritrea | ER | 232 |
| Estonia | EE | 233 |
| Faroe Islands (the) | FO | 234 |
| Falkland Islands (the) [Malvinas] | FK | 238 |
| South Georgia and the South Sandwich Islands | GS | 239 |
| Fiji | FJ | 242 |
| Finland | FI | 246 |
| Åland Islands | AX | 248 |
| France | FR | 250 |
| French Guiana | GF | 254 |
| French Polynesia | PF | 258 |
| French Southern Territories (the) | TF | 260 |
| Djibouti | DJ | 262 |
| Gabon | GA | 266 |
| Georgia | GE | 268 |
| Gambia (the) | GM | 270 |
| Palestine | PS | 275 |
| Germany | DE | 276 |
| Ghana | GH | 288 |
| Gibraltar | GI | 292 |
| Kiribati | KI | 296 |
| Greece | GR | 300 |
| Greenland | GL | 304 |
| Grenada | GD | 308 |
| Guadeloupe | GP | 312 |
| Guam | GU | 316 |
| Guatemala | GT | 320 |
| Guinea | GN | 324 |
| Guyana | GY | 328 |
| Haiti | HT | 332 |
| Heard Island and McDonald Islands | HM | 334 |
| Holy See (the) | VA | 336 |
| Honduras | HN | 340 |
| Hong Kong | HK | 344 |
| Hungary | HU | 348 |
| Iceland | IS | 352 |
| India | IN | 356 |
| Indonesia | ID | 360 |
| Iran (Islamic Republic of) | IR | 364 |
| Iraq | IQ | 368 |
| Ireland | IE | 372 |
| Israel | IL | 376 |
| Italy | IT | 380 |
| Côte d’Ivoire | CI | 384 |
| Jamaica | JM | 388 |
| Japan | JP | 392 |
| Kazakhstan | KZ | 398 |
| Jordan | JO | 400 |
| Kenya | KE | 404 |
| Korea (the Democratic People’s Republic of) | KP | 408 |
| Korea (the Republic of) | KR | 410 |
| Kuwait | KW | 414 |
| Kyrgyzstan | KG | 417 |
| Lao People’s Democratic Republic (the) | LA | 418 |
| Lebanon | LB | 422 |
| Lesotho | LS | 426 |
| Latvia | LV | 428 |
| Liberia | LR | 430 |
| Libya | LY | 434 |
| Liechtenstein | LI | 438 |
| Lithuania | LT | 440 |
| Luxembourg | LU | 442 |
| Macao | MO | 446 |
| Madagascar | MG | 450 |
| Malawi | MW | 454 |
| Malaysia | MY | 458 |
| Maldives | MV | 462 |
| Mali | ML | 466 |
| Malta | MT | 470 |
| Martinique | MQ | 474 |
| Mauritania | MR | 478 |
| Mauritius | MU | 480 |
| Mexico | MX | 484 |
| Monaco | MC | 492 |
| Mongolia | MN | 496 |
| Moldova (the Republic of) | MD | 498 |
| Montenegro | ME | 499 |
| Montserrat | MS | 500 |
| Morocco | MA | 504 |
| Mozambique | MZ | 508 |
| Oman | OM | 512 |
| Namibia | NA | 516 |
| Nauru | NR | 520 |
| Nepal | NP | 524 |
| Netherlands (Kingdom of the) | NL | 528 |
| Curaçao | CW | 531 |
| Aruba | AW | 533 |
| Sint Maarten (Dutch part) | SX | 534 |
| Bonaire | BQ | 535 |
| New Caledonia | NC | 540 |
| Vanuatu | VU | 548 |
| New Zealand | NZ | 554 |
| Nicaragua | NI | 558 |
| Niger (the) | NE | 562 |
| Nigeria | NG | 566 |
| Niue | NU | 570 |
| Norfolk Island | NF | 574 |
| Norway | NO | 578 |
| Northern Mariana Islands (the) | MP | 580 |
| United States Minor Outlying Islands (the) | UM | 581 |
| Micronesia (Federated States of) | FM | 583 |
| Marshall Islands (the) | MH | 584 |
| Palau | PW | 585 |
| Pakistan | PK | 586 |
| Panama | PA | 591 |
| Papua New Guinea | PG | 598 |
| Paraguay | PY | 600 |
| Peru | PE | 604 |
| Philippines (the) | PH | 608 |
| Pitcairn | PN | 612 |
| Poland | PL | 616 |
| Portugal | PT | 620 |
| Guinea-Bissau | GW | 624 |
| Timor-Leste | TL | 626 |
| Puerto Rico | PR | 630 |
| Qatar | QA | 634 |
| Réunion | RE | 638 |
| Romania | RO | 642 |
| Russian Federation (the) | RU | 643 |
| Rwanda | RW | 646 |
| Saint Barthélemy | BL | 652 |
| Saint Helena | SH | 654 |
| Saint Kitts and Nevis | KN | 659 |
| Anguilla | AI | 660 |
| Saint Lucia | LC | 662 |
| Saint Martin (French part) | MF | 663 |
| Saint Pierre and Miquelon | PM | 666 |
| Saint Vincent and the Grenadines | VC | 670 |
| San Marino | SM | 674 |
| Sao Tome and Principe | ST | 678 |
| Saudi Arabia | SA | 682 |
| Senegal | SN | 686 |
| Serbia | RS | 688 |
| Seychelles | SC | 690 |
| Sierra Leone | SL | 694 |
| Singapore | SG | 702 |
| Slovakia | SK | 703 |
| Viet Nam | VN | 704 |
| Slovenia | SI | 705 |
| Somalia | SO | 706 |
| South Africa | ZA | 710 |
| Zimbabwe | ZW | 716 |
| Spain | ES | 724 |
| South Sudan | SS | 728 |
| Sudan (the) | SD | 729 |
| Western Sahara* | EH | 732 |
| Suriname | SR | 740 |
| Svalbard and Jan Mayen | SJ | 744 |
| Eswatini | SZ | 748 |
| Sweden | SE | 752 |
| Switzerland | CH | 756 |
| Syrian Arab Republic (the) | SY | 760 |
| Tajikistan | TJ | 762 |
| Thailand | TH | 764 |
| Togo | TG | 768 |
| Tokelau | TK | 772 |
| Tonga | TO | 776 |
| Trinidad and Tobago | TT | 780 |
| United Arab Emirates (the) | AE | 784 |
| Tunisia | TN | 788 |
| Türkiye | TR | 792 |
| Turkmenistan | TM | 795 |
| Turks and Caicos Islands (the) | TC | 796 |
| Tuvalu | TV | 798 |
| Uganda | UG | 800 |
| Ukraine | UA | 804 |
| North Macedonia | MK | 807 |
| Egypt | EG | 818 |
| United Kingdom of Great Britain and Northern Ireland (the) | GB | 826 |
| Guernsey | GG | 831 |
| Jersey | JE | 832 |
| Isle of Man | IM | 833 |
| Tanzania | TZ | 834 |
| United States of America (the) | US | 840 |
| Virgin Islands (U.S.) | VI | 850 |
| Burkina Faso | BF | 854 |
| Uruguay | UY | 858 |
| Uzbekistan | UZ | 860 |
| Venezuela (Bolivarian Republic of) | VE | 862 |
| Wallis and Futuna | WF | 876 |
| Samoa | WS | 882 |
| Yemen | YE | 887 |
| Zambia | ZM | 894 |

---

## Page: General Provisions
*Source: https://docs.spotware.com/en/WebServices_API/General_Provisions*

# ¶ 3. General Provisions

> The WebServices API is only available when calls are sent from whitelisted IP addresses, the list of which is created by Spotware’s service assurance team during the onboarding process.


## ¶ 3.1. Authentication Provisions


The WebServices API is authenticated under the same manager credentials that are used to log into the cBroker application.


The usage of the API requires the inclusion of an authentication token with each request by appending `?token={token}` to the end of each request URL. To generate the authentication token, use the following API call. Its URL is relative to `https://HOST:PORT/v2`, the value of `HOST:PORT` is provided by Spotware’s service assurance team as part of the onboarding process.

| HTTP Method | URL |
| --- | --- |
| `POST` | `/webserv/managers/token` |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `login` | Yes | integer | Your cBroker manager login. |
| `hashedPassword` | Yes | string | The MD5 of your cBroker manager password. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `webservToken` | An authentication token for the WebServices API. |  |


**Request Example**


```curl
curl -X POST "https://HOST:PORT/v2/webserv/managers/token" -H "accept: application/json" -H "Content-Type: application/json" -d '{"hashedPassword": "0f94e246908667af85916300c57f74b6", "login": 9017800}'

```

**Response Example**


```json
{
    "webservToken": "1dd4ef40-c5b3-61c0-0689-b1b40c97fadc"
}

```

> Note that a manager’s token does not have an expiration time. However, it may become invalidated in certain cases, most notably when a manager’s password is changed. In these cases, a new token must be requested from the same endpoint. As long as the `hashedPassword` parameter is different in the request body, you should receive a new token.

**Expected Status Code**


`200`


## ¶ 3.2. Manager Permissions


Note that some actions may be impossible to perform via the Web Services API depending on your managerial permissions.


Manager permissions are separated by account groups as well as on a per-broker basis via the `https://HOST:PORT/v2`0 parameter. To have access to a specific account or a related server entity (e.g., an order object that was originated by this account), a manager needs to have access to the group to which the account is assigned as well as the `https://HOST:PORT/v2`1 under which the account is registered.

> Each manager also has the `https://HOST:PORT/v2`2 array listing all `https://HOST:PORT/v2`3 to which this manager does not have access. For a manager to have access to an account and related entities, the corresponding `https://HOST:PORT/v2`4 must not be included in the `https://HOST:PORT/v2`5 array of said manager.


## ¶ 3.3.  Denominations of Finance-Related Parameters


When integrating with the Web Services API using this technical documentation, note the following.


- The value of the `https://HOST:PORT/v2`6 parameter is always defined in 10^2 of base asset units. E.g., `https://HOST:PORT/v2`7 equals to 2345.12 of base asset units.

- The values of all parameters related to finance (account balance, commissions, etc.) are always defined in 10^`https://HOST:PORT/v2`8, where `https://HOST:PORT/v2`9 is a separate customizable parameters. E.g., if `HOST:PORT`0 and `HOST:PORT`1, the account balance is 2345.12 deposit currency units.

- Spotware reserves the right to implement request limiters for all new `HOST:PORT`2/`HOST:PORT`3/`HOST:PORT`4 requests in case abnormal API usage is detected. Request limiters do not apply to `HOST:PORT`5 requests.


## ¶ 3.4. Broker-Specific Parameters


There are several request body parameters the values of which are broker-specific and, as such, are provided by Spotware’s service assurance team as part of the onboarding process.

| Parameter | Data Type | Description |
| --- | --- | --- |
| `HOST:PORT`6 | string | A unique name denoting a specific broker (including White Labels). |
| `HOST:PORT`7 | string | A unique name of a specific trading environment. |


## ¶ 3.5. Content Types


All API callls made as part of the WebService API accept both XML and JSON content types for request bodies and responses.

---

## Page: Operations With Symbols and Assets
*Source: https://docs.spotware.com/en/WebServices_API/Operations_With_Assets_Symbols*

# ¶ 6. Operations With Symbols and Assets


All API calls in this section concern operations with assets and symbols.


All URLs for the API calls described below are relative to `https://HOST:PORT/v2`. The value of `HOST:PORT` is provided during the onboarding process by Spotware’s service assurance team.


## ¶ 6.1. Request a List of Symbols

| HTTP Method | URL |
| --- | --- |
| `GET` | `/webserv/symbols` |


Gets the list of all available symbols on the server.


**Parameters**


No parameters.


**Request Body**


No request body.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `symbol` | array | An array of symbol objects; click here to see the JSON schema of a symbol. |
| `symbol.name` | string | The name of a symbol. |
| `symbol.id` | integer | The ID of a symbol. |
| `symbol.description` | string | A custom string describing a symbol. |
| `symbol.assetClass` | string | The name of the asset class to which a symbol belongs to. |
| `symbol.category` | string | The name of the symbol category to which a symbol belongs to. |
| `HOST:PORT`0 | boolean | The flag that determines whether a symbol is currently receiving quotes. |
| `HOST:PORT`1 | boolean | The flag that determines whether a symbol is currently shown in cTrader applications. |


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/symbols?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```

**Response Example**


```json
{
  "symbol":[
    {
      "name":"EURUSD",
      "id":1,
      "description":"EUR to USD",
      "assetClass":"forex",
      "category":"majors",
      "quotesEnabled":true,
      "showInCtrader":false
    },
    {
      "name":"BTCUSD",
      "id":2,
      "description": "BTC to USD",
      "assetClass":"crypto",
      "category":"majors",
      "quotesEnabled":true,
      "showInCtrader":true
    },
    {
      "name":"XAUUSD",
      "id":3,
      "description":"Gold",
      "assetClass":"commodities",
      "category":"metals",
      "quotesEnabled":false,
      "showInCtrader":false
    },
  ]
}

```

**Expected Status Code**


`HOST:PORT`2


## ¶ 6.2. Request a List of Deposit Assets

| HTTP Method | URL |
| --- | --- |
| `HOST:PORT`3 | `HOST:PORT`4 |


Gets the list of all assets available as account deposit assets.


**Parameters**


No parameters.


**Request Body**


No request body.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `HOST:PORT`5 | array | An array containing the names of all available deposit assets. |


**Request Example**


```curl
curl -X GET "https://HOST:PORT/v2/webserv/depositAssets?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```

**Response Example**


```json
{
    "depositAsset":[
    	"EUR",
    	"USD",
    	"GBP"
  ]
}

```

**Expected Status Code**


`HOST:PORT`6

---

## Page: Use Cases
*Source: https://docs.spotware.com/en/WebServices_API/Use_Cases*

# ¶ 8. Use Cases


This section describes the most common use cases for the Web Services API. It also lists the API calls needed to perform specific actions as well as the corresponding request/response examples.

> Note that all examples below assume that `moneyDigits=2`.

> All examples below are made to a ‘sandbox’ allowing you to quickly test them provided you append a valid manager’s token.


## ¶ 8.1. Creating a Trader With Minimal Parameters


To create a new trader with the minimum possible number of parameters in the request body, perform the following request ([**API call 4.1**](/WebServices_API/Operations_With_Accounts#h-41-create-a-trader)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```

You will receive the following response.


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```


## ¶ 8.2. Creating a Trader and Changing Their Group

Send the following request to create another trader ([**API call 4.1**](/WebServices_API/Operations_With_Accounts#h-41-create-a-trader)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```

You will receive the following response.


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```

Note that `groupName` is `"Default"`.


Now, send the request to update the trader you have just created ([**API call 4.5.1**](/WebServices_API/Operations_With_Accounts#h-451-update-a-trader-all-parameters)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```

In the request body, we have changed `groupName` to `"DX_452"` while leaving all other parameters unchanged.


After receiving code `204`, send the below request to check whether the trader’s group has changed as requested ([**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details)).


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```

In the response you receive, `groupName` should be equal to `"DX_452"`.


## ¶ 8.3. Creating a Trader and Changing Their Access Rights


You may want to prevent new traders from performing any trading operations inside the platform until they pass a KYC check.


To create a new trader, send the request below ([**API call 4.1**](/WebServices_API/Operations_With_Accounts#h-41-create-a-trader)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```

Note that `accessRights` is `"NO_TRADING"` in the request body.


You will receive a response containing the following parameters.


```json
{
    "accessRights": "NO_TRADING",
    "login": 8035346,
    ...
}

```

After you see that the trader has passed their KYC check in your client area, send the following request ([**API call 4.5.1**](/WebServices_API/Operations_With_Accounts#h-451-update-a-trader-all-parameters)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035346?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```

If you send the request to read the trader’s details ([**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details)), you should see that the `groupName`0 parameter has switched to `groupName`1.


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035346?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc" -H "Accept: application/json"

```

The response to this call should be as follows.


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
0

## ¶ 8.4. Depositing and Withdrawing Funds

To deposit funds to a trader, send the following request ([**API call 4.7**](/WebServices_API/Operations_With_Accounts#h-47-change-a-traders-balance)).


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
1
You will receive the following example response.


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
2
To see the trader’s current balance, perform the below request ([**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details)).


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
3
You will receive a response containing the following parameter.


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
4
To perform a withdrawal, send the following request ([**API call 4.7**](/WebServices_API/Operations_With_Accounts#h-47-change-a-traders-balance)).


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
5
> Note that the value of the `groupName`2 parameter is still positive even though we are performing a withdrawal.

The response should be as follows.


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
6
The trader’s current balance should now accurately represent both the previous deposit and the withdrawal. Again, perform [**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details)).


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
7
The response should account for your latest withdrawal.


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
8

## ¶ 8.5. Depositing and Withdrawing Bonus

To deposit bonus to a trader, send the following request ([**API call 4.10**](/WebServices_API/Operations_With_Accounts#h-410-change-a-traders-bonus)).


```json
{
    "login": 8035344,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "brokerName": "BESTBROKER",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
9
You should receive the following response.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
0
If you then check the trader’s details ([**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details)), you should see your allocated bonus being added to the value of the `groupName`3 parameter.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
1
The response to the call should reflect the trader’s increased bonus.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
2
To withdraw bonus, perform [**API call 4.10**](/WebServices_API/Operations_With_Accounts#h-410-change-a-traders-bonus) with `groupName`4.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
3
> Note that the value of the `groupName`5 parameter is still positive even though we are performing a withdrawal.

The response should be as follows.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
4
To see the current amount of bonus allocated to the trader, perform the below request ([**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
5
The response should account for the recent withdrawal of bonus.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
6

## ¶ 8.6. Attributing a Trader to a Partner

To attribute a new trader to a partner, simply specify the values of the `groupName`6 and/or `groupName`7 keys when creating a new trader ([**API call 4.1**](/WebServices_API/Operations_With_Accounts#h-41-create-a-trader)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
7
Assuming that `groupName`8 in the response, afterward, you can send [**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details) to see that the trader contains information about the specified partners.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
8
In the response, you should see the following information.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
9
To attribute an existing trader to a partner, send specify the values of the `groupName`9 and/or `"Default"`0 keys when updating a trader ([**API call 4.5.1**](/WebServices_API/Operations_With_Accounts#h-451-update-a-trader-all-parameters)).


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
0
Send [**API call 4.1**](/WebServices_API/Operations_With_Accounts#h-41-create-a-trader) again, and you should see the new partners in the response.


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
1

## ¶ 8.7. Creating a User With Minimal Parameters

To quickly create a new user with minimal parameters, perform the following request ([**API call 5.1**](/WebServices_API/Operations_With_cTID#h-51-create-a-ctid)).


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
2
You should receive the following response.


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
3

## ¶ 8.8. Linking a New Account to an Existing cTID

In many cases, your clients could request the creation of additional accounts the deposit currency and/or the White Label of which differs from their original account.


Consider an example of a trader with the following parameters.


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
4
The `"Default"`1 of the user to which this account is linked is `"Default"`2.


To create a new account with different parameters, perform the following request ([**API call 4.1**](/WebServices_API/Operations_With_Accounts#h-41-create-a-trader)).


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
5
You should receive the following response.


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
6
To link the new trader with a specific cTID, make [**API call 5.2**](/WebServices_API/Operations_With_cTID#h-52-link-an-account-to-a-ctid).


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
7
You will receive the following response.


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
8

## ¶ 8.9. Transferring an Account to Another White Label

There may also be cases when you change the structure of one or more existing White Labels (e.g., when rebranding different White Labels that you own). In this situation, you would need to change the White Label(s) of already existing accounts.


To do so for one trader, send the following request [**API call 5.3**](/WebServices_API/Operations_With_cTID#h-53-change-the-white-label-brokerage-of-a-trading-account). In the example below, we are assuming that the trader with `"Default"`3 is attributed to any White Label the `"Default"`4 of which is different from `"Default"`5.


```json
{
    "login": 8035345,
    "groupName": "Default",
    "depositCurrency": "EUR",
    "accessRights": "FULL_ACCESS",
    "balance": 0,
    "bonus": 0,
    "nonWithdrawableBonus": 0,
    "leverageInCents": 10000,
    "contactDetails": {},
    "registrationTimestamp": 1680163530801,
    "lastUpdateTimestamp": 1680163530802,
    "equity": 0,
    "usedMargin": 0,
    "freeMargin": 0,
    "accountType": "HEDGED",
    "limitedRisk": false,
    "sendOwnStatement": false,
    "swapFree": false,
    "totalMarginCalculationType": "MAX",
    "isLimitedRisk": false,
    "moneyDigits": 2,
}

```
9
Note that this API call does not produce any output. To double-check whether the trader has been transferred to another White Label, send the following request ([**API call 4.2**](/WebServices_API/Operations_With_Accounts#h-42-read-a-traders-details)).


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
0
In the response body, you should see the updated `"Default"`6 key.


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
1

## ¶ 8.10. Reading Trader Attributes

You can retrieve the current attribute sets for one or more traders, or page through all visible traders who have at least one attribute. Traders with no attributes are omitted from the response.


**Usage scenario:**

You may want to list all traders in your system who have a custom label, colour code or other metadata. This is useful for generating reports or applying bulk actions based on attribute values. To fetch the attributes for all traders visible to your ACL in pages of 25, send the following request:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
2
You will receive a response similar to the following:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
3
To continue retrieving traders, pass the value of `"Default"`7 from the previous response as `"Default"`8 in your next request. You can also fetch attributes for specific traders by specifying their IDs. For example, to get attributes for trader 101 and trader 102, send:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
4
The response will only include the specified traders if they have attributes:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
5
If no traders remain beyond the requested `"Default"`9, the `groupName`0 array will be empty:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
6

## ¶ 8.11. Creating/Upserting Trader Attributes

You can bulk-insert new attributes or update existing ones for one or multiple traders in a single request.


**Usage scenario:**

You may want to apply or update labels, colour codes or other metadata for several traders at once, for example, marking a trader as `groupName`1 or changing their assigned colour for internal dashboards. To update the attributes for traders 102 and 999, send the following request:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
7
If you are not authorised to modify any of the specified traders, the request will still succeed for the authorised ones and silently omit the unauthorised IDs from the result. For example, if you are authorised to update trader 102 but not trader 999, you will receive:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
8

## ¶ 8.12. Deleting Trader Attributes

You can remove specific attribute names from one or more traders, or delete all attributes for those traders if you provide an empty `groupName`2 array.


**Usage scenario:**

You may want to remove an outdated label or colour code from traders, or completely clear their attributes when resetting account metadata. To delete the `groupName`3 attribute from traders 201 and 202, send the following request:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "FULL_ACCESS", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "DX_452", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
9
If successful, you will receive:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
0
To delete all attributes for traders 201 and 202, provide an empty `groupName`4 array:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
1
You will receive:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
2

## ¶ 8.13. Reading Trader Group Attributes

You can retrieve the current attribute sets for one or more trader groups. Paging is not supported for this request. You must always specify the `groupName`5 you want to read. Groups with no attributes are omitted from the response.


**Usage scenario:**

You may want to check which trader groups have specific tags or colours assigned, for example to display them in an admin dashboard or apply special handling for `groupName`6 groups. To fetch the attributes for trader groups 456 and 457, send the following request:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
3
You will receive a response similar to:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
4

## ¶ 8.14. Updating Trader Group Attributes

You can bulk-insert new attributes or update existing ones for multiple trader groups in a single request.


**Usage scenario:**

You may want to assign or update colours, tags, or other metadata for several trader groups at once, for example, changing a group’s colour code to `groupName`7 while keeping its `groupName`8 tag. To update attributes for trader groups 456 and 999, send the following request:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
5
If you are not authorised to modify any of the specified trader groups, the request will still succeed for the authorised ones and omit unauthorised IDs from the response. For example, if you are authorised to update group 456 but not group 999, you will receive:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
6

## ¶ 8.15. Deleting Trader Group Attributes

You can remove specific attribute names from one or more trader groups, or delete all attributes for those groups if you provide an empty `groupName`9 array.


**Usage scenario:**

You may want to remove a group’s assigned colour code or tag, or clear all metadata when reclassifying the group. To delete the `"DX_452"`0 attribute from trader groups 456 and 457, send the following request:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
7
If successful, you will receive:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
8
To delete all attributes for trader groups 456 and 457, provide an empty `"DX_452"`1 array:


```curl
curl -X GET "https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders/8035345?token=8fe4a3a3-1fa6-c4cf-da0f-9c04ee0307b1" -H  "accept: */*"

```
9
The response will be:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
0

## ¶ 8.16. Reading Manager Attributes

You can retrieve the current attribute sets for one or more managers. A regular manager may only request their own ID, while a super-admin may request any manager IDs. Managers with no attributes are omitted from the response.


**Usage scenario:**

You may want to check a manager’s personal settings, such as their preferred theme or language, for configuration purposes or to synchronise settings across platforms. To fetch attributes for managers 789 and 790, send the following request:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
1
You will receive a response similar to:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
2
If only manager 789 has attributes, the response will contain only that manager:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
3

## ¶ 8.17. Updating Manager Attributes

You can bulk-insert new attributes or update existing ones for one or more managers in a single request. A regular manager may only specify their own `"DX_452"`2, while a super-admin may specify any manager IDs.


**Usage scenario:**

You may want to set or update manager-specific settings, such as their preferred theme or language, across multiple accounts at once. To update the attributes for managers 789 and 790, send the following request:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
4
If you are not authorised to update certain managers, the request will still succeed for authorised IDs and omit the unauthorised ones from the response. For example, if you are authorised to update manager 789 but not manager 790, you will receive:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
5

## ¶ 8.18. Deleting Manager Attributes

You can remove specific attribute names from one or more managers, or delete all attributes for those managers if you provide an empty `"DX_452"`3 array. A regular manager may only delete their own attributes, while a super-admin may delete any manager’s attributes.


**Usage scenario:**

You may want to remove a setting such as the preferred theme for certain managers, or clear all stored preferences before reassigning or deactivating their accounts. To delete the `"DX_452"`4 attribute from managers 789 and 790, send the following request:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
6
If successful, you will receive:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
7
To delete all attributes for managers 789 and 790, provide an empty `"DX_452"`5 array:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
8
The response will be:


```curl
curl -X POST ‘https://demo-chsandbox2.webapi.ctrader.com:8443/v2/webserv/traders?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc’ -H ‘Accept: application/json’ -H ‘Content-Type: application/json’ -d ‘{"accessRights": "NO_TRADING", "accountType": "HEDGED", "balance": "00", "brokerName": "BESTBROKER", "depositCurrency": "EUR", "groupName": "Default", "hashedPassword": "c5678ghf94578ce06iqrs5ag76a62c5ca4", "leverageInCents": 10000}’

```
9

## ¶ 8.19. Updating With `"DX_452"`6 Returns `"DX_452"`7 Error

`"DX_452"`8 requests are only for adding or modifying attributes. Any attempt to delete an attribute by setting its `"DX_452"`9 to `204`0 is invalid and will be rejected. To remove attributes, you must use the relevant `204`1 endpoint.


**Usage scenario:**

If you try to update a trader’s attributes with a `204`2 value instead of using the delete call, the API will return an error. For example, the following request tries to remove `204`3 by setting its value to `204`4:


```json
{
    "accessRights": "NO_TRADING",
    "login": 8035346,
    ...
}

```
0

---
