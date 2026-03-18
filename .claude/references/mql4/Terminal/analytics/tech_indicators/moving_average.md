# Moving Average

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/moving_average

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)Moving Average

# Moving Average

The Moving Average Technical Indicator shows the mean instrument price value for a certain period of time. When one calculates the moving average, one averages out the instrument price for this time period. As the price changes, its moving average either increases, or decreases.

There are four different types of moving averages: [Simple (also referred to as Arithmetic)](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#simple_moving_average), [Exponential](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#exponential_moving_average), [Smoothed](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#smoothed_moving_average) and [Linear Weighted](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#linear_weighted_moving_average). Moving averages may be calculated for any sequential data set, including opening and closing prices, highest and lowest prices, trading volume or any other indicators. It is often the case when double moving averages are used.

The only thing where moving averages of different types diverge considerably from each other, is when weight coefficients, which are assigned to the latest data, are different. In case we are talking of simple moving average, all prices of the time period in question, are equal in value. [Exponential](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#exponential_moving_average) and [Linear Weighted](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#linear_weighted_moving_average) Moving Averages attach more value to the latest prices.

The most common way to interpreting the price moving average is to compare its dynamics to the price action. When the instrument price rises above its moving average, a buy signal appears, if the price falls below its moving average, what we have is a sell signal.

This trading system, which is based on the moving average, is not designed to provide entrance into the market right in its lowest point, and its exit right on the peak. It allows to act according to the following trend: to buy soon after the prices reach the bottom, and to sell soon after the prices have reached their peak.

Moving averages may also be applied to indicators. That is where the interpretation of indicator moving averages is similar to the interpretation of price moving averages: if the indicator rises above its moving average, that means that the ascending indicator movement is likely to continue: if the indicator falls below its moving average, this means that it is likely to continue going downward.

Here are the types of moving averages on the chart:

-   Simple Moving Average (SMA)
-   Exponential Moving Average (EMA)
-   Smoothed Moving Average (SMMA)
-   Linear Weighted Moving Average (LWMA)

![chart_MA](/en/docs/mt4/terminal/img/chart_ma.png)

## Calculation

### Simple Moving Average (SMA) [#](moving_average#simple_moving_average)

Simple, in other words, arithmetical moving average is calculated by summing up the prices of instrument closure over a certain number of single periods (for instance, 12 hours). This value is then divided by the number of such periods.

SMA = SUM(CLOSE, N) / N

Where:  
N — is the number of calculation periods.

### Exponential Moving Average (EMA) [#](moving_average#exponential_moving_average)

Exponentially smoothed moving average is calculated by adding the moving average of a certain share of the current closing price to the previous value. With exponentially smoothed moving averages, the latest prices are of more value. P-percent exponential moving average will look like:

EMA = (CLOSE(i) \* P) + (EMA(i - 1) \* (100 - P))

Where:  
CLOSE(i) — the price of the current period closure;  
EMA(i-1) — Exponentially Moving Average of the previous period closure;  
P — the percentage of using the price value.

### Smoothed Moving Average (SMMA) [#](moving_average#smoothed_moving_average)

The first value of this smoothed moving average is calculated as the simple moving average (SMA):

SUM1 = SUM(CLOSE, N)

SMMA1 = SUM1/N

The second and succeeding moving averages are calculated according to this formula:

PREVSUM = SMMA(i - 1) \* N

SMMA(i) = (PREVSUM - SMMA(i - 1) + CLOSE(i)) / N

Where:  
SUM1 — is the total sum of closing prices for N periods;  
PREVSUM — smoothed sum of previous bar;  
SMMA1 — is the smoothed moving average of the first bar;  
SMMA(i) — is the smoothed moving average of the current bar (except for the first one);  
CLOSE(i) — is the current closing price;  
N — is the smoothing period.

The formula can be simplified as a result of arithmetic manipulations:

SMMA (i) = (SMMA(i - 1) \* (N - 1) + CLOSE (i)) / N

### Linear Weighted Moving Average (LWMA) [#](moving_average#linear_weighted_moving_average)

In the case of weighted moving average, the latest data is of more value than more early data. Weighted moving average is calculated by multiplying each one of the closing prices within the considered series, by a certain weight coefficient.

LWMA = SUM(Close(i)\*i, N) / SUM(i, N)

Where:  
SUM(i, N) — is the total sum of weight coefficients.

[Money Flow Index](/en/docs/mt4/terminal/analytics/tech_indicators/money_flow_index)

[Moving Average Convergence/Divergence](/en/docs/mt4/terminal/analytics/tech_indicators/macd)