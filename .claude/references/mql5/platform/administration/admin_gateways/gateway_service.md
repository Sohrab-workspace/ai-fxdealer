# Gateway Installation as a Service

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateway_service

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
                -   [Configuration of Gateways](/en/docs/mt5/platform/administration/admin_gateways/gateways_config)
                -   [Status](/en/docs/mt5/platform/administration/admin_gateways/gateway_status)
                -   [Journal of Gateways](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway)
                -   [Positions](/en/docs/mt5/platform/administration/admin_gateways/gateway_positions)
                -   [Setup of Routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_gateways/gateway_service)
                -   [Operation on Weekend](/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend)
                -   [Symbol and Price Translation](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Gateways](/en/docs/mt5/platform/administration/admin_gateways)Setup as Service

# Gateway Installation as a Service

Gateways may run on any remote servers. They are not restricted to the server machine containing the history server.

In order to configure this gateway, you will need to copy the gateway .exe file and the GatewayAPI64.dll library (available in \[history server installation directory\]\\Gateway) to the target server. Then launch the executable file and configure connection to the gateway in the [remote mode](/en/docs/mt5/platform/administration/admin_gateways/gateway_service#setting).

In order not to run the gateway file every time when starting the server, you can install the gateway as a service. In that case, the gateway is launched automatically every time the operating system download starts.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Operation as a service is supported in all <a href="/en/docs/mt5/platform/components/gateways" class="topiclink">gateways developed by MetaQuotes</a>. Support for this mode in third-party gateways is not guaranteed, while it depends on the gateway developers.</span></p></td></tr></tbody></table>

## Service Setup

Copy the gateway .exe file and the GatewayAPI64.dll library (available in \[history server installation directory\]\\Gateway) to the target server. Save both files to the same directory.

To install the gateway as a service, run its executable file with the /install key. The following parameters may be additionally specified:

-   /name:<name> — name of the service to be registered in the system.
-   /display:<display\_name> — service full name.
-   /desc:<description> — service description.

All parameters are optional. If they are not specified, the default values are used.

Sample setup command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">DGCXGateway64.exe&nbsp;/install&nbsp;/name:dgcx</span></p></td></tr></tbody></table>

Service Start

After the setup is complete, launch the gateway service. Run the executable file with the /start key. The gateway launched in such a manner waits for the history server connection. If the history server interrupts connection (for example, in case of a restart), the gateway waits for the next connection. There is no need to restart it.

Sample launch command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">DGCXGateway64.exe&nbsp;/start</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If you need to migrate the gateway to another server, do not forget to additionally migrate the GatewayAPI64.dll library. The gateway will not work without this library.</span></li><li class="p_tableatten"><span class="f_tableatten">A gateway that runs on the remote server, as well as the GatewayAPI64.dll library, are not updated automatically when new versions of the platform are released. You will need to update these files manually.</span></li></ul></td></tr></tbody></table>

## Configuring the Service [#](gateway_service#config)

To configure the gateway service, create a text .cfg settings file having the same name and located in the same directory as the gateway executable file. For example, if the gateway executable file is named DGCXGateway64.exe, then the settings file should be named DGCXGateway64.cfg. The file should contain the following parameters:

-   name=<name> — gateway name to be displayed in the log.
-   address=<address>:<port> — address and port where the gateway waits for the history server connection. The address cannot be specified in the format of [history.server:\[port\]](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#additional_network) since the remote gateway does not know the platform environment.
-   login=<login> — login used by the history server when connecting to the gateway.
-   password=<password> — password used by the history server when connecting to the gateway.
-   timezone — time zone in minutes. The default time used for the remote gateway log is GMT+00:00. If the trade server is working in a [different time zone](/en/docs/mt5/platform/administration/admin_time#time_zone), the time of server logs and gateway logs will be different. To avoid this, specify the time zone of the trade server in the gateway settings. The time zone should be specified in minutes. For example, the value of 60 corresponds to GMT +01:00, and -60 corresponds to GMT -01:00.
-   timecorrect — daylight saving time mode: 0 — DST is not used, 1 — enable DST change. It is recommended to set the mode used on the [trade server](/en/docs/mt5/platform/administration/admin_time#daylight_saving).

Sample settings file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">name=DGCX&nbsp;Gateway</span><br><span class="f_CodeExample">address=10.1.55.159:16100</span><br><span class="f_CodeExample">login=100</span><br><span class="f_CodeExample">password=apxjjz3</span></p></td></tr></tbody></table>

## Configuring the Gateway Connection on the Server Side [#](gateway_service#setting)

[Create the gateway configuration](/en/docs/mt5/platform/administration/admin_gateways/gateways_config) via the Administrator terminal.

![Configuring Connection to a Remote Gateway](/en/docs/mt5/platform/img/gateway_service_config.png "Configuring Connection to a Remote Gateway")

Specify the following parameters:

-   Module — Remote gateway,
-   Gateway server — address and port where the gateway waits for the history server connection (set in the [configuration file](/en/docs/mt5/platform/administration/admin_gateways/gateway_service#config)).
-   Gateway login — gateway connection login set in the configuration file.
-   Password — gateway connection password set in the configuration file.

All other parameters are specified the same way as for a gateway running in normal mode.

## Stop and Uninstall

To stop the gateway service, run its executable file with the /stop key. The current connection to the history server is interrupted and the service is stopped. Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">DGCXGateway64.exe&nbsp;/stop</span></p></td></tr></tbody></table>

To uninstall the previously installed service, run the executable gateway file with the /uninstall key and \[/name:<name>\] parameter. The "name" parameter specifies the name of the uninstalled service. If the service was installed with the default name (without the "name" parameter), the /name parameter is not specified. Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">DGCXGateway64.exe&nbsp;/uninstall&nbsp;/name:dgcx</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you uncheck "Enable" in a gateway configuration, the platform servers will be disconnected from the gateway service, while the service itself will not be stopped.</span></p></td></tr></tbody></table>

[Setup of Routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing)

[Operation on Weekend](/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend)