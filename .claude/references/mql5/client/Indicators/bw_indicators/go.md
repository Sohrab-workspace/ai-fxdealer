# Gator Oscillator

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/bw_indicators/go

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)Gator Oscillator

# Gator Oscillator

Gator Oscillator is based on the [Alligator](/en/docs/mt5/client/indicators/bw_indicators/alligator) and shows the degree of convergence/divergence of the Balance Lines ([Smoothed Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#smma)). The upper histogram is the absolute difference between the values of the blue and the red lines. The lower histogram is the absolute difference between the values of the red line and the green line, but with the minus sign, as the histogram chart is drawn top-down.

![Gator Oscillator](/en/docs/mt5/client/img/gator_oscillator.png "Gator Oscillator")

## Calculation

MEDIAN PRICE = (HIGH + LOW) / 2

ALLIGATORS JAW = SMMA (MEDIAN PRICE, 13, 8)

ALLIGATORS TEETH = SMMA (MEDIAN PRICE, 8, 5)

ALLIGATORS LIPS = SMMA (MEDIAN PRICE, 5, 3)

Where:

MEDIAN PRICE — median price;  
HIGH — the highest price of the bar;  
LOW — the lowest price of the bar;  
SMMA (A, B, C) — [Smoothed Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#smma). Parameter A — smoothed data, B — smoothing period, C — shift to future. For example, SMMA (MEDIAN PRICE, 5, 3) means that the smoothed moving average is taken from the median price, while the smoothing period is equal to 5 bars, and the shift is equal to 3 bars;  
ALLIGATORS JAW — Alligator's jaws (blue line);  
ALLIGATORS TEETH — Alligator's teeth (red line);  
ALLIGATORS LIPS — Alligator's lips (green line).

[Fractals](/en/docs/mt5/client/indicators/bw_indicators/fractals)

[Market Facilitation Index](/en/docs/mt5/client/indicators/bw_indicators/market_facilitation)