# Fractal Adaptive Moving Average

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/fama

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Fractal Adaptive Moving Average

# Fractal Adaptive Moving Average

Fractal Adaptive Moving Average Technical Indicator (FRAMA) was developed by John Ehlers. This indicator is constructed based on the algorithm of the [Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#ema), in which the smoothing factor is calculated based on the current fractal dimension of the price series. The advantage of FRAMA is the possibility to follow strong trend movements and to sufficiently slow down at the moments of price consolidation.

All types of analysis used for [Moving Averages](/en/docs/mt5/client/indicators/trend_indicators/ma) can be applied to this indicator.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_frama" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Fractal Adaptive Moving Average](/en/docs/mt5/client/img/frama.png "Fractal Adaptive Moving Average")

## Calculation

FRAMA(i) = A(i) \* Price(i) + (1 - A(i)) \* FRAMA(i-1)

Where:

FRAMA(i) — current value of FRAMA;  
Price(i) — current price;  
FRAMA(i-1) — previous value of FRAMA;  
A(i) — current factor of exponential smoothing.

Exponential smoothing factor is calculated according to the below formula:

A(i) = EXP(-4.6 \* (D(i) - 1))

Where:

D(i) — current fractal dimension;  
EXP() — mathematical function of exponent.

Fractal dimension of a straight line is equal to one. It is seen from the formula that if D = 1, then A = EXP(-4.6 \*(1-1)) = EXP(0) = 1. Thus if price changes in straight lines, exponential smoothing is not used, because in such a case the formula looks like this::

FRAMA(i) = 1 \* Price(i) + (1 — 1) \* FRAMA(i—1) = Price(i)

I.e. the indicator exactly follows the price.

The fractal dimension of a plane is equal to two. From the formula we get that if D = 2, then the smoothing factor A = EXP(-4.6\*(2-1)) = EXP(-4.6) = 0.01. Such a small value of the exponential smoothing factor is obtained at moments when price makes a strong saw-toothed movement. Such a strong slow-down corresponds to approximately 200-period simple moving average.

Formula of fractal dimension:

D = (LOG(N1 + N2) - LOG(N3))/LOG(2)

It is calculated based on the additional formula:

N(Length,i) = (HighestPrice(i) - LowestPrice(i))/Length

Where:

HighestPrice(i) — current maximal value for Length periods;  
LowestPrice(i) — current minimal value for Length periods;

Values N1, N2 and N3 are respectively equal to:

N1(i) = N(Length,i)

N2(i) = N(Length,i + Length)

N3(i) = N(2 \* Length,i)

[Envelopes](/en/docs/mt5/client/indicators/trend_indicators/envelopes)

[Ichimoku Kinko Hyo](/en/docs/mt5/client/indicators/trend_indicators/ikh)