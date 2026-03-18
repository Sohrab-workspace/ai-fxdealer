# IMTServerAPI::PositionSplit

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionsplit

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
                -   [Common Functions](/en/docs/mt5/api/imtserverapi/serverapi_common)
                -   [Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)
                -   [Clients](/en/docs/mt5/api/imtserverapi/serverapi_clients)
                -   [Users](/en/docs/mt5/api/imtserverapi/serverapi_users)
                -   [Online Connections](/en/docs/mt5/api/imtserverapi/serverapi_online)
                -   [Certificates](/en/docs/mt5/api/imtserverapi/serverapi_certificate)
                -   [Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)
                    -   [Orders](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order)
                    -   [Deals](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal)
                    -   [Positions](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position)
                        -   [PositionCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positioncreate)
                        -   [PositionCreateArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positioncreatearray)
                        -   [PositionSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionsubscribe)
                        -   [PositionUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/positionunsubscribe)
                        -   [PositionDelete](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiondelete)
                        -   [PositionDeleteByTicket](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiondeletebyticket)
                        -   [PositionUpdate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionupdate)
                        -   [PositionGet](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionget)
                        -   [PositionGetByTicket](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiongetbyticket)
                        -   [PositionGetByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiongetbygroup)
                        -   [PositionGetByGroupSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiongetbygroupsymbol)
                        -   [PositionGetByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiongetbylogins)
                        -   [PositionGetByLoginsSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiongetbyloginsymbol)
                        -   [PositionGetByTickets](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positiongetbytickets)
                        -   [PositionSelectByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionselectbygroup)
                        -   [PositionSelectByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionselectbylogins)
                        -   [PositionCheck](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positioncheck)
                        -   [PositionFix](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionfix)
                        -   [PositionSplit](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionsplit)
                    -   [Trade Requests](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request)
                    -   [Request Processing](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_dealer)
                -   [History Data](/en/docs/mt5/api/imtserverapi/serverapi_chart)
                -   [Tick Data](/en/docs/mt5/api/imtserverapi/serverapi_ticks)
                -   [Depth of Market](/en/docs/mt5/api/imtserverapi/serverapi_book)
                -   [Mail Database](/en/docs/mt5/api/imtserverapi/serverapi_mail)
                -   [News Database](/en/docs/mt5/api/imtserverapi/serverapi_news)
                -   [Daily Reports](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily)
                -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_subscription)
                -   [Server Services](/en/docs/mt5/api/imtserverapi/serverapi_server_services)
                -   [Geo Services](/en/docs/mt5/api/imtserverapi/serverapi_geo)
                -   [Dataset](/en/docs/mt5/api/imtserverapi/serverapi_dataset)
                -   [Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)[Positions](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position)PositionSplit

# IMTServerAPI::PositionSplit

Split trading positions. For details please read the [MetaTrader 5 Manager Help](https://support.metaquotes.net/en/docs/mt5/manager/position_split).

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::PositionSplit</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT64*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tickets</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Tickets&nbsp;of&nbsp;positions</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tickets_total</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;tickets</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">adjustments</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Balance&nbsp;adjustments</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;new&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">old_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;old&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_price</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Price&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_volume</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">//&nbsp;Volume&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">flags</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Additional&nbsp;split&nbsp;options</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTAPIRES*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">results</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;of&nbsp;results</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTServerAPI.PositionSplit</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tickets</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Tickets&nbsp;of&nbsp;positions</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">double</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">adjustments</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Balance&nbsp;adjustments</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;new&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">old_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;old&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_price</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Price&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_volume</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">//&nbsp;Volume&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">flags</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Additional&nbsp;split&nbsp;options</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">out&nbsp;MTRetCode[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">results</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;of&nbsp;results</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

tickets

\[in\]  An array of tickets of the positions for which you want to perform the split operation.

ticket\_total

\[in\]  The number of tickets in the 'tickets' array.

adjustments

\[in\]  Adjustment calculation mode:

-   To delegate adjustment calculation to the server, pass nullptr.
-   To use custom adjustment values, pass the filled 'double' array. the array must be filled in accordance with the passed array of position tickets.
-   If no adjustment should be calculated, pass an array of zeros.

new\_shares

\[in\] Number of new shares. Shares are split/consolidated in a certain ratio, while their prices are also converted accordingly.

old\_shares

\[in\] Number of old shares. Shares are split/consolidated in a certain ratio, while their prices are also converted accordingly.

round\_rule\_price

\[in\] The price rounding rule in case the number of digital places of a new price exceeds the value set in the symbol's Digits parameter ([IMTConSymbol::Digits](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_digits)). The following three options are available:

-   0 — standard rounding
-   1 — round down
-   2 — round up

For example, when transforming the price of 35.15 with the ratio of 2:1, we obtain 17.575. When rounded down, the final price is 17.57, when rounded up, it is 17.58. The "Standard" rounding option (standard rounding to the nearest integer) is available as well. For example, if the Digits is 2, the rounding is performed as follows: 17.234 -> 17.23, 17.235 -> 17.24.

round\_rule\_volume

\[in\] The volume rounding rule in case the client will have a fractional number of shares after the split. The following three options are available:

-   0 — standard rounding
-   1 — round down
-   2 — round up

For example, dividing 35 stocks using the 3:2 ratio results in 52.5 stocks. In this case, the number may be rounded down (against a trader) or up (in a trader's favor).

flags

\[in\]  Additional split options as flags:

-   1 — it is recommended to clear trading positions' stop levels to avoid their activation after a split. This can be done by setting flag 1.
-   2 — if the split operation will cause a position volume to become less than one contract, the split operation will be not performed. You can close such positions automatically by using this flag.

results

\[in\]  An array of each position split results.

Return Value

An indication of successful command setting is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, a corresponding error code will be returned.

[PositionFix](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionfix)

[Trade Requests](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request)