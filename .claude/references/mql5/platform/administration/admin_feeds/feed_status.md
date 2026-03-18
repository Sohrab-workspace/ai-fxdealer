# Status

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_feeds/feed_status

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
                -   [Configuration of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_setup)
                -   [Status](/en/docs/mt5/platform/administration/admin_feeds/feed_status)
                -   [Journal of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed)
                -   [Restarting Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/data_feed_restart)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_feeds/feed_service)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)Status

# Status

This page features general information about the data feed: description, version, settings and statistics. From the same page, you can quickly enable and disable the data feed.

To access this section, select a data feed in the tree or click on it in the product showcase.

![Data Feed Status](/en/docs/mt5/platform/img/feed_status.png "Data Feed Status")

## Basic Data

Basic information about the data feed is shown at the top of the window:

-   Module — the name of the data feed executable file.
-   API Version — version and data of the Gateway API, which was used for creating the data feed.
-   Signed by — the company by which the data feed executable is signed.
-   Certificate issued by — the certification authority that issued the certificate to the above company.

## Configuration

The main data feed settings are shown in this block:

-   Source — data transmitted by the data feed (quotes and/or news).
-   Gateway server — the address at which the data feed accepts connections from the history server.
-   Source server — the address of the data source server.

To move to [detailed setup](/en/docs/mt5/platform/administration/admin_gateways/gateways_config), please click ![Settings](/en/docs/mt5/platform/img/configure_button.png "Settings")next to the data feed name.

## Databases

Gateway statistics is shown in this block:

-   Price ticks — the number of price changes received from the data source.
-   Price books — the number of Market Depth changes received from the data feed.
-   News — the number of news items received from the data feed.
-   Traffic — incoming and outgoing data feed traffic.

[Configuration of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_setup)

[Journal of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed)