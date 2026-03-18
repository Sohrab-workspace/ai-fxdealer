# Liquidity Orders

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Liquidity Orders

# Liquidity Orders

Ultency maintains its own database of trading operations. When a client on the platform side places an order that is routed for execution to Ultency, a corresponding operation is created in Ultency. This is referred to as a [matching order](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders). Based on routing rules, Ultency generates one or more requests for execution  these are called liquidity orders. Depending on the execution type, these orders may be routed to liquidity providers (A-Book) or executed internally (B-Book). Deals that execute the liquidity order either by liquidity providers or internally are transmitted to Ultency and can be viewed in the [relevant section](/en/docs/mt5/platform/administration/ultency/ultency_deals).

In this section, you can view all liquidity orders: which provider they originated from, their volume, price, and other parameters.

![Liquidity orders](/en/docs/mt5/platform/img/ultency_liquidity_orders.png "Liquidity orders")

## Request Orders [#](ultency_liquidity_orders#request)

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

## Viewing an Order [#](ultency_liquidity_orders#view)

To view an order, double-click on it in the list. The trade dialog is a full-featured tool that offers many useful functions: displaying the structure of the operation, visualizations, tick and order book history, and the operation log.

![Liquidity order](/en/docs/mt5/platform/img/ultency_liquidity_order_view.png "Liquidity order")

### Account Details [#](ultency_liquidity_orders#account_details)

At the top of the dialog, a summary of the account on which the operation was performed is displayed: name, login, group, and leverage. Click this line to open [detailed account information](/en/docs/mt5/platform/administration/admin_accounts/account_edit).

### Overview and Related Operations [#](ultency_liquidity_orders#connected_transactions)

All related trading operations are shown in this block: deals executed as a result of order execution and the resulting position. Thus you can easily access the entire chain of related actions. Select an operation from the tree and all relevant parameters will be instantly displayed in the bottom part.

![Viewing Related Operations](/en/docs/mt5/platform/img/ultency_operation_tree.png "Viewing Related Operations")

In the example above:

1.  Final position opened on the MetaTrader 5 side as a result of the order executed in Ultency.
2.  Original pending order placed from MetaTrader 5.
3.  Matching order created in Ultency to execute the client's original market order.
4.  Corresponding liquidity order created to fill the matching order.
5.  First deal that partially filled the matching order. Since the volume of the best available ask at that time was smaller (0.04) than the original request (0.1), Ultency filled the order using two price levels.
6.  Second deal that partially filled the matching order. Next after the best ask in the order book.
7.  Final deal created on the MetaTrader 5 side.

### Trading Operation Details [#](ultency_liquidity_orders#details)

For each order, the following parameters are shown:

-   Ultency liquidity order — ticket number of the liquidity order created in Ultency to fill the client order.
-   Order type — type of the liquidity order created in Ultency.
-   Matching order — ticket number of the [matched order](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders) that will be filled by this liquidity order.
-   Size/volume initial — initial volume of the liquidity order, in contracts and lots.
-   Size/volume executed — volume of the liquidity order that was actually executed in Ultency.
-   Provider symbol — name of the [trading instrument](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols) on the liquidity provider side.

-   State — current state of the liquidity order (filled, rejected, partially filled, expired, etc.).
-   Liquidity provider — name of the [liquidity provider](/en/docs/mt5/platform/administration/ultency/ultency_connect#liquidity_providers) to which the liquidity order is sent.
-   External ID — order ticket created on the liquidity provider side.

-   Filling type — additional [fill policy rules](/en/docs/mt5/platform/administration/common_info/general_concept#fill_policy) for the liquidity order: "Fill or kill", "Cancel remainder", "Passive", or "Return remainder".
-   Expiration time — if lifetime of the liquidity order has expired, then this field contains the date and time of expiration.
-   Create time — liquidity order creation time.

-   Execution time — liquidity order execution time in Ultency.
-   Provider contract — contract size of the [trading instrument](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols) on the liquidity provider side.

-   Rate, USD — the exchange rate of the symbol's base currency to USD at the time the order was filled.

-   Price — the initial price requested in the liquidity order.
-   VWAP expected — the price at which the liquidity order was expected to be executed. The value is calculated as the volume-weighted average price based on the current order book from the liquidity provider and the required trade volume. Includes the [provider markup](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#quotes).
-   VWAP executed — the actual price at which the liquidity order was executed. The value is calculated as the volume-weighted average price of the deals executed on the provider side. Includes the [provider markup](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#quotes).
-   Provider markup — markup size as defined in the [provider symbol settings](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#quotes). Specified in points.
-   Place time — the time it took to register the liquidity order with the provider. Specified in microseconds.
-   Fill time — the time from registering the liquidity order with the provider to the execution of the final trade under that order. Specified in microseconds.

### Visualization [#](ultency_liquidity_orders#visualization)

In this section, execution of a trading operation is visualized on the tick chart of the appropriate aggregated symbol.

![Trading visualization](/en/docs/mt5/platform/img/ultency_matching_order_visualization.png "Trading visualization")

### Closest Ticks Before and After the Operation [#](ultency_liquidity_orders#ticks)

When analyzing disputable situations with traders, it is often necessary to analyze quotes that existed at the time of the trading operation. This information can be retrieved in just two clicks. Open the deal details and go to the "Ticks" or "Ultency Ticks" tab. The terminal will automatically request the full day's tick history for the date of the trade. The tick closest to the trade execution time will be automatically highlighted in the list.

-   Ticks — ticks actually shown to traders on the MetaTrader 5 side. These represent the platform-side symbol, which receives tick data from the aggregated symbol in Ultency according to [translation settings](/en/docs/mt5/platform/administration/ultency/ultency_translations). As a result, markup settings from the translation rules and standard price adjustment parameters set for the [symbol](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#spread) or [group](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_common) may apply.
-   Ultency ticks — ticks of the [aggregated symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#quotes) in Ultency.

![Closest Ticks Before and After the Operation](/en/docs/mt5/platform/img/ultency_matching_order_ticks.png "Closest Ticks Before and After the Operation")

### Ultency Book [#](ultency_liquidity_orders#book)

Every time deals are matched, Ultency records the current state of the aggregated order book. This feature provides better understanding of how the system operates and helps resolve potential disputes. For more details, see the [Execution Books](/en/docs/mt5/platform/administration/ultency/ultency_execution_books) section.

![Order book state at the order execution time](/en/docs/mt5/platform/img/ultency_matching_order_book.png "Order book state at the order execution time")

### Trading Operation Journal [#](ultency_liquidity_orders#journal)

This is another tool to assist during the follow-up operation examination. There is no need to manually query [logs from the server](/en/docs/mt5/platform/administration/admin_network/network_journal) or to filter entries. Open the trading operation details, navigate to the "Journal" tab, and the terminal will automatically request the relevant records from the server, filtered by ticket and from the operation date to the current day.

![Trading Operation Journal](/en/docs/mt5/platform/img/ultency_matching_order_journal.png "Trading Operation Journal")

### Trading Operation Report [#](ultency_liquidity_orders#report)

All data from the trading operation dialog can be saved as a report. The report includes the full operation chain from order to position, a visual tick chart, log excerpts, and overall account status.

To generate the file, right-click in the "[Overview and related operations](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders#connected_transactions)" section and select "Report" from the context menu. Then choose which data to include: account status, trading results, log, tick chart, etc.

![Trading Operation Report](/en/docs/mt5/platform/img/ultency_matching_order_report.png "Trading Operation Report")

## Context Menu [#](ultency_liquidity_orders#context)

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
-   Columns — use this submenu to select which [order data](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders#view) fields are displayed in the list.

[Matching Orders](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders)

[Deals](/en/docs/mt5/platform/administration/ultency/ultency_deals)