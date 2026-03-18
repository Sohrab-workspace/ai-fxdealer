# Technical Indicators

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
            -   [View and Configure Charts](/en/docs/mt5/client/charts)
            -   [Publish Online](/en/docs/mt5/client/mql5_charts)
            -   [Technical Indicators](/en/docs/mt5/client/indicators)
                -   [Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)
                -   [Oscillators](/en/docs/mt5/client/indicators/oscillators)
                -   [Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)
                -   [Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)
            -   [Analytical Objects](/en/docs/mt5/client/objects)
            -   [Fundamental Analysis](/en/docs/mt5/client/fundamental)
            -   [Additional Technical Indicators](/en/docs/mt5/client/charts_analysis_get_indicators)
            -   [Additional Features](/en/docs/mt5/client/charts_advanced)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)Technical Indicators

# Technical Indicators

An indicator is the most important tool for technical analysis. Decisions about how and when to trade can be made on the basis of technical indicator signals. The essence of technical indicators is a mathematical transformation of a financial symbol price aimed at forecasting future price changes. This provides an opportunity to identify various characteristics and patterns in price dynamics which are invisible to the naked eye.

## Types of Indicators [#](indicators#type)

In accordance with the functional properties, indicators can be divided into two types: [trend indicators](/en/docs/mt5/client/indicators/trend_indicators) and [oscillators](/en/docs/mt5/client/indicators/oscillators). Trend indicators help to identify the price direction and find trend reversal moments synchronously or with a delay. Oscillators allow to define market reversal points in advance or simultaneously.

A separate category includes indicators calculated based on [volumes](/en/docs/mt5/client/indicators/volume_indicators). For the Forex market, 'volume' means the number of ticks (price changes) within a time interval. For stock securities volume means the volume of executed trades (in contracts or money terms).

Another category is [Bill Williams' indicators](/en/docs/mt5/client/indicators/bw_indicators). They are included into a separate group because they are part of the trading system described in his books.

The above categories include built-in indicators of the trading platform. 38 indicators are available in the platform. A large number of custom technical indicators can also be used in the platform. You can download source codes of various free applications from the [Code Base](/en/docs/mt5/client/charts_analysis_get_indicators). Thousands of ready-to use applications for technical analysis and automated trading are also available on the [Market](/en/docs/mt5/client/market).

For convenience, all the indicators are divided into groups in the Navigator window.

![Groups of Indicators](/en/docs/mt5/client/img/indicator_category.png "Groups of Indicators")

## How to Run an Indicator on the Chart [#](indicators#run)

The most convenient way to apply an indicator is to drag it from the [Navigator](/en/docs/mt5/client/interface) window. You can also use the Indicators command from the [Insert](/en/docs/mt5/client/interface) menu or button ![Indicators](/en/docs/mt5/client/img/indicators_button.png "Indicators") on the [Standard](/en/docs/mt5/client/interface) toolbar.

![Applying an indicator on a chart](/en/docs/mt5/client/img/indicator_run.png "Applying an indicator on a chart")

A technical indicator can be drawn in a separate indicator window with its own vertical scale (for example, [MACD](/en/docs/mt5/client/indicators/oscillators/macd)) or applied directly onto a price chart (like [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma)).

## How to Change Settings of an Applied Indicator [#](indicators#modify)

The settings of a running indicator can be changed. Select the required indicator in the [Indicator List](/en/docs/mt5/client/charts_advanced/charts_objects_list#indicators) and click "Properties" or use the indicator context menu on the chart.

Use the context menu to manage indicators:

-   ![Indicator Properties](/en/docs/mt5/client/img/indicator_properties_icon.png "Indicator Properties") Properties — open [indicator properties](/en/docs/mt5/client/indicators#appearance);
-   ![Delete Indicator](/en/docs/mt5/client/img/delete_indicator_icon.png "Delete Indicator") Delete Indicator — remove the selected indicator from the chart;
-   ![Delete Indicators Window](/en/docs/mt5/client/img/delete_indicator_window.png "Delete Indicators Window") Delete Indicator Window — delete the indicator subwindow. This command is only available in the context menu of indicators running in a separate subwindow;
-   ![List of indicators](/en/docs/mt5/client/img/indicators_list_icon.png "List of indicators") Indicator List — open the [Indicator List](/en/docs/mt5/client/charts_advanced/charts_objects_list#indicators) window.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Moving a mouse cursor to a line, symbol or a histogram border of an indicator, you can precisely define the value of the indicator at this point.</span></p></td></tr></tbody></table>

## How to Customize the Indicator Appearance [#](indicators#appearance)

You can conveniently customize the appearance of indicators in the trading platform. You can set up the indicator parameters when applying it to a chart or modify them later. The indicator appearance is adjusted on the "Properties" tab:

![Customizing indicator appearance](/en/docs/mt5/client/img/indicator_appearance.gif "Customizing indicator appearance")

Indicator line color, width and style are set up in the "Style" field.

Display of various elements can be individually configured for [Ichimoku Kinko Hyo](/en/docs/mt5/client/indicators/trend_indicators/ikh), [Alligator](/en/docs/mt5/client/indicators/bw_indicators/alligator) and [custom indicators](/en/docs/mt5/client/trade_robots_indicators). The line color, width and type can be set on the "Colors" tab.

## How to Choose Data to Draw an Indicator [#](indicators#data)

Indicators can be plotted based on price data and derivatives thereof (Median Price, Typical Price, Weighted Close), as well as on the basis of other indicators. For example, you can apply [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma) to [Awesome Oscillator](/en/docs/mt5/client/indicators/bw_indicators/awesome) and have an additional AO signal line. First you need to draw the AO indicator, and then apply MA to it. In the MA settings select option "Previous Indicator's Data" in the "Apply to" field. If you choose "First Indicator's Data", MA will be applied to the very first added indicator, i.e. it can be any other indicator.

![Parameters](/en/docs/mt5/client/img/indicator_properties_parameters.png "Parameters")

Nine variants of indicator construction are available:

-   Close — based on close prices.
-   Open — based on open prices.
-   High — based on High prices.
-   Low — based on Low prices.
-   Median Price (HL/2) — based on the median price: (High + Low)/2.
-   Typical Price (HLC/3) — based on the typical price: (High + Low + Close)/3.
-   Weighted Close (HLCC/4) — based on the average weighted close price: (High + Low + 2\*Close)/4.
-   First indicator's data — based on the values of the first applied indicator. The option of using the data of the first indicator is only available for indicators in a separate window, because in the main chart window the first indicator is the price.
-   Previous indicator's data — based on the values of the previous indicator.

### How to Set Up Additional Indicator Levels [#](indicators#levels)

For some indicators, additional levels can be enabled. Open the "Levels" tab, click "Add" and enter the level value in the table. You can also optionally add the level description.

![Levels](/en/docs/mt5/client/img/indicator_properties_levels.png "Levels")

The line color, width and style for the levels can be set up below. To edit a level, click "Edit" or double-click on the appropriate field.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For indicators applied to a price chart, levels are drawn by summing the indicator values and the specified level. For indicators drawn in a separate subwindow, levels are drawn as horizontal lines through the specified value on the vertical scale.</span></p></td></tr></tbody></table>

### Indicator Display Settings [#](indicators#visualization)

The indicator display for different timeframes ([period](/en/docs/mt5/client/charts#operations)) can be set up on the "Visualization" tab. The indicator will only be displayed for the selected timeframes. This can be useful when the indicator is designed for use on specific timeframes.

![Indicator Display Settings](/en/docs/mt5/client/img/indicator_visualization.gif "Indicator Display Settings")

Option "Show in the Data Window" allows to manage indicator information displayed in the [Data Window](/en/docs/mt5/client/charts#datawindow).

Some indicators have additional scale settings. Indicator properties window has an additional "Scale" tab:

-   Inherit Scale — enable/disable scale inheritance from the first indicator in the window. If this option is enabled, the indicator has the same scale as the one applied prior to this one;
-   Scale by Line — enable/disable fixation of a certain indicator value in its subwindow using a drag-and-drop line. If this option is enabled, "scale percent" and "scale value" fields become active; the value of the indicator to be fixed can be specified there. Once the value is set, a line is added to the indicator window, using which you can set a fixed level of indicator values on the vertical scale;
-   Fixed Minimum — enable/disable fixation of a minimum value of the vertical scale of an indicator subwindow. If enabled, the option activates the field for entering the corresponding value;
-   Fixed Maximum — enable/disable fixation of a maximum value of the vertical scale of an indicator subwindow. If enabled, the option activates the field for entering the corresponding value.

[Publish Online](/en/docs/mt5/client/mql5_charts)

[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)