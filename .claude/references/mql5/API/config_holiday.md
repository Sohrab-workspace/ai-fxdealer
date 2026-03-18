# Holiday Configuration

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_holiday

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
            -   [Holidays](/en/docs/mt5/api/config_holiday)
                -   [IMTConHoliday](/en/docs/mt5/api/config_holiday/imtconholiday)
                -   [IMTConHolidaySink](/en/docs/mt5/api/config_holiday/imtconholidaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Holidays

# Holiday Configuration

Using the functions and interfaces described in this section, you can add holidays to the work timetable of the server, both for groups of symbols and for each symbol individually. On holidays, clients can connect, view charts and history of trades, but cannot trade.

The following interfaces of holiday settings are available:

-   [IMTConHoliday](/en/docs/mt5/api/config_holiday/imtconholiday)  
    An interface for configuring holidays.
-   [IMTConHolidaySink](/en/docs/mt5/api/config_holiday/imtconholidaysink)  
    An interface for handling events of changes of holiday settings.

The below figure shows different elements of holiday configurations in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![Configuration of holidays in MetaTrader 5 Administrator](/en/docs/mt5/api/img/holiday.png "Configuration of holidays in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [The date of a holiday](/en/docs/mt5/api/config_holiday/imtconholiday/imtconholiday_year).
2.  [Beginning time](/en/docs/mt5/api/config_holiday/imtconholiday/imtconholiday_workfrom).
3.  [End time](/en/docs/mt5/api/config_holiday/imtconholiday/imtconholiday_workto).
4.  [Description of a holiday](/en/docs/mt5/api/config_holiday/imtconholiday/imtconholiday_description).
5.  [State of a holiday](/en/docs/mt5/api/config_holiday/imtconholiday/imtconholiday_mode).
6.  An indication that the holiday is [annual](/en/docs/mt5/api/config_holiday/imtconholiday/imtconholiday_year).
7.  Configuration of [symbols](/en/docs/mt5/api/config_holiday/imtconholiday/imtconholiday_symboladd) to which the holiday applies.

[OnTimeSync](/en/docs/mt5/api/config_time/imtcontimesink/imtcontimesink_ontimesync)

[IMTConHoliday](/en/docs/mt5/api/config_holiday/imtconholiday)