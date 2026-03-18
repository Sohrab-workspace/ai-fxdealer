# Alligator

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators/alligator

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)[Technical Indicators](/en/docs/mt4/terminal/analytics/tech_indicators)Alligator

# Alligator

"Most of the time the market remains stationary. Only for some 1530% of time the market generates trends, and traders who are not located in the exchange itself derive most of their profits from the trends. My Grandfather used to repeat: "Even a blind chicken will find its corns, if it is always fed at the same time". We call the trade on the trend "a blind chicken market". It took us years, but we have produced an indicator, that lets us always keep our powder dry until we reach the blind chicken market"

Bill Williams

In principle, Alligator Technical Indicator is a combination of Balance Lines ([Moving Averages](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average)) that use fractal geometry and nonlinear dynamics.

-   The blue line (Alligators Jaw) is the Balance Line for the timeframe that was used to build the chart (13-period [Smoothed Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average), moved into the future by 8 bars);
-   The red line (Alligators Teeth) is the Balance Line for the value timeframe of one level lower (8-period [Smoothed Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average), moved by 5 bars into the future);
-   The green line (Alligators Lips) is the Balance Line for the value timeframe, one more level lower (5-period [Smoothed Moving Average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average), moved by 3 bars into the future).

Lips, Teeth and Jaw of the Alligator show the interaction of different time periods. As clear trends can be seen only 15 to 30 per cent of the time, it is essential to follow them and refrain from working on markets that fluctuate only within certain price periods.

When the Jaw, the Teeth and the Lips are closed or intertwined, it means the Alligator is going to sleep or is asleep already. As it sleeps, it gets hungrier and hungrier — the longer it will sleep, the hungrier it will wake up. The first thing it does after it wakes up is to open its mouth and yawn. Then the smell of food comes to its nostrils: flesh of a bull or flesh of a bear, and the Alligator starts to hunt it. Having eaten enough to feel quite full, the Alligator starts to lose the interest to the food/price (Balance Lines join together) — this is the time to fix the profit.

![chart_alligator](/en/docs/mt4/terminal/img/chart_alligator.png)

## Calculation

MEDIAN PRICE = (HIGH + LOW) / 2

ALLIGATORS JAW = SMMA (MEDEAN PRICE, 13, 8)

ALLIGATORS TEETH = SMMA (MEDEAN PRICE, 8, 5)

ALLIGATORS LIPS = SMMA (MEDEAN PRICE, 5, 3)

where:  
MEDIAN PRICE — median price;  
HIGH — the highest price of the bar;  
LOW — the lowest price of the bar;  
SMMA (A, B, C) — [smoothed moving average](/en/docs/mt4/terminal/analytics/tech_indicators/moving_average#smoothed_moving_average). A parameter is for data to be smoothed, B is the smoothing period, C is shift to future. For example, SMMA (MEDIAN PRICE, 5, 3) means that the smoothed moving average will be calculated on the median price, smoothing period being equal to 5 bars and shift being 3;  
ALLIGATORS JAW — Alligator's jaws (blue line);  
ALLIGATORS TEETH — Alligator's teeth (red line);  
ALLIGATORS LIPS — Alligator's lips (green line).

[Accumulation/Distribution](/en/docs/mt4/terminal/analytics/tech_indicators/accumulation_distribution)

[Average Directional Movement Index](/en/docs/mt4/terminal/analytics/tech_indicators/average_directional_movement)