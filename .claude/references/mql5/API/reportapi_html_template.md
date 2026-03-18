# Templates

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_html_template

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)Templates

# Templates

Templates can be used in MetaTrader 5 Report API to form [HTML reports](/en/docs/mt5/api/reportapi_html) and [dashboards](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml). Templates are described according to the HTML markup rules.

There is no need to use the templates, as HTML can be directly generated from the code using the [IMTReportAPI::HTMLWrite](/en/docs/mt5/api/imtreportapi/imtreportapi_html/imtreportapi_html_management/imtreportapi_htmlwrite), [IMTReportAPI::HTMLWriteSafe](/en/docs/mt5/api/imtreportapi/imtreportapi_html/imtreportapi_html_management/imtreportapi_htmlwritesafe), [IMTReportDashboardHtml::Write](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_write) and [IMTReportDashboardHtml::WriteSafe](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_writesafe) functions. But it is not recommended to use such method, as the report formatting and its logics will be mixed in the source code. Further work with such a code will be considerably complicated.

The template allows to describe the look of the report separately from the logics. Further it will allow to easily change the template formatting and the source code will be clear and comprehensible.

## Macros

Special macroses cn be used with the templates. The macroses are replaced with the report data when the report is generated.

The macros is a construction having the <mt5:random\_name> look. There are two types of macros:

-   Simple ones have the <mt5:.../> look. Simple macros do not contain embedded constructions.
-   Complex ones have the <mt5:...>...</mt5:...> look. Such macros can contain embedded constructions consisting of HTML contents or another macros.

MetaTrader 5 Report API provides two methods of the macroses processing:

-   [IMTReportAPI::HtmlTplNext](/en/docs/mt5/api/imtreportapi/imtreportapi_html/imtreportapi_html_management/imtreportapi_htmltplnext) — this method orders to get the next macros in a template.
-   [IMTReportAPI::HtmlTplProcess](/en/docs/mt5/api/imtreportapi/imtreportapi_html/imtreportapi_html_management/imtreportapi_htmltplprocess) — this method orders to process constructions embedded in a complex macros. Using complex macroses is similar to the using of the while cycle. As long as the IMTReportAPI::HtmlProcess method is called for a complex macros, its contents will be processed. When the final  </mt5:...> macros is reached, transition to the macros beginning will be performed where the decision concerning its contents processing can be made again. And the counter passed by Report API to the [IMTReportAPI::HtmlTplNext](/en/docs/mt5/api/imtreportapi/imtreportapi_html/imtreportapi_html_management/imtreportapi_htmltplnext) method will increase by one.

A similar pair of methods is available for dashboards: [IMTReportDashboardHtml::TplNext](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplnext) and [IMTReportDashboardHtml::TplProcess](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplprocess).

Using the methods of working with macroses allows to easily process and display the data arrays received from a trade server. [Example of using the macroses](/en/docs/mt5/api/reportapi_html#macro_process) is described in the section devoted to HTML reports.

[Dashboards](/en/docs/mt5/api/reportapi_dashboards)

[Charts](/en/docs/mt5/api/reportapi_html_charts)