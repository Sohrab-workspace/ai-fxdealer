# IMTDatasetSummary::ValueVolumeCurrent

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuevolumecurrent

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
                -   [IMTDatasetField](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield)
                -   [IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest)
                -   [IMTDatasetColumn](/en/docs/mt5/api/reportapi_dataset/imtdatasetcolumn)
                -   [IMTDatasetSummary](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary)
                    -   [Enumerations](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_enum)
                    -   [Release](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_release)
                    -   [Assign](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_assign)
                    -   [Clear](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_clear)
                    -   [ColumnID](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_columnid)
                    -   [Line](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_line)
                    -   [MergeColumn](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_mergecolumn)
                    -   [Color](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_color)
                    -   [Flags](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_flags)
                    -   [Type](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_type)
                    -   [Digits](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_digits)
                    -   [ValueInt](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valueint)
                    -   [ValueUInt](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valueuint)
                    -   [ValueDouble](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuedouble)
                    -   [ValueMoney](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuemoney)
                    -   [ValueString](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuestring)
                    -   [ValueDate](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuedate)
                    -   [ValueTime](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuetime)
                    -   [ValueDateTime](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuedatetime)
                    -   [ValuePrice](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valueprice)
                    -   [ValuePricesBid](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuepricesbid)
                    -   [ValuePricesAsk](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuepricesask)
                    -   [ValuePrices](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valueprices)
                    -   [ValueVolume](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuevolume)
                    -   [ValueVolumeInitial](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuevolumeinitial)
                    -   [ValueVolumeCurrent](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuevolumecurrent)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)[IMTDatasetSummary](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary)ValueVolumeCurrent

# IMTDatasetSummary::ValueVolumeCurrent

Get a previously set current (unexecuted) volume value in a summary cell.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">UINT64&nbsp;&nbsp;</span><span class="f_Functions">IMTDatasetSummary::ValueVolumeCurrent</span><span class="f_CodeExample">()</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

Return Value

A previously set current (unexecuted) volume value in a summary cell. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

Note

A received summary must be of [IMTDatasetSummary::TYPE\_VOLUME\_ORDER](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_enum#entype) type. Otherwise, the method returns 0.

[ValueVolumeInitial](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary/imtdatasetsummary_valuevolumeinitial)

[Data Cache Interfaces](/en/docs/mt5/api/reportapi_cache)