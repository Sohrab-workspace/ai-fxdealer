# MetaTrader 5 Manager API

> Source: https://support.metaquotes.net/en/docs/mt5/api/managerapi

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
        -   [Manager API](/en/docs/mt5/api/managerapi)
            -   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
            -   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
            -   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
            -   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
            -   [.NET Implementation](/en/docs/mt5/api/managerapi_net)
            -   [Python Implementation](/en/docs/mt5/api/managerapi_python)
            -   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
            -   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
            -   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
            -   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
            -   [Interface of Manager API Events](/en/docs/mt5/api/imtmanagersink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)Manager API

# MetaTrader 5 Manager API

The Manager API is a set of functions, a description of the data structure and identifiers used, as well as the manager and administrator interfaces. With the Manager API, you can develop our own administrator and manager tools or even your own manager terminal.

Manager API is a set of functions, a description of the data structure used, identifiers and virtual interfaces of the administrator and manager; supplied in the form of C++ interfaces, 32 and 64 bit DLL-libraries and source codes examples.

All technical details concerning interaction with the trading platform are hidden in DLL library, which gives the possibility to control integration using simple methods. Thus, developer's code does not depend on the internal changes and is always operable.

-   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
-   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
-   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
-   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
-   [Implementation in .NET](/en/docs/mt5/api/managerapi_net)
-   [Python Implementation](/en/docs/mt5/api/managerapi_python)
-   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
-   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
-   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
-   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
-   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
-   [Manager API Events Interface](/en/docs/mt5/api/imtmanagersink)

[OnEOMFinish](/en/docs/mt5/api/imtendofdaysink/imtendofdaysink_oneomfinish)

[Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)