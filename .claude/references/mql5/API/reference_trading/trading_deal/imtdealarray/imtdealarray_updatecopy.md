# IMTDealArray::UpdateCopy

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_updatecopy

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
                        -   [Release](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_release)
                        -   [Assign](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_assign)
                        -   [Clear](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_clear)
                        -   [Add](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_add)
                        -   [AddCopy](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_addcopy)
                        -   [Delete](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_delete)
                        -   [Detach](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_detach)
                        -   [Update](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_update)
                        -   [UpdateCopy](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_updatecopy)
                        -   [Shift](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_shift)
                        -   [Total](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_total)
                        -   [Next](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_next)
                        -   [Sort](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_sort)
                        -   [Search](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_search)
                        -   [SearchGreatOrEq](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_searchgreatoreq)
                        -   [SearchGreater](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_searchgreater)
                        -   [SearchLessOrEq](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_searchlessoreq)
                        -   [SearchLess](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_searchless)
                        -   [SearchLeft](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_searchleft)
                        -   [SearchRight](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_searchright)
                    -   [IMTDealSink](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)[Deals](/en/docs/mt5/api/reference_trading/trading_deal)[IMTDealArray](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray)UpdateCopy

# IMTDealArray::UpdateCopy

Change a deal at the specified position of an array by copying the parameters of a passed object of a deal.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTDealArray::UpdateCopy</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">pos</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Position</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTDealArray.UpdateCopy</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">pos</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Position</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTDeal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

pos

\[in\]  Position of a deal in an array, starting with 0.

order

\[in\]  An object of a deal.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

This method copies the parameters of the deal object into an object of a deal at the specified position of an array.

Unlike the [IMTDealArray::Update](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_update) method, calling this method does not set any additional conditions for the control of the deal object, but is more resource-intensive, since an additional object is created.

[Update](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_update)

[Shift](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray/imtdealarray_shift)