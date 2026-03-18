# Coverage

> Source: https://support.metaquotes.net/en/docs/mt4/manager/risk_management/ug_coverage

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Risk Management](/en/docs/mt4/manager/risk_management)Coverage

# Coverage

The Manager terminal allows covering of clients' positions or assets on the hedge server.

To cover positions and assets, it is necessary to open an account on the hedge server and select an account in the "coverage" group of one's own server. When being covered, positions of the hedge server can be automatically displayed in the selected account of the "coverage" group on one's own server. This allows tracking of the uncovered client's profit in the [Summary](/en/docs/mt4/manager/risk_management/ug_risk) tab or the uncovered assets in the [Exposure](/en/docs/mt4/manager/risk_management/ug_exposure) tab.

The hedge account orders are displayed in the selected account in the "coverage" group according to the following rules:

-   When a position is opened on the hedge account, the corresponding position will be opened on the account in the "coverage" group of one's own server.
-   Stops placed on orders of the hedge account are zeroed on orders of the account in the "coverage" group, otherwise, if price flows are different, the stops on orders of the account in the "coverage" group can trigger before stops on orders of the hedge account trigger.
-   When a position is closed (manually or by triggering of stops) on the hedge account, the corresponding position of the account in the "coverage" group will be closed automatically.
-   The pending orders placed on the hedge account are not displayed in the account of the "coverage" group, otherwise, if price flows are different, the pending orders of the account in the "coverage" group can trigger before pending orders of the hedge account trigger.
-   When a pending order triggers and a position is opened on the hedge account, a position on the account in the "coverage" group will be opened automatically, stops of this position will be zeroed.
-   When connecting to the hedge server, the positions of the hedge account are checked for their compliance with positions on the account in the "coverage" group.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: It is prohibited to connect several Manager terminals to the hedge account. If several Manager terminals were connected to the hedge account, it would result in desynchronization of orders on the hedge account and on the account in the "coverage" group. This would carry a distorted picture of coverage of aggregate clients' positions and assets.</span></p></td></tr></tbody></table>

To be able to cover clients' positions and assets, the manager must must have "Risk manager" right.

## Coverage Setup [#](ug_coverage#setup)

![Coverage Tab](/en/docs/mt4/manager/img/options_coverage.png "Coverage Tab")

The "Coverage" tab of the Manager terminal setup window allows specifying of positions and assets coverage settings. The following parameters can be set up in the "Coverage" tab:

-   Server — IP address and port or name of the hedge server, on which the clients' positions and assets will be covered;
-   Login — trade account login on the hedge server;
-   Password — trade account password on the hedge server;
-   Coverage login — login of the account in the "coverage" group on one's own server; trades of the hedge account will be displayed in this account.

The settings above are stored between launches of the Manager terminal if the "Save account information" option is enabled in the [server settings](/en/docs/mt4/manager/getting_started/ug_setup#server).

## Logging In [#](ug_coverage#login)

One can log in to the hedge account using the "File — Connect Coverage" menu command or clicking on the "Connect" button of the "Coverage" toolbar.

![Coverage Authorization](/en/docs/mt4/manager/img/cov_login.png "Coverage Authorization")

Authorization on the hedge server functions by connecting to the trade server using a login and a password. At this stage, one can also specify the login of the account in the "coverage" group, on which trades on the hedge server will be displayed. when authorizing on the hedge server, one can specify the main or the investor's password. Authorization using the main password gives full rights when working with a trade account. When authorized as investor, one can view the account status, but cannot trade. After one has connected to the hedge server, the connection flag is shown in the status bar of the Manager terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: At connection to the hedge server, the positions of the hedge account are checked for their compliance with positions on the account in the "coverage" group. After having connected, it is necessary to look through the manager's journal to check for records about discordances in positions opened on the hedge account and on the account in "coverage" group.</span></p></td></tr></tbody></table>

## Trading [#](ug_coverage#coverage)

Trading on the hedge account in the Manager terminal is similar to that in the Client Terminal. The "Coverage" tab of the "Toolbox" window contains information about the current status of the hedge account, about positions opened and pending orders placed. Open positions and pending orders can be sorted by any field.

![Coverage](/en/docs/mt4/manager/img/tb_coverage.png "Coverage")

Commands of the "Coverage" tab context menu allow to open a new order on the hedge account, close an order, modify stops or delete a pending order. A new order can be opened by clicking on the "New Order" button of the "Coverage" toolbar or by pressing F9 on the keyboard.

Trading in the hedge account is displayed on orders of the account in the "coverage" group in strict compliance with the above [rules](/en/docs/mt4/manager/risk_management/ug_coverage#rules). Trading results on the hedge account and on the account in the "coverage" group are recorded in the Manager terminal journal.

## Coverage of Aggregate Clients' Positions [#](ug_coverage#summary)

The [Summary](/en/docs/mt4/manager/risk_management/ug_risk) tab contains data about aggregate clients' positions and about total uncovered volumes (Net Lots) and profits for clients' positions.

The "Cover" command of the "Summary" tab context menu allows to hedge uncovered total volumes for the selected symbol. When executiong this command:

-   Among positions on the hedge account, an open position will be searched for, closing of which will result in decreasing of absolute total uncovered volumes. If such a position has been found, the order window will open that suggests to close the found position.
-   If no position for a symbol is found, closing of which would result in decreasing the uncovered volumes, there will be opened the order window that will suggest to open on the hedge account a BUY or SELL position of the total uncovered volume for the symbol.

## Assets Coverage [#](ug_coverage#exposure)

The [Exposure](/en/docs/mt4/manager/risk_management/ug_exposure) tab contains clients's assets and the company's hedged assets by currencies, as well as the company's net currency positions (Net Total).

The "Cover" command of the "Exposure" tab context menu allows to hedge clients' assets for the selected currency, reducing in such a way the net currency position and exchange risks. When executing this command, one selects a currency pair for the given currency and opens the order window that suggests to open or close a position on the hedge account. A currency pair for the currency is chosen according to the following rules:

1.  Such currency pairs are chosen that the net currency position for one currency is long and that for another currency is short.
2.  For the currency pairs found, positions opened on the hedge account are searched for, closing of which would result in decreasing of net currency positions by currencies.
3.  Among open positions found, the position for a symbol with the lowest spread is selected. Then the order window is opened that suggests to close this position on the hedge account.
4.  If no open positions are found, closing of which would result in decreasing of net currency position, the currency with the lowest spread will be chosen among currency pairs found at step 1.
5.  Among currency pairs with the lowest spreads, a currency pair is chosen, opening of a position for which would result in the most significant decreasing of net currency positions. Then the order window opens that suggests to open a position for the selected currency pair.

If no currency pair, opening or closing positions for which would result in decreasing net currency positions, is found, i.e., all net currency positions are long or all of them are long, the order window containing the default currency pair and volume will open upon selection of the "Cover" menu item.

[Exposure](/en/docs/mt4/manager/risk_management/ug_exposure)

[Alerts](/en/docs/mt4/manager/risk_management/ug_alerts)