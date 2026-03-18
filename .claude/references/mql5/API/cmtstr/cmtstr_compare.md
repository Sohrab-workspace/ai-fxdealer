# CMTStr::Compare

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtstr/cmtstr_compare

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
            -   [CMTStr](/en/docs/mt5/api/cmtstr)
                -   [Clear](/en/docs/mt5/api/cmtstr/cmtstr_clear)
                -   [Empty](/en/docs/mt5/api/cmtstr/cmtstr_empty)
                -   [Len](/en/docs/mt5/api/cmtstr/cmtstr_len)
                -   [Max](/en/docs/mt5/api/cmtstr/cmtstr_max)
                -   [Str](/en/docs/mt5/api/cmtstr/cmtstr_str)
                -   [Buffer](/en/docs/mt5/api/cmtstr/cmtstr_buffer)
                -   [Refresh](/en/docs/mt5/api/cmtstr/cmtstr_refresh)
                -   [Assign](/en/docs/mt5/api/cmtstr/cmtstr_assign)
                -   [Format](/en/docs/mt5/api/cmtstr/cmtstr_format)
                -   [ToLower](/en/docs/mt5/api/cmtstr/cmtstr_tolower)
                -   [ToUpper](/en/docs/mt5/api/cmtstr/cmtstr_toupper)
                -   [Trim](/en/docs/mt5/api/cmtstr/cmtstr_trim)
                -   [TrimSpaces](/en/docs/mt5/api/cmtstr/cmtstr_trimspaces)
                -   [Replace](/en/docs/mt5/api/cmtstr/cmtstr_replace)
                -   [ReplaceChar](/en/docs/mt5/api/cmtstr/cmtstr_replacechar)
                -   [Delete](/en/docs/mt5/api/cmtstr/cmtstr_delete)
                -   [FormatStr](/en/docs/mt5/api/cmtstr/cmtstr_formatstr)
                -   [Terminate](/en/docs/mt5/api/cmtstr/cmtstr_terminate)
                -   [Append](/en/docs/mt5/api/cmtstr/cmtstr_append)
                -   [Insert](/en/docs/mt5/api/cmtstr/cmtstr_insert)
                -   [Copy](/en/docs/mt5/api/cmtstr/cmtstr_copy)
                -   [CopyCodePage](/en/docs/mt5/api/cmtstr/cmtstr_copycodepage)
                -   [Compare](/en/docs/mt5/api/cmtstr/cmtstr_compare)
                -   [CompareNoCase](/en/docs/mt5/api/cmtstr/cmtstr_comparenocase)
                -   [CheckGroupMask](/en/docs/mt5/api/cmtstr/cmtstr_checkgroupmask)
                -   [Find](/en/docs/mt5/api/cmtstr/cmtstr_find)
                -   [FindNoCase](/en/docs/mt5/api/cmtstr/cmtstr_findnocase)
                -   [FindR](/en/docs/mt5/api/cmtstr/cmtstr_findr)
                -   [FindChar](/en/docs/mt5/api/cmtstr/cmtstr_findchar)
                -   [FindRChar](/en/docs/mt5/api/cmtstr/cmtstr_findrchar)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[CMTStr](/en/docs/mt5/api/cmtstr)Compare

# CMTStr::Compare

Compare a string object with the specified string.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">int&nbsp;&nbsp;</span><span class="f_Functions">CMTStr::Compare</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">str</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;String</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

Parameters

str

\[in\]  The string, with which you compare the current string object.

Return Value

If the strings are equal, it returns 0. A value < 0 means that the string object is less than str, a value > 0 means that it's greater than str.

Note

The comparison is case sensitive.

# CMTStr::Compare

Compare a string object with the specified string till the specified character.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">int&nbsp;&nbsp;</span><span class="f_Functions">CMTStr::Compare</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">str</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;String</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">count</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;number&nbsp;of&nbsp;the&nbsp;character</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

Parameters

str

\[in\]  The string, with which you compare the current string object.

count

\[in\]  The number of the character, to which the strings are compared. Numbering starts from 0.

Return Value

If the strings are equal, it returns 0. A value < 0 means that the string object is less than str, a value > 0 means that it's greater than str.

Note

Compares a string with the specified one, but to the character specified in the count parameter.

The comparison is case sensitive.

# CMTStr::Compare

Compare a string object with the specified string object.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">int&nbsp;&nbsp;</span><span class="f_Functions">CMTStr::Compare</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;CMTStr&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">str</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;String&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

Parameters

str

\[in\]  The [CMTStr](/en/docs/mt5/api/cmtstr) string object, with which you compare the current string object.

Return Value

If the objects are equal, it returns 0. A value < 0 means that the current string object is less than str, a value > 0 means that it's greater than str.

Note

The comparison is case sensitive.

# CMTStr::Compare

Compare two strings.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">static&nbsp;int&nbsp;&nbsp;</span><span class="f_Functions">CMTStr::Compare</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">str1</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;string&nbsp;to&nbsp;compare</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">str2</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;string&nbsp;to&nbsp;compare</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

str1

\[in\]  A string to compare.

str2

\[in\]  A string to compare.

Return Value

If the strings are equal, it returns 0. A value < 0 means that the string str1 is less than str2, a value > 0 means that str1 is greater than str2.

Note

The comparison is case sensitive.

# CMTStr::Compare

Compare two strings till the specified character.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">static&nbsp;int&nbsp;&nbsp;</span><span class="f_Functions">CMTStr::Compare</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">str1</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;string&nbsp;to&nbsp;compare</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">str2</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;string&nbsp;to&nbsp;compare</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">count</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;number&nbsp;of&nbsp;the&nbsp;character</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

str1

\[in\]  A string to compare.

str2

\[in\]  A string to compare.

count

\[in\]  The number of the character, to which the strings are compared. Numbering starts from 0.

Return Value

If the strings are equal, it returns 0. A value < 0 means that the string str1 is less than str2, a value > 0 means that str1 is greater than str2.

Note

The function compares two strings, but to the character specified in the count parameter.

The comparison is case sensitive.

[CopyCodePage](/en/docs/mt5/api/cmtstr/cmtstr_copycodepage)

[CompareNoCase](/en/docs/mt5/api/cmtstr/cmtstr_comparenocase)