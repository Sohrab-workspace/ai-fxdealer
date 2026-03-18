# Data Feed Configuration

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_datafeeds

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
                -   [IMTConFeeder](/en/docs/mt5/api/config_datafeeds/imtconfeeder)
                -   [IMTConFeederModule](/en/docs/mt5/api/config_datafeeds/imtconfeedermodule)
                -   [IMTConFeederTranslate](/en/docs/mt5/api/config_datafeeds/imtconfeedertranslate)
                -   [IMTConFeederSink](/en/docs/mt5/api/config_datafeeds/imtconfeedersink)
            -   [Time](/en/docs/mt5/api/config_time)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Data Feeds

# Data Feed Configuration

To receive quotes and news in the online trading platform, data feeds are used. Data feeds transmit information to the history server, from which they are translated to access points (data centers) and terminals.

The following interfaces of data feeds are available:

-   [IMTConFeeder](/en/docs/mt5/api/config_datafeeds/imtconfeeder)  
    An interface for configuring data feeds.
-   [IMTConFeederModule](/en/docs/mt5/api/config_datafeeds/imtconfeedermodule)  
    An interface for managing the parameters of data feed modules.
-   [IMTConFeederTranslate](/en/docs/mt5/api/config_datafeeds/imtconfeedertranslate)  
    An interface for managing conversion of symbols and quotes received from a data feed.
-   [IMTConFeederSink](/en/docs/mt5/api/config_datafeeds/imtconfeedersink)  
    An interface for handling events of changes in data feed configurations.

The below figure shows different elements of data feed configuration in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![Working with data feeds in MetaTrader 5 Administrator](/en/docs/mt5/api/img/datafeeds.png "Working with data feeds in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [The name of the data feed configuration](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_name).
2.  [Information supplied by the data feed](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_flags).
3.  [The server from which the data feed transmits information](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_feedserver).
4.  Status of the data feed.
5.  [State of the data feed](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_mode).
6.  [The name of the data feed module](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_module).
7.  [Server address of the gateway, on which the data feed accepts history server connections](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_gatewayserver).
8.  [The login of the gateway server for history server connection](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_gatewaylogin).
9.  [The password of the gateway server for history server connection](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_gatewaypassword).
10.  [Login to connect to the source server](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_feedlogin).
11.  [Password to connect to the source server](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_feedpassword).
12.  [Setup of symbols for transmitting quotes](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_symboladd).
13.  [Setup of conversion of transmitted quotes](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_translateadd).
14.  [Setup of the data feed parameters](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_parameteradd).
15.  [Timeout setup](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_timeout).

[OnPluginSync](/en/docs/mt5/api/config_plugins/imtconpluginsink/imtconpluginsink_onpluginsync)

[IMTConFeeder](/en/docs/mt5/api/config_datafeeds/imtconfeeder)