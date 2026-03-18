# Arrowed Line

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/lines/arrowed_line

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
                    -   [Horizontal Line](/en/docs/mt5/client/objects/lines/hor_line)
                    -   [Vertical Line](/en/docs/mt5/client/objects/lines/vert_line)
                    -   [Trendline](/en/docs/mt5/client/objects/lines/trend_line)
                    -   [Trendline by Angle](/en/docs/mt5/client/objects/lines/trend_line_angle)
                    -   [Cycle Lines](/en/docs/mt5/client/objects/lines/cycle_lines)
                    -   [Arrowed Line](/en/docs/mt5/client/objects/lines/arrowed_line)
                -   [Channels](/en/docs/mt5/client/objects/channels)
                -   [Fibonacci Tools](/en/docs/mt5/client/objects/fibo)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Lines](/en/docs/mt5/client/objects/lines)Arrowed Line

# Arrowed Line

This object is a straight line with an arrow at its end. It is intended for drawing explanatory schemes in charts.

![Arrowed Line](/en/docs/mt5/client/img/arrowed_line.png "Arrowed Line")

## Drawing

To draw an arrowed line, one should select this object and then click with the left mouse button in the chart. After that holding the mouse button one should draw a line in the necessary direction. Additional parameters will be shown near the end point: distance from the initial point along the time axis, distance from the initial point along the price axis, slope line from the horizontal line drawn through the initial point.

## Controls

Three points are located on an arrowed line. Extreme points are points for changing size and slope. The central one is used for moving the object.

## Parameters

There are the following parameters of an arrowed line:

![Parameters](/en/docs/mt5/client/img/arrowed_line_parameters.png "Parameters")

-   Date/Value — coordinates of the initial point (date/value of the price scale);
-   Date/Value — coordinates of the end point (date/value of the price scale).

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Cycle Lines](/en/docs/mt5/client/objects/lines/cycle_lines)

[Channels](/en/docs/mt5/client/objects/channels)