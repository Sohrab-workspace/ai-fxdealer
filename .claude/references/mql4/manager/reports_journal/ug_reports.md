# Reports

> Source: https://support.metaquotes.net/en/docs/mt4/manager/reports_journal/ug_reports

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Reports and Journal](/en/docs/mt4/manager/reports_journal)Reports

# Reports

The "Reports" section allows to create different reports on closed orders. Report generators are delivered as separate dll-files what allows to add new reports and to adjust the existing ones quickly and effectively. The information about the creation of reports is published at the [Support Center](https://support.metaquotes.net) website, in the ["MetaTrader Manager Report API"](https://support.metaquotes.net/en/articles/43) article.

![Reports](/en/docs/mt4/manager/img/br_reports.png "Reports")

Reports are generated on basis of closed orders requested from the server for a group of clients' accounts. The created groups of accounts are displayed in a popup list at the bottom of the report window. The "Add" button is intended for creation of a new group of accounts, the "Edit" button allows to edit the existing group of accounts, the "Delete" button allows to delete the existing group of accounts. When a group of accounts is created or edited, the [groups of accounts](/en/docs/mt4/manager/reports_journal/ug_report_group) window of edition opens.

To request the closed orders for an account group, it is necessary to select a group from a popup list, to give a period for which the orders will be requested, and to press the "Request" button (or execute the "Request" command of the context menu).

A raw report can be generated for a group of accounts for the closed orders within the period using the "Save Raw Report" command of context menu, or select one of the reports of the "Additional Reports" submenu of the context menu:

-   Closed Trades Report;
-   Commissions Report;
-   Detailed Commissions Report;
-   Credit Facility Report;
-   Deposit-Withdrawal Report;
-   Summary Report;
-   Withholding Tax Statement;
-   Phone Report;
-   Segregated Report;
-   Agent Report;
-   Margin Call Report.

The context menu allows to execute the following commands:

-   Request — request orders from the server;
-   Account Details — open the window for managing client's orders;
-   Find — find an order in the order list;
-   Copy — copy the selected orders from the list in the clipboard;
-   Save Raw Reports — save the raw report;
-   Commission Reports — choose the commission report;
-   Additional Reports — choose a report;
-   Auto Arrange — automatic arrangement of column sizes when changing the window size;
-   Grid — show/hide grid to separate columns;
-   Columns — select columns to be shown.

[Reports and Journal](/en/docs/mt4/manager/reports_journal)

[History Reports](/en/docs/mt4/manager/reports_journal/ug_history_reports)