# IMTDealSink::OnDealPerform

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealperform

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
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
            -   [Trade](/en/docs/mt5/api/reference_trading)
                -   [General Principles](/en/docs/mt5/api/reference_trading/general_concept)
                -   [Orders](/en/docs/mt5/api/reference_trading/trading_order)
                -   [Deals](/en/docs/mt5/api/reference_trading/trading_deal)
                    -   [IMTDeal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal)
                    -   [IMTDealArray](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray)
                    -   [IMTDealSink](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink)
                        -   [OnDealAdd](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealadd)
                        -   [OnDealUpdate](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealupdate)
                        -   [OnDealDelete](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealdelete)
                        -   [OnDealClean](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealclean)
                        -   [OnDealSync](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealsync)
                        -   [OnDealPerform](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealperform)
                        -   [OnDealPerformCloseBy](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealperformcloseby)
                -   [Positions](/en/docs/mt5/api/reference_trading/trading_position)
                -   [Accounts](/en/docs/mt5/api/reference_trading/user_account)
                -   [Trade Requests](/en/docs/mt5/api/reference_trading/trading_request)
                -   [Summary Positions](/en/docs/mt5/api/reference_trading/trading_summary)
                -   [Assets](/en/docs/mt5/api/reference_trading/trading_exposure)
                -   [Daily Reports](/en/docs/mt5/api/reference_trading/trading_daily)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)[Deals](/en/docs/mt5/api/reference_trading/trading_deal)[IMTDealSink](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink)OnDealPerform

# IMTDealSink::OnDealPerform

A handler of the event of execution of a deal, created using [IMTServerAPI:DealPerform\*](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealperform), [IMTAdminAPI:DealPerform\*](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_deal/imtadminapi_dealperform) or [IMTManagerAPI::DealPerform\*](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealperform) function.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTDealSink::OnDealPerform</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;deal&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTAccount*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">account</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;trading&nbsp;state&nbsp;of&nbsp;an&nbsp;accounts</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTPosition*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;final&nbsp;position</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTDealSink.OnDealPerform</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTDeal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;deal&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTAccount</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">account</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;trading&nbsp;state&nbsp;of&nbsp;an&nbsp;accounts</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTPosition</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;final&nbsp;position</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

deal

\[in\]  A pointer to the object of the executed [deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal).

account

\[in\]  A pointer to the object of the [account trading state](/en/docs/mt5/api/reference_trading/user_account/imtaccount) after the execution of the deal.

position

\[in\]  A pointer to the object of the resulting [position](/en/docs/mt5/api/reference_trading/trading_position/imtposition) after the execution of the deal. Due to architecture specifics, the position is transmitted with zero values in PriceOpen, TimeCreate and TimeCreateMsc fields.

Note

The call of the handler means that the deal has been executed and the result of its execution is already reflected on the trading account balance and the position state.

For balance operations, a pointer to the position in the 'position' parameter is equal to NULL. To deals that close positions, the position object with a zero volume is passed in the appropriate parameter.

[OnDealSync](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealsync)

[OnDealPerformCloseBy](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealperformcloseby)