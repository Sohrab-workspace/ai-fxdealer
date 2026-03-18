# Market Facilitation Index

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/bw_indicators/market_facilitation

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)Market Facilitation Index

# Market Facilitation Index

Market Facilitation Index Technical Indicator (BW MFI) is the indicator which shows the change of price for one tick. Absolute values of the indicator do not mean anything as they are, only indicator changes have sense. Bill Williams emphasizes the interchanging of MFI and volume:

-   Market Facilitation Index increases and volume increases — this points out that: a) the number of players coming into the market increases (volume increases) b) the new coming players open positions in the direction of bar development, i.e., the movement has begun and picks up speed.
-   Market Facilitation Index falls and volume falls. It means the market participants are not interested anymore.
-   Market Facilitation Index increases, but the volume falls. It is most likely, that the market is not supported with the volume from traders, and the price is changing due to speculations of the floor traders (broker agents and dealers).
-   Market Facilitation Index falls, but the volume increases. There is a battle between bulls and bears, characterized by a large sell and buy volume, but the price is not changing significantly since the forces are equal. One of the contending parties (buyers vs. sellers) will eventually win the battle. Usually, the break of such a bar lets you know if this bar determines the continuation of the trend or annuls the trend. Bill Williams calls such bar "curtsying".

![Market Facilitation Index](/en/docs/mt5/client/img/market_facilitation.png "Market Facilitation Index")

## Calculation

To calculate Market Facilitation Index you need to subtract the lowest bar price from the highest bar price and divide it by the volume.

BW MFI = (HIGH - LOW) / VOLUME

Where:

HIGH — the highest price of the bar;  
LOW — the lowest price of the bar;  
VOLUME — volume of the current bar.

[Gator Oscillator](/en/docs/mt5/client/indicators/bw_indicators/go)

[Analytical Objects](/en/docs/mt5/client/objects)