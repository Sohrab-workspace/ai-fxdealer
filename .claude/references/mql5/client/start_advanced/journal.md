# Platform Logs

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/journal

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Platform Logs

# Platform Logs

Almost all actions performed are logged in the platform journals. The logs reflect all important events: synchronization with the provider's account during copy trading, hosting migration results, details of purchases from the Market, and much more.

Two types of logs are available in the platform:

-   Experts Journal is displayed on the Experts tab of the Toolbox window. It contains information about the running indicators and Expert Advisor, including opening/closing of positions, modification of orders, Expert Advisor alerts and comments, etc.
-   Platform logs are shown on the Journal tab of the Toolbox window. It contains information about the recorded actions of the trader and platform for the current session. Information about the platform start and all events during its operation including execution of all trade operations are displayed here.

![Journals are displayed on the Experts and Journal tabs of Toolbox](/en/docs/mt5/client/img/journal.png "Journals are displayed on the Experts and Journal tabs of Toolbox")

Journal logs are represented in a table with the following fields:

-   Time — the date and time of the event. Specified according to the time zone on the user's computer.
-   Source — event type: Network, Alert, HistoryBase, Experts, the name of a separate Expert Advisor or indicator, etc.;
-   Message — description of the event.

Events are divided into several types and marked by special icons:

-   ![Information](/en/docs/mt5/client/img/journal_info_icon.png "Information") — informational message;
-   ![Warning](/en/docs/mt5/client/img/journal_warning_icon.png "Warning") — warning;
-   ![Error](/en/docs/mt5/client/img/journal_error_icon.png "Error") — error message.

The following commands can be run from the context menu of this tab:

-   ![Open](/en/docs/mt5/client/img/open_offline_icon.png "Open") Open — open the folder that contains the journal log files. Besides that, when this command is executed, all current journal entries are saved in log files. The platform log files are stored in the Logs directory, and Expert log files are saved in MQL5\\Logs. File names correspond to the date of journal generation — YYYYMMDD.LOG. Previous logs on the platform operation can be reviewed from these files, while the "Journal" tab only contains the latest entries;
-   ![Copy](/en/docs/mt5/client/img/copy_button.png "Copy") Copy — copy a row with information to clipboard for use in other applications;
-   ![Send](/en/docs/mt5/client/img/send_icon.png "Send") Send — send the current log file to an administrator by the internal mailing system. Execution of this command opens a message creating window, to which the selected file is attached;
-   ![Alerts](/en/docs/mt5/client/img/alert_icon.png "Alerts") Alerts (in the Experts journal only) — open the window of [Expert Advisor alerts](/en/docs/mt5/client/start_advanced/journal#expert_alerts);
-   ![Viewer](/en/docs/mt5/client/img/viewer_icon.png "Viewer") Viewer — open a special program to view log files;
-   ![Clear](/en/docs/mt5/client/img/delete_icon.png "Clear") Clear — remove current logs from the tab. Logs are not physically removed from the computer, they are still available in log files;
-   Auto Scroll — if this option is enabled, the list of logs is scrolled to the last one every time a new entry appears in the journal;
-   Auto Arrange — if this option is enabled, the size of table columns is selected automatically in case the window size is changed;
-   Grid — enable/disable table field separators.

## Log Viewer [#](journal#viewer)

The platform includes a special program for viewing log files. It can be opened by selecting "Viewer" in the context menu of the Journal and Experts tabs.

![Search for entries and filter them using the log viewer](/en/docs/mt5/client/img/journal_viewer.png "Search for entries and filter them using the log viewer")

A search bar (search is performed by exact words, case sensitive) and the filter of entries (Full, No connection, Errors only) are available at the top of the window. You can specify time range for search. After specifying all the necessary search condition, click "Request".

The following commands are available in the context menu of the log viewer:

-   ![Open](/en/docs/mt5/client/img/open_offline_icon.png "Open") Open — open the folder that contains the journal log files. Besides that, when this command is executed, all current journal entries are saved in log files. The platform log files are stored in the Logs directory, and export log files are saved in MQL5\\Logs. File names correspond to the date of journal generation — YYYYMMDD.LOG. Previous logs on the platform operation can be reviewed from thee files, while the "Journal" tab only contains the latest entries;
-   ![Copy](/en/docs/mt5/client/img/copy_button.png "Copy") Copy — copy a row with information to clipboard for use in other applications;
-   ![Send](/en/docs/mt5/client/img/send_icon.png "Send") Send — send the current log file to an administrator by the internal mailing system. Execution of this command opens a message creating window, to which the selected file is attached;
-   ![Search](/en/docs/mt5/client/img/find_icon.png "Search") Search — open the search window.
-   ![Find Next](/en/docs/mt5/client/img/find_next_icon.png "Find Next") Find next — find the next item matching the search query.
-   ![Find Previous](/en/docs/mt5/client/img/find_previous_icon.png "Find Previous") Find Previous — find the previous item matching the search query.
-   Auto Scroll — if this option is enabled, the list of logs is scrolled to the last one every time a new entry appears in the journal;
-   Auto Arrange — if this option is enabled, the size of table columns is selected automatically in case the window size is changed;
-   Grid — enable/disable table field separators.

### Search in Logs [#](journal#search)

To find a word or phrase in the records displayed, click "![Search](/en/docs/mt5/client/img/find_icon.png "Search") Search" in the context menu or press "Ctrl+F".

![Enter a word or phrase to search](/en/docs/mt5/client/img/logs_search.png "Enter a word or phrase to search")

It contains the following commands and parameters:

-   Find — field to enter the search word or phrase;
-   Match Whole Word Only — this option allows to search by a particular word form, only the word or phrase that exactly match the search query will be found;
-   Match Case — enable/disable case sensitivity when executing the search query;
-   Direction up/down — Enable search up or down from the current cursor position;
-   Find Next — move to the next found item. The same command can be executed by pressing F3;
-   Cancel — close the window.

## Alerts of Expert Advisors [#](journal#expert_alerts)

If the Expert Advisor code provides generation of alerts using the Alert(); function, a special dialog appears when the alerts trigger:

![Using alerts, an Expert Advisor can notify a trader about significant events](/en/docs/mt5/client/img/expert_alert.png "Using alerts, an Expert Advisor can notify a trader about significant events")

The message of the current alert appears at the top of the window. The current and the previous alerts of the Expert Advisor are shown in the table below:

-   Date and time;
-   Name of the MQL5 application, chart symbol and timeframe;
-   Alert message.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Using alerts, an Expert Advisor can notify a trader about significant events. The window of alerts opens even if the window of the platform is minimized.</span></p></td></tr></tbody></table>

[Live Update](/en/docs/mt5/client/start_advanced/autoupdate)

[Task Manager](/en/docs/mt5/client/start_advanced/task_manager)