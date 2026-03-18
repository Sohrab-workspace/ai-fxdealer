# Ultency Matching Engine: Built-in liquidity aggregation and order execution

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Ultency

# Ultency Matching Engine: Built-in liquidity aggregation and order execution

Ultency Matching Engine is an ultra-low latency solution for liquidity aggregation, trade order matching, and risk management. This technological platform enables reliable connection to multiple providers simultaneously, consolidating their prices and execution to deliver the best trading conditions for traders. The system is highly customizable to meet the unique requirements of each broker, offering a comprehensive suite of risk management and reporting tools.

![Ultency Matching Engine: Built-in liquidity aggregation and order execution](/en/docs/mt5/platform/img/ultency_intro_main.png "Ultency Matching Engine: Built-in liquidity aggregation and order execution")

## Ultency for Brokers

Ultency offers unique advantages for brokers:

-   Access multiple [liquidity providers](/en/docs/mt5/platform/administration/ultency/ultency_connect#liquidity_providers) through an intuitive gallery with detailed descriptions of offerings and connect in a few clicks.
-   Choose the best prices from various sources to improve order execution for traders.
-   Lower spreads by accessing multiple liquidity providers. This makes trading more cost-efficient for clients and helps attract new traders.
-   Save on infrastructure costs by avoiding individual connections to each provider. Ultency reduces development and maintenance costs, simplifying scalability.
-   Access various order types and a wide range of risk management tools. Select optimal execution strategies based on market volatility and client needs.
-   Efficiently process orders during news releases and fast market movements. The platform tracks prices from multiple providers, minimizing delays or price gaps.

## Ultency Features

Ultency is a native solution for the MetaTrader 5 platform:

-   The engine uses highly efficient internal data transfer protocols between cluster components, significantly speeding up order processing and enhancing system resilience.
-   The main instrument and trading session parameters are configured once in MetaTrader 5, eliminating the need to monitor their compliance in multiple systems. All order execution, client and configuration change logs are stored in one place, accessible only to the broker.

Each broker gets a dedicated platform that processes only their orders. You can choose from multiple hosting locations depending on which liquidity providers you want to connect to and the markets you offer. For example, to offer access to various exchanges, you can use a server in London for Forex providers and another one in New York for NYSE providers.

![Ultency features](/en/docs/mt5/platform/img/ultency_intro_providers.png "Ultency features")

## Highly Configurable

Ultency allows detailed configuration of price aggregation and order execution parameters:

-   For each instrument, you can specify individual liquidity providers to aggregate prices for clients, and configure custom order book rules, spread adjustments, and execution parameters.
-   For each client/group, you can assign liquidity providers to execute their orders, as well as individual markups. You can manage order routing between A-Book, B-Book, and C-Book executions (partial hedge, overhedge, reverse hedge).

With the flexible template system, you can save markups, price feed configurations, routing rules, and order execution settings. Create templates for different conditions and apply them automatically based on time, market events, or risk management rules.

![Highly configurable](/en/docs/mt5/platform/img/ultency_intro_settings.png "Highly configurable")

## Protection and Risk Management

Intelligent filtering protects against incorrect prices. Each price entering the system is validated and compared with prices from other providers. Based on the validation results, the system decides whether to accept or reject the quote.

The system supports automatic risk management rules, including coverage based on position volume, instrument, currency, turnover, profit, and more. Rules can be set for individual clients, client groups, or the broker's entire portfolio.

![Protection and risk management](/en/docs/mt5/platform/img/ultency_intro_protection.png "Protection and risk management")

## Monitoring and Reporting

Ultency supports special coverage accounts for monitoring key metrics, including funds, profit/loss, total positions, and more. The data can be analyzed by liquidity providers, clients, client groups, and the entire portfolio, and used to configure automatic risk management rules.

A dedicated dashboard allows dealers to monitor performance parameters in real-time, including the volume of orders routed to providers, risk management rules, and the broker's portfolio.

The built-in reports enable the analysis of client trading results, A-Book execution efficiency, earnings from markups, commissions, and swaps. Reports can be segmented by instruments and client groups, allowing you to identify toxic clients and take appropriate measures promptly.

[Execution Speed](/en/docs/mt5/platform/administration/admin_reports/execution_speed_report)

[Connection](/en/docs/mt5/platform/administration/ultency/ultency_connect)