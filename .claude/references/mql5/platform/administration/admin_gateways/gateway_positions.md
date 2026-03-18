# Positions

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateway_positions

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
                -   [Configuration of Gateways](/en/docs/mt5/platform/administration/admin_gateways/gateways_config)
                -   [Status](/en/docs/mt5/platform/administration/admin_gateways/gateway_status)
                -   [Journal of Gateways](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway)
                -   [Positions](/en/docs/mt5/platform/administration/admin_gateways/gateway_positions)
                -   [Setup of Routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_gateways/gateway_service)
                -   [Operation on Weekend](/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend)
                -   [Symbol and Price Translation](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Gateways](/en/docs/mt5/platform/administration/admin_gateways)Positions

# Positions

The tab is used to request the current state of positions from the trading accounts used by the gateway in an external system. Depending on the gateway tab, positions can be displayed via one or several accounts.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">This tab may be absent if the ability to request external system positions is not supported by the gateway. Also, the tab is not displayed if the gateway configuration is <a href="/en/docs/mt5/platform/administration/admin_gateways/gateways_config#common" class="topiclink">disabled</a>.</span></p></td></tr></tbody></table>

![Requesting positions](/en/docs/mt5/platform/img/gateway_positions.png "Requesting positions")

Click "Request" to view positions.

The following information is displayed for each position:

-   Symbol — [symbol](/en/docs/mt5/platform/administration/admin_symbols), for which the position is opened;
-   Type — position type, buy or sell;
-   Volume — position volume in lots;
-   Price — opening price;
-   Comment — a comment to a position.

The total line below shows the total number of positions and the time the states of positions have been fixed. Depending on the gateway (and external trading system), states of positions can be submitted either in real time mode or only at the end of a trading session.

## Context Menu [#](gateway_positions#context)

The context menu of this section allows performing the following commands:

-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — execute positions request;
-   Copy — this command is used for copying data on positions to clipboard;
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export — [export](/en/docs/mt5/platform/administration/common_info/export) requested positions as \*.HTM, \*.HTML files or \*.CSV file;
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled, the size of columns will be selected automatically;
-   Grid — show/hide grid to separate fields in the table with positions;
-   Comment — show/hide "Comment" column.

[Journal of Gateways](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway)

[Setup of Routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing)