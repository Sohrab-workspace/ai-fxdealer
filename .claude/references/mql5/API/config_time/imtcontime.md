# IMTConTime

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_time/imtcontime

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
            -   [Common](/en/docs/mt5/api/config_common)
            -   [Network](/en/docs/mt5/api/config_network)
            -   [Plugins](/en/docs/mt5/api/config_plugins)
            -   [Data Feeds](/en/docs/mt5/api/config_datafeeds)
            -   [Time](/en/docs/mt5/api/config_time)
                -   [IMTConTime](/en/docs/mt5/api/config_time/imtcontime)
                    -   [Enumerations](/en/docs/mt5/api/config_time/imtcontime/imtcontime_enum)
                    -   [Release](/en/docs/mt5/api/config_time/imtcontime/imtcontime_release)
                    -   [Assign](/en/docs/mt5/api/config_time/imtcontime/imtcontime_assign)
                    -   [Clear](/en/docs/mt5/api/config_time/imtcontime/imtcontime_clear)
                    -   [TimeZone](/en/docs/mt5/api/config_time/imtcontime/imtcontime_timezone)
                    -   [TimeServer](/en/docs/mt5/api/config_time/imtcontime/imtcontime_timeserver)
                    -   [TimeTableGet](/en/docs/mt5/api/config_time/imtcontime/imtcontime_timetableget)
                    -   [TimeTableSet](/en/docs/mt5/api/config_time/imtcontime/imtcontime_timetableset)
                    -   [Daylight](/en/docs/mt5/api/config_time/imtcontime/imtcontime_daylight)
                    -   [DaylightState](/en/docs/mt5/api/config_time/imtcontime/imtcontime_daylightstate)
                -   [IMTConTimeSink](/en/docs/mt5/api/config_time/imtcontimesink)
            -   [Holidays](/en/docs/mt5/api/config_holiday)
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
            -   [Gateways](/en/docs/mt5/api/config_gateway)
            -   [Routing](/en/docs/mt5/api/config_route)
            -   [Reports](/en/docs/mt5/api/config_report)
            -   [Mail Servers](/en/docs/mt5/api/config_email)
            -   [Messengers](/en/docs/mt5/api/config_messenger)
            -   [Automations](/en/docs/mt5/api/config_automation)
            -   [VPS](/en/docs/mt5/api/config_vps)
            -   [KYC](/en/docs/mt5/api/config_kyc)
            -   [Subscriptions](/en/docs/mt5/api/config_subscription)
            -   [Funds and ETF](/en/docs/mt5/api/config_funds)
            -   [Additional Parameters](/en/docs/mt5/api/config_param)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)[Time](/en/docs/mt5/api/config_time)IMTConTime

# IMTConTime

The IMTConTime class contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_release" class="topiclink">Release</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the current object.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_assign" class="topiclink">Assign</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a passed object to the current one.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_clear" class="topiclink">Clear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear an object.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_timezone" class="topiclink">TimeZone</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the time zone of a server.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_timeserver" class="topiclink">TimeServer</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the server address.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_timetableget" class="topiclink">TimeTableGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the working time of a trading platform for a specified week and hour.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_timetableset" class="topiclink">TimeTableSet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Set the working time of a trading platform for a specified week and hour.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_daylight" class="topiclink">Daylight</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the mode of switching to the daylight saving time.</span></p></td></tr><tr class="table"><td class="table" style="width:112px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_daylightstate" class="topiclink">DaylightState</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get data on the presence of the daylight saving time in the platform time zone.</span></p></td></tr></tbody></table>

The IMTConTime class contains one enumeration:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Enumeration</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:124px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_time/imtcontime/imtcontime_enum" class="topiclink">EnTimeTableMode</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The platform operation schedule.</span></p></td></tr></tbody></table>

[Time](/en/docs/mt5/api/config_time)

[Enumerations](/en/docs/mt5/api/config_time/imtcontime/imtcontime_enum)