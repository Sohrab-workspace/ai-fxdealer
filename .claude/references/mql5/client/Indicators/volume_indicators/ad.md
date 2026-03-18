# Accumulation/Distribution

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/volume_indicators/ad

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
                    -   [Accumulation/Distribution](/en/docs/mt5/client/indicators/volume_indicators/ad)
                    -   [Money Flow Index](/en/docs/mt5/client/indicators/volume_indicators/mfi)
                    -   [On Balance Volume](/en/docs/mt5/client/indicators/volume_indicators/obv)
                    -   [Volumes](/en/docs/mt5/client/indicators/volume_indicators/volumes)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)Accumulation/Distribution

# Accumulation/Distribution

Accumulation/Distribution Technical Indicator is determined by the changes in price and volume. The volume acts as a weighting coefficient at the change of price — the higher the coefficient (the volume) is the greater the contribution of the price change (for this period of time) will be in the value of the indicator.

In fact, this indicator is a variant of the more commonly used indicator [On Balance Volume](/en/docs/mt5/client/indicators/volume_indicators/obv). They are both used to confirm price changes by means of measuring the respective volume of sales.

When the Accumulation/Distribution indicator grows, it means accumulation (buying) of a particular security, as the overwhelming share of the sales volume is related to an upward trend of prices. When the indicator drops, it means distribution (selling) of the security, as most of sales take place during the downward price movement.

Divergences between the Accumulation/Distribution indicator and the price of the security indicate the upcoming change of prices. As a rule, in case of such divergences, the price tendency moves in the direction in which the indicator moves. Thus, if the indicator is growing, and the price of the security is dropping, a turnaround of price should be expected.

![Accumulation/Distribution](/en/docs/mt5/client/img/ad.png "Accumulation/Distribution")

## Calculation

A certain share of the daily volume is added to or subtracted from the current accumulated value of the indicator. The nearer the closing price to the maximum price of the day is, the higher the added share will be. The nearer the closing price to the minimum price of the day is the greater the subtracted share will be. If the closing price is exactly in between the maximum and minimum of the day, the indicator value remains unchanged.

A/D(i) =((CLOSE(i) - LOW(i)) - (HIGH(i) - CLOSE(i)) \* VOLUME(i) / (HIGH(i) - LOW(i)) + A/D(i-1)

Where:

A/D(i) — value of the Accumulation/Distribution indicator for the current bar;  
CLOSE(i) — close price of the bar;  
LOW(i) — the lowest price of the bar;  
HIGH(i) — the highest price of the bar;  
VOLUME(i) — volume;  
A/D(i-1) — value of the Accumulation/Distribution indicator for the previous bar.

[Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)

[Money Flow Index](/en/docs/mt5/client/indicators/volume_indicators/mfi)