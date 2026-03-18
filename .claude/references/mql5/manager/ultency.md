# Ultency Matching Engine: Built-in liquidity aggregation and order execution

> Source: https://support.metaquotes.net/en/docs/mt5/manager/ultency

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
            -   [Routing](/en/docs/mt5/manager/ultency_routing)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Ultency

# Ultency Matching Engine: Built-in liquidity aggregation and order execution

Ultency Matching Engine is an ultra-low latency solution for liquidity aggregation, trade order matching, and risk management. This technological platform enables reliable connection to multiple providers simultaneously, consolidating their prices and execution to deliver the best trading conditions for traders. The system is highly customizable to meet the unique requirements of each broker, offering a comprehensive suite of risk management and reporting tools.

![Ultency Matching Engine: Built-in liquidity aggregation and order execution](/en/docs/mt5/manager/img/ultency_intro_main.png "Ultency Matching Engine: Built-in liquidity aggregation and order execution")

## Ultency for Brokers

Ultency offers unique advantages for brokers:

-   Access multiple liquidity providers through an intuitive gallery with detailed descriptions of offerings and connect in a few clicks.
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

![Ultency features](/en/docs/mt5/manager/img/ultency_intro_providers.png "Ultency features")

## Highly Configurable

Ultency allows detailed configuration of price aggregation and order execution parameters:

-   For each instrument, you can specify individual liquidity providers to aggregate prices for clients, and configure custom order book rules, spread adjustments, and execution parameters.
-   For each client/group, you can assign liquidity providers to execute their orders, as well as individual markups. You can manage order routing between A-Book, B-Book, and C-Book executions (partial hedge, overhedge, reverse hedge).

With the flexible template system, you can save markups, price feed configurations, routing rules, and order execution settings. Create templates for different conditions and apply them automatically based on time, market events, or risk management rules.

![Highly configurable](/en/docs/mt5/manager/img/ultency_intro_settings.png "Highly configurable")

## Protection and Risk Management

Intelligent filtering protects against incorrect prices. Each price entering the system is validated and compared with prices from other providers. Based on the validation results, the system decides whether to accept or reject the quote.

The system supports automatic risk management rules, including coverage based on position volume, instrument, currency, turnover, profit, and more. Rules can be set for individual clients, client groups, or the broker's entire portfolio.

![Protection and risk management](/en/docs/mt5/manager/img/ultency_intro_protection.png "Protection and risk management")

## Monitoring and Reporting

Ultency supports special coverage accounts for monitoring key metrics, including funds, profit/loss, total positions, and more. The data can be analyzed by liquidity providers, clients, client groups, and the entire portfolio, and used to configure automatic risk management rules.

A dedicated dashboard allows dealers to monitor performance parameters in real-time, including the volume of orders routed to providers, risk management rules, and the broker's portfolio.

The built-in reports enable the analysis of client trading results, A-Book execution efficiency, earnings from markups, commissions, and swaps. Reports can be segmented by instruments and client groups, allowing you to identify toxic clients and take appropriate measures promptly.

[Processing Payments](/en/docs/mt5/manager/payments_processing)

[Routing](/en/docs/mt5/manager/ultency_routing)