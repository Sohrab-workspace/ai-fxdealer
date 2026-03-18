# Journal of Gateways

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/journal_gateway

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Gateways](/en/docs/mt5/platform/administration/admin_gateways)Journal of Gateways

# Journal of Gateways

In order to view the journal of operation of [gateways](/en/docs/mt5/platform/administration/admin_gateways), select it in the tree-like list in the left part of the terminal and go to the "Journal" tab.

![Journal of Gateways](/en/docs/mt5/platform/img/journal_gateway.png "Journal of Gateways")

Working with the journal of gateways is the same as with the server [journal](/en/docs/mt5/platform/administration/admin_network/network_journal). To request logs, specify a keyword, time period and click "Request".

## Extended Logging [#](journal_gateway#extended)

Extended logging mode can be enabled in ["Monitoring"](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#monitoring) tab of the gateway settings. This allows receiving more detailed data on the gateway operation.

### Measuring gateway operation speed

Result of measuring the speed of processing trade operations by the gateway is an important data displayed in the gateway journal in extended logging mode. Data on each request processing speed is shown in three journal lines:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">order&nbsp;</span><span class="f_CodeExample" style="color: #008080;">#100103556</span><span class="f_CodeExample">&nbsp;-&nbsp;process&nbsp;time:&nbsp;78.855&nbsp;ms&nbsp;(request&nbsp;process:&nbsp;12.088&nbsp;ms,&nbsp;order&nbsp;execute:&nbsp;66.767&nbsp;ms)</span><br><span class="f_CodeExample">order&nbsp;</span><span class="f_CodeExample" style="color: #008080;">#100103556</span><span class="f_CodeExample">&nbsp;-&nbsp;gateway&nbsp;API&nbsp;overhead:&nbsp;0.254&nbsp;ms&nbsp;(request&nbsp;lock:&nbsp;0.037&nbsp;ms,&nbsp;request&nbsp;confirm:&nbsp;0.027&nbsp;ms,&nbsp;execution&nbsp;process:&nbsp;0.190&nbsp;ms)</span><br><span class="f_CodeExample">order&nbsp;</span><span class="f_CodeExample" style="color: #008080;">#100103556</span><span class="f_CodeExample">&nbsp;-&nbsp;trade&nbsp;server&nbsp;response:&nbsp;10.410&nbsp;ms,&nbsp;gateway&nbsp;response:&nbsp;68.195&nbsp;ms&nbsp;(request&nbsp;response:&nbsp;1.591&nbsp;ms,&nbsp;execution&nbsp;response:&nbsp;66.604&nbsp;ms)</span></p></td></tr></tbody></table>

"Source" field of these messages contains "Monitor" indication. Order index, relative to which the measurement is performed, is shown after # mark. Let us examine each message separately.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">order&nbsp;</span><span class="f_CodeExample" style="color: #008080;">#100103556</span><span class="f_CodeExample">&nbsp;-&nbsp;process&nbsp;time:&nbsp;78.855&nbsp;ms&nbsp;(request&nbsp;process:&nbsp;12.088&nbsp;ms,&nbsp;order&nbsp;execute:&nbsp;66.767&nbsp;ms)</span></p></td></tr></tbody></table>

The following information is displayed here:

-   process time — total time of trade operation processing at the gateway. The value is calculated as the time passed from the moment when a request was transferred to the gateway up to the moment when a trade server received a notification on placing the order in an external trading system. Processing time consists of two components shown in parentheses:
-   request process — time for making a decision on how the order will be processed (for example, before receiving IMTConfirm confirmation with MT\_RET\_REQUEST\_PLACED response code meaning that the order will be processed in an external system).
-   order execute — time for placing an order in an external system (arrival of the appropriate IMTExecution trade execution).

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">order&nbsp;</span><span class="f_CodeExample" style="color: #008080;">#100103556</span><span class="f_CodeExample">&nbsp;-&nbsp;gateway&nbsp;API&nbsp;overhead:&nbsp;0.254&nbsp;ms&nbsp;(request&nbsp;lock:&nbsp;0.037&nbsp;ms,&nbsp;request&nbsp;confirm:&nbsp;0.027&nbsp;ms,&nbsp;execution&nbsp;process:&nbsp;0.190&nbsp;ms)</span></p></td></tr></tbody></table>

The following information is displayed here:

-   gateway API overhead — time spent for processing data in Gateway API. This parameter consists of three components shown in parentheses:
-   request lock — time spent by Gateway API for locking the request from the trade server's queue.
-   request confirm — time for the request confirmation processing in Gateway API (processing IMTConfirm confirmation received from the gateway).
-   execution process — time for processing the trade execution in Gateway API (processing IMTExecution trade execution received from the gateway).

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">order&nbsp;</span><span class="f_CodeExample" style="color: #008080;">#100103556</span><span class="f_CodeExample">&nbsp;-&nbsp;trade&nbsp;server&nbsp;response:&nbsp;10.410&nbsp;ms,&nbsp;gateway&nbsp;response:&nbsp;68.195&nbsp;ms&nbsp;(request&nbsp;response:&nbsp;1.591&nbsp;ms,&nbsp;execution&nbsp;response:&nbsp;66.604&nbsp;ms)</span></p></td></tr></tbody></table>

The following information is displayed here:

-   trade server response — time between sending Gateway API request for locking the trade request and receiving Gateway API server notification on locking it.
-   gateway response — total time spent waiting for a response from an external system. This parameter consists of two components shown in parentheses:
-   request response — time spent waiting for a request confirmation (for example, waiting for a confirmation that the order has been placed in an external system).
-   execution response — time spent waiting for a trade request execution (for example, filling the order in an external trading system).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">All parameters are in milliseconds.</span></li><li class="p_tableatten"><span class="f_tableatten">More information about IMTConfirm confirmation object and IMTExecution trade execution object can be found in MetaTrader 5 Gateway API documentation.</span></li></ul></td></tr></tbody></table>

## Context Menu [#](journal_gateway#context)

The context menu of the journal of gateways contains the following commands:

-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — request logs;
-   Copy — this command allows copying information from the journal to the clipboard;
-   Export — export the requested logs in a CSV or HTML file;
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — search through requested logs;
-   Auto arrange — If this option is enabled, the size of columns is selected automatically;
-   Grid — show/hide grid to separate fields;
-   Columns — show/hide columns of IP and Message in the Journal.

[Status](/en/docs/mt5/platform/administration/admin_gateways/gateway_status)

[Positions](/en/docs/mt5/platform/administration/admin_gateways/gateway_positions)