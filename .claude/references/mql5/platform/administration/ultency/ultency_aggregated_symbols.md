# Aggregated Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Aggregated Symbols

# Aggregated Symbols

Ultency receives price data from multiple liquidity providers and consolidates it into a single stream. As a result, your clients get better execution prices. This makes trading more attractive and cost-efficient for clients and helps you to attract new traders. In addition to external provider data, Ultency allows you to aggregate your own clients' orders into the order book, enabling the broker to operate as a fully functional ECN.

To collect price data, you need to create aggregated symbols. To avoid creating them manually, simply select the symbols imported from a provider and choose "Copy to Aggregated Symbols":

![Create aggregated symbols based on provider symbols](/en/docs/mt5/platform/img/ultency_aggregated_symbols_copy.png "Create aggregated symbols based on provider symbols")

As a result, the selected symbols will be automatically added to the Aggregated Symbols section, within the same subgroup and with the same settings, including name, description, basis symbol, and trading sessions. Price feeds from the selected provider will also be enabled for these symbols by default.

![Aggregated symbols that will consolidate data from different providers](/en/docs/mt5/platform/img/ultency_aggregated_symbols.png "Aggregated symbols that will consolidate data from different providers")

Once this is done, proceed to configure the remaining parameters.

## Common [#](ultency_aggregated_symbols#common)

![Common settings of the aggregate symbol](/en/docs/mt5/platform/img/ultency_aggregated_symbols_common.png "Common settings of the aggregate symbol")

The following settings are available in the "Common" section:

-   Aggregated symbol — the name of the aggregated symbol.
-   Description — a brief description of the symbol.
-   Basis symbol — the name of the instrument associated with the symbol received from a provider. Each aggregated symbol must have a designated basis symbol, which defines the instrument for which data is collected, as well as the list of providers whose data should be aggregated. Ultency scans all selected providers and aggregates data from instruments that share the [specified](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#basis) basis symbol. The basis symbol is also used for [routing requests](/en/docs/mt5/platform/administration/ultency/ultency_routing).  
       
    A single provider cannot have multiple symbols with the same basis symbol.

-   Base currency digits — the number of decimal places used for calculations in the base currency.

-   Tick size — the minimal step of the price change. This value is used for calculating [profit](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/profit_calculation#futures), [margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula#cfd_index) and [swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps) for CFD Index and Futures. Also, this values is used for rounding the quotes passed form [data feeds](/en/docs/mt5/platform/administration/admin_feeds): for all financial instruments with the disabled [Market Depth](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#dom) and non-exchange instruments (other than Exchange\*) with the enabled Market Depth.
-   Tick value — the cost of one point of the price change. This value is used for calculating [profit](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/profit_calculation#futures), [margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula#cfd_index) and [swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps) for CFD Index and Futures.
-   Calculation — type of calculation of [margin requirements](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex) and [profit](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/profit_calculation) on a symbol. This parameter also influences the calculation of [swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps). The following calculation types are available:

-   Forex — calculation for Forex symbols.

-   Forex No Leverage — totally equivalent to the Forex type except that the client leverage is not taken into account when calculating the margin. Forex No Leverage can be used if it is necessary to calculate the margin with a fixed leverage for all clients regardless of their actual leverage. If this type is selected, the client leverage is not taken into account when [calculating the margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula#noleverage). A fixed leverage can be set through [margin rates](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin_rates) (for example, the rate of 0.01 is similar to the leverage of 1:100).

-   CFD — calculation for CFD.
-   Futures — calculation for Futures.
-   CFD Index — calculation for CFD indexes.
-   CFD Leverage — calculation for CFD with the account of the leverage.
-   Exchange Stocks — calculation for exchange stocks.

-   Exchange MOEX Stocks — calculation for stocks traded at Moscow Exchange.

-   Exchange Bonds — calculation for exchange [bonds](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_bonds).

-   Exchange MOEXBonds — calculation for [bonds](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_bonds) traded at Moscow Exchange.

-   Exchange Futures — calculation for exchange [futures](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_futures).
-   Exchange FORTS Futures — calculation for the FORTS exchange. This mode must only be used together with the [MOEX Deivatives Gateway](/en/docs/mt5/platform/components/gateways/moex_derivatives). Otherwise the margin requirements calculation results may be unpredictable.

-   Exchange Option — calculation for exchange [options](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_options).
-   Collateral — non-tradable instruments of this type are used as client's [assets to provide the required margin for open positions](/en/docs/mt5/platform/administration/admin_accounts/account_edit#collateral) of other instruments. For these instruments the margin and profit are not calculated.

## Coverage [#](ultency_aggregated_symbols#coverage)

![Configuring coverage symbols](/en/docs/mt5/platform/img/ultency_aggregated_symbols_coverage.png "Configuring coverage symbols")

To ensure precise control over the execution of trades for an aggregated symbol, all operations related to that symbol are duplicated to separate coverage accounts. One account collects all transactions routed to external providers (A-Book), while another collects all operations executed within the platform (B-Book).

If you do not specify coverage groups/accounts when adding the configuration for an aggregated symbol, Ultency will automatically copy them from the configurations of other symbols. If the groups/accounts are not yet specified anywhere, Ultency will automatically create new groups and accounts and add them to the aggregated symbol's configuration. The groups are created with the [netting accounting system](/en/docs/mt5/platform/administration/admin_groups/group_position#netting), allowing you to view the net positions for all clients. These groups and accounts will be immediately added to the aggregated symbol's settings. You can control system operations by requesting reports for the relevant groups and accounts through the Manager terminal. For more details, refer to the "[Control and Reporting](/en/docs/mt5/platform/administration/ultency/ultency_reporting#coverage)" section.

-   Coverage symbol — if this option is enabled, coverage deals for the aggregated symbol will be executed on the original MetaTrader 5 symbols from which client requests are [routed](/en/docs/mt5/platform/administration/ultency/ultency_routing) to this aggregated symbol. If you wish to cover trades on a different symbol, disable this option and specify the symbol in the following field.
-   Coverage symbol — the name of the symbol where trades will be duplicated. It is used only when the "Coverage on client symbol" is disabled.
-   A-Book coverage group — the group where the account for duplicating A-Book operations is located.
-   A-Book coverage account — the account where A-Book operations are duplicated.
-   B-Book coverage group — the group where the account for duplicating B-Book operations is located.
-   B-Book coverage account — the account where B-Book operations are duplicated.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Ensure that the settings are correctly aligned: the specified coverage account must belong to the specified group. If you move the account or replace it with an account from a different group, be sure to update the group in the aggregated symbol settings accordingly.</span></p></td></tr></tbody></table>

## Quotes [#](ultency_aggregated_symbols#quotes)

![Quote aggregation settings](/en/docs/mt5/platform/img/ultency_aggregated_symbols_quotes.png "Quote aggregation settings")

This section defines the settings for quote aggregation:

-   Type — type of quote aggregation:
    -   Prioritized providers / Only one active — only one provider is used, the first available one from the [list](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#quotes_providers). If the first provider remains unavailable for the duration specified in the "Quote switch timeout" parameter, the system will switch to the next provider in the list.
    -   Aggregated providers / Mixed market depth — the market depth is formed from the prices of providers in the [list](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#quotes_providers).
    -   Aggregated providers with own orders / Mixed market depth — the market depth is formed from the prices of providers in the [list](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#quotes_providers) and client requests inside the platform. The mode is currently under development.
-   Digits — the number of decimal places to which prices received from sources will be rounded.
-   Market depth — the number of orders/levels displayed in the order book. Depth is set for one side. For example, if set to 16, the book will display up to 16 buy orders and up to 16 sell orders. If the market depth is disabled (the value of 0), requests in B-Book mode are executed in full at best prices.
-   Min. spread — the minimum spread that will be maintained in the instrument's price book, even when orders come in at better prices. More detailed information is provided [below](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#spread).
-   Max. spread — the maximum spread that will be maintained in the instrument's price book, even when orders come in at worse prices. More detailed information is provided [below](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#spread).
-   Ask markup — the number of points by which all ask prices (the ask side of the order book) will be shifted. A positive or negative value can be specified. The markup is applied before the minimum and maximum spread settings.
-   Bid markup — the number of points by which all bid prices (the bid side of the order book) will be shifted. A positive or negative value can be specified. The markup is applied before the minimum and maximum spread settings.
-   Quote switch timeout — used only for aggregation in "Prioritized providers / Only one active" mode. If quotes do not arrive from the prioritized provider within the specified number of seconds, the stream switches to the next provider in the [list](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#quotes_providers). When quotes from the first provider resume, the stream automatically switches back. Upon the end of a quoting session for the prioritized provider, the switch to the next provider occurs immediately, without the timeout.

-   Enable real-time quotes — disable this option if you want to use an aggregated symbol solely for trading, without transmitting any quotes from Ultency. For example, if you wish to trade via Ultency while broadcasting quotes through your own [data feed](/en/docs/mt5/platform/administration/admin_feeds) or [gateway](/en/docs/mt5/platform/administration/admin_gateways). When quotes are disabled, Ultency will continue to maintain an internal order book for B-Book order execution. Orders will still be executed at prices sourced from liquidity providers according to the aggregated symbol settings. However, this internal order book will not be visible to traders.

### Providers [#](ultency_aggregated_symbols#quotes_providers)

This section defines the list of providers whose quotes can be aggregated for the given instrument. The order of providers in the list determines their priority. The first provider is considered the highest priority.

### Minimum and maximum spread [#](ultency_aggregated_symbols#spread)

When aggregating order books from multiple sources and combining orders within the cluster, situations may arise where both sides of a trade are willing to execute at worse prices than actually available. For example, one provider may offer to buy an asset at a price of 100, while another may offer to sell the same asset at 90\. If the actual spread for the symbol becomes narrower than the minimum allowed, Ultency will adjust the displayed prices in the order book to maintain the required spread. Actual order prices remain unchanged, and trades are still executed at provider prices.

The adjustment to maintain the minimum spread is done using the following algorithm:

-   The current spread is calculated as the difference between the best Bid and Ask. The calculation applies all [markups](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#markup) specified for the aggregated symbol.
-   If the current spread is smaller than the defined minimum, the system calculates the spread delta. It is the amount by which the spread needs to be widened.
-   New Bid and Ask prices are computed. Bid New = Bid - floor(spread\_delta/2) points. Ask New = Ask + ceil(spread\_delta/2) points. Here 'floor' and 'ceil' are standard functions for getting the nearest integer value from below and above.
-   For all buy orders with prices higher than Bid New, the visible price is adjusted to Bid New.
-   For all sell orders with prices lower than Ask New, the visible price is adjusted to Ask New.

The Maximum Spread parameter works in a similar way. If the actual spread exceeds the specified maximum, all orders are shifted to reduce the spread.

## Execution [#](ultency_aggregated_symbols#execution)

![ultency_aggregated_symbols_execution](/en/docs/mt5/platform/img/ultency_aggregated_symbols_execution.png)

This section defines order execution settings for the aggregated symbol:

### Type [#](ultency_aggregated_symbols#execution_type)

Order execution type for the symbol:

-   Prioritized providers / Only one active — only one provider is used, the first available from the list in the [Execution](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution_providers) section. If the first provider is unavailable, disabled, or trading is not possible (for example, if there is no active trading session at the moment), the system will automatically attempt to route the order through the next available provider.
-   Best provider — orders are executed through the provider (from the list in the "[Execution](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution_providers)" section) that offers the best available VWAP price for the requested volume.
-   Aggregated providers / Mixed market depth — orders are executed through providers from the list in the "[Execution](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution_providers)" section. Orders can be executed through different providers, including partially. [FOK](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#fill_policy) orders are always executed through only one provider, which currently offers the best available price for the requested volume (as in the "Best provider" mode) and which supports the FOK fill mode.
-   Exchange mode / Own orders only — orders are not routed to external providers. The order book is formed exclusively from your clients' orders. The mode is currently under development.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Find more information in the "<a href="/en/docs/mt5/platform/administration/ultency/ultency_execution" class="topiclink">Order Execution</a>" section.</span></p></td></tr></tbody></table>

### B-Book price mode [#](ultency_aggregated_symbols#b_book_mode)

Ultency allows partial coverage of orders. In the [routing settings](/en/docs/mt5/platform/administration/ultency/ultency_routing#coverage), you can specify what portion of each order should be executed via external providers (A-Book) and what portion should be executed internally within the cluster (B-Book). The "B-Book price mode" parameter defines how the non-covered (B-Book) portion of the order is executed:

-   VWAP — the uncovered volume is executed at prices from the aggregated order book.
-   A-Book — the volume is executed at the same price as the covered volume with the external provider. This mode provides additional protection from off-market prices, assuming the liquidity provider (especially a large one) uses robust filtering mechanisms to avoid incorrect executions.

### B-Book Market Depth Depletion [#](ultency_aggregated_symbols#bbook_depletion)

The B-Book Market Depth Depletion feature reduces available volume at price levels after order execution, simulating real Depth of Market depletion, and restores levels based on the liquidity provider's quote stream. This functionality enables brokers to prevent the effect of unlimited B-Book liquidity and the execution of multiple orders at the best available price.

How it works:

-   Execution of a client order reduces volume at the corresponding Depth of Market levels and marks those levels as Depleted.
-   When an update for the corresponding price is received from the liquidity provider, the depleted level is restored.
-   If no update is received from the provider within the configured timeout period, the level is forcibly restored.
-   If the provider sends a cancellation for a level, the corresponding depleted level is removed entirely.

![Depleted Levels in the Depth of Market](/en/docs/mt5/platform/img/dom-depletion.png "Depleted Levels in the Depth of Market")

### Reject mode [#](ultency_aggregated_symbols#reject_mode)

This setting determines how an order will be handled if rejected by the current prioritized provider:

-   Reject — the order is rejected.
-   B-Book — the order is executed internally within the platform without routing to external providers.

This setting is applied in all execution modes except [Exchange mode / Own orders only](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution_type).

### Slippages [#](ultency_aggregated_symbols#slippage)

This section defines how much the execution price in Ultency can deviate from the client's requested price.

-   Profitable — the number of points by which the price may deviate from the requested one, in a profitable direction for the client.
-   Losing — the number of points by which the price may deviate from the requested one, in an unprofitable direction for the client.

The function has a different behavior depending on the execution mode:

-   A-Book — after an actual deal is executed with the external provider, Ultency compares the execution price with the initially requested price ([considering translation settings](/en/docs/mt5/platform/administration/ultency/ultency_translations)). If the executed price is within the allowed slippage range, the deal is executed on the platform side at the client's original requested price. If the slippage exceeds the limit, Ultency will execute the order on the platform side at the actual execution price applied on the provider side.  
       
    Suppose both profitable and losing slippage values are set to 5 points. Ultency sends a Buy Limit order at 1.14053 to the external provider, but the provider fills it at 1.14051 (2 points better). This slippage is acceptable. Ultency will fill the client's order at the original price, 1.14053.  
       
    If the provider's execution price exceeds the slippage limit, Ultency will fill the order at that price, i.e. 1.14051.
-   B-Book — the price requested by the client is compared to the prices in the aggregated order book, considering the [order fill type](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#fill_policy). For example, if a FOK order cannot be fully filled at acceptable prices, it will be completely rejected. An IOC order will be partially filled within available volumes at acceptable prices.

### Merge execution deals [#](ultency_aggregated_symbols#merge_deals)

Depending on the settings, deals may be split across different sources, partially in B-Book, and partially in A-Book with multiple providers. Ultency records the entire execution chain and can display it to the trader: the trading history on the trader's side will display all deals that executed the order. To hide execution details from traders, enable "Merge execution deals". In this case, all trades used to fill the order on the Ultency side will be presented in the platform as a single combined operation, showing total volume and weighted average price. Thus, the trader will also see a single trader in the account history.

Merging deals affects [slippage](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#slippage) parameters. If merging is disabled, slippage is checked for each individual deal that executes the order. If enabled, slippage is checked only for one combined deal (at the weighted average price).

### Limit and Take Profit orders activation [#](ultency_aggregated_symbols#limit_activation)

Configure how limit orders, [not previously routed to Ultency](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#limit_processing), and Take Profit activations are handled:

-   Mode — type of order to be sent to Ultency upon activation of Take Profit levels and limit orders not previously routed to Ultency. Options: "Limit" and "Market".
-   Timeout — the lifetime of an order routed to Ultency (in milliseconds). If the order is not executed within this time, this order is canceled. In case of the re-activation of a limit order or the Take Profit level, a new order with the specified timeout will be sent to Ultency.

By default, Ultency displays limit orders with a lifetime of 5 seconds.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">These settings do not apply to Stop Loss activations, which are always sent as market orders.</span></p></td></tr></tbody></table>

### Processing limit orders outside Ultency [#](ultency_aggregated_symbols#limit_processing)

You can configure limit orders to remain off Ultency until triggered. Configure [routing rules](/en/docs/mt5/platform/administration/requests_routing/routing_rules) to prevent such orders from being sent for matching before their activation.

Add a rule to process the placing of limit and stop limit orders, as well as the stop limit order activation without forwarding to Ultency. Please note that routing rules are processed top-downward. For example, if you have a general rule according to which all requests are sent to Ultency, then a new rule for processing limit orders should be located above the general one in the list.

![Routing rule for processing limit orders outside Ultency](/en/docs/mt5/platform/img/ultency_routing_limit.png "Routing rule for processing limit orders outside Ultency")

### Providers [#](ultency_aggregated_symbols#execution_providers)

This section defines a list of providers through which orders for this instrument can be executed. The order of providers in the list determines their priority. The first provider is considered the highest priority.

## Levels [#](ultency_aggregated_symbols#bands)

Use these settings to fine-tune aggregation and display of order book levels: combine aggregated levels from different sources by volume for a cleaner, more user-friendly order book. This can be used when processing orders in B-Book mode, when you act as a market maker and there's no need to show all the initial levels from providers.

![Configuring Market Depth levels](/en/docs/mt5/platform/img/ultency_aggregated_symbols_bands.png "Configuring Market Depth levels")

Set volume per level in the number of contracts. The levels are set separately for each side (Bid/Ask). Example for Bid side:

-   First level = 100 000, markup = -1. Ultency will collect the closest orders aggregated to 100,000 contracts into one level. The level price will be set to the volume-weighted average price minus 1 point. The volume is 100,000.
-   Second level = 300,000, markup = -2. Ultency will collect the closest orders aggregated to 300,000 contracts into one level. The level price will be set to the volume-weighted average price minus 2 points. The volume is 300,000. Please note that the volume is always counted from the top of the order book (the price closest to the market), and not from the previous level.
-   The same applies to the other levels.
-   Level ∞. This is a technical level. Its price is calculated as a weighted average of all orders used to form the previous level, adjusted by its own markup. It is not visible in the market depth but is used for order execution  all orders that do not fall into the other levels are executed at this price.

Important: If there isn't enough actual volume to fill a level, the full configured volume is still displayed in the market depth.

Let's consider order merging using two symbols as an example: EURUSD.raw, which is the original aggregated market depth with no level settings specified, and EURUSD with level settings used.

![Example of level settings](/en/docs/mt5/platform/img/ultency_bands_example.png "Example of level settings")

The orders of the original market depth will be displayed as follows:

![Example of combining levels](/en/docs/mt5/platform/img/ultency_bands_example_dom.png "Example of combining levels")

## Sessions [#](ultency_aggregated_symbols#sessions)

Define quote and trade sessions for the aggregated symbol. These sessions can be independent of [provider-side sessions](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#sessions), but make sure providers collectively cover the time to avoid gaps in quotes and execution.

![Configuring symbol sessions](/en/docs/mt5/platform/img/ultency_aggregated_symbols_sessions.png "Configuring symbol sessions")

Click on a day to adjust its session settings:

![Intraday session settings](/en/docs/mt5/platform/img/ultency_provider_symbols_sessions_edit.png "Intraday session settings")

To configure the time of quote and trading sessions separately, enable the corresponding option. Next, set up the sessions. The sliders that control session beginning and end times can be moved with the mouse and with the arrow keys. You can hold down the Shift key to slow down the slider speed. This enables precision of up to minutes when configuring sessions.

[Provider Symbols](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols)

[Translations of Symbols and Quotes](/en/docs/mt5/platform/administration/ultency/ultency_translations)