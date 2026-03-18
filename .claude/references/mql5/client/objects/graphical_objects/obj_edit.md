# Edit

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/graphical_objects/obj_edit

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)[Graphical Objects](/en/docs/mt5/client/objects/graphical_objects)Edit

# Edit

This object is used for adding an editable text field in a chart. Values of the field can be changed directly in the chart. Entered valued can be read by a program written in [MQL5](/en/docs/mt5/client/autotrading#mql5) language. The object is anchored to a chart window and does not move when the chart is scrolled.

## Controls

The object is moved using the anchor point located on its upper left corner.

## Parameters

There are the following parameters of the "Edit" object:

![Parameters](/en/docs/mt5/client/img/obj_edit_parameters.png "Parameters")

-   X-distance — distance in pixels from the anchor corner of the chart window till the control point of the object along the time axis;
-   Y-distance — distance in pixels from the anchor corner of the chart window till the control point of the object along the price axis;
-   Width — width of the editable field in pixels;
-   Height — height of the editable field in pixels;
-   Corner — one of the corners of the chart window, from which distances along X and Y axes will be set;
-   Read Only — enable/disable the "read only" mode. If this mode is enabled, then entering and editing of a text in this field is prohibited;
-   Background — background color for the editable field;
-   Font —  font type and size for the object text.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In order to have the possibility to enter values in a field on a chart, it is necessary to enable the option <a href="/en/docs/mt5/client/objects#disable_selection" class="topiclink">"Disable selection"</a> in object properties.</span></p></td></tr></tbody></table>

Common parameters of object are described in a [separate section](/en/docs/mt5/client/objects#draw_settings).

[Bitmap Label](/en/docs/mt5/client/objects/graphical_objects/obj_bitmap_label)

[Event](/en/docs/mt5/client/objects/graphical_objects/obj_event)