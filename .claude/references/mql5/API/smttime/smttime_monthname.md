# SMTTime::MonthName

> Source: https://support.metaquotes.net/en/docs/mt5/api/smttime/smttime_monthname

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[SMTTime](/en/docs/mt5/api/smttime)MonthName

# SMTTime::MonthName

Get the name of a month by its number.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">static&nbsp;LPCWSTR&nbsp;&nbsp;</span><span class="f_Functions">SMTTime::MonthName</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UCHAR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">month</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Month&nbsp;number</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

month

\[in\]  The number of the month starting with 0. The value 0 corresponds to January, 11 - to December.

Return Value

The name of the month.

Note

If a number outside the range 0-11 is given, the Unknown value is returned.

[MakeTime](/en/docs/mt5/api/smttime/smttime_maketime)

[MonthNameShort](/en/docs/mt5/api/smttime/smttime_monthnameshort)