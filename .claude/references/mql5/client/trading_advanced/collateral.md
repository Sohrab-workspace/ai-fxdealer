# Collateral Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/client/trading_advanced/collateral

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
            -   [Basic Principles](/en/docs/mt5/client/general_concept)
            -   [Depth of Market](/en/docs/mt5/client/depth_of_market)
            -   [Market Watch](/en/docs/mt5/client/market_watch)
            -   [Options Board](/en/docs/mt5/client/options_board)
            -   [Executing Trades](/en/docs/mt5/client/performing_deals)
            -   [One Click Trading](/en/docs/mt5/client/one_click_trading)
            -   [Trading Report](/en/docs/mt5/client/report)
            -   [For Advanced Users](/en/docs/mt5/client/trading_advanced)
                -   [Price Data](/en/docs/mt5/client/trading_advanced/price_data)
                -   [Margin Calculation: Retail Forex, Futures](/en/docs/mt5/client/trading_advanced/margin_forex)
                -   [Margin Calculation: Exchange Model](/en/docs/mt5/client/trading_advanced/margin_exchange)
                -   [Collateral Symbols](/en/docs/mt5/client/trading_advanced/collateral)
                -   [Custom Financial Instruments](/en/docs/mt5/client/trading_advanced/custom_instruments)
                -   [Spreads](/en/docs/mt5/client/trading_advanced/spreads)
                -   [Futures](/en/docs/mt5/client/trading_advanced/futures)
                -   [Trading Report](/en/docs/mt5/client/trading_advanced/history_report)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Operations](/en/docs/mt5/client/trading)[For Advanced Users](/en/docs/mt5/client/trading_advanced)Collateral Symbols

# Collateral Symbols

The trading platform supports a special type of non-tradable assets, which can be used as client's assets to provide the required margin for open positions of other instruments. For example, a certain amount of gold in physical form can be available on a trader's account, which can be used as a margin (collateral) for open positions.

In the [contract specification](/en/docs/mt5/client/market_watch#specification), these instruments have calculation type "Collateral".

![Collateral calculation type](/en/docs/mt5/client/img/specification_collateral.png "Collateral calculation type")

Such assets are displayed as open positions. Their value is calculated by the formula: Contract size \* Lots \* Market Price \* Liquidity Rate. Liquidity Rate here means the share of the asset that a broker allows to use for the margin.

The Assets are added to the client's Equity and increase Free Margin, thus increasing the volumes of allowable trade operations on the account.

![Exposure](/en/docs/mt5/client/img/toolbox_assets.png "Exposure")

In the example above, a trader has 1 ounce of gold having the current market value of 1,210.56 USD. This value is added to the equity and the free margin.

Brokers may allow closing such positions. In this case a trader is able to convert the asset into the deposit currency at the current market rate and use that money for trading.

[Margin Calculation: Exchange Model](/en/docs/mt5/client/trading_advanced/margin_exchange)

[Custom Financial Instruments](/en/docs/mt5/client/trading_advanced/custom_instruments)