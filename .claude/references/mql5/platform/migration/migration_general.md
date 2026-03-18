# Migrating the Platform General Settings

> Source: https://support.metaquotes.net/en/docs/mt5/platform/migration/migration_general

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
            -   [General Settings](/en/docs/mt5/platform/migration/migration_general)
            -   [Financial Instruments](/en/docs/mt5/platform/migration/migration_symbols)
            -   [Trade Groups](/en/docs/mt5/platform/migration/migration_group)
            -   [Import of Accounts and Trades](/en/docs/mt5/platform/migration/migration_account_trade)
            -   [Manager Accounts](/en/docs/mt5/platform/migration/migration_manager)
            -   [Data Feeds](/en/docs/mt5/platform/migration/migration_datafeed)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Migration from MetaTrader 4](/en/docs/mt5/platform/migration)General Settings

# Migrating the Platform General Settings

Here you can find out how to relocate the general settings of the platform.

## Common

The Common section of MetaTrader 4 contains quite a large number of various platform settings. In MetaTrader 5 these settings are allocated among different sections depending on their destination.

### License data and server name

You can view license data and set the server name to be displayed to clients at the [start page](/en/docs/mt5/platform/administration/admin_start) of the platform.

### Server IP address and communication port

It is specified separately for each of the platform servers on the [Network](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) tab:

![Network](/en/docs/mt5/platform/img/network_add_network.png "Network")

### Demo accounts

Demo account settings are specified separately for each [trade server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#demo) of the platform:

![Demo account settings](/en/docs/mt5/platform/img/migration_common_demo.png "Demo account settings")

Account allocation URL is set at the platform [start page](/en/docs/mt5/platform/administration/admin_start). From there you can also specify certain groups, in which clients are to open demo accounts via the terminals.

### Time zone and daylight saving time

General time settings are specified together with the operation schedule in the [Time](/en/docs/mt5/platform/administration/admin_time) section:

![Relocating time settings](/en/docs/mt5/platform/img/migration_time.png "Relocating time settings")

### End of day, swap operation and report generation

Trading days and months closing settings are located in the [trade server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day). The main distinguishing feature of the settings block is that swap operation method in MetaTrader 5 is defined separately for each [trading instrument](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps), rather than for the entire server.

![Relocating end of day and report generation](/en/docs/mt5/platform/img/migration_reports.png "Relocating end of day and report generation")

### Storing emails and ticks

MetaTrader 5 does not allow specifying email and tick data storage parameters. This data is always stored without depth limitations.

### Time optimization

The time of conducting all operations necessary to increase performance and reliability is set separately for each platform server on the [Service](/en/docs/mt5/platform/administration/admin_network/network_add_edit#service) tab.

### Protection against DDoS attacks

These settings are located in the [access server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#antiflood). Apart from the number of allowed connections, MetaTrader 5 enables you to configure the number of connection errors.

![Access](/en/docs/mt5/platform/img/network_add_access.png "Access")

### Data feed switch timeout

This parameter is located in the [history server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server):

![Data feed switch timeout](/en/docs/mt5/platform/img/network_add_history.png "Data feed switch timeout")

### Version update mode

The mode is set at the platform [start page](/en/docs/mt5/platform/administration/admin_start). In MetaTrader 5, the update settings are similar: you can disable them completely, allow updates to release versions or allow updates both to release and beta versions.

### List of IPs for access of Web services

There is no such parameter in MetaTrader 5. In order to connect to the trade platform via Web API, create a special manager account having the right to ["Enable API/FIX connection"](/en/docs/mt5/platform/administration/admin_accounts/account_edit#account) and an [API password](/en/docs/mt5/platform/administration/admin_accounts/account_edit#security).

### Paths to databases

In MetaTrader 5, these parameters are not available since data storage has been allocated among different platform components. If you need to allocate the databases, simply install the platform components on different servers.

-   Trade and client databases — \[trade server directory\]\\bases\\
-   History data — \[history server directory\]\\history\\
-   Logs — \[server directory\]\\logs\\

### Network adapter for monitoring

The network controller for monitoring is set separately for each platform server on the [Service](/en/docs/mt5/platform/administration/admin_network/network_add_edit#service) tab:

![Network adapter for monitoring](/en/docs/mt5/platform/img/network_add_service.png "Network adapter for monitoring")

## Data Centers

MetaTrader 5 [Access Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server) are similar to data centers. They also act as intermediate servers reducing the load on the main one and protecting it against DDoS attacks. Access servers can also be installed on dedicated PCs and enabled as a new access point via MetaTrader 5 Administrator.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Unlike MetaTrader 4, the fifth version of the platform does not allow direct connection to the trade server. You need at least one access server to do that.</span></p></td></tr></tbody></table>

![Relocating data center settings](/en/docs/mt5/platform/img/migration_dc.png "Relocating data center settings")

Each access server can run at multiple IP addresses of a dedicated server (if the server provides such an ability) and listen to multiple ports. If the system has multiple access servers, you can set MetaTrader 5 access server priorities on the Access tab.

In MetaTrader 5, all users (administrators, managers and traders) can connect to and work in the system only via MetaTrader 5 Access Server. Permissions tab allows you to configure access to the system to various connection types, thus allocating manager and client connections among different access servers.

Servers tab allows you to specify trade servers the current access server is used with.

In MetaTrader 5, the number of access servers is not limited.

## Access by IP

Relocation of settings for [access by an IP address](/en/docs/mt5/platform/administration/security/admin_access) from MetaTrader 4 Server to MetaTrader 5 is simple since the settings are similar in both systems.

![Relocation of settings for access by IP addresses](/en/docs/mt5/platform/img/migration_ip.png "Relocation of settings for access by IP addresses")

## Working Time

The [working time](/en/docs/mt5/platform/administration/admin_time) settings in MetaTrader 4 and MetaTrader 5 are similar:

![Relocating working time settings](/en/docs/mt5/platform/img/migration_worktime.png "Relocating working time settings")

## Holidays

[Holiday](/en/docs/mt5/platform/administration/admin_holidays) settings in MetaTrader 4 and MetaTrader 5 are similar.

![Relocating holiday settings](/en/docs/mt5/platform/img/migration_holiday.png "Relocating holiday settings")

[Migration from MetaTrader 4](/en/docs/mt5/platform/migration)

[Financial Instruments](/en/docs/mt5/platform/migration/migration_symbols)