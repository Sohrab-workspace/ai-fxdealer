# Example of Rules

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/requests_routing/routing_example

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
                -   [Actions and Conditions](/en/docs/mt5/platform/administration/requests_routing/routing_rules)
                -   [Example of Rules](/en/docs/mt5/platform/administration/requests_routing/routing_example)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Routing](/en/docs/mt5/platform/administration/requests_routing)Example of Rules

# Example of Rules

In this section we will consider a set of routing rules for processing most common situations that appear in the processing of trade requests. The set consists of eight rules:

![Set of routing rules](/en/docs/mt5/platform/img/routing_example.png "Set of routing rules")

## Automate All Demo

This rule allows to automatically process all requests that come from demo accounts without any changes.

![Automate all demo](/en/docs/mt5/platform/img/routing_example_demo.png "Automate all demo")

The following parameters should be set up on the "Common" tab of the rule:

-   Perform action: Confirm by request price  
    Confirm requests at prices that are specified in orders.
-   Where request is: All  
    For all types of requests.
-   Where order is: All  
    For all types of orders.
-   Where conditions are: Client group = demo\\\*  
    For all sub-groups of the "demo" group.

## Allow Modification

This rule allows modifying positions and pending orders without any limitation. All operations of this type will be processed automatically without any changes.

![Allow modification](/en/docs/mt5/platform/img/routing_example_modify.png "Allow modification")

The following parameters are specified for this rule:

-   Perform action: Confirm by request prices  
    Confirm requests at prices that are specified in orders.
-   Where request is: SL & TP modification, Order modification, Order removal  
    For requests to change levels of Stop Loss and Take Profit of open positions, as well as to change and delete pending orders.
-   Where order is: All  
    For all types of orders.
-   Where conditions are: No  
    No additional conditions are required.

## Large Requests

This rule allows routing large trade requests to be processed by dealers.

![Large requests](/en/docs/mt5/platform/img/routing_example_large_req.png "Large requests")

The following parameters are specified in this rule:

-   Perform action: Process to dealers  
    Pass the processing to dealers specified in the ["Dealers"](/en/docs/mt5/platform/administration/requests_routing#dealers) tab.
-   Where request is: All  
    For all types of requests.
-   Where order is: All  
    For all types of orders.
-   Where conditions are: Request volume >= 10  
    For requests with the volume of 10 lots and more.

## Large Positions

This rule helps to prevent omission of the previous rule that limits automatic execution of requests larger than 10 lots. Some clients may attempt to open large positions by sending several requests of smaller volume. This rule analyzes the size of a client's position of a symbol.

![Large positions](/en/docs/mt5/platform/img/routing_example_large_pos.png "Large positions")

The following parameters are specified in this rule:

-   Perform action: Process to dealers  
    Pass the processing to dealers specified in the ["Dealers"](/en/docs/mt5/platform/administration/requests_routing#dealers) tab.
-   Where request is: All  
    For all types of requests.
-   Where order is: All  
    For all types of orders.
-   Where conditions are: Position volume >= 10  
    For requests, which being fulfilled, the symbol position will be equal to 10 lots or even larger.

## Medium Requests

This rule allows routing trade requests of average volumes to be processed by dealers. In this case this is a different group of dealers, other than that on the previous rule.

![Medium requests](/en/docs/mt5/platform/img/routing_example_med_req.png "Medium requests")

The following parameters are specified in this rule:

-   Perform action: Pass to dealers. Skip this rule if no dealers online.  
    Pass the processing to dealers specified in the ["Dealers"](/en/docs/mt5/platform/administration/requests_routing#dealers) tab. The additional condition is set - the rule will be skipped if there are no dealers online.
-   Where request is: All  
    For all types of requests.
-   Where order is: All  
    For all types of orders.
-   Where conditions are: Request volume >= 1  
    For requests with the volume equal to or larger than 1 lot.

## Medium Positions

This rule helps to prevent omission of the previous rule that limits automatic execution of requests larger than 1 lot. Some clients may attempt to open large positions by sending several requests of smaller volume. This rule analyzes the size of a client's position on this symbol.

![Medium positions](/en/docs/mt5/platform/img/routing_example_med_pos.png "Medium positions")

The following parameters are specified in this rule:

-   Perform action: Pass to dealers. Skip this rule if no dealers online.  
    Pass the processing to dealers specified in the ["Dealers"](/en/docs/mt5/platform/administration/requests_routing#dealers) tab. The additional condition is set - the rule will be skipped if there are no dealers online.
-   Where request is: All  
    For all types of requests.
-   Where order is: All  
    For all types of orders.
-   Where conditions are: Position volume >= 1  
    For requests, which being fulfilled, the symbol position will be equal to 1 lot or even larger.

## Requote Cheaters

This routing rule allows to block trade requests that are at non-market prices. For the additional condition, this rule takes into account the number of non-market requests sent by the client for this day.

![Requote cheaters](/en/docs/mt5/platform/img/routing_example_cheaters_requote.png "Requote cheaters")

The following parameters are specified in this rule:

-   Perform action: Requote  
    Send current market prices replying to the request.
-   Where request is: Request Execution, Instant Execution, Market Execution, Exchange Execution  
    This is the rule for the above execution types.
-   Where order is: Buy, Sell  
    For Buy and Sell orders.
-   Where conditions are: Deviation from market >= 10  
    For requests with the price that differs from the market price by 10 or more points. Clients who have sent 30 requests at non-market prices or more are taken into account.

## Automate Other Requests

This rule allows to automatically process requests that have not been processed according to the above rules. If such a rule is not specified at the end of the list, such requests will not be processed by the server.

![Automate other requests](/en/docs/mt5/platform/img/routing_example_other.png "Automate other requests")

The following parameters are specified in this rule:

-   Perform action: Confirm by market price  
    Confirm by prices specified in orders.
-   Where request is: All  
    For all types of requests.
-   Where order is: All  
    For all types of orders.
-   Where conditions are: No  
    No additional conditions are required.

[Actions and Conditions](/en/docs/mt5/platform/administration/requests_routing/routing_rules)

[Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)