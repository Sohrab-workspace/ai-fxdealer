# Force Index

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/oscillators/fi

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
            -   [View and Configure Charts](/en/docs/mt5/client/charts)
            -   [Publish Online](/en/docs/mt5/client/mql5_charts)
            -   [Technical Indicators](/en/docs/mt5/client/indicators)
                -   [Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)
                -   [Oscillators](/en/docs/mt5/client/indicators/oscillators)
                    -   [Average True Range](/en/docs/mt5/client/indicators/oscillators/atr)
                    -   [Bears Power](/en/docs/mt5/client/indicators/oscillators/bears)
                    -   [Bulls Power](/en/docs/mt5/client/indicators/oscillators/bulls)
                    -   [Chaikin Oscillator](/en/docs/mt5/client/indicators/oscillators/chaikin)
                    -   [Commodity Channel Index](/en/docs/mt5/client/indicators/oscillators/cci)
                    -   [DeMarker](/en/docs/mt5/client/indicators/oscillators/demarker)
                    -   [Force Index](/en/docs/mt5/client/indicators/oscillators/fi)
                    -   [MACD](/en/docs/mt5/client/indicators/oscillators/macd)
                    -   [Momentum](/en/docs/mt5/client/indicators/oscillators/momentum)
                    -   [Moving Average of Oscillator](/en/docs/mt5/client/indicators/oscillators/mao)
                    -   [Relative Strength Index](/en/docs/mt5/client/indicators/oscillators/rsi)
                    -   [Relative Vigor Index](/en/docs/mt5/client/indicators/oscillators/rvi)
                    -   [Stochastic Oscillator](/en/docs/mt5/client/indicators/oscillators/so)
                    -   [Triple Exponential Average](/en/docs/mt5/client/indicators/oscillators/tea)
                    -   [Williams' Percent Range](/en/docs/mt5/client/indicators/oscillators/wpr)
                -   [Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)
                -   [Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)
            -   [Analytical Objects](/en/docs/mt5/client/objects)
            -   [Fundamental Analysis](/en/docs/mt5/client/fundamental)
            -   [Additional Technical Indicators](/en/docs/mt5/client/charts_analysis_get_indicators)
            -   [Additional Features](/en/docs/mt5/client/charts_advanced)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Oscillators](/en/docs/mt5/client/indicators/oscillators)Force Index

# Force Index

Force Index Technical Indicator was developed by Alexander Elder. This index measures the Bulls Power at each increase, and the Bears Power at each decrease. It connects the basic elements of market information: price trend, its drops, and volumes of transactions. This index can be used as it is, but it is better to approximate it with the help of [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma). Approximation with the help a short moving average (the author proposes to use 2 intervals) contributes to finding the best opportunity to open and close positions. If the approximations is made with long moving average (period 13), the index shows the trends and their changes.

-   It is better to buy when the forces become minus (fall below zero) in the period of indicator increasing tendency;
-   The force index signalizes the continuation of the increasing tendency when it increases to the new peak;
-   The signal to sell comes when the index becomes positive during the decreasing tendency;
-   The force index signalizes the Bears' Power and continuation of the decreasing tendency when the index falls to the new depth;
-   If price changes do not correlate to the corresponding changes in volume, the force indicator stays on one level, which tells you the trend is going to change soon.

![Force Index](/en/docs/mt5/client/img/force_index.png "Force Index")

## Calculation

The force of every market movement is characterized by its direction, scale and volume. If the closing price of the current bar is higher than the preceding bar, the force is positive. If the current closing price is lower than the preceding one, the force is negative. The greater the difference in prices is the greater the force is. The greater the transaction volume is the greater the force is.

FORCE INDEX (i) = VOLUME (i) \* ((MA (ApPRICE, N, i) - MA (ApPRICE, N, i-1))

Where:

FORCE INDEX (i) — Force Index of the current bar;  
VOLUME (i) — volume of the current bar;  
MA (ApPRICE, N, i) — any [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma) of the current bar for N periods:  
[Simple](/en/docs/mt5/client/indicators/trend_indicators/ma#sma), [Exponential](/en/docs/mt5/client/indicators/trend_indicators/ma#ema), [Weighted](/en/docs/mt5/client/indicators/trend_indicators/ma#lwma) or [Smoothed](/en/docs/mt5/client/indicators/trend_indicators/ma#smma);  
ApPRICE — applied price;  
N — period of smoothing;  
MA (ApPRICE, N, i-1) — any [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma) of the previous bar.

[DeMarker](/en/docs/mt5/client/indicators/oscillators/demarker)

[MACD](/en/docs/mt5/client/indicators/oscillators/macd)