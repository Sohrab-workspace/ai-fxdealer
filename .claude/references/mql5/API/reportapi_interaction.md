# Interaction with Servers

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_interaction

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
            -   [Purpose of the Report API](/en/docs/mt5/api/reportapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/reportapi_interaction)
            -   [Configuration of Reports](/en/docs/mt5/api/reportapi_configuration)
            -   [Request for Reports](/en/docs/mt5/api/reportapi_request)
            -   [Requirements for Modules](/en/docs/mt5/api/reportapi_requirements)
            -   [Creating a Simple Report](/en/docs/mt5/api/reportapi_simple_report)
            -   [Tabular Reports](/en/docs/mt5/api/reportapi_tables)
            -   [HTML Reports](/en/docs/mt5/api/reportapi_html)
            -   [Dashboards](/en/docs/mt5/api/reportapi_dashboards)
            -   [Templates](/en/docs/mt5/api/reportapi_html_template)
            -   [Charts](/en/docs/mt5/api/reportapi_html_charts)
            -   [Memory Management](/en/docs/mt5/api/reportapi_memory_management)
            -   [Multithreading](/en/docs/mt5/api/reportapi_multithreading)
            -   [Ready-made Examples](/en/docs/mt5/api/reportapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reportapi_entrypoints)
            -   [Report Plugin Interface](/en/docs/mt5/api/imtreportcontext)
            -   [Main Interface of Reports](/en/docs/mt5/api/imtreportapi)
            -   [Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)
            -   [Diagram Interfaces](/en/docs/mt5/api/reportapi_auxiliary)
            -   [Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)
            -   [Data Cache Interfaces](/en/docs/mt5/api/reportapi_cache)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)Interaction with Servers

# Interaction with Servers

The information provided in this section will help the developer to clearly understand how the server and the report module.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The server can only work with the modules, whose bit is the same as that of the server. The server can only work with the modules, whose bit is the same as that of the server. 64-bit servers only work with 64-bit modules, 32-bit servers — only with 32-bit report modules.</span><br><span class="f_tableatten">In connection with this feature, you should always develop report modules in two versions — the 32- and 64-bit.</span><br><span class="f_tableatten">It is recommended to give the module versions the appropriate names depending on the versions: ModuleName.dll and ModuleName64.dll. Our company is used the same naming standard.</span></li><li class="p_tableatten"><span class="f_tableatten">The modules can run only on trade servers.</span></li></ul></td></tr></tbody></table>

## Initialization of modules

The first stage of interaction is the initialization of modules:

1.  When starting the server scans its directory /reports, including all subdirectories, and finds all files with the extension DLL.
2.  The server tries to load all found dll-files and call the [MTReportAbout](/en/docs/mt5/api/reportapi_entrypoints/mtreportabout), function in them, which returns the [MTReportInfo](/en/docs/mt5/api/mtreportinfo) structure containing basic information about the module. If such a function cannot be called, then the dll-file is not a report module.
3.  One DLL module may contain several reports (up to 1024). While downloading a module, a server inquires all reports by the index (index parameter of the [MTReportAbout](/en/docs/mt5/api/reportapi_entrypoints/mtreportabout) function). Inquiry continues until [MT\_RET\_ERR\_NOTFOUND](/en/docs/mt5/api/retcodes_common) or [MT\_RET\_ERROR\_NOTIMPLEMENTED](/en/docs/mt5/api/retcodes_api) return codes are received.
4.  [MTReportInfo](/en/docs/mt5/api/mtreportinfo) informs the server about the version of the API, using which a report module was compiled. The module version must be supported by the server.  
    If the module version is not supported, then it will not be downloaded, and the appropriate entry will appear in the server log. In this case, you should update MetaTrader 5 Report API and recompile the reports module.

## Reading Configuration Files

After viewing the directory and identifying the reports modules, the server goes through all created [reports configurations](/en/docs/mt5/api/reportapi_configuration). Further the found modules are loaded only in accordance with the configurations created previously by the system administrator (via the administrator terminal).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">As compared with MetaTrader 4, in the fifth version of the platform, for each reports module you can create multiple configurations with different parameters. In such a case, the server will run several instances of the module.</span></p></td></tr></tbody></table>

## Waiting for a report request

Reports are generated at a trade server according to the request from the manager terminal. When a request comes, the [MTReportCreate](/en/docs/mt5/api/reportapi_entrypoints/mtreportcreate) function of an appropriate report module is called to create a report generation context (object of the class that realizes the [IMTReportContext](/en/docs/mt5/api/imtreportcontext) interface).

## IMTReportContext interface operation

The [IMTReportContext](/en/docs/mt5/api/imtreportcontext) interface contains two methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:71px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:71px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Release</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">This method removes the created object. In general, the API objects do not count references (AddRef). Thus, when calling the IMTReportContext::Release method, the object is unconditionally removed, and not just the access counter is decreased.</span></p></td></tr><tr class="table"><td class="table" style="width:71px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Generate</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The IMTReportContext::Generate method is called by a server for a report generation. It passes to the plugin the </span><span class="f_Keywords">IMTReportAPI*</span><span class="f_fortable"> </span><span class="f_Param">api</span><span class="f_fortable"> </span><span class="f_li">— the interface that implements the Report API (the interface used for interaction with the server).</span></p></td></tr></tbody></table>

[Purpose of the Report API](/en/docs/mt5/api/reportapi_purpose)

[Configuration of Reports](/en/docs/mt5/api/reportapi_configuration)