# Controlling Subscriptions

> Source: https://support.metaquotes.net/en/docs/mt5/manager/subscriptions_control

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
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
            -   [Controlling Subscriptions](/en/docs/mt5/manager/subscriptions_control)
            -   [Subscription Types](/en/docs/mt5/manager/subscription_types)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Subscriptions](/en/docs/mt5/manager/subscriptions)Controlling Subscriptions

# Controlling Subscriptions

Service usage can be monitored using the Active and History sections. The sections feature active subscriptions and events concerning all subscriptions, respectively.

![Use the Active and History sections to control subscriptions](/en/docs/mt5/manager/img/subscriptions_active.png "Use the Active and History sections to control subscriptions")

Request subscriptions from the server to view them:

-   By trader group — select a group from the list or specify the group name manually.
-   By login — specify one or several accounts separated by commas.

## Active Subscriptions [#](subscriptions_control#active)

The following information is available for each active subscription:

-   ID — the internal identifier of the subscription configuration.
-   Login — subscriber's account number.
-   Subscription — [subscription name](/en/docs/mt5/manager/subscriptions_control#list).
-   Status — current subscription status:

-   Active — the subscription is active and the trader is receiving the service.
-   Suspended — the subscription has been suspended. This status is activated if the [subscription renewal fee](/en/docs/mt5/manager/subscriptions#payments) cannot be payed from a trading account.
-   Canceled — the subscription has been canceled.
-   Subscription time — the date and time when the subscription was activated.
-   Renewal time — the latest renewal date and time.
-   Expiration time — subscription expiration date and time.

Using the context menu, you can also quickly jump to viewing the subscribed [account](/en/docs/mt5/manager/account_overview) and the [service description](/en/docs/mt5/manager/subscriptions_control#list).

## Subscriptions History [#](subscriptions_control#history)

All actions related to subscriptions can be viewed under the "History" tab:

-   ID — the internal identifier of the subscription configuration.
-   Login — subscriber's account number.
-   Subscription — [subscription name](/en/docs/mt5/manager/subscriptions_control#list).
-   Record Id — the unique identifier of the subscription action.
-   Action— action type:

-   Subscription — subscribing to a service.
-   Renewal — renewal of an existing subscription.
-   Suspension — subscription suspension if the relevant [renewal fee](/en/docs/mt5/manager/subscriptions#payments) cannot be paid from the user's account.
-   Cancellation — subscription cancellation by the user.
-   Deletion — subscription deletion by the system, for example when the appropriate configuration is deleted.
-   Amount — subscription cost.
-   Transaction ID — identifier of the [transaction](/en/docs/mt5/manager/edit_trades#deal) through which the [subscription payment](/en/docs/mt5/manager/subscriptions#payments) was charged.

To adjust the amount of information displayed, use the context menu. From this menu, you can also quickly navigate to view the [trading account](/en/docs/mt5/manager/account_overview) associated with the subscription and the [subscribed service details](/en/docs/mt5/manager/subscriptions_control#list).

## Trader Subscriptions [#](subscriptions_control#user_subscriptions)

To view subscription details for a specific trader, open their [account](/en/docs/mt5/manager/accounts) and go to the Subscriptions tab. From here, you can also add or remove subscriptions:

![Each account contains information about subscriptions](/en/docs/mt5/manager/img/subscriptions_account.png "Each account contains information about subscriptions")

When adding a paid subscription, the system will notify the user that the payment for the subscription will be deducted from the trading account.

When canceling a subscription, the user will no longer be able to access the service. However, the record will not be deleted. It will remain in the subscription [history](/en/docs/mt5/manager/subscriptions_control#history) with the appropriate status.

To view [service details](/en/docs/mt5/manager/subscriptions_control#list), simply double-click on the subscription entry.

## Access to subscriptions by country and group [#](subscriptions_control#country_group)

Trader access to subscriptions can be restricted on the server side by group and country lists. A trader's country is determined based on the corresponding field in their [account](/en/docs/mt5/manager/account_personal). Please note:

-   When opening a demo account from the client terminal, the country is detected automatically.
-   When opening a preliminary account, the country is also detected automatically, but the client may manually select a different country in the registration form.
-   When creating a real account, you [specify the country manually](/en/docs/mt5/manager/account_create).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Country and group restrictions also apply to subscription purchases made via Manager terminals or the API. If a service is not available to a trader, they cannot subscribe to it by any means.</span></p></td></tr></tbody></table>

## Service List [#](subscriptions_control#list)

All available services are listed under Subscriptions \\ Settings. Here you can view detailed descriptions and pricing. The same information is displayed in client terminals for traders.

![List of available services](/en/docs/mt5/manager/img/subscriptions_list.png "List of available services")

For adding or modifying subscription settings, please contact the platform administrator.

[Subscriptions](/en/docs/mt5/manager/subscriptions)

[Subscription Types](/en/docs/mt5/manager/subscription_types)