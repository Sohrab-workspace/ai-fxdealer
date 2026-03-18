# Functions for Operations with Selected Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected

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
                -   [Common Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_network)
                -   [Configuration Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config)
                -   [Selected Symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected)
                    -   [SelectedAdd](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedadd)
                    -   [SelectedAddBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedaddbatch)
                    -   [SelectedAddAll](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedaddall)
                    -   [SelectedDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selecteddelete)
                    -   [SelectedDeleteBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selecteddeletebatch)
                    -   [SelectedDeleteAll](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selecteddeleteall)
                    -   [SelectedShift](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedshift)
                    -   [SelectedTotal](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedtotal)
                    -   [SelectedNext](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectednext)
                -   [Clients](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_clients)
                -   [Users](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user)
                -   [Online Connections](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_online)
                -   [Trade Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading)
                -   [History Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick)
                -   [Mail Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_mail)
                -   [News Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_news)
                -   [Trade Activity](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations)
                -   [Market Depth](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_book)
                -   [Summary Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_summary)
                -   [Exposure](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_exposure)
                -   [Daily Reports](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_daily)
                -   [Settings Files](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)
                -   [ECN](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)Selected Symbols

# Functions for Operations with Selected Symbols

The functions described in this section allow users to create an analogue of the "Market Watch" window in applications developed using the Manager API. The main purpose of managing the list of selected symbols is a control of the incoming price stream delivered to the application. In other words, the application only receives prices of selected symbols.

![Selected symbols in Market Watch of the MetaTrader 5 Manager Terminal](/en/docs/mt5/api/img/market_watch.png "Selected symbols in Market Watch of the MetaTrader 5 Manager Terminal")

The functions for managing the list of selected symbols perform the same actions as the context menu commands of Market Watch:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedadd" class="topiclink">SelectedAdd</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Add a symbol to the list by the name.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedaddbatch" class="topiclink">SelectedAddBatch</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Add a batch of symbols to the list of selected symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedaddall" class="topiclink">SelectedAddAll</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Add all available symbols to the list of selected symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selecteddelete" class="topiclink">SelectedDelete</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Remove a symbol from the list of selected symbols by the name or index.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selecteddeletebatch" class="topiclink">SelectedDeleteBatch</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Delete a batch of symbols from the list of selected symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selecteddeleteall" class="topiclink">SelectedDeleteAll</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Delete all symbols from the list of selected symbols</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedshift" class="topiclink">SelectedShift</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Shift a symbol in the list of selected symbols</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedtotal" class="topiclink">SelectedTotal</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Get the total number of symbols in the list of selected symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectednext" class="topiclink">SelectedNext</a></span></p></td><td class="table" style="width:545px;"><p class="p_fortable"><span class="f_fortable">Get the name of a symbol by a position in the list of selected symbols.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To work with the list of selected symbols, an application should be connected in the PUMP_MODE_SYMBOLS <a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_enpumpmodes" class="topiclink">pumping mode</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">When enabling PUMP_MODE_ORDERS and PUMP_MODE_POSITIONS pumping modes, pumping of symbols is automatically enabled, while the symbols, for which there are orders and positions, are automatically added to the list of selected symbols.</span></li></ul></td></tr></tbody></table>

[SubscriptionCfgRequestByID](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config/imtmanagerapi_config_subscription/imtmanagerapi_subscriptioncfgrequestbyid)

[SelectedAdd](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected/imtmanagerapi_selectedadd)