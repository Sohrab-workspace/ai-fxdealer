# Alerts

> Source: https://support.metaquotes.net/en/docs/mt4/manager/risk_management/ug_alerts

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
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
            -   [Summary](/en/docs/mt4/manager/risk_management/ug_risk)
            -   [Exposure](/en/docs/mt4/manager/risk_management/ug_exposure)
            -   [Coverage](/en/docs/mt4/manager/risk_management/ug_coverage)
            -   [Alerts](/en/docs/mt4/manager/risk_management/ug_alerts)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Risk Management](/en/docs/mt4/manager/risk_management)Alerts

# Alerts

Manager terminal allows to create alerts informing about critical changes of total clients' positions, about exceeding a certain level by the symbol price, or about the certain time coming. "Alerts" tab of the "Toolbox" window contains information about alerts created.

![Alerts tab](/en/docs/mt4/manager/img/tb_alerts.png "Alerts tab")

The context menu includes the following commands:

-   Create — create a new alert of an event;
-   Modify — modify an alert;
-   Delete — delete an alert;
-   Enable/Disable — enable or disable the alert;
-   Auto Arrange — automatic arrange of the column sizes when changing the window size;
-   Grid — show or hide the grid to separate columns from each other.

It is possible to begin modifying an alert with double click of the left mouse button. In this case, as well as in the case of executing the "Modify" and "Create" context menu commands, the Alert Editor window will appear:

![Alert Editor window](/en/docs/mt4/manager/img/alert_editor.png "Alert Editor window")

-   Enable — enable or disable an alert;
-   Action — the action to be done when a certain event comes: to play a sound or to launch a file; it is necessary to indicate the corresponding files in the "Source" field;
-   Symbol — financial instrument or group of instruments;
-   Condition — a condition ("Time=", "Bid<", "Bid>", "Ask<", "Ask>", "Deals<", "Deals>", "Net Lots<", "Net Lots>", "Profit<", "Profit>", "Uncovered<", "Uncovered>");
-   Value — the value of the condition;
-   Source — alert; when playing a sound or launching a file, it is necessary to indicate the path to the corresponding file;
-   Timeout — the period of time after which the alert is given;
-   Maximum iteration — maximum number of alerts concerning a certain event;
-   Use popup window — when the event comes, open a popup window containing the message about it;
-   Notification — notification or reminding about actions to be done when the event comes.

The operating of the selected alert can be checked through "Test" button.

[Coverage](/en/docs/mt4/manager/risk_management/ug_coverage)

[User Interface](/en/docs/mt4/manager/user_interface)