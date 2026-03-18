# Price Data in the Trading Platform

> Source: https://support.metaquotes.net/en/docs/mt5/client/trading_advanced/price_data

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Operations](/en/docs/mt5/client/trading)[For Advanced Users](/en/docs/mt5/client/trading_advanced)Price Data

# Price Data in the Trading Platform

Three basic prices of a financial instrument are used in the trading platform:

-   Bid is the highest price at which a trader can sell a financial instrument. It is the best price at which a financial symbol can be sold.
-   Ask is the lowest price at which a trader can buy a financial instrument. It is the best price at which a financial symbol can be bought.
-   Last is the price of the last deal executed on a financial instrument.

A financial symbol can be traded on the exchange and over-the-counter (OTC) market. Different approaches to symbol quote and charting are used depending on the market.

## Exchange Market with the Market Depth

The only source of quotes in the exchange market is the Exchange itself. Buyers and sellers meet on the exchange, which keeps records of all executed deals. Orders of all market participants comprise a single Market Depth.

A Market Depth option featuring real orders of market participants is available in the trading platform for exchange traded symbol. Based on the best orders, the Bid and Ask prices are formed in the Market Depth (these prices are shown in the Market Watch window). Also, the exchange provides prices and volumes of last executed deals (Last and Volume). Last prices are used for creating [price charts](/en/docs/mt5/client/trading_advanced/price_data#charts) and for displaying the Time & Sales tape:

![The Market Depth on the Exchange Market](/en/docs/mt5/client/img/dom_exchange.png "The Market Depth on the Exchange Market")

Although symbol charts are based on Last prices, traders execute deals at Bid and Ask prices (actual prices available in the market).

## Over-The-Counter Market

Participants of the OTC market are big market players, such as banks and prime brokerages. They form networks to trade with each other. Medium market participants, such as banks, management companies and hedge funds connect to large participants. Market participants aggregate prices of their counterparties or they set their own prices based on counterparties' prices, and provide these prices to their clients.

Only Bid and Ask stream quotes are used in OTC market trading, without data on actual executed deals. [Charts](/en/docs/mt5/client/trading_advanced/price_data#charts) are based on Bid prices.

![Market Watch with Bid and Ask prices of OTC financial instruments](/en/docs/mt5/client/img/otc_market_watch.png "Market Watch with Bid and Ask prices of OTC financial instruments")

## Over-The-Counter Market with the Market Depth

Unlike the previous variant, the broker provides traders information on volumes in addition to Bid and Ask prices, which allows displaying the Market Depth. The exchange Market Depth consists of limit orders of market participants, while OTC Market Depth is formed based on the broker's quotes. The broker provides different prices depending on the buying and selling volume.

![The Market Depth on the OTC Market](/en/docs/mt5/client/img/dom_otc.png "The Market Depth on the OTC Market")

The exchange does not participate in trading and does not keep record of performed trades, therefore no Last prices are available in this mode. [Charts](/en/docs/mt5/client/trading_advanced/price_data#charts) are based on Bid prices.

## How Price Charts Are Formed [#](price_data#charts)

One-minute bars are formed based on symbol quotes (or ticks). This bar represents a set of price characteristics of one minute:

-   4 prices: Low and High price during this minute, as well as the beginning and the end of the bar, i.e. the Open and Close prices
-   Spread, which is the minimum difference between Bid and Ask recorded during one minute
-   Tick volume, which shows the number of ticks received during bar formation
-   Volume, i.e. the real volume of deals performed during bar formation (may be not available for OTC markets)
-   Date and time, i.e. the minute to which this bar corresponds

One-minute bars are based on Bid prices for OTC symbols, and are based on Last prices for exchange instruments.

In addition to one-minute bars, price charts in the trading platform can be displayed as larger time intervals. The time included in one bar or candlestick on the chart, is called a timeframe. The platform supports 21 timeframes from 1 minute to a 1-month period.

The trading platform only stores 1-minute bars. All higher timeframes are created based on these bars. This approach ensures compliance of data at all periods, as well as allows to significantly save traffic and disk space.

![Five 1-minute bars and one 5-minute bar on their basis](/en/docs/mt5/client/img/chart_bars.png "Five 1-minute bars and one 5-minute bar on their basis")

[For Advanced Users](/en/docs/mt5/client/trading_advanced)

[Margin Calculation: Retail Forex, Futures](/en/docs/mt5/client/trading_advanced/margin_forex)