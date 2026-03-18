# Trade Server Journal

> Source: https://support.metaquotes.net/en/docs/mt5/manager/server_journal

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
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
            -   [Spread, Commission and Swap](/en/docs/mt5/manager/groups)
            -   [Margin](/en/docs/mt5/manager/margin)
            -   [Managing Plugins](/en/docs/mt5/manager/plugins)
            -   [Trade Server Journal](/en/docs/mt5/manager/server_journal)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)Trade Server Journal

# Trade Server Journal

Managers are able to control the trade server operation requesting its journal. It provides data on accounts, trade operations, as well as changes in the platform settings, system and network events and much more. Open the Navigator, select the Servers section and go to the Journal tab.

![Journal](/en/docs/mt5/manager/img/journal.png "Journal")

Enter the search word or phrase, set the time interval you want to get the journal entries for, and click Request. Additionally, you can specify the time period and event type you want to receive.

Entry types:

-   Full — all types of journal entries;
-   Without logins — all messages except the information about the connections of users to a server;
-   Errors only — only error messages.

Event types:

-   All — all events except for LiveUpdate.
-   Configuration — changes in the server settings.
-   System — system events.
-   Network — events related to the network activities.
-   History — events related to history data.
-   Accounts — events related to [accounts](/en/docs/mt5/manager/accounts) on the server.
-   Trades — events related to [trade operations](/en/docs/mt5/manager/account_trading) on the server.
-   API — events related to working via API.
-   LiveUpdate — events related to the [update](/en/docs/mt5/manager/beginning_advanced/liveupdate) of the platform components.

Occurrence time, IP address (for example, a client's address) and a description are displayed for each event. Messages of different types have appropriate icons for more convenience:

-   ![Error](/en/docs/mt5/manager/img/journal_error_icon.png "Error") — error message.
-   ![Warning](/en/docs/mt5/manager/img/journal_warning2_icon.png "Warning") — warning.
-   ![Information](/en/docs/mt5/manager/img/journal_info_icon.png "Information") — information message.
-   ![Separator](/en/docs/mt5/manager/img/request_icon.png "Separator") — separator of days in the journal. In the IP field of such entries, the amount of generated logs for a selected day is specified.

The context menu allows you to easily apply refined queries for already found entries. Select a journal entry and click one of the available commands in the Search submenu:

-   ![Account](/en/docs/mt5/manager/img/accounts_icon.png "Account") Account — copy an account from the found entry to the request field of the journal.
-   ![Order](/en/docs/mt5/manager/img/orders_icon.png "Order") Order — copy an order ticket from the found entry to the request field of the journal.
-   ![Deal](/en/docs/mt5/manager/img/deals_icon.png "Deal") Deal — copy a deal ticket from the found entry to the request field of the journal.
-   ![Symbol](/en/docs/mt5/manager/img/symbols_icon.png "Symbol") Symbol — copy a symbol name from the found entry to the request field of the journal.
-   ![Computer ID](/en/docs/mt5/manager/img/journal_cid_icon.png "Computer ID") Computer ID — copy a unique computer identifier (CID) of a detected entry to the request field of the journal.
-   ![IP](/en/docs/mt5/manager/img/journl_ip_icon.png "IP") IP — copy an IP address the found entry to the request field of the journal.

After that, click Request.

The context menu also allows you to search for any text detected in entries, copy them to clipboard and save as HTML, CSV and LOG files.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For more accurate query, use <a href="/en/docs/mt5/manager/server_journal#keywords" class="topiclink">keywords</a> and <a href="/en/docs/mt5/manager/server_journal#operators" class="topiclink">logical operators</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">The platform update log (LiveUpdate) does not appear when you select All as an event type, because it is stored in a separate file.</span></li><li class="p_tableatten"><span class="f_tableatten">If the log file was manually edited on the server, the first edited entry and all of the following ones will be highlighted in red.</span></li></ul></td></tr></tbody></table>

## Keywords [#](server_journal#keywords)

For the analysis of the server log, you can use any words or phrases that can be found in the server journal. It should be borne in mind that the request of the entire journal without the request string will not lead to the receipt of the entire server log, because the maximum amount of the given data is limited (to about 30 000 lines of the server log).

For the analysis of specific situations, you can use the following keywords:

-   Startup — information about the initialization and restart of the server.
-   Exit — information about the server stops.
-   Synchronization — history synchronization. Possible errors: no connection to the server, synchronization with which is required.
-   Users — information about working with the database of [accounts](/en/docs/mt5/manager/accounts). Possible errors: invalid header of the database, error writing to disk/reading from disk, not enough memory.
-   History — information about working with history data of a symbol. Possible errors: invalid header of the database, error writing/reading, invalid quotes in the database.
-   datafeed or "Name of a data feed" — activation and operation of data feeds. Possible errors: error creating feeder, wrong timeout stop, error reading data from the feeder.
-   Filter — filtering of quotes (quotes not let through to the server).
-   Mail — work with the [mail database](/en/docs/mt5/manager/communication#mailbox). Possible errors: invalid header of the database, error writing/reading, not enough memory.
-   Monitor — measurement of performance and work with the database of the server operation monitoring. Possible errors: invalid header of the database, inability to obtain information about the computer performance.
-   News — [news database](/en/docs/mt5/manager/toolbox#news). Possible errors: invalid header or database version.
-   Access, Common, Feeders, Groups, Managers, SymbolGroups, HistorySync, Holidays — files of server configurations. Possible errors: error reading/writing.
-   Network — operation of the server. Possible errors: the port is already in use.
-   LiveUpdate — operation of the [LiveUpdate](/en/docs/mt5/manager/beginning_advanced/liveupdate) system.
-   block — blocking and unblocking by the anti-flood control.
-   '...' — to analyze actions by a specific account number, specify it in single quotes. For example: '12345'.
-   #... — to analyze actions by a specific [order](/en/docs/mt5/manager/orders) or [deal](/en/docs/mt5/manager/account_history#deals), specify this order with character "#". For example: #111222.

## Logical operators [#](server_journal#operators)

As a line in the request field, you can specify keywords combined using logical operators.

-   | (or) — logical operator OR, allows selecting log rows that contain either the first or the second keyword;
-   & (and) — logical operator AND, allows selecting only the log rows that contain both the first and the second words; a space between keywords is considered as the operator AND;
-   ^ (-, not) — logical operator of exclusion NOT, allows selecting log rows that do not contain an excluded keyword.

Making an exact search line using logical operators allows you to more effectively select the desired log entries. For example, the search line "'5'& login" allows you to select the journal entries about the logging in of the manager with login 5.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Search is case sensitive. For example, searching for "Session" and "session" will give different results.</span></p></td></tr></tbody></table>

[Managing Plugins](/en/docs/mt5/manager/plugins)

[Server Reports](/en/docs/mt5/manager/reports)