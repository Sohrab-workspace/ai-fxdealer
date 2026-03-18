# MetaTrader 4 Server API

> Source: https://support.metaquotes.net/en/docs/mt4/api/server_api

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
            -   [Development of Plugins](/en/docs/mt4/api/server_api/server_api_dev)
            -   [Common Functions](/en/docs/mt4/api/server_api/server_api_common)
            -   [Configuration Databases](/en/docs/mt4/api/server_api/server_api_config)
            -   [Users](/en/docs/mt4/api/server_api/server_api_user)
            -   [Trading](/en/docs/mt4/api/server_api/server_api_trading)
            -   [Price Data](/en/docs/mt4/api/server_api/server_api_chart)
            -   [Mail, News and Notifications](/en/docs/mt4/api/server_api/server_api_mail_news)
            -   [Daily Reports](/en/docs/mt4/api/server_api/server_api_reference_daily)
            -   [Server Services](/en/docs/mt4/api/server_api/server_api_server_services)
            -   [Hooks](/en/docs/mt4/api/server_api/server_api_hook)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)Server API

# MetaTrader 4 Server API

The MetaTrader 4 Server API is a set of tools for extending the functionality and configuring the operation of the MetaTrader 4 server for specific needs.

Server API is a set of intercepted functions, a description of the data structure used, identifiers and virtual interface of a server. To use these features, you need to write specially designed plugin files as DLLs.

The MetaTrader 4 Server API Reference includes the following sections:

-   [Development of Plugins](/en/docs/mt4/api/server_api/server_api_dev)
-   [Common Functions](/en/docs/mt4/api/server_api/server_api_common)
-   [Configuration Databases](/en/docs/mt4/api/server_api/server_api_config)
-   [Users](/en/docs/mt4/api/server_api/server_api_user)
-   [Trading](/en/docs/mt4/api/server_api/server_api_trading)
-   [Price Data](/en/docs/mt4/api/server_api/server_api_chart)
-   [Mail and News](/en/docs/mt4/api/server_api/server_api_mail_news)
-   [Daily Reports](/en/docs/mt4/api/server_api/server_api_reference_daily)
-   [Server Services](/en/docs/mt4/api/server_api/server_api_server_services)
-   [Hooks](/en/docs/mt4/api/server_api/server_api_hook)

[Trade Requests](/en/docs/mt4/api/reference_retcodes/retcodes_trade_request)

[Development of Plugins](/en/docs/mt4/api/server_api/server_api_dev)