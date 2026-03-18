# Mail Templates

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/trade_server/mail_templates

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Trade Server](/en/docs/mt5/platform/components/trade_server)Mail Templates

# Mail Templates

Several types of emails that are automatically sent to clients are implemented in the the MetaTrader 5 platform:

-   Welcoming email at account opening;
-   Email requesting the certificate confirmation;
-   Daily report on trade activity;
-   Monthly report on trade activity.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">All templates must be of the Unicode format (UTF-16/UCS-2 Little Endian).</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">In order to start using a new template, the main trade server must be restarted.</span></li></ul></td></tr></tbody></table>

## Welcoming Emails [#](mail_templates#greeting)

Welcome messages are sent to clients through the internal mail system when an account is opened. It does not matter how the account is opened: by the trader via the client terminal or by the broker via the Manager/Administrator terminal. The welcome email contains the account number and password, as well as general information about the MetaTrader 5 platform.

Welcome email templates are located in the following [directory](/en/docs/mt5/platform/components/trade_server/trade_server_structure#templates):

-   Trader server directory\\templates\\greeting\\default\\\*.htm — default templates used for groups;
-   Trader server directory\\templates\\greeting\\custom folder\\\*.htm — templates of emails that can be sent only to separate groups with account of their settings;
-   Trader server directory\\templates\\greeting\\preliminary\\\*.htm — templates of emails that are sent when a [preliminary account](/en/docs/mt5/platform/administration/admin_groups/group_types#preliminary) is opened from the client terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">An unlimited number of folders with special templates can be create. The name of the folder with templates that will be used for a group are specified in the "Company" tab in its <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#templates_folder" class="topiclink">settings</a>.</span></p></td></tr></tbody></table>

## Certificate Confirmation Email [#](mail_templates#certificate)

These letters are sent if the [extended authorization](/en/docs/mt5/platform/administration/admin_groups/groups_settings#authorization) and [certificate confirmation](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization#confirm) mode is enabled for this group. Such an email contains information on how to confirm a certificate. Templates of such emails are stored in the following [directory](/en/docs/mt5/platform/components/trade_server/trade_server_structure#templates):

-   Trader server directory\\templates\\certificate\\default\\\*.htm — default templates used for groups;
-   Trader server directory\\templates\\certificate\\custom folder\\\*.htm — templates of emails that are sent only to separate groups with account of their settings.

## Phone and Email Verification [#](mail_templates#confirm)

These emails\\messages are sent to [verify phone numbers and emails](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups#confirmation), specified during registration of demo and preliminary accounts from client terminals.

-   Trader server directory\\templates\\verify\_email\\default\\\*.htm — email templates as HTM files.
-   Trader server directory\\templates\\verify\_phone\\default\\\*.htm — SMS templates as text files. Do not use too long messages. If the allowed length is exceeded (depending on the provider), a message may be cropped or split into multiple SMS.

The <!--CONFIRMATION\_CODE--> macro is used for confirmation emails. This code adds the generated confirmation code to the text.

Templates from the "default" folder are used on default for all groups. If you need to use custom templates for a specific group, create another folder in the same directory and place the template files to it. Then specify the folder name in the [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#templates_folder).

## Daily Report on Trade Activity [#](mail_templates#daily)

Daily reports on trade activity of clients are sent if the "Send daily statements by email" option is enabled in the [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports). Templates of such emails are stored in the following:

-   Trader server directory\\templates\\confirmation\\default\\\*.htm — default templates used for groups;
-   Trader server directory\\templates\\confirmation\\custom folder\\\*.htm — templates of reports that are sent only to separate groups with account of their settings.

## Monthly Report on Trade Activity [#](mail_templates#monthly)

Monthly reports on trade activity of clients are sent if the "Send daily statements by email" option is enabled in the [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports). Templates of such emails are stored in the following:

-   Trader server directory\\templates\\statement\\default\\\*.htm — default templates used for groups;
-   Trader server directory\\templates\\statement\\custom folder\\\*.htm — templates of reports that are sent only to separate groups with account of their settings.

## Payments [#](mail_templates#payments)

These emails/messages are sent when transactions are performed through the [integrated payment system](/en/docs/mt5/platform/administration/payments). The relevant templates are located in the '\[Trade Server Directory\]\\templates\\payments\\' directory.

-   deposit\_completed — successful deposit.
-   deposit\_failed — failed deposit.
-   deposit\_processed — the deposit operation is being processed.
-   withdrawal\_completed — successful withdrawal.
-   withdrawal\_confirmed — withdrawal confirmation. This message is used when a withdrawal request is submitted for processing to the payment system.
-   withdrawal\_failed — failed withdrawal.
-   withdrawal\_verified — withdrawal verification. This sent is used upon manager approval, allowing the user to proceed with the payment. Used for providers where all payment details are entered on the payment system's page (e.g., [AstroPay](/en/docs/mt5/platform/administration/payments/payments_wallets/payments_astropay)). In such cases, during manual processing, the manager only approves the transaction itself.

## Email templates in different languages [#](mail_templates#multilanguage)

All template files should be named according to the language they are written in. A file name is used by the platform to determine which users the template is to be applied to. The user's language is defined in the [account settings](/en/docs/mt5/platform/administration/admin_accounts/account_edit#personal).

Languages are specified in the format standard for the family of Windows operating systems, though without the specification of regional dialect specifics. E.g. English.htm, Russian.htm and so on. The only exceptions are Chinese language templates. In case of simplified Chinese, a template should be named chinese.htm, while in case of traditional Chinese, it is named chinese\_traditional.htm.

If no template was found for the language specified in the account, the default.htm template is used. If a separate folder is specified for a group, the default template is first searched for in this folder, and if it is not found an email according to the default.htm template located in the "Default" folder is sent.

## The Format of Files

A template file can contain a plain text, HTML tags, as well as CSS design elements. To insert images, set them on your web server and specify the appropriate links in <img src="URL">. The web server must operate using the HTTPS protocol. Images with URLs starting with http:// will not be displayed.

Besides, the templates can be equipped with special macros for inserting various data depending on an account an email is sent to.

-   Common macros
-   <!--ACCOUNT--> — account number.
-   <!--LOGIN--> — account number.
-   <!--GROUP--> — user group.
-   <!--PASSWORD--> — account master password.
-   <!--INVESTOR--> — account investor password.
-   <!--NAME--> —  user first name (obsolete macro).
-   <!--USERNAME--> — user first name (obsolete macro).
-   <!--FIRST\_NAME--> — user first name.
-   <!--LAST\_NAME--> — user last name.
-   <!--MIDDLE\_NAME--> — user middle name.
-   <!--COUNTRY--> — country of residence.
-   <!--CITY--> — city of residence.
-   <!--STATE--> — state (region) of residence.
-   <!--ZIPCODE--> — zip code.
-   <!--ADDRESS--> — residential address.
-   <!--PHONE--> — phone number.
-   <!--EMAIL--> — email address.
-   <!--COMMENT--> — account comment.
-   <!--ID--> — ID.
-   <!--STATUS--> — residency status.
-   <!--PHONEPASS--> — phone password.
-   <!--AGENT--> — agent account associated with the user.
-   <!--CURRENCY--> — account deposit currency.
-   <!--COMPANY--> — [company name](/en/docs/mt5/platform/administration/admin_groups/groups_settings#company_name) from the account group settings.
-   <!--LEVERAGE--> — recipient's current leverage.

### Daily and monthly report macros

-   <!--DATE--> — date the report is generated for, YYYY.MM.DD.
-   <!--TIME--> — time the report is generated for, HH::MM:SS.
-   <!--FULLTIME--> — date and time the report is generated for, YYYY.MM.DD HH::MM:SS.
-   <!--BALANCE--> — balance at the time of the report generation.
-   <!--CREDIT--> — credit funds at the time of the report generation.
-   <!--INTERESTRATE--> — client's annual interest rate.
-   <!--COMMISSION\_DAILY--> — amount of standard commissions charged from a client for the day the report is generated for.
-   <!--COMMISSION\_MONTHLY--> — amount of standard commissions charged from a client for the month the monthly report is generated for (or for the current month in case of a daily report).
-   <!--AGENT\_DAILY--> — agent commissions charged from a client for the day the report is generated for.
-   <!--AGENT\_MONTHLY--> — agent commissions charged from client's operations for the month the monthly report is generated for (or for the current month in case of a daily report).
-   <!--PREV\_BALANCE\_DAILY--> — client balance at the end of the previous trading day.
-   <!--PREV\_BALANCE\_MONTHLY--> — client balance at the end of the previous month.
-   <!--PREV\_EQUITY\_DAILY--> — client equity at the end of the previous trading day.
-   <!--PREV\_EQUITY\_MONTHLY--> — client equity at the end of the previous month.
-   <!--PREV\_DATE--> — the date of the last but one closure of the trading day.
-   <!--PREV\_TIME--> — the time of the last but one closure of the trading day.
-   <!--PREV\_FULLTIME--> — the date and time of the last but one closure of the trading day.
-   <!--MARGIN--> — money required to cover open positions as of the end of the day/month.
-   <!--MARGIN\_FREE--> — amount of free margin volume as of the end of the day/month.
-   <!--MARGIN\_LEVEL--> — margin level as of the end of the day/month.
-   <!--FLOATING\_PROFIT--> — floating profit/loss on all open positions at the time of the report generation.
-   <!--FLOATING\_STORAGE--> — size of swaps charged for client's positions for a day, but not yet reflected in the balance.
-   <!--FLOATING\_COMMISSION--> — floating client commission blocked on the account but not yet reflected in the balance at the time of the report generation.
-   <!--FLOATING\_EQUITY--> — client equity volume at the time of the report generation.
-   <!--FLOATING\_PL--> — total client's floating profit/loss at the time of the report generation. Calculated as <!--FLOATING\_PROFIT--> + <!--FLOATING\_STORAGE--> + <!--FLOATING\_COMMISSION-->.
-   <!--FLOATING\_LIABILITIES--> — amount of client liabilities at the time of report generation. It is only used for the [Exchange risk management model](/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk).
-   <!--FLOATING\_ASSETS--> — amount of client assets at the time of report generation. It is only used for the [Exchange risk management model](/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk).
-   <!--CLOSED\_PROFIT--> — total closed profit/loss at all deals per day/month.
-   <!--CLOSED\_STORAGE--> — size of swaps charged for a client's positions for a day/month.
-   <!--CLOSED\_DEPOSIT--> — total funds deposited/withdrawn from the account per day/month.
-   <!--CLOSED\_CREDIT--> —  credit funds deposited/withdrawn from the account per day/month.
-   <!--CLOSED\_CHARGE--> — other depositions/withdrawals from the client's balance per day/month.
-   <!--CLOSED\_CORRECTION--> — corrective balance operations performed on the client's account per day/month.
-   <!--CLOSED\_BONUS--> — bonus funds deposited/withdrawn from the account per day/month.
-   <!--CLOSED\_COMMISSION\_INSTANT--> — standard commissions withdrawn from a client's account per day/month instantly (during a trade).
-   <!--CLOSED\_COMMISSION\_ROUND--> — commission by orders and positions accumulated during a day/month. Depending on the settings (specified for the group in the administrator terminal), preliminary commission calculation is performed during a day/month and the appropriate funds are blocked in the account and displayed here. Final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account by the balance operation.
-   <!--CLOSED\_FEE--> — total fees charged from the client for the day/month.
-   <!--CLOSED\_AGENT--> — agent commissions charged from the client for the day the report is generated for.
-   <!--CLOSED\_INTEREST--> — annual interest rate accruals per day/month the report is generated for.
-   <!--CLOSED\_DIVIDEND--> — dividends received by the client per day/month the report is generated for.
-   <!--CLOSED\_TAX--> — taxes charged per day/month the report is generated for.
-   <!--CLOSED\_PL--> — total profit/loss at a client's account per day/month the report is generated for. Calculated as <!--CLOSED\_PROFIT--> + <!--CLOSED\_STORAGE--> + <!--CLOSED\_COMMISSION\_INSTANT-->.
-   <!--CLOSED\_ADDITIONAL--> — financial result of other transactions conducted on the account for the day/month the report is generated for. These are additional charges, corrections, bonuses, agent commissions, annual interests, dividends and taxes
-   <!--CLOSED\_TOTAL--> — total financial result of the client's account for the day/month the report is generated for. Calculated as the sum of all the above values with the <!--CLOSED\_\*--> prefix apart from <!--CLOSED\_PL--> and <!--CLOSED\_ADDITIONAL-->.
-   <!--CLOSED\_SO\_COMPENSATION--> — the sum of balance operations connected with [the negative balance compensation](/en/docs/mt5/platform/administration/admin_groups/groups_settings#compensate) after Stop Out.
-   <!--CLOSED\_COST--> — the total amount of costs for all deals for the day/month for which the report is generated. The value calculation does not depend on [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#deal_cost). If a macro is included in a report template, its value will be calculated and substituted.
-   <!--PREV\_EQUITY\_DIFF\_PERC\_DAILY--> — a change in equity as compared to the previous day value. Indicated as a percentage.
-   <!--PREV\_EQUITY\_DIFF\_PERC\_MONTHLY--> — a change in equity as compared to the previous month value. Indicated as a percentage.

### Macros of Trading Operations

Daily reports include blocks of trading operations performed by a client during a day/month. Each of these blocks begins with a macro corresponding to the operation type:

-   <!--MQTABLE=Closed Orders--> — closed orders.
-   <!--MQTABLE=Closed Deals--> — executed deals.
-   <!--MQTABLE=Positions--> — current open positions.
-   <!--MQTABLE=Orders--> — current open orders.

Each of these blocks ends with the <!--MQTABLE--> macro. Information about trading operations is displayed using macros inside the blocks. Depending on the block in which a macro is contained, it substitutes information about the appropriate operation type, i.e. order, deal or positions.

-   <!--Ticket--> — the ticket of a trading operation.
-   <!--Type--> — the type of a trading operation (buy, sell or a pending order).
-   <!--Size--> — the volume of a trading operation. The initial and filled volume is additionally displayed for orders.
-   <!--Item--> — the name of a trading instrument.
-   <!--ISIN--> — International Securities Identification Number (ISIN).
-   <!--Price--> — the price at which a trading operation was executed.
-   <!--SL--> — the Stop Loss level.
-   <!--TP--> — the Take Profit level.
-   <!--Open Time--> — operation time.
-   <!--Close Time--> — order or position closing time.
-   <!--State--> — order status (filled, rejected, canceled).
-   <!--Comment--> — a comment on the operation.
-   <!--Entry--> — trade direction (in, out, in/out).
-   <!--Commission--> — commission charged for the operation.
-   <!--Fee--> — the amount of fees for the operation.
-   <!--Swap--> — operation swap.
-   <!--Cost--> — the amount of costs incurred when performing deals relative to the current mid-point spread cost. The value calculation does not depend on [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#deal_cost). If a macro is included in a report template, its value will be calculated and substituted.
-   <!--Profit--> — profit received from the operation.
-   <!--Market--> — the market price of a trading instrument at the time of report generation.
-   <!--Color--> — a macro for alternating the background color of even and odd rows (a row with a white background, the next one has a gray background, etc).

[Structure of Directories and Files](/en/docs/mt5/platform/components/trade_server/trade_server_structure)

[Daily Reports](/en/docs/mt5/platform/components/trade_server/daily_reports)