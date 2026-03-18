# Ichimoku Kinko Hyo

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/ikh

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
                    -   [Adaptive Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ama)
                    -   [Average Directional Movement Index](/en/docs/mt5/client/indicators/trend_indicators/admi)
                    -   [Average Directional Movement Index Wilder](/en/docs/mt5/client/indicators/trend_indicators/admiw)
                    -   [Bollinger Bands](/en/docs/mt5/client/indicators/trend_indicators/bb)
                    -   [Double Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/dema)
                    -   [Envelopes](/en/docs/mt5/client/indicators/trend_indicators/envelopes)
                    -   [Fractal Adaptive Moving Average](/en/docs/mt5/client/indicators/trend_indicators/fama)
                    -   [Ichimoku Kinko Hyo](/en/docs/mt5/client/indicators/trend_indicators/ikh)
                    -   [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma)
                    -   [Parabolic SAR](/en/docs/mt5/client/indicators/trend_indicators/psar)
                    -   [Standard Deviation](/en/docs/mt5/client/indicators/trend_indicators/sd)
                    -   [Triple Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/tema)
                    -   [Variable Index Dynamic Average](/en/docs/mt5/client/indicators/trend_indicators/vida)
                -   [Oscillators](/en/docs/mt5/client/indicators/oscillators)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Ichimoku Kinko Hyo

# Ichimoku Kinko Hyo

Ichimoku Kinko Hyo Technical Indicator is predefined to characterize the market Trend, Support and Resistance Levels, and to generate signals of buying and selling. This indicator works best at weekly and daily charts.

When defining the dimension of parameters, four time intervals of different length are used. The values of individual lines composing this indicator are based on these intervals:

-   Tenkan-sen shows the average price value during the first time interval defined as the sum of maximum and minimum within this time, divided by two;
-   Kijun-sen shows the average price value during the second time interval;
-   Senkou Span A shows the middle of the distance between two previous lines shifted forwards by the value of the second time interval;
-   Senkou Span B shows the average price value during the third time interval shifted forwards by the value of the second time interval.

Chikou Span shows the closing price of the current candle shifted backwards by the value of the second time interval. The distance between the Senkou lines is hatched with another color and called "cloud". If the price is between these lines, the market should be considered as non-trend, and then the cloud margins form the support and resistance levels.

-   If the price is above the cloud, its upper line forms the first support level, and the second line forms the second support level;
-   If the price is below cloud, the lower line forms the first resistance level, and the upper one forms the second level;
-   If the Chikou Span line traverses the price chart in the bottom-up direction it is signal to buy. If the Chikou Span line traverses the price chart in the top-down direction it is signal to sell.

Kijun-sen is used as an indicator of the market movement. If the price is higher than this indicator, the prices will probably continue to increase. When the price traverses this line the further trend changing is possible. Another kind of using the Kijun-sen is giving signals. Signal to buy is generated when the Tenkan-sen line traverses the Kijun-sen in the bottom-up direction. Top-down direction is the signal to sell. Tenkan-sen is used as an indicator of the market trend. If this line increases or decreases, the trend exists. When it goes horizontally, it means that the market has come into the channel.

![Ichimoku Kinko Hyo](/en/docs/mt5/client/img/ichimoku.png "Ichimoku Kinko Hyo")

[Fractal Adaptive Moving Average](/en/docs/mt5/client/indicators/trend_indicators/fama)

[Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma)