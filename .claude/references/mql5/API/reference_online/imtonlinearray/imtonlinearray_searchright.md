# IMTUserArray::SearchRight

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchright

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
            -   [Trade](/en/docs/mt5/api/reference_trading)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
                -   [IMTOnline](/en/docs/mt5/api/reference_online/imtonline)
                -   [IMTOnlineArray](/en/docs/mt5/api/reference_online/imtonlinearray)
                    -   [Release](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_release)
                    -   [Assign](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_assign)
                    -   [Clear](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_clear)
                    -   [Add](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_add)
                    -   [AddCopy](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_addcopy)
                    -   [Delete](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_delete)
                    -   [Detach](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_detach)
                    -   [Update](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_update)
                    -   [UpdateCopy](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_updatecopy)
                    -   [Shift](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_shift)
                    -   [Total](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_total)
                    -   [Next](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_next)
                    -   [Sort](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_sort)
                    -   [Search](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_search)
                    -   [SearchGreatOrEq](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchgreatoreq)
                    -   [SearchGreater](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchgreater)
                    -   [SearchLessOrEq](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchlessoreq)
                    -   [SearchLess](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchless)
                    -   [SearchLeft](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchleft)
                    -   [SearchRight](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchright)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Online Connections](/en/docs/mt5/api/reference_online)[IMTOnlineArray](/en/docs/mt5/api/reference_online/imtonlinearray)SearchRight

# IMTUserArray::SearchRight

Searches in an array for the last element equal to the search key.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">int&nbsp;&nbsp;</span><span class="f_Functions">IMTOnlineArray::SearchRight</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;void</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">*key</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Sort&nbsp;key</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTSortFunctionPtr</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">sort_function</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Pointer&nbsp;to&nbsp;the&nbsp;search&nbsp;function</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

Parameters

\*key

\[in\]  A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void \*left).

sort\_function

\[in\]  A pointer to the [Search function](/en/docs/mt5/api/reference_types#mtsortfunctionptr).

Return Value

If successful, it returns the position of a trade order object that meets the search criteria. Otherwise, it returns -1.

Note

For a successful search, an array must be sorted first by calling the [IMTOnlineArray::Sort](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_sort) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

[SearchLeft](/en/docs/mt5/api/reference_online/imtonlinearray/imtonlinearray_searchleft)

[Certificates](/en/docs/mt5/api/reference_certificate)