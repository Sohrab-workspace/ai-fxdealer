# Macros

> Source: https://support.metaquotes.net/en/docs/mt5/api/smttime/smttime_macros

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[SMTTime](/en/docs/mt5/api/smttime)Macros

# Macros

The include file MT5APITime.h contains definitions of the macros of minutes and seconds that improve the readability of the code by replacing numeric expressions by clear identifiers.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">C++ ID</span></p></th><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">.NET function</span></p></th><th class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">SECONDS_IN_MINUTE</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long MinutesInDay()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">INT64(60)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The number of seconds in a minute.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">SECONDS_IN_HOUR</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long SecondsInHour()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">INT64(60*SECONDS_IN_MINUTE)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The number of seconds in an hour.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">SECONDS_IN_DAY</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long SecondsInDay()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">INT64(24*SECONDS_IN_HOUR)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The number of seconds in a day.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">SECONDS_IN_WEEK</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long SecondsInWeek()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">INT64(7*SECONDS_IN_DAY)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The number of seconds in a week.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">SECONDS_IN_MONTH</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long SecondsInMonth()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">INT64(30*SECONDS_IN_DAY)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The number of seconds in a month.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">MINUTES_IN_HOUR</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long MinutesInHour()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">(60)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Number of minutes in an hour.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">MINUTES_IN_DAY</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long MinutesInDay()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">(24*MINUTES_IN_HOUR)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Number of minutes in a day.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">MINUTES_IN_WEEK</span></p></td><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable">long MinutesInWeek()</span></p></td><td class="table" style="width:199px;"><p class="p_fortable"><span class="f_fortable">(7*MINUTES_IN_DAY)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Number of hours in a week.</span></p></td></tr></tbody></table>

[SMTTime](/en/docs/mt5/api/smttime)

[ParseTime](/en/docs/mt5/api/smttime/smttime_parsetime)