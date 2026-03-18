# Interfaces of dashboards

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_dashboard

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)Dashboard Interfaces

# Interfaces of dashboards

Dashboards form a separate type of reports that allow combining different data and their presentation on one sheet.

A dashboard consists of widgets representing data either in the form of HTML content, or in the form of a diagram and/or table. A set of tabular data ([IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset)) or HTML data ([IMTReportDashboardHtml](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml)) can be used as a data source. The data set is bound to the widget using the [IMTReportDashboardWidget::Html](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_html) or [IMTReportDashboardWidget::Data](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_data) method depending on its type. The same data set can be used in different widgets, for example for displaying the same data in different ways or displaying different parts of data sets in separate tables.

Three interfaces are provided for working with data and widget representation:

-   [IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset) — methods for using a data set for widgets displaying diagrams and tables.
-   [IMTReportDashboardHtml](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml) — methods for working with data for widgets displaying HTML content.
-   [IMTReportDashboardWidget](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget) — methods for working with widget settings: general parameters, alignment and content presentation.

[GeoResolveBatch](/en/docs/mt5/api/imtreportapi/imtreportapi_geo/imtreportapi_georesolvebatch)

[IMTReportDashboardHtml](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml)