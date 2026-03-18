# Journal

> Source: https://support.metaquotes.net/en/docs/mt4/manager/reports_journal/ug_logs

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
    -   [Manager](/en/docs/mt4/manager)
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
            -   [Reports](/en/docs/mt4/manager/reports_journal/ug_reports)
            -   [History Reports](/en/docs/mt4/manager/reports_journal/ug_history_reports)
            -   [Groups of Accounts](/en/docs/mt4/manager/reports_journal/ug_report_group)
            -   [Journal](/en/docs/mt4/manager/reports_journal/ug_logs)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Reports and Journal](/en/docs/mt4/manager/reports_journal)Journal

# Journal

All operations and events are saved in special statistics journals representing text files. The "Journal" section allows to look through these records.

![Journal](/en/docs/mt4/manager/img/br_journal.png "Journal")

Date and time of the event are written in the "Time" field. "IP" is the address from which the action was performed. If there is no record in this field, it means that the actions was performed by the server itself. The events taken place are described in the "Message" column. Icons in the time column allow to select different types of records easily: ![Error Reports](/en/docs/mt4/manager/img/ic_logs_error.png "Error Reports") — error reports; ![Warnings](/en/docs/mt4/manager/img/ic_logs_warning.png "Warnings") — warnings; ![Standard Messages](/en/docs/mt4/manager/img/ic_logs_common.png "Standard Messages") — standard messages.

To find a necessary record according to a given criterion among the results of the request to database, the "Find" should be used. This window can be opened using "Ctrl+F" button combination.

Elements of log requests management are located at the bottom of the window (from left to right):

-   Search field where unique key words can be given;
-   The mode of view:

-   Standard - all messages except for authorization information.
-   Logins - authorization messages.
-   Trades - messages about trade operations.
-   Errors - only error messages.
-   Full - all messages.
-   LiveUpdate - the log of the platform components update module (mtsrvupdate.exe).
-   SendMail - the log of the module for sending reports to clients (mtsendmail.exe).
-   Failover - the log of the the utility for real time data backup (MetaTrader 4 WatchDog).

-   Preset request periods: Today (current day), Last 3 Days (the last 3 days), Last Week (the last week), Last Month (the last month), Last 3 Months (the last 3 months), and Last 6 Months (the last 6 months);
-   The request period can be given manually in the last two fields: the first field is for the beginning of the request period, the second one is for the request period end.

You can also use logical operators for requesting server logs: | (or), & (and), ! (exception).

After all required parameters of the request have been given the "Request" button must be pressed. Taking into consideration that server logs can consist of tens of thousands or hundreds of thousands records, it is recommended to formulate the request as accurately as possible. This will allow to shorten the search period, as well as to find the necessary record quicker and in the less amount of information. The "Save As" context menu command allows to save the formed log in CSV or HTML format.

The context menu allows to execute the following commands:

-   Request — request logs;
-   Account Details — open the window of account details;
-   Technical Details — receive the details of the account owner's connection;
-   Find — call the search window;
-   Search — using this submenu, you can easily form new requests on the basis of an already found entry in the journal:

-   Account — copy an account from the found entry to the request field of the journal;
-   Order — copy an order ticket from the found entry to the request field of the journal;
-   Symbol — copy a symbol name from the found entry to the request field of the journal;
-   IP — copy an IP address the found entry to the request field of the journal.

-   Copy — copy the selected entry to the clipboard;
-   Save — save the requested logs as the HTML file;
-   Auto Arrange — automatic arrangement of column sizes when window size is changed;
-   Grid — show/hide grid to separate columns;
-   Columns — select columns to be shown.

[Groups of Accounts](/en/docs/mt4/manager/reports_journal/ug_report_group)

[Risk Management](/en/docs/mt4/manager/risk_management)