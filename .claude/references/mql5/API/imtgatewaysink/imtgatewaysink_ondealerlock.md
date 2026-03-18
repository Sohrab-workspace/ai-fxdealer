# IMTGatewaySink::OnDealerLock

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Event Interface](/en/docs/mt5/api/imtgatewaysink)OnDealerLock

# IMTGatewaySink::OnDealerLock

A handler of the event of capturing (blocking) of a successive trade request from a requests queue.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewaySink::OnDealerLock</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;MTAPIRES</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">retcode</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Result</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTRequest*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">request</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;trade&nbsp;request</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTUser*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTAccount*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">account</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;trading&nbsp;account</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTOrder*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTPosition*</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Position&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewaySink.OnDealerLock</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTRetCoed</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">retcode</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Result</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTRequest</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">request</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;trade&nbsp;request</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTUser</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTAccount</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">account</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;trading&nbsp;account</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTOrder</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTPosition</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Position&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

retcode

\[in\]  Trading request capture [result code](/en/docs/mt5/api/reference_retcodes). [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) is returned, in case of a successful capture. Code MT\_RET\_OK\_NONE means that the request is no longer available on the trade server. For example, it could have been captured by another dealer or application.

If the return code differs from MT\_RET\_OK, then only the [IMTRequest::ID](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_id) field is guaranteed to be filled in the 'request' parameter. Other request parameters can be left blank.

request

\[in\]  Captured [trade request object](/en/docs/mt5/api/reference_trading/trading_request/imtrequest).

user

\[in\] [Client record object](/en/docs/mt5/api/reference_user/imtuser) who formed a request.

account

\[in\] [Trading account object](/en/docs/mt5/api/reference_trading/user_account/imtaccount) of the client who formed a request.

order

\[in\] [Object of the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder) that corresponds to a request.

position

\[in\]  Client [position object](/en/docs/mt5/api/reference_trading/trading_position/imtposition) by the request instrument before its execution.

Note

The method is used only for gateways.

Filling all the parameters except retcode and request depends on a gateway connection mode determined by the [IMTGatewayAPI:DealerStart](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerstart) method. Filling of some parameters may depend on the request type. For example, for [IMTRequest::TA\_SLTP](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#ta_sltp) the 'order' parameter is not filled even if [IMTGatewayAPI::DEALER\_FLAG\_ORDER](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_enum#endealerrequestflags) is enabled, since no order is created in the platform in this case.

In the 'gateway' parameter, the prices are specified with regard to the translation parameters ([IMTConGatewayTranslate](/en/docs/mt5/api/config_gateway/imtcongatewaytranslate)) set for the gateway, whereas in the 'order' and 'position' parameters, actual prices in the platform are specified (without regard to the translation parameters).

[OnDealerAnswer](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealeranswer)

[HookServerConnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookserverconnect)