# Server and Data Feeds Restart

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/server_commands/ug_server_restart

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
            -   [Server and Data Feeds Restart](/en/docs/mt4/administrator/server_commands/ug_server_restart)
            -   [Synchronization of Charts](/en/docs/mt4/administrator/server_commands/ug_sync)
            -   [Starting LiveUpdate](/en/docs/mt4/administrator/server_commands/ug_liveupdate)
            -   [Activation](/en/docs/mt4/administrator/server_commands/activation)
        -   [Administration](/en/docs/mt4/administrator/administration)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Server Administration Commands](/en/docs/mt4/administrator/server_commands)Server and Data Feeds Restart

# Server and Data Feeds Restart

Server should be restarted after:

-   a new [Data Center (access point)](/en/docs/mt4/administrator/administration/ug_data_server) has been added;
-   a new [Users Group](/en/docs/mt4/administrator/administration/ug_groups) has been added;
-   new [financial instruments](/en/docs/mt4/administrator/administration/ug_symbols) have been added;

-   the Percentage parameter in financial symbols' [margin settings](/en/docs/mt4/administrator/administration/ug_symbols#initial_margin) has been updated;

-   enabling/disabling [plugins](/en/docs/mt4/administrator/administration/ug_plugins);

-   technical failures occur.

The server restart is performed in two steps: shutdown and repeated start. At the shutdown, all connections are broken, all feeders and requests to dealers are terminated. The restart initiates feeders, client bases, orders, and historical data.

You can restart server via "Services — Restart Server" menu command or ![Server Restart](/en/docs/mt4/administrator/img/ic_server_restart.png "Server Restart") button of the toolbar.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: It is necessary to reconnect to the server after restarting. Since the server restart can take from several seconds to one minute, it is impossible to login to the server within this period of time.</span></p></td></tr></tbody></table>

## Data Feeds Restart [#](ug_server_restart#feeds_reset)

The data feeds restart is applied when technical problems occur regarding quotes and news receiving. The server will stop operation of all data feeds and restart them should this occur.

You can reset them via the "Services — Reset Datafeeds" menu command or ![Reset Data Feeds](/en/docs/mt4/administrator/img/ic_feeds_reset.png "Reset Data Feeds") button of the toolbar.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: When <a href="/en/docs/mt4/administrator/administration/ug_data_feeds#data_feeds_setup" class="topiclink">adding a new feeder or changing the priority (position in the list) </a>of any data feed, the automatic resetting will start. It is not recommended to change the priorities of feeders unless absolutely necessary!</span></p></td></tr></tbody></table>

[Server Administration Commands](/en/docs/mt4/administrator/server_commands)

[Synchronization of Charts](/en/docs/mt4/administrator/server_commands/ug_sync)