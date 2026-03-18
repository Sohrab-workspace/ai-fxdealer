# Charts

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_charts

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
                -   [History Import](/en/docs/mt4/administrator/administration/ug_charts/ug_history_import)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Charts

# Charts

Using this section, one can modify any quotes in the database on any instrument or period, and also add new ones.

![Charts](/en/docs/mt4/administrator/img/br_charts.png "Charts")

The parameters of the request are given in fields at the bottom of the list: financial instrument, its period of time, or requesting depth.

Context Menu Commands:

-   Request Chart — requesting the chart of the selected instrument;
-   Correct History — correct history bases of instrument based on lower timeframes;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: History correction may take time and result in temporary trading halt on the trade server for the time of history correction.</span></p><p class="p_tableatten"><span class="f_tableatten">It is strongly recommended to conduct history correction during holidays.</span></p></td></tr></tbody></table>

-   Add Bar — adding a bar to the chart;
-   Update Bar — changing a bar;
-   Delete Bars — deleting bars;
-   Export — exporting charts to the file (CSV or HTM format). It is not recommended to use the \*.HTM format when exporting a large amount of charts (more than 5000 bars);
-   Import — importing data from an external file. More details can be found in the [History Import](/en/docs/mt4/administrator/administration/ug_charts/ug_history_import) section.

The "Add Bar" and "Update Bar" commands activate a window of detailed setting:

![Charts Management](/en/docs/mt4/administrator/img/win_charts_edit.png "Charts Management")

-   Date — the bar changing or creating date;
-   Volume — the volume;
-   Open — at-the-opening price;
-   High — maximum price;
-   Low — minimum price;
-   Close — at-the-close price.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">If, when creating a new bar, you write the value of an existing bar in the "Date" field, the bar will be updated.</span></li><li class="p_tableatten"><span class="f_tableatten">If the changes made are not correct, the bar will be displayed in red color in the window. In all other cases, after pressing "OK", the new or changed quote will come to the base immediately.</span></li></ul></td></tr></tbody></table>

[Order Database Optimization](/en/docs/mt4/administrator/administration/ug_orders/order_base_optimization)

[History Import](/en/docs/mt4/administrator/administration/ug_charts/ug_history_import)