# Gann Line

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/gann/gann_line

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Gann Tools](/en/docs/mt5/client/objects/gann)Gann Line

# Gann Line

Gann Line represents a line drawn at the angle of 45 degrees. This line is also called "one to one" (1x1) what means one change of the price within one unit of time.

According to Gann’s concept, the line having the slope of forty-five degrees represents a long-term trendline (ascending or descending). While prices are above the ascending line, the market holds bull directions. If prices hold below the descending line, the market is characterized as a bear one. Intersection of the Gann Line usually signals of breaking the basic trend. When prices go down to this line during an ascending trend, time and price become fully balanced. The further intersection of Gann Line is the evidence of breaking of this balance and possible changing the trend.

## Drawing

To draw the Gann line, one should select this object and then select an initial point in the chart. After that holding the mouse button one should draw a line in the necessary direction. Additional parameters will be shown near the cursor: distance from the initial point along the time axis, distance from the initial point along the price axis. Besides, during line construction additional vertical lines are shown for the accurate positioning of the initial and end point of the line.

![Gann Line](/en/docs/mt5/client/img/gann_line.png "Gann Line")

## Controls

On the line there are three points that can be moved by a mouse. By moving the first and the last points one can change the slope of a line, as well as its length (if "Ray Right" and "Ray Left" parameters are disabled in the object parameters). The central point (moving point) is used for moving the line in the chart without changing its length or slope.

## Parameters

There are the following parameters of the Gann Line:

![Parameters](/en/docs/mt5/client/img/gann_line_parameters.png "Parameters")

-   Date/Value — coordinates of the initial point (date/value of the price scale);
-   Date — coordinates of the last point along the time axis;
-   Gann Angle — slope angle of the Gann line relative to a horizontal line drawn through the initial point at the scale 1:1 (one price change to one time unit);
-   Pips Per Bar — scale for plotting the Gann Line in a chart. Ratio of pips number to one bar;
-   Ray Right — infinite duration of a trendline to the right;
-   Ray Left — infinite duration of a trendline to the left.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Gann Tools](/en/docs/mt5/client/objects/gann)

[Gann Fan](/en/docs/mt5/client/objects/gann/gann_fan)