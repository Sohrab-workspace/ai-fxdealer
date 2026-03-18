# Parabolic SAR

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/parabolic

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)Parabolic SAR

# Parabolic SAR

Parabolic SAR Technical Indicator was developed for analyzing the trending markets. The indicator is constructed on the price chart. This indicator is similar to the [Moving Average Technical Indicator](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average) with the only difference that Parabolic SAR moves with higher acceleration and may change its position in terms of the price. The indicator is below the prices on the bull market (Up Trend), when its bearish (Down Trend), it is above the prices.

If the price crosses Parabolic SAR lines, the indicator turns, and its further values are situated on the other side of the price. When such an indicator turn does take place, the maximum or the minimum price for the previous period would serve as the starting point. When the indicator makes a turn, it gives a signal of the trend end (correction stage or flat), or of its turn.

The Parabolic SAR is an outstanding indicator for providing exit points. Long positions should be closed when the price sinks below the SAR line, short positions should be closed when the price rises above the SAR line. It is often the case that the indicator serves as a trailing stop line.

If the long position is open (i.e., the price is above the SAR line), the Parabolic SAR line will go up, regardless of what direction the prices take. The length of the SAR line movement depends on the scale of the price movement.

![chart_parabolicSAR](/en/docs/mt4/terminal/img/chart_parabolicsar.png)

## Calculation

SAR(i) = SAR(i-1)+ACCELERATION\*(EPRICE(i-1)-SAR(i-1))

Where:  
SAR(i-1) — is the value of the indicator on the previous bar;  
ACCELERATION — is the acceleration factor;  
EPRICE(i-1) — is the highest (lowest) price for the previous period (EPRICE=HIGH for long positions and EPRICE=LOW for short positions).

The indicator value increases if the price of the current bar is higher than previous bullish and vice versa. The acceleration factor (ACCELERATION) will double at the same time, which would cause Parabolic SAR and the price to come together. In other words, the faster the price grows or sinks, the faster the indicator approaches the price.

[On Balance Volume](/en/docs/mt4/terminal/analytics/tech_indicators/on_balance_volume)

[Relative Strength Index](/en/docs/mt4/terminal/analytics/tech_indicators/relative_strength_index)