# History Import

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_charts/ug_history_import

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Charts](/en/docs/mt4/administrator/administration/ug_charts)History Import

# History Import

Import is converting and transferring history data (charts) from external sources to the server of the system. It helps to carry out the following tasks:

-   creating a history when adding a new instrument;
-   filling in gaps in the history of any existing instrument;
-   correcting of specific history components, if necessary.

To start importing history, it is necessary to execute the "Import" command of the context menu in the ["Charts"](/en/docs/mt4/administrator/administration/ug_charts) section.

![How to Select File for Importing](/en/docs/mt4/administrator/img/win_import_history_1.png "How to Select File for Importing")

In the "File" field please select file containing data to be imported. Now you can use files of different formats: \*.hst, history data of servers and terminals of MetaTrader 3 and MetaTrader 4; \*.csv and \*.prn, text files with separators. For importing history data from text files the following data formats are supported:

-   YYYY.MM.DD HH:MM O H L C V
-   YYYY-MM-DD HH:MM O H L C V
-   YYYY/MM/DD HH:MM O H L C V
-   DD.MM.YYYY HH:MM O H L C V
-   DD-MM-YYYY HH:MM O H L C V
-   DD/MM/YYYY HH:MM O H L C V
-   YYYY.MM.DD,HH:MM O H L C V
-   YYYY-MM-DD,HH:MM O H L C V
-   YYYY/MM/DD,HH:MM O H L C V
-   DD.MM.YYYY,HH:MM O H L C V
-   DD-MM-YYYY,HH:MM O H L C V
-   DD/MM/YYYY,HH:MM O H L C V

It is also necessary to indicate:

-   Separator — separator of text file elements;
-   Skip columns — skipping columns in the LTR order;
-   Skip rows — skipping rows in the top-down order;
-   Use selected only — import only selected bars;
-   Volume — import volumes. If data files contain information concerning volumes, it is necessary to put in this flag. If not, it should be disabled;
-   Shift — time shifting in hours. This option should be used for importing data from other time zones.

The "OK" button completes the history import.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is highly recommended to import data only for your own period and instrument. Otherwise, discrepancies in values of bars and time can occur.</span></p></td></tr></tbody></table>

Limitation of the Amount of History Data

MetaTrader 4 Server has the following limitations on the history data:

-   65536 bars for M1 charts (equal to several months);
-   32768 bars for M5 charts (equal to about 6 months);
-   16384 bars for M15, M30, H1, H4, and D1 charts;
-   1024 bars for W1 charts;
-   256 bars for MN1 charts.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The above figures indicate the maximal history depth that can be stored for the indicated timeframes if the server has no more than 50 symbols. The more symbols are created on the server, the smaller is the amount of history data that can be stored.</span></p></td></tr></tbody></table>

## Copying History Data from Another Symbol

For newly created symbols without any price data, one can copy the data from another symbol in the platform. To do it, specify the name of the symbol from which you need to copy the data in the ["Source"](/en/docs/mt4/administrator/administration/ug_symbols#source) field of the new symbol. The server will automatically copy the entire price history.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Once copying is finished, delete the value of the "Source" field from the new symbol settings.</span></li><li class="p_tableatten"><span class="f_tableatten">Copying works only if the new symbol doesn't have any price data.</span></li></ul></td></tr></tbody></table>

[Charts](/en/docs/mt4/administrator/administration/ug_charts)

[Ticks](/en/docs/mt4/administrator/administration/ug_ticks)