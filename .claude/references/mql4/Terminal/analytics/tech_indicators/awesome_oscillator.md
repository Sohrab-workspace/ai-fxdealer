# Awesome Oscillator

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/awesome_oscillator

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)Awesome Oscillator

# Awesome Oscillator

Awesome Oscillator Technical Indicator (AO) is a 34-period simple moving average, plotted through the middle points of the bars (H+L)/2, which is subtracted from the 5-period simple moving average, built across the central points of the bars (H+L)/2. It shows us quite clearly whats happening to the market driving force at the present moment.

## Signals to buy

### Saucer

This is the only signal to buy that comes when the bar chart is higher than the nought line. One must bear in mind:

-   the saucer signal is generated when the bar chart reversed its direction from the downward to upward. The second column is lower than the first one and is colored red. The third column is higher than the second and is colored green.
-   for the saucer signal to be generated the bar chart should have at least three columns.

Keep in mind, that all Awesome Oscillator columns should be over the nought line for the saucer signal to be used.

### Nought line crossing

The signal to buy is generated when the bar chart passes from the area of negative values to that of positive. It comes when the bar chart crosses the nought line. As regards this signal:

-   for this signal to be generated, only two columns are necessary;
-   the first column is to be below the nought line, the second one is to cross it (transition from a negative value to a positive one);
-   simultaneous generation of signals to buy and to sell is impossible.

### Two pikes

This is the only signal to buy that can be generated when the bar chart values are below the nought line. As regards this signal, please, bear in mind:

-   the signal is generated, when you have a pike pointing down (the lowest minimum) which is below the nought line and is followed by another down-pointing pike which is somewhat higher (a negative figure with a lesser absolute value, which is therefore closer to the nought line), than the previous down-looking pike.
-   the bar chart is to be below the nought line between the two pikes. If the bar chart crosses the nought line in the section between the pikes, the signal to buy doesnt function. However, a different signal to buy will be generated — nought line crossing.
-   each new pike of the bar chart is to be higher (a negative number of a lesser absolute value that is closer to the nought line) than the previous pike.
-   if an additional higher pike is formed (that is closer to the nought line) and the bar chart has not crossed the nought line, an additional signal to buy will be generated.

## Signals to sell

Awesome Oscillator signals to sell are identical to the signals to buy. The saucer signal is reversed and is below zero. Nought line crossing is on the decrease — the first column of it is over the nought, the second one is under it. The two pikes signal is higher than the nought line and is reversed too.

![chart_AwesomeOscillator](/en/docs/mt4/terminal/img/chart_awesomeoscillator.png)

## Calculation

AO is a 34-period simple moving average, plotted through the central points of the bars (H+L)/2, and subtracted from the 5-period simple moving average, graphed across the central points of the bars (H+L)/2.

MEDIAN PRICE = (HIGH+LOW)/2

AO = SMA(MEDIAN PRICE, 5)-SMA(MEDIAN PRICE, 34)

Where:  
SMA — [Simple Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#simple_moving_average).

[Average True Range](/en/docs/mt4/terminal/analytics/tech_indicators/average_true_range)

[Bears Power](/en/docs/mt4/terminal/analytics/tech_indicators/bears_power)