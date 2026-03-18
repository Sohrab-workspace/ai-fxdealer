# Relative Vigor Index

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/oscillators/rvi

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Oscillators](/en/docs/mt5/client/indicators/oscillators)Relative Vigor Index

# Relative Vigor Index

The main point of Relative Vigor Index Technical Indicator (RVI) is that on the bull market the closing price is, as a rule, higher, than the opening price. It is the other way round on the bear market. So the idea behind Relative Vigor Index is that the vigor, or energy, of the move is thus established by where the prices end up at the close. To normalize the index to the daily trading range, divide the change of price by the maximum range of prices for the day. To make a more smooth calculation, one uses [Simple Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#sma). 10 is considered the best period. To avoid probable ambiguity one needs to construct a signal line, which is a 4-period symmetrically weighted moving average of Relative Vigor Index values. The concurrence of lines serves as a signal to buy or to sell.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_rvi" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Relative Vigor Index](/en/docs/mt5/client/img/rvi.png "Relative Vigor Index")

## Calculation

RVI is calculated similarly to [Stochastic Oscillator](/en/docs/mt5/client/indicators/oscillators/so). However, the Vigor Index compares close levels relative to opening levels, and not the minimal price as is done by Stochastic. The indicator is calculated as the value equal to the actual price change for the period, normalized to the maximal range of price change for this period, for example a day or hour.

RVI = (CLOSE - OPEN) / (HIGH - LOW)

Where:

OPEN — opening price;  
HIGH — highest price;  
LOW — lowest price;  
CLOSE — closing price.

Usually RVI is displayed as two lines:

1\. The first one is build the same as RVI, but instead of Close and Open price difference and High and Low price difference sums of 4-period symmetrically weighted moving averages are used. I.e. the 4-period symmetrically weighted average of a numerator is calculated:

MovAverage = (CLOSE-OPEN) + 2 \* (CLOSE-1 - OPEN-1) + 2 \* (CLOSE-2 - OPEN-2) + (CLOSE-3 - OPEN-3)

Where:

CLOSE — current close price;  
CLOSE-1, CLOSE-2, CLOSE-3 — close prices 1, 2 and 3 periods ago;  
OPEN — current open price;  
OPEN-1, OPEN-2, OPEN-3 — open prices 1, 2 and 3 periods ago.

Then the 4-period symmetrically weighted moving average of a denominator is found:

RangeAverage = (HIGH-LOW) + 2 x (HIGH-1 - LOW-1) + 2 x (HIGH-2 - LOW-2) + (HIGH-3 - LOW-3),

Where:

HIGH — maximal price of the last bar;  
HIGH, HIGH-2, HIGH-3 — maximal prices 1, 2 and 3 periods ago;  
LOW — minimal price of the last bar;  
LOW-1, LOW-2, LOW-3 — minimal prices 1, 2 and 3 periods ago.

After that we calculate the sum of these moving averages for the last 4 periods, for example hours or days:

![rvi_formula](/en/docs/mt5/client/img/rvi_formula.png)

2\. The second line is the 4-period symmetrically weighted moving average of the first line:

RVIsignal = (RVIaverage + 2 \* RVIaverage-1 + 2 \* RVIaverage-2 + RVIaverage-3)/6

[Relative Strength Index](/en/docs/mt5/client/indicators/oscillators/rsi)

[Stochastic Oscillator](/en/docs/mt5/client/indicators/oscillators/so)