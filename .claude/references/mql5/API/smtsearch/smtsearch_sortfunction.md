# Sort Function

> Source: https://support.metaquotes.net/en/docs/mt5/api/smtsearch/smtsearch_sortfunction

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
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
            -   [SMTFormat](/en/docs/mt5/api/smtformat)
            -   [SMTMath](/en/docs/mt5/api/smtmath)
            -   [SMTSearch](/en/docs/mt5/api/smtsearch)
                -   [Sort Function](/en/docs/mt5/api/smtsearch/smtsearch_sortfunction)
                -   [Insert](/en/docs/mt5/api/smtsearch/smtsearch_insert)
                -   [QuickSort](/en/docs/mt5/api/smtsearch/smtsearch_quicksort)
                -   [Search](/en/docs/mt5/api/smtsearch/smtsearch_search)
                -   [SearchGreatOrEq](/en/docs/mt5/api/smtsearch/smtsearch_searchgreatoreq)
                -   [SearchGreater](/en/docs/mt5/api/smtsearch/smtsearch_searchgreater)
                -   [SearchLessOrEq](/en/docs/mt5/api/smtsearch/smtsearch_searchlessoreq)
                -   [SearchLess](/en/docs/mt5/api/smtsearch/smtsearch_searchless)
                -   [SearchLeft](/en/docs/mt5/api/smtsearch/smtsearch_searchleft)
                -   [SearchRight](/en/docs/mt5/api/smtsearch/smtsearch_searchright)
            -   [CMTArrayBase](/en/docs/mt5/api/cmtarraybase)
            -   [CMTStr](/en/docs/mt5/api/cmtstr)
            -   [CMTSync](/en/docs/mt5/api/cmtsync)
            -   [CMTThread](/en/docs/mt5/api/cmtthread)
            -   [SMTTime](/en/docs/mt5/api/smttime)
            -   [CMTFile](/en/docs/mt5/api/cmtfile)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[SMTSearch](/en/docs/mt5/api/smtsearch)Sort Function

# Sort Function

The sort function is used in the sort and search methods of the SMTSearch class. It is defined by the programmer. In the methods of the SMTSearch class, a pointer to this function is passed, where the two values, at which its left and right parameters point, are compared. This function is similar to CRT sort functions "qsort" and "bsearch".

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Reserved">typedef</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;(</span><span class="f_Reserved">__cdecl</span><span class="f_CodeExample">&nbsp;</span><span class="f_Macros">*SortFunctionPtr</span><span class="f_CodeExample">)(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;</span><span class="f_Macros">*</span><span class="f_CodeExample">,&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;</span><span class="f_Macros">*</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

Depending on the comparison results, the following values are returned:

-   <0 — if the left parameter is less than the right one
-   0 — if the left parameter is equal to the right one
-   \>0 — if the left parameter is greater than the right one

[SMTSearch](/en/docs/mt5/api/smtsearch)

[Insert](/en/docs/mt5/api/smtsearch/smtsearch_insert)