# Common

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_common

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Subscriptions](/en/docs/mt5/platform/administration/subscriptions)Common

# Common

Set the service name, price and payment frequency in the main section. Choose a clear and understandable name for the service.

![Common subscription settings](/en/docs/mt5/platform/img/subscriptions_common.png "Common subscription settings")

The following settings are available:

-   Name — the name of the service. It should be short and straightforward. This name will be displayed as the product name in client terminals.
-   Depends on — sets if another product subscription is required in order to subscribe to the current product. Using this option you can create product packages. For example, you can create a paid subscription for US market price data, and a dependent free subscription for Asian market data. In this case, traders having the first subscription will be able to receive the second one for free.
-   Price — subscription cost. Another function enabling separate pricing for non-professional (ordinary traders) and professional (legal entities, brokers, banks) clients is currently under development. The price from the Non-Professional fields is currently used for all subscriptions.
-   Prime cost — specify your expenses relating to the service provision. For example, if you are reselling market data, you can specify here how much you are paying for the subscription. This will allow you to build reports on the service profitability.
-   Period — the period of the subscription. If the subscription is canceled before the end of the paid period, data delivery will stop immediately, while the cost of unused time will not be refunded.
-   Free period — subscription trial period. The trading account owner can use the free period once. If the subscription period is extended after the free period (including [automatic renewals](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission#autorenew)), the appropriate amount will be paid from the user's account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To quickly create similar services, use the "<img class="help" alt="Add copy" title="Add copy" width="13" height="15" src="/en/docs/mt5/platform/img/add_copy_icon.png">Add copy" command of the context menu. Instead of creating each service from scratch, create a copy of the existing one and adjust the required parameters.</span></p></td></tr></tbody></table>

[Subscriptions](/en/docs/mt5/platform/administration/subscriptions)

[Description](/en/docs/mt5/platform/administration/subscriptions/subscriptions_description)