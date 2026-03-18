# SendMail Utility

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/trade_server/sendmail

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
                -   [Structure of Directories and Files](/en/docs/mt5/platform/components/trade_server/trade_server_structure)
                -   [Mail Templates](/en/docs/mt5/platform/components/trade_server/mail_templates)
                -   [Daily Reports](/en/docs/mt5/platform/components/trade_server/daily_reports)
                -   [SendMail Utility](/en/docs/mt5/platform/components/trade_server/sendmail)
                -   [Return Errors](/en/docs/mt5/platform/components/trade_server/returned_errors)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
            -   [Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Trade Server](/en/docs/mt5/platform/components/trade_server)SendMail Utility

# SendMail Utility

MetaTrader 5 SendMail is a command-line utility and a component of MetaTrader 5 platform. It is used by a trade server for sending reports and emails. This application can be used for sending reports manually.

## Report Generation

The trade server [prepares reports on](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day) client deals at the end of a working day placing them to the separate directory ("/MetaTraderServer/confirms/YYYYMMDD", where YYYYMMDD is current date). Each report is an HTML file having the name "login\_mail.htm" (for example, "123\_mail.htm"). After generating all reports, the trade server saves the configuration file ("mail.cfg") containing descriptions of account groups with e-mail settings in the same directory and then launches MetaTrader 5 SendMail utility.

## Operation Principles

After launching MetaTrader 5, SendMail reads the configuration file and starts sending emails to account groups. Description of each group contains data that is sufficient for authorization on the specified SMTP server. In case of an authorization error, the program simply moves to the next group sending the appropriate error message to the journal. If authorization is successful, reports are consistently sent to these group's accounts.

Two types of errors may occur when sending reports. First, connection to the SMTP server may be lost. In this case, an attempt to handle the next group is made. Second, the server may report that it is not able to send a report to the specified client address (for example, if the latter is incorrect). In this case, the report is marked as unsent and handling is moved to the next one.

After all MetaTrader 5 groups are handled, SendMail records the results in the same configuration file. Then all the reports and the configuration file are compressed into a ZIP file. ZIP file's name is based on the name of a low-level folder in the path to the reports (for example, if the path is "C:\\mt5\\trade\_server\\confirms\\20130101", then ZIP file's name is "20130101.zip"). After the successful archiving, all source files are deleted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: We strongly recommend to use your own mail server (at least having the </span><span class="f_tableatten" style="font-style: italic;">mail.your_company.domain</span><span class="f_tableatten"> name)</span><span class="f_tableatten"> instead of a provider's or even a public one. That ensures sender's (your company's) authenticity and allows adjusting the mail server's parameters for efficient mailing. Currently, mail servers and providers introduce strict rules concerning mail sending and receiving. That often leads to some brokers having issues when performing mass mailing.</span></p><p class="p_tableatten"><span class="f_tableatten">To simplify the task, you may configure your own mail server, so that it is able to accept any mail from the trade server's IP address without limitations. If you do not have access to your mail server's settings, ask your provider to configure it appropriately.</span></p></td></tr></tbody></table>

# Sending Reports Manually

Reports may be sent manually in two modes: group and individual ones. To choose the mode, one of the keys should additionally be specified in the command line when launching MetaTrader 5 SendMail:

-   mt5sendmail64.exe /mail:\[path\] — individual mailing.
-   mt5sendmail64.exe /group:\[path\] — group mailing.
-   /archive — specify this key after /mail:\[path\] or /group:\[path\] to force the SendMail archive the reports after sending.

### Individual Mailing

MetaTrader 5 SendMail with "mail" key should be launched to send a report to a single user:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">mt5sendmail64.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/mail:"path"&nbsp;/archive</span></p></td></tr></tbody></table>

Path is the path to the directory containing folder.cfg mailing configuration file (the file should have exactly the name mentioned above). Do not add a backslash at the end of the path:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">mt5sendmail64.exe&nbsp;/mail:&nbsp;"C:\MetaTrader&nbsp;5&nbsp;Platform\MainTrade\confirms\2021.05.11.daily"&nbsp;/archive</span></p></td></tr></tbody></table>

Here is an example of a configuration file structure:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">from=abc@company.net</span><br><span class="f_CodeExample">name=ABC</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Company</span><br><span class="f_CodeExample">subject=Trade</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Report</span><br><span class="f_CodeExample">to=johnsmith@mail.net</span><br><span class="f_CodeExample">to_name=John</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Smith</span><br><span class="f_CodeExample">charset=utf-8</span><br><span class="f_CodeExample">body=D:\Reports\John_Smith\mail.htm</span><br><span class="f_CodeExample">attachments=D:\Reports\John_Smith\balance.jpg</span><br><span class="f_CodeExample">smtp_srv=abc@company.net</span><br><span class="f_CodeExample">smtp_login=mailer</span><br><span class="f_CodeExample">smtp_pass=mailerpassword</span></p></td></tr></tbody></table>

The following parameters are specified in the configuration file:

-   from — e-mail address, from which the report is sent.
-   name — sender's name.
-   subject — email subject.
-   to — recipient's email address.
-   to\_name — recipient's name.
-   charset — email's character set.
-   body — path to the HTM file containing the email's contents.
-   attachments — path to the file that is to be attached to the email. If you want to attach several files, specify paths to them divided by tab. The line length, including the parameter name, should not exceed 256 characters.
-   smtp\_srv —  SMTP server address used for sending messages.
-   smtp\_login — login for authorization on the mail server. In most cases, it is a mailbox, for example, "your\_name@mail.ru".
-   smtp\_pass — password for authorization on the mail server (mailbox password).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Up to 8 attachments can be added to an email.</span></li><li class="p_tableatten"><span class="f_tableatten">Attachment size may not exceed 4 MB.</span></li><li class="p_tableatten"><span class="f_tableatten">The password for authorization on the SMTP server is stored in the clear. This is done in order to modify the configuration file easily. The administrator can change the configuration (for example, a password) and launch SendMail manually. For security purposes, it is recommended to limit access to report configuration files.</span></li></ul></td></tr></tbody></table>

### Group Mailing

MetaTrader 5 SendMail with "group" key should be launched to send a report to a group of users:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">mt5sendmail64.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/group:"path"&nbsp;/archive</span></p></td></tr></tbody></table>

Path is a path to mail.cfg file (the file should have exactly the name mentioned above) containing description of mailing settings.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Report files being sent should be in the same directory with </span><span class="f_tableatten" style="font-style: italic;">mail.cfg</span><span class="f_tableatten"> configuration file. The report for each user should be in the form of an HTM file named </span><span class="f_tableatten" style="font-style: italic;">"login_mail.htm"</span><span class="f_tableatten"> (for example, </span><span class="f_tableatten" style="font-style: italic;">"123_mail.htm"</span><span class="f_tableatten">).</span></p></td></tr></tbody></table>

Here is an example of a configuration file structure:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;group&gt;</span><br><span class="f_CodeExample">name=demoforex</span><br><span class="f_CodeExample">company=MetaQuotes</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Software</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Corp.</span><br><span class="f_CodeExample">email=reporter@metaquotes.ru</span><br><span class="f_CodeExample">subject=Trade&nbsp;Report</span><br><span class="f_CodeExample">smtp_srv=mail.metaquotes.ru</span><br><span class="f_CodeExample">smtp_login=reporter</span><br><span class="f_CodeExample">smtp_pass=securepass</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">101</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">1</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">John</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Smith</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;j</span><span class="f_CodeExample">johnsmith@mail.ru</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">102</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">1</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Ivan</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Ivanov</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">ivan@mail.ru</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">103</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">2</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Larisa</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Ivanovna</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">larisa@mail.ru</span><br><span class="f_CodeExample">&lt;/group&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;group&gt;</span><br><span class="f_CodeExample">name=forever</span><br><span class="f_CodeExample">company=MetaQuotes</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Software</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Corp.</span><br><span class="f_CodeExample">email=mailer@metaquotes.ru</span><br><span class="f_CodeExample">smtp_srv=mail.metaquotes.ru</span><br><span class="f_CodeExample">smtp_login=mailer</span><br><span class="f_CodeExample">smtp_pass=mailerpassword</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">151</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Alisa</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">alisa@pole.ru</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">152</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Brom</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">brom@fix.com</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">153</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SirX</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">sirx@fix.com</span><br><span class="f_CodeExample">&lt;/group&gt;</span></p></td></tr></tbody></table>

Each target user group is described by a couple of <group> tags. Description of each group contains several mandatory fields:

-   name — group name.
-   company — company name that will be specified as a sender's name.
-   email — e-mail address, on behalf of which the report is sent.
-   subject — email subject.
-   smtp\_srv —  SMTP server address used for sending messages.
-   smtp\_login — login for authorization on the mail server. In most cases, it is a mailbox, for example, "your\_name@mail.ru".
-   smtp\_pass — password for authorization on the mail server (mailbox password).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_txt">The password for authorization on the SMTP server is stored in the clear. This is done in order to modify the configuration file easily. The administrator can change the configuration (for example, a password) and launch SendMail manually. For security purposes, it is recommended to limit access to report configuration files.</span></p></td></tr></tbody></table>

The group's description is followed by the list of users that should receive the reports. The description and the list should be divided by an empty line used as a separator.

Each entry in the user list consists of the four fields: login, mailing status, recipient name and email. Tab character is used as a field separator. The first field may contain spaces before its contents. Let's examine a sample entry in more details:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">102</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">1</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Ivan</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Ivanov</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">ivan@mail.ru</span></p></td></tr></tbody></table>

Status ID may have the following values:

-   0 — report has not been sent or is on hold.
-   1 — report has been sent successfully.
-   2 — report delivery error, invalid recipient e-mail address.

After the reports have been sent, mailing status is updated in the same configuration file.

[Daily Reports](/en/docs/mt5/platform/components/trade_server/daily_reports)

[Return Errors](/en/docs/mt5/platform/components/trade_server/returned_errors)