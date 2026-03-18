# Development of Plugins

> Source: https://support.metaquotes.net/en/docs/mt4/api/server_api/server_api_dev

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
                -   [System Requirements](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_system_requirements)
                -   [Requirements for Plugins](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_plugin_requirements)
                -   [Configuration of Plugins](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_configuration)
                -   [Interaction with Servers](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_interaction)
                -   [Entry Points](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_entry_points)
                -   [Hooks](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_hooks)
                -   [Processing Ticks and Oders](/en/docs/mt4/api/server_api/server_api_dev/server_api_ticks_orders)
                -   [Debugging](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_debug)
                -   [Ready Examples](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_examples)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Server API](/en/docs/mt4/api/server_api)Development of Plugins

# Development of Plugins

The MetaTrader 4 Server API is a large set of intercepted functions, descriptions of data structures, used identifiers, and the virtual interface of the server. To use these features, you need to write specially designed plugin files as DLLs. The trade server automatically loads all found plugins from the predefined /plugins directory at startup.

Most of the intercepted functions are active and allow you to change or replace the standard calculation or processing mechanisms. For example, by hooking the [MtSrvTradeCommission](/en/docs/mt4/api/server_api/server_api_hook/server_api_commission_rollover/mtsrvtradecommission) function, you can completely replace the standard commission settlement mechanisms.

An important feature of the plugins is that they can hook the same function forming a chain of handlers. Multiple plugins can simultaneously serve the same requests coordinated by the server.

The API components and examples of use in C++ are provided with each licensed copy of the trade server, and are available in the /api directory. New versions of the API are added to the LiveUpdate system and are automatically downloaded together with other components.

The entire API is described in one header file \[trade server installation directory\]/api/include/mt4serverapi.h. It is updated during the server update.

-   [System Requirements](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_system_requirements)
-   [Requirements for Plugins](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_plugin_requirements)
-   [Configuration of Plugins](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_configuration)
-   [Interaction with Servers](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_interaction)
-   [Entry Points](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_entry_points)
-   [Hooks](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_hooks)
-   [Processing Ticks and Oders](/en/docs/mt4/api/server_api/server_api_dev/server_api_ticks_orders)
-   [Debugging](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_debug)
-   [Ready Examples](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_examples)

[Server API](/en/docs/mt4/api/server_api)

[System Requirements](/en/docs/mt4/api/server_api/server_api_dev/server_api_dev_system_requirements)