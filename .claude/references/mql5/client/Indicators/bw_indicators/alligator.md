# Alligator

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/bw_indicators/alligator

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)Alligator

# Alligator

Most of the time the market remains stationary. Only for some 15–30% of time the market generates trends, and traders who are not located in the exchange itself derive most of their profits from the trends. My Grandfather used to repeat: "Even a blind chicken will find its corns, if it is always fed at the same time". We call the trade on the trend "a blind chicken market". It took us years, but we have produced an indicator, that lets us always keep our powder dry until we reach the "blind chicken market".

Bill Williams

Alligator Technical Indicator is a combination of Balance Lines ([Moving Averages](/en/docs/mt5/client/indicators/trend_indicators/ma)) that use fractal geometry and nonlinear dynamics.

-   The blue line (Alligator's Jaw) is the Balance Line for the timeframe that was used to build the chart (13-period [Smoothed Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#smma), moved into the future by 8 bars);
-   Red Line (Alligator's Teeth) is the Balance Line for the value timeframe of one level lower (8-period [Smoothed Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#smma), moved by 5 bars into the future);
-   Green Line (Alligator's Lips) is the Balance Line for the value timeframe, one more level lower (5-period [Smoothed Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#smma), moved by 3 bars into the future).

Lips, Teeth and Jaw of the Alligator show the interaction of different time periods. As clear trends can be seen only 15 to 30 per cent of the time, it is essential to follow them and refrain from working on markets that fluctuate only within certain price periods.

When the Jaw, the Teeth and the Lips are closed or intertwined, it means the Alligator is going to sleep or is asleep already. As it sleeps, it gets hungrier and hungrier — the longer it will sleep, the hungrier it will wake up. The first thing it does after it wakes up is to open its mouth and yawn. Then the smell of food comes to its nostrils: flesh of a bull or flesh of a bear, and the Alligator starts to hunt it. Having eaten enough to feel quite full, the Alligator starts to lose the interest to the food/price (Balance Lines join together) — this is the time to fix the profit.

![Alligator](/en/docs/mt5/client/img/alligator.png "Alligator")

## Calculation

MEDIAN PRICE = (HIGH + LOW) / 2

ALLIGATORS JAW = SMMA (MEDIAN PRICE, 13, 8)

ALLIGATORS TEETH = SMMA (MEDIAN PRICE, 8, 5)

ALLIGATORS LIPS = SMMA (MEDIAN PRICE, 5, 3)

Where:

MEDIAN PRICE — median price;  
HIGH — the highest price of the bar;  
LOW — the lowest price of the bar;  
SMMA (A, B, C) — [Smoothed Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#smma). A parameter is for data to be smoothed, B is the smoothing period, C is shift to future. For example, SMMA (MEDIAN PRICE, 5, 3) means that the smoothed moving average will be calculated on the median price, smoothing period being equal to 5 bars and shift being 3;  
ALLIGATORS JAW — Alligator's jaws (blue line);  
ALLIGATORS TEETH — Alligator's teeth (red line);  
ALLIGATORS LIPS — Alligator's lips (green line).

[Accelerator Oscillator](/en/docs/mt5/client/indicators/bw_indicators/ao)

[Awesome Oscillator](/en/docs/mt5/client/indicators/bw_indicators/awesome)