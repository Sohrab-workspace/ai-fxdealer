# On Balance Volume

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/on_balance_volume

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)On Balance Volume

# On Balance Volume

On Balance Volume Technical Indicator (OBV) is a momentum technical indicator that relates volume to price change. The indicator, which Joseph Granville came up with, is pretty simple. When the security closes higher than the previous close, all of the days volume is considered up-volume. When the security closes lower than the previous close, all of the days volume is considered down-volume.

The basic assumption, regarding On Balance Volume analysis, is that OBV changes precede price changes. The theory is that smart money can be seen flowing into the security by a rising OBV. When the public then moves into the security, both the security and the On Balance Volume will surge ahead.

If the securitys price movement precedes OBV movement, a "non-confirmation" has occurred. Non-confirmations can occur at bull market tops (when the security rises without, or before, the OBV) or at bear market bottoms (when the security falls without, or before, the On Balance Volume Technical Indicator).

The OBV is in a rising trend when each new peak is higher than the previous peak and each new trough is higher than the previous trough. Likewise, the On Balance Volume is in a falling trend when each successive peak is lower than the previous peak and each successive trough is lower than the previous trough. When the OBV is moving sideways and is not making successive highs and lows, it is in a doubtful trend.

Once a trend is established, it remains in force until it is broken. There are two ways in which the On Balance Volume trend can be broken. The first occurs when the trend changes from a rising trend to a falling trend, or from a falling trend to a rising trend.

The second way the OBV trend can be broken is if the trend changes to a doubtful trend and remains doubtful for more than three days. Thus, if the security changes from a rising trend to a doubtful trend and remains doubtful for only two days before changing back to a rising trend, the On Balance Volume is considered to have always been in a rising trend.

When the OBV changes to a rising or falling trend, a "breakout" has occurred. Since OBV breakouts normally precede price breakouts, investors should buy long on On Balance Volume upside breakouts. Likewise, investors should sell short when the OBV makes a downside breakout. Positions should be held until the trend changes.

![chart_OBV](/en/docs/mt4/terminal/img/chart_obv.png)

## Calculation

If todays close is greater than yesterdays close then: OBV(i) = OBV(i-1)+VOLUME(i)

If todays close is less than yesterdays close then: OBV(i) = OBV(i-1)-VOLUME(i)

If todays close is equal to yesterdays close then: OBV(i) = OBV(i-1)

Where:

OBV(i) — is the indicator value of the current period;  
OBV(i-1) — is the indicator value of the previous period;  
VOLUME(i) — is the volume of the current bar.

[Moving Average of Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average_oscillator)

[Parabolic SAR](/en/docs/mt4/terminal/analytics/tech_indicators/parabolic)