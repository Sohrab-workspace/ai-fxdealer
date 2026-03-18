# SMTSearch::Insert

> Source: https://support.metaquotes.net/en/docs/mt5/api/smtsearch/smtsearch_insert

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[SMTSearch](/en/docs/mt5/api/smtsearch)Insert

# SMTSearch::Insert

Insert an element in a pre-sorted array without disturbing the sort order.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">static&nbsp;char*&nbsp;&nbsp;</span><span class="f_Functions">SMTSearch::Insert</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">void</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">*base</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;void</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">*elem</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;element&nbsp;to&nbsp;insert</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">size_t</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">total</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Array&nbsp;size</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;size_t</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">width</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Size&nbsp;of&nbsp;the&nbsp;array&nbsp;element</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">SortFunctionPtr</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">compare</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Sort&nbsp;function</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

\*base

\[in\]  A pointer to an array in which you want to insert an element.

\*elem

\[in\]  A pointer to an element, which you want to insert into an array.

total

\[in\]  The current size of the array in elements.

width

\[in\]  The size of one array element in bytes.

compare

\[in\]  A pointer to the [sort function](/en/docs/mt5/api/smtsearch/smtsearch_sortfunction). A pointer to the inserted elem element is passed as the first parameter in the sort function.

Return Value

A pointer to a new element of the array. If inserting an element fails, or the inserted element already exists in the array, it returns NULL.

Note

After successful insertion the size of the array increases by one element. Memory for the new element should always be pre-allocated by the programmer.

The array must be sorted first using the the [SMTSearch::QuickSort](/en/docs/mt5/api/smtsearch/smtsearch_quicksort) method. The sort function in the sort methods and insertion methods must match.

Example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #808080;">//|&nbsp;Sort&nbsp;Function&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;SortInts(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;*left,</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;*right)</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;lft=*(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;*)left;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;rgh=*(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;*)right;</span><br><span class="f_CodeExample" style="color: #808080;">//---</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(lft&lt;rgh)&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(-1);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(lft&gt;rgh)&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(1);</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(0);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #808080;">//|&nbsp;Example&nbsp;of&nbsp;the&nbsp;Insert&nbsp;method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;Example()</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;arr_a[6]={2,1,5,7,2,2};</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;arr_b[7]={0};</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;c=3;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Sort</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;SMTSearch::QuickSort(arr_a,6,SortInts);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Now&nbsp;arr_a&nbsp;=&nbsp;1,2,2,2,5,7</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Copy&nbsp;arr_a&nbsp;into&nbsp;a&nbsp;larger&nbsp;array&nbsp;arr_b</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;memcpy(arr_b,arr_a,</span><span class="f_CodeExample" style="color: #0000ff;">sizeof</span><span class="f_CodeExample">(arr_a));</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;SMTSearch::Insert(arr_b,&amp;c,6,</span><span class="f_CodeExample" style="color: #0000ff;">sizeof</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">),SortInts);&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;arr_b&nbsp;=&nbsp;{&nbsp;1,2,2,2,3,5,7&nbsp;}</span><br><span class="f_CodeExample" style="color: #808080;">//---</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(0);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span></p></td></tr></tbody></table>

[Sort Function](/en/docs/mt5/api/smtsearch/smtsearch_sortfunction)

[QuickSort](/en/docs/mt5/api/smtsearch/smtsearch_quicksort)