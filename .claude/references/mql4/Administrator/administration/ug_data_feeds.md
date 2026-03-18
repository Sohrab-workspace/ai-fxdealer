# Data Feeds

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_data_feeds

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
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Data Feeds

# Data Feeds

MetaTrader Server allows to connect external data feeds in the "hot" replace mode using the plugin modules (".feed" files). If necessary, you can add support for any data feed just having written your own support module. More details can be found in the article ["DataFeed API: Writing Your Own Data Feeds"](https://support.metaquotes.net/en/articles/2) in [Support Center](https://support.metaquotes.net/).

![Data Feeds](/en/docs/mt4/administrator/img/br_data_feeds.png "Data Feeds")

Main characteristics of each feeder are shown in the program window:

-   Vendor — the data vendor;
-   Source — the data provided ("Quotes", "News", or "Quotes and News");
-   Server — server address and port.

Location of the feeder in the list defines its priority: the higher it is located the higher its priority is. It does not mean that only one or two feeders operate: the server receives information from all data feeds continuously and simultaneously. This allows, in the case of problems, to switch to other feeders immediately. For example, some data feeds provide quotes for the same symbol from different financial companies; the priority defines which of the feeders will be used. If the current data feed does not provide the necessary information within a certain period of time (indicated in the Common section — ["Feeder Switch Timeout"](/en/docs/mt4/administrator/administration/ug_options#feeder_switch) field), the server will automatically switch to the next feeder in the list providing information for the same symbol. However, as soon as the data resumes from the data feed having a higher priority, the server will switch back to using it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When data feeds priority is changed (position in the list) they are restarted automatically. After that they continue working according to the new priority.</span></p></td></tr></tbody></table>

When a feeder is added or changed, a setting window will open:

![Data Feeds Setting Window](/en/docs/mt4/administrator/img/win_data_feeds.png "Data Feeds Setting Window")

-   Enable — enabling/disabling a feeder;
-   Name — the name of the plugin module and the type of the data feed (Quotes, News, or Quotes and News). The "Quotes and News" type means that the feeder provides both quotes and news. Use of special characters (?, \*, <, > etc.) in names is not allowed, as this may cause issues while working with the data feed log files.
-   File — file name for plugin module;
-   Server — the server address and port for connection;
-   Login & Password — login and access password;
-   Keywords — the list of keywords separated by commas. In case of quotes feeders keywords can be used as symbol filters. For example, if EURUSD is specified in this filed, this data feed will translate quotes only for the indicated symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The mask containing wildcard characters '*' or '!' can be used in this field. For example, if '!EURUSD,EUR*' is specified, all quotes for EUR pairs except EURUSD will be translated.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If a non-existent symbol (or set of symbols) is specified, it will be assumed that filtering is disabled and the data feed will provide data on all available symbols.</span></li></ul></td></tr></tbody></table>

-   Language — the language to mark the news translated by the data feed. By default the "Any language" flag is set to news - this means that the news will match any language. Filtering news by languages can be set for [groups of accounts](/en/docs/mt4/administrator/administration/ug_groups#language).
-   Idle timeout — the period of time after which the server reconnects to the data feed if it is not responding (do not confuse with the ["Feeder Switch Timeout"](/en/docs/mt4/administrator/administration/ug_options#feeder_switch) parameter, that is used to switch to another feeder when there are no quotes);
-   reconnect after — time period between first attempts to reconnect to the feeder;
-   Sleep For — the time period between attempts used after first failed attempts to reconnect (indicated in the Attempts field);
-   Attempts — the number of the first attempts to reconnect;
-   Description — the data feed description. It is highly recommended to read the data feed description before use;
-   Journal — journal of the feeder.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: A new data feed starts operating immediately after it has been added.</span></p></td></tr></tbody></table>

[Managers](/en/docs/mt4/administrator/administration/ug_managers)

[Backup](/en/docs/mt4/administrator/administration/ug_backup)