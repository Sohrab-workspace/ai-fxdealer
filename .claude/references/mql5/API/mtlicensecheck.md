# MTLicenseCheck

> Source: https://support.metaquotes.net/en/docs/mt5/api/mtlicensecheck

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Structures](/en/docs/mt5/api/reference_structures)MTLicenseCheck

# MTLicenseCheck

The MTLicenseCheck structure is used for checking the license. The structure is defined with the one-byte alignment.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(push,1)</span><br><span class="f_CodeExample" style="color: #0000ff;">struct</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTLicenseCheck</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">wchar_t</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">name</span><span class="f_CodeExample">[128];&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Name&nbsp;of&nbsp;the&nbsp;license</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">data_reserved</span><span class="f_CodeExample">[128];&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;A&nbsp;reserved&nbsp;field&nbsp;for&nbsp;future&nbsp;use</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">char</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">random</span><span class="f_CodeExample">[256];&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;A&nbsp;random&nbsp;sequence&nbsp;for&nbsp;signature&nbsp;verification</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">random_size</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Size&nbsp;of&nbsp;the&nbsp;random&nbsp;sequence</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">retcode</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Result&nbsp;of&nbsp;the&nbsp;license&nbsp;check</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">result_reserved</span><span class="f_CodeExample">[128];&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;A&nbsp;reserved&nbsp;field&nbsp;for&nbsp;future&nbsp;use</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">char</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">sign</span><span class="f_CodeExample">[1024];&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Signature&nbsp;of&nbsp;the&nbsp;license&nbsp;check&nbsp;results</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_Reserved">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">sign_size</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Size&nbsp;of&nbsp;the&nbsp;signature&nbsp;to&nbsp;check&nbsp;the&nbsp;license</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">sign_reserved</span><span class="f_CodeExample">[64];&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;A&nbsp;reserved&nbsp;field&nbsp;for&nbsp;future&nbsp;use</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">};</span><br><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;pack(pop)</span></p></td></tr></tbody></table>

This structure is used in the following methods:

-   [IMTAdminAPI::LicenseCheck](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_licensecheck)
-   [IMTManagerAPI::LicenseCheck](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_licensecheck)
-   [IMTGatewayAPI::LicenseCheck](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_common/imtgatewayapi_licensecheck)

The structure contains the following parameters:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">name</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">wchar_t</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">License name. It is filled in by a programmer before the call of LicenseCheck.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">data_reserved</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">int</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A reserved field for future use.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">random</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">char</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A random sequence to check the license. It is filled in by a programmer before the call of LicenseCheck. The length of the random sequence must be at least 64 bytes.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">random_size</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">UINT</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The size of a random sequence. It is filled in by a programmer before the call of LicenseCheck.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">retcode</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">MTAPIRES</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The result of license verification. It is filled in by a MetaTrader 5 server after the call of LicenseCheck.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">result_reserved</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">int</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A reserved field for future use.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">sign</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">char</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Signature of the license check results. It is filled in by a MetaTrader 5 server after the call of LicenseCheck.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">sign_size</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">UINT</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The size of the signature to check the license. It is filled in by a MetaTrader 5 server after the call of LicenseCheck.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">sign_reserved</span></p></td><td class="table" style="width:90px;"><p class="p_fortable"><span class="f_fortable">int</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A reserved field for future use.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_licensecheck" class="topiclink">Server API</a> and <a href="/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_licensecheck" class="topiclink">Report API</a> also provide the possibility to control the licenses using LicenseCheck methods; MTLicenseCheck structure is not used in them, only the license name is passed. Plugins and reports work directly on the server, and thus they do not need to transmit data over the network to verify the license. Therefore, there is no need to additionally sign data using random sequences.</span></p></td></tr></tbody></table>

[MTProxyInfo](/en/docs/mt5/api/mtproxyinfo)

[MTTick](/en/docs/mt5/api/mttick)