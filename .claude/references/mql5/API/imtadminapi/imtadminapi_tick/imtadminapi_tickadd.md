# IMTAdminAPI::TickAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_tick/imtadminapi_tickadd

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
                -   [Mail Database](/en/docs/mt5/api/imtadminapi/imtadminapi_mail)
                -   [News Database](/en/docs/mt5/api/imtadminapi/imtadminapi_news)
                -   [History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtadminapi/imtadminapi_tick)
                    -   [TickRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_tick/imtadminapi_tickrequest)
                    -   [TickRequestRaw](/en/docs/mt5/api/imtadminapi/imtadminapi_tick/imtadminapi_tickrequestraw)
                    -   [TickAdd](/en/docs/mt5/api/imtadminapi/imtadminapi_tick/imtadminapi_tickadd)
                    -   [TickReplace](/en/docs/mt5/api/imtadminapi/imtadminapi_tick/imtadminapi_tickreplace)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)[Tick Data](/en/docs/mt5/api/imtadminapi/imtadminapi_tick)TickAdd

# IMTAdminAPI::TickAdd

Add tick data for a symbol.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::TickAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;MTTickShort*&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">ticks</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Ticks&nbsp;to&nbsp;add</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ticks_total</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;number&nbsp;of&nbsp;ticks&nbsp;to&nbsp;add</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.TickAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickShort[]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">ticks</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Ticks&nbsp;to&nbsp;add</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">AdminAPI.TickAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ticks</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Ticks&nbsp;to&nbsp;add</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

symbol

\[in\]  The symbol, for which you want to update historical data.

ticks

\[in\]  An array of [MTTickShort](/en/docs/mt5/api/mttickshort) structures describing ticks to be added.

ticks\_total

\[in\]  The number of ticks to add.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

Unlike [IMTManagerAPI::TickAdd](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickadd), this method directly adds quotes to the price history rather than adding them to the price stream.

[TickRequestRaw](/en/docs/mt5/api/imtadminapi/imtadminapi_tick/imtadminapi_tickrequestraw)

[TickReplace](/en/docs/mt5/api/imtadminapi/imtadminapi_tick/imtadminapi_tickreplace)