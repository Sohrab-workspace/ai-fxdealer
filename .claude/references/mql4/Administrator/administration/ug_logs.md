# Server Journal

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_logs

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
                -   [State Monitoring](/en/docs/mt4/administrator/administration/ug_logs/journal_monitoring)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Server Journal

# Server Journal

All operations performed and all events are stored in special statistical logs representing text files and being kept in the /LOGS directory. The "Journal" section allows to look through these records. Here you can also view the logs of the platform's service components.

![Journal](/en/docs/mt4/administrator/img/br_logs.png "Journal")

The date and time of the event are written in the "Time" field. "IP" is the address from which the action was performed. No entry in this field means that the action was performed by the server itself. The events are described in the "Message" column. The icons in the time column allow to select various types of entries: ![Error Messages](/en/docs/mt4/administrator/img/ic_logs_error.png "Error Messages") show information about errors; ![Warnings](/en/docs/mt4/administrator/img/ic_logs_warning.png "Warnings") show warnings and alerts; ![Common Messages](/en/docs/mt4/administrator/img/ic_logs_common.png "Common Messages") show normal messages.

To find an entry by a given criterion among the results of the database request, you can use the "Find" window. This window can be activated through "Ctrl+F" buttons.

Control log request items are located at the bottom of the window (from left to right):

-   search field where the unique key words can be set;
-   scanning mode:

-   Standard - all messages except for authorization information.
-   Logins - authorization messages.
-   Trades - messages about trade operations.
-   Errors - only error messages.
-   Full - all messages.
-   LiveUpdate - the log of the platform components update module (mtsrvupdate.exe).
-   SendMail - the log of the module for sending reports to clients (mtsendmail.exe).
-   Failover - the log of the the utility for real time data backup (MetaTrader 4 WatchDog).

-   pre-defined request periods: Today (the current day), Last 3 Days (the last three days), Last Week (the last week), Last Month (the last month), Last 3 Months (the last three months), and Last 6 Months (the last six months);
-   you can indicate the request period manually in two latter fields: the first one means the beginning of the request period, and the second one is the end of that period.

Keywords united with logical operators can be specified as the string in the search field. The search string supports the following logical operators:

-   | (or) — logical operator OR, allows to select lines in journal that contain either the first or the second keyword;
-   & (and) — logical operator AND, allows to select lines in journal if they contain both the first and the second keyword, the space between keywords is considered as AND operator;
-   ! (^, not) — logical operator of avoidance (NOT), allows to select lines in journal that do not contain the keyword to be avoided.

Making the search string as precise as possible with the assistance of logical operators allows to select the required lines in journal effectively. For example, the search line of "'1'|'4'|'5' and (" allows to select dealers' replies from journal where market prices are specified, "!'5' and reject" — rejections of all dealers except for that having login of '5'.

You can also use keywords to find messages concerning certain events. Examples of keywords are given in the "[What request lines can be used for analyzing a server journal?](https://support.metaquotes.net/en/articles/1082)" article.

After you have indicated all desired request parameters, press the "Request" button. Considering that the journal can contain hundreds of thousands of entries, it is recommended to formulate the request as accurately as possible. This will allow to shorten the search time and to find a desired entry faster. The "Save As" context menu command allows to save the resulting log in CSV or HTML format.

The context menu allows to execute the following commands:

-   Request — request logs from the server;
-   Technical Details — receive details of IP address connection;
-   Add to Black List — [lock](/en/docs/mt4/administrator/administration/ug_access) IP address;
-   Search — using this submenu, you can easily form new requests on the basis of an already found entry in the journal:

-   Account — copy an account from the found entry to the request field of the journal;
-   Order — copy an order ticket from the found entry to the request field of the journal;
-   Symbol — copy a symbol name from the found entry to the request field of the journal;
-   IP — copy an IP address the found entry to the request field of the journal.

-   Copy As:

-   -   Lines — copy the selected strings in the log to the clipboard;
    -   List of Logins — copy only the logins from the selected strings in the log to the clipboard;
    -   Lines of IP Addresses — copy only the IP addresses from the selected strings in the log to the clipboard;

-   Find — find a string by the criterion in the requested log;
-   Find Next — find the next string;
-   Save As — save the requested log to the file.

[Ticks](/en/docs/mt4/administrator/administration/ug_ticks)

[State Monitoring](/en/docs/mt4/administrator/administration/ug_logs/journal_monitoring)