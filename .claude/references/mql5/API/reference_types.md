# Internal Data Types

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_types

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)Internal Data Types

# Internal Data Types

Fur the purpose of convenience, MetaTrader 5 API has its own data types.

## MTAPIRES [#](reference_types#mtapires)

The internal data type MTAPIRES is designed for returning [response codes](/en/docs/mt5/api/reference_retcodes) of the server. MTAPIRES is a value of the UINT type.

## MTAPISTR [#](reference_types#mtapistr)

MTAPISTR is a data type used for returning strings of a fixed length. This type is an array of values wchar\_t type. The string length is limited to 260 characters (including the sign of the string end).

## MTSortFunctionPtr [#](reference_types#mtsortfunctionptr)

This type is used in the functions of object sorting and search in dynamic arrays. It is a pointer to the function of comparison of two values, to which \*left and \*right point. It is similar to the CRT-functions of sorting "qsort" and "bsearch".

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Reserved">typedef</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">int</span><span class="f_CodeExample">&nbsp;(</span><span class="f_Reserved">__cdecl</span><span class="f_CodeExample">&nbsp;</span><span class="f_Macros">*MTSortFunctionPtr</span><span class="f_CodeExample">)(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;</span><span class="f_Macros">*left</span><span class="f_CodeExample">,&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;</span><span class="f_Macros">*right</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

Depending on the comparison results, the following values are returned:

-   <0 — if left is less than right;
-   0 — if left is equal to right;
-   \>0 — if left is greater than right.

It is used in the search methods of interfaces for working with arrays. For example:

-   [IMTOrderArray](/en/docs/mt5/api/reference_trading/trading_order/imtorderarray)
-   [IMTDealArray](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray)
-   [IMTPositionArray](/en/docs/mt5/api/reference_trading/trading_position/imtpositionarray)

[Installation and Setup of PostgreSQL](/en/docs/mt5/api/sql_export_postgre)

[Journal Constants](/en/docs/mt5/api/journal)