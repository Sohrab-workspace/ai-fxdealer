# Subscriptions for Additional Trader Services

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions

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
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
                -   [Common](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common)
                -   [Description](/en/docs/mt5/platform/administration/subscriptions/subscriptions_description)
                -   [Permissons](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission)
                -   [Symbols](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol)
                -   [News](/en/docs/mt5/platform/administration/subscriptions/subscriptions_news)
                -   [Controlling Subscriptions](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Subscriptions

# Subscriptions for Additional Trader Services

With the "Subscriptions" service, you can offer additional paid services to traders directly in the client terminals. For example, you can sell subscriptions for high-quality market data from well-known providers, offer personal manager services to assist traders in understanding the basics of trading, deliver one-time services such as position transferring or currency conversion, and much more.

## Service Advantages

-   A ready-made showcase of products which can be viewed by all your traders. You [set up products](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common) via the Administrator terminal, and the subscriptions appear straight in client terminals. It means that you will not have to additionally attract traders to your site.
-   [Payment](/en/docs/mt5/platform/administration/subscriptions#payments) is performed directly from a trading account. Traders can easily pay for the product, as they do not have to think which payment methods to use. The easy procedure can increase the probability of a successful purchase.
-   Automated delivery of market data and news. The trader starts receiving the data immediately after purchasing a subscription. Once you set up the subscriptions, you do not need to perform any additional manual actions. For more details, please refer to the article "[Market data subscriptions in MetaTrader 5](https://support.metaquotes.net/en/articles/1014)".
-   Unified Database. Information on subscriptions is linked to trading accounts in the platform. You can easily [view all services purchased by the trader](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control#user_subscriptions) and generate a report.

Set up subscriptions and offer more services to your traders.

![Subscriptions in the Client Terminal](/en/docs/mt5/platform/img/subscriptions_terminal.png "Subscriptions in the Client Terminal")

## Setting up subscriptions [#](subscriptions#setup)

Go to the new Subscriptions service in the Administrator terminal, create a configuration and set the following:

-   Subscription [price and period](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common)
-   [Product description](/en/docs/mt5/platform/administration/subscriptions/subscriptions_description) for a showcase in client terminals
-   Subscription [access permissions](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission) for certain groups and countries
-   [Trading instruments](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol) for market data subscriptions
-   [News categories](/en/docs/mt5/platform/administration/subscriptions/subscriptions_news) for news subscriptions

The platform features a few ready-made examples, which can help you in understanding the service operation and setup principles.

Before setting up specific configurations, we recommend defining the service structure and creating appropriate categories. For example, "Market Data" and "Manager Services". Categories can be created using the context menu in the sections tree.

![Create a structure of services for convenient management](/en/docs/mt5/platform/img/subscriptions_structure.png "Create a structure of services for convenient management")

## Subscription Payments [#](subscriptions#payments)

Subscription fees are paid directly from the trading account balance. Traders will not need to visit other websites, as the payment can be made straight in the platform.

A payment is deducted from the account as [a balance operation of "charge" type](/en/docs/mt5/platform/administration/admin_deals#action). The deal comment will specify "Subscription 'Subscription name'".

To start receiving data, the trader purchases a subscription in the terminal:

-   At this moment, the appropriate amount is debited from the user's trading account balance (for paid subscriptions).
-   An appropriate subscription record is created, indicating the subscription expiry date.
-   If [automated renewal](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission#autorenew) is enabled for a subscription, an attempt to deduct the appropriate amount from the account will be performed upon expiration. If the attempt is successful, the subscription will remain active.
-   If the required amount is not available on the account, the suspended status is set for the subscription. A repeated payment attempt will be made an hour later. Repeated attempts are made within a day. If a payment cannot be made during this time, the subscription is canceled.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Since the payment can only be made from an account balance, subscriptions are only available for real and preliminary accounts.</span></p></td></tr></tbody></table>

[Synchronization Features](/en/docs/mt5/platform/administration/admin_synchronization/synchronization_features)

[Common](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common)