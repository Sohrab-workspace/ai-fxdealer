# Ellipse

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/shapes/ellipse

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
                -   [Elliott Tools](/en/docs/mt5/client/objects/elliott)
                -   [Shapes](/en/docs/mt5/client/objects/shapes)
                    -   [Rectangle](/en/docs/mt5/client/objects/shapes/rectangle)
                    -   [Triangle](/en/docs/mt5/client/objects/shapes/triangle)
                    -   [Ellipse](/en/docs/mt5/client/objects/shapes/ellipse)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Shapes](/en/docs/mt5/client/objects/shapes)Ellipse

# Ellipse

To draw an ellipse, one should select the object and define an initial point in a chart. After that one should define the second point and holding the mouse drag the ellipse till the necessary size and shape.

![Ellipse](/en/docs/mt5/client/img/ellipse.png "Ellipse")

## Controls

This object has four control points that can be moved with the mouse. Points located on faces are used for changing the size and shape of the ellipse. The point located in the center is used for moving the object without changing its shape.

## Parameters

There are the following parameters of an ellipse:

![Parameters](/en/docs/mt5/client/img/ellipse_parameters.png "Parameters")

-   Date/Value — coordinates of the first point of the ellipse (date/value of the price scale);
-   Date/Value — coordinates of the second point of the ellipse (date/value of the price scale);
-   Date/Value — coordinates of the third point of the ellipse (date/value of the price scale);
-   Fill — enable/disable color filling inside the shape.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To fill the object with the color of its lines, you should enable option the "Draw object as background" at the <a href="/en/docs/mt5/client/objects#common" class="topiclink">"Common"</a> tab.</span></p></td></tr></tbody></table>

[Triangle](/en/docs/mt5/client/objects/shapes/triangle)

[Arrows](/en/docs/mt5/client/objects/arrows)