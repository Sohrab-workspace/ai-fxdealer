# CMTStr

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtstr

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)CMTStr

# CMTStr

This class contains additional functions for working with strings. In fact, it is a wrapping of the Unicode string.

To use the methods of the CMTStr class for working with a string, assign it one of the predefined types:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Size</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr16</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">16 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr32</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">32 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr64</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">64 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr128</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">128 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr256</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">256 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStrPath</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">260 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr512</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">512 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr1024</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">1024 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr2048</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">2048 characters.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable">CMTStr4096</span></p></td><td class="table" style="width:676px;"><p class="p_fortable"><span class="f_fortable">4096 characters.</span></p></td></tr></tbody></table>

If you need to declare a string with the size differing from the predefined ones, use the TMTStrStatic<xxx> method, where xxx is the size of a string in characters. For example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">TMTStrStatic&lt;20&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">str;</span></p></td></tr></tbody></table>

The following methods are available in the CMTStr class:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:124px; height:18px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_clear" class="topiclink">Clear</a></span></p></td><td class="table" style="width:614px; height:18px;"><p class="p_fortable"><span class="f_fortable">Clear the line. After the execution of this method, the string is empty.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_empty" class="topiclink">Empty</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Check whether the string is empty.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_len" class="topiclink">Len</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Get the length of a string without the end of line character.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_max" class="topiclink">Max</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Get the maximum number of characters that can be placed in the string object.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_str" class="topiclink">Str</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Get a constant pointer to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_buffer" class="topiclink">Buffer</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Get a non-constant pointer to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_refresh" class="topiclink">Refresh</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Update a cached string size after modification.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_assign" class="topiclink">Assign</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Assign a string to an object object.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_format" class="topiclink">Format</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Fill in the string object in accordance with the format string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_tolower" class="topiclink">ToLower</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Covert characters to lowercase.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_toupper" class="topiclink">ToUpper</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Covert characters to uppercase.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_trim" class="topiclink">Trim</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Truncate a strung to the specified number of characters.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_trimspaces" class="topiclink">TrimSpaces</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Remove all space characters from the beginning and end of the string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_replace" class="topiclink">Replace</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Replace the specified substring in the string object with another substring.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_replacechar" class="topiclink">ReplaceChar</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Replace the specified character in the string object with another character.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_delete" class="topiclink">Delete</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Remove a substring from a string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_formatstr" class="topiclink">FormatStr</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Fill in the specified string in accordance with the format string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_terminate" class="topiclink">Terminate</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Null the last element (insert end of line character) of the specified string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_append" class="topiclink">Append</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Add a string/character at the end of a string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_insert" class="topiclink">Insert</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Add a substring/character in a string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_copy" class="topiclink">Copy</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Copy strings.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_copycodepage" class="topiclink">CopyCodePage</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Convert a string encoded in one of the ANSI code pages to a UTF-16 encoded string using the specified code page.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_compare" class="topiclink">Compare</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Compare strings.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_comparenocase" class="topiclink">CompareNoCase</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Case insensitive comparison of strings.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_checkgroupmask" class="topiclink">CheckGroupMask</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Check the correspondence of a string to the specified mask.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_find" class="topiclink">Find</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Find a substring in a string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_findnocase" class="topiclink">FindNoCase</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Case insensitive search of a substring in a string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_findr" class="topiclink">FindR</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Search for a substring from the end of the string.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_findchar" class="topiclink">FindChar</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Find a character.</span></p></td></tr><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtstr/cmtstr_findrchar" class="topiclink">FindRChar</a></span></p></td><td class="table" style="width:614px;"><p class="p_fortable"><span class="f_fortable">Search for a character from the end of the string.</span></p></td></tr></tbody></table>

[SearchRight](/en/docs/mt5/api/cmtarraybase/cmtarraybase_searchright)

[Clear](/en/docs/mt5/api/cmtstr/cmtstr_clear)