# Dealing and Risk Management

> Source: https://support.metaquotes.net/en/docs/mt5/manager/dealing_risk_management

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Dealing and Risk Management

# Dealing and Risk Management

One of the main available tasks in the Manager terminal is [processing trade requests](/en/docs/mt5/manager/dealing) of clients. To do this, the dealer is provided with all the necessary tools: the ability to confirm requests partially or completely, reject them, issue new prices in response, and much more. When a request is received, the dealer immediately receives complete information about a client: general data, account status, open positions, orders and query history.

For a risk manager, the terminal provides data on [summary positions](/en/docs/mt5/manager/summary_positions) and [assets](/en/docs/mt5/manager/exposure) of clients, as well as on uncovered positions.

![Processing trade requests and managing risks in the Manager terminal](/en/docs/mt5/manager/img/dealing_risk.png "Processing trade requests and managing risks in the Manager terminal")

Besides, managers have access to [Margin call](/en/docs/mt5/manager/margin_calls) account lists and are able to send notifications asking for an account replenishment. Besides, a risk manager can quickly [modify trading symbol settings](/en/docs/mt5/manager/quotes_symbols#profile) during important news releases.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Before processing requests, please read the <a href="/en/docs/mt5/manager/trade_principles" class="topiclink">general information on the platform's trading system</a> and basic concepts.</span></p></td></tr></tbody></table>

[Splitting Positions](/en/docs/mt5/manager/position_split)

[Dealing](/en/docs/mt5/manager/dealing)