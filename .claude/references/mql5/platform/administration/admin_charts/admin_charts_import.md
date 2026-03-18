# Import of History Data

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_charts/admin_charts_import

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
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
                -   [Import of History Data](/en/docs/mt5/platform/administration/admin_charts/admin_charts_import)
                -   [Split Stocks](/en/docs/mt5/platform/administration/admin_charts/split_charts)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)Import of History Data

# Import of History Data

The import of history data implements the following tasks:

-   creating history when a new symbol is added;
-   filling up missing parts of history of an existing symbol;
-   correcting separate parts of history.

History data can be imported from a single file or from multiple files at once (from a folder).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Only one-minute bars are stored in the platform; all other timeframes are built in client terminals based on these bars. The use of 1-minute bars allows saving the disk space and network traffic, as well as preserve data consistency on all timeframes.</span><br><span class="f_tableatten">&nbsp;</span><br><span class="f_tableatten">You can import data from higher timeframes (for example when <a href="/en/docs/mt5/platform/migration/migration_symbols" class="topiclink">switching from MetaTrader 4</a>). However please note that lower timeframe charts will be incomplete. For example, if you import D1 data, these data will be written as 1-minute bars as of the beginning of corresponding days. The D1 and higher timeframe charts will be complete, but charts on lower timeframes will have gaps.</span></p></td></tr></tbody></table>

## Import from File

In order to start importing data, click "![Import from File](/en/docs/mt5/platform/img/import_button.png "Import from File") Import from File" in the [context menu](/en/docs/mt5/platform/administration/admin_charts#context) of the "Charts" section. After that the following window will be opened:

![Import](/en/docs/mt5/platform/img/charts_import.png "Import")

Specify the following information here:

-   File — specify a file to import using the "Browse" button. You can import files of different formats: \*.hst and \*.hsc — history data of the MetaTrader 4 servers and terminals; \*.csv, \*.prn and \*.txt — text files with separators;
-   Separator — separator of elements in a text file;
-   Skip columns and rows — number of columns (left to right) and rows (top to bottom) that should be skipped when importing;
-   Shift — time shift in hours. This option is used when importing data from other time zones;
-   Use selected only — this option allows importing only lines selected in the preview window. Strings can be selected using the mouse, holding "Ctrl" or "Shift".
-   Tick volume — if this option is not checked, the information on tick volumes will not be imported from the file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Data are imported for the symbol that is currently selected by request in the <a href="/en/docs/mt5/platform/administration/admin_charts" class="topiclink">"Charts"</a> section.</span></p></td></tr></tbody></table>

## Import from Folder

You can import history data in bulk from multiple files. To do it, click "![Import from Folder](/en/docs/mt5/platform/img/import_folder_icon.png "Import from Folder") Import from Folder" in the [context menu](/en/docs/mt5/platform/administration/admin_charts#context) of the "Charts" section. After that the following window will be opened:

![Import Folder](/en/docs/mt5/platform/img/charts_import_folder.png "Import Folder")

Specify the following information here:

-   Folder — using the "Browse" button choose a folder containing history data files that should be imported. Only CSV format of data files is supported. File names must correspond to the names of the symbols created in the trading platform. For example, EURUSD.csv, GBPUSD.csv, etc.;
-   Separator — separator of elements in a text file;
-   Skip columns and rows — number of columns (left to right) and rows (top to bottom) that should be skipped when importing;
-   Shift — time shift in hours. This option is used when importing data from other time zones;
-   Tick volume — if this option is not checked, the information on tick volumes will not be imported from the files.

Once a folder is selected, the recognized price data will be displayed in the bottom part of the window. Selected symbols that should be imported by putting a check mark against them and click OK.

## Record Format

The following types of entries in text formats are supported by import:

-   YYYY.MM.DD HH:MM O H L C V
-   YYYY-MM-DD HH:MM O H L C V
-   YYYY/MM/DD HH:MM O H L C V
-   DD.MM.YYYY HH:MM O H L C V
-   DD-MM-YYYY HH:MM O H L C V
-   DD/MM/YYYY HH:MM O H L C V
-   MM.DD.YYYY HH:MM O H L C V
-   MM-DD-YYYY HH:MM O H L C V
-   MM/DD/YYYY HH:MM O H L C V
-   YYYY.MM.DD,HH:MM O H L C V
-   YYYY-MM-DD,HH:MM O H L C V
-   YYYY/MM/DD,HH:MM O H L C V
-   DD.MM.YYYY,HH:MM O H L C V
-   DD-MM-YYYY,HH:MM O H L C V
-   DD/MM/YYYY,HH:MM O H L C V
-   MM.DD.YYYY,HH:MM O H L C V
-   MM-DD-YYYY,HH:MM O H L C V
-   MM/DD/YYYY,HH:MM O H L C V
-   YYYYMMDD,HHMMSS,O,H,L,C,V

Time can be also specified in the format HH:MM:SS.

## Copying History Data from Another Symbol

For newly created symbols without any price data, one can copy the data from another symbol in the platform. To do it, specify the name of the symbol from which you need to copy the data in the [Source](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#source) field of the new symbol. The server will automatically copy the entire price history.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Once copying is finished, delete the value of the Source field from the new symbol settings.</span></li><li class="p_tableatten"><span class="f_tableatten">Copying works only if the new symbol doesn't have any price data. To make sure there are no historical prices available, check the history\[symbol_name] directory on the history server. This directory must be empty.</span></li></ul></td></tr></tbody></table>

[1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)

[Split Stocks](/en/docs/mt5/platform/administration/admin_charts/split_charts)