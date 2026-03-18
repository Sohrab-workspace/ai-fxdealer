# Order Execution

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_execution

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Order Execution

# Order Execution

A client order submitted to Ultency may be executed in A-Book, B-Book, or hybrid mode, depending on [routing settings](/en/docs/mt5/platform/administration/ultency/ultency_routing). When routing orders to external liquidity providers, the system takes into account each provider's instrument settings, including execution policy, permitted volumes, and other constraints.

## Executed Order Volume [#](ultency_execution#volume)

The portion of an order routed to an external liquidity provider depends on the "A-Book/Coverage" and "Minimum coverage volume" parameters defined in the [routing rule](/en/docs/mt5/platform/administration/ultency/ultency_routing#coverage). When routing an order, the system validates the provider's [volume settings](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#trading).

If the routed order volume does not comply with the provider's volume step, it is rounded down to the nearest permitted increment. The remaining volume is executed in B-Book.

If the routed volume is below the provider's minimum allowable volume, the provider is skipped and the following entry is recorded in the log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table" style="height:15px;"><p class="p_CodeExample"><span class="f_CodeExample">2026.02.05&nbsp;18:11:12.079&nbsp;&nbsp;&nbsp;&nbsp;A-Book&nbsp;&nbsp;&nbsp;&nbsp;'2022':&nbsp;matching&nbsp;skipped&nbsp;#2170669441031&nbsp;XAGUSD&nbsp;vs&nbsp;liquidity&nbsp;provider&nbsp;#15&nbsp;LP1&nbsp;10002&nbsp;due&nbsp;to&nbsp;minimum&nbsp;volume&nbsp;limit</span></p></td></tr></tbody></table>

If the order volume is below the minimum allowable volume for all providers, the entire order is executed in B-Book.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table" style="height:15px;"><p class="p_CodeExample"><span class="f_CodeExample">2026.02.10&nbsp;16:36:49.478 &nbsp; &nbsp; &nbsp; &nbsp;A-Book &nbsp; &nbsp; &nbsp; &nbsp;'2022':&nbsp;remaining&nbsp;A-Book&nbsp;volume&nbsp;999.95&nbsp;for&nbsp;order&nbsp;#2170675666951&nbsp;sell&nbsp;500K&nbsp;/&nbsp;24K&nbsp;(abook:&nbsp;24.99995K&nbsp;/&nbsp;24K,&nbsp;bbook:&nbsp;475.00005K)&nbsp;AUDCAD&nbsp;at&nbsp;market&nbsp;is&nbsp;too&nbsp;small&nbsp;to&nbsp;be&nbsp;executed&nbsp;on&nbsp;liquidity&nbsp;providers&nbsp;and&nbsp;will&nbsp;be&nbsp;executed&nbsp;in&nbsp;B-Book</span></p></td></tr></tbody></table>

If the order cannot be executed with any provider (except in cases where the volume is below the minimum), it is rejected and an error is written to the log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table" style="height:15px;"><p class="p_CodeExample"><span class="f_CodeExample">2026.02.05&nbsp;17:47:19.114&nbsp;&nbsp;&nbsp;&nbsp;A-Book&nbsp;&nbsp;&nbsp;&nbsp;'2022':&nbsp;no&nbsp;liquidity&nbsp;to&nbsp;match&nbsp;order&nbsp;#2170667868167&nbsp;buy&nbsp;5M&nbsp;(abook:&nbsp;249.99995K,&nbsp;bbook:&nbsp;4.75000005M)&nbsp;AUDCAD&nbsp;at&nbsp;market&nbsp;in&nbsp;book&nbsp;reference&nbsp;#8089872305640964119</span></p></td></tr></tbody></table>

The selection of liquidity providers depends on the [execution mode](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution_type) configured for the aggregated symbol.

## Fill policy [#](ultency_execution#fill_policy)

When routing an order to an external liquidity provider, Ultency verifies whether the [fill policy](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#fill_policy) specified in the order is supported by that provider.

### Fill or Kill

A FOK order may be executed only with a single provider that supports this execution policy. In "[Aggregated providers / Mixed market depth](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution_type)" mode, FOK orders are not split across multiple providers; instead, they are executed entirely with the provider offering the best price.

If the selected provider does not support the FOK policy, the provider is skipped and the following log entry is added:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2026.02.05&nbsp;18:11:12.079&nbsp;&nbsp;&nbsp;&nbsp;A-Book&nbsp;&nbsp;&nbsp;&nbsp;'2022':&nbsp;matching&nbsp;skipped&nbsp;#2170669441031&nbsp;XAGUSD&nbsp;vs&nbsp;liquidity&nbsp;provider&nbsp;#15&nbsp;LP1&nbsp;10002&nbsp;due&nbsp;to&nbsp;FOK&nbsp;disabled&nbsp;on&nbsp;provider</span></p></td></tr></tbody></table>

If there is insufficient liquidity in the provider's order book to execute the FOK order, the provider is skipped and the following message is logged:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2026.02.05&nbsp;18:11:12.079&nbsp;&nbsp;&nbsp;&nbsp;A-Book&nbsp;&nbsp;&nbsp;&nbsp;'2022':&nbsp;matching&nbsp;skipped&nbsp;#2170669441031&nbsp;XAGUSD&nbsp;vs&nbsp;liquidity&nbsp;provider&nbsp;#15&nbsp;LP1&nbsp;10002&nbsp;due&nbsp;to&nbsp;not&nbsp;enough&nbsp;liquidity</span></p></td></tr></tbody></table>

If the order is partially covered and the A-Book portion is rejected by the provider, the B-Book portion is also rejected in full.

If, for any reason, the external provider partially fills a FOK order, the handling of the B-Book portion is governed by the "[Reject mode](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#reject_mode)" setting in the aggregated symbol configuration:

-   Reject — the B-Book portion is reduced proportionally to the executed A-Book volume. In this case, the execution behaves similarly to IOC described below.
-   B-Book — the unfilled portion of the A-Book volume is redirected to B-Book.

If the order cannot be executed with any provider (except in cases where the volume is below the minimum), it is rejected and an error is written to the log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table" style="height:15px;"><p class="p_CodeExample"><span class="f_CodeExample">2026.02.05&nbsp;17:47:19.114&nbsp;&nbsp;&nbsp;&nbsp;A-Book&nbsp;&nbsp;&nbsp;&nbsp;'2022':&nbsp;no&nbsp;liquidity&nbsp;to&nbsp;match&nbsp;order&nbsp;#2170667868167&nbsp;buy&nbsp;5M&nbsp;(abook:&nbsp;249.99995K,&nbsp;bbook:&nbsp;4.75000005M)&nbsp;AUDCAD&nbsp;at&nbsp;market&nbsp;in&nbsp;book&nbsp;reference&nbsp;#8089872305640964119</span></p></td></tr></tbody></table>

### Immediate or Cancel

In "[Aggregated providers / Mixed market depth](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#execution_type)" mode, an IOC order may be split across multiple providers to achieve the best available execution price. If a provider supports IOC mode, it is used; otherwise, FOK is applied.

If an order is rejected by a provider or partially executed with the remainder canceled, the remaining volume is routed to other providers.

If the order is partially covered and the A-Book portion is partially executed, the B-Book portion is reduced proportionally. For example:

-   The client places an IOC order for 20 lots.
-   According to the routing settings, 40% of the volume is routed externally — in this case, 8 lots. The remaining 12 lots are executed in B-Book.
-   External providers partially execute the A-Book portion — only 6 lots are filled.
-   Ultency proportionally reduces the B-Book portion from 12 lots to 8 lots.
-   As a result, the client receives a partial fill of 14 lots, while the broker maintains the configured coverage ratio.

If the order cannot be executed with any provider (except in cases where the volume is below the minimum), it is rejected and an error is written to the log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table" style="height:15px;"><p class="p_CodeExample"><span class="f_CodeExample">2026.02.05&nbsp;17:47:19.114&nbsp;&nbsp;&nbsp;&nbsp;A-Book&nbsp;&nbsp;&nbsp;&nbsp;'2022':&nbsp;no&nbsp;liquidity&nbsp;to&nbsp;match&nbsp;order&nbsp;#2170667868167&nbsp;buy&nbsp;5M&nbsp;(abook:&nbsp;249.99995K,&nbsp;bbook:&nbsp;4.75000005M)&nbsp;AUDCAD&nbsp;at&nbsp;market&nbsp;in&nbsp;book&nbsp;reference&nbsp;#8089872305640964119</span></p></td></tr></tbody></table>

[Conditions](/en/docs/mt5/platform/administration/ultency/ultency_routing/ultency_routing_conditions)

[Matching Orders](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders)