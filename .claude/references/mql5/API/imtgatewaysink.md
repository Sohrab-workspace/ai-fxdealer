# IMTGatewaySink Interface

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewaysink

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
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
            -   [Interaction of the Platform and Gateway API](/en/docs/mt5/api/gatewayapi_interaction)
            -   [Trade Operations in Gateway API](/en/docs/mt5/api/gatewayapi_trade_processing)
            -   [Development and Debugging of Gateways](/en/docs/mt5/api/gatewayapi_develop_gateway)
            -   [Symbol and Price Translation](/en/docs/mt5/api/gatewayapi_translation)
            -   [Development of Data Feeds](/en/docs/mt5/api/gatewayapi_develop_datafeed)
            -   [.NET Implementation](/en/docs/mt5/api/gatewayapi_net)
            -   [Exported Functions](/en/docs/mt5/api/gatewayapi_exported)
            -   [CMTGatewayAPIFactory](/en/docs/mt5/api/cmtgatewayapifactory)
            -   [Main Interface](/en/docs/mt5/api/imtgatewayapi)
            -   [Event Interface](/en/docs/mt5/api/imtgatewaysink)
                -   [OnServerDisconnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserverdisconnect)
                -   [OnServerSynchronized](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversynchronized)
                -   [OnServerSymbolAdd](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversymboladd)
                -   [OnServerSymbolDelete](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversymboldelete)
                -   [OnGatewayConfig](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayconfig)
                -   [OnGatewayStart](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystart)
                -   [OnGatewayStop](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystop)
                -   [OnGatewayShutdown](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayshutdown)
                -   [OnGatewayAccountSet](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountset)
                -   [OnGatewayAccountAnswer](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountanswer)
                -   [OnDealerAnswer](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealeranswer)
                -   [OnDealerLock](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock)
                -   [HookServerConnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookserverconnect)
                -   [HookGatewayPositionsRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewaypositionsrequest)
                -   [HookGatewayPositionsCheck](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewaypositionscheck)
                -   [HookGatewayOrdersRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayordersrequest)
                -   [HookGatewayAccountRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayaccountrequest)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)Event Interface

# IMTGatewaySink Interface

IMTGatewaySink interface is used to notify on the events happening at a trading platform. It also allows to manage a platform connection to Gateway API.

IMTGatewaySink interface contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserverdisconnect" class="topiclink">OnServerDisconnect</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of the end of connection to one of the MetaTrader 5 platform components (server).</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversynchronized" class="topiclink">OnServerSynchronized</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of data synchronization between Gateway API and one of the MetaTrader 5 platform (server) components.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversymboladd" class="topiclink">OnServerSymbolAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of symbol adding.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversymboldelete" class="topiclink">OnServerSymbolDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of symbol removal.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayconfig" class="topiclink">OnGatewayConfig</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of passing a gateway/data feed own configuration from a history server connected to it.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystart" class="topiclink">OnGatewayStart</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the following event: Gateway API is synchronized with the platform and is ready for work.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystop" class="topiclink">OnGatewayStop</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">OnGatewayStart inverse events hadler. Notifies on the fact that Gateway API is not synchronized with the platform and not ready for work.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayshutdown" class="topiclink">OnGatewayShutdown</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event notifying about the trading platform shutdown or gateway/data feed disconnection.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountanswer" class="topiclink">OnGatewayAccountAnswer</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of requesting information about a client from MetaTrader 5 platform.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountset" class="topiclink">OnGatewayAccountSet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of modifying information about a client via <a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountset" class="topiclink">IMTGatewayAPI::GatewayAccountSet</a> method.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock" class="topiclink">OnDealerLock</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of capturing (blocking) of a successive trade request from a requests queue.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealeranswer" class="topiclink">OnDealerAnswer</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event notifying on a request confirmation or execution result.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookserverconnect" class="topiclink">HookServerConnect</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The hook for managing MetaTrader 5 platform components connections to Gateway API.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewaypositionsrequest" class="topiclink">HookGatewayPositionsRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The hook for receiving states of trading accounts used by the gateway to operate in an external system.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewaypositionscheck" class="topiclink">HookGatewayPositionsCheck</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Hook for positions verification. This method is reserved for future use.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayordersrequest" class="topiclink">HookGatewayOrdersRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The hook for receiving the state of the client's current pending orders in an external trading system.</span></p></td></tr><tr class="table"><td class="table" style="width:190px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayaccountrequest" class="topiclink">HookGatewayAccountRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The hook for synchronizing client's trading data with an external trading system.</span></p></td></tr></tbody></table>

[SettingsGet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_settings/imtgatewayapi_settingsget)

[OnServerDisconnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserverdisconnect)