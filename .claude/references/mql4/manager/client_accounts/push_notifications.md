# Sending Push Notifications

> Source: https://support.metaquotes.net/en/docs/mt4/manager/client_accounts/push_notifications

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
            -   [Adding a New Account](/en/docs/mt4/manager/client_accounts/ug_new_accounts)
            -   [Accounts](/en/docs/mt4/manager/client_accounts/ug_accounts)
            -   [Online](/en/docs/mt4/manager/client_accounts/ug_online)
            -   [Orders](/en/docs/mt4/manager/client_accounts/ug_orders)
            -   [Sending Notifications](/en/docs/mt4/manager/client_accounts/push_notifications)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Client Accounts](/en/docs/mt4/manager/client_accounts)Sending Notifications

# Sending Push Notifications

Push notifications are personal messages sent over the Internet. They do not depend on the phone number or mobile network operator. Messages are delivered instantly; no need to run any applications on the receiver's device.

Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 4 Mobile for [iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=ru&utm_campaign=download&utm_source=metatrader4.help "iPhone") или [Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=ru&utm_campaign=download&utm_source=metatrader4.help "Android").

## How to Send Push Notifications

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The "Push Notifications" permission should be enabled for a manager via MetaTrader 4 Administrator.</span></p></td></tr></tbody></table>

To send a notification, select "Notification" in the context menu of an account in the list. A similar command is available in the account edit dialog. Type the comma separated list of logins or MetaQuotes IDs and the message text. Ranges of logins can also be specified, e.g. 1000-2000.

![Sending push notifications](/en/docs/mt4/manager/img/push.png "Sending push notifications")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">MetaQuotes ID must be specified in the settings of appropriate accounts in order to send messages by specifying logins.</span></li><li class="p_tableatten"><span class="f_tableatten">The maximum message length is 255 characters.</span></li></ul></td></tr></tbody></table>

The send mode affects the automatic signature in push notifications:

-   If you send messages specifying logins, the signature will contain the name of the Owner company from the settings of the group, to which the accounts belong. Use this type for White Labels to add the correct company name in the signature.
-   If MetaQuotes IDs are used, the company name from the Server License will be specified in the signature.

Clients will immediately receive the sent notifications on their mobile devices. Push notifications received from a broker appear in the special category of the Messages section in the mobile trading platform:

![A push notification received in a mobile device](/en/docs/mt4/manager/img/push_receive.png "A push notification received in a mobile device")

[Orders](/en/docs/mt4/manager/client_accounts/ug_orders)

[Mail, News and Support](/en/docs/mt4/manager/news_mail)