# MACD

> Source: https://support.metaquotes.net/en/docs/mt5/iphone/chart/indicators/oscillators/macd

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
                -   [Oscillators](/en/docs/mt5/iphone/chart/indicators/oscillators)
                    -   [Average True Range](/en/docs/mt5/iphone/chart/indicators/oscillators/average_true_range)
                    -   [Bears Power](/en/docs/mt5/iphone/chart/indicators/oscillators/bears_power)
                    -   [Bulls Power](/en/docs/mt5/iphone/chart/indicators/oscillators/bulls_power)
                    -   [Commodity Channel Index](/en/docs/mt5/iphone/chart/indicators/oscillators/commodity_channel_index)
                    -   [DeMarker](/en/docs/mt5/iphone/chart/indicators/oscillators/demarker)
                    -   [Force Index](/en/docs/mt5/iphone/chart/indicators/oscillators/force_index)
                    -   [MACD](/en/docs/mt5/iphone/chart/indicators/oscillators/macd)
                    -   [Momentum](/en/docs/mt5/iphone/chart/indicators/oscillators/momentum)
                    -   [Moving Average of Oscillator](/en/docs/mt5/iphone/chart/indicators/oscillators/moving_average_oscillator)
                    -   [Relative Strength Index](/en/docs/mt5/iphone/chart/indicators/oscillators/relative_strength_index)
                    -   [Relative Vigor Index](/en/docs/mt5/iphone/chart/indicators/oscillators/relative_vigor_index)
                    -   [Stochastic Oscillator](/en/docs/mt5/iphone/chart/indicators/oscillators/stochastic_oscillator)
                    -   [Williams' Percent Range](/en/docs/mt5/iphone/chart/indicators/oscillators/williams_percent_range)
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

[MetaTrader 5](/en/docs/mt5)[iPhone/iPad](/en/docs/mt5/iphone)[Chart](/en/docs/mt5/iphone/chart)[Indicators](/en/docs/mt5/iphone/chart/indicators)[Oscillators](/en/docs/mt5/iphone/chart/indicators/oscillators)MACD

# MACD

Moving Average Convergence/Divergence (MACD) is a trend-following dynamic indicator. It indicates the correlation between two [Moving Averages](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average) of a price.

The Moving Average Convergence/Divergence (MACD) Technical Indicator is the difference between a 26-period and 12-period [Exponential moving averages (EMA)](/en/docs/mt5/iphone/chart/indicators/trend_indicators/moving_average#ema). In order to clearly show buy/sell opportunities, a so-called signal line (9-period moving average of the indicator) is plotted on the MACD chart.

The MACD proves most effective in wide-swinging trading markets. There are three popular ways to use the Moving Average Convergence/Divergence: crossovers, overbought/oversold conditions, and divergences.

## Crossovers

The basic MACD trading rule is to sell when the MACD falls below its signal line. Similarly, a buy signal occurs when the Moving Average Convergence/Divergence rises above its signal line. It is also popular to buy/sell when the MACD goes above/below zero.

## Overbought/Oversold Conditions

The MACD is also useful as an overbought/oversold indicator. When the shorter moving average pulls away dramatically from the longer moving average (i.e., the MACD rises), it is likely that the symbol price is overextending and will soon return to more realistic levels.

## Divergences

An indication that an end to the current trend may be near occurs when the MACD diverges from the symbol. A bullish divergence occurs when the Moving Average Convergence/Divergence indicator is making new highs while prices fail to reach new highs. A bearish divergence occurs when the MACD is making new lows while prices fail to reach new lows. Both of these divergences are most significant when they occur at relatively overbought/oversold levels.

![Moving Average Convergence/Divergence](/en/docs/mt5/iphone/img/macd.png "Moving Average Convergence/Divergence")

## Calculation

The MACD is calculated by subtracting the value of a 26-period exponential moving average from a 12-period exponential moving average. A 9-period dotted simple moving average of the MACD (the signal line) is then plotted on top of the MACD.

MACD = EMA(CLOSE, 12) - EMA(CLOSE, 26)

SIGNAL = SMA(MACD, 9)

Where:

EMA — exponential moving average;  
SMA — simple moving average;  
SIGNAL — the signal line of the indicator.

[Force Index](/en/docs/mt5/iphone/chart/indicators/oscillators/force_index)

[Momentum](/en/docs/mt5/iphone/chart/indicators/oscillators/momentum)