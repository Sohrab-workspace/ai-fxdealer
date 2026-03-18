# Subscription Types

> Source: https://support.metaquotes.net/en/docs/mt5/manager/subscription_types

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
            -   [Controlling Subscriptions](/en/docs/mt5/manager/subscriptions_control)
            -   [Subscription Types](/en/docs/mt5/manager/subscription_types)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Subscriptions](/en/docs/mt5/manager/subscriptions)Subscription Types

# Subscription Types

The Subscriptions service allows brokers to sell any type of service by acting both as a convenient gallery within client terminals and as a built-in payment processor. Once a trader purchases a service, it appears in their Active Subscriptions section, and the broker is responsible for delivering it. For services that require additional handling  such as providing a personal account manager or performing currency exchanges  the broker manages the process independently. However, for two categories of services, the system supports full automation: Market Data Subscriptions and News Data Subscriptions.

## Market Data Subscriptions [#](subscription_types#quotes)

The service enables brokers to resell market data available on their trading server. The process works as follows:

-   You enter into a redistribution agreement with a market data provider (such as an exchange or trading system). Market data is intellectual property, so reselling requires proper licensing.
-   The platform administrator configures a [gateway](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways) or [data feed](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_feeds) to receive this data within the platform. The [App Store](https://support.metaquotes.net/en/market/mt5/aggregation) offers ready-made solutions for popular liquidity providers.
-   The administrator sets up [data subscriptions](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol) for specific financial instruments. Different levels of access can be offered:
    -   Delayed Data — data in the Market Watch in client terminals is shown with a delay. Order book (Depth of Market) and tick history are unavailable. Often used as a demo option.
    -   Level 1 realtime, best Bid/Ask — real-time data appears in Market Watch. Order books are not available.
    -   Level 2 realtime — includes real-time best Bid/Ask plus access to the order book.
    -   Tick history — in addition to real-time best prices, traders receive access to tick history. Such data enables more precise strategy testing.

After purchasing a subscription, traders see the corresponding instruments in Market Watch and gain access to quotes in real time or to the full historical data, depending on the subscription type.

### Access to symbols on the client terminal side [#](subscription_types#access)

Subscriptions restrict access to trading instruments within the platform. If an instrument is not linked to any subscription, access is controlled by standard [settings of the group](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols) to which the account belongs.

If a subscription exists for an instrument, data access (quotes, history, order book, tick history) depends on whether the trader has an active subscription and the associated [permissions](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission).

-   If permission settings include the trader group, then the trader will be able to access the real-time symbol data by subscription. Without a subscription, the trader will only receive [delayed data](/en/docs/mt5/manager/subscription_types#delayed). It means that you do not disable access to symbol data by setting up a subscription. Without a subscription, the trader can still receive the symbol data, but only with a delay.
-   If there are no subscriptions available to this client group, the trader will be able to receive the relevant market data without a subscription. The access will be provided in accordance with the group settings.

Example: You have a EURUSD symbol subscription with access for the 'real-usd' group.

-   A trader from the 'real-usd' group will need a subscription to receive the EURUSD data.
-   Traders from any other groups will receive the EURUSD data in accordance with the appropriate group settings, without a subscription.

If a trader has multiple overlapping subscriptions, they receive the highest level of access available. For example, if a trader has a subscription for the delayed EURUSD data and a subscription for EURUSD Level 2, then Level 2 data will be available to the trader.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Subscriptions restrict access to data that is originally available to the user group. For example, if only Forex\* symbols are available to a trader's group, then no subscription can provide access to data from the Stocks\* group.</span></p></td></tr></tbody></table>

### Licensing Control [#](subscription_types#license_control)

Each subscription allows up to three connections: one from a desktop terminal, one from a mobile terminal, and one from a web terminal. Additional connections automatically fall back to delayed data with a 15-minute lag. Accounts connected in investor mode always receive delayed data only, without tick history.

### Delayed Data [#](subscription_types#delayed)

You may provide delayed market data. For example, this option can be used for a free trial version. A certain delay in quote delivery can also be demanded by some exchanges providing data.

The default delay is 15 minutes, but this can be customized per trading instrument via the [administrator terminal](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration#delay):

![Data Delay Settings for Symbols](/en/docs/mt5/manager/img/subscriptions_delay_settings.png "Data Delay Settings for Symbols")

A delay is specified at this level, because exchanges can have different requirements for each trading instrument. Therefore, you cannot create multiple subscriptions for the same trading instrument with different delay values. The value specified in symbol settings will be applied for all subscriptions associated with this instrument.

This works as follows on the client terminal side:

-   Quotes in the Market Watch will be received with a delay.
-   Charts will be updated with a delay.
-   The current prices for positions and orders in the Trade section will be updated with a delay.
-   Profit by position and account balance will be updated at current prices, without delay.
-   The tick history is only available for the current terminal operation session (deep history is not available, regardless of the subscription settings).
-   Order books are not available.

A special indication is used in client terminals to inform traders about which data is provided with a delay:

-   Symbols in Market Watch are marked with a clock icon, and the delay value is displayed in the tooltip
-   Data delay notification is displayed on charts

![If the data is delivered with a delay, the trader will see the relevant information in the terminal](/en/docs/mt5/manager/img/subscriptions_delay_terminal.png "If the data is delivered with a delay, the trader will see the relevant information in the terminal")

## News Subscriptions [#](subscription_types#news)

The service also enables brokers to resell financial news delivered to the trading server. For example, in addition to a basic news feed, you can offer extended analytics, trading ideas, or detailed market reviews. How it works:

-   You sign a redistribution agreement with a news provider, since news content is also protected intellectual property.
-   The platform administrator configures a [gateway](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways) or [data feed](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_feeds) to receive this data within the platform. Multiple ready-made integrations are available in the [App Store](https://support.metaquotes.net/en/market/mt5/datafeeds).
-   The administrator sets up [data subscriptions](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_news).

### Access to news on the client terminal side [#](subscription_types#access_news)

Subscriptions limit access to news in the platform. A subscription is needed to access news if the following conditions are met:

-   The subscription specifies the client group.
-   The subscription includes the relevant news category and language.

If no applicable subscription exists, the news feed is delivered according to the trader's [group settings](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/groups_settings#news_mail), without requiring a subscription.

[Controlling Subscriptions](/en/docs/mt5/manager/subscriptions_control)

[App Store](/en/docs/mt5/manager/appstore)