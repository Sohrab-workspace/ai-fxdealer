# Exposure

> Source: https://support.metaquotes.net/en/docs/mt4/manager/risk_management/ug_exposure

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Risk Management](/en/docs/mt4/manager/risk_management)Exposure

# Exposure

The "Exposure" tab of the "Toolbox" window contains the balance of open clients and "coverage" positions.

![Exposure tab](/en/docs/mt4/manager/img/tb_exposure.png "Exposure tab")

For the purpose of usability, the exposure is given in the table having the following fields:

-   Currency — exposure currency;
-   Clients — clients exposure - volume of client's positions;
-   Coverage — coverage exposure - volume of positions of "coverage" group;
-   Net Total — net total - difference between client exposure and coverage exposure;
-   Rate — exchange rate of net total to selected currency;
-   Net Total (CCY) — net total converted to selected currency;
-   Positive (CCY) — positive net total converted to selected currency.

The table also contains the graph representing clients and coverage exposure ratio.

The context menu allows to execute the following commands:

-   Copy — copy the selected lines of the list in the clipboard;
-   Currency — choose a currency to be used for displaying net total; the deposit currency of user groups of the server are available;
-   Save — save the exposure list in the file;
-   Auto Arrange — automatic arrangement of column sizes when changing the window size;
-   Grid — show/hide grid to separate columns.

[Summary](/en/docs/mt4/manager/risk_management/ug_risk)

[Coverage](/en/docs/mt4/manager/risk_management/ug_coverage)