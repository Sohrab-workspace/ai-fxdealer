# Fractals

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/bw_indicators/fractals

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)Fractals

# Fractals

All markets are characterized by the fact that on the most part the prices do not change too much, and only short periods of time (15–30 percent) account for trend changes. Most lucrative periods are usually the case when market prices change according to a certain trend.

A Fractal is one of five indicators of Bill Williams’ trading system, which allows to detect the bottom or the top. Technical definition of the upwards fractal is a series of at least five successive bars, with the highest HIGH in the middle, and two lower HIGHs on both sides. The reversing set is a series of at least five successive bars, with the lowest LOW in the middle, and two higher LOWs on both sides, which correlates to the sell fractal. The fractals have High and Low values and are indicated with the up and down arrows in a chart.

The Fractal signals need to be filtrated with the use of [Alligator](/en/docs/mt5/client/indicators/bw_indicators/alligator). In other words, you should not close a buy transaction, if the fractal is lower than the Alligator’s Teeth, and you should not close a sell transaction, if the fractal is higher than the Alligator’s Teeth. After the fractal signal has been created and is in force, which is determined by its position beyond the Alligator’s Mouth, it remains a signal until it gets attacked, or until a more recent fractal signal emerges.

![Fractals](/en/docs/mt5/client/img/fractals.png "Fractals")

[Awesome Oscillator](/en/docs/mt5/client/indicators/bw_indicators/awesome)

[Gator Oscillator](/en/docs/mt5/client/indicators/bw_indicators/go)