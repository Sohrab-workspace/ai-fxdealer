# Charts

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_charts

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)1 Minute History Charts

# Charts

This section allows managing price data of financial instruments. The history of prices is stored in the platform in the form of one-minute bars and [ticks](/en/docs/mt5/platform/administration/admin_ticks). One-minute bars are used for displaying history charts in client terminals. Such charts allow traders to analyze price dynamics, perform technical analysis and test trading robots.

Only one-minute bars are stored in the platform; all other timeframes are built in client terminals (including mobile and web platforms) using these bars. The use of 1-minute bars allows saving the disk space and network traffic, as well as preserve data consistency on all timeframes.

The trading platform ([the history server](/en/docs/mt5/platform/components/history_server)) builds bars using ticks received from datafeeds and gateways. Depending on the ["Charts" parameter of a trading symbol](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#charts), bars are based on Bid or Last prices (the price of the last executed trade). As a rule, charts of exchange instruments with the enabled [Market Depth](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#dom) feature are based on the Last price.

Bars are only formed and accumulated using newly received ticks. To meet traders' needs, it is highly recommended to find a high-quality deep history of all your financial instruments and [import](/en/docs/mt5/platform/administration/admin_charts/admin_charts_import) it to the platform. The history can also be [synchronized](/en/docs/mt5/platform/administration/admin_synchronization) with another MetaTrader 4/5 server.

![History Data](/en/docs/mt5/platform/img/charts.png "History Data")

Each bar can store the following data:

-   Date — the bar formation date (minute).
-   Open — the price at the beginning of bar formation (the beginning of the minute).
-   High — the highest price inside the bar.
-   Low — the lowest price inside the bar.
-   Close — the price at the end of bar formation (the end of the minute).
-   Tick Volume — the number of ticks received during bar formation. The variable only counts the ticks that change the price based on which the bar is constructed (Bid or Last, depending on [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#charts)). Several ticks in a row with the same price will be counted as one.
-   Volume — the real volume of trades executed during bar formation.
-   Spread — the lowest symbol spread recorded during the bar formation time.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#charts" class="topiclink">chart constructing mode</a> is changed, the accumulated price history will not be re-built. Settings only apply to new received data.</span></li><li class="p_tableatten"><span class="f_tableatten">For the symbols, the charts of which are based on Bid prices, the history server does no accept Last prices and volumes from <a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">gateways</a> and <a href="/en/docs/mt5/platform/administration/admin_feeds" class="topiclink">datafeeds</a>. These <a href="/en/docs/mt5/platform/administration/admin_ticks" class="topiclink">ticks</a> are not saved and are not delivered to other components of the platform.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The price data received from gateways and data feeds is stored under [history server installation directory\history]. If the free disk space on the history server drops below 2 gigabytes, no saving of new arriving price data is performed. This prevents data from occupying of all available disk space. Thus, the overall server performance is preserved. If data cannot be written to disk, the following message is added into the history servers log: "'EURUSD' save skipped due not enough free space on disk", "bars and ticks are not saved due not enough free space on disk", "synchronization was stopped due not enough free space on disk ". In this case, you should immediately increase free disk space on the server.</span></li></ul></td></tr></tbody></table>

## Requesting Data [#](admin_charts#request)

In order to view or edit bars of a symbol, you should request them.

-   Choosing a symbol  
    In the first field, specify one of financial symbols from the platform. The symbol can be specified manually or chosen from the list which opens by clicking on the down arrow.
-   Choosing a period  
    Then specify the period, for which you want to request bars. You can choose one of the predefined periods by clicking on ![Periodicity](/en/docs/mt5/platform/img/calendar.png "Periodicity")(today, last 3 days, last week, last month, last 3 months, last 6 months or the entire history). You can also specify a custom time interval.
-   Request execution  
    To receive the history data, click "Request" or choose the same command from the context menu ![Request](/en/docs/mt5/platform/img/request_button.png "Request").

## Adding and Editing Data [#](admin_charts#add_edit)

To add a bar, click "![Add bar](/en/docs/mt5/platform/img/add_button.png "Add bar") Add Bar" in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit#add) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu. To edit a bar, click "![Edit bar](/en/docs/mt5/platform/img/edit_button.png "Edit bar")Edit Bar" or double-click on it.

![Adding/editing a quote](/en/docs/mt5/platform/img/chart_add_edit.png "Adding/editing a quote")

Each bar can store the following data:

-   Date — the bar formation date (minute).
-   Open — the price at the beginning of bar formation (the beginning of the minute).
-   High — the highest price inside the bar.
-   Low — the lowest price inside the bar.
-   Close — the price at the end of bar formation (the end of the minute).
-   Tick Volume — the number of ticks received during bar formation.
-   Volume — the real volume of trades executed during bar formation.
-   Spread — the lowest symbol spread recorded during the bar formation time.

To delete a bar, select it and click "![Delete bars](/en/docs/mt5/platform/img/delete_button.png "Delete bars")Delete Bars". To delete multiple bars, select them with the mouse while holding down "Shift" or "Ctrl", and then click "![Delete bars](/en/docs/mt5/platform/img/delete_button.png "Delete bars")Delete Bars".

## Context Menu [#](admin_charts#context)

The following commands are available from the context menu of this section:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new bar.
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected bar.
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete selected bars.
-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — request history data.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export — [export](/en/docs/mt5/platform/administration/common_info/export) current requested history data to a file in CSV or HTML format.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/admin_charts/admin_charts_import) history data to the current requested symbol from a file.
-   ![Import from Folder](/en/docs/mt5/platform/img/import_folder_icon.png "Import from Folder") Import from Folder — [import](/en/docs/mt5/platform/administration/admin_charts/admin_charts_import) history data to the current requested symbol from multiple files.
-   ![Split Stock](/en/docs/mt5/platform/img/split_icon.png "Split Stock") Split Stock — [transform](/en/docs/mt5/platform/administration/admin_charts/split_charts) minute bars after splitting stocks.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [Search](/en/docs/mt5/platform/administrator/interface/search) window.
-   Auto Arrange — if this option is enabled the size of columns is selected automatically.
-   Grid — this option shows/hides field separators in the table.
-   Columns — select columns to display. You can additionally enable "Volume", "Spread" and "Tick volume".

[Spreads](/en/docs/mt5/platform/administration/spreads)

[Import of History Data](/en/docs/mt5/platform/administration/admin_charts/admin_charts_import)