# Execution Books

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_execution_books

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Execution Books

# Execution Books

Ultency captures the current state of the aggregated order book each time a deal is matched. This feature provides better understanding of how the system operates and helps resolve potential disputes.

The system maintains two separate order books:

-   A Book, which is assembled according to [execution settings](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution) for the aggregated symbol. This book is used for executing orders routed to liquidity providers. It is not visible to traders.
-   B-Book, which is assembled according to [quote settings](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#quotes) for the aggregated symbol. It is used for executing orders internally within the platform, and it is the one visible to traders when trading through Ultency.

Together, these books provide a full picture of trade execution in any mode: what book was visible to the trader, what levels were actually available from liquidity providers, and how the execution occurred.

The easiest way to view market conditions at the time of a trading operation is to open it from the [Matching orders](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders), [Liquidity orders](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders), or [Deals](/en/docs/mt5/platform/administration/ultency/ultency_deals) section and navigate to the "Ultency Book" tab. The "Execution Books" section allows you to view the full history of all saved order book snapshots.

![Execution Books](/en/docs/mt5/platform/img/ultency_execution_books.png "Execution Books")

## Requesting Data [#](ultency_execution_books#request)

To view order books for a symbol, request them, following these steps:

-   Symbol Selection  
    In the first field, specify one of the financial symbols from the system. The symbol can be specified manually or chosen from the list, which opens by clicking on the down arrow.
-   Period Selection  
    Specify the period for which you want to request books. You can choose one of the predefined periods by clicking on ![Reference](/en/docs/mt5/platform/img/calendar.png "Reference") (today, last 3 days, last week, last month, last 3 months, last 6 months or the entire history). You can also specify a custom time interval.
-   Request Execution  
    To retrieve the tick data, click the "Request" button or use the corresponding context menu command ![Request](/en/docs/mt5/platform/img/request_button.png "Request").

## Viewing the Order Book [#](ultency_execution_books#view)

Click on any order book in the list to view its details. Then, in the context menu, select the [order book type](/en/docs/mt5/platform/administration/ultency/ultency_execution_books#dom_type): A-Book or B-Book.

![Ultency Executed Book](/en/docs/mt5/platform/img/ultency_execution_books_view.png "Ultency Executed Book")

The following information is available for each order book:

-   Source — the liquidity provider from which the buy/sell level was received. This field is available only for the A-Book. The [provider configuration](/en/docs/mt5/platform/administration/ultency/ultency_connect#connect) name is displayed as the source.
-   Buy/Sell — the available volume (in number of contracts) at each bid or ask price. If the field shows the infinity symbol (∞), it indicates a technical level created according to the [settings of the aggregated symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#bands).
-   Price — the sell or buy level price. In A-Book mode, this column also shows B-Book prices calculated based on [minimum spread](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#spread) or [markup](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#markup) settings, but excluding [levels](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#bands) themselves.
-   Flags — additional attributes of the price level:

-   Liquid — the level is liquid, meaning trades can be executed at this price.
-   Visible — the level is visible to clients in the aggregated order book. Currently, only [technical levels](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#bands) with infinite liquidity created based on aggregated symbol settings can be invisible.

At the bottom of the window, the timestamp of the saved order book snapshot is displayed along with its unique identifier. This same identifier appears when viewing details of a [matching order](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders#book_reference). It can also be used to retrieve order books in this section.

Use the context menu to manage the appearance and content of the order book. From here, you can switch between order book types, toggle columns, and enable or disable the grid display. Additional available commands include:

-   Invisible levels — disable this option to hide [technical levels](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#bands) with infinite liquidity from the order book. When enabled, both visible and hidden levels will be shown.
-   Illiquid levels — disable this option to hide price levels at which orders cannot be executed.

[Ticks](/en/docs/mt5/platform/administration/ultency/ultency_ticks)

[Control and Reporting](/en/docs/mt5/platform/administration/ultency/ultency_reporting)