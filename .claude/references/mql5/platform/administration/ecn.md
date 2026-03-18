# Electronic Communication Network

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn

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
                -   [Forming Market Depth](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation)
                -   [Market Depth Journal](/en/docs/mt5/platform/administration/ecn/ecn_dom_journal)
                -   [Order Matching](/en/docs/mt5/platform/administration/ecn/ecn_matching)
                -   [Order Execution](/en/docs/mt5/platform/administration/ecn/ecn_execution)
                -   [Price Translations](/en/docs/mt5/platform/administration/ecn/ecn_translation)
                -   [Matching History](/en/docs/mt5/platform/administration/ecn/ecn_matching_history)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)ECN

# Electronic Communication Network

The trading platform allows you to implement your own Electronic Communication Network (ECN). The ECN allows you to:

-   Provide liquidity and best execution prices to your clients.
-   Profit from the matching of orders and spread widening when forwarding operations to an external system.
-   Become a full-fledged liquidity provider for other companies.
-   Implement your own trading facility.
-   Avoid using expensive third-party solutions.

## Market Depth formation algorithm

The ECN allows combining data from an unlimited number of external sources and this form a single quotes stream and the Market Depth feature for symbols.

The system receives Market Depth data from [gateways](/en/docs/mt5/platform/components/gateways) and [data feeds](/en/docs/mt5/platform/administration/admin_feeds), aggregates them and uploads to ordinary [symbols](/en/docs/mt5/platform/administration/admin_symbols). The entire operation is performed within the framework of a standard scheme of price data delivery to the platform, so no additional integration is required for the ECN.

Price data aggregation is flexibly configurable. The broker selects data sources and data to be collected. For example, you may choose to use Buy requests from one ECN gateway and Sell requests from a different one. Data can be additionally filtered by request volume, time, etc.

In addition to data aggregation from external sources, the ECN can collect orders placed by clients within a trading cluster. Thus, the broker's clients can see their own market and limit orders in the Market Depth. Separate settings are provided in the ECN for the aggregation of internal orders. The broker determines orders from specific groups or even individual clients which can be added to the Market Depth.

![Market Depth aggregation in the ECN](/en/docs/mt5/platform/img/ecn_dom_agregation.png "Market Depth aggregation in the ECN")

Price data in the ECN are aggregated using the special Price Aggregator engine. It directly connects to gateways and data feeds, and collects Market Depth changes from them in accordance with [translation settings](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#price_rules).

Another engine — Cluster Aggregator — collects price data from traders within the cluster. During server start, the engine collects the list of all open orders on all trade servers within the cluster and then maintains this data up to date in accordance with all trade transactions performed on servers. Cluster Aggregator notifies Price Aggregator about changes in order status. Based on such notifications, Price Aggregator maintains the Market Depth feature in an up-to-date state.

All received data is recorded in ECN symbols.

![Price aggregation in the ECN](/en/docs/mt5/platform/img/ecn_price_aggregation.png "Price aggregation in the ECN")

## Enabling of ECN and operation statistics

The ECN can be enabled or disabled under the Status section. The same section contains general system operating statistics:

-   Total requests — the total number of requests received by the ECN for processing. These include not only market operation requests, but also requests to modify or delete orders.
-   Total active orders — the number of orders currently waiting to be matched (which are currently being processed).
-   Total deals in ECN — the total number of deals, which have been created as a result of order matching within the cluster.
-   Total deals in Gateways — the total number of deals, which have been created as a result of order matching with external liquidity providers.
-   Price ticks — the number of ticks which have been generated by the ECN. In fact, these are the ticks which are created during deal execution (they reflect the Last price changes).
-   Price books — the number of order book changes which have been generated by the ECN as a result of aggregation.

![ECN Status](/en/docs/mt5/platform/img/ecn_common.png "ECN Status")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">In case of server restart, the existing ECN operation statistics is reset and collection of statistics starts from scratch.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">When disconnected, the ECN does not collect any price data and it does not process orders, which are forwarded to the ECN in accordance with routing rules.</span></li></ul></td></tr></tbody></table>

[Become a Provider](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_offers)

[Forming Market Depth](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation)