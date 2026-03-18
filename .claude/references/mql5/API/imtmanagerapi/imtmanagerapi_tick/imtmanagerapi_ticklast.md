# IMTManagerAPI::TickLast

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_ticklast

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
                -   [History Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick)
                    -   [TickSubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_ticksubscribe)
                    -   [TickUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickunsubscribe)
                    -   [TickAdd](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickadd)
                    -   [TickAddBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickaddbatch)
                    -   [TickAddStat](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickaddstat)
                    -   [TickLast](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_ticklast)
                    -   [TickLastRaw](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_ticklastraw)
                    -   [TickStat](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickstat)
                    -   [TickHistoryRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickhistoryrequest)
                    -   [TickHistoryRequestRaw](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickhistoryrequestraw)
                    -   [TickHistoryAdd](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickhistoryadd)
                    -   [TickHistoryReplace](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickhistoryreplace)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Tick Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick)TickLast

# IMTManagerAPI::TickLast

Get the last quote of a symbol taking into account spread difference settings ([IMTConGroupSymbol::SpreadDiff](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_spreaddiff)) for the group of the manager account, which is used for Manager API [connection](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_connect).

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::TickLast</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickShort&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">tick</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reference&nbsp;to&nbsp;the&nbsp;quote&nbsp;structure</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.TickLast</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickShort</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tick</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Quotes&nbsp;structure</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.TickLast</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

symbol

\[in\]  The symbol, for which you need to get a quote.

tick

\[out\]  A reference to the structure describing the quote ([MTTickShort](/en/docs/mt5/api/mttickshort)).

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred, which corresponds to the response code.

Note

The symbol for which data are requested must be included into the [list of selected symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected).

# IMTManagerAPI::TickLast

Get the last quote of a symbol taking into account spread widening settings ([IMTConGroupSymbol::SpreadDiff](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_spreaddiff)) of the specified group.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::TickLast</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Group</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickShort&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">tick</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reference&nbsp;to&nbsp;the&nbsp;quote&nbsp;structure</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.TickLast</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Group</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">out&nbsp;MTTickShort&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">tick</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Quote&nbsp;structure</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.TickLast</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Group</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

symbol

\[in\]  The symbol, for which you need to get a quote.

group

\[in\]  A group, whose [spread difference settings](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_spreaddiff) are applied to the quote.

tick

\[out\]  A reference to the structure describing the quote ([MTTickShort](/en/docs/mt5/api/mttickshort)).

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred, which corresponds to the response code.

Note

The symbol for which data are requested must be included into the [list of selected symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected).

Example

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//---&nbsp;connect&nbsp;manager&nbsp;in&nbsp;the&nbsp;full&nbsp;pumping&nbsp;mode</span><br><span class="f_CodeExample">res=manager-&gt;Connect(server,login,password,L</span><span class="f_CodeExample" style="color: #008080;">""</span><span class="f_CodeExample">,IMTManagerAPI::PUMP_MODE_FULL,MT5_TIMEOUT_CONNECT);</span><br><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(res!=MT_RET_OK)</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;wprintf_s(L</span><span class="f_CodeExample" style="color: #008080;">"Manager&nbsp;connection&nbsp;failed&nbsp;(%u)\n"</span><span class="f_CodeExample">,res);</span><br><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;wprintf_s(L</span><span class="f_CodeExample" style="color: #008080;">"manager&nbsp;connected\n"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #808080;">//---</span><br><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(manager)</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">BOOL</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stop_flag=FALSE;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;LPCWSTR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;symbol=L</span><span class="f_CodeExample" style="color: #008080;">"EURUSD"</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;LPCWSTR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group=L</span><span class="f_CodeExample" style="color: #008080;">"demo\\demoforex"</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;SYSTEMTIME&nbsp;&nbsp;current_tick_time={0};</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;MTTickShort&nbsp;ticks;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;add&nbsp;the&nbsp;symbol&nbsp;to&nbsp;the&nbsp;list&nbsp;of&nbsp;selected&nbsp;symbols</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;manager-&gt;SelectedAdd(symbol);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;get&nbsp;last&nbsp;ticks&nbsp;in&nbsp;a&nbsp;loop</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">while</span><span class="f_CodeExample">(!stop_flag)</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;get&nbsp;the&nbsp;last&nbsp;tick&nbsp;considering&nbsp;the&nbsp;group&nbsp;settings</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;res=manager-&gt;TickLast(symbol,group,ticks);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;if&nbsp;the&nbsp;ticks&nbsp;has&nbsp;been&nbsp;requested&nbsp;successfully,&nbsp;print&nbsp;its&nbsp;details&nbsp;to&nbsp;the&nbsp;journal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(res==MT_RET_OK)</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SMTTime::TimeToST(ticks.</span><span class="f_CodeExample" style="color: #0000ff;">datetime</span><span class="f_CodeExample">,&nbsp;current_tick_time);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wprintf_s(L</span><span class="f_CodeExample" style="color: #008080;">"current&nbsp;tick&nbsp;time:&nbsp;%04d.%02d.%02d&nbsp;%02d:%02d:%02d&nbsp;::&nbsp;%02d\n"</span><span class="f_CodeExample">,current_tick_time.wYear,current_tick_time.wMonth,current_tick_time.wDay,current_tick_time.wHour,current_tick_time.wMinute,current_tick_time.wSecond,current_tick_time.wMilliseconds);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wprintf_s(L</span><span class="f_CodeExample" style="color: #008080;">"symbol&nbsp;%s&nbsp;TickLast:&nbsp;current&nbsp;bid&nbsp;=&nbsp;%.5lf&nbsp;current&nbsp;ask&nbsp;=&nbsp;%.5lf\n"</span><span class="f_CodeExample">,symbol,ticks.bid,ticks.ask);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wprintf_s(L</span><span class="f_CodeExample" style="color: #008080;">"symbol&nbsp;%s&nbsp;TickLast&nbsp;failed&nbsp;(%u)\n"</span><span class="f_CodeExample">,symbol,res);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;wait</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Sleep</span><span class="f_CodeExample">(1000);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span></p></td></tr></tbody></table>

[TickAddStat](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickaddstat)

[TickLastRaw](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_ticklastraw)