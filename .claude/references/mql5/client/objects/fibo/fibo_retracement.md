# Fibonacci Retracement

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/fibo/fibo_retracement

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
            -   [Analytical Objects](/en/docs/mt5/client/objects)
                -   [Lines](/en/docs/mt5/client/objects/lines)
                -   [Channels](/en/docs/mt5/client/objects/channels)
                -   [Fibonacci Tools](/en/docs/mt5/client/objects/fibo)
                    -   [Fibonacci Retracement](/en/docs/mt5/client/objects/fibo/fibo_retracement)
                    -   [Fibonacci Time Zones](/en/docs/mt5/client/objects/fibo/fibo_timezones)
                    -   [Fibonacci Fan](/en/docs/mt5/client/objects/fibo/fibo_fan)
                    -   [Fibonacci Arcs](/en/docs/mt5/client/objects/fibo/fibo_arcs)
                    -   [Fibonacci Channel](/en/docs/mt5/client/objects/fibo/fibo_channel)
                    -   [Fibonacci Expansion](/en/docs/mt5/client/objects/fibo/fibo_expansion)
                -   [Gann Tools](/en/docs/mt5/client/objects/gann)
                -   [Elliott Tools](/en/docs/mt5/client/objects/elliott)
                -   [Shapes](/en/docs/mt5/client/objects/shapes)
                -   [Arrows](/en/docs/mt5/client/objects/arrows)
                -   [Graphical Objects](/en/docs/mt5/client/objects/graphical_objects)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Fibonacci Tools](/en/docs/mt5/client/objects/fibo)Fibonacci Retracement

# Fibonacci Retracement

Fibonacci Retracement is built as follows: first, a [trendline](/en/docs/mt5/client/objects/lines/trend_line) is built between two extreme points, for example, from the trough to the opposing peak. Then, nine horizontal lines intersecting the trend line at Fibonacci levels of 0.0, 23.6, 38.2, 50, 61.8, 100, 161.8, 261.8, and 423.6 percent are drawn. After a significant rise or decline, prices often return to their previous levels correcting an essential part (and sometimes completely) of their initial movement. Prices often face support/resistance at the level of Fibonacci Retracements or near them in the course of such a reciprocal movement.

## Drawing

To draw Fibonacci Retracement, one should select this object and indicate an initial point in the chart. After that holding the mouse button one should draw a trendline setting the necessary length and slope. Additional parameters will be shown near the end point of the trendline: distance from the initial point along the time axis and distance from the initial point along the price axis, as well as the slope angle relative to a horizontal line drawn through the initial point at the scale 1:1.

![Fibonacci Retracement](/en/docs/mt5/client/img/fibo_retracement.png "Fibonacci Retracement")

## Controls

On the trendline there are three points that can be moved using a mouse. The first and the last points allow changing the trendline length and direction. The central point (moving point) is used for moving the object without changing its dimensions.

## Levels

![Levels](/en/docs/mt5/client/img/obj_properties_levels.png "Levels")

This tab is intended for managing [levels](/en/docs/mt5/client/objects#levels) of the tool. The Fibonacci Retracement has additional feature of displaying price value of each level. To do it, specify the (%$) symbols in the "Description" field.

## Parameters

For Fibonacci Retracement construction [settings](/en/docs/mt5/client/objects#levels) can be changed. Besides, there are the following parameters for this object:

![Parameters](/en/docs/mt5/client/img/fibo_retracement_parameters.png "Parameters")

-   Date/Value — coordinates of the initial point of the trend line (date/value of the price scale);
-   Date/Value — coordinates of the end point of the trend line (date/value of the price scale);
-   Ray Right — infinite duration of Fibonacci Retracement to the right;
-   Ray Left — infinite duration of Fibonacci Retracement to the left.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Fibonacci Tools](/en/docs/mt5/client/objects/fibo)

[Fibonacci Time Zones](/en/docs/mt5/client/objects/fibo/fibo_timezones)