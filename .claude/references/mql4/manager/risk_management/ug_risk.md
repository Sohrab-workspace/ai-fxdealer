# Summary

> Source: https://support.metaquotes.net/en/docs/mt4/manager/risk_management/ug_risk

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Risk Management](/en/docs/mt4/manager/risk_management)Summary

# Summary

The "Summary" tab of the "Toolbox" window contains the information about the summary of open positions of clients grouped according to financial instruments being traded. When hedging the clients' positions, there is an opportunity to display the covered positions at the account in the group having the predefined name of "coverage".

![Summary tab](/en/docs/mt4/manager/img/tb_summary.png "Summary tab")

For the purpose of usability, all summary positions are given in the table having the following fields:

-   Item — symbol of the financial instrument;
-   Deals — the amount of clients' deals / the amount of hedging deals;
-   Buy Volume — the amount of bought lots / hedged bought lots;
-   Buy Price — the average buy price;
-   Sell Volume — the amount of sold lots / hedged sold lots;
-   Sell Price — the average sell price;
-   Net Volume — summarized volume (the bought volume minus the hedged bought volume minus (the sold volume minus the hedged sold volume));
-   Profit (CCY) — the client's profit or loss converted to selected currency;
-   Uncovered (CCY) — uncovered profit or loss converted to selected currency.

In addition to the symbols for which clients have open positions, the section shows all symbols enabled in the [Market Watch window](/en/docs/mt4/manager/user_interface/ug_market_watch).

The context menu allows to execute the following commands:

-   Cover — [coverage](/en/docs/mt4/manager/risk_management/ug_coverage#summary) of the aggregate clients' positions by the symbol;
-   Currency — choose a currency to be used for displaying profit/loss; the deposit currency of user groups of the server are available;
-   Profit — choose a variant of clients' profit/loss calculation:

-   -   without swap and commission — without considering the swaps and commissions;
    -   with swap and commission — considering the swaps and commissions;

-   Copy — copy the selected lines of the list in the clipboard;
-   Save — save the list of summary positions in the file;
-   Auto Arrange — automatic arrangement of column sizes when changing the window size;
-   Grid — show/hide grid to separate columns.

[Risk Management](/en/docs/mt4/manager/risk_management)

[Exposure](/en/docs/mt4/manager/risk_management/ug_exposure)