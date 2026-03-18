# Summary Positions and Coverage

> Source: https://support.metaquotes.net/en/docs/mt5/manager/summary_positions

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
            -   [Dealing](/en/docs/mt5/manager/dealing)
            -   [Accounts with Margin Call/Stop Out](/en/docs/mt5/manager/margin_calls)
            -   [Queue of Trade Requests](/en/docs/mt5/manager/trade_queue)
            -   [Quoting and Symbol Management](/en/docs/mt5/manager/quotes_symbols)
            -   [Summary Positions and Coverage](/en/docs/mt5/manager/summary_positions)
            -   [Exposure](/en/docs/mt5/manager/exposure)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
    -   [Client terminal](/en/docs/mt5/client)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)Summary Positions and Coverage

# Summary Positions and Coverage

The Manager terminal allows viewing data on clients' summary positions. A risk manager can in real time view the volume of short and long positions for each symbol, as well as manage non-covered profits on client's positions. This information is displayed in the Summary tab of the Toolbox window:

![Summary positions](/en/docs/mt5/manager/img/toolbox_summary.png "Summary positions")

The following information on summary positions is available:

-   Symbol — name of a financial security.
-   Positions — number of clients' positions/number of covering positions.
-   Buy Volume — volume of clients' open buy positions/volume of the corresponding position on a coverage account.
-   Buy Price — average weighted open price of the clients' buy positions/the corresponding open price on a coverage account.
-   Sell Volume — volume of the clients' open sell positions/volume of the corresponding position on a coverage account.
-   Sell Price — average weighted open price of the clients' sell positions/the corresponding open price on a coverage account.
-   Net Volume — difference between the volumes of clients' buy and sell positions, at that the corresponding volume on the coverage account is subtracted from the buy or sell position.
-   Profit (Currency) — total profit (loss) from the clients' positions/profit (loss) on a coverage account position. Currency, in which the profit is displayed, is specified in brackets. You can change the currency using the Currency command of the context menu.
-   Uncovered (Currency) — difference between the total profit (loss) from the clients' positions and the corresponding position on the coverage account. Currency, in which the uncovered profit is displayed, is specified in brackets. You can change the currency using the Currency command of the context menu.

The Total line in the lower part displays the total rates by all symbols.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Coverage accounts are those created in groups whose names start with "coverage" (case sensitive). For example, coverage\forex. This tab displays summary positions for all coverage accounts of a trade server.</span></p></td></tr></tbody></table>

## Covering client's positions [#](summary_positions#coverage)

MetaTrader 5 allows you to cover client's positions on other trade servers protecting your company against risks. For example, traders have opened the total of 100 lots of buy and 120 lots of sell positions for EURUSD. As a result, an imbalance of 20 lots occurs — a net position posing risk for the company. In this case, the brokerage company can open their own position at their market maker (for example, another broker) for selling 20 lots. A special type of accounts is provided in the platform for that. These accounts are created in groups whose names begin with the "coverage" symbols. For example, coverage\\forex. Performing trading operations on a coverage account, a manager covers clients' positions on another trade server.

To perform a coverage, a trading platform administrator should perform the following settings:

-   Create a group with its name starting with "coverage".
-   Create an account in that group; this account will be used for covering.
-   Open a trade account on an external trade server, where coverage positions will be opened.
-   Set up the MetaTrader 5 Gateway - specify the authorization details of the account opened on the external trade server.
-   Set up routing of trade operations on the coverage account to the external trade system through the gateway.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A more detailed description of setting up covering is provided in the MetaTrader 5 Administrator <a href="https://support.metaquotes.net/en/docs/mt5/platform/components/gateways/metatrader5gateway#coverage" target="_blank" class="weblink">User Guide</a>.</span></p></td></tr></tbody></table>

Once a coverage account is set up, a manager can perform [trade operations](/en/docs/mt5/manager/account_trading) on it using the Manager terminal. The summary rates for all coverage accounts on the trade server are displayed in the [Summary](/en/docs/mt5/manager/summary_positions) and [Exposure](/en/docs/mt5/manager/exposure) tabs of the Toolbox window.

## Context menu [#](summary_positions#context)

The following commands can be run from the context menu of this tab:

-   Currency — open the submenu of selecting a currency to be used for displaying a profit by symbols. Any currency used as a deposit currency of a group of accounts at the server is available for selection.
-   Profit — open the submenu of selecting a profit display mode. There are two modes implemented — with and without swaps and commissions.
-   ![Copy](/en/docs/mt5/manager/img/copy_icon.png "Copy") Copy — copy a selected line to the clipboard.
-   Report — generate a report on summary positions in the XML or HTML format.
-   ![Save](/en/docs/mt5/manager/img/save_icon.png "Save") Save — save the information about the summary positions as an HTML file.
-   Reset Sort Order — restore the default sorting order.
-   Auto Arrange — set the size of columns automatically.
-   Grid — show/hide the grid to separate fields in the table.

[Quoting and Symbol Management](/en/docs/mt5/manager/quotes_symbols)

[Exposure](/en/docs/mt5/manager/exposure)