# Request for Reports

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_request

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)Request for Reports

# Request for Reports

Reports are requested from the Manager terminal. When a manager requests a report, the corresponding command is sent to the trading server. The trading server generates a report and sends it to the Manager terminal where it is displayed as a table, HTML page or dashboard.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The reports are generated in accordance with the permissions granted to the <a href="/en/docs/mt5/api/config_manager/imtconmanager" class="topiclink">manager account</a>. It is not possible to request a report on accounts, symbols, clients or trading operations if the manager account does not have the necessary access permissions.</span></p></td></tr></tbody></table>

![Reports](/en/docs/mt5/api/img/manager_reports.png "Reports")

Using the context menu commands, you can save the report in CSV, Open XML, MHT or HTML file. Diagram settings are available in the context menu for dashboard reports:

-   Title — show/hide the chart title.
-   Legend — show/hide the chart legend.
-   Details — show/hide the chart details.
-   Color — switch color. The option is used for charts displaying information about an entity.
-   Type — switch the chart view: Bar chart, Line chart, Area chart, Donut chart, value (shows the total variable value).
-   Stacking — switch chart stacking type. Used for charts, which compare several entities and their contribution to the overall value. For example, you may distribute positions by symbols and market sentiment. Available options:

-   None — data series are displayed separately
-   With negative values — data series are combined, values are not summed up
-   Regular — data series are combined, values are summed up
-   100% — rows are combined, the general contribution of each series to the total value in percentage is shown

## Requesting a Report [#](reportapi_request#request)

A report is requested from the server automatically when you select it from the list or change its parameters. To force a report refresh, click the ![Refresh](/en/docs/mt5/api/img/refresh_icon.png "Refresh") button in the upper right corner.

Reports may have settings: filters by groups, dates and symbols. They can be changed in the upper right corner of the section.

![Report settings](/en/docs/mt5/api/img/manager_report_settings.png "Report settings")

The availability of the settings depends on the specific report.

-   Groups — group of users, on which the report is generated. When making a request, you may specify:

-   One of the trading groups or subgroups, for example, "demo\\\*.
-   User logins are comma-separated, for example "10011, 10012, 10015".
-   Create or use a previously saved [custom set of accounts](/en/docs/mt5/api/reportapi_request).

-   Symbols — symbol, for which the report will be generated (for example, report on operation on a certain symbol). Possibility to filter by symbols depends on the report type.
-   Period — custom period for report generation (for example, report on trading operations for the last week). Dates can be specified both manually and using a calendar that is opened when you press ![Calendar](/en/docs/mt5/api/img/calendar_icon2.png "Calendar"). Using the ![Calendar](/en/docs/mt5/api/img/calendar_icon.png "Calendar") allows to select one of predefined time periods to generate a report for.
-   ![Dashboard](/en/docs/mt5/api/img/report_dashboard_icon.png "Dashboard")/![Regular Report](/en/docs/mt5/api/img/report_old_icon.png "Regular Report") — switch between report types: regular and dashboard. Depending on the implementation of the report by its developer, it can support both types or only one of them.

[Configuration of Reports](/en/docs/mt5/api/reportapi_configuration)

[Requirements for Modules](/en/docs/mt5/api/reportapi_requirements)