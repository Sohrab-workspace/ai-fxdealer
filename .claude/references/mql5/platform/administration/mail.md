# Mailbox

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/mail

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Mailbox

# Mailbox

The MetaTrader 5 trading platform features an internal email system which enables communications with clients and between employees. Using emails, you can effectively send important information about your services and company events to traders. The email system is integrated directly into trading terminals. When a message is received in the terminal, a sound notification is played, and thus the trader will not miss important information. In addition, the built-in email system allows you to reach potential clients for whom you do not have reliable contact information, such as phone number or email addresses. If a trader has opened a demo account and connected to your server, your managers can contact the trader offering a real accounts.

Using the [Automations](/en/docs/mt5/platform/administration/automation/automation_action#message) service, you can automate any mailings. For example, send promotional materials immediately after opening an account. This will save employee time, eliminate human errors, and increase customer conversion.

All emails received and sent from your account are displayed under the "Mail" section:

![Mailbox](/en/docs/mt5/platform/img/mailbox.png "Mailbox")

Each email contains the subject, sender, recipient, and time of sending/receiving.

Unread mails are indicated by icon ![Unread Mail](/en/docs/mt5/platform/img/unread_mail_icon.png "Unread Mail"), while read ones — by ![Read Mail](/en/docs/mt5/platform/img/read_mail_icon.png "Read Mail"). In order to start viewing the message, click in the field of its subject with the left mouse button. Outgoing mails are marked with the ![Outgoing Mail](/en/docs/mt5/platform/img/outgoing_mail_icon.png "Outgoing Mail")icon. When using the function of replying to a message, mails are grouped in a chain which allows to navigate through mailing with different clients easily. Email threads have an additional icon![Email thread](/en/docs/mt5/platform/img/mail_branch_icon.png "Email thread"). Click on it to view the entire conversation.

## Context Menu [#](mail#context)

The context menu of the "Mailbox" tab contains the following commands:

-   ![Create](/en/docs/mt5/platform/img/mail_create_button.png "Create") Create — [create](/en/docs/mt5/platform/administration/mail#create) a message;
-   ![View](/en/docs/mt5/platform/img/mail_view_button.png "View") View — open a selected mail;
-   ![Delete](/en/docs/mt5/platform/img/mail_delete_button.png "Delete") Delete — delete a selected message;
-   ![Expand](/en/docs/mt5/platform/img/mail_expand_button.png "Expand") Expand — expand a selected mail chain;
-   Auto Arrange — if this option is enabled, the size of columns is selected automatically;
-   Grid — this option shows/hides grid to separate fields of the mail table.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The command of creating a mail is active only if the mailbox name is specified in the <a href="/en/docs/mt5/platform/administration/admin_managers#mailbox" class="topiclink">settings</a> of the manager's account.</span></li><li class="p_tableatten"><span class="f_tableatten">Mails are stored at the trade server. If a mail is deleted in the terminal interface, it won't be re-downloaded. However, if you delete the mail base of the terminal (the file "/profiles/server_name/mail/mail-account_number.dat") or connect using another terminal, all the mails for the last 30 days will be downloaded again.</span></li></ul></td></tr></tbody></table>

## Viewing Messages [#](mail#view)

To start viewing a message, click with the left mouse button in the field of its subject. After that the following window will be opened:

![Message Viewing](/en/docs/mt5/platform/img/mail_view.png "Message Viewing")

The upper part of the message contains the client's account and name, the date of mail coming, its subject and attached files (if there are).

The toolbar of this window contains the following commands:

-   ![Reply](/en/docs/mt5/platform/img/mail_answer_button.png "Reply") Reply — open the window of writing a message with filled address of recipient and the quotation of received message;
-   ![Save](/en/docs/mt5/platform/img/save_button.png "Save") Save — save the message on a computer as a HTML file or a text file of the Unicode standard;
-   ![Print](/en/docs/mt5/platform/img/print_button.png "Print") Print — print the message;
-   ![Print Preview](/en/docs/mt5/platform/img/print_preview_button.png "Print Preview") Print Preview — view the message before printing it;
-   ![Attachment](/en/docs/mt5/platform/img/attachment_button.png "Attachment") Attachment — save files attached to the message. Also, an attached file can be opened and saved by simply clicking on its name.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/platform/administrator/settings/settings_common" class="topiclink">Configure the directory</a>, to which email attachments will be saved. When you open an attached file, the terminal checks its extension and the corresponds of file contents to this extension. If the file type is allowed and its contents are checked, the terminal will open the file and save it to the specified directory. Otherwise, a warning will be displayed, notifying that the file may harm the computer, and the file will not be saved. The following file types are allowed: PNG, JPG/JPEG, BMP, ZIP, 7Z, GIF, DOC, XLS, DOCX, XSLX, ODT, RTF, CSV, TXT, LOG.</span></p><p class="p_tableatten"><span class="f_tableatten">If a file with the same name and a different content exists in the directory, the manager's login and email arrival date/time up to a second will be added to the saved file name: [login]-[file name]-[date and time].[extension]. For example, the log file 20170501.log will be saved as 1001-20170501-20170502-170038.log.</span></p><p class="p_tableatten"><span class="f_tableatten">By default, files are saved to C:\Users\[Windows username]\Downloads\MetaTrader.</span></p></td></tr></tbody></table>

## Viewing Attached Log Files [#](mail#journal_viewer)

If a client's message has a log file (a file that has the \*.log extension) attached then one can view it using a special function. To do it, it is necessary to click on its name in the "Attachment" field. The following window will be opened:

![Journal Viewing](/en/docs/mt5/platform/img/mailbox_journal_viewer.png "Journal Viewing")

The upper part of the window of viewing contains the line of searching through the log (the search is performed only by the exact words and it is case sensitive) and the filter of entries (Standard, Errors, Full). Once having the searched word and filter specified, one should press the "Request" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If a client has changed even one entry of the journal then all the entries starting from it are shown with the red color. At the attempt of saving such a file, the warning that says which line in it was changed, is shown.</span></p></td></tr></tbody></table>

The context menu of the window of viewing the journal allows to execute the following commands:

-   ![Copy](/en/docs/mt5/platform/img/copy_button.png "Copy") Copy — copy selected entries to the clipboard;
-   ![Save](/en/docs/mt5/platform/img/save_button.png "Save") Save — save the received logs to the disk as a text document;
-   Auto Arrange — if this option is enabled, the size of columns is selected automatically;
-   Grid — this option shows/hides grid to separate table fields.

## Sending Messages [#](mail#create)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">In order to be able to send messages it is necessary to:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Enable <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#enable_mail" class="topiclink">corresponding option</a> in the manager's group settings;</span></li><li class="p_tableatten"><span class="f_tableatten">Grant manager the permission of <a href="/en/docs/mt5/platform/administration/admin_managers#mail" class="topiclink">sending mails</a>;</span></li><li class="p_tableatten"><span class="f_tableatten">Specify the <a href="/en/docs/mt5/platform/administration/admin_managers#mailbox" class="topiclink">name of manager's mailbox</a>.</span></li></ul></td></tr></tbody></table>

To create a message, one should press the "![Create](/en/docs/mt5/platform/img/mail_create_button.png "Create") Create" button of the context menu or use the "Insert" hot key having the "Toolbox" window active. The window of creating the mail will appear as soon as it is pressed:

![Message Creating](/en/docs/mt5/platform/img/mail_create.png "Message Creating")

In this window one should fill out the following fields:

-   To — the account number of the message recipient.
-   Subject — title of the message.
-   Template — in this field one can select a mail [template](/en/docs/mt5/platform/administration/mail#templates).
-   Internal mail — select this option to send a message using the internal mail system.
-   Email — use this option to send an email. The address specified in [account personal data](/en/docs/mt5/platform/administration/admin_accounts/account_edit#personal) will be used. Please note:

-   [A mail server](/en/docs/mt5/platform/administration/integration/integration_mail) must be configured in the platform to enable email sending.
-   Messages sent by email are not displayed under the "Toolbox \\ Mail" section. To check the sending, request the [trade server journal](/en/docs/mt5/platform/administration/admin_network/network_journal) using the 'email' keyword. If an email has been sent successfully, the recipient address and the configuration name of the mail server through which the email has been sent, are shown in the log: email to someaddress@mail.net sent \[MailServer\].

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The attachment of files has the following limitations:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">The size of one attached file cannot exceed 2MB;</span></li><li class="p_tableatten"><span class="f_tableatten">The total size of attached files cannot exceed 4MB;</span></li><li class="p_tableatten"><span class="f_tableatten">Up to 5 files can be attached.</span></li></ul></td></tr></tbody></table>

The window for working with the mail text is located lower. The editor features commands for creating lists, as well as inserting images, links and tables. To view or edit the source HTML code of the message, click ![Switch to HTML mode](/en/docs/mt5/platform/img/html_visual_button.png "Switch to HTML mode") on the toolbar.

The context menu of the window of text editing contains the standard commands of working with text: "Copy", "Cut", "Paste", "Insert Link", "Insert Table" and "Insert Image". The context menu also allows to work with mail [templates](/en/docs/mt5/platform/administration/mail#templates) and [macros](/en/docs/mt5/platform/administration/mail#macro).

To send the message, one should press the "Send" button.

### Bulk Mailing [#](mail#mass_mailing)

To send emails to multiple recipients, enter a range of accounts through a hyphen in the "To" field. For example, 1000-9000. You can also select [multiple accounts in the list](/en/docs/mt5/platform/administration/admin_accounts) and click 'Email' in the context menu. The numbers of the selected accounts will be inserted into the "To" field.

When using Email instead of the internal mail, it could be more efficient to send emails to a list of clients rather than accounts. Clients often have multiple accounts that use the same email address. Because of this, when sending emails to a list of accounts, the client may receive several identical messages. To avoid this, send emails from the [Clients](/en/docs/mt5/platform/administration/clients) section. Select the desired client records and click "Internal mail/Email" in the menu. The mailing list will only include unique email addresses from all the trading accounts linked to the selected clients.

## Templates [#](mail#templates)

To manage templates, use the context menu of the [mail editing](/en/docs/mt5/platform/administration/mail#create) window (text editing area). Open the "Templates" submenu:

-   Save Template — save the current text of the message as a template in the \*.htm format. All templates are stored in the [/templates/mail](/en/docs/mt5/platform/administrator/getting_started/structure#mail_templates) folder of the administrator terminal;
-   Load Template — open the window of choosing a previously saved template for loading it;
-   Remove Template — delete the currently selected template.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">When executing the "Remove Template" command a template is irrecoverably deleted from PC.</span></p></td></tr></tbody></table>

## Macros [#](mail#macro)

Using the "Macros" submenu of the context menu of the [mail creating](/en/docs/mt5/platform/administration/mail#create) window, one can insert macros into the text. They allow to substitute various information depending on the message recipient. The following macros are available:

-   Login (#LOGIN#) — the email/messenger recipient's Account number.
-   Name (#USERNAME#) — the first name and the last name of the recipient.
-   Currency (#USER\_CURRENCY#) — the recipient's deposit currency. The currency is determined by the [group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#currency), in which the user account is created.
-   Balance (#USER\_BALANCE#) — the recipient's balance.
-   Credit (#USER\_CREDIT#) — the credit amount on the recipient's account.
-   Equity (#USER\_EQUITY#) — the equity amount on the recipient's account.
-   Leverage (#USER\_LEVERAGE#) — account leverage.
-   Margin (#USER\_MARGIN#) —  the amount of funds reserved on the recipient's account.
-   Free margin (#USER\_MARGIN\_FREE#) — the free margin amount on the recipient's account.
-   Margin level (#USER\_MARGIN\_LEVEL#) — the margin level on the recipient's account.

These macros substitute email sending time in the message text:

-   Trading time — time used in the platform, taking into account its [settings](/en/docs/mt5/platform/administration/admin_time).
-   Local time — time used in the computer on which the platform is installed.
-   UTC time — [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) time.

[Controlling Subscriptions](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control)

[Live Update](/en/docs/mt5/platform/administration/admin_update)