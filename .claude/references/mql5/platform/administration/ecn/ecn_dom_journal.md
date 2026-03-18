# Market Depth Journal

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_dom_journal

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
                -   [Forming Market Depth](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation)
                -   [Market Depth Journal](/en/docs/mt5/platform/administration/ecn/ecn_dom_journal)
                -   [Order Matching](/en/docs/mt5/platform/administration/ecn/ecn_matching)
                -   [Order Execution](/en/docs/mt5/platform/administration/ecn/ecn_execution)
                -   [Price Translations](/en/docs/mt5/platform/administration/ecn/ecn_translation)
                -   [Matching History](/en/docs/mt5/platform/administration/ecn/ecn_matching_history)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[ECN](/en/docs/mt5/platform/administration/ecn)Market Depth Journal

# Market Depth Journal

The trading platform stores the Marked Depth formation history, showing what levels from what providers were accepted, what levels were rejected or merged. Since the history volume is large, the special log visualizer tool is provided for history analysis.

![Market Depth Journal](/en/docs/mt5/platform/img/ecn_dom_journal.png "Market Depth Journal")

Select the symbol, day and time, for which you want to view the history, and click "Request". After that, you will see the Market Depth status as of the initial request time. To view Market Depth changes over time, use the slider below.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Due to the large amount of information, you can request history for only one symbol and for one day at a time.</span></p></td></tr></tbody></table>

The time of the presented Market Depth state is shown below, as well as the ordinal number of the Market Depth change and the total number of changes for the selected time period.

The following Market Depth information is provided in the Journal:

-   Source — liquidity provider from which the Buy/Sell level was received. The source is the gateway configuration name. When you hover over it, a tooltip appears featuring the provider's basic information, such as the used module, the default name, the gateway ID, version of the gateway and used Gateway API.
-   Buy/Sell — the lot volume of buy/sell orders at the specified price.
-   Price — the price of Buy and Sell orders. In the "Full book" mode, the column may contain an additional price shown in brackets. This price appears if the original price was modified, for example due to [minimum spread](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#minimal_spread) settings or due to [different number of decimal places](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#digits) used in the trading platform and by the liquidity provider. This is the price, which was visible to clients.
-   Flags — additional data on the price level:

-   Liquid — the level is liquid, a trading operation (order matching) can be performed at this level.
-   Visible — the level is visible in the internal ECN order book. This flag is set only based on [price rules](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#price_rules) and does not mean that the level will be visible to traders. It means that the level can be visible to traders under certain conditions, such as compliance with the [minimum spread](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#minimal_spread) and [market depth limitation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#dom) requirements. For details, please visit the [Availability of Market Depth (order book) for clients](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation) section.
-   Tick — the level is formed at the best prices. Such a flag is provided in case the data source, for whatever reason, starts broadcasting only the best prices, without the Market Depth information.

Use the context menu to manage the Market Depth appearance. You can change the Market Depth type, choose volume mode (lots and units), as well as show and hide columns and grid. The following commands are also available in the context menu:

-   Invisible levels — show price levels, which are hidden from clients in accordance with [aggregation settings](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#price_rules).
-   Full book — show all levels, which were passed to the ECN symbol from gateways and the trading cluster in accordance with the aggregation settings.
-   Aggregated book — show the Market Depth, which is actually displayed to clients. [Minimum spread](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#minimal_spread) settings are applied to this Market Depth state, while invisible levels are hidden from it.

[Forming Market Depth](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation)

[Order Matching](/en/docs/mt5/platform/administration/ecn/ecn_matching)