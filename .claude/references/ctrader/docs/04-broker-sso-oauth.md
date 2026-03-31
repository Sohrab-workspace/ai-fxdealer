# Broker SSO (OAuth) — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/en/Broker_SSO_OAuth
>   - https://docs.spotware.com/Broker_SSO_OAuth/Introduction
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/Introduction
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/General_Provisions_Requirements
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/Flows_Stages
>   - https://docs.spotware.com/Broker_SSO_OAuth/Flows_Stages/Embedded_Web_Flow
>   - https://docs.spotware.com/Broker_SSO_OAuth/Flows_Stages/User_Creation_Flow
>   - https://docs.spotware.com/Broker_SSO_OAuth/API_Calling_Backend
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/API_Calling_Backend
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/API_Calling_CRM
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/Conformance_Testing
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/Glossary
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/Getting_Started
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/Concluding_Remarks
>   - https://docs.spotware.com/en/Broker_SSO_OAuth/Additional_Error_Codes

---

## Page: Broker SSO (OAuth)
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth*

# ¶ Broker SSO (OAuth)


This documentation covers Spotware's broker SSO (OAuth) solution. It includes the following sections.


  - Glossary. The definitions of the key terms used in the documentation.

  - 1. Introduction to broker SSO (OAuth). A brief description of the SSO (OAuth) solution and how it works.

  - 2. General provisions and requirements. A list of general provisions for deployment.

  - 3. API calls for calling the cTrader backend. The descriptions of the API calls your CRM system would need to make to the cTrader backend as part of SSO (OAuth) flows.

  - 4. API calls for token verification and exchange. The descriptions of the API calls that the cTrader backend would need to make to your CRM system as part of SSO (OAuth) flows.

  - 5. User flows and their stages. Detailed definitions of Spotware's broker SSO (OAuth) flows.

  - 6. Getting started with deployment. A list of actions you would need to do to proceed with deploying broker SSO (OAuth) flows.

  - 7. Concluding remarks. Brief summary of the SSO (OAuth) solution and future plans for its development.

  - Appendix. Supplementary materials for deploying the SSO (OAuth) flows.

---

## Page: Introduction to Broker SSO (OAuth)
*Source: https://docs.spotware.com/Broker_SSO_OAuth/Introduction*

# ¶ 1. Introduction


## ¶ 1.1. Purpose of the Documentation


This documentation defines the API calls made when working with Spotware’s broker SSO (OAuth) flows and InApp controls. The documentation also contains essential provisions for integration including conformance tests and process diagrams.

> Note that the SSO (OAuth) solution is a paid add-on. It is not provided by default as part of the onboarding package. To proceed with integration and access additional information, contact Spotware’s account management team.

> The SSO API is not a replacement for the WebServices API, and vice versa. Instead, the SSO API is complementary to all other APIs offered by Spotware. You do not lose access to the functionalities of the WebServices API by integrating with the SSO API.


## ¶ 1.2. Brief Description of the Solutions


Spotware’s SSO (OAuth) flows establish a single access point for all actions related to user creation and authorisation inside the trading terminal and a broker’s client area/CRM. InApp controls allow users to perform certain actions (e.g., passing KYC) directly inside cTrader when previously these actions could only be completed in brokers’ client areas.


This is achieved via exposing several endpoints in the cTrader backend and requiring brokers to expose other endpoints inside their client area/CRM. Using a simple REST API, you can ensure that your traders can access your client area/CRM directly from the trading terminal, eliminating the need for needlesly complex UX. The deployment of SSO (OAuth) and InApp controls is highly recommended for any broker wishing to provide superior UX and boost lead-to-trader conversion by widening the typical onboarding funnel.

> Even though this documentation discusses SSO (OAuth) and InApp flows separately, InApp controls are included in the broker SSO (OAuth) package. Deploying SSO (OAuth) flow also means deploying InApp controls and vice versa.

> The SSO (OAuth) flow gives traders the opportunity to perform deposits/withdrawals inside the platform. Note this is done by displaying an interactive deposit/withdrawal screen entirely hosted inside your client area. cTrader itself is not a payment processor; all deposit/withdrawal requests and resolutions would need to be handled by your usual service provider.


For a detailed look at broker SSO (OAuth), you can [**consult this video**](https://www.youtube.com/watch?v=PWud8-Nbf6Y).


## ¶ 1.3. Structure of the Documentation


- Section 2 includes the general provisions and rules for working with the broker SSO (OAuth) web API covered in this document.

- Sections 3 and 4 describe the API calls made as part of Spotware’s SSO (OAuth) flows.

- Section 5 contains process diagrams summarising the main SSO (OAuth) flows.

- Section 6 details the conformance tests you need to pass as part of deployment of the SSO (OAuth) solution and its continuous integration.

- Section 7 outlines the initial actions you need to make when deploying the SSO (OAuth) solution.

- Section 8 contains concluding remarks and the possible directions for the future development of the SSO (OAuth) flows and InApp controls.

- Section 9 includes a list of the custom error codes you may receive when working with our SSO (OAuth) flows.

---

## Page: General Provisions
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/General_Provisions_Requirements*

# ¶ 2. General Provisions


## ¶ 2.1. Key Rules


The API calls covered in this document follow these rules.


- By using Spotware’s API, you automatically agree to the company’s terms of service.

- All requests must be made to secure endpoints using the `https` protocol instead of `http`.

- API calls 3.1-3.11 are made by the cTrader backend to your client area/CRM. API calls 4.1.-4.4. are made by a broker’s CRM system to the cTrader backend.

- The content types accepted by the API calls defined in Section 3 differ according to the below table.


| Endpoint Starting With | Accepted Content Types |
| --- | --- |
| `/ctid/` or `/oauth2/` | Text/JSON only |
| `/webserv/` | Text/JSON and text/XML |


- The endpoints in Section 3 are relative to the following URLs. The unique value of `https://HOST:PORT` is provided by Spotware Systems to each individual broker.


| Endpoint Starting With | Relative To |
| --- | --- |
| `/ctid/` or `/oauth2/` | `https://HOST:PORT/cid` |
| `/webserv/` | `http`0 |


- All API calls received by your client area/CRM (see their list here) must be available at endpoints relative to one consistent URL. Avoid establishing some endpoints at `http`1 while hosting others at `http`2. To avoid confusion, these endpoints are referenced as `http`3. Additional information about this URL is provided in this tutorial.

- Several fields related to finances (`http`4, `http`5, `http`6, `http`7, `http`8, and `http`9) list their respective values in 10^`/ctid/`0, where `/ctid/`1 is a separate JSON key taking integer values. An equity of 234512 with a `/ctid/`2 value of 2 would equal 2345.12 currency units.

- If the number of requests per hour exceeds a certain threshold, all new `/ctid/`3/`/ctid/`4/`/ctid/`5 requests will be rejected. There are no rate limits for `/ctid/`6 requests.


## ¶ 2.2. Authentication Provisions


The broker’s backend is authenticated under the same manager’s credentials used to login into the cBroker backend application. For the API calls made by the broker’s backend office to the cTrader backend, append an authentication token to each request by placing `/ctid/`7 at the end of each request URL. Additional details about the manager authentication token can be [**found here**](/Broker_SSO_OAuth/API_Calling_Backend/).


The SSO (OAuth) REST API also requires the cTrader backend to be authenticated when making requests to your client area. As specified in [**API call 4.1.**](/Broker_SSO_OAuth/API_Calling_CRM/), the cTrader backend exchanges a pre-generated password to acquire a long-term authentication token that must be valid for at least one week. This token is added to each request made by the cTrader back office by appending `/ctid/`8 to each request URL.


## ¶ 2.3. Broker-Specific Parameters Provided by Spotware


The API calls defined in [**Section 3**](/Broker_SSO_OAuth/API_Calling_Backend/) take several request body keys and/or query parameters the values of which are provided by Spotware Systems on a per-broker basis. These keys are summarised in the following table.

| Parameter | Data Type | Description |
| --- | --- | --- |
| `/ctid/`9 | string | A unique name designating a broker’s CRM system. If several brokers share the same CRM system, they will also have the same `/oauth2/`0 value. |
| `/oauth2/`1 | string | A unique name denoting a specific broker (including White Labels). |


## ¶ 2.4. Firebase Integration


Spotware’s API also supports Firebase integration. You can use this functionality when both conditions below are true.


- The user accesses an SSO (OAuth) screen using cTrader Mobile.

- Sending Firebase analytics is enabled. To enable this option, contact Spotware’s Service Assurance team.


To send events to Firebase, the API supports the `/oauth2/`2 query parameter.

| Parameter | Data Type | Description |
| --- | --- | --- |
| `/oauth2/`3 | string | The name of the event to be sent to Firebase. |


You can add this parameter to the URLs that host various SSO (OAuth) screens. When a user is transferred from one URL to another during an SSO (OAuth) flow (e.g., when completing the first stage of the account registration process and being sent to the second stage) and `/oauth2/`4 is specified in the screen URL, the event is sent to Firebase under the specified name.


As a result, you can attain detailed statistics about how and when users are redirected as part of broker SSO (OAuth) flows. This functionality facilitates tracking users’ progression along the onboarding funnel.

> You can use `/oauth2/`5 to track how many traders who have opened an account with your brokerage choose to start passing your KYC checks as well as how many traders are lost at each distinct stage of your KYC process (if these stages have custom screens shown on different URLs).


## ¶ 2.5. SSO (OAuth) Screens and InApp Controls Examples


The SSO (OAuth) flows require you to create and host various screens inside your client area. Below, we provide examples of how these screens may look like depending on their type. We also provide an example of an InApp control (a ribbon).


### ¶ Login/Signup Screens

- Web Example One
- Mobile Example One
- Web Example Two
- Mobile Example Two
- Web Example Three
- Mobile Example Three

---

## Page: URLs and User Flows
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/Flows_Stages*

# ¶ 5. URLs and User Flows


## ¶ 5.1. Key Rules


Section 5 outlines the key SSO (OAuth) and InApp flows. Along with a process diagram, each flow is provided with a detailed description of its stages. When applicable, the process diagrams also list the relevant API calls in brackets.


All user flows described in this section are fully compliant with the OAuth 2 standard ([**RFC8252**](https://datatracker.ietf.org/doc/html/rfc8252)) to maximise security and improve UX.


## ¶ 5.2. URLs and Their Parameters


The SSO (OAuth) flows require the existence of a custom user creation/authorisation (login/signup) screen. Additionally, the [**user creation flow (5.3.)**](/Broker_SSO_OAuth/Flows_Stages/User_Creation_Flow) requires a trading account creation screen.


The front-end component of these screens is designed and implemented by the broker. Please note that the screens should be designed replace the default cTrader login/signup (and account creation) pages. The screens must not include any browser-related controls.


When performing various InApp actions, users are also sent to pre-defined URLs relevant to a particular InApp action. For example, clicking on the button for making a deposit should provide users with a custom deposit options screen. Similarly to the above provisions, these screens must be created by brokers and should be consistent with other elements of the UI. However, users must be able to close these screens by clicking on a ‘Back’ button, an ‘X’ button, or something similar.


The URLs hosting your SSO (OAuth) screens can accept several mandatory and optional query parameters.


**Parameters**

| Parameter | Screen(s) | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `lang` | All screens | No | `string` | The language of the device OS. This parameter allows for displaying forms and screens in different languages. The parameter takes Alpha-2 (ISO 369-2) codes as values. |
| `source` | All screens | No | `string` | The type of the application accessing the screen. Applicable values include `"Web"`, `"Android"`, `"iOS"`, `"MacOS"`, and `"Desktop"`. Brokers can also use this parameter to adjust the screen design for various devices. |
| `theme` | All screens | No | `string`0 | The preferred colour scheme of the app (can be either `string`1 or `string`2). This parameter is needed for the broker to establish a consistent design and ensure that the screens appear native to the trading application. |
| `string`3 | Login/signup | No | `string`4 | A flag determining whether this is the user’s first login attempt on the current device. As Spotware only supports a single URL for the login/signup screen, this parameter is needed for the broker’s CRM system to correctly recognise whether it needs to open its user creation page or the login form. The value of `string`5 denotes the user’s first per-device login, and vice versa. |
| `string`6 | Login/signup | No | `string`7 | The email assigned as a partner identifier to a specific user or an account. |
| `string`8 | InApp actions | Yes | `string`9 | The OT token required for authorisation. |
| `source`0 | InApp actions | Yes (only for deposits/withdrawals); No (in other cases) | `source`1 | The number of a specific trading account linked to the user. |


Note that cTrader Mobile also supports UTM parameters as query parameters for all broker SSO (OAuth) screens.

| Parameter | Screen(s) | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `source`2 | All screens | No | `source`3 | The source channel from which the user is transferred to an OAuth screen. |
| `source`4 | All screens | No | `source`5 | The type of content that encouraged the user to click on a link and be transferred to an SSO (OAuth) screen. |
| `source`6 | All screens | No | `source`7 | The name of the marketing campaign as a result of which the user is transferred to an SSO (OAuth) screen. |
| `source`8 | All screens | No | `source`9 | The keyword that the user engages with and, as a result, is transferred to an SSO (OAuth) screen. |
| `string`0 | All screens | No | `string`1 | The Google Click identifier assigned to the user being transferred to an SSO (OAuth) screen. |


## ¶ 5.3. User Creation Flow


This user flow covers actions necessary for first-time user creation. To learn more, [**click here**](/Broker_SSO_OAuth/Flows_Stages/User_Creation_Flow).


## ¶ 5.4. User Authorization With a Password Flow


This flow covers the cases in which a user is already registered in the cTrader backend and in the broker’s CRM system. To learn more, [**click here**](/Broker_SSO_OAuth/Flows_Stages/User_Authorization_Flow).


## ¶ 5.5. Automatic Re-Login Flow


This flow applies to cases in which a user has been previously authorized using the same application and the same device as in their current session; additionally, the ‘Keep Me Logged In’ (or a similarly named) option is selected. To learn more, [**proceed here**](/Broker_SSO_OAuth/Flows_Stages/Automatic_Relogin_Flow).


## ¶ 5.6. Embedded cTrader Web Flow


This flow describes the cases in which users that have registered their first account in the broker’s CRM want to open embedded cTrader Web. To learn more, [**click here**](/Broker_SSO_OAuth/Flows_Stages/Embedded_Web_Flow).


## ¶ 5.7. InApp Actions Flow


This flow outlines the general sequence of event that occur when a user wants to perform an InApp action. To learn more, [**click here**](/Broker_SSO_OAuth/Flows_Stages/InApp_Actions_Flow).


## ¶ 5.8. Trader Attribution Flows


These flows showcase how trader-partner attribution works when our SSO (OAuth) solution is deployed. To learn more, [**click here**](/Broker_SSO_OAuth/Flows_Stages/Trader_Attribution).

---

## Page: Embedded cTrader Web
*Source: https://docs.spotware.com/Broker_SSO_OAuth/Flows_Stages/Embedded_Web_Flow*

# ¶ 5.6. Embedded cTrader Web


This SSO (OAuth) flow only applies to users who, upon being authorized in their broker’s CRM system, want to launch cTrader Web inside this client area or in a separate tab from the broker’s backend. By allowing users to avoid inputting an additional set of credentials before starting trading, this flow eliminates disruptions to UX.


The embedded cTrader web flow incorporates the following stages.


- The user is successfully authorized inside the broker’s CRM system.

- The user clicks to launch the cTrader Web platform while within the confines of the broker’s client area.

- The broker’s backend generates an OT token.

- cTrader Web is opened inside a separate iframe with `token` (the OT token) as a parameter. As an example, cTrader Web can be opened via the following URL: https://app.ctrader.com/info?source=web&token=f44bade2-2138-47c2-89e6-ce978bcca028&lang=en&acc=8003098. To see the full list of valid cTrader Web deeplinks, click here.

- cTrader Web takes the `token` and sends a request to the cTrader backend to authorise the corresponding user.

- The application opens a new connection with the cTrader backend and sends an authorisation request including `token` as a parameter.

- The cTrader backend sends a POST-request via REST API to exchange the OT token for a long-term access token (API call 4.2.).

- The broker’s CRM verifies the token and responds with `userId` and `accessToken` (API call 4.2.).

- The cTrader backend authorizes the session under the provided `userId` and returns the `accessToken` to the application.

- The platform stores the `accessToken` for future usage.

- The application starts authorised communications with the cTrader backend.

---

## Page: User Creation Flow
*Source: https://docs.spotware.com/Broker_SSO_OAuth/Flows_Stages/User_Creation_Flow*

# ¶ 5.3. User Creation Flow


The following figure summarises the SSO (OAuth) user creation flow.


The user creation flows passes through the following stages.


- The user launches the cTrader application.

- The platform tries (and fails) to find an existing `accessToken` locally.

- Upon its failure to find a suitable `accessToken`, the platform opens the custom login/signup screen with the `firstLogin` parameter equalling `true`.

- The user interacts with the login/signup screen, fulfills their broker’s requirements, and successfully registers on the broker’s CRM.

- The broker’s backend sends a user creation request to the cTrader backend via API call 3.2.

- On success, the cTrader backend creates a new user and sends a response containing the `userId` API call 3.2.

- The broker’s client area stores the link between the ID of its internal user and the `userId`.

- (Optional) The user confirms the agreement forwarded by the broker (API call 3.13.).

- Following successful user creation, the web browser automatically opens the custom account creation screen. After the account creation form is submitted, a corresponding request is sent to the broker’s backend.

- As per API call 3.3., the broker’s CRM system submits a request for a trading account creation to the cTrader backend. On success, the cTrader backend sends a request containing the account `login`.

- The broker’s client area sends a request for account linkage; upon its fulfilment, the cTrader backend produces a confirmatory response (API call 3.4.).

- A record of the new trading account is stored in the broker’s CRM system. Subsequently, the CRM system generates a corresponding OT token.

- The user is redirected to the chosen success URL which also includes the OT token as a query parameter (`token`).

- As soon as the user visits the success URL, the application closes the web browser and stores the token.

- The application opens a new connection with the cTrader backend and sends an authorisation request including `token` as a parameter.

- The cTrader backend sends a POST-request via REST API to exchange the OT token for a long-term access token (API call 4.2.).

- The broker’s CRM verifies the `token` and responds with `accessToken`0 and `accessToken`1 (API call 4.2.).

- The cTrader backend authorizes the session under the provided `accessToken`2 and returns the `accessToken`3 to the application.

- The platform stores the `accessToken`4 for future usage.

- The application starts authorised communications with the cTrader backend.

---

## Page: Calls to the cTrader Backend
*Source: https://docs.spotware.com/Broker_SSO_OAuth/API_Calling_Backend*

# ¶ 3. Calls to the cTrader Backend


All API calls in this section are made by the broker’s backend to the cTrader backend.


## ¶ 3.1. Generate a Manager’s Token

| Method | URL |
| --- | --- |
| `POST` | `/webserv/managers/token` |


Creates a manager token required for API authentication. This token does not have an expiration period.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `hashedPassword` | Yes | string | The MD5 of the manager’s password. |
| `login` | Yes | integer | The unique ID of the manager. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `webservToken` | string | A long-term token authenticating the manager. |


**Request Example**


```curl
curl -X POST ‘https://HOST:PORT/v2/webserv/managers/token’ -H ‘Accept:application/json’ -H ‘Content-Type: application/json’ -d ‘{"hashedPassword": "0f94e246908667af85916300c57f74b6", "login": 2309}’

```

**Expected Response Status Code**


`200`


**Response Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```


## ¶ 3.2. Create a User

| Method | URL |
| --- | --- |
| `POST` | `/oauth2/ctid/create` |

Creates a new user via the SSO (OAuth) flow.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `brokerCrmName` | Yes | string | See Section 2.3. |
| `email` | Yes | string | The user’s email address. |
| `/webserv/managers/token`0 | No | string | The user’s first name. The value of this parameter can be used for sending notifications (e.g., ‘Dear {name}’). |
| `/webserv/managers/token`1 | No | string | The user’s cTID name. |
| `/webserv/managers/token`2 | No | string | The user’s preferred language. The parameter takes Alpha-2 (ISO 369-2) codes as values. |

> If the specified `/webserv/managers/token`3 is unique, it is set from the request. However, if the specified `/webserv/managers/token`4 is not unique or invalid (e.g., too long, contains forbidden characters, etc), it is inferred from the `/webserv/managers/token`5. If a`/webserv/managers/token`6 is not specified, it is inferred from the user’s email. If the `/webserv/managers/token`7 from the user’s email already exists, it is inferred from the `/webserv/managers/token`8.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/webserv/managers/token`9 | integer | The unique ID of a specific user. |


**Request Example**


```curl
curl -X POST 'https://HOST:PORT/cid/oauth2/ctid/create?token=04d95575-c9af-42fba72e-2f0ce93f01d4' --H 'Content-Type: application/json' --H 'Accept: application/json' -d '{"brokerCrmName": "BESTBROKERCRM", "email": "president@bestbroker.com", "firstName": "Trader", "nickname": "letstrade", "preferredLanguage": "en"}'

```

**Expected Response Status Code**


`hashedPassword`0


**Response Example**


```json
{
    "userId": 10345533
}

```


## ¶ 3.3 Create a Trader

| HTTP Method | URL |
| --- | --- |
| `hashedPassword`1 | `hashedPassword`2 |

Creates a new trader entity.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `hashedPassword`3 | Yes | enum | The access rights of the account. The following values are accepted. `hashedPassword`4. The account can perform all operations with no restrictions.`hashedPassword`5. The account can only close existing positions.`hashedPassword`6. The account cannot perform any trading operations.`hashedPassword`7. The account cannot log into cTrader. |
| `hashedPassword`8 | Yes | enum | The type of the trading account. The following values are accepted.`hashedPassword`9. The account can open positions in both directions for the same symbol simultaneously.`login`0. The account can only positions in one directions for a given symbol.`login`1. The account can perform spread betting operations. |
| `login`2 | Yes | long | The total balance of the new account. This parameter primarily exists for the creation of demo accounts with a non-zero balance. |
| `login`3 | Yes | string | A unique name denoting a specific broker (including White Labels). |
| `login`4 | Yes | string | The name of the currency that the account uses for making deposits and withdrawals. |
| `login`5 | Yes | string | The name of the group to which the account is assigned. |
| `login`6 | Yes | string | The MD5 of the account password. |
| `login`7 | Yes | integer | The total amount of leverage available to the account; is specified in 10^2. E.g., the 1:1 leverage is `login`8 while the 1:100 leverage is `login`9. |
| `webservToken`0 | Yes | enum | The strategy via which the account margin is calculated. The following values are accepted.`webservToken`1. The total margin requirements per symbol are equal to the maximum margin requirements for all positions opened for this symbol.`webservToken`2. The total margin requirements per symbol are equal to the sum of all margin requirements of all positions opened for this symbol.`webservToken`3. The total margin requirements per symbol are equal to the difference between the margin requirements for all long positions and all short positions opened for this symbol. |
| `webservToken`4 | No | JSON object | A JSON object containing the trader’s address, phone number, and other details as shown below. |
| `webservToken`5 | No | string | The trader’s address of residence. |
| `webservToken`6 | No | string | The trader’s city of residence. |
| `webservToken`7 | No | integer | The identifier the trader’s country of residence. The full list of these identifiers can be accessed here. |
| `webservToken`8 | No | string | The trader’s unique document ID. |
| `webservToken`9 | No | string | The trader’s email address. |
| `200`0 | No | string | The trader’s phone number. |
| `200`1 | No | string | The trader’s state of residence. |
| `200`2 | No | string | The zip code of the trader’s residence. |
| `200`3 | No | string | A custom identifier of the first-level partner that has introduced this trader. |
| `200`4 | No | string | A custom identifier of the second level-partner that has introduced this trader. |
| `200`5 | No | string | The description of the account. |
| `200`6 | No | boolean | The trader’s limited risk (LR) status. LR means the establishment of guaranteed stop losses. If `200`7, LR is enabled, and vice versa. |
| `200`8 | No | string | The last name of the account holder. |
| `200`9 | No | enum | The margin calculation strategy used for the limited risk account. The following values are accepted.`POST`0. Margin requirements have to be calculated based on the account leverage.`POST`1. Margin requirements have to be calculated based on the distance between the position open price and the guaranteed stop loss.`POST`2. cServer calculates the leverage-based and GSL-based margin requirements, and chooses the larger of the two values. |
| `POST`3 | No | integer | The maximum amount of leverage (in the base currency units) available to the account. Specified in 10^2. |
| `POST`4 | No | string | The first name of the account holder. |
| `POST`5 | No | boolean | A flag determining whether a daily trading statement is sent to the trader. |
| `POST`6 | No | boolean | A flag determining whether a daily account trading statement is sent to the broker under which the account is registered. |
| `POST`7 | No | boolean | A flag determining whether the account is charged swaps (`POST`8) or administrative fees (`POST`9). |


**Output**


For a JSON schema of the output, [**click here**](/WebServices_API/JSON_Schemas).


Several keys from the request body are repeated in the output, namely `/oauth2/ctid/create`0, `/oauth2/ctid/create`1, `/oauth2/ctid/create`2, `/oauth2/ctid/create`3, `/oauth2/ctid/create`4, `/oauth2/ctid/create`5, `/oauth2/ctid/create`6, `/oauth2/ctid/create`7, `/oauth2/ctid/create`8, `/oauth2/ctid/create`9, `brokerCrmName`0, `brokerCrmName`1, `brokerCrmName`2, `brokerCrmName`3, `brokerCrmName`4, `brokerCrmName`5, and `brokerCrmName`6.

| Key | Data Type | Description |
| --- | --- | --- |
| `brokerCrmName`7 | integer | The total amount of bonus funds allocated to the account. Subject to `brokerCrmName`8. |
| `brokerCrmName`9 | integer | The total amount of equity possessed by the account. Subject to `email`0. |
| `email`1 | integer | The amount of free margin available to the account. Subject to `email`2. |
| `email`3 | integer | The current amount of funds that the account can withdraw.It is calculated via the following formula: `email`4, where `email`5 are all management fees charged by the providers of strategies that the account owner has invested in. Subject to `email`6. |
| `email`7 | integer | A timestamp with the date and time of the latest account update. |
| `email`8 | integer | The number of a specific trading account. |
| `email`9 | integer | The number that determines how finance-related values are defined for the account. E.g., if `/webserv/managers/token`00 and `/webserv/managers/token`01, the account balance is 12345.12 in the account deposit currency.Additional details are given in Section 3. |
| `/webserv/managers/token`02 | integer | The total amount of the non-withdrawable bonus allocated to the account. Subject to `/webserv/managers/token`03. |
| `/webserv/managers/token`04 | integer | A timestamp with the date and time of account registration. |
| `/webserv/managers/token`05 | boolean | If this parameter equals true, rollover commissions are applied to the account instead of swaps. The reverse applies if the parameter is false. This field is useful for ensuring compliance with Sharia law. |
| `/webserv/managers/token`06 | integer | The total amount of margin in use by the account. Subject to `/webserv/managers/token`07. |


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
  "login": 8673590,
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


`/webserv/managers/token`08


## ¶ 3.4. Link a Trading Account to a User

| HTTP Method | URL |
| --- | --- |
| `/webserv/managers/token`09 | `/webserv/managers/token`10 |


Links a trader entity to a user entity.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/managers/token`11 | Yes | integer | The number of a specific trading account. |
| `/webserv/managers/token`12 | Yes | integer | The MD5 of the account password. |
| `/webserv/managers/token`13 | Yes | integer | The unique identifier of a user entity. |
| `/webserv/managers/token`14 | Yes | string | A unique name denoting a specific broker (including White Labels). |
| `/webserv/managers/token`15 | Yes | string | A unique name of a specific trading environment where the specified `/webserv/managers/token`16 is registered. |
| `/webserv/managers/token`17 | No | boolean | A flag that denotes whether the `/webserv/managers/token`18 key is returned in the response to this API call. Set it to `/webserv/managers/token`19 to ensure that the response to this call is not empty. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/webserv/managers/token`20 | integer | The unique identifier of the linkage between a specific user and one of their trading accounts. |


**Request Example**


```curl
curl -X POST 'https://HOST:PORT/cid/ctid/link?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc' -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"environmentName": "demo", "brokerName": "BESTBROKER", "traderLogin": 9017800, "traderPasswordHash": "0f94e246908667af85916300c57f74b6", "userId": 10333, "returnAccountDetails": true}'

```

**Response Example**


```json
{
    "ctidTraderAccountId": 90178000
}

```

**Expected Status Code**


`/webserv/managers/token`21

> Note that the response body will be empty if `/webserv/managers/token`22 is `/webserv/managers/token`23.


## ¶ 3.5. Change a Trader’s Balance

| HTTP Method | URL |
| --- | --- |
| `/webserv/managers/token`24 | `/webserv/managers/token`25 |


Changes the balance of a trader entity (including allocating/removing credit).


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `/webserv/managers/token`26 | path | Yes | integer | The number of a specific trading account. |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/managers/token`27 | No | string | A short note that can be attached to any balance change. This note is not shown to retail clients. |
| `/webserv/managers/token`28 | No | string | A number that matches an external identifier of the broker’s choosing. For instance, the value of `/webserv/managers/token`29 could be equal to the number of the bank transfer order through which the user chose to make a deposit. |
| `/webserv/managers/token`30 | No | string | A brief comment that can supplement a deposit or a withdrawal. In contrast to `/webserv/managers/token`31, this text is displayed to retail clients. |
| `/webserv/managers/token`32 | Yes | integer | The number of a specific trading account. |
| `/webserv/managers/token`33 | Yes | double | The precise amount of withdrawn or deposited funds/credit. Specified as a decimal number. For BTC and similar assets, the value of `/webserv/managers/token`34 can include as many as eight digits after the decimal point. |
| `/webserv/managers/token`35 | No | string | The designated source of the deposit/withdrawal. |
| `/webserv/managers/token`36 | Yes | string | The desired type of balance change. The following values are accepted.`/webserv/managers/token`37. Deposit funds to the trader.`/webserv/managers/token`38. Withdraw funds from the trader.  `/webserv/managers/token`39. Deposit credit to the trader. `/webserv/managers/token`40. Withdraw credit from the trader. |

> Note that only positive values are accepted when specifying the `/webserv/managers/token`41 parameter. The direction of the balance change is regulated entirely by the `/webserv/managers/token`42 parameter.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/webserv/managers/token`43 | integer | The identifier of a balance history entity containing all balance-related transactions for the specified trader.Note that bonus and credit are not included in `/webserv/managers/token`44. |


**Request Example**


```curl
curl -X POST 'https://HOST:PORT/v2/webserv/traders/8673590/changebalance?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc' -H 'Accept: application/json' -H 'Content-Type: application/json' -d '{"comment": "Test deposit", "externalId": "082123301", "externalNote": "New deposit!", "login": 8673590, "preciseAmount": 123.45, "source": "Source One", "type": "DEPOSIT"}'

```

**Output Example**


```json
{
  "balanceHistoryId": 6340680
}

```

**Expected Status Code**


`/webserv/managers/token`45


## ¶ 3.6. Set a New Partner Identifier

| Method | URL |
| --- | --- |
| `/webserv/managers/token`46 | `/webserv/managers/token`47 |


Creates a new partner by linking a partner identifier (a string) from the broker’s backend to an existing user or an existing account on the cTrader backend.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/managers/token`48 | Yes | string | See Section 2.3.. |
| `/webserv/managers/token`49 | Yes | string | The string assigned as a partner identifier to a specific user or an account. |
| `/webserv/managers/token`50 | No (if the chosen partner is an account) | integer | The unique ID of a specific user. |
| `/webserv/managers/token`51 | No (if the chosen partner is a user) | integer | The unique ID of the linkage between a specific user and one of their trading accounts. |

> The request body can include either a `/webserv/managers/token`52  or a `/webserv/managers/token`53 depending on the entity to which the partner identifier is assigned. To elaborate, `/webserv/managers/token`54 is a mandatory parameter if the identifier is assigned to a user; alternatively, `/webserv/managers/token`55 is a mandatory parameter if the identifier is assigned to an account.


**Request Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
0
**Expected Response Status Code**


`/webserv/managers/token`56


## ¶ 3.7. Read a Partner Identifier

| Method | URL |
| --- | --- |
| `/webserv/managers/token`57 | `/webserv/managers/token`58 |


Retrieves the unique partner identifier of a specific partner entity.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `/webserv/managers/token`59 | query | No (if the partner entity is an account) | integer | The unique ID of a specific user. |
| `/webserv/managers/token`60 | query | No (if the partner entity is a user) | integer | The unique ID of the linkage between a specific user and one of their trading accounts. |
| `/webserv/managers/token`61 | query | Yes | string | See Section 2.3.. |

> The request body can include either a `/webserv/managers/token`62  or a `/webserv/managers/token`63 depending on the entity to which the partner identifier is assigned. To elaborate, `/webserv/managers/token`64 is a mandatory parameter if the identifier is assigned to a user; alternatively, `/webserv/managers/token`65 is a mandatory parameter if the identifier is assigned to an account.


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/webserv/managers/token`66 | integer | The unique ID of the linkage between a specific user and one of their trading accounts. |
| `/webserv/managers/token`67 | integer | The unique ID of a specific user. |
| `/webserv/managers/token`68 | string | The string assigned as a partner identifier to a specific user or an account. |


**Request Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
1
**Expected Response Status Code**


`/webserv/managers/token`69


**Response Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
2

## ¶ 3.8. Delete an Existing Partner Identifier

| Method | URL |
| --- | --- |
| `/webserv/managers/token`70 | `/webserv/managers/token`71 |

Deletes the partner identifier attached to a specific partner entity.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `/webserv/managers/token`72 | query | Yes | integer | The unique ID of a specific user. |
| `/webserv/managers/token`73 | query | No | integer | The unique ID of the linkage between a specific user and one of their trading accounts. |
| `/webserv/managers/token`74 | query | Yes | string | See Section 2.3.. |


If `/webserv/managers/token`75 is unspecified, only a record with an unspecified account will be deleted.


**Request Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
3
**Expected Response Status Code**


`/webserv/managers/token`76


## ¶ 3.9. Create a New InApp Control

| Method | URL |
| --- | --- |
| `/webserv/managers/token`77 | `/webserv/managers/token`78 |


Sets up one or more InApp controls in the form of ribbons.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/webserv/managers/token`79 | Yes | string | See Section 2.3. |
| `/webserv/managers/token`80 | Yes | integer | The ID of the user to whom the created InApp controls will be displayed. |
| `/webserv/managers/token`81 | Yes | object | An object containing the key types of the created InApp control(s). |
| `/webserv/managers/token`82 | Yes | array | An array containing the main characteristics of the created ribbons. Each ribbon constitutes a separate JSON object. |
| `/webserv/managers/token`83 | Yes | string | The six-digit HEX value of the color assigned to a specific ribbon. |
| `/webserv/managers/token`84 | Yes | string | The text displayed on the ribbon. |
| `/webserv/managers/token`85 | Yes | boolean | A boolean value determining whether a ribbon is active (i.e., shown to the user). |
| `/webserv/managers/token`86 | Yes | boolean | A boolean value determining whether the ribbon is closable by the user. Upon subsequent application launches, all closed ribbons will be re-shown to the user. |
| `/webserv/managers/token`87 | No | string | The name of a specific broker. The ribbon will only be shown to users whose trading account belongs to this broker. |
| `/webserv/managers/token`88 | No | string | The unique ID of the linkage between a specific user and one of their trading accounts. |
| `/webserv/managers/token`89 | Yes | object | An object listing the InApp actions that occur when users interact with the ribbon. |
| `/webserv/managers/token`90 | No (but only when using in-app URLs) | string | The external URL assigned to the relevant InApp action. Upon interaction, opens a separate external browser window. |
| `/webserv/managers/token`91 | No (but only when using external URLs) | string | The in-app URL assigned to the relevant InApp action. Upon interaction, opens an iframe. |

> As the `/webserv/managers/token`92 array may include several JSON objects (each acting as a unique ribbon), you may combine parameters to create custom sets of InApp controls shown under different circumstances. For instance, you may create ribbons that are only shown to users logged in under a specific account; alternatively, certain ribbons may only be shown to users whose current account belongs to a certain White Label (`/webserv/managers/token`93).


There are three possible cases that may arise depending on the parameters specified in the request body.


- If a valid `/webserv/managers/token`94 is specified, the ribbon(s) will only be shown to sessions logged in under this specific account.

- If `/webserv/managers/token`95 is unspecified but a valid `/webserv/managers/token`96 is specified, and there is no ribbon matching by account, the ribbon(s) will be shown to sessions under this specific `/webserv/managers/token`97.

- If neither `/webserv/managers/token`98 nor `/webserv/managers/token`99 is specified and there is no ribbon matching by account or `hashedPassword`00, the ribbons(s) will be shown to sessions under the specified `hashedPassword`01.


You may also choose to send an empty `hashedPassword`02 object to immediately clear all ribbons already shown to the sessions specified via other parameters.


**Request Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
4
**Alternate Example** (for clearing ribbons)


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
5
**Expected Response Status Code**


`hashedPassword`03


## ¶ 3.10. Change a User’s Email

| Method | URL |
| --- | --- |
| `hashedPassword`04 | `hashedPassword`05 |


Changes a user’s email in the cTrader backend in the event of an email change in the broker’s CRM system.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `hashedPassword`06 | Yes | integer | The unique ID of a specific user. |
| `hashedPassword`07 | Yes | string | The user’s new email address. |
| `hashedPassword`08 | Yes | string | See Section 2.3. |


**Request Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
6
**Expected Response Status Code**


`hashedPassword`09


## ¶ 3.11. Read a User’s Identifier by Email

| Method | URL |
| --- | --- |
| `hashedPassword`10 | `hashedPassword`11 |


Gets the `hashedPassword`12 of the user with the specified `hashedPassword`13.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `hashedPassword`14 | query | Yes | string | See Section 2.3. |
| `hashedPassword`15 | query | Yes | string | The email of the user for which you would like to get `hashedPassword`16. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `hashedPassword`17 | integer | The unique ID of a specific user. |


**Request Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
7
**Expected Status Code**


`hashedPassword`18


**Response Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
8
> Note that if the user with the specified `hashedPassword`19 and `hashedPassword`20 does not exist, you will still receive code `hashedPassword`21; however, the response will be empty.


## ¶ 3.12. Log Out a User From cTrader

| Method | URL |
| --- | --- |
| `hashedPassword`22 | `hashedPassword`23 |

Logs out the user with the specified `hashedPassword`24 from all cTrader applications and drop all of the user’s current sessions if they exist.

> The primary purpose of this call is to log out a user from cTrader whenever they log out from inside your client area.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `hashedPassword`25 | query | Yes | string | See Section 2.3. |
| `hashedPassword`26 | query | Yes | integer | The unique ID of a specific user. |


**Output**


This API call does not produce an output.


**Request Example**


```json
{
    "webservToken": "04d95575-c9af-42fba72e-2f0ce93f01d4"
}

```
9
**Expected Status Code**


`hashedPassword`27


## ¶ 3.13. Confirm User Agreement

| Method | URL |
| --- | --- |
| `hashedPassword`28 | `hashedPassword`29 |


Confirms user agreement by updating the user’s details.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `hashedPassword`30 | query | Yes | string | See Section 2.3. |
| `hashedPassword`31 | query | Yes | integer | The unique ID of a specific user. |


**Output**


This API call does not produce an output.


**Request Example**


```curl
curl -X POST 'https://HOST:PORT/cid/oauth2/ctid/create?token=04d95575-c9af-42fba72e-2f0ce93f01d4' --H 'Content-Type: application/json' --H 'Accept: application/json' -d '{"brokerCrmName": "BESTBROKERCRM", "email": "president@bestbroker.com", "firstName": "Trader", "nickname": "letstrade", "preferredLanguage": "en"}'

```
0
**Expected Status Code**


`hashedPassword`32

---

## Page: Calls to the Broker's CRM
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/API_Calling_CRM*

# ¶ 4. Calls to the Broker’s CRM


All API calls in this section are made by the cTrader backend to your client area/CRM. All endpoints are relative to [**the URL of your client area**](/Broker_SSO_OAuth/Getting_Started/). You need to provide this URL to Spotware at the initial stages of deployment.

> The `inappToken` parameter provides an additional validation mechanism for generating OT tokens for performing InApp actions, You can optionally return this parameter as part of API call 4.2 and API call 4.3. If you choose to return it, you would later need to verify it as part of API call 4.4. If this verification is failed, your backend must not issue an OT token for performing an InApp action. If you choose to not return it, no additional verifications would need to be made as part of API call 4.4.


## ¶ 4.1. Authenticate the cTrader Backend

| Method | URL |
| --- | --- |
| `POST` | `/oauth2/crmApiToken` |


Authenticates all subsequent requests made by the cTrader backend by exchanging a pre-generated valid password with an access token. This token should be valid for at least a week; its expiration period can be increased at your discretion.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `password` | Yes | string | The password generated by the cTrader backend. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `crmApiToken` | string | A non-repeatable token authenticating the cTrader backend. After it is issued, it is placed in the memory storage of the cTrader backend. |


**Request Example**


```curl
curl -X POST ‘https://brokerCrmUrl.com/oauth2/crmApiToken’ -H ‘Content-Type: application/json’ -H ‘Accept: application/json’ -d ‘{"password": "af34mn0pphg2893nmaf26hmy"}’

```

**Expected Response Status Code**


`200`

> Click here to see the additional error codes that may arise when making this call.


**Output**


```json
{
    "crmApiToken": "cr56mng23454laf5545sdfdf234fs541200sdf"
}

```


## ¶ 4.2. Verify and Exchange an OT Token

| Method | URL |
| --- | --- |
| `POST` | `/oauth2/onetime/authorize` |

Verifies an OT token and exchanges it for a long-term access token.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `code` | Yes | string | An OT token generated by the broker’s backend. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `accessToken` | string | A non-repeatable token allowing for long-term access to the trading environment. It is only returned if a user has previously clicked on the ‘Keep Me Logged In’ tick box or a similarly named alternative. |
| `POST`0 | integer | The unique ID of a specific user. |
| `POST`1 | string | An optional token that you can use for additional validation when generating an OT token for an InApp action as part of API call 4.4. |


**Request Example**


```curl
curl -X POST ‘https://brokerCrmUrl.com/oauth2/onetime/authorize?crmApiToken=cr56mng23454laf5545sdfdf234fs541200sdf’ -H ‘Content-Type: application/json’ -H ‘Accept: application/json’ -d ‘{"code": "16chD7xeIxc3p387Cjdcnpax2er"}’

```

**Expected Response Status Code**


`POST`2

> Click here to see the additional error codes that may arise when making this call.


**Response Example**


```json
{
    "accessToken": "0eZXAw8GJQ55RlDcALSVi6xPDHTRCivfE9STSyBfeMxRWZAGEIe0VujpibDP",
    "userId": 10345533,
    "inappToken": "12MBoxLAP_2313PxolklqPX_weq1kjksaPASDHJ_sx"
}

```


## ¶ 4.3. Verify a Long-Term Access Token

| Method | URL |
| --- | --- |
| `POST`3 | `POST`4 |

Verifies a long-term access token during the automatic re-login flow.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `POST`5 | Yes | string | A non-repeatable token allowing for long-term access to the trading environment. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `POST`6 | integer | The unique ID of a specific user. |
| `POST`7 | string | An optional token that you can use for additional validation when generating an OT token for an InApp action as part of API call 4.4. |


**Request Example**


```curl
curl -X POST ‘https://brokerCrmUrl.com/oauth2/authorize?crmApiToken=cr56mng23454laf5545sdfdf234fs541200sdf’ -H ‘Content-Type: application/json’ -H ‘Accept: application/json’ -d ‘{"accessToken": "0eZXAw8GJQ55RlDcALSVi6xPDHTRCivfE9STSyBfeMxRWZAGEIe0VujpibDP"}’

```

**Expected Response Status Code**


`POST`8

> Click here to see the additional error codes that may arise when making this call.


**Response Example**


```json
{
    "userId": 10345533,
    "inappToken": "12MBoxLAP_2313PxolklqPX_weq1kjksaPASDHJ_sx"
}

```


## ¶ 4.4. Generate an OT Token for an InApp Action

| Method | URL |
| --- | --- |
| `POST`9 | `/oauth2/crmApiToken`0 |

Requests the creation of an OT token required for perfoming an InApp action.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `/oauth2/crmApiToken`1 | query | No | string | An optional token that you can use for additional validation when generating an OT token for an InApp action. |


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `/oauth2/crmApiToken`2 | Yes | integer | The unique ID of a specific user. |


**Output**

| Key | Data Type | Description |
| --- | --- | --- |
| `/oauth2/crmApiToken`3 | string | An OT token generated by the broker’s backend. |


**Request Example**


```curl
curl -X POST ‘https://brokerCrmUrl.com/oauth2/onetime/generate?inappToken=12MBoxLAP_2313PxolklqPX_weq1kjksaPASDHJ_sx&crmApiToken=cr56mng23454laf5545sdfdf234fs541200sdf’ -H ‘Content-Type: application/json’ -H ‘Accept: application/json’ -d ‘{"userId": 10345533}’

```

**Expected Response Status Code**


`/oauth2/crmApiToken`4


**Response Example**


```json
{
    "token": "16chD7xeIxc3p387Cjdcnpax2er"
}

```

> Click here to see the additional error codes that may arise when making this call.


## ¶ 4.5. Log Out a User From the CRM

| Method | URL |
| --- | --- |
| `/oauth2/crmApiToken`5 | `/oauth2/crmApiToken`6 |

Log out the user with the specified `/oauth2/crmApiToken`7 from the CRM.

> The primary purpose of this API call is to log out a user from your client area whenever they log out of any cTrader app.


**Parameters**

| Parameter | Parameter Type | Required? | Data Type | Description |
| --- | --- | --- | --- | --- |
| `/oauth2/crmApiToken`8 | query | Yes | string | The unique ID of a specific user. |
| `/oauth2/crmApiToken`9 | query | Yes | string | A non-repeatable token allowing for long-term access to the trading environment. It is only returned if a user has previously clicked on the ‘Keep Me Logged In’ tick box or a similarly named alternative. |


**Output**


This API call should not produce an output.


**Request Example**


```curl
curl -X POST ‘https://brokerCrmUrl.com/oauth2/logout?crmApiToken=cr56mng23454laf5545sdfdf234fs541200sdf&userId=10345533&accessToken=0eZXAw8GJQ55RlDcALSVi6xPDHTRCivfE9STSyBfeMxRWZAGEIe0VujpibDP’ -H ‘Content-Type: application/json’ -H ‘Accept: application/json’

```

**Expected Response Status Code**


`password`0

---

## Page: Conformance Testing
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/Conformance_Testing*

# ¶ 6. Conformance Testing


This section contains conformance tests, their stages, and accepted results.


Note that conformance testing is a regular process conducted entirely by Spotware. Passing conformance tests is an essential requirement for continued operations with our SSO (OAuth) flows.

> When performing an API call as part of conformance testing and encountering an error, provide the error description to Spotware’s Service Assurance team.

> In cases 6.2.1 - 6.2.4 and case 6.2.6, check the following screens.
> 1. The login/signup screen.
> 2. The deposit/withdrawal screen.
> 3. The ‘Open New Account’ screen.
> 4. The ‘Change Password’ screen.
> 5. The ‘Change Email’ screen.


When testing how content is displayed by variious SSO (OAuth) screens as part of cases **6.2.1** and **6.2.2**, make sure that the screens conform to the following requirements.


- The screens have responsive designs to match mobile and desktop layouts.

- None of the screens mentions ‘cTrader ID’.

- None of the screens mentions other trading platforms except cTrader.

- The screens mention correct legal entities and do not mislead users (e.g., by referring to incorrect jurisdictions).

- No pop-up messages appear on any screen.

- The screens are neatly organised with no unnecessary UI elements (e.g., ‘Chat’ buttons or equivalent in the login/signup screen).

- The screen loading times are three seconds or less on any platform, hardware, and all common Internet connection speeds.


> Note that the majority of all tests described on this page are mandatory. They cover essential SSO (OAuth) operations, user flows, and API calls. Only tests 6.2.3-6.2.6 are optional and are marked as such in their titles.


## ¶ 6.1. API Calls Testing


**6.1.1. The cTrader backend is authenticated [(API call 4.1**)](/Broker_SSO_OAuth/API_Calling_CRM#h-41-authenticate-the-ctrader-backend)

| Test Steps | Expected Results |
| --- | --- |
| 1. Send a `POST` request to authenticate the cTrader backend with a valid password.2. Send a `POST` request to authenticate the cTrader backend with an invalid password. | 1. The broker’s backend returns a response with code `200`; the output contains `crmApiToken`.2. The broker’s backend returns a response with an error with code `403`; the output does not contain `crmApiToken`. |


**6.1.2. An OT token is checked, verified, and exchanged [(API call 4.2**)](/Broker_SSO_OAuth/API_Calling_CRM#h-42-verify-and-exchange-an-ot-token)

| Test Steps | Expected Results |
| --- | --- |
| 1. Send a `POST` request to verify and exchange a valid OT token with a valid `crmApiToken`.2. Send a `POST` request to verify and exchange an invalid OT token with a valid `crmApiToken`.3. Send a `POST`0 request to verify an OT token with an invalid `POST`1. | 1. The broker’s backend returns a response with code `POST`2; the output contains `POST`3 and `POST`4.2. The broker’s backend returns a response with an error with code `POST`5. The output does not contain `POST`6 and `POST`7.3. The broker’s backend sends a response with an error with code `POST`8. The output does not contain `POST`9 and `200`0. |


**6.1.3. A long-term access token is checked and verified [(API call 4.3**)](/Broker_SSO_OAuth/API_Calling_CRM#h-43-verify-a-long-term-access-token)

| Test Steps | Expected Results |
| --- | --- |
| 1. Send a `200`1 request to verify a long-term access token with a valid `200`2.2. Send a `200`3 request to verify a long-term access token with an invalid `200`4.3. Send a `200`5 request to verify an long-term token with an invalid `200`6. | 1. The broker’s backend returns a response with code `200`7; the output contains `200`8.2. The broker’s backend returns a response with an error with code `200`9; the output does not contain the `crmApiToken`0.3. The broker’s backend sends a response with an error with code `crmApiToken`1. The output does not contain `crmApiToken`2 and `crmApiToken`3. |


**6.1.4. An OT token is generated for an InApp action [(API call 4.4**)](/Broker_SSO_OAuth/API_Calling_CRM#h-44-generate-an-ot-token-for-an-inapp-action)

| Test Steps | Expected Results |
| --- | --- |
| 1. Send a `crmApiToken`4 request to generate an OT token with a valid `crmApiToken`5.2. Send a `crmApiToken`6 request to generate an OT token with an invalid `crmApiToken`7.3. Send a `crmApiToken`8 request to generate an OT token with an invalid `crmApiToken`9. | 1. The broker’s backend returns a response with code `403`0; the output contains an OT token.2. The broker’s backend returns a response with an error with code `403`1; the output does not contain an OT token.3. The broker’s backend sends a response with an error with code `403`2. The output does not contain `403`3 and `403`4. |


**6.1.5. The broker’s backend generates a new OT token each time it is requested to do so**

| Test Steps | Expected Results |
| --- | --- |
| 1. Log in under an existing user.2. Wait for the success page to appear.3. Log in under an existing user in incognito mode.4. Wait for the success page to appear. | 1. The success page is opened after a successful login.2. The broker’s backend generates and returns an OT token.3. The success page is opened after a successful login.4. The broker’s backend generates and returns an OT token; this token is different from the one generated during Step 2. |


**6.1.6. Different OT tokens are generated for different users**

| Test Steps | Expected Results |
| --- | --- |
| 1. Authorise the user with `403`5 inside the broker’s backend and generate an OT token for this user.2.Authorise the user with `403`6 inside the broker’s backend and generate an OT token for this user. | 1. A valid OT token is generated.2. A valid OT token is generated. It is different from the token generated during Step 1. |


**6.1.7. OT tokens expire one minute after generation**

| Test Steps | Expected Results |
| --- | --- |
| 1. Authorise a user inside the broker’s backend, generate an OT token for the corresponding `403`7, and remember it.2. Wait one minute.3. Send a request to exchange this token for an `403`8 (API call 4.2.) with a valid `403`9. | 1. A valid OT token is generated.2. A minute is expired.3. The broker’s backend returns a request containing an error as the OT token has expired. |


**6.1.8. All API calls use the `crmApiToken`0 protocol**

| Test Steps | Expected Results |
| --- | --- |
| 1. Send any request with valid parameters and a request body using the `crmApiToken`1 protocol. 2. Send any request with valid parameters and a request body using the `crmApiToken`2 protocol. | 1. The request is unsuccessful. 2. The request is unsuccessful. |


**6.1.9. All servers have valid certificates**

| Test Steps | Expected Results |
| --- | --- |
| 1. Check server certificates. | 1. All servers have valid certificates. |


## ¶ 6.2. Design Testing


**6.2.1. Check screen designs when using different browsers**


Repeat this case for all major browsers including Chrome, Firefox, Safari and Edge. Use incognito tabs for each step. For examples of screens, see [**Section 2**](/Broker_SSO_OAuth/General_Provisions_Requirements/).

| Test Steps | Expected Results |
| --- | --- |
| 1. Open an SSO (OAuth) screen through all of its stages. | 1. The screen contents are displayed correctly and satisfy key requirements (see above). |


**6.2.2. Check screen designs when using different screen sizes.**


Repeat this process for all common screen sizes and aspect ratios such as 4:3 and 16:9.

| Test Steps | Expected Results |
| --- | --- |
| 1. Open an SSO (OAuth) screen through all of its stages. | 1. The screen contents are displayed correctly and satisfy key requirements (see above). |


**6.2.3. The screens support the [`crmApiToken`3 parameter](/Broker_SSO_OAuth/Flows_Stages#h-52-urls-and-their-parameters) (optional test)**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open an SSO (OAuth) screen with `crmApiToken`4 equal to `crmApiToken`5.2. Open the same screen with `crmApiToken`6 equal to another valid Alpha-2 code that your brokerage supports.3. Open the same screen with `crmApiToken`7 equal to an Alpha-2 code that the broker’s backend does not support. | 1. The opened iframe displays the correct screen and has `crmApiToken`8. The screen is displayed in English.2. The opened iframe displaus the correct screen and has `crmApiToken`9. The screen is displayed in the language matching the specified code. 3. The opened iframe displays the correct screen and has `POST`0. The screen is displayed using whatever language is specified as the default language by the broker’s backend. |


**6.2.4. The screens support the [`POST`1 parameter](/Broker_SSO_OAuth/Flows_Stages#h-52-urls-and-their-parameters) (optional test)**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open an SSO (OAuth) screen with `POST`2 equal to `POST`3.2. Open the same screen screen with `POST`4 equal to `POST`5. | 1. The opened iframe displays the correct screen and has `POST`6. The screen is displayed using the light UI theme.2. The opened iframe displays the correct screen and has `POST`7. The screen is displayed using the dark UI theme. |


**6.2.5. The screens support the [`POST`8 parameter](/Broker_SSO_OAuth/Flows_Stages#h-52-urls-and-their-parameters) (optional test)**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open the login/signup screen with `POST`9 equal to `crmApiToken`0.2. Open the login/signup screen with `crmApiToken`1 equal to `crmApiToken`2. | 1. The opened iframe displays the signup screen and has `crmApiToken`3. The screen displays suitable information for first-time user creation.2. The opened iframe displays the signup screen and has `crmApiToken`4. The screen displays suitable information for an existing user; the screen does not offer to create a first account. |


**6.2.6. The screens support changing multiple parameters simultaneously  (optional test).**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open an SSO (OAuth) screen with `crmApiToken`5 and `crmApiToken`6.2. Change `crmApiToken`7 to a valid Alpha-2 code supported by your brokerage; change `crmApiToken`8 to `crmApiToken`9. | 1. The iframe displays the correct screen, its content is in English, and it has the dark UI theme.2. The iframe displays the correct screen, its content is in the specified language, and it has the light UI theme. |


**6.2.7. The login/signup screen contains the ‘Reset Password**’ button or its equivalent.

| Test Steps | Expected Results |
| --- | --- |
| 1. Open the login/signup screen with `POST`0. | 1. The screen displays a ‘Reset Password’ button or its equivalent. This control can be interacted with. |


## ¶ 6.3. Functional Testing


**6.3.1. A new user is able to pass the [user creation flow](/Broker_SSO_OAuth/Flows_Stages/User_Creation_Flow).**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open the login/signup screen.2. Type valid data into all fields and complete the signup process.3. Wait while the cTrader backend sends a request to exchange the OT token for a long-term access token (API call 4.2).4. Wait until you are logged into the newly created account.5. Close cTrader.6. Open cTrader. | 1. The login/signup screen is opened; `POST`1 is missing.2. The broker’s backend sends a request to create a new user (API call 3.2.) followed by a request for live trading account creation (API call 3.3.), and user-account linkage (API call 3.4). The cTrader backend creates a live trading account and links it to the correct cTID. The broker’s backend receives a response with `POST`2. The success URL is opened with a valid OT token.3.  The broker’s backend verifies the OT token and returns a successful response containing `POST`3 and `POST`4 (API call 4.2). The cTrader backend authorises the user and returns `POST`5 to the application.4. The user is successfully authorised under the correct cTID; `POST`6 is saved.5. cTrader is closed.6. cTrader is opened. API call 4.3 is performed with the `POST`7 saved during Step 4. The broker’s backend returns a correct `POST`8. The user is authorised under the cTID from Step 3. |


**6.3.2. A user is able to log in using valid credentials.**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open the login/signup screen.2. Type a valid email and password and click on the ‘Submit’ button or its equivalent.3. Check the URL of the success page.4. Wait until the current iframe is closed.5. Wait until you are logged in.6. Close cTrader.7. Open cTrader. | 1. The login/signup screen is opened; `POST`9 is missing. 2. The broker’s backend finds the `crmApiToken`0 of the user and generates an OT token.3. The URL contains the OT token generated during Step 2. 4. The application sends a request to the cTrader backend with the OT token. The cTrader backend sends a request to exchange the OT token for a long-term access token (API call 4.2). The broker’s backend verifies the OT token and returns a successful response containing `crmApiToken`1 and `crmApiToken`2 (API call 4.2). The cTrader backend authorises the user and returns `crmApiToken`3 to the application.5. The user is authorized successfully under the correct cTID; `crmApiToken`4 is saved.6. cTrader is closed.7. cTrader is opened. API call 4.3 is performed with the `crmApiToken`5 saved during Step 5. The broker’s backend returns a correct `crmApiToken`6. The user is authorized under the cTID from Step 5. |


**6.3.3. Traders are attributed to correct partners via the `crmApiToken`7 parameter**

| Test Steps | Expected Results |
| --- | --- |
| 1. Create a new user in the broker’s client area.2. Register the new user as a partner in the broker’s client area and receive a unique partner identifier.3. Open the login/signup screen in incognito mode with the value of the `crmApiToken`8 parameter equal to the identifier received during Step 2.4. Complete the signup flow while using a different set of credentials compared to the one used during Step 1.5. In the broker’s client area, log in as the user from Step 1 and proceed to the list of attributed traders. | 1. A new user is successfully created in the broker’s client area.2. A valid partner identifier is generated either at the account or the user level.3. The login/signup screen is opened; its URL contains the correct `crmApiToken`9.4. The user creation flow is passed successfully (see case 6.3.1). The broker’s client area attributes the new user to the user whose partner identifier matches the `POST`00 parameter from the login/signup screen URL.5. The user sees a new trader in their list of attributed traders. This trader has the same details as the new user created during Step 4. |


**6.3.4. An authorised user can make a deposit**

| Test Steps | Expected Results |
| --- | --- |
| 1. Log into the trading platform. 2. Click on the ‘Deposit’ button. 3. Fill out the form with correct data and submit it. | 1. Login is successful under the correct cTID. 2. cTrader sends a request to the cTrader backend to attain an OT token. The cTrader backend sends a request to the broker’s client area containing `POST`01 (API call 4.4). The broker’s backend verifies `POST`02, generates an OT token and returns it to the cTrader backend (API call 4.4). The cTrader backend returns the token to the application; the deposit/withdrawal screen is opened in an iframe containing the OT token as a query parameter. 3. The application sends a request to the broker’s backend; the broker’s backend sends a request to the cTrader backend to change the account balance (API call 3.5). The cTrader backend sends a response with `POST`03 to the broker’s backend (API call 3.5). The broker’s backend returns a response to the application. The user is redirected to the success page. |


**6.3.5. An authorised trader can make a withdrawal.**

| Test Steps | Expected Results |
| --- | --- |
| 1. Log into the trading platform. 2. Click on the ‘Withdrawal’ button. 3. Fill out the form with correct data and submit it. | 1. Login is successful under the correct cTID. 2. cTrader sends a request to the cTrader backend to attain an OT token. The cTrader backend sends a request to the broker’s client area containing `POST`04 (API call 4.3). The broker’s backend verifies `POST`05, generates an OT token and returns it to the cTrader backend (API call 4.4). The cTrader backend returns the token to the application; the deposit/withdrawal screen is opened in an iframe containing the OT token as a query parameter. 3. The application sends a request to the broker’s backend; the broker’s backend sends a request to the cTrader backend to change the account balance (API call 3.5). The cTrader backend sends a response with `POST`06 to the broker’s backend (API call 3.5). The broker’s backend returns a response to the application. The user is redirected to the success page… |


**6.3.6. An authorised user can create a new trading account**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open the ‘Create New Account’ form.2. Fill all required fields and submit the form. | 1. The ‘Create New Account’ form is opened. The form URL has `POST`07.2. The broker’s backend sends a request to create a new account. The cTrader backend returns a response with the account `POST`08 (API call 3.3). The broker’s backend sends a request to link the new account (API call 3.4). The cTrader backend returns a confirmatory response with `POST`09. The broker’s backend has a record about the new account.3. The user sees the success page. The user is automatically switched to their new account after the success page is closed. |


**6.3.7. The user is able to switch between login and signup on the login/signup screen**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open the login/signup screen.2. Click on a link to proceed to the login form.3. Click on a link to the signup form. | 1. The login/signup screen is opened.2. The login form is opened. This form contains a link to the signup form.3. The signup form is opened. This form contains a link to the login form. |


**6.3.8. The user can open embedded cTrader Web from the broker’s client area**

| Test Steps | Expected Results |
| --- | --- |
| 1. Log into the broker’s client area.2. Access cTrader Web using either of the two possible options (in an iframe or via a link/button). | 1. The authorised user sees a means to open cTrader Web from the broker’s client area.2. The user accesses cTrader Web and is authorised inside the application. |


**6.3.9. Traders can reset their password via the ‘Reset Password’ button (or equivalent) on the login screen.**

| Test Steps | Expected Results |
| --- | --- |
| 1. Open the login/signup screen.2. Click on the ‘Reset Password’ button or equivalent.3. Receive a new email containing a link to resetting your password.4. Follow the link and complete the password reset flow.5. Open the login/signup screen. 6. In the ‘Password’ field or equivalent type the password chosen during Step 2 and proceed with authorisation. | 1. The login/signup screen is opened; it displays suitable information for an existing user.2. The button is clickable and a password reset is requested.3. A valid email is received containing a password reset link.4. When clicking on the link, the user is redirected to the platform. After seeing the confirmation message, the user is automatically authorised inside the platform.5. The login/signup screen is opened; it displays suitable information for an existing user.6. The user is authorised inside the platform. |

---

## Page: Glossary
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/Glossary*

# ¶ Glossary


This section defines the key terms used in this technical documentation. General-purpose terms are not included unless their meaning sufficiently differs from their ordinary definition.


**Broker SSO (OAuth)**. A series of flows enabling traders to engage in user creation/authorisation without leaving cTrader. Spotware’s SSO (OAuth) solution still uses brokers’ client areas as user creation/authorisation servers.


**Broker’s client area/CRM system/backend**. A software suite belonging to a broker. In general, such systems allow managers to perform several actions embedded into the broker’s business flows including making withdrawals/deposits, creating accounts, and passing KYC checks. Performing these actions is only permitted to existing authorised users.


**cTrader/cTrader backend**. A piece of software designed and distributed by Spotware Systems. This backend suite allows for managing, creating, and authorising users within the cTrader environment.


**Application/platform**. These terms denote cTrader mobile applications (both iOS and Android), the cTrader web client, and the cTrader desktop suite.


**One-time (OT) token**. A one-time access token that is generated by a broker’s client area as a response to a request sent by the cTrader backend. OT tokens can also be generated by brokers’ backend systems automatically when authorising existing users or creating new users.


**Long-term access token (`accessToken`)**. A long-term access token that is similarly generated by a broker’s backend when responding to a request from the cTrader backend. Alternatively, in the automatic re-login flow, brokers’ CRM systems are tasked with validating an already existing long-term token. Long-term tokens are issued for an indefinite period determined by individual brokers.

> Note that the long-term token is only issued if a user selects the ‘Keep Me Logged In’ (or a similarly named) option during creation/authorisation.


**Partner/IB**. An individual stakeholder whose main responsibility is to attract new traders to brokers; successful trader acquisitions typically result in the provision of monetary rewards.


**InApp controls**. A set of UI controls available to end users. Interacting with an InApp control should result in the platform performing an associated InApp action (defined below). InApp controls are included in the broker SSO (OAuth) package.


**InApp action**. An action that, from a user’s perspective, needs to be taken within the trading platform but is, nevertheless, carried out within a broker’s client area/CRM.

---

## Page: Starting Deployment
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/Getting_Started*

# ¶ 7. Starting Deployment


In this section, we explain what you should do to start deploying Spotware’s broker SSO (OAuth) solution.


At the initial stages of deployment, Spotware will provide you with a dedicated environment for user acceptance testing (UAT). To do so, Spotware will require you to provide two URLs.


## ¶ 7.1. The URL to Your Login/Signup Screen


The first URL should lead to your custom branded login/signup screen.


For [**first-time users**](/Broker_SSO_OAuth/Flows_Stages/User_Creation_Flow/) or for [**users logging in with a password**](/Broker_SSO_OAuth/Flows_Stages/User_Authorization_Flow/) the new SSO (OAuth) flows display a custom fully branded login/signup screen as discussed in [**Section 5.2**](/Broker_SSO_OAuth/Flows_Stages#h-52-urls-and-their-parameters).


This screen is essentially the first thing that is shown to new users upon launching cTrader. As such, we require you to provide us with a URL to this screen to proceed with deploying our SSO (OAuth) flows.

> Note that the `?firstLogin` query parameter discussed in Section 5.2 controls whether users are presented with a signup screen or a login screen. As such, both the login and the signup screen have to be hosted at the same URL. For an illustration, refer to the below examples.
> `https://ct.brokerName.com/Trader/Logon?firstLogin=true` should lead users to the signup screen.
> `https://ct.brokerName.com/Trader/Logon?firstLogin=false` should lead users to the login screen.

> If your login/signup page allows users to login or signup using their Apple ID (using the ‘Sign in with Apple’ button or equivalent), note that the creation of user accounts using `@privaterelay.appleid.com` addresses is not supported. Any API requests containing such emails will return an error response. To this end, and in order to ensure a smooth user experience, we request that you either implement corresponding logic to prevent the use of such email addresses, or consider removing social authentication options from your login/signup screen.


## ¶ 7.2. The URL to Your Client Area


The second URL should be for your client area.


As detailed in [**general provisions**](/Broker_SSO_OAuth/General_Provisions_Requirements/), the endpoints for all API calls made by the cTrader backend to the broker’s client area (covered in [**Section 4**](/Broker_SSO_OAuth/API_Calling_CRM/)) are relative to a specific URL denoted as `https://brokerCrmUrl.com/`.


After you provide the necessary URLs, Spotware will proceed with creating and deploying a UAT environment.


Afterward, Spotware will supply you with a fully functional set of cTrader applications that will implement SSO (OAuth) flows according to your specifications. When using these applications, you will be able to test how your login/signup screens look like and whether InApp controls perform the designated actions.


After fully testing the deployment of the SSO (OAuth) flows, contact Spotware’s Service Assurance team to inquire about the next steps in the integration process.

> After UAT is complete, you will need to provide new URLs to your login/signup screen and your client area, respectively. These URLs will be used to configure the broker SSO (OAuth) flows in your production environment.

---

## Page: Concluding Remarks
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/Concluding_Remarks*

# ¶ 8. Concluding Remarks


## ¶ 8.1. Summary of the Solution


Spotware’s broker SSO (OAuth) flows offer high-quality UX that can widen the onboarding funnel and increase live trader conversion rates. As demonstrated by this documentation, deploying this solution incurs relatively few costs. We estimate that our broker SSO (OAuth) solution should confer significant benefits to all cTrader-affiliated brokers.


## ¶ 8.2. Possible Directions for Future Development


Adding custom menu items is a possible direction for the future development of InApp controls.


Similarly to ribbons, custom menu items could be assigned with fully customisable links, icons, and InApp actions. For example, custom menu items could be used to enable users to contact their broker’s support, open a help centre page, initiate KYC checks, and request to become a partner. In our estimation, custom menu items will empower brokers to provide users with quick and easy access to several important actions.

---

## Page: Additional Error Codes
*Source: https://docs.spotware.com/en/Broker_SSO_OAuth/Additional_Error_Codes*

# ¶ 9. Additional Error Codes


The following table summarises the error codes that may be returned when attempting to verify and exchange an OT token, or validate a long-term access token.

| Error Code | Code Designation | Code Explanation |
| --- | --- | --- |
| `400` | `Bad Request` | This error occurs when at least one required field is not specified. |
| `403` | `Forbidden` | Error cases:  `CH_CLIENT_AUTH_FAILURE` occurs when access has been denied to the broker’s backend, e.g., when an invalid `password` is passed in API call 4.1. or an invalid `crmApiToken` is passed in API calls 4.2-4.4.  `CH_INSUFFICIENT_PERMISSIONS` occurs when at least one `brokerName` contained in the specified `brokerCrmName` lacks access rights because it is listed in `Bad Request`0. |
| `Bad Request`1 | `Bad Request`2 | This error occurs in the following cases: - The OT token (`Bad Request`3) passed in the request body of API call 4.2 is not found by the broker’s backend.- The long-term access token (`Bad Request`4) passed in the request body of API call 4.3 is not found by the broker’s backend.- The user identifier (`Bad Request`5) passed in the request body of API call 4.4 is not found by the broker’s backend. |
| `Bad Request`6 | `Bad Request`7 | `Bad Request`8 occurs when an expired token is used to access the broker’s backend. |
| `Bad Request`9 | `403`0 | `403`1 occurs when an invalid token is used to access the broker’s backend. |

---
