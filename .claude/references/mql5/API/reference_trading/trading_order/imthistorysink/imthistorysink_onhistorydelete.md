# IMTHistorySink::OnHistoryDelete

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistorydelete

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
                    -   [IMTOrder](/en/docs/mt5/api/reference_trading/trading_order/imtorder)
                    -   [IMTOrderArray](/en/docs/mt5/api/reference_trading/trading_order/imtorderarray)
                    -   [IMTOrderSink](/en/docs/mt5/api/reference_trading/trading_order/imtordersink)
                    -   [IMTHistorySink](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink)
                        -   [OnHistoryAdd](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistoryadd)
                        -   [OnHistoryUpdate](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistoryupdate)
                        -   [OnHistoryDelete](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistorydelete)
                        -   [OnHistoryClean](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistoryclean)
                        -   [OnHistorySync](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistorysync)
                -   [Deals](/en/docs/mt5/api/reference_trading/trading_deal)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)[Orders](/en/docs/mt5/api/reference_trading/trading_order)[IMTHistorySink](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink)OnHistoryDelete

# IMTHistorySink::OnHistoryDelete

A handler of the event of deleting a closed order.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTHistorySink::OnHistoryDelete</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTOrder*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTHistorySink.OnHistoryDelete</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTOrder&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

order

\[in\]  A pointer to the object of a deleted order.

Note

This method is used in Server API only. It is called to notify that a closed order has been deleted.

Closed orders include executed, expired and canceled orders (inactive).

[OnHistoryUpdate](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistoryupdate)

[OnHistoryClean](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistoryclean)