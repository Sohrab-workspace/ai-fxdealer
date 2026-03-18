# MetaTrader 5 Platform API Guide

> Source: https://support.metaquotes.net/en/docs/mt5/api

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

[MetaTrader 5](/en/docs/mt5)API

# MetaTrader 5 Platform API Guide

The MetaTrader 5 platform features open APIs which allow further expanding the platform capabilities, integrating with other trading systems and back-office components, as well as customizing the platform to fit specific business needs.

The platform provides five APIs and an additional option enabling real-time data export to an SQL database.

<table class="help" cellspacing="0" cellpadding="10" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; width:68px; padding:10px; border:none"><p class="p_fortable"><img class="help" alt="server-api" width="48" height="48" src="/en/docs/mt5/api/img/server-api.png"></p></td><td style="vertical-align:top; width:120px; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/serverapi" class="topiclink">Server API</a></span><br><span class="f_fortable">C++</span></p></td><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable">Set of tools for expanding functionality and customizing the MetaTrader 5 server operation logic: custom commissioning and swap calculation algorithms, routing of financial operations, and more. <a href="/en/docs/mt5/api/serverapi_examples" class="topiclink">Ready-made examples</a> for expanding the Web and Manager API protocols</span></p></td></tr><tr><td style="vertical-align:top; width:68px; padding:10px; border:none"><p class="p_fortable"><img class="help" alt="manager-api" width="48" height="48" src="/en/docs/mt5/api/img/manager-api.png"></p></td><td style="vertical-align:top; width:120px; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/managerapi" class="topiclink">Manager API</a></span><br><span class="f_fortable">C++, C#, .NET, Python</span></p></td><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable">Set of functions for developing and editing accounts, depositing and withdrawing funds, processing trade requests and managing the server settings. The API is provided as C++ interfaces (32 and 64-bit DLL library) with <a href="/en/docs/mt5/api/managerapi_examples" class="topiclink">sample source codes</a>.</span></p></td></tr><tr><td style="vertical-align:top; width:68px; padding:10px; border:none"><p class="p_fortable"><img class="help" alt="gateway-api" width="48" height="48" src="/en/docs/mt5/api/img/gateway-api.png"></p></td><td style="vertical-align:top; width:120px; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/gatewayapi" class="topiclink">Gateway API</a></span><br><span class="f_fortable">C++, C#, .NET</span></p></td><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable">Allows for the development of custom <a href="/en/docs/mt5/api/gatewayapi_develop_gateway" class="topiclink">gateways</a> and <a href="/en/docs/mt5/api/gatewayapi_develop_datafeed" class="topiclink">data sources</a> for integrating the MetaTrader 5 platform with other trading systems. The main objectives are executing and synchronizing orders and positions with an external system, developing and modifying <a href="/en/docs/mt5/api/gatewayapi_translation" class="topiclink">trading symbols</a>, providing quotes, etc.</span></p></td></tr><tr><td style="vertical-align:top; width:68px; padding:10px; border:none"><p class="p_fortable"><img class="help" alt="report-api" width="48" height="48" src="/en/docs/mt5/api/img/report-api.png"></p></td><td style="vertical-align:top; width:120px; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi" class="topiclink">Report API</a></span><br><span class="f_fortable">C++</span></p></td><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable">Set of tools for developing custom MetaTrader 5 Manager reports. To use these features, you need to write specially designed reports modules as DLLs. The API supports <a href="/en/docs/mt5/api/reportapi_multithreading" class="topiclink">multithreading</a> and <a href="/en/docs/mt5/api/reportapi_memory_management" class="topiclink">memory management</a>, allows generation of <a href="/en/docs/mt5/api/reportapi_html" class="topiclink">HTML reports</a> and contains <a href="/en/docs/mt5/api/reportapi_examples" class="topiclink">ready-made application examples</a>.</span></p></td></tr><tr><td style="vertical-align:top; width:68px; padding:10px; border:none"><p class="p_fortable"><img class="help" alt="web-api" width="48" height="48" src="/en/docs/mt5/api/img/web-api.png"></p></td><td style="vertical-align:top; width:120px; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi" class="topiclink">Web API</a></span><br><span class="f_fortable">Any language</span></p></td><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable">Provides a Rest API for integrating the MetaTrader 5 platform with web resources and other services of a company. The API allows creating and editing client trade accounts via a website, as well as deposit and withdraw funds directly from a trader's room in real time</span></p></td></tr><tr><td style="vertical-align:top; width:68px; padding:10px; border:none"><p class="p_fortable"><img class="help" alt="export-to-sql" width="48" height="48" src="/en/docs/mt5/api/img/export-to-sql.png"></p></td><td style="vertical-align:top; width:120px; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/sql_export" class="topiclink">Export to SQL</a></span><br><span class="f_fortable">MySQL, MS SQL, Oracle, FireBird</span></p></td><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><span class="f_fortable">The standard real-time export of data to an SQL database allows for generating various reports:</span></p><ul><li class="p_li"><span class="f_li">Matching orders, trades and positions with external trading systems</span></li><li class="p_li"><span class="f_li">Reports sent to regulators</span></li><li class="p_li"><span class="f_li">Risk management reports</span></li></ul><p class="p_fortable"><span class="f_fortable">This functionality is enabled by simple specification of settings for connection to DBMS via MetaTrader 5 Administrator</span></p></td></tr></tbody></table>

MetaTrader 5 API additionally provides interfaces for accessing [configurations](/en/docs/mt5/api/reference_configurations) and [databases](/en/docs/mt5/api/reference_bases), assistant [tools](/en/docs/mt5/api/reference_tools) for facilitating routine operations, and [structures](/en/docs/mt5/api/reference_structures) for transmitting data.

To get API headers, libraries, and examples, please [download MetaTrader 5 SDK](https://support.metaquotes.net/en/download/mt5).

[WebTerminal](/en/docs/mt5/platform/components/web_terminal)

[Getting Started](/en/docs/mt5/api/getting_started)