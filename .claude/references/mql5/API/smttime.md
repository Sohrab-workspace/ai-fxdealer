# SMTTime

> Source: https://support.metaquotes.net/en/docs/mt5/api/smttime

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)SMTTime

# SMTTime

This class is used for working with dates and times. It contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_parsetime" class="topiclink">ParseTime</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Parse a date in the Unix time format into a tm structure.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_maketime" class="topiclink">MakeTime</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Form a date in the Unix time format from a passed tm structure.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_monthname" class="topiclink">MonthName</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the name of a month by its number.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_monthnameshort" class="topiclink">MonthNameShort</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the short name of a month by its number.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_weekbegin" class="topiclink">WeekBegin</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the week beginning by the passed date.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_daybegin" class="topiclink">DayBegin</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the day beginning by the passed date.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_monthbegin" class="topiclink">MonthBegin</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the month beginning by the passed date.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_yearbegin" class="topiclink">YearBegin</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the year beginning by the passed date.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_sttotime" class="topiclink">STToTime</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Converting a date in the SYSTEMTIME structure to the Unix time format.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_timetost" class="topiclink">TimeToST</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Converting a date in the Unix time format into the SYSTEMTIME structure.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_year" class="topiclink">Year</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the year from the date passed in the Unix time format.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_month" class="topiclink">Month</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the month from the date passed in the Unix time format.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_day" class="topiclink">Day</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the day from the date passed in the Unix time format.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_hour" class="topiclink">Hour</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the hour from the date passed in the Unix time format.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_min" class="topiclink">Min</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get minutes from the date passed in the Unix time format.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smttime/smttime_sec" class="topiclink">Sec</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get seconds from the date passed in the Unix time format.</span></p></td></tr></tbody></table>

The include file MT5APITime.h contains definitions of the [macros](/en/docs/mt5/api/smttime/smttime_macros) of minutes and seconds that improve the readability of the code by replacing numeric expressions by clear identifiers.

[Priority](/en/docs/mt5/api/cmtthread/cmtthread_priority)

[Macros](/en/docs/mt5/api/smttime/smttime_macros)