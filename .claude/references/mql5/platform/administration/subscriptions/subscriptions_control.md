# Subscriptions Control

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_control

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Subscriptions](/en/docs/mt5/platform/administration/subscriptions)Controlling Subscriptions

# Subscriptions Control

The service usage can be monitored using the Active and History sections. The sections feature active subscriptions and events concerning all subscriptions, respectively.

![Use the Active and History sections to control subscriptions](/en/docs/mt5/platform/img/subscriptions_active.png "Use the Active and History sections to control subscriptions")

Request subscriptions from the server to view them:

-   By trader group — select a group from the list or specify the group name manually.
-   By login — specify one or several accounts separated by commas.

## Active Subscriptions [#](subscriptions_control#active)

The following information is available for each active subscription:

-   ID — the internal identifier of the subscription configuration.
-   Login — subscriber's account number.
-   Subscription name — [the name of the subscription](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common).
-   Status — current subscription status:

-   Active — the subscription is active and the trader is receiving the service.
-   Suspended — the subscription has been suspended. This status is activated if the [subscription renewal fee](/en/docs/mt5/platform/administration/subscriptions#payments) cannot be payed from a trading account.
-   Canceled — the subscription has been canceled.
-   Subscription time — the date and time when the subscription was activated.
-   Renewal time — the latest renewal date and time.
-   Expiration time — subscription expiration date and time.

Using the context menu, you can quickly jump to viewing the subscribed [account](/en/docs/mt5/platform/administration/admin_accounts) and the [subscription configuration](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common).

Here you can edit the parameters of an active subscription:

-   Service and subscription status. If you change the subscription state to "Canceled", this subscription will not be available in the list during the next request of active subscriptions.
-   Free period. This is an indication that the user has received the subscription as a free trial. If you disable this option, the user will be able to use a free period once again at the next subscription.
-   Subscription, next renewal and expiration dates. When the subscription period is changed, no additional fees are debited from the account.

![Changing the parameters of an active subscription](/en/docs/mt5/platform/img/subscriptions_active_edit.png "Changing the parameters of an active subscription")

### Delete and unsubscribe [#](subscriptions_control#delete_unsubscribe)

When a subscription is canceled or deleted, the user will no longer be able to use the service. However, these actions have fundamental differences:

-   When a subscription is canceled, the relevant information remains in the database, and the [history](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control#history) will contain a separate record about subscription cancellation.
-   When deleted, the whole subscription record is removed from the database. If you delete a trial subscription record, the trader will be able to use the free period again, since there will be no record in the database that it has already been used.

Both actions can be performed using the context menu of the active subscriptions section.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Manager account needs appropriate <a href="/en/docs/mt5/platform/administration/admin_managers#subscriptions" class="topiclink">permissions</a>in order to access subscription editing options.</span></p></td></tr></tbody></table>

## Subscriptions History [#](subscriptions_control#history)

All actions related to subscriptions can be viewed under the "History" tab:

-   ID — the internal identifier of the subscription configuration.
-   Login — subscriber's account number.
-   Subscription name — [the name of the subscription](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common).
-   Record Id — the unique identifier of the subscription action.
-   Action— action type:

-   Subscription — subscribing to a service.
-   Renewal — renewal of an existing subscription.
-   Suspension — subscription suspension if the relevant [renewal fee](/en/docs/mt5/platform/administration/subscriptions#payments) cannot be paid from the user's account.
-   Cancellation — subscription cancellation by the user.
-   Deletion — subscription deletion by the system, for example when the appropriate configuration is deleted.
-   Amount — subscription cost.
-   Deal Id— the identifier of the [deal](/en/docs/mt5/platform/administration/admin_deals) by which the appropriate [subscription fee](/en/docs/mt5/platform/administration/subscriptions#payments) amount was charged from the account.

To adjust the amount of information displayed, use the context menu. Using the menu, you can also quickly jump to viewing the subscribed [account](/en/docs/mt5/platform/administration/admin_accounts) and the [subscription configuration](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common).

If you have [appropriate permissions](/en/docs/mt5/platform/administration/admin_managers#subscriptions), you can edit actions in history. To do this, double-click on the line.

The following parameters can be edited:

-   Service and type of action. Changes do not affect active trader subscriptions. If you change the action type from "Cancel" to "Subscription", the trader's subscription will not be restored.
-   The date of the action.
-   Subscription fee. The change does not affect the deal by which the subscription payment was conducted.

![Changing the parameters of a subscription action](/en/docs/mt5/platform/img/subscriptions_history_edit.png "Changing the parameters of a subscription action")

## Trader Subscriptions [#](subscriptions_control#user_subscriptions)

To view subscription data of a specific trader, open his or her [account](/en/docs/mt5/platform/administration/admin_accounts) and navigate to the "Subscriptions" tab.

To navigate to [general subscription settings](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common), double-click on the line.

From this section, you can add a new subscription or delete an existing one:

![Each account contains information about subscriptions](/en/docs/mt5/platform/img/subscriptions_account.png "Each account contains information about subscriptions")

When adding a paid subscription, the system will notify the user that the payment for the subscription will be debited from the trading account.

[News](/en/docs/mt5/platform/administration/subscriptions/subscriptions_news)

[Mailbox](/en/docs/mt5/platform/administration/mail)