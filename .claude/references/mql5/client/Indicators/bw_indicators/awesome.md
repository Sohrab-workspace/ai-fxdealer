# Awesome Oscillator

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/bw_indicators/awesome

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
                -   [Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)
                -   [Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)
                    -   [Accelerator Oscillator](/en/docs/mt5/client/indicators/bw_indicators/ao)
                    -   [Alligator](/en/docs/mt5/client/indicators/bw_indicators/alligator)
                    -   [Awesome Oscillator](/en/docs/mt5/client/indicators/bw_indicators/awesome)
                    -   [Fractals](/en/docs/mt5/client/indicators/bw_indicators/fractals)
                    -   [Gator Oscillator](/en/docs/mt5/client/indicators/bw_indicators/go)
                    -   [Market Facilitation Index](/en/docs/mt5/client/indicators/bw_indicators/market_facilitation)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)Awesome Oscillator

# Awesome Oscillator

Bill Williams's Awesome Oscillator Technical Indicator (AO) is a 34-period simple moving average, plotted through the bars midpoints (H+L)/2, which is subtracted from the 5-period simple moving average, built across the bars midpoints (H+L)/2. It shows us quite clearly what’s happening to the market driving force at the present moment.

## Signals to Buy

"Saucer" is the only signal to buy that comes when the bar chart is higher than the zero line. One must bear in mind:

-   the saucer signal is generated when the bar chart reversed its direction from the downward to upward. The second column is lower than the first one and is colored red. The third column is higher than the second and is colored green;
-   for the saucer signal to be generated the bar chart should have at least three columns.

Keep in mind, that all Awesome Oscillator columns should be over the zero line for the saucer signal to be used.

"Zero line crossing" is the signal to buy generated when the bar chart passes from the area of negative values to that of positive. It comes when the bar chart crosses the zero line. As regards this signal:

-   for this signal to be generated, only two columns are necessary;
-   the first column is to be below the zero line, the second one is to cross it (transition from a negative value to a positive one);
-   simultaneous generation of signals to buy and to sell is impossible.

"Twin peaks" is the only signal to buy that can be generated when the bar chart values are below the zero line. As regards this signal, please, bear in mind:

-   the signal is generated, when you have a peak pointing down (the lowest minimum) which is below the zero line and is followed by another down-pointing peak which is somewhat higher (a negative figure with a lesser absolute value, which is therefore closer to the zero line), than the previous down-looking peak;
-   the bar chart is to be below the zero line between the twin peaks. If the bar chart crosses the zero line in the section between the peaks, the signal to buy doesn’t function. However, a different signal to buy will be generated — zero line crossing;
-   each new peak of the bar chart is to be higher (a negative number of a lesser absolute value that is closer to the zero line) than the previous peak;
-   if an additional higher peak is formed (that is closer to the zero line) and the bar chart has not crossed the zero line, an additional signal to buy will be generated.

## Signals to Sell

Awesome Oscillator signals to sell are identical to the signals to buy. The saucer signal is reversed and is below zero. Zero line crossing is on the decrease — the first column of it is over the zero, the second one is under it. The twin peaks signal is higher than the zero line and is reversed too.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_ao" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Awesome Oscillator](/en/docs/mt5/client/img/ao.png "Awesome Oscillator")

## Calculation

AO is a 34-period simple moving average, plotted through the central points of the bars (H+L)/2, and subtracted from the 5-period simple moving average, graphed across the central points of the bars (H+L)/2.

MEDIAN PRICE = (HIGH + LOW) / 2

AO = SMA (MEDIAN PRICE, 5) - SMA (MEDIAN PRICE, 34)

Where:

MEDIAN PRICE — median price;  
HIGH — the highest price of the bar;  
LOW — the lowest price of the bar;  
SMA — [Simple Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#sma).

[Alligator](/en/docs/mt5/client/indicators/bw_indicators/alligator)

[Fractals](/en/docs/mt5/client/indicators/bw_indicators/fractals)