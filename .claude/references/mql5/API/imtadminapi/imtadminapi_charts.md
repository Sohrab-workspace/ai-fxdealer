# History Data Functions

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_charts

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
                -   [Common Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtadminapi/imtadminapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtadminapi/imtadminapi_network)
                -   [Server Management](/en/docs/mt5/api/imtadminapi/imtadminapi_server_manage)
                -   [Configuration Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_config)
                -   [Clients](/en/docs/mt5/api/imtadminapi/imtadminapi_clients)
                -   [Users](/en/docs/mt5/api/imtadminapi/imtadminapi_user)
                -   [Trade Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_trading)
                -   [Mail Database](/en/docs/mt5/api/imtadminapi/imtadminapi_mail)
                -   [News Database](/en/docs/mt5/api/imtadminapi/imtadminapi_news)
                -   [History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)
                    -   [ChartRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartrequest)
                    -   [ChartDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartdelete)
                    -   [ChartUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartupdate)
                    -   [ChartReplace](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartreplace)
                    -   [ChartSplit](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartsplit)
                -   [Tick Data](/en/docs/mt5/api/imtadminapi/imtadminapi_tick)
                -   [Settings Files](/en/docs/mt5/api/imtadminapi/imtadminapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtadminapi/imtadminapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_custom)
                -   [ECN](/en/docs/mt5/api/imtadminapi/imtadminapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtadminapi/imtadminapi_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)History Data

# History Data Functions

The MetaTrader 5 Manager API provides functions for working with historical price data of the platform that are available in the form of minute bars. They allow you to edit or delete minute bars.

Functions for working with historical data:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartrequest" class="topiclink">ChartRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Request minute bars for a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartdelete" class="topiclink">ChartDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete a bar by the symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartupdate" class="topiclink">ChartUpdate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Change historical data of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartreplace" class="topiclink">ChartReplace</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Full replacement of history data in the specified period with the passed data.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartsplit" class="topiclink">ChartSplit</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Split of the symbol's bar history.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Price data is stored on the history server in the form of one minute bars. Larger timeframes are formed on a client side from the minute bars according to the following principle: bars from the first to the last second of a period are used for calculation. For example, a H1 bar for 13:00 consists of minute bars within the range from 13:00:00 to 13:59:59.</span></p></td></tr></tbody></table>

[NewsSend](/en/docs/mt5/api/imtadminapi/imtadminapi_news/imtadminapi_newssend)

[ChartRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartrequest)