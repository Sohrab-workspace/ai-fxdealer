# Restarting and Stopping Servers

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/restart

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
                -   [Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)
                -   [Hosted Access Servers](/en/docs/mt5/platform/administration/admin_network/hosted_access_server)
                -   [Restarting and Stopping Servers](/en/docs/mt5/platform/administration/admin_network/restart)
                -   [Managing Machines](/en/docs/mt5/platform/administration/admin_network/manage_machines)
                -   [Status](/en/docs/mt5/platform/administration/admin_network/network_status)
                -   [Monitor](/en/docs/mt5/platform/administration/admin_network/network_monitoring)
                -   [Journal](/en/docs/mt5/platform/administration/admin_network/network_journal)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Network cluster](/en/docs/mt5/platform/administration/admin_network)Restarting and Stopping Servers

# Restarting and Stopping Servers

A number of operations on the trading platform setup require servers being restarted afterwards. To restart a server, select the necessary one in the "Network" section and execute command "![Restart Server](/en/docs/mt5/platform/img/restart_server_button.png "Restart Server") Restart server" in the [Service](/en/docs/mt5/platform/administrator/interface/main_menu/menu_services) menu, in the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the [context menu](/en/docs/mt5/platform/administration/admin_network#context).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When the main trade server is restarted, all other components are restarted automatically.</span></p></td></tr></tbody></table>

The platform (main trade server) needs to be restarted after the following operations:

-   Addition of a new [server](/en/docs/mt5/platform/administration/admin_network/network_add_edit);
-   Changing of the [platform name](/en/docs/mt5/platform/administration/admin_start#name) visible to clients;
-   Changing of parameter "[Risk management](/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk)" in group settings;
-   Changing of [network parameters](/en/docs/mt5/platform/administration/admin_network/network_add_edit#common) of the server (address, port, login or password);
-   Changing of [access points](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network), [bindings](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) and of the list of serviced [trade servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#servers) for access servers;
-   Changing of parameters ["Digits"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#digits), ["Tick size"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#tick_size), ["Tick value"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#tick_price) and "[Market depth](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#dom)" in symbol settings;
-   Changing of the server [time zone](/en/docs/mt5/platform/administration/admin_time#time_zone);
-   Changing of the mode of switching to [Daylight Saving Time](/en/docs/mt5/platform/administration/admin_time#daylight_saving);
-   Changing of the [ranges of accounts, orders and deals](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#accounts);

-   Changing if the "[Datafeeds timeout](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server#history)" parameter in the history server settings;

-   Appearance of faults.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Servers should be restarted only on weekends and holidays, or at night when the trading activity is minimal. The restart of servers can take from several seconds to a minute. During this time connection to this server is impossible.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">One should not confuse the restart of a server with the restart of a server's system service. After changing the platform settings, restart the server using the corresponding command in MetaTrader 5 Administrator. If you just restart the trade server's service, the other components of the platform may not be notified of changes in the settings.</span></li></ul></td></tr></tbody></table>

## Stopping and Starting Servers

All MetaTrader 5 servers work as services in the operating system. If you need to temporarily stop them, you need to stop the corresponding services. This can be done in several ways:

-   in the [command line](/en/docs/mt5/platform/platform_installation/console_setup) execute the command \[server executable file\] /stop. For example, mt5history.exe \\stop.
-   in the command line execute the command sc stop \[service name\]. For example, sc stop mt5srv.
-   in the Start menu execute the command MetaTrader 5 Platform\\\[server name\]\\Stop \[server name\]. For example, MetaTrader 5 Platform\\History Server\\Stop History Server.

In the same way the servers can be started:

-   in the [command line](/en/docs/mt5/platform/platform_installation/console_setup) execute the command \[server executable file\] /start. For example, mt5history.exe \\start.
-   in the command line execute the command sc start \[service name\]. For example, sc start mt5srv.
-   in the Start menu execute the command MetaTrader 5 Platform\\\[server name\]\\Start \[server name\]. For example, MetaTrader 5 Platform\\History Server\\Start History Server.

[Hosted Access Servers](/en/docs/mt5/platform/administration/admin_network/hosted_access_server)

[Managing Machines](/en/docs/mt5/platform/administration/admin_network/manage_machines)