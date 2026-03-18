# Symbols Import

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_symbols/ug_symbols_import

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
                -   [Symbols Import](/en/docs/mt4/administrator/administration/ug_symbols/ug_symbols_import)
                -   [Margin Calculation](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation)
                -   [Swap Calculation](/en/docs/mt4/administrator/administration/ug_symbols/swap_calculation)
                -   [Profit Calculation](/en/docs/mt4/administrator/administration/ug_symbols/profit_calculation)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Symbols](/en/docs/mt4/administrator/administration/ug_symbols)Symbols Import

# Symbols Import

Import is intended for prompt transfer of financial instruments (symbols) from other servers of MetaTrader 3 or MetaTrader 4. It can be useful, for example, when changing MetaTrader 3 for MetaTrader 4, creating a new server or in other similar cases. When importing, not only symbols are transferred, but also [all their settings](/en/docs/mt4/administrator/administration/ug_symbols#setup_symbol). To start importing an instrument, it is necessary to execute the "Import" context menu command in the ["Symbols"](/en/docs/mt4/administrator/administration/ug_symbols) section.

![Connection Setting for Financial Instrument Import](/en/docs/mt4/administrator/img/win_symbols_import_1.png "Connection Setting for Financial Instrument Import")

The parameters of connection to the exporting server should be given in this window:

-   Server — IP address and port of the server from which instruments are imported. It must appear as \[IP or server domain\] : \[port number\] ;
-   Server Type — type of the server (MetaTrader 3 or MetaTrader 4). It is necessary to know the type of the exporting server exactly since the necessary information is kept differently in different servers;
-   Login — the account login enabling to connect to the server. Any trader's account is appropriate for importing;
-   Password — access password.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: When importing data from MetaTrader 3, such parameters as <a href="/en/docs/mt4/administrator/administration/ug_symbols#currency" class="topiclink">Currency</a>, <a href="/en/docs/mt4/administrator/administration/ug_symbols#background" class="topiclink">Background</a> and <a href="/en/docs/mt4/administrator/administration/ug_symbols#swap_enable" class="topiclink">Swaps Enable</a> will be set "on default". The matter is that instruments in MetaTrader 3 have less settings than MetaTrader 4.</span></p></td></tr></tbody></table>

All desired instruments must be ticked in the following window. "Select All" — select all accessible instruments.

![Selecting Financial Instruments](/en/docs/mt4/administrator/img/win_symbols_import_2.png "Selecting Financial Instruments")

After pressing the "Done" button, the immediate import is performed, and new instruments appear in the ["Symbols"](/en/docs/mt4/administrator/administration/ug_symbols) section. To start operation with imported instruments, it is necessary to restart the server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">You may not start operations without checking all imported instruments! Particularly, you should pay attention to: <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_symbol" class="topiclink">basic settings</a>, <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_filter" class="topiclink">filtering parameters</a>, <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_calculation" class="topiclink">calculation terms</a>, <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_swaps" class="topiclink">swaps</a>, and <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_sessions" class="topiclink">working hours</a></span></li><li class="p_tableatten"><span class="f_tableatten">To start operation with newly imported instruments, it is necessary to restart the server.</span></li><li class="p_tableatten"><span class="f_tableatten">You should always check the possibility of delivery quotes for the imported instruments by feeders.</span></li><li class="p_tableatten"><span class="f_tableatten">If you try to import an already existing instrument, its parameters will be rewritten. In this case, the server will operate with the changed instrument without restarting.</span></li></ul></td></tr></tbody></table>

[Symbols](/en/docs/mt4/administrator/administration/ug_symbols)

[Margin Calculation](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation)