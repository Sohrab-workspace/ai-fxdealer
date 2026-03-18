# Accounts with Margin Call/Stop Out

> Source: https://support.metaquotes.net/en/docs/mt5/manager/margin_calls

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)Accounts with Margin Call/Stop Out

# Accounts with Margin Call/Stop Out

The Manager terminal allows tracking accounts with insufficient funds to cover open positions and pending orders. There are two conditions of an account with insufficient funds:

-   Margin Call — an account will soon have no funds to cover open positions. If the account is not replenished, the Stop Out condition may occur.
-   Stop Out — an account has no enough funds to cover open positions. When this state occurs, trading positions and orders on the account are forcibly closed.

Both levels are configured separately for each client group on the trade server. They are set as a threshold value of the "Margin level" parameter (calculated as Funds / Margin \* 100) or "Funds" on a trading account.

A separate window is available in the terminal to track Margin Call accounts. To open it, select "![Margin Call](/en/docs/mt5/manager/img/margin_calls_icon.png "Margin Call") Margin Call" in the [View](/en/docs/mt5/manager/main_menu#view) menu or on the [toolbar](/en/docs/mt5/manager/toolbar).

![Margin Call](/en/docs/mt5/manager/img/margin_calls.png "Margin Call")

The level of funds in the window is shown in percent or money, depending on how the Margin Call and Stop Out levels are configured in the client group settings (by margin or funds level). If an account has a red background, then it is already in Stop Out state.

Use the [internal email system](/en/docs/mt5/manager/communication#mail) in the context menu to quickly inform a client about the lack of funds on the account. Select the account and click ![Send an email to a client](/en/docs/mt5/manager/img/mail_create_icon.png "Send an email to a client") E-Mail... To view detailed information about the client, double-click the account number.

## Stop out auto processing [#](margin_calls#stopout_processing)

When Stop Out is processed automatically by the server (not a plugin or a manager), forced order removal and position closing are performed as follows:

-   Client's pending orders that are currently not in the process of execution are analyzed.
-   An order requiring the greatest amount of margin is removed.
-   If Equity (or Margin level, depending on how the SO level is determined) is still under the stop out level, the next order is deleted. Orders with no margin requirements are not deleted.
-   If Equity (or Margin level) is still under the stop out level, the server closes a position with the largest loss. If all positions are profitable, the position with the lowest profit is closed (excluding swaps and commissions). The server will not close a position by Stop Out (will skip it) if trading for the corresponding symbol is prohibited (for example, if the closure attempt occurs outside the trading session).
-   Positions are closed until Equity (or Margin level) becomes higher than the stop out level.

-   [Netting accounts](/en/docs/mt5/manager/trade_principles#netting) allow partial position closure by Stop out if the volume of the position to be closed exceeds the maximum allowable volume for the symbol. For example, a trader has a 50-lot position, while the [maximum permissible deal volume](/en/docs/mt5/manager/market_watch#specification) is 20. In the event of a Stop out, the platform will first close 20 lots of the position. If after this the client's funds level is still below the threshold, the platform will close the next 20 lots. Otherwise, the trader will have part of the position remaining open. In this case, the position comment will indicate \[so XX%\], where XX is the margin level at which Stop out occurred. Position can only be closed partially on real accounts. On demo accounts, the entire volume is closed at once, regardless of the symbol settings.

If the forced deletion of orders and closing of positions are not performed by the server, that can be automated in the Manager terminal. Enable the following options at the [Automation](/en/docs/mt5/manager/settings#automation) tab in the terminal settings:

-   Delete Stopout Pending Order — enable to delete pending orders with a margin reserved.
-   Close Stopout Positon — enable to delete most unprofitable positions.

The mechanism of processing a Stop out situation by the Manager terminal is similar to automatic processing by the server.

[Dealing](/en/docs/mt5/manager/dealing)

[Queue of Trade Requests](/en/docs/mt5/manager/trade_queue)