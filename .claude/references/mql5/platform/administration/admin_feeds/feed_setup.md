# Configuration of Data Feeds

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_feeds/feed_setup

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)Configuration of Data Feeds

# Configuration of Data Feeds

In order to add or modify a data feed, in the [corresponding section](/en/docs/mt5/platform/administration/admin_feeds) press "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" or "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit", respectively. In order to delete a data feed, press "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete". These commands are also available in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar and in the context menu.

## Common [#](feed_setup#common)

![Common](/en/docs/mt5/platform/img/data_feeds_common.png "Common")

The main information about the data feed server is specified on this tab:

-   Enable — enable/disable the data feed. Working data feeds are automatically turned off at [non-working hours](/en/docs/mt5/platform/administration/admin_time) of the server. Once the trade server starts working, the data feeds are turned on. For the data feeds running [as a service](/en/docs/mt5/platform/administration/admin_feeds/feed_service) via the "Remote gateway" module, unchecking "Enable" will lead to disconnection of platform servers from the data feed service, while the service itself will not be stopped.
-   Name — name of the data feed. Use of special characters (?, \*, <, > etc.) is not allowed, as this may cause issues while working with the data feed log files.
-   Module — name of the [data feed](/en/docs/mt5/platform/components/datafeeds) module file, as well the type of translated data (news, quotes, market books).
-   Feed server — address of the data source server.
-   Feed login — login to access the data feed server.
-   Password — password to access the data feed server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you change any of the parameters, the data feed automatically restarts to apply the changes.</span></p></td></tr></tbody></table>

### Advanced Network Settings [#](feed_setup#additional_network)

Additional network settings include history/trade server to data feed connection parameters. These settings are designed to provide the security of operation between the server and the data feed. In most cases, the settings are hidden and do not require configuration (the history server sets the required address and connection parameters).

These parameters need to be specified in two cases: when working in the [remote datafeed](/en/docs/mt5/platform/components/datafeeds/remote_datafeed) mode, and if the address/port selected for the data feed is busy. In the second case, the following message is written to the log: datafeed address 'Data freed name' already used, please setup another address for datafeed.

-   Gateway sever — address at which the data feed will receive connections from the history server. The system automatically determines available addresses of network interfaces of the history server and displays them in this field.
-   Gateway login — login that will be used for authorization of the history server on the data feed. Only a positive number can be specified as a login.
-   Password — password that will be used for authorization of the history and trade server on the data feed. The password must fulfill the security requirements (at least 6 characters long with two of three types of symbols: upper case letters, lower case letters and digits).

You can also specify the address 127.0.0.1 or localhost for the gateway server. This is the so-called [Loopback](https://en.wikipedia.org/wiki/Loopback) or a virtual network interface, which is not linked to any hardware. Such addresses are used by default when the data feed, the history server and trade servers operate on the same computer. For such addresses, the platform performs additional checks to ensure proper operation:

1.  The platform receives lists of addresses listened by the history and trade servers
2.  If at least one trade server does not have the same address as the history server, it is considered that at least one platform component is installed on another physical computer.
3.  In this case, the data feed will not be run on localhost (127.0.0.1), but on a set of listening addresses of the history server. The port specified in the "Gateway server" parameter is used for the port. For example, if the address 127.0.0.1:16387 is specified for a data feed, and the server operates on 192.168.0.1:442, the data feed will run on 192.168.0.1:16387.
4.  When connecting to the data feed, the trade server also determines which address to connect to (as in points 1 and 2): Loopback or a set of addresses. The port specified in the "Gateway server" parameter is used for the port. The following addresses are used for the set of addresses (in the order of priority):

-   Public addresses of the history server
-   Local addresses listened by the history server, which coincide with its public points (located on the same subnet).

You can also specify the address as history.server:port. For example, history.server:12345. Peculiarities of using such address:

-   -   The data feed will accept connections on the specified port of all the IP addresses the history server works on (they are specified in the list of listen addresses on the ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#bind) tab of the history sever).
    -   The data feed will accept connections from the trade servers on the public access points of the history server (they are specified in the list of public addresses on the ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#public) tab of the history server).
    -   If the list of list addresses of the history server includes 0.0.0.0, then the data feed will use this address for operation. 0.0.0.0 means listening on all addresses.

-   -   Specifying the address in this way allows automatic [switching the history server](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto) with set up local data feeds to a backup server without need to set up the addresses of the data feeds manually.

-   -   An address in this format cannot be used for [remote data feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_service) since they do not know the platform environment.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you install the <a href="/en/docs/mt5/platform/administration/admin_feeds/feed_service" class="topiclink">data feed as a service</a> on the Loopback address and then move any of the platform components to a different computer, the data feed will become unavailable for that component.</span></p></td></tr></tbody></table>

## Symbols [#](feed_setup#symbols)

![Symbols](/en/docs/mt5/platform/img/data_feeds_symbols.png "Symbols")

This tab is intended for specifying a list of symbols for translating quotes. For example, if you specify EURUSD, quotes for this symbol only will be received from this data feed.

Click "Add" and select the desired symbol or group of symbols. They can also be specified manually: one or multiple symbols separated by commas.

You can additionally use mask "\*" and the negation sign "!". For example, Cboe FX\\\*,!Cboe FX\\EURUSD — all symbols from the Cboe FX group except EURUSD. The exception does not work for a single "\*" mask. It always allows all symbols:

-   Forex\\\*,!Forex\\EURUSD — all symbols in the Forex subgroup, except EURUSD.
-   \*,!Forex\\EURUSD — all symbols. The EURUSD symbol will not be excluded.

For details, please visit the [Specification of Symbols and Groups](/en/docs/mt5/platform/administration/common_info/common_mask) section.

If the symbol row in the table is highlighted in red, then this symbol no longer exists. It may have been moved or deleted. Open the entry and edit the symbol path.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">This tab is not displayed for data feeds that transmit news only.</span></p></td></tr></tbody></table>

### Allow importing symbol settings [#](feed_setup#import)

Using this option, you can enable/disable the import of settings of the [symbols](/en/docs/mt5/platform/administration/admin_symbols) quoted and traded through the data feed. The option will only work if the relevant functionality is supported by the gateway.

Please pay attention to the following features when importing symbol settings via the gateway:

-   If the symbol does not exist in the trading platform, it will be created in the Preliminary [group](/en/docs/mt5/platform/administration/admin_symbols#groups).
-   All newly added symbols are imported with the [trading option disabled](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#trade_disabled). The platform administrator must check all the settings and manually enable trading.

-   If the symbol already exists in the platform, only the symbol settings are updated. Since trading is not executed through data feed, no update can be received for symbol trading parameters, including trading modes, execution and expiration, available order types, volume and margin settings, and options parameters.

Automatic import of symbol settings greatly simplifies the work of the platform administrator. Instead of the manual addition of all settings, you can simply move symbols from the Preliminary group the desired group and allow trading.

When the data feed changes symbol settings, the following log is added to the main trade server [journal](/en/docs/mt5/platform/administration/admin_network/network_journal): "symbol config updated". The name of the data feed is indicated as the IP address of the source in such records (the "IP" field).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When the "Allow importing symbol settings" option is enabled, the data feed can add and edit any symbols in the Preliminary\* group, even if they are not indicated in the list above.</span></p></td></tr></tbody></table>

## Translations [#](feed_setup#translation)

![Translations](/en/docs/mt5/platform/img/data_feeds_translation.png "Translations")

Information that is received from data feeds can be transformed:

-   Symbol — name of symbol at the MetaTrader 5 server;
-   Source — name of symbol in the external source (initial name of symbols). This parameter is used for adjusting the names of symbols in external data sources with the names of symbols in the platform;
-   Bid — in this field you can specify a number of points to change the Bid price on.
-   Ask — in this field you can specify a number of points to change the Ask price on.

If a parameter is not specified, default values transmitted by the data feed will be used for it.

If more than one translation settings match the same symbol on the platform side, only the one located higher in the list will be applied. For example, the following settings are available:

-   EURUSD.GW | EURUSD | Bid -1 | Ask +1
-   \*.GW | \* | Bid -2 | Ask +2

In this case, EURUSD prices will be changed by -1/+1, and the prices of all other symbols will be changed by -2/+2.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">This tab is not displayed for data feeds that transmit news only.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">When translating prices, make sure the prices are correct. Usually a negative (or zero) value is indicated for the Bid price, and a positive (or zero) value is indicated for Ask. Otherwise, you may get a negative spread.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Translations also affect the depth of market.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Find out more in the <a href="/en/docs/mt5/platform/administration/admin_gateways/gateway_translation" class="topiclink">"Symbol and Price Translation"</a> section.</span></li></ul></td></tr></tbody></table>

## Parameters [#](feed_setup#parameters)

This tab allows to specify additional parameters of a data feed that are not implemented at the "Server" tab. Presence of this parameters is stipulated by a necessity of passing additional settings to a data feed for its correct operation. For example, if a data feed receives incoming connections, allowed IP address can be specified in those parameters.

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters.png "Parameters")

The parameters are described in these fields:

-   Parameter — name of a parameter;
-   Value — value of a specified parameter.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If additional parameters are implemented then while adding a data feed they are automatically specified with default values.</span></li><li class="p_tableatten"><span class="f_tableatten">The description of possible parameters is given <a href="/en/docs/mt5/platform/components/datafeeds" class="topiclink">separately for each data feed</a> that is included in the standard &nbsp;delivery of the platform.</span></li></ul></td></tr></tbody></table>

This tab contains the following commands for managing the parameters:

-   Add — add a new parameter. A new line will appear in this window as soon as you press it. In the "Parameter" field enter the name of the parameter, in "Value" - the necessary value to assign to this parameter;
-   Edit — modify a selected parameter. The same action can be performed by double clicking on the selected field;
-   Delete — delete a selected parameter.
-   Default — set default parameters.

### Standard Parameters

All data feeds have a standard set of supported parameters:

-   NewsCategory — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups/groups_settings#news).
-   Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow. The parameter is not supported for [MetaTrader 4 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader4feeder) and [MetaTrader 5 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader5feeder).
-   Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
-   Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
-   Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.

The parameters for thinning out of price data can be used together with Quotes Delay. Allowed values are from 100 to 3000 milliseconds.

If a parameter value is incorrect, it won't be used.

### News Category and Language [#](feed_setup#news_category)

-   Usually, news categories are provided by data feeds. News providers supplement news with the information about categories to which the news belong. The same applies to the news language.
-   A news category can be additionally specified in the [News Category](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) parameter of the data feed. This is a standard parameter supported by all data feeds. The parameter is applied as follows:

-   If a data source does not provide news categories, news items will be added to the category specified in this parameter (the category will be specified in the news).
-   If the data source provides a category, then the data feed will add the "News Category" parameter value before the original category name. The resulting category will look like "\[value from News Category\] \\ \[category from data source\]". The "\\" characters in a category name are interpreted as subcategory separators. Therefore, it means that all news items are added to the category specified in the parameter, within which original categories from the data source will be used.

## Timeouts [#](feed_setup#timeouts)

![Timeouts](/en/docs/mt5/platform/img/data_feeds_timeouts.png "Timeouts")

This tab describes the behavior of data feeds in case data receipt is stopped.

-   Interval between reconnections — time period between the attempts to reconnect to the data feed;
-   Number of reconnection attempts — a number of reconnection attempts is specified in this field. If a series of reconnection attempts doesn't result in establishing a connection, attempts will be stopped for a time period specified in the field below;
-   Interval between series of reconnections — if a series of specified number of reconnection attempts doesn't result in establishing a connection, attempts will be stopped for a time period specified in this field. After this time period another series of reconnections will be performed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">An example of working with timeouts of data feeds is given in a <a href="/en/docs/mt5/platform/components/history_server/history_server_datafeeds" class="topiclink">separate section</a>.</span></p></td></tr></tbody></table>

[Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)

[Status](/en/docs/mt5/platform/administration/admin_feeds/feed_status)