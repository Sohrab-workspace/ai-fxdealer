# Standard Deviation Channel

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/channels/stddev_channel

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
                    -   [Equidistant Channel](/en/docs/mt5/client/objects/channels/equidistant_channel)
                    -   [Standard Deviation Channel](/en/docs/mt5/client/objects/channels/stddev_channel)
                    -   [Regression Channel](/en/docs/mt5/client/objects/channels/regression_channel)
                    -   [Andrews' Pitchfork](/en/docs/mt5/client/objects/channels/andrews_pitchfork)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Channels](/en/docs/mt5/client/objects/channels)Standard Deviation Channel

# Standard Deviation Channel

Standard Deviation Channel is built on base of Linear Regression Trend representing a usual [trendline](/en/docs/mt5/client/objects/lines/trend_line) built between two points on the price chart using the method of least squares. As a result, this line proves to be the exact median line of the changing price. It can be considered as an equilibrium price line, and any deflection up or down indicates the superactivity of buyers or sellers respectively.

Standard Deviation Channel consists of two parallel lines, equidistant up and down from the Linear Regression Trend. The distance between frame of the channel and regression line equals to the value of the standard deviation of the close price from the regression line. All price changes take place within Standard Deviation Channel, where the lower frame works as support line, and the upper one does as resistance line. Prices usually exceed the channel frames for a short time. If they keep outside of the channel frames for a longer time than usually, it forecasts the possibility of trend turn.

## Drawing

To draw the channel, one should select this object and then click with the left mouse button in the chart. After that holding the mouse button one should draw the channel in the necessary direction and set its length. Additional parameters will be shown near the end point of the trendline of the channel: distance from the initial point along the time axis, distance from the initial point along the price axis.

![Standard Deviation Channel](/en/docs/mt5/client/img/stddev_channel.png "Standard Deviation Channel")

## Controls

On the trend line of the channel linear regression there are three points that can be moved with the mouse. The first and the last points are used to change the channel length in different directions. The central point (moving point) is used to move a channel in the chart without changing its dimensions.

## Parameters

There are the following parameters of the standard deviation channel:

![Parameters](/en/docs/mt5/client/img/stddev_channel_parameters.png "Parameters")

-   Date — coordinate on the time scale of the first point of the trend of the channel linear regression.
-   Date — coordinate on the time scale of the last point of the trend of the channel linear regression.
-   Ray Right — infinite duration of the channel to the right;
-   Ray Left — infinite duration of the channel to the left;
-   Fill — enable/disable color filling inside the channel;
-   Deviations — number of standard deviation values for building the channel borders.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Equidistant Channel](/en/docs/mt5/client/objects/channels/equidistant_channel)

[Regression Channel](/en/docs/mt5/client/objects/channels/regression_channel)