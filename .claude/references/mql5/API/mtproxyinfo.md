# MTProxyInfo

> Source: https://support.metaquotes.net/en/docs/mt5/api/mtproxyinfo

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Structures](/en/docs/mt5/api/reference_structures)MTProxyInfo

# MTProxyInfo

The MTProxyInfo structure is used for passing parameters of a proxy server. The structure is defined with the one-byte alignment.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(push,1)</span><br><span class="f_CodeExample" style="color: #0000ff;">struct</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTProxyInfo</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Types&nbsp;of&nbsp;proxy&nbsp;servers</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">enum</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">PROXY_SOCKS4</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=</span><span class="f_Indicators">0</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;SOCKS4</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">PROXY_SOCKS5</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=</span><span class="f_Indicators">1</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;SOCKS5</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">PROXY_HTTP</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=</span><span class="f_Indicators">2</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;HTTP&nbsp;(including&nbsp;NTLM)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">PROXY_FIRST</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=PROXY_SOCKS4,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;First&nbsp;type</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">PROXY_LAST</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=PROXY_HTTP</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Last&nbsp;type</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">};</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Description&nbsp;of&nbsp;a&nbsp;proxy&nbsp;server</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">enable</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Flag&nbsp;of&nbsp;proxy&nbsp;server&nbsp;using</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">type</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Type&nbsp;of&nbsp;a&nbsp;proxy&nbsp;server</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">wchar_t</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">address</span><span class="f_CodeExample">[64];</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;IP-address:Port&nbsp;of&nbsp;a&nbsp;proxy&nbsp;server</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">wchar_t</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">auth</span><span class="f_CodeExample">[64];</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Login:Password</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">};</span><br><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(pop)</span></p></td></tr></tbody></table>

This structure is used in the following methods:

-   [IMTAdminAPI::ProxySet](/en/docs/mt5/api/imtadminapi/imtadminapi_connection/imtadminapi_proxyset)
-   [IMTManagerAPI:ProxySet](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_proxyset)

This structure contains an enumeration, in which types of proxy servers passed in the type parameter are described:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable">PROXY_SOCKS4</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Type SOCKS4.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable">PROXY_SOCKS5</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Type SOCKS5.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable">PROXY_HTTP</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">2</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Type HTTP, including NTLM authentication.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable">PROXY_FIRST</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Beginning of enumeration. Corresponds to PROXY_SOCKS4.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable">PROXY_LAST</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">End of enumeration. Corresponds to PROXY_HTTP.</span></p></td></tr></tbody></table>

The structure contains the following parameters:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:115px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:115px;"><p class="p_fortable"><span class="f_fortable">enable</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">int</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A flag of connection through a proxy server. 0 — proxy server is not used, 1 — connection through a proxy server.</span></p></td></tr><tr class="table"><td class="table" style="width:115px;"><p class="p_fortable"><span class="f_fortable">type</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">int</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Proxy server type passed using the enumeration described above.</span></p></td></tr><tr class="table"><td class="table" style="width:115px;"><p class="p_fortable"><span class="f_fortable">address</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">wchart_t</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The IP address of the proxy server and the port number separated by a colon. For example, 192.168.0.1:3180.</span></p></td></tr><tr class="table"><td class="table" style="width:115px;"><p class="p_fortable"><span class="f_fortable">auth</span></p></td><td class="table" style="width:72px;"><p class="p_fortable"><span class="f_fortable">wchart_t</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The login and password for connecting to the proxy server, separated by a colon.</span></p></td></tr></tbody></table>

[Structures](/en/docs/mt5/api/reference_structures)

[MTLicenseCheck](/en/docs/mt5/api/mtlicensecheck)