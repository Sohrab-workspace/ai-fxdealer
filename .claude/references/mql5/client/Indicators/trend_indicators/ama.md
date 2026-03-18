# Adaptive Moving Average

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/ama

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Adaptive Moving Average

# Adaptive Moving Average

Adaptive Moving Average (AMA) Technical Indicator is used for constructing a moving average with low sensitivity to price series noises and is characterized by the minimal lag for trend detection. This indicator was developed and described by Perry Kaufman in his book "Smarter Trading".

One of disadvantages of different smoothing algorithms for price series is that accidental price leaps can result in the appearance of false trend signals. On the other hand, smoothing leads to the unavoidable lag of a signal about trend stop or change. This indicator was developed for eliminating these two disadvantages.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_ama" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Adaptive Moving Average](/en/docs/mt5/client/img/ama.png "Adaptive Moving Average")

## Calculation

To define the current market state Kaufman introduced the notion of Efficiency Ratio (ER), which is calculated by the below formula:

ER(i) = Signal(i)/Noise(i)

Where:

ER(i) — current value of the Efficiency Ratio;  
Signal(i) = ABS(Price(i) - Price(i - N)) — current signal value, absolute value of difference between the current price and price N period ago;  
Noise(i) = Sum(ABS(Price(i) - Price(i-1)),N) — current noise value, sum of absolute values of the difference between the price of the current period and price of the previous period for N periods.

At a strong trend the Efficiency Ratio (ER) will tend to 1; if there is no directed movement, it will be a little more than 0. The obtained value of ER is used in the exponential smoothing formula:

EMA(i) = Price(i) \* SC + EMA(i-1) \* (1 - SC)

Where:

SC = 2/(n+1) — EMA smoothing constant, n — period of the exponential moving;  
EMA(i-1) — previous value of EMA.

The smoothing ratio for the fast market must be as for EMA with period 2 (fast SC = 2/(2+1) = 0.6667), and for the period of no trend EMA period must be equal to 30 (slow SC = 2/(30+1) = 0.06452). Thus the new changing smoothing constant is introduced (scaled smoothing constant) SSC:

SSC(i) = (ER(i) \* ( fast SC - slow SC) + slow SC

or

SSC(i) = ER(i) \* 0.60215 + 0.06425

For a more efficient influence of the obtained smoothing constant on the averaging period Kaufman recommends squaring it.

Final calculation formula:

AMA(i) = Price(i) \* (SSC(i)^2) + AMA(i-1)\*(1-SSC(i)^2)

or (after rearrangement):

AMA(i) = AMA(i-1) + (SSC(i)^2) \* (Price(i) - AMA(i-1))

Where:

AMA(i) — current value of AMA;  
AMA(i—1) — previous value of AMA;  
SSC(i)  — current value of the scaled smoothing constant.

[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)

[Average Directional Movement Index](/en/docs/mt5/client/indicators/trend_indicators/admi)