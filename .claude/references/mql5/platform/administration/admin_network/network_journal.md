# Journal

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_journal

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
                -   [Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)
                -   [Hosted Access Servers](/en/docs/mt5/platform/administration/admin_network/hosted_access_server)
                -   [Restarting and Stopping Servers](/en/docs/mt5/platform/administration/admin_network/restart)
                -   [Managing Machines](/en/docs/mt5/platform/administration/admin_network/manage_machines)
                -   [Status](/en/docs/mt5/platform/administration/admin_network/network_status)
                -   [Monitor](/en/docs/mt5/platform/administration/admin_network/network_monitoring)
                -   [Journal](/en/docs/mt5/platform/administration/admin_network/network_journal)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Network cluster](/en/docs/mt5/platform/administration/admin_network)Journal

# Journal

On this tab you can view logs of work of the platform components.

![Journal](/en/docs/mt5/platform/img/network_journal.png "Journal")

In the journal, entries are marked by different icons:

-   ![Error](/en/docs/mt5/platform/img/journal_error_icon.png "Error") — error message.

-   ![Critical error](/en/docs/mt5/platform/img/journal_critical_error_icon.png "Critical error") — critical error message.

-   ![Warning](/en/docs/mt5/platform/img/journal_warning2_icon.png "Warning") — warning.
-   ![Information](/en/docs/mt5/platform/img/journal_info_icon.png "Information") — information message.
-   ![Separator](/en/docs/mt5/platform/img/journal_book_icon.png "Separator") — day separator in the journal. In the IP field of such entries the total size of logs generated for the day is shown.

Log files for all servers except the backup server can be found at \[server installation directory\]\\logs. The backup server logs are available at \[backup server installation directory\]\\logs\\mtbackup. The files are stored in a readable format and can be opened with any text editor.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Different types of errors returned by the server are described in the <a href="/en/docs/mt5/platform/components/trade_server/returned_errors" class="topiclink">separate section</a>.</span></p></td></tr></tbody></table>

## Requesting Entries [#](network_journal#request)

You can also request only some of journal entries. In order to do this, enter the searched word in the search field. Additionally you can specify the time period and type of log request:

-   Full — all types of journal entries;
-   Without logins — all messages except the information about the connections of users to a server;
-   Errors only — only messages about errors.

You can also select the type of events:

-   All — all types of events, except LiveUpdate;
-   Configuration — changes in the server configuration;
-   System — system events;
-   Network — events connected with the network activity;
-   History — events connected with [history data](/en/docs/mt5/platform/administration/admin_charts);
-   Accounts — events connected with [accounts](/en/docs/mt5/platform/administration/admin_accounts) on the server;
-   Trades — events connected with trade operations on the server;
-   API — events connected with work via API;
-   LiveUpdate — events connected with [update](/en/docs/mt5/platform/administration/admin_update) of the platform components;
-   Report Mailer — events connected with sending [daily reports](/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports) via e-mail;
-   Failover — events connected with [automatic switching to a backup server](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto).

-   Switch — entries from a copy of the backup server log for the last day ([\*.log.failover](/en/docs/mt5/platform/components/backup_server/backup_server_features#journal)). This request type is available only for trade and history servers.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_Normal"><span class="f_tableatten">Please note that the request of logs is performed only by the server that is chosen in the tree to the left.</span></li><li class="p_tableatten"><span class="f_tableatten">The LiveUpdate logs are not displayed when choosing the "All" type of events, because they are stored in a separate file (mt5srvupdater.log).</span></li><li class="p_tableatten"><span class="f_tableatten">For a more accurate request of journal entries, use <a href="/en/docs/mt5/platform/administration/admin_network/network_journal#keywords" class="topiclink">keywords</a>.</span></li></ul></td></tr></tbody></table>

To receive logs press "Request" or execute the same command of the [context menu](/en/docs/mt5/platform/administration/admin_network/network_journal#context). After that the logs will be displayed as a table with  the following fields:

-   Time — time when the event occurred;
-   IP — IP address, with which this event id connected;
-   Message — description of the event.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">If the journal file was manually edited on the server, then the first edited entry and all coming after it will be highlighted red.</span></p></td></tr></tbody></table>

## Request Language

To request entries from the [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) of the server operation, keywords and logic operators are used. It will help to easily find the required information about different aspects of the platform functioning.

### Keywords [#](network_journal#keywords)

To analyze the server journal use any words and word phrases that can be found in server logs. You should remember that if you request the full journal without the request line, you will not receive the whole server journal, because the volume of given information is limited (approximately up to 30000 lines of the server journal).

To analyze separate situations use the following key words:

-   Startup — information about server initialization and restart;
-   Exit — information about server stop;
-   Synchronization — [synchronization](/en/docs/mt5/platform/administration/admin_synchronization) of history. Possible errors: no connection with the server you want to synchronize with;
-   ClientBase — information on work with the base of [accounts](/en/docs/mt5/platform/administration/admin_accounts). Possible errors: incorrect base header, error writing/reading from disk, not enough memory;
-   History — information on work with history data of a symbol. Possible errors: incorrect base header, error writing/reading from disk, incorrect quotes in the base;
-   datafeed or 'Datafeed name'  — activation and work of [datafeeds](/en/docs/mt5/platform/administration/admin_feeds). Possible errors: error creating feeder, incorrect timeout stop, error reading data from the feeder;
-   Filter — filtering of quotes (quotes no passed to the server);
-   Mail — work with the [mail base](/en/docs/mt5/platform/administration/mail). Possible errors: incorrect base header, error writing/reading from disk, not enough memory;
-   Monitor — performance measuring and work with the [monitoring](/en/docs/mt5/platform/administration/admin_network/network_monitoring) base. Possible errors: incorrect base header, impossibility to obtain information about the PC performance;
-   News — [news base](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news). Possible errors: incorrect header or base version;
-   Access, Common, Feeders, Groups, Managers, SymbolGroups, HistorySync, Holidays — files of corresponding server configurations. Possible errors: read/write error;
-   Network — [server](/en/docs/mt5/platform/administration/admin_network) operation. Possible errors: port already busy;
-   LiveUpdate — work of the [LiveUpdate](/en/docs/mt5/platform/administration/admin_update) system and its base;
-   block — block setting and removing by [antiflood control](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#antiflood);
-   '...' — to analyze actions on a certain account, specify the account number in single quotes. For example: '12345';
-   #... — to analyze actions on a certain [order](/en/docs/mt5/platform/administration/admin_orders) or [deal](/en/docs/mt5/platform/administration/admin_deals), specify this order with symbol "#". For example: #111222.
-   login — connection with an account to the server. These entries contain information about connection: time, type (client, manager, web, etc.), terminal build and other details.
-   logout — disconnection of an account from the server.

### Logical Operators

You can specify key words joined by logical operators in the request line. The search line supports the following logical operators:

-   | (or) — logical operator OR allows selecting journal lines that contain either the first or the second key word;
-   & (and) — logical operator AND allows selecting only those journal lines that contain both the first and the second key words. A space between key words is considered logical operator AND;
-   ^ (-, not) — logical operator of exclusion NOT allows selecting journal lines that do not contain the specified key word.

The possibility to create a precise request line using logical operators allows quickly and efficiently select required logs. For example, line "'5'&login" allows selecting the journal entries about the logging in of a manager with login 5.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The request is case sensitive. For example, search by "Session" and "session" will give different results.</span></p></td></tr></tbody></table>

## Context Menu [#](network_journal#context)

The journal context menu contains the following commands:

-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — request logs;
-   Search — using this submenu, you can easily form new requests on the basis of an already found entry in the journal:

-   ![Account](/en/docs/mt5/platform/img/accounts_icon.png "Account") Account — copy an account from the found entry to the request field of the journal;
-   ![Order](/en/docs/mt5/platform/img/orders_icon.png "Order") Order — copy an order ticket from the found entry to the request field of the journal;
-   ![Deal](/en/docs/mt5/platform/img/deals_icon.png "Deal") Deal — copy a deal ticket from the found entry to the request field of the journal
-   ![Symbol](/en/docs/mt5/platform/img/symbols_icon.png "Symbol") Symbol — copy a symbol name from the found entry to the request field of the journal;
-   ![Computer ID](/en/docs/mt5/platform/img/journal_cid_icon.png "Computer ID") Computer ID — copy a unique computer identifier (CID) the found entry to the request field of the journal;
-   ![IP](/en/docs/mt5/platform/img/journl_ip_icon.png "IP") IP — copy an IP address the found entry to the request field of the journal.
-   Copy As — this command allows copying information from the journal to the clipboard. There are three variants of how to save it: "![Save As Lines](/en/docs/mt5/platform/img/copy_button.png "Save As Lines") As Lines", "As List of Logins", "As List of IP Addresses";
-   Firewall — enables the quick addition of [firewall rules](/en/docs/mt5/platform/administration/security/admin_access) without leaving the journal page. Select one or more log lines containing the required addresses in the "IP" field. For example, these can be logs about anti-flood control activation. Next, select "Allow" or "Block" in the menu. This will add a new record containing the selected addresses to the end of the list of firewall rules. The "Allow" command adds rules with the "Permit always" type.  
    When adding the rule, the system searches for the selected addresses in existing rules. If the address to be blocked (allowed) has already been blocked (or allowed), a new rule is not created.
-   Export — export the requested logs in a CSV or HTML file;
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — search through requested logs;
-   Auto arrange — If this option is enabled, the size of columns is selected automatically;
-   Grid — show/hide grid to separate fields;
-   Columns — show/hide columns of IP and Message in the Journal.

[Monitor](/en/docs/mt5/platform/administration/admin_network/network_monitoring)

[Integrations](/en/docs/mt5/platform/administration/integration)