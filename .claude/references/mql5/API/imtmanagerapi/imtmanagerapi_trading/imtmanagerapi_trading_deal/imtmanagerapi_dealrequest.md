# IMTManagerAPI::DealRequest

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequest

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
            -   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
            -   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
            -   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
            -   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
            -   [.NET Implementation](/en/docs/mt5/api/managerapi_net)
            -   [Python Implementation](/en/docs/mt5/api/managerapi_python)
            -   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
            -   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
            -   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
                -   [Common Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_network)
                -   [Configuration Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config)
                -   [Selected Symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected)
                -   [Clients](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_clients)
                -   [Users](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user)
                -   [Online Connections](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_online)
                -   [Trade Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading)
                    -   [Orders](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_order)
                    -   [Deals](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal)
                        -   [DealCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealcreate)
                        -   [DealCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealcreatearray)
                        -   [DealSubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealsubscribe)
                        -   [DealUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealunsubscribe)
                        -   [DealRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequest)
                        -   [DealRequestByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequestbygroup)
                        -   [DealRequestByGroupSymbol](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequestbygroupsymbols)
                        -   [DealRequestByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequestbylogins)
                        -   [DealRequestByLoginsSymbol](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequestbyloginssymbol)
                        -   [DealRequestByTickets](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequestbytickets)
                        -   [DealRequestPage](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequestpage)
                        -   [DealAdd](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealadd)
                        -   [DealAddBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealaddbatch)
                        -   [DealAddBatchArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealaddbatcharray)
                        -   [DealUpdate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealupdate)
                        -   [DealUpdateBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealupdatebatch)
                        -   [DealUpdateBatchArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealupdatebatcharray)
                        -   [DealDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealdelete)
                        -   [DealDeleteBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealdeletebatch)
                        -   [DealPerform](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealperform)
                        -   [DealPerformBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealperformbatch)
                        -   [DealPerformBatchArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealperformbatcharray)
                    -   [Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position)
                -   [History Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick)
                -   [Mail Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_mail)
                -   [News Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_news)
                -   [Trade Activity](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations)
                -   [Market Depth](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_book)
                -   [Summary Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_summary)
                -   [Exposure](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_exposure)
                -   [Daily Reports](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_daily)
                -   [Settings Files](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)
                -   [ECN](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_geo)
            -   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
            -   [Interface of Manager API Events](/en/docs/mt5/api/imtmanagersink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Trade Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading)[Deals](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal)DealRequest

# IMTManagerAPI::DealRequest

Get a deal by a ticket.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::DealRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">ticket</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;ticket&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.DealRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ticket</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;ticket&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTDeal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.DealRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ticket</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;The&nbsp;ticket&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

ticket

\[in\]  The number (ticket) of a deal.

deal

\[out\]  An object of a deal. The deal object must be first created using the [IMTManagerAPI::DealCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealcreate) method.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

This method copies the data of a deal with the specified ticket to the deal object.

This method cannot be called from event handlers (any methods of IMT\*Sink classes).

# IMTManagerAPI::DealRequest

Get the deals of a client in the specified date range.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::DealRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_Keywords">&nbsp;&nbsp;&nbsp;const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">from</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Beginning&nbsp;of&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">to</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;End&nbsp;of&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTDealArray*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">deals</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;array&nbsp;of&nbsp;deals</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.DealRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_Keywords">&nbsp;&nbsp;&nbsp;long&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">from</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Beginning&nbsp;of&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">to</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;End&nbsp;of&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTDealArray</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">deals</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;array&nbsp;of&nbsp;deals</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.DealRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Login</span><br><span class="f_Keywords">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">from</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Beginning&nbsp;of&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">to</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;End&nbsp;of&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\]  The login of the client, whose deals you need to get.

from

\[in\]  The beginning of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

to

\[in\]  The end of the period for which you need to get deals. The date is specified in seconds that have elapsed since 01.01.1970.

deals

\[out\]  An object of the array of deals. The deals object must be first created using the [IMTManagerAPI::DealCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealcreatearray) method.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

This method cannot be called from event handlers (any methods of IMT\*Sink classes).

[DealUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealunsubscribe)

[DealRequestByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal/imtmanagerapi_dealrequestbygroup)