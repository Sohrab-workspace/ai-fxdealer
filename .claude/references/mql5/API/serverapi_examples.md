# Ready-made Examples

> Source: https://support.metaquotes.net/en/docs/mt5/api/serverapi_examples

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)Ready-made Examples

# Ready-made Examples

The installation package of the MetaTrader 5 Server API includes ready-made examples of server plugins represented as source code. Analyzing the examples will help the developer quicker understand the specifics of the Server API and implement their own plugins.

The plugin examples are located in the [/Examples](/en/docs/mt5/api/files_folders_structure#exmaples) folder of the MetaTrader 5 Server API installation directory.

-   ServerPlugin — this plugin demonstrates basic principle of working with the Server API:

-   basics of plugin making, basic concepts;
-   tracking events;
-   getting plugin parameters;
-   creation of server interfaces (objects) and working with them.

-   InterstRates — this plugin demonstrates how to subscribe to events and how to use the hooks of interest charging depending on the state of trade accounts.

-   APIExtension — example of handling custom commands sent from [Manager API](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom) and [Web API](/en/docs/mt5/api/webapi_protocol_extension). In turn, Web API and Manager API packages contain examples for sending commands handled by that plugin.
-   FeedCommission — example of implementing a custom algorithm for charging standard commissions at the end of a trading month. The plugin shows how to work with [external parameters](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_parameterget), use event handlers by the example of [IMTEndOfDaySink::OnEOMFinish](/en/docs/mt5/api/imtendofdaysink/imtendofdaysink_oneomfinish), calculate a client turnover by trades and charge the commission using a balance transaction.
-   SwapsCopier — example of using Manager API in Server API plugins. The plugin shows how to create a manager connection in a separate thread, subscribe it to symbol change events on a remote server and update swap settings of the symbols on the server, where the plugin is used.
-   StopOutReporter — the plugin sends email notifications to customers informing them of Margin Call or Stop Out on their accounts. The templates from the mc\_notify.htm and so\_notify.htm files are used for emails. During the first launch, the plugin saves them on the disk to read them afterwards. Thus, users are able to customize templates for their own needs.

-   SingleSessionPlugin — the plugin demonstrates how to limit the number of simultaneous connections per one client login.

[Debugging](/en/docs/mt5/api/serverapi_debug)

[Entry Points](/en/docs/mt5/api/reference_entrypoints)