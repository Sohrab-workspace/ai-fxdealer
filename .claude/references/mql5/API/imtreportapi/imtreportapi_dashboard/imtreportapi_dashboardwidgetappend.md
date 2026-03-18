# IMTReportAPI::DashboardWidgetAppend

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgetappend

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
                -   [Enumerations](/en/docs/mt5/api/imtreportapi/imtreportapi_enum)
                -   [Common Functions](/en/docs/mt5/api/imtreportapi/imtreportapi_common)
                -   [Report Parameters](/en/docs/mt5/api/imtreportapi/imtreportapi_parameters)
                -   [HTML Reports](/en/docs/mt5/api/imtreportapi/imtreportapi_html)
                -   [Tabular Reports](/en/docs/mt5/api/imtreportapi/imtreportapi_table)
                -   [Dashboards](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard)
                    -   [DashboardWidth](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidth)
                    -   [DashboardHeight](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardheight)
                    -   [DashboardTitle](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardtitle)
                    -   [DashboardFlags](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardflags)
                    -   [DashboardHtmlAppend](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardhtmlappend)
                    -   [DashboardHtmlClear](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardhtmlclear)
                    -   [DashboardHtmlDelete](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardhtmldelete)
                    -   [DashboardHtmlTotal](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardhtmltotal)
                    -   [DashboardHtmlNext](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardhtmlnext)
                    -   [DashboardWidgetAppend](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgetappend)
                    -   [DashboardWidgetClear](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgetclear)
                    -   [DashboardWidgetDelete](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgetdelete)
                    -   [DashboardWidgetTotal](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgettotal)
                    -   [DashboardWidgetNext](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgetnext)
                -   [Configuration Databases](/en/docs/mt5/api/imtreportapi/imtreportapi_config)
                -   [Clients](/en/docs/mt5/api/imtreportapi/imtreportapi_client)
                -   [Users](/en/docs/mt5/api/imtreportapi/imtreportapi_user)
                -   [Trade Databases](/en/docs/mt5/api/imtreportapi/imtreportapi_trade)
                -   [Daily Reports](/en/docs/mt5/api/imtreportapi/imtreportapi_daily)
                -   [Price Data](/en/docs/mt5/api/imtreportapi/imtreportapi_price)
                -   [Dataset](/en/docs/mt5/api/imtreportapi/imtreportapi_dataset)
                -   [Data cache](/en/docs/mt5/api/imtreportapi/imtreportapi_cache)
                -   [Subscriptions](/en/docs/mt5/api/imtreportapi/imtreportapi_subscription)
                -   [Geo Services](/en/docs/mt5/api/imtreportapi/imtreportapi_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Main Interface of Reports](/en/docs/mt5/api/imtreportapi)[Dashboards](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard)DashboardWidgetAppend

# IMTReportAPI::DashboardWidgetAppend

Add a widget to a dashboard.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">IMTReportDashboardWidget*&nbsp;&nbsp;</span><span class="f_Functions">IMTReportAPI::DashboardWidgetAppend</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Return Value

Pointer to the created [IMTReportDashboardWidget](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget) widget object.

Note

The method creates a widget bound to the dashboard and returns a pointer to it. To display data in the widget, bind a data set to it using the [IMTReportDashboardWidget::Data](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_data) or [IMTReportDashboardWidget::Html](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_html) method.

[DashboardHtmlNext](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardhtmlnext)

[DashboardWidgetClear](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgetclear)