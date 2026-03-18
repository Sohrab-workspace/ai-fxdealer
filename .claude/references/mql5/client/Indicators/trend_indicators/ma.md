# Moving Average

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/ma

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Moving Average

# Moving Average

The Moving Average Technical Indicator shows the mean instrument price value for a certain period of time. When one calculates the moving average, one averages out the instrument price for this time period. As the price changes, its moving average either increases, or decreases.

There are four different types of moving averages: [Simple](/en/docs/mt5/client/indicators/trend_indicators/ma#sma) (also referred to as Arithmetic), [Exponential](/en/docs/mt5/client/indicators/trend_indicators/ma#ema), [Smoothed](/en/docs/mt5/client/indicators/trend_indicators/ma#smma) and [Weighted](/en/docs/mt5/client/indicators/trend_indicators/ma#lwma). Moving Average may be calculated for any sequential data set, including opening and closing prices, highest and lowest prices, trading volume or any other indicators. It is often the case when double moving averages are used.

The only thing where moving averages of different types diverge considerably from each other, is when weight coefficients, which are assigned to the latest data, are different. In case we are talking of [Simple Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#sma),  all prices of the time period in question are equal in value. [Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#ema) and [Linear Weighted Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#lwma) attach more value to the latest prices.

The most common way to interpreting the price moving average is to compare its dynamics to the price action. When the instrument price rises above its moving average, a buy signal appears, if the price falls below its moving average, what we have is a sell signal.

This trading system, which is based on the moving average, is not designed to provide entrance into the market right in its lowest point, and its exit right on the peak. It allows to act according to the following trend: to buy soon after the prices reach the bottom, and to sell soon after the prices have reached their peak.

Moving averages may also be applied to indicators. That is where the interpretation of indicator moving averages is similar to the interpretation of price moving averages: if the indicator rises above its moving average, that means that the ascending indicator movement is likely to continue: if the indicator falls below its moving average, this means that it is likely to continue going downward.

Here are the types of moving averages on the chart:

-   Simple Moving Average (SMA)
-   Exponential Moving Average (EMA)
-   Smoothed Moving Average (SMMA)
-   Linear Weighted Moving Average (LWMA)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_ma" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Moving Average](/en/docs/mt5/client/img/ma.png "Moving Average")

## Calculation

### Simple Moving Average (SMA) [#](ma#sma)

Simple, in other words, arithmetical moving average is calculated by summing up the prices of instrument closure over a certain number of single periods (for instance, 12 hours). This value is then divided by the number of such periods.

SMA = SUM (CLOSE (i), N) / N

Where:

SUM — sum;  
CLOSE (i) — current period close price;  
N — number of calculation periods.

### Exponential Moving Average (EMA) [#](ma#ema)

Exponentially smoothed moving average is calculated by adding of a certain share of the current closing price to the previous value of the moving average. With exponentially smoothed moving averages, the latest close prices are of more value. P-percent exponential moving average will look like:

EMA = (CLOSE (i) \* P) + (EMA (i - 1) \* (1 - P))

Where:

CLOSE (i) — current period close price;  
EMA (i - 1) — value of the Moving Average of a preceding period;  
P — the percentage of using the price value.

### Smoothed Moving Average (SMMA) [#](ma#smma)

The first value of this smoothed moving average is calculated as the simple moving average (SMA):

SUM1 = SUM (CLOSE (i), N)

SMMA1 = SUM1 / N

The second moving average is calculated according to this formula:

SMMA (i) = (SMMA1\*(N-1) + CLOSE (i)) / N

Succeeding moving averages are calculated according to the below formula:

PREVSUM = SMMA (i - 1) \* N

SMMA (i) = (PREVSUM - SMMA (i - 1) + CLOSE (i)) / N

Where:

SUM — sum;  
SUM1 — total sum of closing prices for N periods; it is counted from the previous bar;  
PREVSUM — smoothed sum of the previous bar;  
SMMA (i-1) — smoothed moving average of the previous bar;  
SMMA (i) — smoothed moving average of the current bar (except for the first one);  
CLOSE (i) — current close price;  
N — smoothing period.

After arithmetic conversions the formula can be simplified:

SMMA (i) = (SMMA (i - 1) \* (N - 1) + CLOSE (i)) / N

### Linear Weighted Moving Average (LWMA) [#](ma#lwma)

In the case of weighted moving average, the latest data is of more value than more early data. Weighted moving average is calculated by multiplying each one of the closing prices within the considered series, by a certain weight coefficient:

LWMA = SUM (CLOSE (i) \* i, N) / SUM (i, N)

Where:

SUM — sum;  
CLOSE(i) — current close price;  
SUM (i, N) — total sum of weight coefficients;  
N — smoothing period.

[Ichimoku Kinko Hyo](/en/docs/mt5/client/indicators/trend_indicators/ikh)

[Parabolic SAR](/en/docs/mt5/client/indicators/trend_indicators/psar)