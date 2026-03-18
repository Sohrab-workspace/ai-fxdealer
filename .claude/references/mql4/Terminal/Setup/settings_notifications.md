# Notifications

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/settings_notifications

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
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
            -   [Server](/en/docs/mt4/terminal/setup/setup_server)
            -   [Charts](/en/docs/mt4/terminal/setup/setup_charts)
            -   [Objects](/en/docs/mt4/terminal/setup/setup_objects)
            -   [Trade](/en/docs/mt4/terminal/setup/setup_trade)
            -   [Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts)
            -   [Notifications](/en/docs/mt4/terminal/setup/settings_notifications)
            -   [Email](/en/docs/mt4/terminal/setup/setup_email)
            -   [FTP](/en/docs/mt4/terminal/setup/setup_publisher)
            -   [Events](/en/docs/mt4/terminal/setup/setup_events)
            -   [Community](/en/docs/mt4/terminal/setup/settings_mql5community)
            -   [Signals](/en/docs/mt4/terminal/setup/settings_signals)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Notifications

# Notifications

The client terminal supports sending of notifications about various events to mobile devices powered by [iOS](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader4.com "iOS") and [Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader4.com "Android") using push messages. With this feature, a trader can track all the updates.

Push notifications are short messages of up to 255 characters. Such notification are delivered immediately and are never lost.

There are two ways to send push notifications from the client terminal:

## Through an MQL4 application

The MQL4 language provides a special SendNotification function which allows MQL4 programs to send push notifications to a MetaQuotes ID specified in the terminal settings.

## Through the signals function

The client terminal allows you to create signals for alerting you of events in the market. This feature is available in the [Signals](/en/docs/mt4/terminal/overview/terminal/terminal_alerts) tab of the Terminal window. One of the event notification types is push notifications.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Push notifications can also be used to obtain information about the updates on the MQL5.community site. To do this, specify your MetaQuotes ID in the user profile in "Contacts" tab.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">There is a limitation on the number of messages that can be sent: no more than 1 message per 0,5 second and no more that 10 messages per minute.</span></li></ul></td></tr></tbody></table>

![Notifications](/en/docs/mt4/terminal/img/options_notifications.png "Notifications")

The notifications setup window includes the following options:

-   Enable Push notifications — to allow the client terminal to send notifications, enable this option.

-   Notify of trade operations — if this option is enabled, the client terminal will automatically send notifications about successful trade operations to a specified MetaQuotes ID. The platform will also send notifications about any balance operations performed on the account as well as about the Margin Call state (in this case notifications are sent periodically, as long as the account is in the Margin Call state). Notifications about unsuccessful operations (for example, an order is rejected due to incorrect parameters) are not sent.

After setting up the options, enter one or more MetaQuotes IDs, separated by commas. You can specify up to 4 MetaQuotes IDs; the notifications will be sent to all of the devices simultaneously.

To find your MetaQuotes ID, open your mobile terminal and go to Settings -> Messages. This page in the terminal for iPhone looks as follows:

![MetaQuotes ID](/en/docs/mt4/terminal/img/mq_id.png "MetaQuotes ID")

To test the function notification sending, click Test. If your notification is successfully sent, you see an appropriate message, and the notification will arrive on your mobile device.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To install the mobile version of the terminal, use the following links:</span></p><ul><li class="p_tableatten"><span class="f_tableatten"><a href="https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&amp;utm_campaign=metaquotes.download&amp;utm_source=www.metatrader4.com" target="_blank" class="weblink" title="Mobile Terminal for iPhone">Mobile Terminal for iPhone</a></span></li><li class="p_tableatten"><span class="f_tableatten"><a href="https://download.terminal.free/cdn/mobile/mt4/android?hl=en&amp;utm_campaign=metaquotes.download&amp;utm_source=www.metatrader4.com" target="_blank" class="weblink" title="Mobile Terminal for Android">Mobile Terminal for Android</a></span></li></ul></td></tr></tbody></table>

[Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts)

[Email](/en/docs/mt4/terminal/setup/setup_email)