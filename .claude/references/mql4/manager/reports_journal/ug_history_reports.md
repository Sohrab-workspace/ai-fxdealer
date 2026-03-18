# History Reports

> Source: https://support.metaquotes.net/en/docs/mt4/manager/reports_journal/ug_history_reports

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Reports and Journal](/en/docs/mt4/manager/reports_journal)History Reports

# History Reports

"History Reports" section allows to create various reports on the daily reports created by the server. Report generators are delivered as separate dll-files what allows to add new reports and to set the existing ones quickly and effectively. The information about the creation of reports is published at the [Support Center](https://support.metaquotes.net) website, in the ["MetaTrader Manager Report API"](https://support.metaquotes.net/en/articles/43) article.

![History Reports](/en/docs/mt4/manager/img/br_history_reports.png "History Reports")

History reports are generated on the base of daily reports requested from the server for a group of client accounts. The account groups created are displayed in a popup list at the bottom of the report window. The "Add" button is intended for creating a new account group, the "Edit" button edits the existing account group, the "Delete" button deletes the existing account group. When a group of accounts is created and edited, the [editing window of an account group](/en/docs/mt4/manager/reports_journal/ug_report_group) will open.

To make a request of daily reports for a group of accounts, it is necessary to select the group in the popup list, indicate the period within which the reports will be requested, and press the "Request" button (or execute the "Request" context menu command).

For purpose of usability, all the daily reports requested from the server are summarized in a table with the following cells:

-   Time — time of the daily report generation on the server;
-   Login — the account number;
-   Deposit — the account deposit;
-   Closed P/L — realized gain of the account;
-   Balance — the account balance;
-   Credit — the account credit;
-   Floating P/L — unrealized profit of the account;
-   Equity — assets of the account.
-   Used Margin — used margin of the account;
-   Free Margin — free margin of the account;

According to daily reports for a group of accounts requested within the period, it is possible to generate a raw history report using the "Save Raw Report" context menu command or select one of the reports in "Additional Reports" submenu of the context menu:

-   Common History Report;
-   Equity Report;
-   Profit and Loss Report.

The context menu allows to execute the following commands:

-   Request — request the reports from the server;
-   Account Details — open window of the client's order management;
-   Find — find the line in the order list;
-   Copy — copy the selected lines of the list to clipboard;
-   Save Raw Reports — save the raw report;
-   Additional Reports — choose a report;
-   Auto Arrange — automatic arrangement of the column sizes when changing the window size;
-   Grid — show/hide the grid to separate columns;
-   Columns — select columns to be displayed.

[Reports](/en/docs/mt4/manager/reports_journal/ug_reports)

[Groups of Accounts](/en/docs/mt4/manager/reports_journal/ug_report_group)