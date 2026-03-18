# Email

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/setup_email

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Email

# Email

In this tab, the electronic mailbox is set up. Later on, these settings will be used to send message by the [expert advisor](/en/docs/mt4/terminal/autotrading/experts) command or by a triggered [alert](/en/docs/mt4/terminal/overview/terminal/terminal_alerts).

![options_email](/en/docs/mt4/terminal/img/options_email.png)

To start setting up of email, the "Enable" must be enabled and the following fields must be filled out:

-   SMTP Server — address of the SMTP server and port used. This server will be utilized to send the message. The record must be made in the following format "\[server web address\] : \[port number\]". For example, "smtp.your\_email\_provider.com:25" where "smtp.your\_email\_provider.com" is the server web address, "25" is the port number.
-   SMTP Login — a login to be authorized on the trade server. Normally, it is an electronic mailbox. Example: your\_name@your\_email\_provider.com
-   SMTP Password — a password to be authorized (mailbox access password).
-   From — the email address, from which the message will be sent. In this field, there must be name and emailing address on the mail server, the SMTP of which will be utilized. The name usually coincides with the first part of the electronic address, but the name can be omitted. Example: your\_name, your\_name@your\_email\_provider.com
-   To — the email address, to which the messages will be sent. The "Your Name" part of the address can be omitted. Generally, in the "To" field, any really existing email can be specified. Example: any\_name, your\_name@your\_email\_provider.com

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Only one email address may be specified for either of fields "From" and "To". Several emails given with or without separators will not be accepted.</span></p></td></tr></tbody></table>

The "Test" sends a test message using the settings specified to test their workability. If it has been tested successfully, the "OK" button must be pressed to apply these settings. In case the test did not succeed, it is recommended to check all settings again, restart the terminal and resend the test message.

[Notifications](/en/docs/mt4/terminal/setup/settings_notifications)

[FTP](/en/docs/mt4/terminal/setup/setup_publisher)