# IMTAdminAPI::PositionSplit

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionsplit

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
                -   [Common Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtadminapi/imtadminapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtadminapi/imtadminapi_network)
                -   [Server Management](/en/docs/mt5/api/imtadminapi/imtadminapi_server_manage)
                -   [Configuration Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_config)
                -   [Clients](/en/docs/mt5/api/imtadminapi/imtadminapi_clients)
                -   [Users](/en/docs/mt5/api/imtadminapi/imtadminapi_user)
                -   [Trade Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_trading)
                    -   [Orders](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_order)
                    -   [Deals](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_deal)
                    -   [Positions](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position)
                        -   [PositionCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positioncreate)
                        -   [PositionCreateArray](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positioncreatearray)
                        -   [PositionRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionrequest)
                        -   [PositionRequestByGroup](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionrequestbygroup)
                        -   [PositionRequestByGroupSymbol](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionrequestbygroupsymbol)
                        -   [PositionRequestByLogins](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionrequestbylogins)
                        -   [PositionRequestByLoginsSymbol](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionrequestbyloginsymbol)
                        -   [PositionRequestByTickets](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionrequestbytickets)
                        -   [PositionUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionupdate)
                        -   [PositionUpdateBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionupdatebatch)
                        -   [PositionUpdateBatchArray](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionupdatebatcharray)
                        -   [PositionDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positiondelete)
                        -   [PositionDeleteByTicket](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positiondeletebyticket)
                        -   [PositionDeleteBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positiondeletebatch)
                        -   [PositionBackupList](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionbackuplist)
                        -   [PositionBackupRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionbackuprequest)
                        -   [PositionBackupRestore](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionbackuprestore)
                        -   [PositionCheck](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positioncheck)
                        -   [PositionFix](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionfix)
                        -   [PositionSplit](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionsplit)
                -   [Mail Database](/en/docs/mt5/api/imtadminapi/imtadminapi_mail)
                -   [News Database](/en/docs/mt5/api/imtadminapi/imtadminapi_news)
                -   [History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtadminapi/imtadminapi_tick)
                -   [Settings Files](/en/docs/mt5/api/imtadminapi/imtadminapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtadminapi/imtadminapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_custom)
                -   [ECN](/en/docs/mt5/api/imtadminapi/imtadminapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtadminapi/imtadminapi_geo)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)[Trade Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_trading)[Positions](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position)PositionSplit

# IMTAdminAPI::PositionSplit

Split trading positions. For details please read the [MetaTrader 5 Manager Help](https://support.metaquotes.net/en/docs/mt5/manager/position_split).

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::PositionSplit</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT64*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tickets</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Tickets&nbsp;of&nbsp;positions</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tickets_total</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;tickets</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">adjustments</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Balance&nbsp;adjustments</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;new&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">old_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;old&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_price</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Price&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_volume</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">//&nbsp;Volume&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">flags</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Additional&nbsp;split&nbsp;options</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTAPIRES*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">results</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;of&nbsp;results</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.PositionSplit</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tickets</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Tickets&nbsp;of&nbsp;positions</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">adjustments</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Balance&nbsp;adjustments</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;new&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">old_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;old&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_price</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Price&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_volume</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">//&nbsp;Volume&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">flags</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Additional&nbsp;split&nbsp;options</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTRetCode[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">results</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;of&nbsp;results</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">AdminAPI.PositionSplit</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tickets</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Tickets&nbsp;of&nbsp;positions</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">adjustments</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Balance&nbsp;adjustments</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Number&nbsp;of&nbsp;new&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">old_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Number&nbsp;of&nbsp;old&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_price</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Price&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">round_rule_volume</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">#&nbsp;Volume&nbsp;rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">flags</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Additional&nbsp;split&nbsp;options</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

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

[PositionFix](/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionfix)

[Mail Database](/en/docs/mt5/api/imtadminapi/imtadminapi_mail)