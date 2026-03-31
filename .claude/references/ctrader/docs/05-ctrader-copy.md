# cTrader Copy — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/en/cTrader_Copy
>   - https://docs.spotware.com/en/cTrader_Copy/Glossary
>   - https://docs.spotware.com/en/cTrader_Copy/Plant_Mode
>   - https://docs.spotware.com/en/cTrader_Copy/WL_Isolation
>   - https://docs.spotware.com/cTrader_Copy/Integration
>   - https://docs.spotware.com/en/cTrader_Copy/Integration
>   - https://docs.spotware.com/en/cTrader_Copy/Embedded_Copy_Service
>   - https://docs.spotware.com/en/cTrader_Copy/API_Calls

---

## Page: cTrader Copy: Configuration Options
*Source: https://docs.spotware.com/en/cTrader_Copy*

# ¶ cTrader Copy: Configuration Options


## ¶ Introduction


cTrader Copy is a versatile and powerful platform for money managers and investors. Via cTrader Copy, skilled traders can provide strategies for other traders to invest it. When a trader invests in a strategy, they automatically copy the trades executed by the strategy provider.


Investors are free to allocate different amounts of capital into different strategies, which means that traders can create custom ‘portfolios’ containing one or more strategies that they have invested in. In turn, strategy providers may choose to charge various fees to investors, creating an additional revenue stream and incentivizing becoming a strategy provider.

> If you have access to the cBroker back office, you can learn more about cTrader Copy by watching the ‘How to Interpret Data from the Collateral Application’ video available in the Home application.


This documentation also details Spotware’s solution for [**embedding the copy service**](/cTrader_Copy/Embedded_Copy_Service) into the broker’s client area.


## ¶ General Provisions


In general, investors can allocate funds to strategies the providers of which are registered with different cTrader-affiliated brokers.

> For example, an investor registered with Broker 1 can see and allocate funds to strategies created under Broker 2, Broker 3, and Broker 4, even if these brokers exist on different plants and constitute independent business entities.


However, depending on your business needs, you may want to adjust the availability of cTrader Copy to traders registered on different plants or within the same plant but with different White Labels. Consider the examples below.


- You own a White Label that offers unique trading conditions compared to your ‘main’ brokerage (e.g., different symbols). To control Copy-related flows of funds, you could choose to isolate this WL from all other WLs on the plant and from all other plants.

- You are a White Label reseller and, as part of your risk management effort, you want to ensure what WLs have access to the Copy service and in what capacity.

- You want to encourage Copy trading only within the confines of your brokerage so that you no longer have to worry about external strategy providers or external investors.


To help you achieve your aims, Spotware provides access to three options for configuring the availability of cTrader Copy.


- Plant mode. Via this feature, you can define Copy availability at the plant level.

- WL isolation. This option allows you to determine strategy/investment availability at the level of individual WLs. WL isolation is more granular than plant mode and, as such, adds a new layer of security constraints for certain WLs within the same plant.

- Disabling Copy. If needed, you can also disable Copy entirely for individual White Labels.


## ¶ Structure of the Documentation


The documentation for cTrader Copy consists of the following sections:


- Glossary. The glossary explains the key terms used in the documentation.

- Plant mode. This section defines plant modes and what they mean to you, strategy providers and investors.

- WL isolation and disabling Copy. This section describes the different methods of WL isolation and how they work under various plant modes.

- Embedded copy service. This section introduces the embedded copy service and highlights its benefits for the broker’s client area.

- Integration. This section outlines the rules, requirements and flow steps to integrate the embedded copy service.

- API Calls. This section outlines the API calls for the embedded copy service integration.

---

## Page: Glossary
*Source: https://docs.spotware.com/en/cTrader_Copy/Glossary*

# ¶ Glossary


The documentation for cTrader Copy uses the following terms:


**cTrader Copy**. A social trading service within the cTrader platform that allows traders to choose from hundreds of successful cross-broker strategies and copy them automatically in real time.


**Strategy provider**. A trader who registers a strategy inside the cTrader Copy service.


**Strategy fees**. Predefined fees that a strategy provider takes from their investors.


**Investor**. A trader who allocates a certain amount of funds to replicate the trades performed by the strategy provider.


**Broker/White Label (WL)**. An entity whose main purpose is to segregate accounts registered on the same plant. As such, it can refer to different White Labels or jurisdictions. By default, a plant has just one White Label but new White Labels can be added on request with no restrictions.


**Collateral balance**. A special ledger the main purpose of which is to ensure that a broker can always pay the fees its investors owe to any and all strategy providers registered with other brokers.

> If you have access to the cBroker back office, you can learn more about collateral balance by watching the ‘How to Interpret Data from the Collateral Application’ video available in the Home application.


**Broker CRM**. Broker’s backend software for managing business operations, including account creation, deposits, withdrawals and KYC procedures. User registration and authorisation are required for all actions performed in this software.


**Broker’s client area**. An online portal where traders undergo registration and interact with brokerage services, integrated with the broker’s CRM system.


**cTrader backend**. Software developed by Spotware Systems Ltd for managing operations within cTrader applications, including account creation, user authorisation and more.


**SSO**. A single-entry authentication flow that allows traders, once registered in the broker’s client area, to seamlessly access the cTrader Copy service and other products while staying on the broker’s website, without needing to log in to the trading platform.


**One-time code**. A code requested by the broker’s CRM, generated by the cTrader backend, and valid for 60 seconds. Since this code can only be used once, the cTrader application exchanges it for a token.


**Token**. An authentication token used to authorise a user whenever a relevant request is received from the cTrader backend or platform.


**Environment**. A dedicated trading server that is itself an instance of the backend solution provided by Spotware. Environments can have any naming; our generic setup includes one `demo` and one `live` environment.


**Plant**. A collection of several environments. In most cases, one plant contains all environments managed by a single broker.


**Plant mode**. A configuration that defines the availability of certain strategies to investors as well as the availability of the Copy service in general.

---

## Page: Plant Mode
*Source: https://docs.spotware.com/en/cTrader_Copy/Plant_Mode*

# ¶ Plant Mode


Plant mode is a means for massively changing the rules of engagement with the Copy service. There exist three plant modes.

> cTrader Copy is a powerful tool that is in high demand among professional traders, partners, and regular investors. To leverage its entire functionality, we highly recommend choosing Full Mode as your plant mode and avoiding any restrictions at the White Label level. Any other arrangement may not generate the same revenue streams as the configuration described above.


## ¶ Full Mode


Brokers conforming to this mode operate under the conditions designated above - their traders can freely see and invest funds in strategies whose providers registered with other brokers that exist on plants with the same mode with no restrictions.

> To be eligible for this mode, a broker must have at least one `live` trading environment established and configured. The broker must have also paid its collateral balance.


As stated previously, **Full Mode** is the mode that offers the most opportunities for generating significant revenue streams originating from cTrader Copy. It provides strategy providers with a rich landscape where they attract new investors with no restrictions whereas investors can freely choose strategies to invest in based on their risk tolerance levels and other factors.


While enabling **Full Mode** requires paying your [**collateral balance**](/cTrader_Copy/Glossary), this is offset by increasing the inflows of new traders and incentivizing live account creation for investment in profitable strategies.


## ¶ Free Mode


Brokers with this mode operate under the default conditions with one notable limitation as their traders can only access and invest funds in free strategies (i.e., the strategies the providers of which do not charge any fees).


There are no restrictions on the brokers with which the providers of these strategies may be registered. Strategy providers registered on plants with this mode cannot take fees from their investors.

> To be eligible for this mode, a broker must have at least one `demo` trading environment configured and established.


In our estimation, **Free Mode** is suitable for brokers who want to test how cTrader Copy can be integrated into their existing value proposition without having to estimate collateral balance. When **Free Mode** is enabled, you do not have to worry about covering any Copy-related fees for your traders, which makes it perfect if your business is just starting to offer advanced social trading solutions. Nonetheless, staying in **Free Mode** for too long will mean offering a limited selection of strategies to investors and disallowing strategy providers to earn funds through fees, limiting your growth.


## ¶ Isolated Mode


Brokers with this mode operate outside of the general rules defined above in that their Copy service is effectively confined to just one plant and, subsequently, any White Labels that exist on said plant. The investors registered on this plant are unable to allocate funds to strategies the providers of which exist on a different plant. The strategy providers from an isolated plant cannot attain investors that exist outside of this plant.

> To be eligible for this mode, a broker must have at least one `live` trading environment established and configured.


**Isolated Mode** is the safest possible mode in the sense that all Copy-related flows of funds are constrained to just one plant and, therefore, could be easily monitored and controlled. When in **Isolated Mode**, you can always be sure that fees are transferred between White Labels whose operations you can easily influence. However, this mode imposes significant constraints on strategy/investor availability, which is why **Full Mode** is a preferable alternative.

---

## Page: WL Isolation
*Source: https://docs.spotware.com/en/cTrader_Copy/WL_Isolation*

# ¶ WL Isolation and Disabling Copy


WL isolation is a powerful risk management solution allowing for defining custom Copy-related conditions at the WL level within a single [**plant**](/cTrader_Copy/Glossary).


Note that WL isolation is independent of [**plant mode**](/cTrader_Copy/Plant_Mode). For example, while your plant mode may be **Full Mode**, you can request that some of your WLs become isolated with different modes of isolation per individual WL, in which case appropriate isolation rules will apply to them but not to any other WLs on your [**plant**](/cTrader_Copy/Glossary).

> In addition to high-level configurations of Copy, strategy creation and/or investment in strategies can also be allowed/prohibited at the level of individual account groups, in which case these settings will be combined with all other restrictions enforced at the plant or WL level.


## ¶ Defining WL Isolation and Disabling Copy


There exist three mutually exclusive modes of WL isolation.


- Strategy isolation. All strategies whose providers are registered with the isolated WL can only be followed by investors registered under the same WL. Depending on plant mode, investors registered with the isolated WL can still allocate funds to strategies from different plants and WLs.

- Investor isolation. All traders registered with the isolated WL can only invest funds in strategies whose providers are registered with the same WL. Depending on plant mode, strategy providers registered with the isolated WL can still acquire investors from different plants and WLs.

- Full isolation. This mode combines strategy isolation with investor isolation. Strategy providers registered with a fully isolated WL can only acquire investors from this WL. Simultaneously, traders belonging to the fully isolated WL can only invest funds in strategies whose providers are from the same WL.


In addition to enabling any of these modes, you can disable the availability of cTrader Copy entirely for individual White Labels as described below.


- Disabling Copy. None of the traders registered with the WL to which this setting is applied can create strategies or invest in any existing strategies regardless of their plant/WL of origin. This arrangement is mutually exclusive with any WL isolation modes.


In essence, WL isolation is a means of fine-tuning any plant mode settings you may have.

> As an illustration, your may have the Free Mode configuration. In this case, traders belonging to a WL with investor isolation would only be able to invest in free strategies created by providers registered with the same WL. Traders belonging to a different WL with strategy isolation will be able to invest in free strategies with no other WL or plant-level restrictions.

> Alternatively, you may have a plant with the Isolated Mode configuration where one of your WLs is isolated at the strategy level. Subsequently, strategy providers from this WL will only be able to attain new investors from the same WL. Investors registered with this WL will be able to allocate funds to strategies registered with the same WL as well as any other WLs that exist on the plant.


## ¶ WL Isolation and Plant Mode


The following table summarizes how WL isolation could be combined with plant mode. Note that for some of these combinations, your remaining [**collateral balance**](/cTrader_Copy/Glossary) must be greater than zero which is also mentioned in the table.

| Plant Mode | WL Isolation Mode | Collateral Required | Description |
| --- | --- | --- | --- |
| Full Mode | No isolation | Yes | There are no restrictions on strategy/investors availability. This is the recommended configuration. |
| Strategy isolation | Yes | Investors from the isolated WL can allocate funds to strategies from any other brokers (WLs) on any other plants. Strategy providers can only acquire new investors from the isolated WL. |
| Investor isolation | No | Investors can only allocate funds to strategies whose providers are from the isolated WL. Strategy providers can acquire new investors from any other brokers (WLs) on any other plants. |
| Full isolation | No | Investors can only allocate funds to strategies whose providers are from the isolated WL. Strategy providers can only acquire new investors from the isolated WL. |
| Free Mode | No isolation | No | It is only possible to create/invest in free strategies with no other restrictions. |
| Strategy isolation | No | Investors from the isolated WL can allocate funds to free strategies from any other brokers (WLs) on any other plants. Strategy providers can only create free strategies and only acquire new investors from the isolated WL. |
| Investor isolation | No | Investors can only allocate funds to free strategies whose providers are from the isolated WL. Strategy providers can only create free strategies but they can acquire new investors from any other brokers (WLs) on any other plants. |
| Full isolation | No | Investors can only allocate funds to free strategies whose providers are from the isolated WL. Strategy providers can only create free strategies and only acquire new investors from the isolated WL. |
| Isolated Mode | No isolation | No | Attaining investors is only possible within the confines of the single plant. |
| Strategy isolation | No | Investors can only allocate funds to strategies whose providers are registered on the isolated plant. Strategy providers can only acquire new investors from the isolated WL. |
| Investor isolation | No | Investors can only allocate funds to strategies whose providers are from the isolated WL. Strategy providers can only acquire new investors from the isolated plant. |
| Full isolation | No | Investors can only allocate funds to strategies whose providers are from the isolated WL. Strategy providers can only acquire new investors from the isolated WL. |


## ¶ Example of WL Isolation


The below diagram illustrates a [**plant with two environments**](/cTrader_Copy/Glossary) shared among four WLs.


Here is how cTrader Copy will work for the strategy providers and investors registered under the different WLs existing on `plantOne`.


For `brokerOne`:


- Investors can allocate funds to strategies from other plants depending on the mode of these plants. On `plantOne` they can only follow strategies originating from `brokerOne` and `brokerTwo`.

- Strategy providers can attain new investors from other plants depending on the mode of these plants. On `plantOne` they can only attain investors originating from `brokerOne` and `brokerThree`.


For `brokerOneUK`:


- Investors can only allocate funds to strategies originating from `brokerOneUK`.

- Strategy providers can only attain new investors from `brokerOne`0.


For `brokerOne`1:


- Investors can only allocate funds to strategies originating from `brokerOne`2.

- Strategy providers can attain new investors from other plants depending on the mode of these plants. On plantOne they can only attain investors originating from `brokerOne`3, `brokerOne`4, and `brokerOne`5.


For `brokerOne`6:


- Investors can allocate funds to strategies from other plants depending on the mode of these plants. On plantOne they can only follow strategies originating from `brokerOne`7, `brokerOne`8, and `brokerOne`9.

- Strategy providers can only attain new investors from `plantOne`0.


As shown above, [**plant modes**](/cTrader_Copy/Plant_Mode) and WL isolation allow for establishing granular systems of control over how strategy providers can attract new investors and how investors can allocate funds to strategies.

---

## Page: Integration
*Source: https://docs.spotware.com/cTrader_Copy/Integration*

# ¶ Integration


## ¶ Rules


Spotware’s SSO solution adheres to the following rules:


- A broker may use both methods of authorisation:

SSO (described in this document)

- Native cTrader ID authorisation for users through any branded cTrader application.


When a code request is made for SSO, the broker specifies a list of white labels (broker names) for the code. An authenticated session opened via this code will only have access to accounts belonging to the specified white labels.


- The SSO flow does not register users in the cTrader backend. Before a broker uses the SSO solution to authenticate a trader in the cTrader platform, the broker must first use a WebServices API request to register a user. The broker will then receive a userId, which can be used to request a one-time code.

- The SSO flow becomes available upon a broker’s request to support@spotware.com, provided that integration has been fully completed on the broker’s side and conformance testing has been performed by Spotware Systems.

- The broker needs to adjust their Terms of Service for Spotware to comply with GDPR.


## ¶ Requirements for the Broker’s CRM


- Support request to register a user.

- Support request to get code for the user.

- Support redirect to the cTrader platform with `authCode`, e.g.: `/copy-widget/?authCode=3b8aa6ff-ec5b-460e-a149-346e7ec2b9ff&lang=en&theme=light`, where

`authCode` is the received code.


> This code is requested by the broker’s CRM, generated by the cTrader backend, and valid for 60 seconds. Since this code can only be used once, the cTrader application exchanges it for a token.


- `lang` is the user’s preferred language

- `theme` is the UI theme (`dark` or `light`).


## ¶ Flow Steps


The scheme below illustrates the authentication flow.


- A user authenticates into the broker’s CRM.

- If the user is not registered in the cTrader platform, the broker’s CRM sends a request to register the user and receives a `userId` in response.

- The broker’s CRM sends a request for the code with the `userId` and receives the code.

- The broker’s CRM redirects the user to the cTrader application with the code set as the URL path parameter.

- The cTrader application exchanges the code for a token and then sends an authentication request with the token to create an authenticated session.


Learn more about the [**API Calls**](/cTrader_Copy/API_Calls) for integrating the copy service.

---

## Page: Embedded Copy Service
*Source: https://docs.spotware.com/en/cTrader_Copy/Embedded_Copy_Service*

# ¶ Embedded Copy Service


## ¶ Introduction


While the broker's client area handles essential functions such as client registration and interaction with brokerage services, it does not actively engage traders in trading activities or encourage retention on the broker’s website. The need for a separate set of credentials and authorisation for the trading platform introduces extra steps for traders, negatively impacting user experience and conversion rates from new clients to active traders.


## ¶ Spotware's Solution


Embedding the cTrader Copy service into the broker's client area allows brokers to effectively engage new clients in beginner-friendly trading on the spot, without leaving the broker’s website and requiring additional authorisation for the trading platform.

*
  Figure 1: Embedded cTrader Copy service*


Once cTrader Copy is integrated by the broker, the trader flow from the personal area to the social trading platform becomes seamless.

*
  Figure 2: Trader flow*


## ¶ Benefits for Brokers


Spotware's [**copy trading solution**](https://www.spotware.com/products/traders/ctrader-copy) is renowned for its vast selection of strategies, transparent strategy statistics and a fair copying model. Specifically, embedding cTrader Copy into the broker’s client area offers the following benefits to brokers.


  - Growing trading volume. Adding the cTrader Copy service to the client area, brokers unlock zero-experience and effortless trading, which inevitably boosts overall trading volume.

  - Increased trader conversion. Without multiple authorisations, the trader journey is streamlined, increasing the chances of trading activity.

  - Upgraded client area. Brokers enhance the functionality of their websites, increasing trader retention and providing more comprehensive services on the spot.

  - Reduced support load. With fewer registration steps, support requests due to authorisation issues are minimised.


Learn more about the [**integration**](/cTrader_Copy/Integration) of the copy service into your client area.

---

## Page: API Calls
*Source: https://docs.spotware.com/en/cTrader_Copy/API_Calls*

# ¶ API Calls


All API calls here are made by the broker’s backend to the cTrader backend.


## ¶ Register a User

| HTTP Method | URL |
| --- | --- |
| `POST` | `/ctid/create` |


Creates a new user entity.


**Parameters**


No parameters.


**Request Body**

| Key | Required? | Data Type | Description |
| --- | --- | --- | --- |
| `brokerName` | No | string | A unique name denoting a specific broker (including White Labels). |
| `email` | Yes | string | The email address assigned to the new user. |
| `preferredLanguage` | No | string | An Alpha-2 code denoting the preferred language of the new user. |


**Output**

> Note that there are two possible outputs depending on whether you specify a unique `email` in the request body (an email that is not used by any of the users registered on your server). If `email` is unique, the response will include all parameters from the below table. If the specified `email` is already assigned to an existing user, the output will only include the `userId` parameter.

| Key | Data Type | Description |
| --- | --- | --- |
| `userId` | integer | The unique identifier of the user entity. |
| `/ctid/create`0 | string | The nickname of the user entity. By default, `/ctid/create`1. |
| `/ctid/create`2 | string | The email assigned to the user entity. |
| `/ctid/create`3 | string | An Alpha-2 code denoting the preferred language of the user entity. |
| `/ctid/create`4 | integer | The epoch unix timestamp of the creation of the user entity. |
| `/ctid/create`5 | enum | The status of the new user entity. Possible values: - `/ctid/create`6. The default status for any new user.- `/ctid/create`7. The status denoting an existing active user who has confirmed their email address in the cTrader ecosystem. Note that only users with `/ctid/create`8 as their `/ctid/create`9 receive trading notifications in their email inbox.- `brokerName`0. The status denoting a deleted user entity.Note that receiving `brokerName`1 or `brokerName`2 in the response body would constitute unexpected behavior. |


For a JSON schema of the output, [**click here**](/WebServices_API/JSON_Schemas).


**Request Example**


```curl
curl -X POST 'https://HOST:PORT/cid/ctid/create?token=1dd4ef40-c5b3-61c0-0689-b1b40c97fadc' -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"brokerName": "BESTBROKER", "email": "president@bestbroker.com", "preferredLanguage": "EN"}'

```

**Response Examples**

- If a Unique `brokerName`3 Is Specified
- If an Existing `brokerName`4 Is Specified

---
