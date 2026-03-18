# Groups

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_groups

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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
                -   [Group Types](/en/docs/mt4/administrator/administration/ug_groups/group_types)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Groups

# Groups

All users of the system are divided into groups. There are no users on the server who would not belong to a group. Up to 511 groups can be created. Initially, the system has some pre-defined groups having certain rights:

-   manager — manager accounts (the largest possible rights in the system);
-   demoforex — demo accounts;

![Groups](/en/docs/mt4/administrator/img/br_group.png "Groups")

-   Name is the unique user group name;
-   Company is the name of the company servicing the group;
-   MC/SO are the Margin Call and Stop Out levels;
-   Securities is the list of securities that are availale to the group.

The context menu commands "Add" and "Edit", the same commands of the "Edit" menu, and buttons like ![Add User Group](/en/docs/mt4/administrator/img/ic_config_add.png "Add User Group") and ![Group Setting](/en/docs/mt4/administrator/img/ic_config_edit.png "Group Setting") of the toolbar activate window of detailed user group settings. And the "Delete" command and the ![Delete User Group](/en/docs/mt4/administrator/img/ic_config_delete.png "Delete User Group") button delete user group if there are no accounts in it. The "Move Up" and "Move Down" commands allow to move different user groups in the list without changing their properties.

## User Group Detailed Setting in the Common Tab [#](ug_groups#group_common)

When a group has been added or changed, a setup window will open:

![Common Tab](/en/docs/mt4/administrator/img/win_group_common.png "Common Tab")

-   Enable — enable/disable a group. Using this option, you can easily manage groups. For example, after the contest has been finished, you can just disable the "contest" group. Starting the next contest, you can enable it again;
-   Name is the unique user group name (Latin letters, no spaces or "\*" characters). It is recommended to give some reasonable names to the groups (e.g., forex) as traders will see them in the "Account Type" field on the client terminal;

-   One-time password — use of OTP (one-time password) provides an additional level of security when working with trading accounts. The user is required to enter a unique one-time password every time to connect to an account. One-time passwords are generated in the [mobile terminal for iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=download&utm_source=metatrader4.help "mobile terminal for iPhone") and the [mobile terminal for Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=download&utm_source=metatrader4.help "mobile terminal for Android"). This option allows to disable the use of OTP or enable OTP using a standard generator TOTP SHA-256. The use of OTP can be [disabled for certain clients](/en/docs/mt4/administrator/administration/ug_accounts#otp) in the group.
-   Force one-time password usage — in some countries, regulators require use of additional account security measures, such as the use of OTP. When this option is enabled, all clients in this group have to use one-time passwords to connect. Otherwise, clients can either use the default authentication method via login and password, or additionally bind their accounts to an OTP generator.  
    Before you force OTP usage, please inform your clients. Be extremely careful when enabling this option for the only one manager group on the trading server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_ol">The instructions for using one-time password are provide in the client terminal user guide.</span></li><li class="p_tableatten"><span class="f_tableatten">One-time passwords are available only for client accounts in desktop and mobile terminals. OTP authorization is currently not available for the manager and administrator terminals as well as for webterminals.</span></li></ul></td></tr></tbody></table>

-   Owner — the name of the company that manages this group. It is shown to traders in the terminal and is also used when generating reports. The list of companies available for selection is formed based on the trading platform license. This can only be the company that owns either the main or additional [White Label](https://support.metaquotes.net/en/articles/334).

-   Support page is an address of the website of the technical support team. The specified page will be displayed in the "Company" tab of the "Toolbox" window in the client terminals. If the address is not specified, that tab will be hidden.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When specifying the address, one can use macros that are replaced on the client terminal side forming the final address:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">[lang:en|ru|es|..] — list of languages in ISO 639-1 format. If one of the languages in the list matches the one of the client terminal's interface, the latter one is used. Otherwise, the first one from the list is applied. Example: www.broker-support-site.com/[lang:en|ru|es|cn]/.</span></li><li class="p_tableatten"><span class="f_tableatten">[login] — client's current login.</span></li><li class="p_tableatten"><span class="f_tableatten">[uniq] — unique ID of the client's PC.</span></li></ul></td></tr></tbody></table>

-   Deposit by default means the deposit by default. This option is used only by opening demo accounts. If a definite value is given, all demo accounts to be opened will have the indicated deposit;
-   Deposit Currency means the deposit currency by default. Latin characters only, no punctuation marks, spaces or special characters. This option cannot be changed when the server is operating provided at least one client is included into the group;
-   Leverage by default is the leverage by default. This option is used only by opening demo accounts. If a definite value is given, all demo accounts to be opened will have the indicated leverage;
-   Annual Interest Rate interest rate to be calculated for free margin (annual interest);

## User Group Detailed Setting in the Permissions Tab [#](ug_groups#group_rights)

![Permissions Tab](/en/docs/mt4/administrator/img/win_group_rights.png "Permissions Tab")

-   Timeout contains the time period within which the user's response can be waited for. The recommended value is 7 seconds (2 seconds - for network deference + 5 seconds for client to think over);
-   News enables news mode (disable — disables news delivery; topics only — allows to show only topics; full package — enables to deliver all news completely);
-   News languages — select the language of news that will be broadcast to the clients in this group. To [set up languages](/en/docs/mt4/administrator/administration/ug_groups#language) click "Change".
-   Maximum symbols — the available symbol list limitation. Clients will only be allowed to operate with indicated amount of instruments (symbols);
-   Maximum orders — the maximum amount of both open positions and pending orders for the account of this group;
-   Trade signals — allow/prohibit using the ["Signals"](https://www.mql5.com/en/signals "Trade Signals in MetaTrader 5") service in the client terminals.

-   Disabled — if this option is selected, the signal settings (the "Options" window) and the signal list (the "Toolbox" window) are hidden in client terminals connected using the accounts from this group. Users will not be able to subscribe to any signals both from the terminal and via www.mql5.com.
-   Enable all signals from all brokers — this option allows using the ["Signals"](https://www.mql5.com/en/signals "Trading Signals in MetaTrader 5") service in trading terminals without limitations.
-   Enable signals from my severs only — if this option is selected, clients in this groups will be able to subscribe only to the signals created on the basis of accounts opened in your brokerage company (broker name in a signal must match the "Owner" field in the group settings). Signals created on the basis of other accounts will not be displayed in the client terminals.

-   Enable internal mail system — enable/disable clients' access to the internal mail system;
-   Enable charge of swaps — enable/disable charging swaps and interests for free margins of the account;
-   Enable trading by Expert Advisors — enable/disable trading by Expert Advisors;
-   Enable expiration of pending orders — enable/disable expiration time of pending orders in client terminals;
-   Enable trailing stops — enable/disable using of trailing stops;
-   Check request prices in IE — check client's request prices by symbols in Instant Execution mode for presence in the quotes stream from datafeeds;
-   Prohibit hedge positions — enabling this option prohibits all accounts in the group to have open opposite positions on one symbol at the same time;
-   Position closing according to FIFO rule — enables/disables the mode of closing positions in accordance with the FIFO rule. If this option is enabled, it is allowed to close positions by each symbol only in the same order as they were opened. Enabling this option also forces enabling the "Prohibit hedge positions" option. More detailed description of the FIFO rule is given in the article: ["NFA and FIFO: Deliberation about NFA Compliance Rule 2-43(b)"](https://support.metaquotes.net/en/articles/168).
-   Use partial close with full close initial position — enable/disable partial closure mode with full closing of initial position. If this option is disabled, during partial position closing its remaining part is closed too and then reopened with the new volume at the same price. If this option is enabled, the remaining part is reopened at a current price.

-   Show the risk warning window after connection — if this option is enabled, when a client connects in the trading terminal, a warning about the risks associated with operations on the financial markets appears. Trade operations on a client's account are not allowed until the client confirms that he or she has read the warning and is aware of the risks. To confirm, the client should check "I am aware of the risks and I wish to trade high risk investment products". This warning is displayed once per session of the terminal. The next time it will appear after the restart of the terminal.

![Risk warning](/en/docs/mt4/administrator/img/high_risk_warning.png "Risk warning")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The risk warning is not displayed for <a href="/en/docs/mt4/administrator/administration/ug_groups/group_types#demo" class="topiclink">demo accounts</a>.</span></p></td></tr></tbody></table>

### Selecting News Language [#](ug_groups#language)

News sent to the clients from a particular group can be filtered. The language parameter is assigned to news in accordance with the [settings of the data feed](/en/docs/mt4/administrator/administration/ug_data_feeds#language) that translates the news. Also, the language news can be set when sending the news from the manager terminal.

The default parameter "Any Language" is set to the group. This means that the news for the client group will not be filtered by their language. To specify one or more news languages for the group of clients, click "Change" near the "News language" field.

![>Selecting News Language](/en/docs/mt4/administrator/img/news_language.png ">Selecting News Language")

To select a language, move it from the left part of the window to the right one using the mouse or the corresponding buttons. Up eight languages can be selected. If more than eight languages are selected, the "Any Language" parameter is automatically set.

## User Group Detailed Setting in the Archiving Tab [#](ug_groups#group_archiving)

![Archiving Tab](/en/docs/mt4/administrator/img/win_group_archiving.png "Archiving Tab")

-   Inactivity period — inactivity period (time elapsed after the latest connection, in days), after its expiration the account and its trade positions will be moved to the archive (minimum permissible value is 90 days);
-   Maximum balance — the highest balance value for accounts to be moved to the archive database;
-   Archive deleted pendings older — enabling/disabling the archivation of deleted pending orders. To enable this option, specify the age (in months), older than which deleted pendig orders should be archived.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Accounts that belong to demo*, manager and coverage groups are not archived. For deleting old and unused demo accounts the <a href="/en/docs/mt4/administrator/administration/ug_options" class="topiclink">Time of demo</a> options is provided.</span></li><li class="p_tableatten"><span class="f_tableatten">Archivation of deleted pending orders is performed at the same time as other archivations: every Sunday during <a href="/en/docs/mt4/administrator/administration/ug_options#optimization" class="topiclink">the optimization time</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">See the <a href="https://support.metaquotes.net/en/articles/148" target="_blank" class="weblink">"What To Do with Accounts of Inactive Clients?"</a> article for more detailed instructions on working with archiving.</span></li></ul></td></tr></tbody></table>

## User Group Detailed Setting in the Margins Tab [#](ug_groups#group_margins)

![Margins Tab](/en/docs/mt4/administrator/img/win_group_margins.png "Margins Tab")

-   Margin Call Level — the level of warnings;
-   Stop Out Level — the level of removing positions;

Margin call level in percentage terms is calculated as follows:

MC = Equity / Margin \* 100

Margin call level in monetary terms is equal to equity:

MC = Equity

If the current level lies under Margin Call level, the account will get to the alert section appearing in the dealer's Margin Calls window. If the level reaches the point lower than Stop Out level, the most unprofitable position will be closed on accounts quoted automatically, as for those quoted by a dealer, a request will be sent to the latter one for closing the most unprofitable position (but dealer can close any other position of the client at the dealer's will).

A special comment is added to the orders closed as a result of Stop Out. For example, "\[so/a: -135.0% -2430.0/1800.0\]":

-   so — StopOut process.
-   /a — executed by manager automation.
-   \-135.0% — level of margin requirement.
-   \-2430.0 — current equity.
-   1800.0 — current margin.

As a free margin calculation alternative considering profits/losses of already opened positions the Free Margin parameter is used:

-   do not use unrealized profit — open positions will not be taken into consideration at all;
-   use unrealized profit/loss — use both profit and loss;
-   use unrealized profit — use only profit;
-   use unrealized loss — use only loss.

Virtual credit to be used by traders provided they do not have enough cash resources is indicated in the "Virtual Credit" field. If a trader wants to withdraw his/her money, this request will not apply to this credit given to client. And Margin Call levels will also be calculated on the money put on the account but without considering the credit sum.

Option "Skip fully hedged accounts when checking for stop out" allows to skip accounts with completely hedged positions (with zero margin requirements) when checking for stop out. If this option is unchecked, the accounts having completely hedged positions (with zero margin requirements) and negative equity (balance plus unrealized profits/losses) will get into stop out.

Option "Calculate hedged margin using larger leg" enables the mode of calculation of margin using the larger position. For example, if there are two hedging positions of one symbol, but with different volumes - sell 1.0 EURUSD at 1.21200 and buy 2.0 EURUSD at 1.21300, then the total margin will be equal to the margin of the larger position (buy 2.0 EURUSD at 1.21300).

## User Group Detailed Setting in the Securities Tab [#](ug_groups#group_securities)

This inlay contains the list of all instruments (symbols) available for a given group.

![Securities Tab](/en/docs/mt4/administrator/img/win_group_securities.png "Securities Tab")

To set instruments in more detail double-click the desired group.

![Detailed Setting of Financial Instruments](/en/docs/mt4/administrator/img/win_group_securities_det.png "Detailed Setting of Financial Instruments")

-   Enable — enabling/disabling of a group of instruments;
-   Trade — enabling/disabling to trade with the instruments of the group;
-   Use Confirmations in REQUEST Mode — requesting additional confirmations of trade operations from the dealer in Request execution mode;
-   Execution — the orders execution mode.

-   -   Manual only, without any automation — dealer's manual order execution mode;
    -   Automatic only — automatic orders execution mode;
    -   Manual, but automatic if no dealers online — the orders execution mode is chosen depending on the dealer's activity. If the dealer is not active within 3 min, he/she will be disconnected, and the server switches to the automatic quotation mode. But, as soon as the dealer's request arrives, the execution will be performed manually again.

-   Spread difference — shows how the financial instrument spread for a specific user group differs from [instruments group basic spread](/en/docs/mt4/administrator/administration/ug_symbols#spread) ;
-   Maximum deviation — maximum admissible deviation from the current price in the client's request (applies only to Instant Execution). If the request for execution of an operation exceeds this value, the request will be declined, and the client will receive the "Requote" message;
-   Do not check free margin after dealer's answer — do not recheck free margin after the dealer's answer, the check of the available free margin will only be made before sending the request to the dealer;
-   Fast confirmation on IE with deviation specified — fast confirmation of the client's order in Instant Execution. This option is enabled by default: if the price given by dealer meets the deviation required by the client, the order will be executed by the server automatically. If the fast confirmation is disabled and the price given by dealer meets the deviation given by the client, then the order will be corrected according to the dealer's prices and returned to the dealer again;

### Close by

-   Enable — enabling/disabling use of the command to close two orders to the contrary on the same instrument. Having enabled this option, the client terminal can send a command to the server to close two orders in contrary at the same time, the resulting rest being calculated;
-   Multiple close by orders — enabling/disabling use of the command to close all overlapping orders on the same instrument. Having enabled this option, the client terminal can send a command to the server to close all overlapping orders at the same time, the resulting rest being calculated;
-   Auto close-out — automatic closing of the counter positions at the end of day. The following variants are available:

-   -   None, do not use auto close-out at the end of day — the counter positions will not be closed at the end of a day;
    -   HIHI, highest sell against highest buys — a sell position with the highest profit will be closed by a buy position with the highest profit;
    -   LOLO, lowest sells against lowest buys — a sell position with the lowest profit will be closed by a buy position with the lowest profit;
    -   HILO, highest sells against lowest buys — a sell position with the highest profit will be closed by a buy position with the lowest profit;
    -   LOHI, lowest sells against highest buys — a sell position with the lowest profit will be closed a buy position with the highest profit;
    -   FIFO, fisrt bought/sold against first sold/bought — the earliest buy/sell position will be closed by the earliest sell/buy position;
    -   LIFO, last bought/sold against first sold/bought — the latest buy/sell position will be closed by the earliest sell/buy position;
    -   Intraday followed by FIFO — the same as FIFO but the position to be closed by is searched within the current day at first.

### Lots

-   Minimum is the minimum permitted amount of a lot;
-   Maximum is the maximum permitted amount of a lot;
-   Step is the size of the object changing steps;

### Commissions

-   Standard is standard commission (in the currency of the group deposit, in points, or in percentage; for an operation or for a lot);
-   Taxes — taxes to commission (in percentage);
-   Agent Points means entering the commission in the agent's account (in the deposit currency of the group or in points);

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: It is not necessary for the clients of an agent to operate with the same deposit currency as the agent. The commission is converted at the current rates.</span></p></td></tr></tbody></table>

## User Group Detailed Setting in the Symbols Tab [#](ug_groups#group_symbols)

This inlay is intended for installation of individual values of swaps and margin for the selected group.

![Symbols Tab](/en/docs/mt4/administrator/img/win_group_symbols.png "Symbols Tab")

You can add, modify or delete the individual settings of the symbols using the commands of the context menu of the symbols list.

![Symbols](/en/docs/mt4/administrator/img/win_group_symbols_prop.png "Symbols")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The maximum number of instruments that can be added in the Symbols tab is 128.</span></p></td></tr></tbody></table>

## User Group Detailed Setting in the Report Tab [#](ug_groups#group_reports)

This inlay is intended for managing reports.

![Reports Tab](/en/docs/mt4/administrator/img/win_group_report.png "Reports Tab")

-   Enable — enabling/disabling to generate daily reports;
-   SMTP Server — the mail server address through which the reports will be distributed;
-   Templates path — template directory used when generating the specific report. This field remains empty by default, i.e. templates contained in the "confirms" in the server directory are used. If it is necessary to use custom templates for this group only the subdirectory name must be given which contains these templates (modified confirmation.htm and statements.htm files). For example, the subdirectory "my\_custom\_templates" inside of "confirms" in the server directory is created, and modified template files of confirmation.htm and statements.htm are placed in the subdirectory "my\_custom\_templates". In this case, my\_custom\_templates must be given in the "Templates path" field;
-   SMTP Login — login to send emails;
-   SMTP Password —password for sending emails through SMTP server;
-   Support email — email address to be put in the outgoing reports;
-   Copy reports to support — send a copy of each of daily report to the mailbox specified in the "Support email" field;
-   Signature — signature at the bottom of each report.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For successful generation of reports, the "Support email" field must be filled out.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Daily reports are not generated for <a href="/en/docs/mt4/administrator/administration/ug_accounts#personal" class="topiclink">disabled accounts</a>.</span></li></ul></td></tr></tbody></table>

You can find more detailed information concerning reports in the article ["Purpose and Functions of MetaTrader SendMail"](https://support.metaquotes.net/en/articles/12) in [Support Center](https://support.metaquotes.net).

[Securities](/en/docs/mt4/administrator/administration/ug_securities)

[Group Types](/en/docs/mt4/administrator/administration/ug_groups/group_types)