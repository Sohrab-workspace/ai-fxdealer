# Sending Push Notifications and SMS

> Source: https://support.metaquotes.net/en/docs/mt5/manager/push_notifications

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

# Sending Push Notifications and SMS

The MetaTrader 5 platform provides fast and efficient tools for notifying traders of important server operation news or real account opening offers. You can send push notifications or SMS to mobile devices straight from the Manager terminal.

## How to send push notifications

Push notifications are personal messages sent over the Internet. They do not depend on a phone number or a mobile network operator. Messages are delivered instantly: there is no need to run any applications on the receiver's device.

Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 5 Mobile for [iPhone](https://download.mql5.com/cdn/mobile/mt5/ios?hl=en&utm_campaign=download&utm_source=metatrader5.help "iPhone") or [Android](https://download.mql5.com/cdn/mobile/mt5/android?hl=en&utm_campaign=download&utm_source=metatrader5.help "Android").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Push Notifications permission should be enabled for a manager via MetaTrader 5 Administrator.</span></p></td></tr></tbody></table>

To send a notification, select Notification in the context menu of an account in the list. A similar command is available in the account edit dialog. Type the comma separated list of logins or MetaQuotes IDs and a message text. Ranges of logins can also be specified, e.g. 1000-2000.

![How to send push notifications](/en/docs/mt5/manager/img/push.png "How to send push notifications")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">MetaQuotes ID should be specified in the settings of appropriate accounts in order to send messages by specifying logins.</span></li><li class="p_tableatten"><span class="f_tableatten">The maximum message length is 255 characters.</span></li></ul></td></tr></tbody></table>

The sending mode affects the automatic signature in push notifications:

-   If you send messages specifying logins, the signature will contain the name of the Owner company from the settings of the group the accounts belong to. Use this type for White Labels to add a correct company name in the signature.
-   If MetaQuotes IDs are used, a company name from the Server License is specified in the signature.

Clients will immediately receive sent notifications on their mobile devices. Broker's push notifications appear in the special category of the Messages section in the mobile trading platform:

![The push notification received in the mobile device](/en/docs/mt5/manager/img/push_receive.png "The push notification received in the mobile device")

## How to send SMS [#](push_notifications#sms)

SMS messages are sent similarly to Push notifications. Click "Push-notification / SMS" in the context menu of the account, then set logins and enter the text. The message will be sent to the phone number indicated in [account personal data](/en/docs/mt5/manager/account_personal).

Some SMS providers support the specification of the message sender name. In this case, the received will see the company name instead of the phone number. Contact your platform administrator to find out whether this feature is supported by your provider. If it is, fill in the appropriate field when sending an SMS.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The SMS sending option requires a properly configured list of providers available on the trade server. If the function is not available, please contact your platform administrator.</span></p></td></tr></tbody></table>