# Bid/Ask/Last Ticks

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_ticks

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Bid/Ask/Last Ticks

# Bid/Ask/Last Ticks

This section allows managing tick data of financial instruments. Quotes are received by the history server from [data feeds](/en/docs/mt5/platform/administration/admin_feeds) and [gateway](/en/docs/mt5/platform/administration/admin_gateways) as a stream of ticks, trade statistics and Market Depth changes. The server passes this data to clients, but only stores the history of tick data. Trade statistics and Market Depth changes are not saved.

It is recommended to find a high-quality deep history of all your financial instruments and [import](/en/docs/mt5/platform/administration/admin_ticks/admin_ticks_import) it to the platform. The ability to test Expert Advisors using ticks in the Strategy Tester is an important function for traders. This testing mode is the most precise one while it is close to real market conditions.

## The Features of Tick History Generation

If a data feed or gateway sends symbol Market Depth changes to a platform, the history server automatically monitors changes of the best Bid and Ask price in it. If the best Bid or Ask price has changed, the history server generates a tick with the values ​​of the best Bid and Ask prices. In this tick, the value of the last trade price and the volume will be zero.

The gateway/datafeed must only send ticks with the filled Last price and volume value. Otherwise, there will be duplicate Bid/Ask ticks (formed by history server and sent by the gateway/datafeed).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">At the beginning of each quoting session, a Bid/Ask quote is automatically added for symbols with the enabled Market Depth feature. The quote is generated based on the current Market Depth state. The purpose of this quote addition is to ensure that prices in the Market Watch window in client terminals correspond to the Market Depth state. An appropriate message is printed to the History server log in such case, for example: "AUDUSD tick added 0.75761 / 0.75779 due quotes session start". If the Market Depth is enabled, but one of the sides is absent (it has a zero Bid or Ask), a tick is added at the session beginning only if the symbol has the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation" class="topiclink">Exchange calculation type</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">For the symbols, the charts of which are based on Bid prices, the history server does no accept Last prices and volumes from gateways and datafeeds. These <a href="/en/docs/mt5/platform/administration/admin_ticks" class="topiclink">ticks</a> are not saved and are not delivered to other components of the platform.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The history server generates ticks using the best Market Depth prices only if the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#dom" class="topiclink">"Market depth"</a> parameter in the appropriate symbol settings is not equal to "disabled".</span></li></ul></td></tr></tbody></table>

![Ticks](/en/docs/mt5/platform/img/ticks.png "Ticks")

Each tick can store the following data:

-   Date — the date and time of tick arrival.
-   Bid — the Bid price.
-   Ask — the Ask price.
-   Last — the price of the last executed trade (for exchange instruments).
-   Volume — the volume of the last executed trade (for exchange instruments).
-   Direction — direction of a deal, as a result of which the tick was generated: Buy or Sell. Data on direction is generally filled by the source of ticks, i.e. a gateway or a data feed. If the data source does not provide such information, the history server fills the direction automatically using the following algorithm:
    -   If the Last deal price is greater than or equal to the last Ask price, the price is considered to be the result of a buy deal.
    -   If the Last deal price is less than or equal to the last Bid price, the price is considered to be the result of a sell deal.
    -   In other cases, it is considered that the direction can't be determined, and both directions, Buy and Sell, are assigned to the tick.
-   Data source — the name of the [datafeed/gateway](/en/docs/mt5/platform/administration/admin_ticks#datafeed).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The price data received from gateways and data feeds is stored under [history server installation directory\history]. If the free disk space on the history server drops below 2 gigabytes, no saving of new arriving price data is performed. This prevents data from occupying of all available disk space. Thus, the overall server performance is preserved. If data cannot be written to disk, the following message is added into the history servers log: "'EURUSD' save skipped due not enough free space on disk", "bars and ticks are not saved due not enough free space on disk", "synchronization was stopped due not enough free space on disk ". In this case, you should immediately increase free disk space on the server.</span></p></td></tr></tbody></table>

## Raw and Accepted Ticks [#](admin_ticks#type)

The trading platform can store two types of ticks: raw and accepted. Raw (![Raw](/en/docs/mt5/platform/img/tick_raw_icon.png "Raw")) are ticks received directly from datafeeds/gateways. Accepted (![Accepted](/en/docs/mt5/platform/img/tick_filtered_icon.png "Accepted")) are the ticks that were filtered and converted in accordance with [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration).

If you need to store raw ticks of a selected symbol on the server, the [appropriate option](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration#raw_ticks) must be enabled in symbol settings. Accepted ticks are always saved on the [history server](/en/docs/mt5/platform/components/history_server/history_server_structure#history).

## Trade Statistics [#](admin_ticks#statistics)

In addition to the basic price data of the trading instrument, the platform allows broadcasting to traders many useful [statistics](https://www.metatrader5.com/en/terminal/help/trading/market_watch#details), such as session opening and closing prices, the highest and lowest Bid/Ask/Last prices for the day, and much more.

Calculated statistics can be transmitted through data sources and gateways. If ready statistical variables are not available, the appropriate metrics can be calculated on the history server and client terminal side. The statistical variables are calculated as follows:

-   Open Price —  the open price of the last (recent) session. If [the symbol chart is built by Bid prices](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#charts), the Bid price value from the first tick of the session is remembered. If the tick has no Bid, the next tick is used, and so on. Similarly, the Last price is used for the instruments whose charts are based on last deal prices. If the value is provided by a gateway or data feed, exactly this will be used. No extra check or calculation is performed until history server restart.
-   Close Price — the close price of the last (recent) session. If [the symbol chart is built by Bid prices](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#charts), the Bid price value from the last tick of the session is remembered. If the tick has no Bid, the previous tick is used, and so on. Similarly, the Last price is used for the instruments whose charts are based on last deal prices. If the value is provided by a gateway or data feed, exactly this will be used. No extra check or calculation is performed until history server restart.
-   Price Change — indicates the difference between the last price of the instrument and the close price of the last session in percentage terms. The value is always calculated on the client terminal side. The calculation formula depends on the [symbol charting mode](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#charts):  
       
    By Last prices: ((Last - Last price at session close)/Last price at session close)\*100  
    By Bid prices: ((Bid - Bid price at session close)/Bid price at session close)\*100.  
       
    For futures symbols, the clearing price is used instead of the the session close price, if the clearing price is provided by the broker (non-zero):  
       
    By Last prices: ((Last - Clearing price)/Clearing price)\*100  
    By Bid prices: ((Bid - Clearing price)/Clearing price)\*100.

## Requesting Data [#](admin_ticks#request)

To view or edit ticks of a symbol, request them:

-   Choosing a symbol  
    In the first field, specify one of financial symbols from the system. The symbol can be specified manually or chosen from the list which opens by clicking on the down arrow.
-   Choosing a type  
    Choose the [type of ticks](/en/docs/mt5/platform/administration/admin_ticks#type) to be requested: All, Accepted or Raw.
-   Choosing a period  
    Specify the period, for which you want to request ticks. You can choose one of the predefined periods by clicking on ![Periodicity](/en/docs/mt5/platform/img/calendar.png "Periodicity")(today, last 3 days, last week, last month, last 3 months, last 6 months or the entire history). You can also specify a custom time interval.
-   Request execution  
    To receive ticks, click "Request" or choose the same command from the context menu ![Request](/en/docs/mt5/platform/img/request_button.png "Request").

## Analyzing Data Feed [#](admin_ticks#datafeed)

The information about each tick contains the index of a [data feed](/en/docs/mt5/platform/administration/admin_feeds#switching) it came from. Index is the position of a data feed in the list at the time of the tick coming. The "Data Feed" column of ticks displays a data feed that currently corresponds to the index written for a tick.

Thus, in most cases the "Data Feed" column will display a data feed that is currently the first one in the list. However, that is not always so.

An error in the operation of a data feed may occur, in that case the translation of quotes will be automatically switched to the next data feed in the list. That exact moment can be traced by analyzing the information displayed in the "Data Feed" column.

Switching of data feeds (or [gateways](/en/docs/mt5/platform/administration/admin_gateways) that can also be used as sources of quotes) can be tracked in the [journal of the history server operation](/en/docs/mt5/platform/administration/admin_network/network_journal). For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">"18:32:44 &nbsp; &nbsp;Ticks &nbsp; &nbsp;datafeed 2: &nbsp;EURUSD activation"</span></p></td></tr></tbody></table>

This entry tells that at 18:32:44 the flow of quotes from the data feed 2 in the list of configurations has been activated for EURUSD.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The numeration of gateways and data feeds in the list of configurations starts from 0.</span></p></td></tr></tbody></table>

## Adding and Editing Tick Data [#](admin_ticks#add_edit)

To add a tick, click "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" button in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit#add) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu. To edit a tick, click "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit")Edit" or double-click on it.

![Adding/editing a tick](/en/docs/mt5/platform/img/tick_edit.png "Adding/editing a tick")

The following data can be edited:

-   Date — the date and time of tick arrival.
-   Bid — the Bid price.
-   Ask — the Ask price.
-   Last — the price of the last executed trade (for exchange instruments).
-   Volume — the volume of the last executed trade (for exchange instruments).

## Mass Deletion of Tick Data

To delete the tick data for a symbol:

-   stop the history server using the [console command](/en/docs/mt5/platform/platform_installation/console_setup) mt5history.exe /stop or by execution the command MetaTrader 5 Platform\\History Server\\Stop History Server in the Start menu.
-   go to the folder \\history\\\[symbol name\] on the history server and delete files with \*.tkc extension. Tick data for each month are stored in a separate file. For example, 201203.tkc contains tick for March 2012.

## Context Menu [#](admin_ticks#context)

The context menu of this section allows executing the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new tick.
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected tick.
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete selected ticks.
-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — request tick data.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export — [export](/en/docs/mt5/platform/administration/common_info/export) the current requested tick data in a file of CSV, HTM or HTML format.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/admin_ticks/admin_ticks_import) tick data to the current requested symbol from a file.
-   ![Import from Folder](/en/docs/mt5/platform/img/import_folder_icon.png "Import from Folder") Import from Folder — [import](/en/docs/mt5/platform/administration/admin_ticks/admin_ticks_import) tick data to the current requested symbol from multiple files.
-   ![Split Stock](/en/docs/mt5/platform/img/split_icon.png "Split Stock") Split Stock — [transform](/en/docs/mt5/platform/administration/admin_ticks/split_ticks) tick data after splitting stocks.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window.
-   Auto Arrange — if this option is enabled the size of columns is selected automatically.
-   Grid — this option shows/hides field separators in the table.
-   Columns — select columns to display.

[Split Stocks](/en/docs/mt5/platform/administration/admin_charts/split_charts)

[Import Tick Data](/en/docs/mt5/platform/administration/admin_ticks/admin_ticks_import)