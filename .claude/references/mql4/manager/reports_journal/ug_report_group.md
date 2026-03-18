# Groups of Accounts

> Source: https://support.metaquotes.net/en/docs/mt4/manager/reports_journal/ug_report_group

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Reports and Journal](/en/docs/mt4/manager/reports_journal)Groups of Accounts

# Groups of Accounts

Reports and history reports are generated for a group of clients specified in a request sent from the manager terminal to the server. A group of accounts is [created or edited](/en/docs/mt4/manager/reports_journal/ug_reports) using the following window:

![Account Group window](/en/docs/mt4/manager/img/accounts_group.png "Account Group window")

The left list contains client accounts available for reports, the right one contains the accounts taken to the group. Accounts can be included into a group in several ways:

-   To add a single account, click on it with the left mouse button.
-   To add several accounts, select them with the mouse while holding Ctrl or Ctrl+Shift. Then click the "Add >>" button.
-   To add all accounts from specific groups, select one account from each group and then click  "Group >>".
-   To add all accounts from specific countries, select one account from each country and then click  "Country >>".
-   To add accounts, one can use a CSV file containing a list of accounts. Click "Browse", select a file and click "OK". Accounts from the file are selected in the list on the left, and you can add them using the "Add >>" button.

To delete an account from the list, click on it with the left mouse button. To delete several accounts, select them with the mouse while holding Ctrl or Ctrl+Shift, then click "<< Delete".

The list of available accounts can be filtered by a user group. To do it, double click in any line of the "Group" column and select the necessary group in the window appeared. To disable filtering, an empty line should be selected in the list.

Once all the necessary accounts are selected, specify a name for the groups of accounts in the "Name" field and click "OK". Now you can use the group for [requesting the reports](/en/docs/mt4/manager/reports_journal/ug_reports).

[History Reports](/en/docs/mt4/manager/reports_journal/ug_history_reports)

[Journal](/en/docs/mt4/manager/reports_journal/ug_logs)