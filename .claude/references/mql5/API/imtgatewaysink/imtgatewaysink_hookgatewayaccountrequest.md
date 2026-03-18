# IMTGatewaySink::HookGatewayAccountRequest

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayaccountrequest

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Event Interface](/en/docs/mt5/api/imtgatewaysink)HookGatewayAccountRequest

# IMTGatewaySink::HookGatewayAccountRequest

The hook for synchronizing MetaTrader 5 client's trading data with an external trading system. The hook is called when clicking "Synchronize" at "Account" tab of MetaTrader 5 Administrator, as well as when calling IMTAdminAPI::UserExternalSync and IMTManagerAPI::UserExternalSync methods from MetaTrader 5 Manager API.

When calling the hook, the gateway developer should decide whether orders, positions and client balance from an external system should be requested. Depending on the decision, one of [response codes](/en/docs/mt5/api/retcodes_successful) should be returned from the hook:

-   MT\_RET\_OK — if this code is returned, the developer is to call [IMTGatewayAPI::GatewayAccountAnswer](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountanswer) method that will be used to pass the response code for receiving data from an external system (MT\_RET\_OK) and the data itself, if it is received successfully. After that, the passed orders, positions and balance replace the same data for the specified client account.
-   MT\_RET\_OK\_NONE — if this code is returned, the gateway developer signalizes that the current orders, positions and client balance have already been synchronized with an external system, the new synchronization does not happen.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewaySink::HookGatewayAccountRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">account_id</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Account&nbsp;number&nbsp;in&nbsp;an&nbsp;external&nbsp;system</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewaySink.HookGatewayAccountRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">srting&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">account_id</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Account&nbsp;number&nbsp;in&nbsp;an&nbsp;external&nbsp;system</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\]  Account login, for which synchronization is performed.

\*account\_id

\[in\]  ID of the client's external trading system account, for which synchronization is performed.

Return Value

MT\_RET\_OK or MT\_RET\_OK\_NONE response code depending on whether the data is synchronized. In case of an error, the appropriate [error code](/en/docs/mt5/api/reference_retcodes) should be returned.

[HookGatewayOrdersRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayordersrequest)

[Report API](/en/docs/mt5/api/reportapi)