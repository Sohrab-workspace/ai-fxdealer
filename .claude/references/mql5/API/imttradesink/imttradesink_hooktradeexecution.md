# IMTTradeSink::HookTradeExecution

> Source: https://support.metaquotes.net/en/docs/mt5/api/imttradesink/imttradesink_hooktradeexecution

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Interface of Trade Events](/en/docs/mt5/api/imttradesink)HookTradeExecution

# IMTTradeSink::HookTradeExecution

A hook of applying a trade execution.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTTradeSink::HookTradeExecution</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConGateway*</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">gateway</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;gateway&nbsp;configuration</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTExecution*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">execution</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;trade&nbsp;execution&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;group&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConSymbol*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;symbol&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTPosition*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;position&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTOrder*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;deal&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

gateway

\[in\]  A pointer to the object of a [gateway configuration](/en/docs/mt5/api/config_gateway/imtcongateway) the trade execution is received from. This parameter is not used and is always equal to NULL.

execution

\[in\]   A pointer to the object of the [trade execution](/en/docs/mt5/api/reference_trading/trading_request/imtexecution) received.

group

\[in\]  A pointer to the object of the [configuration of the group](/en/docs/mt5/api/config_group) of a client, for whom the trade execution is being processed.

symbol

\[in\]\[out\]  A pointer to the object of the [configuration of a symbol](/en/docs/mt5/api/config_symbol), for which the trade execution is being processed.

position

\[in\]\[out\]   A pointer to the object of a [trade position](/en/docs/mt5/api/reference_trading/trading_position/imtposition), which corresponds to the client and symbol, for which the trade execution is being processed.

order

\[in\]\[out\]  A pointer to the object of a [trade order](/en/docs/mt5/api/reference_trading/trading_order/imtorder), which corresponds to the trade execution being processed.

deal

\[in\]\[out\]  A pointer to the object of a [trade deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal) created as a result of applying the trade execution.

Return Value

In case of confirmation [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) should be returned, otherwise, the trade execution be rejected with a response code returned from the hook. Thus, if the response code is different from MT\_RET\_OK, the trade execution will not be applied.

Note

Depending on the request type, parameters symbol, position and order can be equal to NULL.

Note that after applying the trade execution, a specified order, a deal and a position will be passed in a recalculated state. Accordingly, when modify them, you should monitor the data integrity (for example, when the price of order execution changes, you should also change the deal price and the weighted average price of the position).

[HookTradeCommissionCharge](/en/docs/mt5/api/imttradesink/imttradesink_hooktradecommissioncharge)

[HookTradeSplit](/en/docs/mt5/api/imttradesink/imttradesink_hooktradesplit)