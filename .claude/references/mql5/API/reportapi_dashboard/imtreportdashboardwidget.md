# IMTReportDashboardWidget

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget

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
                    -   [Enumerations](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_enum)
                    -   [Assign](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_assign)
                    -   [Clear](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_clear)
                    -   [Title](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_title)
                    -   [Description](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_description)
                    -   [Type](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_type)
                    -   [ChartStackType](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_chartstacktype)
                    -   [ChartValueAxis](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_chartvalueaxis)
                    -   [Flags](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_flags)
                    -   [Width](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_width)
                    -   [Height](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_height)
                    -   [Left](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_left)
                    -   [Top](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_top)
                    -   [Html](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_html)
                    -   [Data](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_data)
                    -   [DataColumnTitle](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumntitle)
                    -   [DataColumnClear](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnclear)
                    -   [DataColumnAdd](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnadd)
                    -   [DataColumnDelete](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumndelete)
                    -   [DataColumnShift](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnshift)
                    -   [DataColumnTotal](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumntotal)
                    -   [DataColumnNext](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnnext)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)IMTReportDashboardWidget

# IMTReportDashboardWidget

A widget is a separate type of presentation that can be used on a dashboard. It allows presenting data as HTML content, chart and/or table. The IMTReportDashboardWidget interface allows managing its properties and contents.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_assign" class="topiclink">Assign</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a passed object to the current one.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_clear" class="topiclink">Clear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear an object.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_title" class="topiclink">Title</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set a widget title.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_description" class="topiclink">Description</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set widget description.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_type" class="topiclink">Type</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set a default display type for the widget diagram.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_chartstacktype" class="topiclink">ChartStackType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set a default accumulation type for the widget diagram.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_chartvalueaxis" class="topiclink">ChartValueAxis</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the type of the value axis for the chart.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_flags" class="topiclink">Flags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set widget display flags.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_width" class="topiclink">Width</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set a widget width.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_height" class="topiclink">Height</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set a widget height.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_left" class="topiclink">Left</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set a widget indent from the left dashboard border.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_top" class="topiclink">Top</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set a widget indent from the upper dashboard border.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_html" class="topiclink">Html</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and add data for displaying in the widget as HTML content.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_data" class="topiclink">Data</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and add data for displaying in the widget as a diagram and/or table.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumntitle" class="topiclink">DataColumnTitle</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set an ID of a column containing headers of all the remaining table columns.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnclear" class="topiclink">DataColumnClear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear the widget columns display rules.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnadd" class="topiclink">DataColumnAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add the column to the display rules.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumndelete" class="topiclink">DataColumnDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete a column from the display rules.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnshift" class="topiclink">DataColumnShift</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Change column position in the display rules.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumntotal" class="topiclink">DataColumnTotal</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the number of columns in the display rules.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_datacolumnnext" class="topiclink">DataColumnNext</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get column ID by its position in the display rules.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Use <a href="/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard/imtreportapi_dashboardwidgetappend" class="topiclink">IMTReportAPI::DashboardWidgetAppend</a> to create a widget object.</span></li><li class="p_tableatten"><span class="f_tableatten">The IMTReportDashboardWidget::DataColumn* method group defines what columns from the <a href="/en/docs/mt5/api/reportapi_dataset/imtdataset" class="topiclink">IMTDataset</a> data set are to be displayed in the dashboard widget, as well as their display order. If the DataColumn array is empty, all columns are displayed in the order they are added to IMTDataset. The values from the first column are to be used as headers.</span></li></ul></td></tr></tbody></table>

The IMTReportDashboardWidget interface contains the following enumerations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Interface</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_enum#enwidgettype" class="topiclink">EnWidgetType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Types of diagrams and widget contents.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_enum#enchartstacktype" class="topiclink">EnChartStackType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Accumulation types for widget diagrams.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_enum#enwidgetflags" class="topiclink">EnWidgetFlags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Widget display flags.</span></p></td></tr></tbody></table>

[TplProcess](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardhtml/imtreportdashboardhtml_tplprocess)

[Enumerations](/en/docs/mt5/api/reportapi_dashboard/imtreportdashboardwidget/imtreportdashboardwidget_enum)