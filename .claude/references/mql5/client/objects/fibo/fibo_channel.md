# Fibonacci Channel

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/fibo/fibo_channel

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Fibonacci Tools](/en/docs/mt5/client/objects/fibo)Fibonacci Channel

# Fibonacci Channel

Fibonacci Channels are built using several parallel [trendlines](/en/docs/mt5/client/objects/lines/trend_line). To build this instrument, the channel having the width taken as a unit measure is used. Then, parallel lines are drawn at the values equal to the Fibonacci Numbers, beginning with 0.618-fold size of the channel, then 1.000-fold, 1.618-fold, 2.618-fold, 4.236-fold, etc. As soon as the fifth wave finishes, correction in the direction opposite to the trend can be expected.

It is necessary to remember for a correct Fibonacci Channel building: base line limits the upper part of the channel when trend is ascending, and the lower part of it when trend is descending.

## Drawing

To draw Fibonacci Channel, one should select this object and indicate an initial point of the main trendline in the chart. After that holding the mouse button one should draw a trendline in the necessary direction. Additional parameters will be shown near the end point of the trendline: distance from the initial point along the time axis and distance from the initial point along the price axis. Other lines will be automatically drawn parallel to the main one.

![Fibonacci Channel](/en/docs/mt5/client/img/fibo_channel.png "Fibonacci Channel")

## Controls

On the main trendline there are three points that can be moved by a mouse. The first and the last points are used for changing the length and direction of lines. The central point (moving point) is used for moving Fibonacci Channel without changing its dimensions and direction. On the second border of the channel there is a point used for changing the width of the channel. The second border of the channel is moved independently from the first one.

## Parameters

For Fibonacci Channel trendline construction [settings](/en/docs/mt5/client/objects#levels) can be changed. Besides, there are the following parameters for this object:

![Parameters](/en/docs/mt5/client/img/fibo_channel_parameters.png "Parameters")

-   Date/Value — coordinates of the first point on the main line of Fibonacci Channel (date/value of the price scale);
-   Date/Value — coordinates of the last point on the main line of Fibonacci Channel (date/value of the price scale);
-   Date/Value — coordinates of the point on the second line of Fibonacci Channel (date/value of the price scale);
-   Ray Right — infinite duration of Fibonacci Channel to the right;
-   Ray Left — infinite duration of Fibonacci Channel to the left.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Fibonacci Arcs](/en/docs/mt5/client/objects/fibo/fibo_arcs)

[Fibonacci Expansion](/en/docs/mt5/client/objects/fibo/fibo_expansion)