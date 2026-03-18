# Routing

> Source: https://support.metaquotes.net/en/docs/mt5/manager/ultency_routing

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
                -   [Conditions](/en/docs/mt5/manager/ultency_routing/ultency_routing_conditions)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Ultency](/en/docs/mt5/manager/ultency)Routing

# Routing

To define how trading requests are processed inside Ultency, use the "Routing" section in the settings of the respective Ultency server. Depending on various conditions (symbol, volume, trader group, etc.), you can manage trade execution flexibly, such as routing orders to different providers or rejecting them.

![Configure trade requests routing rules](/en/docs/mt5/manager/img/ultency_routing.png "Configure trade requests routing rules")

Через менеджерский терминал можно только изменять существующие правила. Для создания новых правил используйте [терминал администратора](https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_routing).

Для правил доступны следующие параметры:

-   Name — name of the routing rule.
-   Perform action — action to be taken when a request matches the [rule conditions](/en/docs/mt5/manager/ultency_routing#conditions).
    -   Route to Ultency symbol — the request will be executed based on the settings of the specified aggregated symbol.
    -   Reject — the request will be rejected.
-   Symbol — aggregated symbol according to which the request will be executed. For convenience, symbols can be specified as subgroups. For example, Forex\\\*. Based on the symbol in the incoming request, Ultency will automatically select a matching aggregated symbol from this subgroup. See symbol selection logic [below](/en/docs/mt5/manager/ultency_routing#symbol_matching).
-   A-Book/Coverage — portion of the order to be sent to an external provider (A-Book share). 0 indicates that the entire order will be executed internally (B-Book), 100  the entire order will be routed to an external liquidity provider as per [execution settings](https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution).

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

![Conditions for a routing rule](/en/docs/mt5/manager/img/ultency_routing_conditions.png "Conditions for a routing rule")

A detailed description of available conditions is provided in a [separate section](/en/docs/mt5/manager/ultency_routing/ultency_routing_conditions).

## Rule Execution Order [#](ultency_routing#priority)

Rules are executed from the top downwards. If an incoming request matches the conditions of the first rule, it will be processed according to that rule. If it doesn't match, the system checks the next rule, and so on.

Для изменения положения правил в списке используйте [терминал администратора](https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_routing#priority).

## How Aggregated Symbols Are Selected [#](ultency_routing#symbol_matching)

Routing rules enable different handling of operations on the same instrument, depending on the conditions. For example, EURUSD orders from clients in the real\\regular group may be routed to one liquidity provider, while forwarding orders from real\\vip clients to another. To implement such differentiation, create separate [sets of aggregated symbols](https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_routing#routing_ultency). Then, define a specific routing rule for each client group, indicating the corresponding subgroup of aggregated symbols as the symbol.

Example: Assume that Ultency has two sets of aggregated instruments:

-   Forex\\Liquidity Provider 1\\\*. The subgroup contains EURUSD.lp1 which has EURUSD set as its [basis symbol](https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#basis).
-   Forex\\Liquidity Provider 2\\\*. This subgroup contains EURUSD.lp2 which also has EURUSD as the basis symbol.

Each symbol is configured to execute through its respective liquidity provider.

Through [symbol translation settings](https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_translations), both subgroups are mapped to a single symbol set on the trading platform side:

-   Forex\\Liquidity Provider 1\\\* -> Ultency\\Forex\\\*
-   Forex\\Liquidity Provider 2\\\* -> Ultency\\Forex\\\*

As a result, the trading platform features a single symbol, Ultency\\Forex\\EURUSD, available for client trading. A routing rule is then set up as follows:

![Example of a routing rule](/en/docs/mt5/manager/img/ultency_routing_example.png "Example of a routing rule")

How the selection works:

1.  When a trading request for EURUSD is received, the system checks the routing rules from top to bottom and identifies the first rule that matches the request conditions. Let's say the rule specified above applies.
2.  The system checks the group of aggregated symbols specified in the rule. In this case, it is Forex\\Liquidity Provider 1\\\*.
3.  Ultency checks the list of instruments in the Forex\\Liquidity Provider 1\\\* subgroup and selects the one whose basis symbol matches the symbol in the request  EURUSD. In this case, it is EURUSD.lp1. This symbol will be used to execute the client's order.

[Ultency](/en/docs/mt5/manager/ultency)

[Conditions](/en/docs/mt5/manager/ultency_routing/ultency_routing_conditions)