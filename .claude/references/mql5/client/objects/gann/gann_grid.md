# Gann Grid

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/gann/gann_grid

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Gann Tools](/en/docs/mt5/client/objects/gann)Gann Grid

# Gann Grid

Gann Grid represents [trends](/en/docs/mt5/client/objects/lines/trend_line) built at the angle of 45 degrees ([Gann Lines](/en/docs/mt5/client/objects/gann/gann_line)). According to Gann’s concepts, a line having a slope of forty-five degrees represents a long-term trendline (ascending or descending). While prices are above the ascending line, the market holds bull directions. If prices hold below the descending line, the market is characterized as a bear one. Intersection of the Gann Line usually signals of breaking the basic trend. When prices go down to this line during an ascending trend, time and price become fully balanced. The further intersection of Gann Lines is an evidence of breaking of this balance and possible change of the trend.

## Drawing

To draw Gann Grid, one should select this object and indicate an initial point in the chart. After that holding the mouse button one should define the second point setting thus the size of cells. An additional parameter will be shown near this point — distance along the time axis from the initial point.

![Gann Grid](/en/docs/mt5/client/img/gann_grid.png "Gann Grid")

## Controls

On the main line of Gann Grid there are three points that can be moved by a mouse. The first and last points are used for setting the grid cell size. The central point (moving point) is used for moving Gann Grid in the chart without changing its dimensions. The slope of lines is defined by the "Pips Per Bar" parameter described below.

## Parameters

There are the following parameters of Gann Grid:

![Parameters](/en/docs/mt5/client/img/gann_grid_parameters.png "Parameters")

-   Date/Value — coordinates of the initial point (date/value of the price scale);
-   Date — coordinates of the last point along the time axis;
-   Pips Per Bar — scale for plotting the Gann Grid in a chart. Ratio of pips number to one bar;
-   Downtrend — if this field is checked, the Gann Grid will be directed downwards. This parameter is used for building the Gann Fan at downtrends.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Gann Fan](/en/docs/mt5/client/objects/gann/gann_fan)

[Elliott Tools](/en/docs/mt5/client/objects/elliott)