# IMTTradeSink::OnTradeRequestAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestadd

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Interface of Trade Events](/en/docs/mt5/api/imttradesink)OnTradeRequestAdd

# IMTTradeSink::OnTradeRequestAdd

A handler of the event of adding a checked [trade request](/en/docs/mt5/api/reference_trading/trading_request/imtrequest) in the requests queue.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTTradeSink::OnTradeRequestAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTRequest*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">request</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;request&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;group&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConSymbol*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;symbol&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTPosition*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;position&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTOrder*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

request

\[in\]  A pointer to the object of a [trade request](/en/docs/mt5/api/reference_trading/trading_request/imtrequest).

group

\[in\]  A pointer to the object of the [configuration of the group](/en/docs/mt5/api/config_group) of a client, for whom the request is being processed.

symbol

\[in\]  A pointer to the object of the [configuration of a symbol](/en/docs/mt5/api/config_symbol), which request is being processed.

position

\[in\]  A pointer to the object of a [trade position](/en/docs/mt5/api/reference_trading/trading_position/imtposition), which corresponds to the client and symbol, for which a request is being processed.

order

\[in\]  A pointer to the object of a [trade order](/en/docs/mt5/api/reference_trading/trading_order/imtorder), which corresponds to the request being processed: a newly created or modified order.

Note

This method notifies that the correctness of the appropriate trade request has been check and it has been added to the trade requests queue.

Depending on the request type, parameters symbol, position and order can be equal to NULL.

[Interface of Trade Events](/en/docs/mt5/api/imttradesink)

[OnTradeRequestUpdate](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestupdate)