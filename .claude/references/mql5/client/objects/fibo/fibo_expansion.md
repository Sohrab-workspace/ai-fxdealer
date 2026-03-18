# Fibonacci Expansion

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/fibo/fibo_expansion

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Fibonacci Tools](/en/docs/mt5/client/objects/fibo)Fibonacci Expansion

# Fibonacci Expansion

Fibonacci Expansion is largely similar to [Fibonacci Retracement](/en/docs/mt5/client/objects/fibo/fibo_retracement) and intended for determining of the end of the third wave. Unlike Fibonacci Retracement, this instrument is built not on the only one [trendline](/en/docs/mt5/client/objects/lines/trend_line), but on two waves.

First, the line of the first wave is drawn, its height will be considered as a unit interval later on. The end of the second wave serves as a reference point for building an invisible vertical line. The corresponding lines are drawn from the reference point on the interval equal to 61.8, 100%, and 161.8 per cent of the unit interval. The third wave is considered to finish near these levels.

## Drawing

To draw Fibonacci extension, one should select this object and indicate the first point of the first wave in the chart. After that one should define the second point of the first wave. To plot the second wave one should click on the second point of the first wave and holding the mouse button draw it. When selecting each point additional parameters will be shown near it: distance from the initial point along the time axis and distance from the initial point along the price axis.

![Fibonacci Expansion](/en/docs/mt5/client/img/fibo_expansion.png "Fibonacci Expansion")

## Controls

On the first wave there are three points that can be moved by a mouse. Using the first point and the last point (which is the first point of the second wave) length and slope are defined. The last point of the second wave is used for changing its length and slope. The central point (moving point) is used for moving the whole object without changing its size and shape.

## Levels

![Levels](/en/docs/mt5/client/img/fibo_expansion_levels.png "Levels")

This tab is intended for managing [levels](/en/docs/mt5/client/objects#levels) of the tool. The Fibonacci Expansion has additional feature of displaying price value of each level. To do it, specify the (%$) symbols in the "Description" field.

## Parameters

There are the following parameters of the object:

![Parameters](/en/docs/mt5/client/img/fibo_expansion_parameters.png "Parameters")

-   Date/Value — coordinates of the first point of the first wave (date/value of the price scale);
-   Date/Value — coordinates of the last point of the first wave (date/value of the price scale);
-   Date/Value — coordinates of the last point of the second wave (date/value of the price scale);
-   Ray Right — infinite duration of levels to the right;
-   Ray Left — infinite duration of levels to the left.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Fibonacci Channel](/en/docs/mt5/client/objects/fibo/fibo_channel)

[Gann Tools](/en/docs/mt5/client/objects/gann)