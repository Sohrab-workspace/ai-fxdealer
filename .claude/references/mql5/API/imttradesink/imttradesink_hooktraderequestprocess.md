# IMTTradeSink::HookTradeRequestProcess

> Source: https://support.metaquotes.net/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestprocess

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
                -   [OnTradeRequestAdd](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestadd)
                -   [OnTradeRequestUpdate](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestupdate)
                -   [OnTradeRequestDelete](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestdelete)
                -   [OnTradeRequestProcess](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestprocess)
                -   [OnTradeRequestProcessCloseBy](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestprocesscloseby)
                -   [OnTradeRequestRefuse](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestrefuse)
                -   [OnTradeExecution](/en/docs/mt5/api/imttradesink/imttradesink_ontradeexecution)
                -   [OnTradeSplit](/en/docs/mt5/api/imttradesink/imttradesink_ontradesplit)
                -   [HookTradeRequestAdd](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestadd)
                -   [HookTradeRequestRoute](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestroute)
                -   [HookTradeRequestProcess](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestprocess)
                -   [HookTradeRequestProcessCloseBy](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestprocesscloseby)
                -   [HookTradeRequestRuleFilter](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestrulefilter)
                -   [HookTradeRequestRuleApply](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestrulesapply)
                -   [HookTradeRollover](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderollover)
                -   [HookTradeInterest](/en/docs/mt5/api/imttradesink/imttradesink_hooktradeinterest)
                -   [HookTradeInterestCharge](/en/docs/mt5/api/imttradesink/imttradesink_hooktradeinterestcharge)
                -   [HookTradeInterestChargeDeal](/en/docs/mt5/api/imttradesink/imttradesink_hooktradeinterestchargedeal)
                -   [HookTradeCommissionOrder](/en/docs/mt5/api/imttradesink/imttradesink_hooktradecommissionorder)
                -   [HookTradeCommissionDeal](/en/docs/mt5/api/imttradesink/imttradesink_hooktradecommissiondeal)
                -   [HookTradeCommissionCharge](/en/docs/mt5/api/imttradesink/imttradesink_hooktradecommissioncharge)
                -   [HookTradeExecution](/en/docs/mt5/api/imttradesink/imttradesink_hooktradeexecution)
                -   [HookTradeSplit](/en/docs/mt5/api/imttradesink/imttradesink_hooktradesplit)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Interface of Trade Events](/en/docs/mt5/api/imttradesink)HookTradeRequestProcess

# IMTTradeSink::HookTradeRequestProcess

A hook of [trade request](/en/docs/mt5/api/reference_trading/trading_request/imtrequest) execution.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTTradeSink::HookTradeRequestProcess</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTRequest*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">request</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;request&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConfirm*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">confirm</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;confirmation&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;group&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConSymbol*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;symbol&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTPosition*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;position&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTOrder*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;deal&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

request

\[in\]  A pointer to the object of a [trade request](/en/docs/mt5/api/reference_trading/trading_request/imtrequest).

confirm

\[in\]  A pointer to the object of [confirmation of a trade request](/en/docs/mt5/api/reference_trading/trading_request/imtconfirm), as a result of which a deal is executed.

group

\[in\]  A pointer to the object of the [configuration of the group of a client](/en/docs/mt5/api/config_group), for whom the request is being processed.

symbol

\[in\]  A pointer to the object of the [configuration of a symbol](/en/docs/mt5/api/config_symbol), which request is being processed.

position

\[in\]\[out\]  A pointer to the object of a [trade position](/en/docs/mt5/api/reference_trading/trading_position/imtposition), which corresponds to the client and symbol, for which a request is being processed. The parameter passes the future state of the position as if the processed request has been executed. Accordingly, when processing a request to completely close the position, zero values are passed in the object for all fields except direction and symbol, since the request results in the position liquidation. For more data on the position, use [IMTServerAPI::PositionGet](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionget) or [IMTServerAPI::PositionGetByTicket](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiongetbyticket).

order

\[in\]\[out\]  A pointer to the object of a [trade order](/en/docs/mt5/api/reference_trading/trading_order/imtorder), which corresponds to the request being processed: a newly created or modified order.

deal

\[in\]\[out\]  A pointer to the object of a [trade deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal) created as a result of the execution of a trade request.

Return Value

In case of confirmation [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) should be returned, otherwise, the request will be rejected with a response code returned from the hook.

Note

Depending on the request type, parameters symbol, position and order can be equal to NULL.

Note that after the execution of a specified order, a deal and a position will be passed in a recalculated state. Accordingly, when modify them, you should monitor the data integrity (for example, when the price of order execution changes, you should also change the deal price and the weighted average price of the position).

During a day/month closing, trade requests are not processed by the server in order not to distort the data provided in the reports. Therefore, the HookTradeRequestProcess hook is not called at that time as well.

Example of canceling a pending order activation and removing the activated pending order

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CPluginInstance::HookTradeRequestProcess(</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTRequest*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">request,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTConfirm*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">confirm,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTConGroup*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">group,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTConSymbol*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">symbol,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTPosition*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">position,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTOrder*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">order,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTDeal*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">deal)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTAPISTR</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">str;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">IMTRequest*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new=NULL;</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;check</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(!request</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">||</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">!m_api)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_PARAMS);</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;notify</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogOK,L</span><span class="f_CodeExample" style="color: #008080;">"HookTradeRequestProcess&nbsp;New&nbsp;request:&nbsp;%s"</span><span class="f_CodeExample">,request-&gt;Print(str));</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;check&nbsp;order</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(!position)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogOK,L</span><span class="f_CodeExample" style="color: #008080;">"HookTradeRequestProcess&nbsp;position&nbsp;=&nbsp;NULL"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">else</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogOK,L</span><span class="f_CodeExample" style="color: #008080;">"HookTradeRequestProcess&nbsp;position&nbsp;=&nbsp;%s"</span><span class="f_CodeExample">,position-&gt;Print(str));</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(request-&gt;Action()==IMTRequest::TA_ACTIVATE)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogErr,L</span><span class="f_CodeExample" style="color: #008080;">"TA_ACTIVATE"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new=m_api-&gt;TradeRequestCreate();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Clear();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Login(request-&gt;Login());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Action(IMTRequest::TA_DEALER_ORD_REMOVE);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Type(request-&gt;Type());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Symbol(request-&gt;Symbol());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Order(request-&gt;Order());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Comment(L</span><span class="f_CodeExample" style="color: #008080;">"TestCancel"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;SourceLogin(</span><span class="f_CodeExample" style="color: #008000;">1001</span><span class="f_CodeExample">);&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;1001&nbsp;is&nbsp;a&nbsp;used&nbsp;dealer&nbsp;account</span><br><span class="f_CodeExample" style="color: #808080;">&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">retcodes=m_api-&gt;TradeRequest(request_new);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogOK,L</span><span class="f_CodeExample" style="color: #008080;">"[test-log]protect,&nbsp;retcodes[%u]"</span><span class="f_CodeExample">,retcodes);</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(retcodes==MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">return</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">(MT_RET_REQUEST_CANCEL);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">request_new-&gt;Release();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #808080;">//---</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_OK);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

[HookTradeRequestRoute](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestroute)

[HookTradeRequestProcessCloseBy](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestprocesscloseby)