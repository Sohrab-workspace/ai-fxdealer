# Manager API Events Interface — IMTManagerSink

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagersink

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
                -   [OnConnect](/en/docs/mt5/api/imtmanagersink/imtmanagersink_onconnect)
                -   [OnDisconnect](/en/docs/mt5/api/imtmanagersink/imtmanagersink_ondisconnect)
                -   [OnTradeAccountSet](/en/docs/mt5/api/imtmanagersink/imtmanagersink_ontradeaccountset)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)Interface of Manager API Events

# Manager API Events Interface — IMTManagerSink

IMTManagerSink interface contains the following handlers:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagersink/imtmanagersink_onconnect" class="topiclink">OnConnect</a></span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">A handler that notifies of establishing/restoring a connection between the manager or administrator terminal and the server.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagersink/imtmanagersink_ondisconnect" class="topiclink">OnDisconnect</a></span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">A handler that notifies of loss of connection between the manager or administrator terminal and the server.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagersink/imtmanagersink_ontradeaccountset" class="topiclink">OnTradeAccountSet</a></span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">This handler receives <a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_trade_account/imtmanagerapi_tradeaccountset" class="topiclink">IMTManagerAPI::TradeAccountSet</a> method execution result, as well as the final status of a client entry (after the passed changes have been applied).</span></p></td></tr></tbody></table>

[OnDealerAnswer](/en/docs/mt5/api/imtdealersink/imtdealersink_ondealeranswer)

[OnConnect](/en/docs/mt5/api/imtmanagersink/imtmanagersink_onconnect)