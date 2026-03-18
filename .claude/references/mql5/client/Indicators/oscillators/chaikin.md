# Chaikin Oscillator

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/oscillators/chaikin

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Oscillators](/en/docs/mt5/client/indicators/oscillators)Chaikin Oscillator

# Chaikin Oscillator

Chaikin's Oscillator (CHO) is the difference of moving averages of [Accumulation/Distribution](/en/docs/mt5/client/indicators/volume_indicators/ad).

"The concept of this oscillator is based on three main theses. First: if a share or an index is higher when it closes than it was during the day (you can calculate the average value as \[max+min\]/2), it means that it was a day of accumulation. The closer the closing index of a share or an index gets to the maximum, the more active the accumulation is. Vice versa, if a share's closing price is lower than the average level of the day, it means that distribution took place. The closer to the minimum the share gets, the more active is the distribution.

Second: stable price growth is accompanied by increase in trade volume and strong accumulation of the volume. As the volume is like fuel that feeds market growth, the lag of volume along with the growth of prices shows that there isn't enough fuel to continue the rise.

Vice versa, a slump in prices is usually accompanied by low amount and ends up in panic liquidation of positions by institutional investors. Therefore, first of all we see a growth of volume, then a slump in prices accompanied by reduced volume and finally, when the market is close to foundation, some accumulation takes place.

Third: with a Chaikin's oscillator you can trace back the volume of money resources coming in to the market and leaving it. Comparing the dynamics of volume and prices allows finding out peaks and foundations of the market, both short- and medium-term.

As there are no correct methods of technical analysis, I would recommend you using this oscillator along with other technical indicators. The reliability of short-term and medium-term trade signals will be higher if you use a Chaikin's oscillator together with, for example, [Envelopes](/en/docs/mt5/client/indicators/trend_indicators/envelopes) based on a 21-day moving average and some oscillator of outbidding/resale.

The most important signal arises when the prices reach a maximum or a minimum level (especially on the level of outbidding/resale), but the Chaikin's oscillator can't overcome its previous extremum and so it turns around.

-   Signals moving in the direction of the medium-term trend are more reliable than those moving against it.
-   The fact that an oscillator confirms a new maximum or minimum doesn't mean that the prices will move on in that direction. I regard this event as unimportant.

Another way of using Chaikin's oscillator implies the following: a change in its direction is a signal for purchase or a sale, but only if it coincides with the price trend direction. For example, if a share is on the rise and its price is higher than a 90-day moving average, then an up-turn of the oscillator curve in the area of negative values can be regarded as a signal for purchase (but the share price must be higher than a 90-day moving average - not less).

A down-turn of the oscillator curve in the area of positive values (above zero) can be regarded as a signal for sale, but the share price must be lower than the 90-day moving average of closing prices."

![Chaikin Oscillator](/en/docs/mt5/client/img/chaikin_oscillator.png "Chaikin Oscillator")

## Calculation

To calculate the Chaikin's oscillator, you must subtract a 10-period exponential moving average of [Accumulation/Distribution](/en/docs/mt5/client/indicators/volume_indicators/ad) indicator from a 3-period exponential moving average of the same indicator.

CHO = EMA (A/D, 3) - EMA (A/D, 10)

Where:

EMA — exponential moving average;  
A/D — value of the Accumulation/Distribution indicator.

[Bulls Power](/en/docs/mt5/client/indicators/oscillators/bulls)

[Commodity Channel Index](/en/docs/mt5/client/indicators/oscillators/cci)