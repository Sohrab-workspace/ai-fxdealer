# Fibonacci Arcs

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/fibo/fibo_arcs

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Fibonacci Tools](/en/docs/mt5/client/objects/fibo)Fibonacci Arcs

# Fibonacci Arcs

Fibonacci Arcs are built as follows: first, the trend line is drawn between two extreme points, for example, from the trough to the opposing peak. Then three arcs are built having their centers in the second extreme point and intersecting the trend line at Fibonacci levels of 38.2, 50, and 61.8 percent.

Fibonacci arcs are considered to be potential support and resistance levels. Fibonacci Arcs and [Fibonacci Fan](/en/docs/mt5/client/objects/fibo/fibo_fan) are usually plotted together on the chart, and support and resistance levels are determined by the points of intersection of these lines.

It should be noted that the points of intersection of Arcs and the price curve can change depending on the chart scale since an arc is a part of a circumference, and its form is always the same.

## Drawing

To draw Fibonacci Arcs, one should select this object and indicate an initial point in the chart and, holding the mouse button, one should draw a trendline till the second extreme point. Additional parameters will be shown near the end point of the trendline: distance from the initial point along the time axis and distance from the initial point along the price axis, as well as the slope angle relative to a horizontal line drawn through the initial point at the scale 1:1.

![Fibonacci Arcs](/en/docs/mt5/client/img/fibo_arcs.png "Fibonacci Arcs")

## Controls

On the trendline there are three points that can be moved by a mouse. The first and the last points are used for changing the length and direction of lines. The central point (moving point) is used for moving Fibonacci Arcs without changing their dimensions and direction.

## Parameters

For Fibonacci Arcs construction [settings](/en/docs/mt5/client/objects#levels) can be changed. Besides, there are the following parameters for this object:

![Parameters](/en/docs/mt5/client/img/fibo_arcs_parameters.png "Parameters")

-   Date/Value — coordinates of the initial point of the trend line (date/value of the price scale);
-   Date/Value — coordinates of the end point of the trend line (date/value of the price scale);
-   Scale — ratio of the minor and larger radii of arcs. The minor radius is measured along the price scale, the larger one - along the time scale. This parameter sets the ratio of pips number to one bar;
-   Ellipse — if this field is checked, Fibonacci Arcs will be specularly closed by identical arcs  thus building the shape of an ellipse.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Fibonacci Fan](/en/docs/mt5/client/objects/fibo/fibo_fan)

[Fibonacci Channel](/en/docs/mt5/client/objects/fibo/fibo_channel)