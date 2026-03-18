# Technical Indicators

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/analytics/tech_indicators

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Analytics](/en/docs/mt4/terminal/analytics)Technical Indicators

# Technical Indicators

Technical indicator is a mathematical manipulation of a security price and/or volumes aimed at forecasting of future price changes. Decisions about how and when to open or close positions can be made on basis of signals from technical indicators. According to their functionalities, indicators can be divided into two groups: trend indicators and oscillators. Trend indicators help to assess the price direction and detect the turn moments synchronously or with a delay. Oscillators allow to find the turning moments ahead or synchronously.

Indicators are imposed into the chart from the ["Navigator" window](/en/docs/mt4/terminal/overview/navigator) by means of Drag\`n\`Drop technique, by execution of the ["Insert — Indicators" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert) command, or by pressing of the ![tb_charts_indicators](/en/docs/mt4/terminal/img/tb_charts_indicators.png) button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts). A technical indicator can be drawn in a separate indicator window that has a specific vertical scale (for example, MACD)

![chart_MACD](/en/docs/mt4/terminal/img/chart_macd.png)

or it can be imposed directly into the price chart (for example, Moving Average).

![chart_MA](/en/docs/mt4/terminal/img/chart_ma.png)

At that, indicators can be drawn not only for price data and derivatives thereof (Median Price, Typical Price, Weighted Close), but also for other indicators. For example, Moving Average for Awesome Oscillator can be drawn, and a signal line can be obtained additionally to AO in this way. To do so, one has to draw AO indicator first, and then, using Drag\`n\`Drop technique, impose MA into AO and select "Previous Indicator Data" option in its settings in the "Apply to" option. If the "First Indicator Data" option is selected, MA will be drawn on basis of data of the very first imposed indicator that can be other than AO.

Besides analytical parameters, one can set colors for various elements, thickness of lines, and sizes of signs used, at setting up of the indicator. Moreover, the visualization mode of the object for different timeframes can be changed in the "Visualization" tab. At that, indicator will be shown on at timeframes that have been selected. This function can be useful if the tool has different settings for different timeframes. Using the "Show in the Data Window" option in the same tab, one can control over visualization of information about indicators in the ["Data Window"](/en/docs/mt4/terminal/overview/data_window).

All settings can be changed. To do so, one has to select the desired indicator in the "Indicators List" window and press the "Edit" button or execute the "Properties..." command of the indicator context menu.

![indicator_properties_parameters](/en/docs/mt4/terminal/img/indicator_properties_parameters.png)

Indicator context menu can be called by clicking with the right mouse button on a line, sign, or diagram of the desired indicator. To remove an indicator, one has to execute the "Delete Indicator" indicator context menu command or the "Delete Indicator Window" command in the chart or indicator context menus. The "Delete Indicator Window" command closes the indicator window.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Having placed cursor near a line, a sign, or a column border of an indicator histogram, one can determine precise value of this given indicator in this point.</span></p></td></tr></tbody></table>

[Line Studies](/en/docs/mt4/terminal/analytics/objects_control/line_studies)

[Accelerator/Decelerator Oscillator](/en/docs/mt4/terminal/analytics/tech_indicators/accelerator_decelerator)