# Text

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/graphical_objects/obj_text

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
                -   [Arrows](/en/docs/mt5/client/objects/arrows)
                -   [Graphical Objects](/en/docs/mt5/client/objects/graphical_objects)
                    -   [Text](/en/docs/mt5/client/objects/graphical_objects/obj_text)
                    -   [Text Label](/en/docs/mt5/client/objects/graphical_objects/obj_text_label)
                    -   [Button](/en/docs/mt5/client/objects/graphical_objects/obj_button)
                    -   [Graph](/en/docs/mt5/client/objects/graphical_objects/obj_chart)
                    -   [Bitmap](/en/docs/mt5/client/objects/graphical_objects/obj_bitmap)
                    -   [Bitmap Label](/en/docs/mt5/client/objects/graphical_objects/obj_bitmap_label)
                    -   [Edit](/en/docs/mt5/client/objects/graphical_objects/obj_edit)
                    -   [Event](/en/docs/mt5/client/objects/graphical_objects/obj_event)
                    -   [Rectangle Label](/en/docs/mt5/client/objects/graphical_objects/obj_rect_label)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Graphical Objects](/en/docs/mt5/client/objects/graphical_objects)Text

# Text

This object is intended for adding text labels to a chart. The object is bound to a chart and moves together with it. To place the object in a chart, one should select it and define the necessary point in a chart.

![Text](/en/docs/mt5/client/img/obj_text.png "Text")

## Controls

The object is moved using the anchor point located on one of object sides or corners. The text content is changed via the object settings in the "Description" field of the ["Common"](/en/docs/mt5/client/objects#common) tab.

## Parameters

There are the following parameters of the object:

![Parameters](/en/docs/mt5/client/img/obj_text_parameters.png "Parameters")

-   Date/Value — coordinates of the anchor point of the object (date/value of the price scale);
-   Angle in degrees — angle of the object slope from the horizontal line drawn through its anchor point;
-   Font —  font type and size for the object text;
-   Anchor — one of object sides or corners, where the anchor point is located.

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Graphical Objects](/en/docs/mt5/client/objects/graphical_objects)

[Text Label](/en/docs/mt5/client/objects/graphical_objects/obj_text_label)