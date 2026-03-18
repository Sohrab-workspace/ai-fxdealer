# Configuration of History Synchronization

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_historysync

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
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
                -   [IMTConHistorySync](/en/docs/mt5/api/config_historysync/imtconhistorysync)
                -   [IMTConHistorySyncSink](/en/docs/mt5/api/config_historysync/imtconhistorysyncsink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)History Synchronization

# Configuration of History Synchronization

Using the functions and interfaces described in this section, you can manage configurations of price data synchronization with other MetaTrader 5 and MetaTrader 4 servers. They also allow to subscribe and unsubscribe from events associated with their change.

The following interfaces of group settings are available:

-   [IMTConHistorySync](/en/docs/mt5/api/config_historysync/imtconhistorysync)  
    An interface that provides access to all the main parameters of history data synchronization.
-   [IMTConHistorySyncSink](/en/docs/mt5/api/config_manager/imtconmanagersink)  
    An interface for handling events of changes in configurations of history data synchronization.

The below figure shows different elements of configuration of historical data synchronization in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![Configuration of history data in MetaTrader 5 Administrator](/en/docs/mt5/api/img/historysync.png "Configuration of history data in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Address of the server fro data synchronization](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_server).
2.  [The beginning of the period for which data are synchronized](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_from).
3.  [The end of the period for which data are synchronized](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_to).
4.  [Symbols for which data is synchronized](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_symboladd).
5.  [State of configuration](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_mode).
6.  [Type of server with which data are synchronized](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_servertype).
7.  [Data synchronization mode](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_modesync).
8.  [Time zone correction](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_timecorrection).
9.  [Taking into account quoting sessions during synchronization](/en/docs/mt5/api/config_historysync/imtconhistorysync/imtconhistorysync_flags).

[HookManagerDelete](/en/docs/mt5/api/config_manager/imtconmanagersink/imtconmanagersink_hookmanagerdelete)

[IMTConHistorySync](/en/docs/mt5/api/config_historysync/imtconhistorysync)