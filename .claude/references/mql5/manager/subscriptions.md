# Subscriptions for Additional Trader Services

> Source: https://support.metaquotes.net/en/docs/mt5/manager/subscriptions

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Subscriptions

# Subscriptions for Additional Trader Services

With the "Subscriptions" service, brokers can offer additional paid services to traders directly through client terminals. For example, you can offer premium market data from reputable providers, offer personal manager services to help traders master trading fundamentals, deliver one-off services such as position transferring or currency conversion, and much more.

## Service advantages

-   Ready-to-use [product gallery](/en/docs/mt5/manager/subscriptions_control#list). All your traders instantly see available services in their terminals. You simply configure products via the administrator terminal, and they appear directly in client terminals. Traders stay focused on their workspace, and you avoid the hassle of driving traffic to your website.
-   Seamless [payments](/en/docs/mt5/manager/subscriptions#payments) from trading accounts. Traders don't need to enter card details or go through additional steps — services are purchased directly from their account balance. The easier it is to buy, the higher the likelihood of purchase.
-   Automated delivery of market data and news. The trader starts receiving the data immediately after purchasing a subscription. Once you set up the subscriptions, you do not need to perform any additional manual actions. Learn more in the article "[Market data subscriptions in MetaTrader 5](https://support.metaquotes.net/en/articles/1014)". You can also see a real-life example in "[Subscribe to real-time Nasdaq data](https://www.metatrader5.com/en/news/2365)".
-   Unified subscription database. Subscription details are linked to trading accounts within the platform. You can easily [review purchased services](/en/docs/mt5/manager/subscriptions_control#user_subscriptions) and generate reports.

Set up subscriptions and offer more services to your traders.

![Subscriptions for Additional Trader Services](/en/docs/mt5/manager/img/subscriptions.png "Subscriptions for Additional Trader Services")

## Subscription Payments [#](subscriptions#payments)

Subscription fees are paid directly from the trading account balance. Traders will not need to visit other websites, as payments will be made automatically within the platform.

Payments are executed as [balance transactions of "charge" type](/en/docs/mt5/manager/edit_trades#action). The deal comment will specify "Subscription 'Subscription name'".

To start receiving data, the trader purchases a subscription in the terminal:

-   At this moment, the appropriate amount is debited from the user's trading account balance (for paid subscriptions).
-   An appropriate subscription record is created, indicating the subscription expiration date.
-   If [automated renewal](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_permission#autorenew) is enabled for a subscription, an attempt to deduct the appropriate amount from the account will be performed upon expiration. If the attempt is successful, the subscription will remain active.
-   If the required amount is not available on the account, the suspended status is set for the subscription. A repeated payment attempt will be made an hour later. Repeated attempts are made within a day. If a payment cannot be made during this time, the subscription is canceled.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Since the payment is made from an account balance, subscriptions are only available for real and preliminary accounts.</span></p></td></tr></tbody></table>

## Setting up Subscriptions [#](subscriptions#setup)

Services are configured through the [Administrator terminal](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions). The manager terminal provides full subscription oversight:

-   View [active subscription](/en/docs/mt5/manager/subscriptions_control#active) and [history](/en/docs/mt5/manager/subscriptions_control#history)
-   [Add or remove subscriptions](/en/docs/mt5/manager/subscriptions_control#user_subscriptions) linked to trading accounts
-   View the list of available services

[Conditions](/en/docs/mt5/manager/ultency_routing/ultency_routing_conditions)

[Controlling Subscriptions](/en/docs/mt5/manager/subscriptions_control)