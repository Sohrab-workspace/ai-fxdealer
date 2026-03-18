# Double Exponential Moving Average

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/dema

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Double Exponential Moving Average

# Double Exponential Moving Average

Double Exponential Moving Average Technical Indicator (DEMA) was developed by Patrick Mulloy and published in February 1994 in the "Technical Analysis of Stocks & Commodities" magazine. It is used for smoothing price series and is applied directly on a price chart of a financial security. Besides, it can be used for smoothing values of other indicators.

The advantage of this indicator is that it eliminates false signals at the saw-toothed price movement and allows saving a position at a strong trend.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_dema" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Double Exponential Moving Average](/en/docs/mt5/client/img/dema.png "Double Exponential Moving Average")

## Calculation

This indicator is based on the [Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#ema) (EMA). Let's view the error of price deviation from EMA value:

err(i) = Price(i) - EMA(Price, N, i)

Where:

err(i)  — current EMA error;  
Price(i) — current price;  
EMA(Price, N, i) — current EMA value of Price series with N period.

Let's add the value of the exponential average error to the value of the exponential moving average of a price and we will receive DEMA:

DEMA(i) = EMA(Price, N, i) + EMA(err, N, i) = EMA(Price, N, i) + EMA(Price - EMA(Price, N, i), N, i) =

\= 2 \* EMA(Price, N, i) - EMA(Price - EMA(Price, N, i), N, i) = 2 \* EMA(Price, N, i) - EMA2(Price, N, i)

Where:

EMA(err, N, i) — current value of the exponential average of error err;  
EMA2(Price, N, i) — current value of the double consequential smoothing of prices.

[Bollinger Bands](/en/docs/mt5/client/indicators/trend_indicators/bb)

[Envelopes](/en/docs/mt5/client/indicators/trend_indicators/envelopes)