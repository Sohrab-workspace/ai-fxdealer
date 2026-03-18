# Lists of Objects Applied

> Source: https://support.metaquotes.net/en/docs/mt5/client/charts_advanced/charts_objects_list

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
            -   [Fundamental Analysis](/en/docs/mt5/client/fundamental)
            -   [Additional Technical Indicators](/en/docs/mt5/client/charts_analysis_get_indicators)
            -   [Additional Features](/en/docs/mt5/client/charts_advanced)
                -   [Chart Settings](/en/docs/mt5/client/charts_advanced/charts_settings)
                -   [Chart Print](/en/docs/mt5/client/charts_advanced/charts_print)
                -   [Chart Management](/en/docs/mt5/client/charts_advanced/charts_manage)
                -   [Lists of Objects Applied](/en/docs/mt5/client/charts_advanced/charts_objects_list)
                -   [Deleted Charts](/en/docs/mt5/client/charts_advanced/charts_deleted)
                -   [Templates and Profiles](/en/docs/mt5/client/charts_advanced/templates_profiles)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Additional Features](/en/docs/mt5/client/charts_advanced)Lists of Objects Applied

# Lists of Objects Applied

For each chart you can open a list of all applied objects: indicators, analytical objects and Expert Advisors. From the list you can modify the properties of objects or delete them from the chart.

-   [List of indicators](/en/docs/mt5/client/charts_advanced/charts_objects_list#indicators)
-   [List of objects](/en/docs/mt5/client/charts_advanced/charts_objects_list#objects)
-   [List of Expert Advisors](/en/docs/mt5/client/charts_advanced/charts_objects_list#ea)

## List of Indicators [#](charts_objects_list#indicators)

To manage [indicators](/en/docs/mt5/client/trade_robots_indicators) applied on the chart click "![List of indicators](/en/docs/mt5/client/img/indicators_list_icon.png "List of indicators") Indicator List" in the context menu or press "Ctrl+I".

![List of indicators](/en/docs/mt5/client/img/indicators_list.png "List of indicators")

Indicators are divided into two groups: those plotted in the main chart window and indicators drawn in separate windows. Select an indicator and click "Properties" to open [indicator settings](/en/docs/mt5/client/indicators#appearance). To remove an indicator from the chart, click "Delete".

## List of Objects [#](charts_objects_list#objects)

To manage [analytical objects](/en/docs/mt5/client/objects) applied on the chart click "![List of objects](/en/docs/mt5/client/img/objects_list_icon.png "List of objects") Object List" in its context menu or press "Ctrl+B".

![List of objects](/en/docs/mt5/client/img/objects_list.png "List of objects")

The following information is available in the list of objects:

-   Object — object type. Tick the "Object" field to select the object on the chart;
-   Name — object name. This name is formed of the period of the chart the object is attached to, the object type and the unique ID that is automatically assigned to each object. The name can be changed in the [object properties](/en/docs/mt5/client/objects#name);
-   Description — object description. It can also be changed from the [object properties](/en/docs/mt5/client/objects#description);
-   Window — the number of the window the object is added on. 0 is the main chart window, further numbers mean serial numbers of indicator sub-windows from the top down.

The "Objects" window contains the following commands:

-   Show — move the chart to the selected object;
-   Properties — [edit the properties](/en/docs/mt5/client/objects#parameters) of the selected object;
-   Delete — delete the selected object;
-   List all — any object can be marked as hidden (property OBJPROP\_HIDDEN) from a [MQL5](/en/docs/mt5/client/autotrading#mql5) application. Such objects are displayed on a chart, but they are not displayed in the object list by default. Click "List all" to show the hidden objects in the list.

Press Ctrl+A to select all objects.

## List of Expert Advisors [#](charts_objects_list#ea)

To manage [Expert Advisors](/en/docs/mt5/client/trade_robots_indicators) and [scripts](/en/docs/mt5/client/autotrading#type) running on a chart click "![List of Expert Advisors](/en/docs/mt5/client/img/experts_list_icon.png "List of Expert Advisors") List of Expert Advisors" in its [context menu](/en/docs/mt5/client/charts_advanced/charts_manage#experts_list).

![List of Expert Advisors](/en/docs/mt5/client/img/experts_list.png "List of Expert Advisors")

The list includes Expert Advisors and scripts running on all currently open charts. The Charts column contains the name and timeframe of the chart, on which the Expert Advisor or the script is running.

Select an Expert Advisor or a script and click "Show" to move to the chart, on which the MQL5 application is running. To open [settings](/en/docs/mt5/client/trade_robots_indicators#run) of the selected Expert Advisor or script click "Properties". The "Delete" button stops the program and removes it from the chart.

[Chart Management](/en/docs/mt5/client/charts_advanced/charts_manage)

[Deleted Charts](/en/docs/mt5/client/charts_advanced/charts_deleted)