# Trendline by Angle

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/lines/trend_line_angle

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Lines](/en/docs/mt5/client/objects/lines)Trendline by Angle

# Trendline by Angle

To draw a trendline by angle, one should select this object and then click with the left mouse button in the chart to choose the initial point of the line. After that holding the mouse button one should draw a line in the necessary direction. Additional parameters will be shown near the end point: distance from the initial point along the time axis, distance from the initial point along the price axis, slope line from the horizontal line drawn through the initial point.

![Trendline by Angle](/en/docs/mt5/client/img/trend_line_angle.png "Trendline by Angle")

## Parameters

There are the following parameters of a trendline by angle:

![Parameters](/en/docs/mt5/client/img/trend_line_angle_parameters.png "Parameters")

-   Date/Value — coordinates of the initial point (date/value of the price scale);
-   Date/Value — coordinates of the end point (date/value of the price scale);
-   Angle in degrees — slope angle of the trendline from a horizontal line drawn through the initial point;
-   Ray Right — infinite duration of a trendline to the right;
-   Ray Left — infinite duration of a trendline to the left.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Trendline](/en/docs/mt5/client/objects/lines/trend_line)

[Cycle Lines](/en/docs/mt5/client/objects/lines/cycle_lines)