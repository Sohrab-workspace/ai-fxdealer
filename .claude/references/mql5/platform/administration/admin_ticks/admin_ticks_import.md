# Tick Data Import

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_ticks/admin_ticks_import

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
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
                -   [Import Tick Data](/en/docs/mt5/platform/administration/admin_ticks/admin_ticks_import)
                -   [Split Stocks](/en/docs/mt5/platform/administration/admin_ticks/split_ticks)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)Import Tick Data

# Tick Data Import

Tick data import has the following objectives:

-   generating a tick history when a new symbol is added;
-   filling in missing parts of an existing symbol's tick history;
-   correcting individual fragments of a tick history if needed.

Tick data can be imported both from a single file and from multiple files simultaneously (from a folder).

## Import from File

Click "![Import from File](/en/docs/mt5/platform/img/import_button.png "Import from File") Import from File" in the [context menu](/en/docs/mt5/platform/administration/admin_ticks#context) of the "Ticks" section.

![Import](/en/docs/mt5/platform/img/ticks_import_file.png "Import")

The following data should be specified here:

-   File — use the "Browse" button to specify a file to import. You can use history files of different formats: \*.tkc — MetaTrader 4 terminal and server tick data; \*.csv, \*.prn, and \*.txt — text files with separators;
-   Separator — element separator in a text file;
-   Skip columns and rows — amount of columns (from left to right) and rows (top to bottom) to be skipped during an import;
-   Shift — time shift by hours. The option is used when importing data from other time zones;
-   Use selected only — import only rows highlighted in the row view area. You can highlight rows with your mouse while holding Ctrl or Shift.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Data import is performed for a symbol currently selected in the <a href="/en/docs/mt5/platform/administration/admin_ticks" class="topiclink">"Ticks"</a> section.</span></p></td></tr></tbody></table>

## Import from Folder

You can import tick data from multiple files. Click "![Import from Folder](/en/docs/mt5/platform/img/import_folder_icon.png "Import from Folder") Import from Folder" in the [context menu](/en/docs/mt5/platform/administration/admin_ticks#context) of the "Ticks" section.

![Import from Folder](/en/docs/mt5/platform/img/ticks_import_folder.png "Import from Folder")

The following data should be specified here:

-   Folder — use the "Browse" button to select a folder containing CSV price history files to be imported. File names should match symbol names created in the trade platform. For example, EURUSD.csv, GBPUSD.csv, etc.;
-   Separator — element separator in a text file;
-   Shift — time shift by hours. The option is used when importing data from other time zones;
-   Skip columns and rows — amount of columns (from left to right) and rows (top to bottom) to be skipped during an import.

After selecting a folder, information on the found price data is displayed at the bottom of the window. Tick ![Selected symbol](/en/docs/mt5/platform/img/access_permit_icon.png "Selected symbol") the symbols to be imported and click OK.

[Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)

[Split Stocks](/en/docs/mt5/platform/administration/admin_ticks/split_ticks)