# Collateral Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/manager/trading_advanced/symbols_collateral

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
            -   [Basic Principles](/en/docs/mt5/manager/trade_principles)
            -   [Market Watch](/en/docs/mt5/manager/market_watch)
            -   [Market Depth](/en/docs/mt5/manager/depth_of_market)
            -   [Economic Calendar](/en/docs/mt5/manager/economic_calendar)
            -   [Trading Notifications](/en/docs/mt5/manager/trade_alerts)
            -   [Working with Trading Positions](/en/docs/mt5/manager/positions)
            -   [Working with Trading Orders](/en/docs/mt5/manager/orders)
            -   [Viewing and Editing Trading Operations](/en/docs/mt5/manager/edit_trades)
            -   [For Advanced Users](/en/docs/mt5/manager/trading_advanced)
                -   [Margin Calculation: Basic](/en/docs/mt5/manager/trading_advanced/margin_formula)
                -   [Margin Calculation: Retail Forex, CFD, Futures — Netting](/en/docs/mt5/manager/trading_advanced/margin_forex)
                -   [Margin Calculation: Retail Forex, CFD, Futures — Hedging](/en/docs/mt5/manager/trading_advanced/margin_forex_hedge)
                -   [Margin Calculation: Stock Exchange](/en/docs/mt5/manager/trading_advanced/margin_exchange)
                -   [Spreads](/en/docs/mt5/manager/trading_advanced/spreads)
                -   [Collateral Symbols](/en/docs/mt5/manager/trading_advanced/symbols_collateral)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Trading Operations](/en/docs/mt5/manager/trading)[For Advanced Users](/en/docs/mt5/manager/trading_advanced)Collateral Symbols

# Collateral Symbols

The trading platform supports a special type of non-tradable assets, which can be used as client's assets to provide the required margin for open positions of other instruments. For example, a certain amount of gold in physical form can be available on a trader's account, which can be used as a margin (collateral) for open positions.

These instruments have [Collateral](/en/docs/mt5/manager/market_watch#calculation) calculation type. They have the following features:

-   Clients cannot perform any operations with them except closing. A position can be opened only by a manager.
-   No profit can be accrued for the positions of these symbols, they have no stop loss or take profit.

Such assets are displayed as open positions. Their value is calculated by the formula: Contract size \* Lots \* Market Price \* Liquidity Rate.

-   Contract size — size of a contract
-   Lots — volume in lots
-   Market Price — current market price of the financial instrument
-   Liquidity Rate here means the share of the asset that a broker allows to use for the margin

The Assets are added to the client's Equity and increase Free Margin, thus increasing the volumes of allowable trade operations on the account.

![Trader's assets](/en/docs/mt5/manager/img/account_assets.png "Trader's assets")

In the example above, a trader has 1 ounce of gold having the current market value of 1 210.54 USD. This value is added to the equity and the free margin

Collateral symbol settings on the server may allow clients and managers close such positions (Trade = Close only). In this case, a trader is able to convert the asset into the deposit currency at the current market rate and use that money for trading. Closing can be performed only if an asset/deposit currency conversion rate is present.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To delete a collateral position without crediting any profit, a manager should close the position at the zero price.</span></li><li class="p_tableatten"><span class="f_tableatten">To close a position with adding its value to a trader's balance, a manager should close it at the current market price.</span></li></ul></td></tr></tbody></table>

[Spreads](/en/docs/mt5/manager/trading_advanced/spreads)

[Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)