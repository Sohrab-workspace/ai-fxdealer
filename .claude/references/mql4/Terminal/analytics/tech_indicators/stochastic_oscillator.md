# Stochastic Oscillator

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/stochastic_oscillator

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)Stochastic Oscillator

# Stochastic Oscillator

The Stochastic Oscillator Technical Indicator compares where a securitys price closed relative to its price range over a given time period. The Stochastic Oscillator is displayed as two lines. The main line is called %K. The second line, called %D, is a [Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average) of %K. The %K line is usually displayed as a solid line and the %D line is usually displayed as a dotted line.

There are several ways to interpret a Stochastic Oscillator. Three popular methods include:

-   Buy when the Oscillator (either %K or %D) falls below a specific level (for example, 20) and then rises above that level. Sell when the Oscillator rises above a specific level (for example, 80) and then falls below that level;
-   Buy when the %K line rises above the %D line and sell when the %K line falls below the %D line;
-   Look for divergences. For instance: where prices are making a series of new highs and the Stochastic Oscillator is failing to surpass its previous highs.

![chart_StochasticOs](/en/docs/mt4/terminal/img/chart_stochasticos.png)

## Calculation

The Stochastic Oscillator has four variables:

-   %K periods. This is the number of time periods used in the stochastic calculation;
-   %K Slowing Periods. This value controls the internal smoothing of %K. A value of 1 is considered a fast stochastic; a value of 3 is considered a slow stochastic;
-   %D periods. his is the number of time periods used when calculating a moving average of %K;
-   %D method. The method (i.e., Exponential, Simple, Smoothed, or Weighted) that is used to calculate %D.

The formula for %K is: %K = (CLOSE-LOW(%K))/(HIGH(%K)-LOW(%K))\*100

Where:  
CLOSE — is todays closing price;  
LOW(%K) — is the lowest low in %K periods;  
HIGH(%K) — is the highest high in %K periods.

The %D moving average is calculated according to the formula: %D = SMA(%K, N)

Where:  
N — is the smoothing period;  
SMA — is the [Simple Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#simple_moving_average).

[Standard Deviation](/en/docs/mt4/terminal/analytics/tech_indicators/standard_deviation)

[Williams' Percent Range](/en/docs/mt4/terminal/analytics/tech_indicators/williams_percent_range)