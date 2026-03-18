# SMTFormat::FormatDateTimeMsc

> Source: https://support.metaquotes.net/en/docs/mt5/api/smtformat/smtformat_formatdatetimemsc

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
                -   [Enumerations](/en/docs/mt5/api/smtformat/smtformat_enum)
                -   [FormatError](/en/docs/mt5/api/smtformat/smtformat_formaterror)
                -   [FormatDouble](/en/docs/mt5/api/smtformat/smtformat_formatdouble)
                -   [FormatMoney](/en/docs/mt5/api/smtformat/smtformat_formatmoney)
                -   [FormatPrice](/en/docs/mt5/api/smtformat/smtformat_formatprice)
                -   [FormatPrices](/en/docs/mt5/api/smtformat/smtformat_formatprices)
                -   [FormatVolume](/en/docs/mt5/api/smtformat/smtformat_formatvolume)
                -   [FormatVolumeDouble](/en/docs/mt5/api/smtformat/smtformat_formatvolumedouble)
                -   [FormatVolumeExt](/en/docs/mt5/api/smtformat/smtformat_formatvolumeext)
                -   [FormatSize](/en/docs/mt5/api/smtformat/smtformat_formatsize)
                -   [FormatVolumeOrder](/en/docs/mt5/api/smtformat/smtformat_formatvolumeorder)
                -   [FormatVolumeExtOrder](/en/docs/mt5/api/smtformat/smtformat_formatvolumeextorder)
                -   [FormatSizeOrder](/en/docs/mt5/api/smtformat/smtformat_formatsizeorder)
                -   [FormatDateTime](/en/docs/mt5/api/smtformat/smtformat_formatdatetime)
                -   [FormatDateTimeMsc](/en/docs/mt5/api/smtformat/smtformat_formatdatetimemsc)
                -   [FormatTime](/en/docs/mt5/api/smtformat/smtformat_formattime)
                -   [FormatTimeMsc](/en/docs/mt5/api/smtformat/smtformat_formattimemsc)
                -   [FormatIP](/en/docs/mt5/api/smtformat/smtformat_formatip)
                -   [FormatPositionType](/en/docs/mt5/api/smtformat/smtformat_formatpositiontype)
                -   [FormatOrderType](/en/docs/mt5/api/smtformat/smtformat_formatordertype)
                -   [FormatOrderStatus](/en/docs/mt5/api/smtformat/smtformat_formatorderstatus)
                -   [FormatOrderTypeFilling](/en/docs/mt5/api/smtformat/smtformat_formatordertypefilling)
                -   [FormatOrderTypeTime](/en/docs/mt5/api/smtformat/smtformat_formatordertypetime)
                -   [FormatOrderTypeReason](/en/docs/mt5/api/smtformat/smtformat_formatordertypereason)
                -   [FormatOrderPrice](/en/docs/mt5/api/smtformat/smtformat_formatorderprice)
                -   [FormatDealAction](/en/docs/mt5/api/smtformat/smtformat_formatdealaction)
                -   [FormatDealEntry](/en/docs/mt5/api/smtformat/smtformat_formatdealentry)
            -   [SMTMath](/en/docs/mt5/api/smtmath)
            -   [SMTSearch](/en/docs/mt5/api/smtsearch)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[SMTFormat](/en/docs/mt5/api/smtformat)FormatDateTimeMsc

# SMTFormat::FormatDateTimeMsc

Formating date and time in the SYSTEMTIME format into a string with an indication of milliseconds.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">static&nbsp;LPCWSTR&nbsp;&nbsp;</span><span class="f_Functions">SMTFormat::FormatDateTimeMsc</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CMTStr</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">&amp;str</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reference&nbsp;to&nbsp;a&nbsp;string&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;SYSTEMTIME</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">&amp;st</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reference&nbsp;to&nbsp;SYSTEMTIME</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">bool</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">useTime=true</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Flag&nbsp;of&nbsp;hours&nbsp;and&nbsp;minutes</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">bool</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">useSec=false</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Flag&nbsp;of&nbsp;seconds</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Program Parameters

&str

\[out\]  Reference to the [CMTStr](/en/docs/mt5/api/cmtstr) string object, into which information is placed.

&st

\[in\]  A reference to the SYSTEMTIME structure. The structure contains the following members:

-   wYear - a value from 1601 to 30827 that indicates the year.
-   wMonth - a value from 1 to 12 that indicates the month (1 corresponds to January).
-   wDayOfWeek - a value from 0 to 6 that indicates the weekday (0 corresponds to Sunday).
-   wDay - a value from 1 to 31 indicating the day of the month.
-   wHour - a value from 0 to 23 indicating the number of hours since midnight..
-   wMinute - a value from 0 to 59 indicating the number of minutes.
-   wSecond - a value from 0 to 59 indicating the number of seconds.
-   wMilliseconds - a value from 0 to 999 indicating the number of milliseconds.

A detailed description of the structure is available in [MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724950%28v=vs.85%29.aspx "Description of SYSTEMTIME in MSDN").

useTime=true

\[in\]  The flag of hours and minutes. If true, hours and minutes are shown in the summary line.

useSec=false

\[in\]  The flag of seconds. If true, seconds are shown in the summary line. Seconds are not shown if hours and minutes are not shown.

Return Value

Returns a constant pointer to a string in the str object.

Note

Time is shown in the YYYY.MM.DD HH:MM:SS.MSC format.

# SMTFormat::FormatDateTimeMsc

Format date and time into a string with an indication of milliseconds.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">static&nbsp;LPCWSTR&nbsp;&nbsp;</span><span class="f_Functions">SMTFormat::FormatDateTimeMsc</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CMTStr</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">&amp;str</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reference&nbsp;to&nbsp;a&nbsp;string&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ctm</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Date&nbsp;and&nbsp;Time</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">bool</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">useTime=true</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Flag&nbsp;of&nbsp;hours&nbsp;and&nbsp;minutes</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">bool</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">useSec=false</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Flag&nbsp;of&nbsp;seconds</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Program Parameters

&str

\[out\]  Reference to the [CMTStr](/en/docs/mt5/api/cmtstr) string object, into which information is placed.

ctm

\[in\]  Date and time in milliseconds since 01.01.1970.

useTime=true

\[in\]  The flag of hours and minutes. If true, hours and minutes are shown in the summary line.

useSec=false

\[in\]  The flag of seconds. If true, seconds are shown in the summary line. Seconds are not shown if hours and minutes are not shown.

Return Value

Returns a constant pointer to a string in the str object.

Note

Time is shown in the YYYY.MM.DD HH:MM:SS.MSC format.

[FormatDateTime](/en/docs/mt5/api/smtformat/smtformat_formatdatetime)

[FormatTime](/en/docs/mt5/api/smtformat/smtformat_formattime)