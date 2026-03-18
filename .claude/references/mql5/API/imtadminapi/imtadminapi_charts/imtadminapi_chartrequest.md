# IMTAdminAPI::ChartRequest

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartrequest

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
                    -   [ChartRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartrequest)
                    -   [ChartDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartdelete)
                    -   [ChartUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartupdate)
                    -   [ChartReplace](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartreplace)
                    -   [ChartSplit](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartsplit)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)[History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)ChartRequest

# IMTAdminAPI::ChartRequest

Request minute bars for a symbol.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::ChartRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">from</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Beginning&nbsp;of&nbsp;the&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">to</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;End&nbsp;of&nbsp;the&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTChartBar*&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">bars</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;of&nbsp;bars</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">bars_total</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;received&nbsp;bars</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTChartBar[]&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.ChartRequest</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">from</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Beginning&nbsp;of&nbsp;the&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">to</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;End&nbsp;of&nbsp;the&nbsp;period</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTRetCode</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">res</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Response&nbsp;code</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

news

\[in\]  The symbol for which you want to request historical data (bars).

from

\[in\]  The beginning of the period for which you need to get data. The date is specified in seconds that have elapsed since 01.01.1970.

to

\[in\]  The end of the period for which you need to get data. The date is specified in seconds that have elapsed since 01.01.1970.

bars

\[out\]  An array of bars ([MTChartBar](/en/docs/mt5/api/mtchartbar) structures).

bars\_total

\[out\]  The number of obtained bars.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, a corresponding error code will be returned.

The [MT\_RET\_OK\_NONE](/en/docs/mt5/api/retcodes_successful) code means that the access server used to connect the Manager API application has not yet synchronized the data with the history server. If that is the case, perform one or several new data requests with a pause between them.

Note

Price data is stored on the history server in the form of one minute bars. Larger timeframes are formed on a client side from the minute bars according to the following principle: bars from the first to the last second of a period are used for calculation. For example, a H1 bar for 13:00 consists of minute bars within the range from 13:00:00 to 13:59:59.

The bars array that is passed by the function is sorted by the datetime field of the [MTChartBar](/en/docs/mt5/api/mtchartbar) structure.

After using, the bars array must be released using the [IMTAdminAPI::Free](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_free) method.

The manager account performing the request must have the [IMTConManager::RIGHT\_CFG\_SYMBOLS](/en/docs/mt5/api/config_manager/imtconmanager/imtconmanager_enum#enmanagerrights) and [IMTConManager::RIGHT\_CHARTS](/en/docs/mt5/api/config_manager/imtconmanager/imtconmanager_enum#enmanagerrights) permissions. In addition, the group, to which the manager belongs, must have access to the appropriate symbol ([IMTConGroup::Symbol\*](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_symboladd)). If the required permissions are not available, the method will return the [MT\_RET\_ERR\_NOTFOUND](/en/docs/mt5/api/retcodes_common) error.

This method cannot be called from event handlers (any methods of IMT\*Sink classes).

[History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)

[ChartDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartdelete)