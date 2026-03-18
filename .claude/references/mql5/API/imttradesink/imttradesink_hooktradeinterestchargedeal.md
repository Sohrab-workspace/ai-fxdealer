# IMTTradeSink::HookTradeInterestChargeDeal

> Source: https://support.metaquotes.net/en/docs/mt5/api/imttradesink/imttradesink_hooktradeinterestchargedeal

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Interface of Trade Events](/en/docs/mt5/api/imttradesink)HookTradeInterestChargeDeal

# IMTTradeSink::HookTradeInterestChargeDeal

A hook of a balance deal for charging annual interest. A hook is called immediately prior to a balance operation.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTTradeSink::HookTradeInterestChargeDeal</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">datetime</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;time&nbsp;of&nbsp;interest&nbsp;adding</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;pointer&nbsp;to&nbsp;the&nbsp;group&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTUser*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;pointer&nbsp;to&nbsp;the&nbsp;user&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;pointer&nbsp;to&nbsp;the&nbsp;deal&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

datetime

\[in\]  The time of interest charging in seconds that have elapsed since 01.01.1970.

group

\[in\]  A pointer to the object of the [configuration of the group](/en/docs/mt5/api/config_group) of a client, for whom the interest is added.

user

\[in\]  A pointer to the [object of the client record](/en/docs/mt5/api/reference_user/imtuser), for which the interest is added.

deal

\[in/out\]  A pointer to the [object of the deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal) used to charge the annual interest.

Return Value

In case of confirmation, [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) should be returned, otherwise, the request will be rejected with a response code returned from the hook. Thus, if the response code is different from MT\_RET\_OK, the interest is not added.

Note

The hook is called after [IMTTradeSink::HookTradeInterestCharge](/en/docs/mt5/api/imttradesink/imttradesink_hooktradeinterestcharge). Unlike the latter, it allows modifying different parameters of the deal executed on a client account in addition to a charged amount. For example, it allows you to set custom comments to annual interest charging deals ([IMTDeal::Comment](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_comment)).

If the obtained response is different from MT\_RET\_OK, no annual interest is charged (even if it is confirmed in the IMTTradeSink::HookTradeInterestCharge hook). The sum of accumulated interest in the client record ([IMTUser::InterestRate](/en/docs/mt5/api/reference_user/imtuser/imtuser_interestrate)) is not reset to zero and accumulation is resumed.

[HookTradeInterestCharge](/en/docs/mt5/api/imttradesink/imttradesink_hooktradeinterestcharge)

[HookTradeCommissionOrder](/en/docs/mt5/api/imttradesink/imttradesink_hooktradecommissionorder)