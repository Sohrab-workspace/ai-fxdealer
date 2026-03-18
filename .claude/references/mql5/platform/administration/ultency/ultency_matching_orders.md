# Matching Orders

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_matching_orders

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
                -   [Connection](/en/docs/mt5/platform/administration/ultency/ultency_connect)
                -   [Provider Symbols](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols)
                -   [Aggregated Symbols](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols)
                -   [Translations of Symbols and Quotes](/en/docs/mt5/platform/administration/ultency/ultency_translations)
                -   [Routing](/en/docs/mt5/platform/administration/ultency/ultency_routing)
                -   [Order Execution](/en/docs/mt5/platform/administration/ultency/ultency_execution)
                -   [Matching Orders](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders)
                -   [Liquidity Orders](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders)
                -   [Deals](/en/docs/mt5/platform/administration/ultency/ultency_deals)
                -   [Ticks](/en/docs/mt5/platform/administration/ultency/ultency_ticks)
                -   [Execution Books](/en/docs/mt5/platform/administration/ultency/ultency_execution_books)
                -   [Control and Reporting](/en/docs/mt5/platform/administration/ultency/ultency_reporting)
                -   [Service Desk](/en/docs/mt5/platform/administration/ultency/ultency_service_desk)
                -   [Become a Provider](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_offers)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Matching Orders

# Matching Orders

Ultency maintains its own database of trading operations. When a client on the platform side places an order that is routed for execution to Ultency, a corresponding operation is created in Ultency. This is referred to as a matching order. Based on routing rules, Ultency generates one or more requests for execution  these are called [liquidity orders](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders). Depending on the execution type, these orders may be routed to liquidity providers (A-Book) or executed internally (B-Book). Deals that execute the liquidity order either by liquidity providers or internally are transmitted to Ultency and can be viewed in the [relevant section](/en/docs/mt5/platform/administration/ultency/ultency_deals).

In this section, you can view all the orders that are being matched: when and by whom they were created, as well as how they were forwarded and executed in Ultency.

![Matching Orders](/en/docs/mt5/platform/img/ultency_matching_orders.png "Matching Orders")

## Request Orders [#](ultency_matching_orders#request)

To view orders, request them using one of the following methods:

-   By Groups  
    Select a group from the dropdown list.
-   By Logins  
    Enter one or more account numbers separated by commas.
-   By Symbols  
    Specify one or more instruments separated by commas.

Additional query parameters may include:

-   "Open Only" — display orders that have not yet been executed.
-   One of the predefined date ranges: "Today", "Last 3 days", "Last week", "Last 3 months", "Last 6 months" or "All history". To specify a custom request period, use the fields to the right. Orders are requested by execution time. Open orders do not have this parameter, so they will be included in all queries.
-   Exact time range. Specify the start or end time manually or use the calendar popup, opened via the button ![Calendar](/en/docs/mt5/platform/img/calendar_button.png "Calendar").

After entering the required parameters, click "Request".

## Viewing an Order [#](ultency_matching_orders#view)

To view an order, double-click on it in the list. The trade dialog is a full-featured tool that offers many useful functions: displaying the structure of the operation, visualizations, tick and order book history, and the operation log.

![Matching order](/en/docs/mt5/platform/img/ultency_matching_order_view.png "Matching order")

### Account Details [#](ultency_matching_orders#account_details)

At the top of the dialog, a summary of the account on which the operation was performed is displayed: name, login, group, and leverage. Click this line to open [detailed account information](/en/docs/mt5/platform/administration/admin_accounts/account_edit).

### Overview and Related Operations [#](ultency_matching_orders#connected_transactions)

All related trading operations are shown in this block: deals executed as a result of order execution and the resulting position. Thus you can easily access the entire chain of related actions. Select an operation from the tree, and all relevant parameters will be instantly displayed in the bottom part.

![Viewing Related Operations](/en/docs/mt5/platform/img/ultency_operation_tree.png "Viewing Related Operations")

In the example above:

1.  Final position opened on the MetaTrader 5 side as a result of the order executed in Ultency.
2.  Original pending order placed from MetaTrader 5.
3.  Matching order created in Ultency to execute the client's original market order.
4.  Corresponding liquidity order created to fill the matching order.
5.  First deal that partially filled the matching order. Since the volume of the best available ask at that time was smaller (0.04) than the original request (0.1), Ultency filled the order using two price levels.
6.  Second deal that partially filled the matching order. Next after the best ask in the order book.
7.  Final deal created on the MetaTrader 5 side.

### Trading Operation Details [#](ultency_matching_orders#details)

For each order, the following parameters are shown:

-   Ultency matching order — ticket number of the order created in Ultency.
-   Order type — type of the order created in Ultency.
-   MT5 order type — type of the original order created on the MetaTrader 5 side.
-   MT5 order — ticket number of the original order created on the MetaTrader 5 side.
-   MT5 server — name of the [trading server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server), on which the original order was created.
-   MT5 group — name of the [group](/en/docs/mt5/platform/administration/admin_groups) associated with the account from which the original order originated.
-   MT5 action — trading action that triggered the original order: 'market' — placement of a market order, 'activate' — activation of a pending order.
-   Symbol — [aggregated symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols) in Ultency for which the matching order was created.
-   MT5 symbol — symbol of the original order on the MetaTrader 5 side.

-   State — current status of the matching order (e.g., filled, rejected, partially filled, expired, etc.).

-   Expiration type — [expiration type](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#expiration) of the matching order: "GTC" (Good Till Canceled), "Day" or "Specified".
-   MT5 expiration type — expiration type of the original order on the MetaTrader 5 side: "GTC" (Good Till Canceled), "Day" or "Specified".
-   Expiration time — if the matching order expired, this field shows the expiration date and time.
-   MT5 expiration time — if the original order on the MetaTrader 5 expired, this field shows its expiration date and time.
-   Filling type — additional [fill policy rules](/en/docs/mt5/platform/administration/common_info/general_concept#fill_policy) for the matching order: "Fill or kill", "Cancel remainder", "Passive", or "Return remainder".
-   MT5 filling type — additional [fill policy rules](/en/docs/mt5/platform/administration/common_info/general_concept#fill_policy) for the original order on the MetaTrader 5 side: "Fill or kill", "Cancel remainder", "Passive", or "Return remainder".
-   Matching flags — additional execution settings applied to the matching order. For example, 'merge deals' means [execution deal merging](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#merge_deals) was enabled.
-   Create time — matching order creation time.

-   Done time — matching order execution time in Ultency.
-   Coverage — value of the "[A-Book/Coverage](/en/docs/mt5/platform/administration/ultency/ultency_routing#minimum_coverage)" setting from the routing rule that was used to process the order. This field sores the value that was specified in the rule at the moment the order was routed.

-   Minimum coverage volume — value of the  "[Minimum coverage volume](/en/docs/mt5/platform/administration/ultency/ultency_routing#minimum_coverage)" setting from the routing rule that was used to process the order. This field sores the value that was specified in the rule at the moment the order was routed.

-   Price — price at which the matching order was routed for execution in either A-Book or B-Book.
-   MT5 price — price at which the original order was submitted on the MetaTrader 5 side.
-   MT5 contract size — contract size of the [trading instrument](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#contract_size) on the MetaTrader 5 side.

-   Rate, USD — the exchange rate of the symbol's base currency to USD at the time the order was filled.

-   MT5 size/volume — volume requested in the original order on the MetaTrader 5 side. Specified in contracts and lots.
-   MT5 size/volume executed — volume from the MT5 side that was executed as a result of order matching in Ultency. Specified in contracts and lots.
-   MT5 VWAP executed — final price at which the original order was executed. Calculated as the volume-weighted average price across all deals that executed the order on the Ultency side, including all markups.
-   Aggregated symbol markup — markup size as defined in the [aggregated symbol settings](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#markup). Specified in points.
-   A-Book size — initial volume intended to be routed through A-Book according to the [routing rules](/en/docs/mt5/platform/administration/ultency/ultency_routing#coverage).
-   B-Book size — initial volume intended to be routed through B-Book according to the routing rules.
-   A-Book size taken — A-Book volume that was sent to the liquidity provider but not yet executed. A value in this field indicates the order is still in the process of being filled.
-   A-Book size executed — volume that was actually executed through A-Book (on the liquidity provider side).
-   A-Book VWAP executed — volume-weighted average price of all deals that filled the A-Book portion of the order.
-   B-Book size executed — volume that was actually executed through B-Book (on the platform side).
-   B-Book VWAP executed — volume-weighted average price of all deals that filled the B-Book portion of the order.

Additional information that may be displayed in the list of matching orders:

-   Coverage — portion of the matching order volume executed through A-Book.
-   Book link — identifier of the order book snapshot captured at the moment of execution. This can be used to request corresponding data in the "[Execution Books](/en/docs/mt5/platform/administration/ultency/ultency_execution_books)" section.

### Visualization [#](ultency_matching_orders#visualization)

In this section, execution of a trading operation is visualized on the tick chart of the appropriate aggregated symbol.

![Trading visualization](/en/docs/mt5/platform/img/ultency_matching_order_visualization.png "Trading visualization")

### Closest Ticks Before and After the Operation [#](ultency_matching_orders#ticks)

When analyzing disputable situations with traders, it is often necessary to analyze quotes that existed at the time of the trading operation. This information can be retrieved in just two clicks. Open the deal details and go to the "Ticks" or "Ultency Ticks" tab. The terminal will automatically request the full day's tick history for the date of the trade. The tick closest to the trade execution time will be automatically highlighted in the list.

-   Ticks — ticks actually shown to traders on the MetaTrader 5 side. These represent the platform-side symbol, which receives tick data from the aggregated symbol in Ultency according to [translation settings](/en/docs/mt5/platform/administration/ultency/ultency_translations). As a result, markup settings from the translation rules and standard price adjustment parameters set for the [symbol](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#spread) or [group](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_common) may apply.
-   Ultency ticks — ticks of the [aggregated symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#quotes) in Ultency.

![Closest Ticks Before and After the Operation](/en/docs/mt5/platform/img/ultency_matching_order_ticks.png "Closest Ticks Before and After the Operation")

### Ultency Book [#](ultency_matching_orders#book)

Every time deals are matched, Ultency records the current state of the aggregated order book. This feature provides a better understanding of how the system operates and helps resolve potential disputes. For more details, see the [Execution Books](/en/docs/mt5/platform/administration/ultency/ultency_execution_books) section.

![Order book state at the order execution time](/en/docs/mt5/platform/img/ultency_matching_order_book.png "Order book state at the order execution time")

### Trading Operation Journal [#](ultency_matching_orders#journal)

This is another tool to assist during the follow-up operation examination. There is no need to manually query [logs from the server](/en/docs/mt5/platform/administration/admin_network/network_journal) or to filter entries. Open the trading operation details, navigate to the "Journal" tab, and the terminal will automatically request the relevant records from the server, filtered by ticket and from the operation date to the current day.

![Trading Operation Journal](/en/docs/mt5/platform/img/ultency_matching_order_journal.png "Trading Operation Journal")

### Trading Operation Report [#](ultency_matching_orders#report)

All data from the trading operation dialog can be saved as a report. The report includes the full operation chain from order to position, a visual tick chart, log excerpts, and overall account status.

To generate the file, right-click in the "[Overview and related operations](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders#connected_transactions)" section and select "Report" from the context menu. Then choose which data to include: account status, trading results, log, tick chart, etc.

![Trading Operation Report](/en/docs/mt5/platform/img/ultency_matching_order_report.png "Trading Operation Report")

## Context Menu [#](ultency_matching_orders#context)

The context menu of this section includes the following commands:

-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — open the selected order.
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete the selected order.
-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — execute a [request](/en/docs/mt5/platform/administration/admin_orders#request).
-   Copy As — copy the orders selected in the list:
    -   ![Copy as lines](/en/docs/mt5/platform/img/copy_button.png "Copy as lines") Lines — copy all selected information.
    -   List Of Logins — copy only the list of logins.
    -   List Of Tickets — copy only the list of tickets.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal By — query [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) entries for the selected order.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export — [export](/en/docs/mt5/platform/administration/common_info/export) the requested orders to an \*.HTM, \*.HTML, or \*.CSV file.
-   ![Search](/en/docs/mt5/platform/img/find_button.png "Search") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window.
-   Auto Arrange — if this option is enabled, the size of columns is selected automatically.
-   Grid — show/hide grid to separate fields in the orders table.
-   Columns — use this submenu to select which [order data](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders#view) fields are displayed in the list.

[Order Execution](/en/docs/mt5/platform/administration/ultency/ultency_execution)

[Liquidity Orders](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders)