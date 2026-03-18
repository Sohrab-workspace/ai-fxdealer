# Files and Folders

> Source: https://support.metaquotes.net/en/docs/mt5/manager/beginning_advanced/structure

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
            -   [Installing the Terminal](/en/docs/mt5/manager/beginning_advanced/installation)
            -   [Files and Folders](/en/docs/mt5/manager/beginning_advanced/structure)
            -   [Extended Authentication](/en/docs/mt5/manager/beginning_advanced/extended_authorization)
            -   [One Time Passwords - 2FA/TOTP](/en/docs/mt5/manager/beginning_advanced/otp)
            -   [Auto Update](/en/docs/mt5/manager/beginning_advanced/liveupdate)
            -   [Data Export](/en/docs/mt5/manager/beginning_advanced/export)
            -   [Terminal Deinstallation](/en/docs/mt5/manager/beginning_advanced/deinstallation)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[For Advanced Users](/en/docs/mt5/manager/beginning_advanced)Files and Folders

# Files and Folders

This section describes the storage structure of directories and files of the Manager terminal. In the [guest mode](/en/docs/mt5/manager/start#guest) of the terminal launch, changeable and unchangeable files of the terminal are stored separately.

## Unchangeable files

These files are located in the directory /Program Files/Terminal/, they include:

-   mt5manager.exe — executable file of the Manager terminal.
-   Uninstall.exe — program for the terminal [deinstallation](/en/docs/mt5/manager/beginning_advanced/deinstallation).
-   /help/\*.chm — built-in help files of the terminal.

## Changeable files

The main directory of the terminal contains three folders: bases, config, logs. A special command is used in the terminal for quick access to data storage location — "![Open Data Folder](/en/docs/mt5/manager/img/open_data_folder_button.png "Open Data Folder") Open Data Folder" located in the [File](/en/docs/mt5/manager/main_menu#file) menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">All text files are of Unicode format. Use appropriate software to edit them.</span></p></td></tr></tbody></table>

The bases directory contains terminal databases arranged by trade servers, and some settings:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders and files</span></p></th><th class="table" style="width:200px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th><th class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Sub-folders</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" rowspan="4" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Default</span></p></td><td class="table" rowspan="4" style="width:200px;"><p class="p_fortable"><span class="f_fortable">Default folder of the terminal database</span></p></td><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Certificates</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">*.pfx certificate files<a name="certificate" class="hmanchor"></a>.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">History</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">History data of financial instruments. Each symbol is stored in a separate directory that also contains ticks.dat file with tick data.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Mail<a name="mail" class="hmanchor"></a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">All <a href="/en/docs/mt5/manager/communication#mailbox" class="topiclink">emails</a> received or sent from the terminal. Mail databases are stored in *.dat files. For each account opened in the terminal, a separate file is created for storing emails. For example, mail-xxxxx.dat, where xxxxx </span><span class="f_ol">is an account number.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">News</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">One news.dat file containing the database of all <a href="/en/docs/mt5/manager/toolbox#news" class="topiclink">news</a> ever received in the terminal from a selected trade server.</span></p></td></tr><tr class="table"><td class="table" rowspan="4" style="width:125px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">MetaTrader 5 Server 1 — N</span></p></td><td class="table" rowspan="4" style="width:200px;"><p class="p_fortable"><span class="f_fortable">Terminal database folders for different trade servers</span></p></td><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Orders</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The current base of <a href="/en/docs/mt5/manager/orders" class="topiclink">orders</a> available to a manager account. Bases of orders are stored in separate orders-xxxxxx.dat files for each account. Here xxxxxx </span><span class="f_ol">is a number of the manager account.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Positions</span></p></td><td class="table"><p class="p_fortable"><span class="f_ol">The current base of <a href="/en/docs/mt5/manager/positions" class="topiclink">positions</a> available to the manager account. Bases of positions are stored in separate positions-xxxxxx.dat files for each account. Here xxxxxx is a number of the manager account.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Symbols</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">selected-xxxxx.dat file contains the symbol base currently selected in the <a href="/en/docs/mt5/manager/market_watch" class="topiclink">Market Watch</a> window. symbols-xxxxx.dat file contains the common database of symbols available on this trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Users</span></p></td><td class="table"><p class="p_fortable"><span class="f_ol">The current base of <a href="/en/docs/mt5/manager/accounts" class="topiclink">accounts</a> available to a manager account. Bases of accounts are stored in separate users-xxxxxx.dat files for each account. Here xxxxxx is a number of the manager account.</span></p></td></tr><tr class="table"><td class="table" style="width:125px; height:16px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">profiles</span></p></td><td class="table" colspan="3" style="height:16px;"><p class="p_fortable"><span class="f_fortable">Files of the Market Watch window symbol <a href="/en/docs/mt5/manager/quotes_symbols#profile" class="topiclink">profiles</a> (*.prf).</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">alerts.dat</span></p></td><td class="table" colspan="3"><p class="p_fortable"><span class="f_fortable">The database of created <a href="/en/docs/mt5/manager/trade_alerts" class="topiclink">alerts</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">books.dat</span></p></td><td class="table" colspan="3"><p class="p_fortable"><span class="f_fortable">A list of currently open windows of request queues.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">dnslookups.dat</span></p></td><td class="table" colspan="3"><p class="p_fortable"><span class="f_fortable">IP addresses of the currently <a href="/en/docs/mt5/manager/online_accounts" class="topiclink">connected accounts</a> and name of hosts they are attached to.</span></p></td></tr></tbody></table>

config directory contains terminal configuration files:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">accounts.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The database of manager accounts, using which <a href="/en/docs/mt5/manager/connect" class="topiclink">connections</a> to server were established.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">common.ini</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/manager/settings" class="topiclink">Settings</a> of the Manager terminal.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5admin.ini</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">All configurations of the terminal interface, the last used values for window positions, etc.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">servers.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Parameters of the servers you <a href="/en/docs/mt5/manager/connect" class="topiclink">connect</a> to.</span></p></td></tr></tbody></table>

The logs directory contains files of the terminal journal and crash logs:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders and files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Crash/crash.log.*</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The /crash directory contains files of the terminal crashes. These files are automatically sent to the developer company to determine and eliminate their causes.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">yyyymmdd.log</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Files of the <a href="/en/docs/mt5/manager/toolbox#journal" class="topiclink">journal</a> that contain all the information about events occurring in the manager terminal. Terminal logs are stored in separate files for each day it runs. Here yyyy is a year, mm is a month, dd is a day.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><a name="dealing" class="hmanchor"></a><span class="f_fortable" style="font-weight: bold;">dealing.log</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The <a href="/en/docs/mt5/manager/dealing#journal" class="topiclink">journal</a> file of trade request processing by a dealer.</span></p></td></tr></tbody></table>

The templates directory contains mail and news templates:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders</span></p></th><th class="table" style="width:200px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th><th class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mail<a name="mail_templates" class="hmanchor"></a></span></p></td><td class="table" style="width:200px;"><p class="p_fortable"><span class="f_fortable">Email templates.</span></p></td><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">*.htm</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">HTM files of <a href="/en/docs/mt5/manager/communication#mail_template" class="topiclink">mail templates</a>, which were saved by the appropriate command in the email writing window.</span></p></td></tr><tr class="table"><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">news<a name="news_templates" class="hmanchor"></a></span></p></td><td class="table" style="width:200px;"><p class="p_fortable"><span class="f_fortable">News templates.</span></p></td><td class="table" style="width:125px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">*.htm</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">HTM files of <a href="/en/docs/mt5/manager/toolbox#news_template" class="topiclink">news templates</a>, which were saved by the appropriate command of the news sending window.</span></p></td></tr></tbody></table>

## Database Security

All terminal databases, including saved accounts (servers.dat) and mail data, are encrypted and protected against use in other platforms. The databases are bound to the operating system user account and the specific hardware configuration of the computer. If an attempt is made to transfer and open them on another machine, they will be automatically destroyed.

[Installing the Terminal](/en/docs/mt5/manager/beginning_advanced/installation)

[Extended Authentication](/en/docs/mt5/manager/beginning_advanced/extended_authorization)