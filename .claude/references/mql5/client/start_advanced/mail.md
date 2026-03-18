# Mailbox

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/mail

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
            -   [User Interface](/en/docs/mt5/client/interface)
            -   [Open an Account](/en/docs/mt5/client/acc_open)
            -   [Connect to an Account](/en/docs/mt5/client/authorization)
            -   [Deposits and withdrawals](/en/docs/mt5/client/payments)
            -   [Platform Settings](/en/docs/mt5/client/settings)
            -   [For Advanced Users](/en/docs/mt5/client/start_advanced)
                -   [Platform Installation](/en/docs/mt5/client/start_advanced/installation)
                -   [Installation on Mac OS](/en/docs/mt5/client/start_advanced/install_mac)
                -   [Installation on Linux](/en/docs/mt5/client/start_advanced/install_linux)
                -   [Platform Start](/en/docs/mt5/client/start_advanced/start)
                -   [Extended Authentication](/en/docs/mt5/client/start_advanced/extended_authorization)
                -   [One Time Passwords - 2FA/TOTP](/en/docs/mt5/client/start_advanced/otp)
                -   [Files and Folders](/en/docs/mt5/client/start_advanced/structure)
                -   [Manage Trading Accounts](/en/docs/mt5/client/start_advanced/account_manage)
                -   [Mailbox](/en/docs/mt5/client/start_advanced/mail)
                -   [Security System](/en/docs/mt5/client/start_advanced/security)
                -   [Live Update](/en/docs/mt5/client/start_advanced/autoupdate)
                -   [Platform Logs](/en/docs/mt5/client/start_advanced/journal)
                -   [Task Manager](/en/docs/mt5/client/start_advanced/task_manager)
                -   [Hot Keys](/en/docs/mt5/client/start_advanced/hotkeys)
                -   [Uninstalling the Platform](/en/docs/mt5/client/start_advanced/deinstallation)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Mailbox

# Mailbox

The trading platform contains an internal mail system. It allows you to receive important information from your broker: information about open accounts, useful information about the platform features, upcoming events, etc.

All the emails are displayed in the Mailbox tab of the Toolbox window.

![Mail System](/en/docs/mt5/client/img/mail.png)

Email subject

Email sender's name

Email recipient's name

Email sending or receiving time

[Write an email](/en/docs/mt5/client/start_advanced/mail#create)

Unread messages are marked with icon ![Unread message](/en/docs/mt5/client/img/mail_unread_icon.png "Unread message"), read ones - ![Read message](/en/docs/mt5/client/img/mail_read_icon.png "Read message"). Outgoing emails are marked with icon ![Outgoing message](/en/docs/mt5/client/img/mail_outgoing_icon.png "Outgoing message"). When the function of response to an email is used, messages are joint into threads, which makes it easy to navigate in conversations with clients. Email threads are marked with icon ![Email Thread](/en/docs/mt5/client/img/mail_branch_icon.png "Email Thread"). To expand a thread, click on this icon.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Emails are stored on the trade server. When you delete an email from the platform interface, it will not be re-downloaded. However, if you delete the platform mail database (the file "/bases/server_name/mail/mail-account_number.dat") or connect from another platform, all the mails for the last 30 days will be downloaded again.</span></p></td></tr></tbody></table>

## Reading an Email [#](mail#view)

Double-click on an email to read it.

![To read an email, double-click on it in the list](/en/docs/mt5/client/img/mail_view.png "To read an email, double-click on it in the list")

The top of the email contains the following data: a client's account and name, date of email, its subject and attachments (if any).

The toolbar of this window contains the following commands:

-   ![Reply](/en/docs/mt5/client/img/mail_answer_icon.png "Reply") Reply — open email creation window with the field "To" filled in and a quote of a received email;
-   ![Save](/en/docs/mt5/client/img/save_icon.png "Save") Save — save the email on a computer as a HTML file or a text file in Unicode standard;
-   ![Print](/en/docs/mt5/client/img/print_icon.png "Print") Print — print the email;
-   ![Print preview](/en/docs/mt5/client/img/print_preview_icon.png "Print preview") Print Preview — open the preview window before printing the email;
-   ![Attachment](/en/docs/mt5/client/img/mail_attachment_icon.png "Attachment") Attachment — save files attached to the email. Another way to save an attachment is to click on its name in the appropriate field of the email header.

## Writing an Email [#](mail#create)

To create an email, select the appropriate command in the context menu, or use the hot key "Insert" on the Mailbox tab.

![Select the email recipient, add email subject and body](/en/docs/mt5/client/img/mail_create.png "Select the email recipient, add email subject and body")

Specify the following data in this window:

-   To — the account of a trade server administrators you want to send an email to;
-   Subject — subject of the email;
-   Attachments — files attached to the email. To attach a file click ![Add attachment](/en/docs/mt5/client/img/add_attachment_button.png "Add attachment"), and specify the desired file. To remove an attachment click ![Delete attachment](/en/docs/mt5/client/img/delete_attachment_button.png "Delete attachment"). If several files are attached to an email, they are deleted starting from the last one;
-   Below is the window for working with am email text. It contains three tabs: Edit, View and Source. In the Edit tab you can write an email text and use commands for working with it. You can view the final email in the View tab. The Source tab allows working with the source HTML code of an email.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note the following limitations on attachments:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">The size of one attached file cannot exceed 8MB;</span></li><li class="p_tableatten"><span class="f_tableatten">The total size of attached files cannot exceed 16MB;</span></li><li class="p_tableatten"><span class="f_tableatten">Up to 5 files can be attached.</span></li></ul></td></tr></tbody></table>

[Manage Trading Accounts](/en/docs/mt5/client/start_advanced/account_manage)

[Security System](/en/docs/mt5/client/start_advanced/security)