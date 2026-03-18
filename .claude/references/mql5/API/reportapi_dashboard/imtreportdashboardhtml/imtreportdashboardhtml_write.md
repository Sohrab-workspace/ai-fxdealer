# IMTReportDashboardHtml::Write

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_write

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
                -   [IMTReportDashboardHtml](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml)
                    -   [Assign](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_assign)
                    -   [Clear](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_clear)
                    -   [Write](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_write)
                    -   [WriteString](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_writestring)
                    -   [WriteSafe](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_writesafe)
                    -   [WriteChart](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_writechart)
                    -   [TplLoad](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplload)
                    -   [TplLoadFile](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplloadfile)
                    -   [TplLoadResource](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplloadresource)
                    -   [TplNext](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplnext)
                    -   [TplProcess](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplprocess)
                -   [IMTReportDashboardWidget](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)[IMTReportDashboardHtml](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml)Write

# IMTReportDashboardHtml::Write

Output of a line with formatting to an HTML page.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTReportDashboardHtml::Write</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">format</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;output&nbsp;line</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">...</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;optional&nbsp;arguments</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

format

\[in\]  Output line with optional arguments.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code is returned.

Note

Maximum size of an HTML part is 128 MB. When reaching the maximum size, the IMTReportDashboardHtml::Write method returns the [MT\_RET\_REPORT\_LIMIT\_REPORT](/en/docs/mt5/api/retcodes_reports) error.

Example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">value=100;</span><br><span class="f_CodeExample">Write(L</span><span class="f_CodeExample" style="color: #a31515;">"Text&nbsp;%d"</span><span class="f_CodeExample">,value);</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;This&nbsp;example&nbsp;will&nbsp;display&nbsp;"Text&nbsp;100"&nbsp;in&nbsp;the&nbsp;output&nbsp;HTML</span></p></td></tr></tbody></table>

[Clear](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_clear)

[WriteString](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_writestring)