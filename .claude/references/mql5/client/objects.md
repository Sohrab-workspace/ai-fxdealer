# Analytical Objects

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)Analytical Objects

# Analytical Objects

Identifying trends, plotting channels, defining cycles and support/resistance levels — all these and many other tasks can be solved using analytical objects. The trading platform provides 46 analytical tools. They include geometric shapes, channels, Gann, Fibonacci and Elliott tools, and more. Unlike [technical indicators](/en/docs/mt5/client/indicators), graphical objects are plotted manually.

![Analytical Objects](/en/docs/mt5/client/img/objects_overview.png "Analytical Objects")

## Types of Analytical Objects [#](objects#type)

46 analytical objects are available in the trading platform. They are grouped into the following categories:

-   [Lines](/en/docs/mt5/client/objects/lines) — various lines (trend lines, horizontal, cyclic lines, etc.) added to price charts and indicators;
-   [Channels](/en/docs/mt5/client/objects/channels) — various channels (equidistant, regression channel, etc.) added to price charts and indicators;
-   [Gann Tools](/en/docs/mt5/client/objects/gann) — a set of technical analysis tools developed by W. D. Gann;
-   [Fibonacci Tools](/en/docs/mt5/client/objects/fibo) — a set of technical analysis tools created on the basis of the numerical sequence by L. Fibonacci;
-   [Elliott Tools](/en/docs/mt5/client/objects/elliott) — a set of tools technical analysis based on the wave theory of R. N. Elliott;
-   [Shapes](/en/docs/mt5/client/objects/shapes) — geometric shapes (square, triangle, and ellipse) that allow to mark various areas in the price chart;
-   [Arrows](/en/docs/mt5/client/objects/arrows) — symbols (arrows, check and stop signs) allowing to mark the most significant points in the chart;
-   [Graphical objects](/en/docs/mt5/client/objects/graphical_objects) — various graphical objects (text, text labels, button, etc.)

For convenience, all objects are grouped by categories in the [Insert](/en/docs/mt5/client/interface) menu and the [Line Studies](/en/docs/mt5/client/interface) toolbar.

![Analytical objects in the trading platform](/en/docs/mt5/client/img/objects.png "Analytical objects in the trading platform")

## How to Add an Object to a Chart [#](objects#draw)

To add an object, select it from the [Insert](/en/docs/mt5/client/interface) menu or on the [Line Studies](/en/docs/mt5/client/interface) toolbar.

Simple objects such as horizontal and vertical lines, arrows, labels, and others are plotted using one point. Select an object, click on the chart, and the object will be immediately added.

More complex objects that are built along the trend, such as channels, Gann and Fibonacci tools, etc. have multiple control points. They are added as follows: click on a chart to add the starting point, then hold down the mouse button and set the object direction and its second point. Below is an example of adding an equidistant channel.

![Adding an equidistant channel](/en/docs/mt5/client/img/object_plot.png "Adding an equidistant channel")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Some objects require setting more than one point. The object appears on the chart only after setting all the required points.</span></p></td></tr></tbody></table>

## Managing Object on the Chart [#](objects#manage)

A created object can be moved and modified. Click on an object to select it. Square markers or frames appear for a selected object. The markers are used for moving objects and changing their drawing parameters.

For example, to change the Fibonacci Fan location, grab its central marker with the left mouse button and move the cursor. Moving of any of its extreme markers changes the object drawing parameters.

The object moving points is its central point as a rule.

Any object can be removed from the chart using the context menu commands. Using the Backspace key, you can remove objects sequentially. Any removed object can be restored. To restore an object, click "Object — Undo Delete" in the [Charts](/en/docs/mt5/client/interface) menu or press Ctrl+Z.

### Some features of working with objects:

-   The platform allows you to quickly create copies of various objects. Select an object, hold down Ctrl and move the object using its central marker.
-   To move a group of objects, select them and drag the point of one of them while holding down Alt.
-   You can use a single click to select objects instead of the double click by enabling option "Select objects by single mouse click" in the [platform settings](/en/docs/mt5/client/settings#single_click).
-   Magnet sensitivity of objects can be set in the [platform settings](/en/docs/mt5/client/settings#magnet). When you move a point to the area within the distance specified in "Magnet sensitivity" from one of the bar prices ("Open", "High", "Low" or "Close"), the point is automatically moved to this price level. This feature enables convenient positioning of objects on the chart.

## How to Modify Object Properties [#](objects#modify)

Parameters of an added object can be modified. Select the required object in the [Object List](/en/docs/mt5/client/charts_advanced/charts_objects_list#objects) window and click "Edit" or select "![Properties](/en/docs/mt5/client/img/object_properties_button.png "Properties") Properties" in the context menu of the object on the chart.

Use the context menu to manage objects:

-   ![Properties](/en/docs/mt5/client/img/object_properties_button.png "Properties") Properties — open the properties of a selected object.
-   ![List of objects](/en/docs/mt5/client/img/objects_list_icon.png "List of objects") Object List — open the [Object List](/en/docs/mt5/client/charts_advanced/charts_objects_list#objects) to manage objects on the chart.
-   Delete — delete the selected object.
-   ![Delete All Arrows](/en/docs/mt5/client/img/delete_all_arrows_icon.png "Delete All Arrows") Delete All Arrows — delete all arrows belonging to the [Arrows](/en/docs/mt5/client/objects/arrows) group.
-   ![Delete All Selected](/en/docs/mt5/client/img/delete_all_selected_icon.png "Delete All Selected") Delete All Selected — delete all selected objects.
-   ![Cancel selection of all objects](/en/docs/mt5/client/img/cancel_selection_objects_icon.png "Cancel selection of all objects") Unselect All — unselect all objects on the chart.
-   Unselect — unselect the selected object.
-   ![Undo Delete](/en/docs/mt5/client/img/undo_delete_icon.png "Undo Delete") Undo Delete — restore the last deleted object.

## How to Customize the Object Appearance [#](objects#appearance)

You can conveniently customize the appearance of analytical objects in the trading platform. You can set up the object parameters when adding it to a chart or modify them later. The object appearance is adjusted on the "Common" tab:

![Common](/en/docs/mt5/client/img/obj_properties_common.png "Common")

Line color, width and style are set up in the "Style" field. Other general object parameters can be set up here:

-   Name — the unique name of an object within one chart, it is set automatically. It can be changed by entering another name in this field. Such names make it easy to find an object among many other objects of the same type;
-   Description — a text description of an object which also helps to identify objects. The description can be shown on the chart if the "Show object descriptions" option is enabled in the chart settings;

## Object Display Settings [#](objects#visualization)

The object display on different timeframes (periods) can be changed in the "Visualization" tab.

![Object display settings](/en/docs/mt5/client/img/object_visualization.gif "Object display settings")

The object only appears on the selected timeframes. This can be useful when an object has different settings on different timeframes. If the field "All timeframes" is selected, the object is visible on all timeframes.

The "Levels" tab is specifically used only for [Fibonacci tools](/en/docs/mt5/client/objects/fibo) and [Andrews' Pitchfork](/en/docs/mt5/client/objects/channels/andrews_pitchfork). The list of the object levels is available in the form of a table here.

The values of the levels can be changed or deleted (the "Delete" button). A new level can be added by clicking the "Add" button. The "Defaults" button sets the initial values. The color, width and style of the object levels are set up in the "Style" field.

## Object Drawing Parameters [#](objects#draw_settings)

Object drawing parameters are available on the "Common" tab.

![Object drawing Parameters](/en/docs/mt5/client/img/object_plot_settings.gif "Object drawing Parameters")

Parameters include:

-   Draw object as background — draw object in the background, behind the chart. This option also sets color filling of objects like shapes or channels (excluding Fibonacci Channel).
-   Disable selection — disable the possibility of object selection. This possibility is intended for control objects (["Button"](/en/docs/mt5/client/objects/graphical_objects/obj_button), ["Entry field"](/en/docs/mt5/client/objects/graphical_objects/obj_edit), ["Graphic label"](/en/docs/mt5/client/objects/graphical_objects/obj_bitmap_label)). This option allows to change the state of buttons and graphic labels, as well enter values in the entry fields.

Coordinates of the object control points can be changed on the "Parameters" tab. Time coordinates are set in the "Date" fields. Values of coordinates along the vertical axis are entered in the "Value" fields. An object can have from one to three coordinates.

For some objects, additional options are available in the "Parameters" tab:

-   Angle in degrees — angle of the object slope counter-clockwise in degrees;
-   Scale — ratio between units of vertical (pips) and horizontal (bars) axes of the object. Normally, the number of pixels in a unit of the horizontal (time) axis differs from that of the vertical (prices) axis. Scale 1:1 sets them to the same value. Changing this setting for individual objects changes the ratio;
-   Arrow code — code of the object;
-   Ray right/left — displaying trend lines as rays in specified directions;
-   Anchor — one of the chart corners or sides where its anchor point is located;
-   X-distance: — horizontal distance between the anchor corner of the window and the text label in pixels;
-   Y-distance: — vertical distance between the anchor corner of the window and the text label in pixels;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The complete list of object parameters is available in object description sections.</span></p></td></tr></tbody></table>

## What Platform Settings Affect Object Drawing [#](objects#general)

The trading platform has common object drawing settings, which are available in the [Chart](/en/docs/mt5/client/settings#charts) section.

-   Show object properties after creation — all objects have certain [properties](/en/docs/mt5/client/objects#parameters). For example, thickness and color of the trend line, period of the indicator's signal line, etc. Most traders use standard settings of all graphical objects, but in some cases you may need to set them up individually. Option "Show object properties after creation" allows to automatically open the window of properties of [graphical objects](/en/docs/mt5/client/objects#parameters) and [indicators](/en/docs/mt5/client/indicators#run) after they are applied to a chart.
-   Select objects by single mouse click — graphical objects in the platform can be selected by a single or double click. This option allows to switch between the object selection methods. If it is enabled, all objects are selected by a single click. If this option is disabled, all objects are selected by a double click.
-   Precise time scale — if this option is disabled, objects are bound to bars along the horizontal scale of a chart. If you enable it, then it is possible to position an object at any point between bars.
-   Select objects after creation — objects are positioned on charts manually. After creating an object you may need to move it, for example to accurately position a trend line. To do that, it is necessary to select the object first. This option allows to do that automatically right after placing an object on a chart.
-   Magnet sensitivity — the platform allows to "dock" anchor points (except for the central moving points) of [graphical objects](/en/docs/mt5/client/objects) to different bar prices to locate them more precisely. In the "Magnet sensitivity" field, the sensitivity of this option in pixels can be defined. For example, if the value of 10 is specified, the object is automatically docked to a bar if the object's anchor point is located within a distance of 10 pips from the nearest bar price (OHLC). The point should also be within the bar width. To disable the option, set the parameter to 0.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you add an object to a chart with the <a href="/en/docs/mt5/client/charts#operations" class="topiclink">timeframe</a> other than M1, the following magnet features are active:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">When anchoring a point of an object to one of the extreme price (OHLC), the specific minute is determined, where the extremum was recorded. Point of the object is bound to that minute, and it is reflected in the <a href="/en/docs/mt5/client/objects#parameters" class="topiclink">object properties</a>. This kind of behavior allows keeping proper positioning of objects when switching between timeframes.</span></li><li class="p_tableatten"><span class="f_tableatten">If the "Precise time scale" option is additionally enabled, then you may observe an effect when the anchor point moves away from an extreme point. This behavior appears if the actual extreme point does not correspond to the extreme point of a bar.</span></li></ul></td></tr></tbody></table>

[Market Facilitation Index](/en/docs/mt5/client/indicators/bw_indicators/market_facilitation)

[Lines](/en/docs/mt5/client/objects/lines)