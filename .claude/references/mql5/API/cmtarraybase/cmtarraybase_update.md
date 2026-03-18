# CMTArrayBase::Update

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtarraybase/cmtarraybase_update

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
            -   [CMTArrayBase](/en/docs/mt5/api/cmtarraybase)
                -   [Constructor](/en/docs/mt5/api/cmtarraybase/cmtarraybase_constructor)
                -   [Templates](/en/docs/mt5/api/cmtarraybase/cmtarraybase_templates)
                -   [Total](/en/docs/mt5/api/cmtarraybase/cmtarraybase_total)
                -   [Width](/en/docs/mt5/api/cmtarraybase/cmtarraybase_width)
                -   [Max](/en/docs/mt5/api/cmtarraybase/cmtarraybase_max)
                -   [Step](/en/docs/mt5/api/cmtarraybase/cmtarraybase_step)
                -   [Compare](/en/docs/mt5/api/cmtarraybase/cmtarraybase_compare)
                -   [Clear](/en/docs/mt5/api/cmtarraybase/cmtarraybase_clear)
                -   [Zero](/en/docs/mt5/api/cmtarraybase/cmtarraybase_zero)
                -   [Shutdown](/en/docs/mt5/api/cmtarraybase/cmtarraybase_shutdown)
                -   [Compact](/en/docs/mt5/api/cmtarraybase/cmtarraybase_compact)
                -   [Assign](/en/docs/mt5/api/cmtarraybase/cmtarraybase_assign)
                -   [Swap](/en/docs/mt5/api/cmtarraybase/cmtarraybase_swap)
                -   [Reserve](/en/docs/mt5/api/cmtarraybase/cmtarraybase_reserve)
                -   [Resize](/en/docs/mt5/api/cmtarraybase/cmtarraybase_resize)
                -   [Add](/en/docs/mt5/api/cmtarraybase/cmtarraybase_add)
                -   [AddRange](/en/docs/mt5/api/cmtarraybase/cmtarraybase_addrange)
                -   [AddEmpty](/en/docs/mt5/api/cmtarraybase/cmtarraybase_addempty)
                -   [Append](/en/docs/mt5/api/cmtarraybase/cmtarraybase_append)
                -   [Insert](/en/docs/mt5/api/cmtarraybase/cmtarraybase_insert)
                -   [InsertEmpty](/en/docs/mt5/api/cmtarraybase/cmtarraybase_insertempty)
                -   [Delete](/en/docs/mt5/api/cmtarraybase/cmtarraybase_delete)
                -   [DeleteRange](/en/docs/mt5/api/cmtarraybase/cmtarraybase_deleterange)
                -   [Remove](/en/docs/mt5/api/cmtarraybase/cmtarraybase_remove)
                -   [Update](/en/docs/mt5/api/cmtarraybase/cmtarraybase_update)
                -   [Shift](/en/docs/mt5/api/cmtarraybase/cmtarraybase_shift)
                -   [Trim](/en/docs/mt5/api/cmtarraybase/cmtarraybase_trim)
                -   [Next](/en/docs/mt5/api/cmtarraybase/cmtarraybase_next)
                -   [Prev](/en/docs/mt5/api/cmtarraybase/cmtarraybase_prev)
                -   [At](/en/docs/mt5/api/cmtarraybase/cmtarraybase_at)
                -   [Position](/en/docs/mt5/api/cmtarraybase/cmtarraybase_position)
                -   [Range](/en/docs/mt5/api/cmtarraybase/cmtarraybase_range)
                -   [Sort](/en/docs/mt5/api/cmtarraybase/cmtarraybase_sort)
                -   [Search](/en/docs/mt5/api/cmtarraybase/cmtarraybase_search)
                -   [SearchGreatOrEq](/en/docs/mt5/api/cmtarraybase/cmtarraybase_searchgreatoreq)
                -   [SearchGreater](/en/docs/mt5/api/cmtarraybase/cmtarraybase_searchgreater)
                -   [SearchLessOrEq](/en/docs/mt5/api/cmtarraybase/cmtarraybase_searchlessoreq)
                -   [SearchLess](/en/docs/mt5/api/cmtarraybase/cmtarraybase_searchless)
                -   [SearchLeft](/en/docs/mt5/api/cmtarraybase/cmtarraybase_searchleft)
                -   [SearchRight](/en/docs/mt5/api/cmtarraybase/cmtarraybase_searchright)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[CMTArrayBase](/en/docs/mt5/api/cmtarraybase)Update

# CMTArrayBase::Update

Update the element at the specified position in the array.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">bool&nbsp;&nbsp;</span><span class="f_Functions">CMTArrayBase::Update</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">pos</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Position</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;void</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">*elem</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;New&nbsp;element</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

pos

\[in\]  The position at which you want to update the element. Numbering starts from 0.

\*elem

\[in\]  A pointer to the element that you want to use instead the specified one.

Return Value

If successful, returns true, otherwise returns false.

Note

The size of the new element must match the size of the array elements [CMTArrayBase::Width](/en/docs/mt5/api/cmtarraybase/cmtarraybase_width).

[Remove](/en/docs/mt5/api/cmtarraybase/cmtarraybase_remove)

[Shift](/en/docs/mt5/api/cmtarraybase/cmtarraybase_shift)