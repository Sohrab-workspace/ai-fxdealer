# Monitoring and reporting

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_reporting

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Control and Reporting

# Monitoring and reporting

Ultency supports specialized coverage accounts for monitoring key metrics such as funds, profit/loss, net positions, and more. Data can be analyzed by liquidity providers, clients, client groups, and the entire portfolio. It can also be used to configure automated risk management rules.

Built-in reports enable company management and dealers to analyze client trading results, A-Book execution efficiency, and revenue from markups, commissions, and swaps. Reports can be segmented by instruments and client groups, helping to timely identify toxic clients and take appropriate actions.

## Coverage Groups and Accounts [#](ultency_reporting#coverage)

When a [liquidity provider is added](/en/docs/mt5/platform/administration/ultency/ultency_connect) to the platform, a dedicated group and a corresponding trading account are created. All client orders routed through this provider are mirrored to this account. Essentially, this account replicates your omnibus account with the liquidity provider and allows you to monitor operations:

-   You can connect to the account using a standard client terminal and view trade history or generate [trading reports](https://www.metatrader5.com/ru/terminal/help/trading/report).
-   You can also use any [server reports](/en/docs/mt5/platform/administration/admin_reports) for analysis by querying coverage groups via the [manager terminal](https://support.metaquotes.net/ru/docs/mt5/manager/reports).

![Ultency operations report](/en/docs/mt5/platform/img/ultency_reports.png "Ultency operations report")

The coverage group and account are specified in the liquidity provider's connection settings:

![Liquidity provider settings](/en/docs/mt5/platform/img/ultency_provider_settings.png "Liquidity provider settings")

Once the coverage account is created and the connection to the provider is established, the current balance from the provider's account is immediately copied to the coverage account using a separate balance operation. From that point on, the system will replicate all operations routed through this provider to the coverage account.

Each time the system connects to the provider, Ultency compares the coverage account balance with that of the provider. If discrepancies are found, corrective balance operations are automatically applied to the coverage account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">The coverage account must be located in the coverage group. Do not move it to other groups. The coverage group must be located on the main trading server.</span></p></th></tr></thead></table>

### Dedicated Accounts for Aggregated Symbols [#](ultency_reporting#coverage_symbol)

To ensure precise control over trade execution for aggregated symbols, all operations for each symbol are duplicated to separate coverage accounts. Each symbol is assigned two accounts. One account collects all operations routed to external providers (A-Book), while another collects all operations executed internally within the platform (B-Book).

![Configuring coverage symbols](/en/docs/mt5/platform/img/ultency_aggregated_symbols_coverage.png "Configuring coverage symbols")

If you do not specify coverage groups/accounts when adding the configuration for an aggregated symbol, Ultency will automatically copy them from the configurations of other symbols. If the groups/accounts are not yet specified anywhere, Ultency will automatically create new groups and accounts and add them to the aggregated symbol's configuration. The groups are created with the [netting accounting system](/en/docs/mt5/platform/administration/admin_groups/group_position#netting), allowing you to view the net positions for all clients. These groups and accounts will be immediately added to the aggregated symbol's settings. You can control system operations by requesting reports for the relevant groups and accounts through the Manager terminal.

-   Coverage symbol — if this option is enabled, coverage deals for the aggregated symbol will be executed on the original MetaTrader 5 symbols from which client requests are [routed](/en/docs/mt5/platform/administration/ultency/ultency_routing) to this aggregated symbol. If you wish to cover trades on a different symbol, disable this option and specify the symbol in the following field.
-   Coverage symbol — the name of the symbol where trades will be mirrored. It is used only when the "Coverage on client symbol" is disabled.
-   A-Book coverage group — the group where the account for duplicating A-Book operations is located.
-   A-Book coverage account — the account where A-Book operations are duplicated.
-   B-Book coverage group — the group where the account for duplicating B-Book operations is located.
-   B-Book coverage account — the account where B-Book operations are duplicated.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Ensure that the settings are correctly aligned: the specified coverage account must belong to the specified group. If you move the account or replace it with an account from a different group, be sure to update the group in the aggregated symbol settings accordingly.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Coverage groups must be located on the main trading server.</span></li></ul></td></tr></tbody></table>

When an order is filled through multiple deals, one aggregated deal with the total volume and volume-weighted average price is sent to the coverage account. This prevents data duplication in the system:

-   All A-Book deals are already mirrored on coverage accounts [at the liquidity provider level](/en/docs/mt5/platform/administration/ultency/ultency_reporting)
-   All B-Book deals already exist in your platform database

Example:

A client placed a Buy 100 EURUSD order. Of this, 50 lots are executed in A-Book, 25 lots are executed with one provider, and another 25 with a different provider. The remaining 50 lots are executed in B-Book.

The volume in A-Book was executed in three deals according to the order book:

-   5 lots at 1.16650
-   20 lots at 1.16651
-   25 lots at 1.16652

The volume in B-Book was executed in two deals in accordance with the order book:

-   20 lots at 1.16653
-   30 lots at 1.16654

As a result, you will see the following deals on the coverage accounts:

-   On the provider's general account  all five deals
-   On the A-Book account  one deal with a volume of 50 lots and a price of 1.166514, calculated as (5 \* 1.16650 + 20 \* 1.16651 + 25 \* 1.6652) \\ 50
-   On the B-Book account  one deal with a volume of 50 lots and a price of 1.166536, calculated as (20 \* 1.16653 + 30 \* 1.16654) \\ 50

## Turnover Report [#](ultency_reporting#turnover_report)

For additional control over operations, the platform includes the [server report](/en/docs/mt5/platform/administration/admin_reports) "Turnover by LP". It displays trading turnover with each liquidity provider used in Ultency. Data is categorized by symbol and time.

![Turnover Report](/en/docs/mt5/platform/img/ultency_turnover_by_lp.png "Turnover Report")

### Filters

Data requested for the report can be filtered. Specify the following parameters before requesting a report in the manager terminal:

-   Top symbols — the number of symbols with the highest turnover to be included in the report.
-   Symbols — the symbol or group of symbols to be included in the report.
-   Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas.
-   Period — starting and ending date of the period, for which the report will be generated.

### Report Content

The report contains two data tables: turnover by symbol and total daily turnover.

-   Symbol — the name of the aggregated symbol for which turnover is displayed.

-   ABook — the volume of operations in lots executed through liquidity providers.
-   Deals — the number of deals executed through liquidity providers.

-   BBook — the volume of B-Book operations (executed internally) in lots over the reporting period.

-   Deals — the number of deals executed on the platform side.

-   Total — the total volume of operations executed through Ultency during the reporting period.
-   \[Liquidity Provider Name\] — the volume of operations in lots executed through the specified provider over the reporting period.

-   Deals — the number of deals executed through the previously specified provider.

In addition, daily turnover data is visualized in a chart for easier analysis.

## LP Imbalance Report [#](ultency_reporting#imbalance)

The report provides brokers with transparent control over hedging in Ultency. It allows you to quickly identify discrepancies and optimize coverage across different liquidity providers. Reviewing the report prior to the daily rollover helps reduce operational and financing costs.

Based on the analysis of [coverage accounts](/en/docs/mt5/platform/administration/ultency/ultency_reporting#coverage), the report calculates the current aggregate position volume per symbol routed to each Ultency liquidity provider. Using this data, it determines the covered volume (Imbalance) that can be closed out. For example, the following EURUSD volumes have been routed:

-   LP1 — 100 lots Buy
-   LP2 — 100 lots Sell
-   LP3 — 50 lots Buy

The volumes at LP1 and LP2 fully cover each other. Closing these positions does not increase exposure to unhedged client positions, as they cover one another. By closing them, you reduce rollover charges associated with carrying positions overnight at liquidity providers.

To close the positions, connect to the coverage accounts linked to the respective liquidity providers. All trades executed on these accounts are automatically routed to the liquidity providers. In the example above, you need to:

-   Sell 100 lots on LP1 to close the corresponding Buy position volume.
-   Buy 100 lots on LP2 to close the corresponding Sell position volume.

In the report, Buy volumes are displayed as positive values, while Sell volumes are shown as negative values.

![LP Imbalance Report](/en/docs/mt5/platform/img/ultency_report_imbalance.png "LP Imbalance Report")

### Filters

Data requested for the report can be filtered. Before generating the report in the Manager terminal, specify the following parameters:

-   Matching Engine — the Ultency server processing the data.
-   Groups — the account groups for which the report should be generated. You may specify one or multiple groups separated by commas.

## LP Slippage By Symbols Report [#](ultency_reporting#slippage)

The Report enables brokers to conduct deeper analysis of order execution quality and liquidity provider performance. It shows exactly where slippage occurs — by individual symbols, volume ranges, or liquidity providers.

Slippage is a natural part of the trading process; however, controlling it is critical to maintaining fair and transparent execution. The LP Slippage by Symbols Report helps brokers:

-   Identify providers with systematically high negative slippage.
-   Detect instruments where execution quality requires attention.
-   Make data-driven decisions on liquidity flow redistribution.
-   Maintain a high level of client satisfaction.

![LP Slippage By Symbols Report](/en/docs/mt5/platform/img/ultency_report_lp_slippage.png "LP Slippage By Symbols Report")

### Filters

Data requested for the report can be filtered. Before generating the report in the Manager terminal, specify the following parameters:

-   Basis symbol — the [underlying symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#basis) for which trades will be included in the provider-level breakdown.
-   Groups — the account groups for which the report should be generated. You may specify one or multiple groups separated by commas.
-   Period — the start and end dates of the reporting period.
-   Min and max lots — the minimum and maximum trade volume (in lots) to be included in the report.

### Report Data

The report contains two data tables: slippage breakdown by symbols and by liquidity providers.

-   Symbol — financial instrument.
-   Liquidity Provider — name of the liquidity provider.
-   Total Orders — total number of orders routed via A-Book.
-   Slipped Orders — number of orders where slippage occurred.
-   Slipped, % — percentage of orders with recorded slippage.
-   AVG Slippage, pts — average slippage in points, including both favorable and unfavorable slippage.
-   Pos. Slippage, orders — number of orders with slippage in favor of the broker.
-   Pos. Slippage, % — percentage of orders with slippage in favor of the broker.
-   Pos. AVG Slippage, pts — average favorable slippage in points.
-   Neg. Slippage, orders — number of orders with slippage against the broker.
-   Neg. Slippage, % — percentage of orders with slippage against the broker.
-   Neg. AVG Slippage, pts — average unfavorable slippage in points.
-   Pos. Slippage, USD — total favorable slippage amount in USD.
-   Neg. Slippage, USD — total unfavorable slippage amount in USD.
-   Total Slippage, USD — net slippage amount in USD.

In addition to tabular data, provider-level slippage is visualized in diagrams for both the selected reporting period and the last 24 hours.

[Execution Books](/en/docs/mt5/platform/administration/ultency/ultency_execution_books)

[Service Desk](/en/docs/mt5/platform/administration/ultency/ultency_service_desk)