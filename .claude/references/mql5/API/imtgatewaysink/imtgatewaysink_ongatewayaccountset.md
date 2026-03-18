# IMTGatewayAPI::OnGatewayAccountSet

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountset

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Event Interface](/en/docs/mt5/api/imtgatewaysink)OnGatewayAccountSet

# IMTGatewayAPI::OnGatewayAccountSet

This handler receives [IMTGatewayAPI::GatewayAccountSet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountset) method execution result, as well as the final status of a client entry (after the passed changes have been applied).

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewayAPI::OnGatewayAccountSet</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;MTAPIRES</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">retcode</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Result</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">request_id</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Request&nbsp;ID</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTUser*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTAccount*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">account</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;trading&nbsp;account</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTOrderArray*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">orders</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;of&nbsp;orders</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTPositionArray*</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">positions</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Positions&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewayAPI.OnGatewayAccountSet</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTRetCode</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">retcode</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Result</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">request_id</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Request&nbsp;ID</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTUser</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTAccount</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">account</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;trading&nbsp;account</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTOrderArray</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">orders</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;of&nbsp;orders</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTPositionArray</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">positions</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Positions&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

retcode

\[in\] [IMTGatewayAPI::GatewayAccountSet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountset) execution result code. MT\_RET\_OK response code is passed if a client entry has been successfully changed. Otherwise, the appropriate [error code](/en/docs/mt5/api/reference_retcodes) is returned.

request\_id

\[in\]  Arbitrary request ID. It is used for binding the requests executed by [IMTGatewayAPI::GatewayAccountSet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountset) method and the answers received via this handler.

user

\[in\] [An object of the client record](/en/docs/mt5/api/reference_user/imtuser). [Login](/en/docs/mt5/api/reference_user/imtuser/imtuser_login) field is used in IMTUser object for identifying a user, whose data has been changed. The client external system's account number corresponding to the gateway can also be used for identification. Account in an external system can be defined using [IMTUser::ExternalAccountAdd](/en/docs/mt5/api/reference_user/imtuser/imtuser_externalaccountadd) method.

account

\[in\] [Trading account object](/en/docs/mt5/api/reference_trading/user_account/imtaccount). Only [Balance](/en/docs/mt5/api/reference_trading/user_account/imtaccount/imtaccount_balance) field is used in IMTAccount object for passing the balance value.

orders

\[in\] [An object of the array of orders](/en/docs/mt5/api/reference_trading/trading_order/imtorderarray) placed for the specified account.

positions

\[in\] [An object of the array of positions](/en/docs/mt5/api/reference_trading/trading_position/imtpositionarray) placed for the specified account.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

After a client's data is changed using [IMTGatewayAPI::GatewayAccountSet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountset) method, the status of the client's trading account, orders and positions is passed to account, orders and positions parameters.

[OnGatewayShutdown](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayshutdown)

[OnGatewayAccountAnswer](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountanswer)