# Data Feed Installation as a Service

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_feeds/feed_service

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
                -   [Configuration of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_setup)
                -   [Status](/en/docs/mt5/platform/administration/admin_feeds/feed_status)
                -   [Journal of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed)
                -   [Restarting Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/data_feed_restart)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_feeds/feed_service)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)Setup as Service

# Data Feed Installation as a Service

Data feeds can be running on any remote server different from the server where the history server is installed.

In order to configure this data feed, you will need to copy the data feed .exe file and the GatewayAPI64.dll library (available in \[history server installation directory\]\\Datafeed) to the target server. Then launch the executable file and configure connection to the data feed in the [remote mode](/en/docs/mt5/platform/administration/admin_feeds/feed_service#settings).

To avoid the necessity to start the data feed file manually every time when starting the server, you should install the data feed as a service. In that case, the data feed is launched automatically every time the operating system download starts.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Operation as a service is supported in <a href="/en/docs/mt5/platform/components/datafeeds" class="topiclink">all data feeds developed by MetaQuotes</a>, except for those that are built directly into the platform (do not have a separate executable file), such as MetaTrader 4 Feeder, MetaTrader 5 Feeder and MetaTrader 5 UniFeeder. Support for this mode in third-party data feeds is not guaranteed, while it depends on the gateway developers.</span></p></td></tr></tbody></table>

## Service Setup

Copy the data feed .exe file and the GatewayAPI64.dll library (available in \[history server installation directory\]\\Datafeed) to the target server. Save both files to the same directory.

To install the data feed in the service mode, run the data feed .exe file with the /install key. The following parameters may be additionally specified:

-   /name:<name> — name of the service to be registered in the system.
-   /display:<display\_name> — service full name.
-   /desc:<description> — service description.

All parameters are optional. If they are not specified, default values will be used.

Sample setup command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">feeder64.exe&nbsp;/install&nbsp;/name:mt5feeder</span></p></td></tr></tbody></table>

Service Start

After the installation, launch the data feed service by launching its .exe file with the /start switch. The data feed launched in such a manner waits for the history server connection. If the history server interrupts connection (for example, in case of a restart), the data feed waits for the next connection. There is no need to restart it.

Sample launch command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">feeder64.exe&nbsp;/start</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If you need to migrate the data feed to another server, do not forget to additionally migrate the GatewayAPI64.dll library. The data feed will not work without this library.</span></li><li class="p_tableatten"><span class="f_tableatten">The data feed that runs on the remote server, as well as the GatewayAPI64.dll library, are not updated automatically when new versions of the platform are released. You will need to update these files manually.</span></li></ul></td></tr></tbody></table>

## Configuring the Service [#](feed_service#config)

To configure the data feed service, create a text .cfg settings file having the same name and located in the same directory as the data feed .exe file. For example, if the executable file of the data feed is MetaTrader5Feeder64.exe, the configuration file should be named MetaTrader5Feeder64.cfg. The file should contain the following parameters:

-   name=<name> — the name of the data feed. This name will be shown in the Journal.
-   address=<address>:<port> — address and port where the data feed waits for the history server connection. The address cannot be specified in the format of [history.server:\[port\]](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#additional_network) since the remote data feed does not know the platform environment.
-   login=<login> — login used by the history server when connecting to the data feed.
-   password=<password> — password used by the history server when connecting to the data feed.
-   timezone — time zone in minutes. The default time used for the remote data feed log is GMT+00:00. If the trade server is working in a [different time zone](/en/docs/mt5/platform/administration/admin_time#time_zone), the time of server logs and data feed logs will be different. To avoid this, specify the time zone of the trade server in the data feed settings. The time zone should be specified in minutes. For example, the value of 60 corresponds to GMT +01:00, and -60 corresponds to GMT -01:00.
-   timecorrect — daylight saving time mode: 0 — DST is not used, 1 — enable DST change. It is recommended to set the mode used on the [trade server](/en/docs/mt5/platform/administration/admin_time#daylight_saving).

Sample settings file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">name=My&nbsp;Feeder</span><br><span class="f_CodeExample">address=10.1.55.159:16100</span><br><span class="f_CodeExample">login=100</span><br><span class="f_CodeExample">password=apxjjz3</span></p></td></tr></tbody></table>

## Configuring the Data Feed Connection on the Server Side [#](feed_service#settings)

[Create a configuration](/en/docs/mt5/platform/administration/admin_feeds/feed_setup) of the data feed via the administrator terminal.

![Configuring Connection to a Remote Data Feed](/en/docs/mt5/platform/img/feeder_service_config.png "Configuring Connection to a Remote Data Feed")

Specify the following parameters:

-   Module — Remote datafeed,
-   Gateway server — address and port where the data feed waits for the history server connection (set in the [configuration file](/en/docs/mt5/platform/administration/admin_feeds/feed_service#config)).
-   Gateway login — data feed connection login set in the configuration file.
-   Password — data feed connection password set in the configuration file.

All other parameters are specified the same way as for a data feed running in normal mode.

## Stop and Uninstall

To stop a data feed service, run its executable file with the /stop key. The current connection to the history server is interrupted and the service is stopped. An example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">feeder64.exe&nbsp;/stop</span></p></td></tr></tbody></table>

To uninstall the previously installed service, run the data feed .exe file with the /uninstall key and \[/name:<name>\] parameter. The "name" parameter specifies the name of the service that you want to uninstall. If the service was installed with the default name (without the "name" parameter), the /name parameter is not specified. An example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">feeder64.exe&nbsp;/uninstall&nbsp;/name:dgcx</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you uncheck "Enable" in a data feed configuration, the platform servers will be disconnected from the data feed service, while the service itself will not be stopped.</span></p></td></tr></tbody></table>

[Restarting Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/data_feed_restart)

[Plugins](/en/docs/mt5/platform/administration/admin_plugins)