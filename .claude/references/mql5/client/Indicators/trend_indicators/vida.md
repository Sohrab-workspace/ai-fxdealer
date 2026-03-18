# Variable Index Dynamic Average

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/vida

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Variable Index Dynamic Average

# Variable Index Dynamic Average

Variable Index Dynamic Average Technical Indicator (VIDYA) was developed by Tushar  Chande. It is an original method of calculating the [Exponential Moving Average (EMA)](/en/docs/mt5/client/indicators/trend_indicators/ma#ema) with the dynamically changing period of averaging. Period of averaging depends on the market volatility; as the measure of volatility Chande Momentum Oscillator (CMO) was chosen. This oscillator measures the ratio between the sum of positive increments and sum of negative increments for a certain period (CMO period). CMO value is used as the ratio to the smoothing factor EMA. Thus VIDYA has to setup parameters: period of CMO and period of EMA.

## Application

Usually not VIDYA itself is used in trading systems, but its upper and lower borders (Upper band & Lower band), that are by N% above and below VIDYA. Interpretation of the indicator for receiving trade signals in this form is performed similar to [Bollinger Bands®](/en/docs/mt5/client/indicators/trend_indicators/bb).

![Variable Index Dynamic Average](/en/docs/mt5/client/img/vidya.png "Variable Index Dynamic Average")

## Calculation

The standard [Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#ema) is calculated according to the below formula:

EMA(i) = Price(i) \* F + EMA(i-1)\*(1-F)

Where:

F = 2/(Period\_EMA+1) — smoothing factor;  
Period\_EMA — EMA averaging period;  
Price(i) — current price;  
EMA(i-1) — previous value of EMA.

The value of Variable Index Dynamic Average is calculated in the analogous way using CMO:

VIDYA(i) = Price(i) \* F \* ABS(CMO(i)) + VIDYA(i-1) \* (1 - F\* ABS(CMO(i)))

Where:

ABS(CMO(i)) — absolute current value Chande Momentum Oscillator;  
VIDYA(i-1) — previous value of VIDYA.

The value of CMO is calculated according to the below formula:

CMO(i) = (UpSum(i) - DnSum(i))/(UpSum(i) + DnSum(i))

Where:

UpSum(i) = current sum of positive price increments for the period;  
DnSum(i) = current sum of negative price increments for the period.

[Triple Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/tema)

[Oscillators](/en/docs/mt5/client/indicators/oscillators)