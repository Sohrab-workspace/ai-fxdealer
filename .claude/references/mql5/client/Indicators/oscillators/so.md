# Stochastic Oscillator

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/oscillators/so

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Oscillators](/en/docs/mt5/client/indicators/oscillators)Stochastic Oscillator

# Stochastic Oscillator

The Stochastic Oscillator Technical Indicator compares where a security’s price closed relative to its price range over a given time period. The Stochastic Oscillator is displayed as two lines. The main line is called %K. The second line, called %D, is a [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma) of %K. The %K line is usually displayed as a solid line and the %D line is usually displayed as a dotted line. There are several ways to interpret a Stochastic Oscillator. Three popular methods include:

-   Buy when the Oscillator (either %K or %D) falls below a specific level (for example, 20) and then rises above that level. Sell when the Oscillator rises above a specific level (for example, 80) and then falls below that level.
-   Buy when the %K line rises above the %D line and sell when the %K line falls below the %D line.
-   Look for divergences. For instance: where prices are making a series of new highs and the Stochastic Oscillator is failing to surpass its previous highs.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_stochastic" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Stochastic Oscillator ](/en/docs/mt5/client/img/stochastic.png "Stochastic Oscillator ")

## Calculation

Four variables are used for the calculation of the Stochastic Oscillator:

-   %K periods. This is the number of time periods used in the stochastic calculation.
-   %K Slowing Periods. This value controls the internal smoothing of %K. A value of 1 is considered a fast stochastic; a value of 3 is considered a slow stochastic.
-   %D periods. This is the number of time periods used when calculating a moving average of %K.
-   %D method. The method (i.e., Exponential, Simple, Smoothed, or Weighted) that is used to calculate %D.

The formula for %K is:

%K = (CLOSE - MIN (LOW (%K))) / (MAX (HIGH (%K)) - MIN (LOW (%K))) \* 100

Where:

CLOSE — today’s closing price;  
MIN (LOW (%K)) — the lowest minimum in %K periods;  
MAX (HIGH (%K)) — the highest maximum in %K periods.

The %D moving average is calculated according to the formula:

%D = SMA (%K, N)

Where:

N — smoothing period;  
SMA — [Simple Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#sma).

[Relative Vigor Index](/en/docs/mt5/client/indicators/oscillators/rvi)

[Triple Exponential Average](/en/docs/mt5/client/indicators/oscillators/tea)