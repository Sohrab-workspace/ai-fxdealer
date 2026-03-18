# MTChartBar

> Source: https://support.metaquotes.net/en/docs/mt5/api/mtchartbar

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
            -   [MTProxyInfo](/en/docs/mt5/api/mtproxyinfo)
            -   [MTLicenseCheck](/en/docs/mt5/api/mtlicensecheck)
            -   [MTTick](/en/docs/mt5/api/mttick)
            -   [MTTickShort](/en/docs/mt5/api/mttickshort)
            -   [MTTickRate](/en/docs/mt5/api/mttickrate)
            -   [MTTickStat](/en/docs/mt5/api/mttickstat)
            -   [MTMailRange](/en/docs/mt5/api/mtmailrange)
            -   [MTLogRecord](/en/docs/mt5/api/mtlogrecord)
            -   [MTChartBar](/en/docs/mt5/api/mtchartbar)
            -   [MTBookItem](/en/docs/mt5/api/mtbookitem)
            -   [MTBook/MTBookDiff](/en/docs/mt5/api/mtbook)
            -   [MTGatewayInfo](/en/docs/mt5/api/mtgatewayinfo)
            -   [MTNews](/en/docs/mt5/api/mtnews)
            -   [MTEconomicEvent](/en/docs/mt5/api/mteconomicevent)
            -   [MTReportInfo](/en/docs/mt5/api/mtreportinfo)
            -   [MTReportParam](/en/docs/mt5/api/mtreportparam)
            -   [MTReportServerInfo](/en/docs/mt5/api/mtreportserverinfo)
            -   [MTPluginInfo](/en/docs/mt5/api/mtplugininfo)
            -   [MTPluginParam](/en/docs/mt5/api/mtpluginparam)
            -   [MTServerInfo](/en/docs/mt5/api/mtserverinfo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Structures](/en/docs/mt5/api/reference_structures)MTChartBar

# MTChartBar

The MTChartBar structure describes the bar of a chart. The structure is defined with the one-byte alignment.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(push,1)</span><br><span class="f_CodeExample" style="color: #0000ff;">struct</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTChartBar</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">INT64</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">datetime</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Date&nbsp;and&nbsp;time</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;prices</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">double</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">open</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;The&nbsp;Open&nbsp;price</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">double</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">high</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;The&nbsp;High&nbsp;price</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">double</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">low</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;The&nbsp;Low&nbsp;price</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">double</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">close</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;The&nbsp;Close&nbsp;price</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;volume</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT64</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tick_volume</span><span class="f_Reserved" style="color: #000000;">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Tick&nbsp;volume</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">INT32</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">spread</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Spread</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT64</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">volume</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Volume</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">};</span><br><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(pop)</span></p></td></tr></tbody></table>

This structure is used in the following methods:

-   [IMTAdminAPI::ChartRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartrequest)
-   [IMTAdminAPI::ChartDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartdelete)
-   [IMTAdminAPI::ChartUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_charts/imtadminapi_chartupdate)
-   [IMTGatewayAPI::ChartRequest](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts/imtgatewayapi_chartrequest)
-   [IMT](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts/imtgatewayapi_chartdelete)[Gateway](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts/imtgatewayapi_chartrequest)[API::ChartDelete](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts/imtgatewayapi_chartdelete)
-   [IMT](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts/imtgatewayapi_chartupdate)[Gateway](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts/imtgatewayapi_chartrequest)[API::ChartUpdate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts/imtgatewayapi_chartupdate)
-   [IMTReportAPI::ChartHistoryGet](/en/docs/mt5/api/imtreportapi/imtreportapi_price/imtreportapi_charthistoryget)
-   [IMTServerAPI::ChartGet](/en/docs/mt5/api/imtserverapi/serverapi_chart/imtserverapi_chartget)
-   [IMTServerAPI::ChartDelete](/en/docs/mt5/api/imtserverapi/serverapi_chart/imtserverapi_chartdelete)
-   [IMTServerAPI::ChartUpdate](/en/docs/mt5/api/imtserverapi/serverapi_chart/imtserverapi_chartupdate)

The structure contains the following parameters:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">datetime</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">INT64</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Date and time of a bar in seconds that have elapsed since 01.01.1970.</span></p></td></tr><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">open</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">double</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Bar open price — price at the beginning of bar formation (beginning of a minute).</span></p></td></tr><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">high</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">double</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The highest price inside the bar.</span></p></td></tr><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">low</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">double</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The lowest price inside the bar.</span></p></td></tr><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">close</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">double</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Bar close price — price at the end of bar formation (end of the minute).</span></p></td></tr><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">tick_volume</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">UINT64</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Tick volume — number of ticks received during bar formation. The variable only counts the ticks that change the price based on which the bar is constructed (Bid or Last, depending on symbol settings). Several ticks in a row with the same price will be counted as one.</span></p></td></tr><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">spread</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">INT32</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The lowest symbol spread recorded during the bar formation time.</span></p></td></tr><tr class="table"><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">volume</span></p></td><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable">UINT64</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The real volume of trades executed during bar formation.</span></p></td></tr></tbody></table>

For more information about working with price data in the platform, please see the [Price Data](https://support.metaquotes.net/en/docs/mt5/platform/administration/common_info/price_data) and [Charts](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_charts) sections.

[MTLogRecord](/en/docs/mt5/api/mtlogrecord)

[MTBookItem](/en/docs/mt5/api/mtbookitem)