# Synchronization

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_synchronization

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Synchronization

# Synchronization

Synchronization is used for quickly filling missing data through other MetaTrader servers. This function has been introduced into our platforms to solve the problem of missing data.

![Synchronization Setup](/en/docs/mt4/administrator/img/br_synchronization.png "Synchronization Setup")

The "Add" and "Edit" context menu commands, the corresponding commands of the "Edit" menu, and ![Add](/en/docs/mt4/administrator/img/ic_config_add.png "Add") and ![Edit](/en/docs/mt4/administrator/img/ic_config_edit.png "Edit") buttons of the toolbar will activate the synchronization setup window:

![Synchronization Setup](/en/docs/mt4/administrator/img/win_synchronization.png "Synchronization Setup")

-   Enable — enabling/disabling using the server for synchronization;
-   Server — the server address from which data will be downloaded;
-   Mode — data update mode (Add — adding missing data; Update — changing the existing data; Replace — replacing all data and store the missing ones);
-   Time zone correction — function of correcting time zones. It allows to easily synchronize history data by MetaTrader servers located in different time zones. There are two variants of operation of this function:

-   Auto detect — If this variant is selected, the time difference will be detected automatically. Besides, it will also be detected, whether the option of [Daylight saving time](/en/docs/mt4/administrator/administration/ug_options#dst) is enabled on both servers.
-   Setting a precise correction — when this variant is chosen, history data will be shifted strictly by this value, not taking into account the DST.

-   Symbols — the list of symbols (separated with commas) to be updated. Empty list means that all data must be used;
-   Limits — setting time limits when charts synchronizing.

To synchronize data, it is necessary to execute the "Operations — Synchronize Historical Charts" command or press the ![Charts Synchronization](/en/docs/mt4/administrator/img/ic_bases_synchronize.png "Charts Synchronization") button of the toolbar.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">To perform successful synchronization, it is necessary to use only those servers which operate in the same time zone and have the same parameters of checking the Daylight Saving Time as your server.</span></li><li class="p_tableatten"><span class="f_tableatten">The server to synchronize with must have at least one demo group (even a disabled one) with all necessary symbol types permitted in its settings.</span></li></ul></td></tr></tbody></table>

It is very important that not only charts are synchronized, but also system time of the computer is correct. A standard network protocol of time synchronization TIME is used for this purpose (the [Common](/en/docs/mt4/administrator/administration/ug_options) section). Time synchronization is performed every start of the server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: You may not use time synchronization programs developed by any outside producers! In this case, the mistiming of quotes delivery is possible (messages of the server journal having the Old tick USDCHF x.xxxx / x.xxxx appearance).</span></p></td></tr></tbody></table>

[Live Update](/en/docs/mt4/administrator/administration/ug_live_update)

[Plugins](/en/docs/mt4/administrator/administration/ug_plugins)