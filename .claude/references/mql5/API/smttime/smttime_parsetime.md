# SMTTime::ParseTime

> Source: https://support.metaquotes.net/en/docs/mt5/api/smttime/smttime_parsetime

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
            -   [CMTSync](/en/docs/mt5/api/cmtsync)
            -   [CMTThread](/en/docs/mt5/api/cmtthread)
            -   [SMTTime](/en/docs/mt5/api/smttime)
                -   [Macros](/en/docs/mt5/api/smttime/smttime_macros)
                -   [ParseTime](/en/docs/mt5/api/smttime/smttime_parsetime)
                -   [MakeTime](/en/docs/mt5/api/smttime/smttime_maketime)
                -   [MonthName](/en/docs/mt5/api/smttime/smttime_monthname)
                -   [MonthNameShort](/en/docs/mt5/api/smttime/smttime_monthnameshort)
                -   [WeekBegin](/en/docs/mt5/api/smttime/smttime_weekbegin)
                -   [DayBegin](/en/docs/mt5/api/smttime/smttime_daybegin)
                -   [MonthBegin](/en/docs/mt5/api/smttime/smttime_monthbegin)
                -   [YearBegin](/en/docs/mt5/api/smttime/smttime_yearbegin)
                -   [STToTime](/en/docs/mt5/api/smttime/smttime_sttotime)
                -   [TimeToST](/en/docs/mt5/api/smttime/smttime_timetost)
                -   [Year](/en/docs/mt5/api/smttime/smttime_year)
                -   [Month](/en/docs/mt5/api/smttime/smttime_month)
                -   [Day](/en/docs/mt5/api/smttime/smttime_day)
                -   [Hour](/en/docs/mt5/api/smttime/smttime_hour)
                -   [Min](/en/docs/mt5/api/smttime/smttime_min)
                -   [Sec](/en/docs/mt5/api/smttime/smttime_sec)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[SMTTime](/en/docs/mt5/api/smttime)ParseTime

# SMTTime::ParseTime

Parse a date in the Unix time format into a tm structure.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">static&nbsp;bool&nbsp;&nbsp;</span><span class="f_Functions">SMTTime::ParseTime</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">ctm</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Date</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">tm</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">*ttm</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;tm&nbsp;structure</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

ctm

\[in\]  Date in seconds that have elapsed since 01.01.1970.

\*ttm

\[out\]  The tm structure that contains the following members:

-   tm\_sec contains a value from 0 to 59 indicating the number of seconds.
-   tm\_min contains a value from 0 to 59 indicating the number of minutes.
-   tm\_hour contains a value from 0 to 23 indicating the number of hours since midnight.
-   tm\_mday contains a value from 1 to 31 indicating the day of the month.
-   tm\_mon contains a value from 0 to 11 indicating the month number (0 corresponds to January).
-   tm\_year indicates the number of years that have elapsed since 1990.
-   tm\_wday contains a value from 0 to 6 indicating the number if the weekday (0 corresponds to Sunday).
-   tm\_yday contains a value from 0 to 365 that indicates the number of days since January 1.
-   tm\_isdst indicates the use of the daylight saving time (true - enabled, false - disabled).

For more information about the tm structure please read [MSDN](https://msdn.microsoft.com/en-us/library/windows/hardware/ff567981%28v=vs.85%29.aspx "Description of the tm structure in MSDN").

Return Value

In case of a successful parse returns true, otherwise returns false.

[Macros](/en/docs/mt5/api/smttime/smttime_macros)

[MakeTime](/en/docs/mt5/api/smttime/smttime_maketime)