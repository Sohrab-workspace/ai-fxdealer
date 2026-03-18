# Equidistant Channel

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/channels/equidistant_channel

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Channels](/en/docs/mt5/client/objects/channels)Equidistant Channel

# Equidistant Channel

Equidistant Channel represents two parallel [trendlines](/en/docs/mt5/client/objects/lines/trend_line) connecting extreme maximum and minimum close prices. Market price jumps, draws peaks and troughs forming the channel in the trend direction. Early identification of the channel can give valuable information including that about changes in the trend direction what allows to estimate possible profits and losses.

## Drawing

To draw the equidistant channel, one should select this object and then click with the left mouse button in the chart. After that holding the mouse button one should draw the channel in the necessary direction and set its width. Additional parameters will be shown near the end point of the lower border of the channel: distance from the initial point along the time axis, distance from the initial point along the price axis.

![Equidistant Channel](/en/docs/mt5/client/img/equidistant_channel.png "Equidistant Channel")

## Controls

On the main channel line there are three points that can be moved with the mouse. Moving of the first point changes the channel width and the length of the upper and lower borders (length of borders is changed proportionally but in different directions). Moving of the central point of the main line will move the channel without changing its dimensions. Manipulations with the third point allow changing the length and direction of the whole channel. Moving of the point of the second channel line allows moving this border independently from the main line.

## Parameters

There are the following parameters of the equidistant channel:

![Parameters](/en/docs/mt5/client/img/equidistant_channel_parameters.png "Parameters")

-   Date/Value — coordinates of the first point (anchor) on the main line (date/value of the price scale);
-   Date/Value — coordinates of the last point (moving point) on the main line (date/value of the price scale);
-   Date/Value — point coordinates of the second line (date/value of the price scale);
-   Ray Right — infinite duration of the channel to the right;
-   Ray Left — infinite duration of the channel to the left;
-   Fill — enable/disable color filling inside the channel.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Channels](/en/docs/mt5/client/objects/channels)

[Standard Deviation Channel](/en/docs/mt5/client/objects/channels/stddev_channel)