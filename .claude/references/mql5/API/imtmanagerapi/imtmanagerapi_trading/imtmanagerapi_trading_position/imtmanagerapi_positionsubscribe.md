# IMTManagerAPI::PositionSubscribe

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionsubscribe

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
                    -   [Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position)
                        -   [PositionCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positioncreate)
                        -   [PositionCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positioncreatearray)
                        -   [PositionSubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionsubscribe)
                        -   [PositionUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionunsubscribe)
                        -   [PositionGet](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionget)
                        -   [PositionGetByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiongetbygroup)
                        -   [PositionGetByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiongetbylogins)
                        -   [PositionGetByTicket](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiongetbyticket)
                        -   [PositionGetByTickets](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiongetbytickets)
                        -   [PositionGetBySymbol](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiongetbysymbol)
                        -   [PositionRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionrequest)
                        -   [PositionRequestByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionrequestbygroup)
                        -   [PositionRequestByGroupSymbol](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionrequestbygroupsymbol)
                        -   [PositionRequestByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionrequestbylogins)
                        -   [PositionRequestByLoginsSymbol](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionrequestbyloginsymbol)
                        -   [PositionRequestByTickets](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionrequestbytickets)
                        -   [PositionUpdate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionupdate)
                        -   [PositionUpdateBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionupdatebatch)
                        -   [PositionUpdateBatchArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionupdatebatcharray)
                        -   [PositionDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiondelete)
                        -   [PositionDeleteByTicket](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiondeletebyticket)
                        -   [PositionDeleteBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positiondeletebatch)
                        -   [PositionSplit](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionsplit)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Trade Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading)[Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position)PositionSubscribe

# IMTManagerAPI::PositionSubscribe

Subscribe to the events associated with changes in the database of positions.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::PositionSubscribe</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTPositionSink*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">sink</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;IMTPositionSink&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.PositionSubscribe</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTPositionSink</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">sink</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;CIMTPositionSink&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.PositionSubscribe</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">sink</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;IMTPositionSink&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

sink

\[in\]  A pointer to the object that implements the [IMTPositionSink](/en/docs/mt5/api/reference_trading/trading_position/imtpositionsink) interface.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

Subscribing to events is thread safe. One and the same interface [IMTPositionSink](/en/docs/mt5/api/reference_trading/trading_position/imtpositionsink) cannot subscribe to an event twice - in this case the response code [MT\_RET\_ERR\_DUPLICATE](/en/docs/mt5/api/retcodes_common) is returned.

To receive [IMTPositionSink::OnPositionSync](/en/docs/mt5/api/reference_trading/trading_position/imtpositionsink/imtpositionsink_onpositionsync) events, subscribe before calling the [IMTManagerAPI::Connect](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_connect) method.

The object at which sink points, must remain in the memory (must not be removed) until the call of [IMTManagerAPI::PositionUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionunsubscribe) or until the administrator interface is deleted using the [IMTManagerAPI::Release](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_release) method.

To receive events connected with position database changes, the pumping mode [IMTManagerAPI::PUMP\_MODE\_POSITIONS](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_enpumpmodes) must be enabled.

[PositionCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positioncreatearray)

[PositionUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionunsubscribe)