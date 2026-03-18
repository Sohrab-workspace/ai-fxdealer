# Permissions

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Subscriptions](/en/docs/mt5/platform/administration/subscriptions)Permissons

# Permissions

Specify here subscription access permissions: to which client groups and countries the subscription will be available.

![Set up subscription access permissions](/en/docs/mt5/platform/img/subscriptions_permissions.png "Set up subscription access permissions")

Specify the following settings:

-   Auto renew subscription — this option enables automated subscription renewal upon expiration. During renewal, the subscription amount will be automatically debited from the client's trading account.
-   Agreement URL — you can specify here a link to additional Agreement/Rules to be accepted by the trader. An agreement link will be displayed in the subscription confirmation dialog in client terminals.
-   Permissions — select the subscription actions available to traders:

-   Full — the client can subscribe and unsubscribe from the service.
-   Unsubscribe — the client can only unsubscribe from the service. The subscription can only be created through the Manager terminal or the API. If the user is not subscribed to a service with this permission, the appropriate subscription will not be shown to the trader in the client terminal.
-   View — the client can view the service in the terminal, but subscribe and unsubscribe options are only available through the Manager terminal or the API. If the user is not subscribed to a service with this permission, the appropriate subscription will not be shown to the trader in the client terminal.
-   Hidden — clients cannot view the service in the terminal, even if they are subscribed to this services (the subscription fee is charged from the trading account, as for regular subscriptions). The subscription can only be created through the Manager terminal or the API.

## Access to subscriptions by country and group [#](subscriptions_permission#country_group)

You can create subscriptions for traders from certain countries. To limit access, specify the list of countries in the appropriate field. To select/deselect all countries in the list, right-click on the list.

Note:

-   When opening a demo account from the client terminal, the client's country is determined automatically.
-   When opening a preliminary account, the country is also determined automatically, but the client can specify another country in the registration form.
-   When creating a real account, you [specify the country manually](/en/docs/mt5/platform/administration/admin_accounts/account_edit#personal).

Similarly, you can limit access, allowing subscriptions only for clients from individual [groups](/en/docs/mt5/platform/administration/admin_groups).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Restrictions by countries and groups also affect the ability to subscribe through Manager terminals or the API. If the service is not available for the trader, there is no way to subscribe to it.</span></p></td></tr></tbody></table>

[Description](/en/docs/mt5/platform/administration/subscriptions/subscriptions_description)

[Symbols](/en/docs/mt5/platform/administration/subscriptions/subscriptions_symbol)