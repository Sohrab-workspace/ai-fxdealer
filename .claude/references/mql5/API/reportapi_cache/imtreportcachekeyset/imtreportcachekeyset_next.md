# IMTReportCacheKeySet::Next

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_next

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
                -   [IMTReportCache](/en/docs/mt5/api/reportapi_cache/imtreportcache)
                -   [IMTReportCacheValue](/en/docs/mt5/api/reportapi_cache/imtreportcachevalue)
                -   [IMTReportCacheKeySet](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset)
                    -   [Release](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_release)
                    -   [Assign](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_assign)
                    -   [Clear](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_clear)
                    -   [Swap](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_swap)
                    -   [Total](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_total)
                    -   [Array](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_array)
                    -   [Next](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_next)
                    -   [Search](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_search)
                    -   [ContainsSet](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_containsset)
                    -   [Reserve](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_reserve)
                    -   [Insert](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_insert)
                    -   [InsertArray](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_insertarray)
                    -   [InsertSet](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_insertset)
                    -   [Remove](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_remove)
                    -   [RemoveArray](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_removearray)
                    -   [RemoveSet](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_removeset)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Data Cache Interfaces](/en/docs/mt5/api/reportapi_cache)[IMTReportCacheKeySet](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset)Next

# IMTReportCacheKeySet::Next

Get the next key from a sorted key array.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">const&nbsp;UINT64*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Functions">IMTReportCacheKeySet::Next</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">key</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Key</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

key

\[in\]  A pointer to a key in the sorted array of keys. To get the pointer to the first key from the set, use the [IMTReportCacheKeySet::Array](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_array) method.

Return Value

A pointer to the next key or NULL if the array end is reached.

[Array](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_array)

[Search](/en/docs/mt5/api/reportapi_cache/imtreportcachekeyset/imtreportcachekeyset_search)