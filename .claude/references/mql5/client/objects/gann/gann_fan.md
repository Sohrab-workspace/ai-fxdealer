# Gann Fan

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/gann/gann_fan

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
                -   [Gann Tools](/en/docs/mt5/client/objects/gann)
                    -   [Gann Line](/en/docs/mt5/client/objects/gann/gann_line)
                    -   [Gann Fan](/en/docs/mt5/client/objects/gann/gann_fan)
                    -   [Gann Grid](/en/docs/mt5/client/objects/gann/gann_grid)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Gann Tools](/en/docs/mt5/client/objects/gann)Gann Fan

# Gann Fan

Lines of Gann Fan are built at different angles from an important base or peak at the price chart. The trendline of 1x1 was considered by Gann the most important. If the price curve is located above this line, it is the indication of the bull market, if it is below this line it is that of the bear market. Gann thought that the ray of 1x1 is a powerful support line when the trend is ascending, and he considered the breaking this line as an important turn signal. Gann emphasized the following nine basic angles, the angle of 1x1 being the most important of all:

-   1x8 — 82,5 degrees
-   1x4 — 75 degrees
-   1x3 — 71,25 degrees
-   1x2 — 63,75 degrees
-   1x1 — 45 degrees
-   2x1 — 26,25 degrees
-   3x1 — 18,75 degrees
-   4x1 — 15 degrees
-   8x1 — 7,5 degrees

For the considered ratios of price and time increments to have corresponding angles of slope in degrees, X and Y axes must have the same scales. It means that a unit interval on X axis (i.e., hour, day, week, month) must correspond with the unit interval on Y axis. The simplest method of chart calibration consists in checking the slope of the ray of 1x1: it must make 45 degrees.

Gann noted that each of the above-listed rays can serve as support or resistance depending on the price trend direction. For example, ray of 1x1 is usually the most important support line when the trend is ascending. If prices fall below 1x1 line, it means the trend turns. According to Gann, prices should then sink down to the next trend line (in this case, it is the ray of 2x1). In other words, if one of rays is broken, the price consolidation should be expected to occur near the next ray.

## Drawing

To draw Gann Fan, one should select this object and indicate an initial point in the chart. After that holding the mouse button one should draw the tool at the necessary length. An additional parameter will be shown near the end point — distance along the time axis from the initial point.

![Gann Fan](/en/docs/mt5/client/img/gann_fan.png "Gann Fan")

## Controls

Gann Fan can be managed using two points located on the trendline 1x1; the points can be moved using a mouse. These points are used for positioning Gann Fan in a chart. The line slope angle can be changed in the "Pips Per Bar" parameter described below.

## Parameters

There are the following parameters of the Gann Fan:

![Parameters](/en/docs/mt5/client/img/gann_fan_parameters.png "Parameters")

-   Date/Value — coordinates of the initial point (date/value of the price scale);
-   Date — coordinates of the last point along the time axis;
-   Pips Per Bar — scale for plotting the Gann Fan in a chart. Ratio of pips number to one bar;
-   Downtrend — if this field is checked, the Gann Fan will be inclined downwards. This parameter is used for building the Gann Fan at downtrends.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Gann Line](/en/docs/mt5/client/objects/gann/gann_line)

[Gann Grid](/en/docs/mt5/client/objects/gann/gann_grid)