# Andrews' Pitchfork

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/channels/andrews_pitchfork

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Channels](/en/docs/mt5/client/objects/channels)Andrews' Pitchfork

# Andrews' Pitchfork

Andrews’ Pitchfork is an instrument consisting of three parallel [trendlines](/en/docs/mt5/client/objects/lines/trend_line). This instrument was developed by Dr. Alan Andrews. Interpretation of Andrews’ Pitchfork is based on standard rules of interpretation of support and resistance. The first trend line starts in a selected extreme left point (it is an important peak or trough) and is drawn exactly between two extreme right points. This line is the pitchfork «helve». Then, the second and the third trendlines outgoing from the above-mentioned rightmost points (significant peak and trough) are drawn in parallel to the first trendline. These lines are the pitchfork «teeth». Signal lines are drawn parallel to "tines" of the pitchfork. They are drawn at distances proportional to Fibonacci numbers. The distance between the median line (continuation of a "handle") and "teeth" of the pitchfork.

## Drawing

To draw Andrews' Pitchfork, one should select this object and then click with the left mouse button in the chart plotting the first point (beginning of the "handle"). After that one should plot the second point of the "handle" in a chart and holding the mouse button move the cursor thus setting "teeth" of the pitchfork and signal lines at the necessary distance. Additional parameters will be shown near the cursor - three pairs of numbers. The first pair indicates the "handle" beginning, the first value is always equal to zero (because it is the initial point of the object); the second number indicates the distance between "teeth". The second and third pairs of numbers show distance along the time axis and price axis from the "teeth" to the "handle" beginning point.

![Andrews' Pitchfork](/en/docs/mt5/client/img/andrews_pitchfork.png "Andrews' Pitchfork")

## Controls

Moving of the "handle" beginning point will change the direction of "teeth" only. The second point of the "handle" allows moving Andrews' Pitchfork in the chart without changing its dimensions. Points of "teeth" beginning allow changing the position of teeth separately; when one point is moved, the second stays in its place.

## Parameters

For Andrews' Pitchfork [level settings](/en/docs/mt5/client/objects#levels) (of signal lines). Besides there are the following parameters of the pitchfork:

![Parameters](/en/docs/mt5/client/img/andrews_pitchfork_parameters.png "Parameters")

-   Date/Value — coordinates of the beginning point of Andrews' Pitchfork "handle" (date/value of the price scale);
-   Date/Value — coordinates of the point of the lower "tooth" (lower pivot point) of Andrews' Pitchfork (date/value of the price scale);
-   Date/Value — coordinates of the point of the upper "tooth" (upper pivot point) of Andrews' Pitchfork (date/value of the price scale);
-   Ray Right — infinite duration of the pitchfork to the right;
-   Ray Left — infinite duration of the pitchfork to the left.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Regression Channel](/en/docs/mt5/client/objects/channels/regression_channel)

[Fibonacci Tools](/en/docs/mt5/client/objects/fibo)