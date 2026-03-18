# Communication with clients: Push notifications, SMS and emails

> Source: https://support.metaquotes.net/en/docs/mt5/manager/communication

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
            -   [Clients](/en/docs/mt5/manager/clients)
            -   [Online Accounts](/en/docs/mt5/manager/online_accounts)
            -   [Creation of Accounts](/en/docs/mt5/manager/account_create)
            -   [Importing Accounts](/en/docs/mt5/manager/account_import)
            -   [Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)
            -   [Push Notifications, SMS and Mail](/en/docs/mt5/manager/communication)
            -   [Account Overview](/en/docs/mt5/manager/account_overview)
            -   [Exposure](/en/docs/mt5/manager/account_exposure)
            -   [Personal Data](/en/docs/mt5/manager/account_personal)
            -   [Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)
            -   [Balance Operations](/en/docs/mt5/manager/account_balance)
            -   [Trading Operations](/en/docs/mt5/manager/account_trading)
            -   [Account History](/en/docs/mt5/manager/account_history)
            -   [Security and Certificates](/en/docs/mt5/manager/account_security)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Push Notifications, SMS and Mail

# Communication with clients: Push notifications, SMS and emails

The MetaTrader 5 platform provides fast and efficient tools for notifying traders about important server operation news or real account opening offers. Straight from the Manager terminal, you can send messages to mobile devices, as well as emails and internal mail messages.

## How to send push notifications

Push notifications are personal messages sent over the Internet. They do not depend on a phone number or a mobile network operator. Messages are delivered instantly: there is no need to run any applications on the receiver's device.

Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 5 Mobile for [iPhone](https://download.terminal.free/cdn/mobile/mt5/ios?hl=en&utm_campaign=download&utm_source=metatrader5.help "iPhone") or [Android](https://download.terminal.free/cdn/mobile/mt5/android?hl=en&utm_campaign=download&utm_source=metatrader5.help "Android").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Push Notifications permission should be enabled for a manager via MetaTrader 5 Administrator.</span></p></td></tr></tbody></table>

To send a notification, select Notification in the context menu of an account in the list. A similar command is available in the account edit dialog. Type the comma separated list of logins or MetaQuotes IDs and a message text. Ranges of logins can also be specified, e.g. 1000-2000.

![How to send push notifications](/en/docs/mt5/manager/img/push.png "How to send push notifications")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">MetaQuotes ID should be specified in the settings of appropriate accounts in order to send messages by specifying logins.</span></li><li class="p_tableatten"><span class="f_tableatten">The maximum message length is 1024 characters.</span></li></ul></td></tr></tbody></table>

The sending mode affects the automatic signature in push notifications:

-   If you send messages specifying logins, the signature will contain the name of the Owner company from the settings of the group the accounts belong to. Use this type for White Labels to add a correct company name in the signature.
-   If MetaQuotes IDs are used, a company name from the Server License is specified in the signature.

Clients will immediately receive sent notifications on their mobile devices. Broker's push notifications appear in the special category of the Messages section in the mobile trading platform:

![The push notification received in the mobile device](/en/docs/mt5/manager/img/push_receive.png "The push notification received in the mobile device")

## How to send SMS [#](communication#sms)

SMS messages are sent similarly to Push notifications. Click "Push-notification / SMS" in the context menu of the account, then set logins and enter the text. The message will be sent to the phone number indicated in [account personal data](/en/docs/mt5/manager/account_personal).

Some SMS providers support the specification of the message sender name. In this case, the received will see the company name instead of the phone number. Contact your platform administrator to find out whether this feature is supported by your provider. If it is, fill in the appropriate field when sending an SMS.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The SMS sending option requires a properly configured list of providers available on the trade server. If the function is not available, please contact your platform administrator.</span></p></td></tr></tbody></table>

## How to send internal mail messages and emails [#](communication#mail)

The MetaTrader 5 trading platform features an internal email system which enables communications with clients and between employees. Using emails, you can effectively send important information about your services and company events to traders. The email system is integrated directly into trading terminals. When a message is received in the terminal, a sound notification is played, and thus the trader will not miss important information. In addition, the built-in email system allows you to reach potential clients for whom you do not have reliable contact information, such as phone number or email addresses. If a trader has opened a demo account and connected to your server, your managers can contact the trader offering a real accounts.

To send an email, select "Internal mail/Email" in the account menu. For bulk mailing, you can first select all the required account in the list. Their logins will be included in the "To" field.

![Sending an Email](/en/docs/mt5/manager/img/mail_send.png "Sending an Email")

When using Email instead of the internal mail, a more convenient option may be to send emails to a list of clients rather than accounts. Clients often have multiple accounts that use the same email address. Because of this, when sending emails to a list of accounts, the client may receive several identical messages. To avoid this, send emails from the [Clients](/en/docs/mt5/manager/clients) section. Select the desired entries in the list and click "Internal mail/Email" in the menu. The mailing list will only include unique email addresses from all the trading accounts linked to the selected clients.

Fill in the following fields in the email:

-   To — account number of the email recipient. The terminal allows the [sending of emails to multiple clients simultaneously](/en/docs/mt5/manager/communication#mass_mail).
-   Subject — email subject.
-   Template — any email can be saved as a template using the context menu. For example, you can save a typical maintenance works email as a template. To get a ready-made email afterwards, simply select the template in this field.
-   Internal mail — select this option to send a message using the internal mail system.
-   Email — use this option to send an email. The address specified in [account personal data](/en/docs/mt5/manager/account_personal) will be used. Please note:

-   A mail server must be configured in the platform to enable email sending. If the feature is not available, please contact your platform administrator.
-   Messages sent by email are not displayed under the "Toolbox \\ Mail" section. To check the sending, request the [trade server journal](/en/docs/mt5/manager/server_journal) using the 'email' keyword. If an email has been sent successfully, the recipient address and the configuration name of the mail server through which the email has been sent, are shown in the log: email to someaddress@mail.net sent \[MailServer\].

By selecting ![Attach file](/en/docs/mt5/manager/img/attach_button.png "Attach file") on the toolbar, you can attach a file to the email. Please mind the following attachment restrictions:

-   The size of one file should not exceed 8 MB
-   The total size of attachments should not exceed 16 MB
-   Up to 5 files can be attached

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_Normal"><span class="f_fortable">To enable the mailing feature, you should specify the mailbox name in the manager's account on the trade server. Also, the manager should have sufficient permissions. Contact the platform administrator to configure the account.</span></p></td></tr></tbody></table>

Below is the window for working with an email text. Commands for creating lists and inserting images, links and tables, etc. are available in the editor. To view or edit the source HTML code of the news, click![Switch to HTML mode](/en/docs/mt5/manager/img/html_visual_button.png "Switch to HTML mode")on the toolbar.

The context menu of the text editing window contains standard commands for working with the text: Copy, Cut, Paste, Insert Hyperlink, Insert Table and Insert Image. From the context menu, you can also work with [templates](/en/docs/mt5/manager/communication#mail_template) of mails and [macros](/en/docs/mt5/manager/communication#macro).

### Bulk mailing [#](communication#mass_mail)

The manager terminal supports emailing to user groups. The list of users is defined in the message field "To".

-   Multiple Logins — specify several usernames separated by a comma. For example, 1000, 1001, 1002.
-   Range of Logins — send emails to a range of logins, specify the range through a hyphen. For example, 1000-9000.
-   Group of Accounts — to send emails to a certain group, specify the following construction: "group:group name". For example, to send mails to group demoforex, in the To field specify group:demoforex. You can also specify several groups separating them by commas.
-   Country of Residence — emails can be sent to account holders living in a certain country. To do this, specify the following construction: "country:country name" in the To field. For example, to send mails to all clients who live in Germany, specify country:Germany. You can also specify several countries separating them by commas.
-   City of Residence — to send mails to clients in certain cities, specify "city:city name". You can specify several cities separated by commas.

In the To field, you can specify several delivery parameters separated by a semi colon (;). In this case the mail will be sent to all the clients who meet at least one of the specified parameters. For example, if you specify "group:demoforex, managers; city:Hamburg; 1000-2000", emails will be sent to all clients from 'demoforex' and 'managers' groups, all clients who live in Hamburg and to all of the clients from the accounts range from 1000 to 2000 inclusive.

When specifying the mailing parameters, you can use the negation sign "!". It allows the excluding of clients from the mailing list by a certain parameter. For example, if you specify "group:!managers", then messages will be sent to all the users except the ones who belong to the managers group.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When sending an email, the system checks whether there are any clients with the specified delivery parameters. If there are no such clients, the email will not be sent. In this case a corresponding message will appear in the <a href="/en/docs/mt5/manager/toolbox#journal" class="topiclink">journal</a>.</span></p></td></tr></tbody></table>

### Templates [#](communication#mail_template)

Use templates for a more convenient operation. They are available as HTML files which contain macros and enable email customization to address each recipient.

Use the email creation window context menu to work with templates.

All email templates are stored in the /templates/mail folder of the Manager terminal.

### Macros [#](communication#macro)

Using the "Macros" submenu of the context menu of the email creation window, you can insert macros in the text. They allow substituting different data depending on the email recipient.

-   Login (#LOGIN#) — the email/messenger recipient's Account number.
-   Name (#USERNAME#) — the first name and the last name of the recipient.
-   Currency (#USER\_CURRENCY#) — the recipient's deposit currency.
-   Balance (#USER\_BALANCE#) — the recipient's balance.
-   Credit (#USER\_CREDIT#) — the credit amount on the recipient's account.
-   Equity (#USER\_EQUITY#) — the equity amount on the recipient's account.
-   Leverage (#USER\_LEVERAGE#) — account leverage.
-   Margin (#USER\_MARGIN#) —  the amount of funds reserved on the recipient's account.
-   Free margin (#USER\_MARGIN\_FREE#) — the free margin amount on the recipient's account.
-   Margin level (#USER\_MARGIN\_LEVEL#) — the margin level on the recipient's account.

These macros substitute email sending time in the message text:

-   Trading time — internal platform time.
-   Local time — time used in the computer on which the platform is installed.
-   UTC time — [UTC](https://ru.wikipedia.org/wiki/%D0%92%D1%81%D0%B5%D0%BC%D0%B8%D1%80%D0%BD%D0%BE%D0%B5_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5_%D0%B2%D1%80%D0%B5%D0%BC%D1%8F) time.

### Email history [#](communication#mailbox)

The history of emails sent over the internal system is displayed in the Mailbox section.

![Internal mail system](/en/docs/mt5/manager/img/mail.png "Internal mail system")

Unread messages are marked with icon ![Unread message](/en/docs/mt5/manager/img/unread_mail_icon.png "Unread message"), read ones — ![Read Mail](/en/docs/mt5/manager/img/read_mail_icon.png "Read Mail"). Outgoing emails are marked with icon ![Outgoing message](/en/docs/mt5/manager/img/outgoing_mail_icon.png "Outgoing message"). When the function of response to an email is used, messages are joint into threads, which makes it easy to navigate in conversations with clients. Email threads are marked with icon ![Email Chain](/en/docs/mt5/manager/img/mail_branch_icon.png "Email Chain"). Click on it to expand the chain.

To read an email, click on its title in the list. In the email view window, there are several commands available on the toolbar. They allow you to reply to an email, save it as HTML files (in Unicode format), as well as print it. If files are attached to an email, you can open them by selecting "![Attachment](/en/docs/mt5/manager/img/attachment_icon.png "Attachment") Attachment".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Emails are stored on the trade server. If an email is deleted in the terminal interface, it will not be re-downloaded. However, if you delete the mail base of the terminal (the "/bases/server_name/mail/mail-account_number.dat" file) or connect using another terminal, all the mails for the last 30 days are downloaded again.</span></li><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/manager/settings#server" class="topiclink">Configure the directory</a> email attachments to be saved to. When you open an attached file, the terminal checks its extension and the correspondence of file contents to this extension. If the file type is allowed and its contents is checked, the terminal opens the file and saves it to the specified directory. Otherwise, a warning is displayed, notifying that the file may harm the computer, and it is not saved. The following file types are allowed: PNG, JPG/JPEG, BMP, ZIP, 7Z, GIF, DOC, XLS, DOCX, XSLX, ODT, RTF, CSV, TXT and LOG.</span><br><span class="f_tableatten">If a file with the same name and a different content exists in the directory, the manager's login and email arrival date/time up to a second will be added to the saved file name: [login]-[file name]-[date and time].[extension]. For example, the log file 20170501.log will be saved as 1001-20170501-20170502-170038.log.</span><br><span class="f_tableatten">By default, files are saved to C:\Users\[Windows username]\Downloads\MetaTrader.</span></li></ul></td></tr></tbody></table>

### Viewing attached log files [#](communication#journal_viewer)

If a log file (file with \*.log extension) is attached to a client's email, it can be viewed using a special viewer. To do this, just click on the file name in the email header.

![Viewing the log](/en/docs/mt5/manager/img/journal_viewer.png "Viewing the log")

A search bar (search is performed by exact words, case sensitive) and the filter of entries (Full, No connection, Errors only) are available at the top of the window. Enter a word to search for and click Request.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If a client has manually changed any of the journal entries, all records starting from it will be highlighted in red. When trying to save such a file, you will see a warning of what line of the file has been changed.</span></p></td></tr></tbody></table>

[Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)

[Account Overview](/en/docs/mt5/manager/account_overview)