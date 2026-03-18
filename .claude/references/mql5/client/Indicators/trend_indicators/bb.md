# Bollinger Bands®

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/bb

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Bollinger Bands

# Bollinger Bands®

Bollinger Bands (BB) are similar to [Envelopes](/en/docs/mt5/client/indicators/trend_indicators/envelopes). The only difference is that the bands of Envelopes are plotted a fixed distance (%) away from the [moving average](/en/docs/mt5/client/indicators/trend_indicators/ma), while the Bollinger Bands are plotted a certain number of standard deviations away from it. Standard deviation is a measure of volatility, therefore Bollinger Bands adjust themselves to the market conditions. When the markets become more volatile, the bands widen and they contract during less volatile periods.

Bollinger Bands are usually drawn on the price chart, but they can be also added to the indicator chart. Just like in case of the [Envelopes](/en/docs/mt5/client/indicators/trend_indicators/envelopes), the interpretation of the Bollinger Bands is based on the fact that the prices tend to remain in between the top and the bottom line of the bands. A distinctive feature of the Bollinger Band indicator is its variable width due to the volatility of prices. In periods of considerable price changes (i.e. of high volatility) the bands widen leaving a lot of room to the prices to move in. During standstill periods, or the periods of low volatility the band contracts keeping the prices within their limits.

The following traits are particular to the Bollinger Band:

1.  abrupt changes in prices tend to happen after the band has contracted due to decrease of volatility;
2.  if prices break through one of the bands, a continuation of the current trend is to be expected;
3.  if the pikes and hollows outside the band are followed by pikes and hollows inside the band, a reverse of trend may occur;
4.  the price movement that has started from one of the band’s lines usually reaches the opposite one.

The last observation is useful for forecasting price guideposts.

![Bollinger Bands](/en/docs/mt5/client/img/bollinger_bands.png "Bollinger Bands")

## Calculation

Bollinger bands are formed by three lines. The middle line (ML) is a usual [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma).

ML = SUM (CLOSE, N) / N = SMA (CLOSE, N)

The top line (TL) is the same as the middle line shifted up by a certain number of standard deviations (D).

TL = ML + (D \* StdDev)

The bottom line (BL) is the middle line shifted down by the same number of standard deviations.

BL = ML - (D \* StdDev)

Where:

SUM (..., N) is the sum for N periods;  
CLOSE is the close price;  
N is the number of period used for calculations;  
SMA is a [simple moving average](/en/docs/mt5/client/indicators/trend_indicators/ma#sma);  
SQRT is a square root;  
StdDev means standard deviation:

StdDev = SQRT (SUM ((CLOSE — SMA (CLOSE, N))^2, N)/N)

It is recommended to use 20-period Simple Moving Average as the middle line, and plot top and bottom lines two standard deviations away from it. Besides, moving averages of less than 10 periods are of little effect.

[Average Directional Movement Index Wilder](/en/docs/mt5/client/indicators/trend_indicators/admiw)

[Double Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/dema)