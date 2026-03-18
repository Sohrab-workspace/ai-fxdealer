# IMTDataset::ColumnAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnadd

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)[IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset)ColumnAdd

# IMTDataset::ColumnAdd

Add a column description to a table end.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTDataset::ColumnAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTDatasetColumn</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">*column</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;column&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

column

\[in\] [Table column description object](/en/docs/mt5/api/reportapi_dataset/imtdatasetcolumn).

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code is returned.

Note

By default, the values from the first column are used as headers for all other columns.

[ColumnClear](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columnclear)

[ColumnDelete](/en/docs/mt5/api/reportapi_dataset/imtdataset/imtdataset_columndelete)