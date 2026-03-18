# IMTDataset

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_dataset/imtdataset

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
                -   [IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset)
                    -   [Enumerations](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_enum)
                    -   [Release](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_release)
                    -   [Assign](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_assign)
                    -   [Clear](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_clear)
                    -   [Flags](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_flags)
                    -   [ColumnCreate](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columncreate)
                    -   [ColumnClear](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnclear)
                    -   [ColumnAdd](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnadd)
                    -   [ColumnDelete](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columndelete)
                    -   [ColumnTotal](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columntotal)
                    -   [ColumnSize](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnsize)
                    -   [ColumnNext](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnnext)
                    -   [RowClear](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_rowclear)
                    -   [RowWrite](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_rowwrite)
                    -   [RowTotal](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_rowtotal)
                    -   [SummaryCreate](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarycreate)
                    -   [SummaryClear](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summaryclear)
                    -   [SummaryAdd](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summaryadd)
                    -   [SummaryDelete](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarydelete)
                    -   [SummaryNext](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarynext)
                    -   [SummaryTotal](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarytotal)
                -   [IMTDatasetField](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield)
                -   [IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest)
                -   [IMTDatasetColumn](/en/docs/mt5/api/reportapi_dataset/imtdatasetcolumn)
                -   [IMTDatasetSummary](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)IMTDataset

# IMTDataset

The IMTDataset interface is designed to work with dashboard data: columns, rows and final values. These data can be displayed in the widget as a graph and/or a table. It contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:124px; height:17px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table" style="height:17px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_release" class="topiclink">Release</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the current object.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_assign" class="topiclink">Assign</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a passed object to the current one.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_clear" class="topiclink">Clear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear an object.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_flags" class="topiclink">Flags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set data set flags.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columncreate" class="topiclink">ColumnCreate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create a column object.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnclear" class="topiclink">ColumnClear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear table columns description.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnadd" class="topiclink">ColumnAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add a column description to a table end.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columndelete" class="topiclink">ColumnDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete a column description from a table by index.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columntotal" class="topiclink">ColumnTotal</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a number of columns in a table.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnsize" class="topiclink">ColumnSize</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a total size of one table row in bytes.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnnext" class="topiclink">ColumnNext</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a column description by index.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_rowclear" class="topiclink">RowClear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the contents of a whole table.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_rowwrite" class="topiclink">RowWrite</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add (output) one record to a table.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_rowtotal" class="topiclink">RowTotal</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the number of rows in a table.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarycreate" class="topiclink">SummaryCreate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create an object of a totals row cell.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summaryclear" class="topiclink">SummaryClear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear all total records.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summaryadd" class="topiclink">SummaryAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add a totals row cell into a table.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarydelete" class="topiclink">SummaryDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete a cell in a table totals row by its index.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarynext" class="topiclink">SummaryNext</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the cells of a table totals row by its index.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_summarytotal" class="topiclink">SummaryTotal</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the total amount of totals cells in a table.</span></p></td></tr></tbody></table>

The IMTDataset interface contains the following enumerations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Interface</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_enum#endatasetflags" class="topiclink">EnDataSetFlags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Data set flags.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In earlier MetaTrader 5 API versions, the IMTDataset interface was called IMTReportDashboardData.</span></p></td></tr></tbody></table>

[Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)

[Enumerations](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_enum)