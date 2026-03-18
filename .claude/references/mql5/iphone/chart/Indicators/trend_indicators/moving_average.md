# Moving Average

> Source: https://support.metaquotes.net/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
        -   [Getting Started](/en/docs/mt5/iphone/getting_started)
        -   [Quotes](/en/docs/mt5/iphone/quotes)
        -   [Depth of Market](/en/docs/mt5/iphone/depth_of_market)
        -   [Chart](/en/docs/mt5/iphone/chart)
            -   [Indicators](/en/docs/mt5/iphone/chart/indicators)
                -   [Trend Indicators](/en/docs/mt5/iphone/chart/indicators/trend_indicators)
                    -   [Average Directional Movement Index](/en/docs/mt5/iphone/chart/indicators/trend_indicators/average_directional_movement_index)
                    -   [Bollinger Bands](/en/docs/mt5/iphone/chart/indicators/trend_indicators/bollinger_bands)
                    -   [Envelopes](/en/docs/mt5/iphone/chart/indicators/trend_indicators/envelopes)
                    -   [Ichimoku Kinko Hyo](/en/docs/mt5/iphone/chart/indicators/trend_indicators/ichimoku_kinko_hyo)
                    -   [Moving Average](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average)
                    -   [Parabolic SAR](/en/docs/mt5/iphone/chart/indicators/trend_indicators/parabolic_sar)
                    -   [Standard Deviation](/en/docs/mt5/iphone/chart/indicators/trend_indicators/standard_deviation)
                    -   [ZigZag](/en/docs/mt5/iphone/chart/indicators/trend_indicators/zigzag)
                -   [Oscillators](/en/docs/mt5/iphone/chart/indicators/oscillators)
                -   [Volume Indicators](/en/docs/mt5/iphone/chart/indicators/volume_indicators)
                -   [Bill Williams' Indicators](/en/docs/mt5/iphone/chart/indicators/bw_indicators)
            -   [Objects](/en/docs/mt5/iphone/chart/objects)
        -   [Trade](/en/docs/mt5/iphone/trade)
        -   [History](/en/docs/mt5/iphone/history)
        -   [Accounts](/en/docs/mt5/iphone/settings_accounts)
        -   [Mailbox](/en/docs/mt5/iphone/settings_mail)
        -   [News](/en/docs/mt5/iphone/settings_news)
        -   [Messages](/en/docs/mt5/iphone/settings_messages)
        -   [Push Notifications](/en/docs/mt5/iphone/push)
        -   [Settings](/en/docs/mt5/iphone/settings)
        -   [iPad Version](/en/docs/mt5/iphone/ipad)
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

[MetaTrader 5](/en/docs/mt5)[iPhone/iPad](/en/docs/mt5/iphone)[Chart](/en/docs/mt5/iphone/chart)[Indicators](/en/docs/mt5/iphone/chart/indicators)[Trend Indicators](/en/docs/mt5/iphone/chart/indicators/trend_indicators)Moving Average

# Moving Average

The Moving Average Technical Indicator shows the mean instrument price value for a certain period of time. When one calculates the moving average, one averages out the instrument price for this time period. As the price changes, its moving average either increases, or decreases.

There are four different types of moving averages: [Simple](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#sma) (also referred to as Arithmetic), [Exponential](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#ema), [Smoothed](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#smma) and [Weighted](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#lwma). Moving Average may be calculated for any sequential data set, including opening and closing prices, highest and lowest prices, trading volume or any other indicators. It is often the case when double moving averages are used.

The only thing where moving averages of different types diverge considerably from each other, is when weight coefficients, which are assigned to the latest data, are different. In case of the [Simple Moving Average](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#sma), all prices of the time period in question are equal in weight. [Exponential Moving Average](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#ema) and [Linear Weighted Moving Average](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#lwma) assign more weight to the latest prices.

The most common way to interpreting the price moving average is to compare its dynamics to the price action. When the instrument price rises above its moving average, a buy signal appears, if the price falls below its moving average, what we have is a sell signal.

This trading system, which is based on the moving average, is not designed to provide entrance into the market right in its lowest point, and its exit right on the peak. It allows to act according to the following trend: to buy soon after the prices reach the bottom, and to sell soon after the prices have reached their peak.

Moving averages may also be applied to indicators. That is where the interpretation of indicator moving averages is similar to the interpretation of price moving averages: if the indicator rises above its moving average, that means that the ascending indicator movement is likely to continue: if the indicator falls below its moving average, this means that it is likely to continue going downward.

Here are the types of moving averages on the chart:

-   Simple Moving Average (SMA)
-   Exponential Moving Average (EMA)
-   Smoothed Moving Average (SMMA)
-   Linear Weighted Moving Average (LWMA)

![Moving Average](/en/docs/mt5/iphone/img/moving_average.png "Moving Average")

## Calculation

### Simple Moving Average (SMA) [#](moving_average#sma)

Simple, in other words, arithmetical moving average is calculated by summing up the prices of instrument closure over a certain number of single periods (for instance, 12 hours). This value is then divided by the number of such periods.

SMA = SUM (CLOSE (i), N) / N

where:

SUM — the sum;  
CLOSE (i) — the current period close price;  
N — the number of calculation periods.

### Exponential Moving Average (EMA) [#](moving_average#ema)

Exponentially smoothed moving average is calculated by adding of a certain share of the current closing price to the previous value of the moving average. With exponentially smoothed moving averages, the latest close prices are of more value. P-percent exponential moving average will look like:

EMA = (CLOSE (i) \* P) + (EMA (i - 1) \* (1 - P))

where:

CLOSE (i) — the close price of the current period;  
EMA (i - 1) — the value of the Moving Average of the previous period;  
P — the percentage of using the price value.

### Smoothed Moving Average (SMMA) [#](moving_average#smma)

The first value of this smoothed moving average is calculated as the simple moving average (SMA):

SUM1 = SUM (CLOSE (i), N)

SMMA1 = SUM1 / N

The second moving average is calculated according to this formula:

SMMA (i) = (SMMA1\*(N-1) + CLOSE (i)) / N

Further moving averages are calculated using the following formula:

PREVSUM = SMMA (i - 1) \* N

SMMA (i) = (PREVSUM - SMMA (i - 1) + CLOSE (i)) / N

where:

SUM — the sum;  
SUM1 — the total sum of the close prices for N periods starting from the previous bar;  
PREVSUM — the smoothed sum of the previous bar;  
SMMA (i-1) — the smoothed moving average of the previous bar;  
SMMA (i) — the smoothed moving average of the current bar (except for the first bar);  
CLOSE (i) — the current close price;  
N — the period of smoothing.

The formula can be simplified by applying arithmetic transformation:

SMMA (i) = (SMMA (i - 1) \* (N - 1) + CLOSE (i)) / N

### Linear Weighted Moving Average (LWMA) [#](moving_average#lwma)

In the case of weighted moving average, the latest data is of more value than more early data. Weighted moving average is calculated by multiplying each one of the closing prices within the considered series, by a certain weight coefficient:

LWMA = SUM (CLOSE (i) \* i, N) / SUM (i, N)

where:

SUM — the sum;  
CLOSE(i) — the current close price;  
SUM (i, N) — the total sum of weight coefficients;  
N — the period of smoothing.

[Ichimoku Kinko Hyo](/en/docs/mt5/iphone/chart/indicators/trend_indicators/ichimoku_kinko_hyo)

[Parabolic SAR](/en/docs/mt5/iphone/chart/indicators/trend_indicators/parabolic_sar)