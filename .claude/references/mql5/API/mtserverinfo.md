# MTServerInfo

> Source: https://support.metaquotes.net/en/docs/mt5/api/mtserverinfo

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Structures](/en/docs/mt5/api/reference_structures)MTServerInfo

# MTServerInfo

Using the MTServerInfo structure, the server provides the plugin with the information about the trading platform and the server on which it is running. The structure is defined with the one-byte alignment.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(push,1)</span><br><span class="f_CodeExample" style="color: #0000ff;">struct</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTServerInfo</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">wchar_t</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">platform_name</span><span class="f_CodeExample">[64];&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Name&nbsp;of&nbsp;the&nbsp;platform</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">wchar_t</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">platform_owner</span><span class="f_CodeExample">[128];&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Owner&nbsp;of&nbsp;th&nbsp;eplatform</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">server_version</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Server&nbsp;version</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">server_build</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Server&nbsp;build</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">server_type</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Server&nbsp;type</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT64</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">server_id</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Server&nbsp;ID</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">reserverd</span><span class="f_CodeExample">[32];</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;A&nbsp;reserved&nbsp;field</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">};</span><br><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(pop)</span></p></td></tr></tbody></table>

This structure is used in the [IMTServerAPI::About](/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_about) method.

The structure contains the following parameters:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable">platform_name</span></p></td><td class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable">wchar_t</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Name of the platform.</span></p></td></tr><tr class="table"><td class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable">platform_owner</span></p></td><td class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable">wchar_t</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The name of the platform owner.</span></p></td></tr><tr class="table"><td class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable">server_version</span></p></td><td class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable">UINT</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Version of the server on which the plugin is running.</span></p></td></tr><tr class="table"><td class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable">server_build</span></p></td><td class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable">UINT</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Build of the server on which the plugin is running.</span></p></td></tr><tr class="table"><td class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable">server_type</span></p></td><td class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable">UINT</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Type of the server on which the plugin is running. To pass the server type, the <a href="/en/docs/mt5/api/config_network/imtconserver/imtconserver_enum#enservertypes" class="topiclink">IMTConServer::EnServerTypes</a> enumeration is used.</span></p></td></tr><tr class="table"><td class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable">server_id</span></p></td><td class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable">UINT64</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The ID of the server on which the plugin is running.</span></p></td></tr><tr class="table"><td class="table" style="width:113px;"><p class="p_fortable"><span class="f_fortable">reserved</span></p></td><td class="table" style="width:77px;"><p class="p_fortable"><span class="f_fortable">UINT</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A reserved field for future use.</span></p></td></tr></tbody></table>

[MTPluginParam](/en/docs/mt5/api/mtpluginparam)

[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)