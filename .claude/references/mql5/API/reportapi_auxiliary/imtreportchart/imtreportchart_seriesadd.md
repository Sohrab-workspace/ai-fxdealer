# IMTReportChart::SeriesAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesadd

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
                -   [IMTReportSeries](/en/docs/mt5/api/reportapi_auxiliary/imtreportseries)
                -   [IMTReportChart](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart)
                    -   [Enumerations](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_enum)
                    -   [Release](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_release)
                    -   [Assign](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_assign)
                    -   [Clear](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_clear)
                    -   [Title](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_title)
                    -   [Type](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_type)
                    -   [Digits](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_digits)
                    -   [Flags](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_flags)
                    -   [BarHeight](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_barheight)
                    -   [PieceTooltip](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_piecetooltip)
                    -   [PieceDescription](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_piecedescription)
                    -   [SeriesClear](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesclear)
                    -   [SeriesAdd](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesadd)
                    -   [SeriesAddCopy](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesaddcopy)
                    -   [SeriesDelete](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesdelete)
                    -   [SeriesDetach](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesdetach)
                    -   [SeriesUpdate](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesupdate)
                    -   [SeriesShift](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesshift)
                    -   [SeriesTotal](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriestotal)
                    -   [SeriesNext](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesnext)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Diagram Interfaces](/en/docs/mt5/api/reportapi_auxiliary)[IMTReportChart](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart)SeriesAdd

# IMTReportChart::SeriesAdd

Add data series to a chart.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTReportChart::SeriesAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTReportSeries*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">series</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Data&nbsp;series&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

series

\[in\] [Data series](/en/docs/mt5/api/reportapi_auxiliary/imtreportseries) object.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

This method places a pointer to a passed object at a chart object. After a successful call of this method, the control over the life time of the series object is passed to the chart object. Thus, when deleting a chart object ([IMTReportChart::Release](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_release) call), an earlier inserted object will be automatically removed.

In turn, the removal of a newly inserted object will cause the pointer stored within the chart object to become invalid, and its call (including the case of the chart object deletion) will cause the crash of the plugin and the server.

Never add a link to one and the same object, because this will lead to a crash during memory release.

[SeriesClear](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesclear)

[SeriesAddCopy](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesaddcopy)