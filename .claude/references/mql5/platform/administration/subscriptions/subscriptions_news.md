# News

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_news

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Subscriptions](/en/docs/mt5/platform/administration/subscriptions)News

# News

For news data services, set the news categories in this section.

## Preparatory Steps [#](subscriptions_news#prepare)

Before you start offering news subscriptions, you should configure news delivery via [data feeds](/en/docs/mt5/platform/administration/admin_feeds). The news categories specified in subscription settings must be available in the platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To start offering news, you will need to sign an agreement with appropriate agencies, as news constitute proprietary data.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The support website <a href="https://support.metaquotes.net/en/market/mt5/datafeeds" target="_blank" class="weblink">App Store</a> features a variety of solutions enabling receiving of news data from popular providers.</span></li></ul></td></tr></tbody></table>

## Setup [#](subscriptions_news#setup)

![If you are setting up a news delivery service, specify news categories](/en/docs/mt5/platform/img/subscriptions_news.png "If you are setting up a news delivery service, specify news categories")

In the settings, specify those news categories, which will be available by subscription.

-   Usually, news categories are provided by data feeds. News providers supplement news with the information about categories to which the news belong. The same applies to the news language.
-   A news category can be additionally specified in the [News Category](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) parameter of the data feed. This is a standard parameter supported by all data feeds. The parameter is applied as follows:

-   If a data source does not provide news categories, news items will be added to the category specified in this parameter (the category will be specified in the news).
-   If the data source provides a category, then the data feed will add the "News Category" parameter value before the original category name. The resulting category will look like "\[value from News Category\] \\ \[category from data source\]". The "\\" characters in a category name are interpreted as subcategory separators. Therefore, it means that all news items are added to the category specified in the parameter, within which original categories from the data source will be used.

## Access to news on the client terminal side [#](subscriptions_news#access)

Subscriptions limit access to news in the platform. A subscription is needed to access news if the following conditions are met:

-   There is a subscription with a [list of groups](/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission#country_group) containing the trader group.
-   There is a subscription, having the news category and language in the "News" section.

If there are no appropriate subscriptions in the platform, it is considered that the subscription is not required and the news will be delivered in a normal way, in accordance with the [parameters of the group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols) to which the account belongs.

[Symbols](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol)

[Controlling Subscriptions](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control)