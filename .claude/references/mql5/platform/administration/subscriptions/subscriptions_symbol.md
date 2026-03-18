# Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
                -   [Common](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common)
                -   [Description](/en/docs/mt5/platform/administration/subscriptions/subscriptions_description)
                -   [Permissons](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission)
                -   [Symbols](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol)
                -   [News](/en/docs/mt5/platform/administration/subscriptions/subscriptions_news)
                -   [Controlling Subscriptions](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Subscriptions](/en/docs/mt5/platform/administration/subscriptions)Symbols

# Symbols

For market data services, set the list of trading instruments in the Symbols section. After purchasing a subscription, the trader will have access to these symbols in Market Watch, including their real-time quotes and available price history.

## Preparatory Steps [#](subscriptions_symbol#prepare)

Before you start offering market data to your traders, you should configure receiving of appropriate symbol data from liquidity providers. The process is similar to adding trading symbols available to traders in the platform:

-   Create the required [symbols](/en/docs/mt5/platform/administration/admin_symbols)
-   Set up [gateways](/en/docs/mt5/platform/administration/admin_gateways) and/or [data feeds](/en/docs/mt5/platform/administration/admin_feeds) to receive appropriate symbol data.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To start offering market data, you will need to sign an agreement with appropriate exchanges and trading systems, as the data is proprietary.</span></li><li class="p_tableatten"><span class="f_tableatten">The support website <a href="https://support.metaquotes.net/en/market/mt5/aggregation" target="_blank" class="weblink">App Store</a> features a variety of solutions enabling receiving of data from popular liquidity providers.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If you are further transmitting subscription data between your servers using gateways or data feeds, enable the "<a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#subscription_data_feed" class="topiclink">Allow access to subscription data via data feeds</a>" permission in the settings of the trading account you are using for connecting to the source server.</span></li></ul></td></tr></tbody></table>

# Setup

![For market data services, set the list of trading instruments](/en/docs/mt5/platform/img/subscriptions_symbols.png "For market data services, set the list of trading instruments")

Specify the symbols and/or symbol groups which data will be available by subscription. Specify, which data will be available for each of the symbols or groups:

-   Level — data type that will be available by subscription:

-   Delayed — data in the Market Watch in client terminals will be displayed with a [delay](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol#delayed). Depth of Market and tick history will not be available.
-   Level 1 realtime, best Bid/Ask — data in the Market Watch will be displayed in real time. Depths of Market will not be available.
-   Level 2 realtime — the subscriber will receive in real time the best Bid/Ask prices in the Market Watch, as well ad the Depth of Market data.
-   Available tick history — the tick history depth that will be available by subscription.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To provide Depth of Market or tick history by subscription, the relevant data must be available in your platform (must be provided by the gateways/data feeds that you use).</span></p></td></tr></tbody></table>

## Access to symbols on the client terminal side [#](subscriptions_symbol#access)

Subscription limit general access to [trading symbols](/en/docs/mt5/platform/administration/admin_symbols) available in the platform. If a symbol is not used in subscriptions, this symbol can be accessed in a regular way — in accordance with the [settings of the group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols) to which the account belongs.

If a symbol subscription exists in the platform, then access to the symbol data (quotes, history, Depth of Market, tick history) depends on whether the subscription is available to the trader in accordance with the subscription [permission settings](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission#country_group).

-   If [permission settings](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission#country_group) include the trader's group, then the trader will be able to access the real-time symbol data by subscription. Without a subscription, the trader will only receive [delayed data](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol#delayed). It means that you do not disable access to symbol data by setting up a subscription. Without a subscription, the trader can still receive the symbol data, but only with a delay.
-   If there are no subscriptions available to this client group, the trader will be able to receive the relevant market data without a subscription. The access will be provided in accordance with the group settings.

Example: you have a EURUSD symbol subscription with access for the 'real-usd' group.

-   A trader from the 'real-usd' group will need a subscription to receive the EURUSD data.
-   Traders from any other groups will receive the EURUSD data in accordance with the appropriate group settings, without a subscription.

If the trader has multiple intersecting subscriptions, the maximum subscribed data will be available. For example, if a trader has a subscription for the delayed EURUSD data and a subscription for EURUSD Level 2, then Level 2 data will be available to the trader.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Subscriptions restrict access to data that is originally <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols" class="topiclink">available to the user group</a>. For example, if only Forex\* symbols are available to a trader's group, then no subscription can provide access to data from the Stocks\* group.</span></p></td></tr></tbody></table>

## License Control [#](subscriptions_symbol#license_control)

Each subscription allows up to three connections: one from a desktop terminal, one from a mobile terminal, and one from a web terminal. Additional connections will receive subscription data with a 15-minute delay. Accounts connected in investor mode will always receive delayed data and will not have access to tick history.

## Delayed data [#](subscriptions_symbol#delayed)

You can provide market data with a [minute delay](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol#level). For example, this can serve as a free trial version of your service. A certain delay in quote delivery can also be demanded by some exchanges providing data.

The default delay is 15 minutes, however you can override this value for each [trading instrument](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration#delay):

![Data Delay Settings for Symbols](/en/docs/mt5/platform/img/subscriptions_delay_settings.png "Data Delay Settings for Symbols")

The delay is specified at this level, because exchanges can have different requirements for each trading instrument. Therefore, you cannot create multiple subscriptions for the same trading instrument with different delay values. The value specified in symbol settings will be applied for all subscriptions connected to this instrument.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A restart of <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server" class="topiclink">access servers</a> is required for new delay settings to take effect.</span></p></td></tr></tbody></table>

This works as follows on the client terminal side:

-   Quotes in the Market Watch will be received with a delay.
-   Charts will be updated with a delay.
-   The current prices for positions and orders in the Trade section will be updated with a delay.
-   Profit by position and account balance will be updated at current prices, without delay.
-   The tick history is only available for the current terminal operation session (deep history is not available, regardless of the subscription settings).
-   Depths of Market is not be available.

A special indication is used in client terminals to inform traders about which data is provided with a delay:

-   Symbols in Market Watch are marked with a clock icon, and the delay value is displayed in the tooltip
-   Data delay notification is displayed on charts

![If the data is delivered with a delay, the trader will see the relevant information in the terminal](/en/docs/mt5/platform/img/subscriptions_delay_terminal.png "If the data is delivered with a delay, the trader will see the relevant information in the terminal")

[Permissons](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission)

[News](/en/docs/mt5/platform/administration/subscriptions/subscriptions_news)