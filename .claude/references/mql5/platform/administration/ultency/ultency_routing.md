# Routing

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_routing

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
                    -   [Conditions](/en/docs/mt5/platform/administration/ultency/ultency_routing/ultency_routing_conditions)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Routing

# Routing

To ensure client trading requests are forwarded to Ultency for execution, define [routing rules](https://support.metaquotes.net/ru/docs/mt5/platform/administration/requests_routing). In the Common settings, specify which requests should be routed to Ultency. For example, all requests for symbols matching Ultency\*. Select "Send to Ultency" for the action and specify the Ultency server that will handle execution.

![Trade request routing in Ultency](/en/docs/mt5/platform/img/ultency_platform_routing.png "Trade request routing in Ultency")

Requests forwarded to Ultency in accordance with the routing rules will be processed according to Ultency's internal rules.

## Internal Routing in Ultency [#](ultency_routing#routing_ultency)

To define how trading requests are processed inside Ultency, use the "Routing" section in the settings of the respective Ultency server. Depending on various conditions (symbol, volume, trader group, etc.), you can manage trade execution flexibly, such as routing orders to different providers or rejecting them.

To implement different execution conditions for the same symbols, create separate sets of aggregated instruments. Select the required symbols from the list and choose "Add Copy" from the context menu.

![Export aggregated symbol settings to create a copy](/en/docs/mt5/platform/img/ultency_aggregated_symbols_add_copy_menu.png "Export aggregated symbol settings to create a copy")

Next, define a postfix that will be added to all symbol names in the new set. You should also specify a subfolder name where these symbol copies will be placed.

![Creating a copy of aggregated symbols](/en/docs/mt5/platform/img/ultency_aggregated_symbols_add_copy.png "Creating a copy of aggregated symbols")

After creating copies, adjust their settings as needed.

Once you have prepared the necessary sets of aggregated symbols, proceed to configure routing rules:

![Configure trade requests routing rules](/en/docs/mt5/platform/img/ultency_routing.png "Configure trade requests routing rules")

Create a rule and specify the following parameters:

-   Name — name of the routing rule.
-   Perform action — action to be taken when a request matches the [rule conditions](/en/docs/mt5/platform/administration/ultency/ultency_routing#conditions).
    -   Route to Ultency symbol — the request will be executed based on the settings of the specified aggregated symbol.
    -   Reject — the request will be rejected.
-   Symbol — aggregated symbol according to which the request will be executed. For convenience, symbols can be specified as subgroups. For example, Forex\\\*. Based on the symbol in the incoming request, Ultency will automatically select a matching aggregated symbol from this subgroup. See symbol selection logic [below](/en/docs/mt5/platform/administration/ultency/ultency_routing#symbol_matching).
-   A-Book/Coverage — portion of the order to be sent to an external provider (A-Book share). 0 indicates that the entire order will be executed internally (B-Book), 100  the entire order will be routed to an external liquidity provider as per [execution settings](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution).

### Minimum coverage volume [#](ultency_routing#minimum_coverage)

In the "Minimum Coverage Volume" field, you can specify the volume (in lots) that will always be executed via B-Book, regardless of the percentage set in the "A-Book/Coverage" field. For example, an order of 30 lots is received for execution, and the following settings are specified:

-   A-Book/Coverage = 20%
-   Minimum Coverage Volume = 10 lots

10 lots will be executed unconditionally via B-Book, while the remaining 20 lots will be distributed according to the coverage percentage: 4 lots to A-Book and 16 lots to B-Book. In total, 26 lots will be executed via B-Book, and 4 lots via A-Book.

If the A-Book portion is partially filled, the B-Book portion exceeding the minimum coverage volume will be reduced proportionally. So, if only 3 out of 4 lots are filled via A-Book in the above example, the 16 lots intended for B-Book (beyond the minimum coverage volume) will be reduced proportionally to 12 lots. Final result:

-   3 lots executed via A -Book
-   22 lots executed via B-Book
-   5 lots remain unfilled

## Rule Conditions [#](ultency_routing#conditions)

To define which requests should be processed according to the rule, specify a set of conditions:

![Conditions for a routing rule](/en/docs/mt5/platform/img/ultency_routing_conditions.png "Conditions for a routing rule")

A detailed description of available conditions is provided in a [separate section](/en/docs/mt5/platform/administration/ultency/ultency_routing/ultency_routing_conditions).

## Rule Execution Order [#](ultency_routing#priority)

Rules are executed from the top downwards. If an incoming request matches the conditions of the first rule, it will be processed according to that rule. If it doesn't match, the system checks the next rule, and so on.

To reorder rules, use the "![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up" and "![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down" options in the context menu or the corresponding commands in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu and [Standard Toolbar](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard).

## How Aggregated Symbols Are Selected [#](ultency_routing#symbol_matching)

Routing rules enable different handling of operations on the same instrument, depending on the conditions. For example, EURUSD orders from clients in the real\\regular group may be routed to one liquidity provider, while forwarding orders from real\\vip clients to another. To implement such differentiation, create separate sets of aggregated symbols as mentioned earlier. Then, define a specific routing rule for each client group, indicating the corresponding subgroup of aggregated symbols as the symbol.

Example: Assume that Ultency has two sets of aggregated instruments:

-   Forex\\Liquidity Provider 1\\\*. The subgroup contains EURUSD.lp1 which has EURUSD set as its [basis symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#basis).
-   Forex\\Liquidity Provider 2\\\*. This subgroup contains EURUSD.lp2 which also has EURUSD as the basis symbol.

Each symbol is configured to [execute](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution) through its respective liquidity provider.

Through [symbol translation settings](/en/docs/mt5/platform/administration/ultency/ultency_translations), both subgroups are mapped to a single symbol set on the trading platform side:

-   Forex\\Liquidity Provider 1\\\* -> Ultency\\Forex\\\*
-   Forex\\Liquidity Provider 2\\\* -> Ultency\\Forex\\\*

As a result, the trading platform features a single symbol, Ultency\\Forex\\EURUSD, available for client trading. A routing rule is then set up as follows:

![Example of a routing rule](/en/docs/mt5/platform/img/ultency_routing_example.png "Example of a routing rule")

How the selection works:

1.  When a trading request for EURUSD is received, the system checks the routing rules from top to bottom and identifies the first rule that matches the request conditions. Let's say the rule specified above applies.
2.  The system checks the group of aggregated symbols specified in the rule. In this case, it is Forex\\Liquidity Provider 1\\\*.
3.  Ultency checks the list of instruments in the Forex\\Liquidity Provider 1\\\* subgroup and selects the one whose [basis symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#basis) matches the symbol in the request  EURUSD. In this case, it is EURUSD.lp1. This symbol will be used to execute the client's order.

[Translations of Symbols and Quotes](/en/docs/mt5/platform/administration/ultency/ultency_translations)

[Conditions](/en/docs/mt5/platform/administration/ultency/ultency_routing/ultency_routing_conditions)