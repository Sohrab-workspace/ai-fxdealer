# On Balance Volume

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/volume_indicators/obv

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)On Balance Volume

# On Balance Volume

On Balance Volume Technical Indicator (OBV) is a momentum technical indicator that relates volume to price change. The indicator, which Joseph Granville came up with, is pretty simple. If the close price of the current bar is higher than that of the previous bar, the volume of the current bar is added to the previous OBV. If the current bar close price is lower than of the previous one, the current volume is subtracted from the previous OBV.

The basic assumption, regarding On Balance Volume analysis, is that OBV changes precede price changes. The theory is that smart money can be seen flowing into the security by a rising OBV. When the public then moves into the security, both the security and the On Balance Volume will surge ahead.

If the security’s price movement precedes OBV movement, a "non-confirmation" has occurred. Non-confirmations can occur at bull market tops (when the security rises without, or before, the OBV) or at bear market bottoms (when the security falls without, or before, the On Balance Volume Technical Indicator).

The OBV is in a rising trend when each new peak is higher than the previous peak and each new trough is higher than the previous trough. Likewise, the On Balance Volume is in a falling trend when each successive peak is lower than the previous peak and each successive trough is lower than the previous trough. When the OBV is moving sideways and is not making successive highs and lows, it is in a doubtful trend.

Once a trend is established, it remains in force until it is broken. There are two ways in which the On Balance Volume trend can be broken. The first occurs when the trend changes from a rising trend to a falling trend, or from a falling trend to a rising trend.

The second way the OBV trend can be broken is if the trend changes to a doubtful trend and remains doubtful for more than three days. Thus, if the security changes from a rising trend to a doubtful trend and remains doubtful for only two days before changing back to a rising trend, the On Balance Volume is considered to have always been in a rising trend.

When the OBV changes to a rising or falling trend, a "breakout" has occurred. Since OBV breakouts normally precede price breakouts, investors should buy long on On Balance Volume upside breakouts. Likewise, investors should sell short when the OBV makes a downside breakout. Positions should be held until the trend changes.

![On Balance Volume](/en/docs/mt5/client/img/obv.png "On Balance Volume")

## Calculation

If the current close price is higher than the previous one, then:

OBV (i) = OBV (i - 1) + VOLUME (i).

If the current close price is lower than the previous one, then:

OBV (i) = OBV (i - 1) - VOLUME (i)

If the current close price is equal to the previous one, then:

OBV (i) = OBV (i - 1)

Where:

OBV (i) — value of the On Balance Volume indicator in the current period;  
OBV (i - 1) — value of the On Balance Volume indicator in the previous period;  
VOLUME (i) — volume of the current bar.

[Money Flow Index](/en/docs/mt5/client/indicators/volume_indicators/mfi)

[Volumes](/en/docs/mt5/client/indicators/volume_indicators/volumes)