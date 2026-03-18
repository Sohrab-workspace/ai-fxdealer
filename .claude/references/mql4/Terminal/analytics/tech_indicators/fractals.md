# Fractals

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/fractals

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)Fractals

# Fractals

All markets are characterized by the fact that on the most part the prices do not change too much, and only short periods of time (1530 percent) account for trend changes. Most lucrative periods are usually the case when market prices change according to a certain trend.

A Fractal is one of five indicators of Bill Williams trading system, which allows to detect the bottom or the top.

Fractal Technical Indicator it is a series of at least five successive bars, with the highest HIGH in the middle, and two lower HIGHs on both sides. The reversing set is a series of at least five successive bars, with the lowest LOW in the middle, and two higher LOWs on both sides, which correlates to the sell fractal. The fractals are have High and Low values and are indicated with the up and down arrows.

The fractal needs to be filtrated with the use of [Alligator](/en/docs/mt4/terminal/analytics/tech_indicators/alligator). In other words, you should not close a buy transaction, if the fractal is lower than the Alligators Teeth, and you should not close a sell transaction, if the fractal is higher than the Alligators Teeth. After the fractal signal has been created and is in force, which is determined by its position beyond the Alligators Mouth, it remains a signal until it gets attacked, or until a more recent fractal signal emerges.

![chart_fractals](/en/docs/mt4/terminal/img/chart_fractals.png)

[Force Index](/en/docs/mt4/terminal/analytics/tech_indicators/force_index)

[Gator Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/gator_oscillator)