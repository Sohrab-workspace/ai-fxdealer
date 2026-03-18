# Bollinger Bands®

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/bollinger_bands

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
            -   [Graphical Objects](/en/docs/mt4/terminal/analytics/objects_control)
            -   [Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)
                -   [Accelerator/Decelerator Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/accelerator_decelerator)
                -   [Accumulation/Distribution](/en/docs/mt4/terminal/analytics/tech_indicators/accumulation_distribution)
                -   [Alligator](/en/docs/mt4/terminal/analytics/tech_indicators/alligator)
                -   [Average Directional Movement Index](/en/docs/mt4/terminal/analytics/tech_indicators/average_directional_movement)
                -   [Average True Range](/en/docs/mt4/terminal/analytics/tech_indicators/average_true_range)
                -   [Awesome Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/awesome_oscillator)
                -   [Bears Power](/en/docs/mt4/terminal/analytics/tech_indicators/bears_power)
                -   [Bollinger Bands](/en/docs/mt4/terminal/analytics/tech_indicators/bollinger_bands)
                -   [Bulls Power](/en/docs/mt4/terminal/analytics/tech_indicators/bulls_power)
                -   [Commodity Channel Index](/en/docs/mt4/terminal/analytics/tech_indicators/commodity_channel_index)
                -   [DeMarker](/en/docs/mt4/terminal/analytics/tech_indicators/demarker)
                -   [Envelopes](/en/docs/mt4/terminal/analytics/tech_indicators/envelopes)
                -   [Force Index](/en/docs/mt4/terminal/analytics/tech_indicators/force_index)
                -   [Fractals](/en/docs/mt4/terminal/analytics/tech_indicators/fractals)
                -   [Gator Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/gator_oscillator)
                -   [Ichimoku Kinko Hyo](/en/docs/mt4/terminal/analytics/tech_indicators/ichimoku)
                -   [Market Facilitation Index](/en/docs/mt4/terminal/analytics/tech_indicators/market_facilitation_index)
                -   [Momentum](/en/docs/mt4/terminal/analytics/tech_indicators/momentum)
                -   [Money Flow Index](/en/docs/mt4/terminal/analytics/tech_indicators/money_flow_index)
                -   [Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average)
                -   [Moving Average Convergence/Divergence](/en/docs/mt4/terminal/analytics/tech_indicators/macd)
                -   [Moving Average of Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average_oscillator)
                -   [On Balance Volume](/en/docs/mt4/terminal/analytics/tech_indicators/on_balance_volume)
                -   [Parabolic SAR](/en/docs/mt4/terminal/analytics/tech_indicators/parabolic)
                -   [Relative Strength Index](/en/docs/mt4/terminal/analytics/tech_indicators/relative_strength_index)
                -   [Relative Vigor Index](/en/docs/mt4/terminal/analytics/tech_indicators/relative_vigor_index)
                -   [Standard Deviation](/en/docs/mt4/terminal/analytics/tech_indicators/standard_deviation)
                -   [Stochastic Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/stochastic_oscillator)
                -   [Williams' Percent Range](/en/docs/mt4/terminal/analytics/tech_indicators/williams_percent_range)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)Bollinger Bands

# Bollinger Bands®

Bollinger Bands Technical Indicator (BB) is similar to [Envelopes](/en/docs/mt4/terminal/analytics/tech_indicators/envelopes). The only difference is that the bands of Envelopes are plotted a fixed distance (%) away from the [moving average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average), while the Bollinger Bands are plotted a certain number of standard deviations away from it. Standard deviation is a measure of volatility, therefore Bollinger Bands adjust themselves to the market conditions. When the markets become more volatile, the bands widen and they contract during less volatile periods.

Bollinger Bands are usually plotted on the price chart, but they can be also added to the indicator chart (Custom Indicators). Just like in case of the [Envelopes](/en/docs/mt4/terminal/analytics/tech_indicators/envelopes), the interpretation of the Bollinger Bands is based on the fact that the prices tend to remain in between the top and the bottom line of the bands. A distinctive feature of the Bollinger Band indicator is its variable width due to the volatility of prices. In periods of considerable price changes (i.e. of high volatility) the bands widen leaving a lot of room to the prices to move in. During standstill periods, or the periods of low volatility the band contracts keeping the prices within their limits.

The following traits are particular to the Bollinger Band:

1.  abrupt changes in prices tend to happen after the band has contracted due to decrease of volatility.
2.  if prices break through one of the bands, a continuation of the current trend is to be expected.
3.  if the pikes and hollows outside the band are followed by pikes and hollows inside the band, a reverse of trend may occur.
4.  the price movement that has started from one of the bands lines usually reaches the opposite one. The last observation is useful for forecasting price guideposts.

![chart_BollingerBands](/en/docs/mt4/terminal/img/chart_bollingerbands.png)

## Calculation

Bollinger bands are formed by three lines. The middle line (ML) is a usual Moving Average.

ML = SUM \[CLOSE, N\]/N

The top line (TL) is the same as the middle line shifted up by a certain number of standard deviations (D).

TL = ML + (D\*StdDev)

The bottom line (BL) is the middle line shifted down by the same number of standard deviations.

BL = ML — (D\*StdDev)

Where:  
N — is the number of periods used in calculation;  
SMA — [Simple Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average);  
StdDev — means Standard Deviation.  
StdDev = SQRT(SUM\[(CLOSE — SMA(CLOSE, N))^2, N\]/N)

It is recommended to use 20-period [Simple Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average) as the middle line, and plot top and bottom lines two standard deviations away from it. Besides, moving averages of less than 10 periods are of little effect.

[Bears Power](/en/docs/mt4/terminal/analytics/tech_indicators/bears_power)

[Bulls Power](/en/docs/mt4/terminal/analytics/tech_indicators/bulls_power)