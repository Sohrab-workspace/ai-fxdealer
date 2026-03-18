# Data Export

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/common_info/export

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
                -   [Trading System](/en/docs/mt5/platform/administration/common_info/general_concept)
                -   [Price Data](/en/docs/mt5/platform/administration/common_info/price_data)
                -   [Working with Instructions](/en/docs/mt5/platform/administration/common_info/common_instructions)
                -   [Specifying Symbols and Groups](/en/docs/mt5/platform/administration/common_info/common_mask)
                -   [Data Export](/en/docs/mt5/platform/administration/common_info/export)
                -   [Import/Export Settings](/en/docs/mt5/platform/administration/common_info/import_export_config)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[General Information](/en/docs/mt5/platform/administration/common_info)Data Export

# Data Export

The administrator terminal can export data to \*.HTM, \*.HTML and \*.CSV files. Data can be exported from the following sections:

-   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
-   [Clients](/en/docs/mt5/platform/administration/clients)
-   [Orders](/en/docs/mt5/platform/administration/admin_orders)
-   [Deals](/en/docs/mt5/platform/administration/admin_deals)
-   [Positions](/en/docs/mt5/platform/administration/admin_positions)
-   [Charts](/en/docs/mt5/platform/administration/admin_charts)
-   [Ticks](/en/docs/mt5/platform/administration/admin_ticks)

Request data in the appropriate section to execute an export operation. Then click "![Export](/en/docs/mt5/platform/img/export_button.png "Export")Export in the context menu of this section. After that the window where one should specify a folder to save the file to will appear. Its lower part contains the block of the export settings:

![Export Settings](/en/docs/mt5/platform/img/export_settings.png "Export Settings")

The following export variants are available here:

-   All — export all information regardless of the currently selected columns;
-   Visible — export only the columns that are enabled at the moment;
-   Selected — open the window of manual selection of columns to be exported, which is described below.

In order to export the information, one should specify the name of the end file and press the "Save" button.

### Selecting Columns for Export

![Selecting Columns](/en/docs/mt5/platform/img/charts_export_columns.png "Selecting Columns")

The left part contains the available columns and the right part contains the chosen ones. The window contains the following commands:

-   Insert — add the selected column to the list of chosen ones;
-   Remove — remove the selected columns from the chosen ones. Some fields are obligatory for exporting, they cannot be deleted;
-   Up — move the added column up relatively to the others. The order of selected columns determines the sequence of data in the exported file;
-   Down — move the added column down relatively to the others;
-   Reset — restore the default settings of columns.

It is also possible to move the columns by a double-click with the left mouse button on them.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">There is a special entry "Skip column" in the list of available columns. Using it, one can create empty columns separated with the selected separator in the exported file.</span></p></td></tr></tbody></table>

[Specifying Symbols and Groups](/en/docs/mt5/platform/administration/common_info/common_mask)

[Import/Export Settings](/en/docs/mt5/platform/administration/common_info/import_export_config)