# Chart Management

> Source: https://support.metaquotes.net/en/docs/mt5/client/charts_advanced/charts_manage

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Additional Features](/en/docs/mt5/client/charts_advanced)Chart Management

# Chart Management

This section provides information about how to manage charts in the trading platform.

-   [Chart managing using the context menu and the "Charts" menu](/en/docs/mt5/client/charts_advanced/charts_manage#context)
-   [Chart managing using a mouse](/en/docs/mt5/client/charts_advanced/charts_manage#mouse)
-   [Chart managing from keyboard](/en/docs/mt5/client/charts_advanced/charts_manage#keyboard)
-   [Fixed chart position](/en/docs/mt5/client/charts_advanced/charts_manage#fixed)

## Chart Managing Using the Context Menu and the ["Chart"](/en/docs/mt5/client/interface) Menu [#](charts_manage#context)

Commands in these menus are identical (except for "Save As Picture" and "Delete Indicators Window" that are available only in the context menu) and allow to manage chart settings:

-   Trading — open the menu of trading operations for the symbol of the chart: [placing stop levels](/en/docs/mt5/client/one_click_trading#chart_deal) or [pending orders](/en/docs/mt5/client/performing_deals#pending_chart).
-   ![Depth of Market](/en/docs/mt5/client/img/dom_icon.png "Depth of Market") Depth Of Market — open the Depth of Market of the current chart's symbol.
-   ![List of indicators](/en/docs/mt5/client/img/indicators_list_icon.png "List of indicators") Indicator List — open the ["Indicator List"](/en/docs/mt5/client/charts_advanced/charts_objects_list#indicators) window for managing indicators running on the chart.
-   Objects — open the objects control submenu:

-   ![List of objects](/en/docs/mt5/client/img/objects_list_icon.png "List of objects") Object List — open the ["Object List"](/en/docs/mt5/client/charts_advanced/charts_objects_list#objects) to manage objects on the chart.

-   Delete Last — delete the last added object.
-   ![Delete All Selected](/en/docs/mt5/client/img/delete_all_selected_icon.png "Delete All Selected") Delete All Selected — delete all selected objects.
-   ![Delete All Arrows](/en/docs/mt5/client/img/delete_all_arrows_icon.png "Delete All Arrows") Delete All Arrows — delete all arrows belonging to the [Arrows](/en/docs/mt5/client/objects/arrows) group.
-   Delete All — delete all [objects](/en/docs/mt5/client/objects) from the current chart;
-   Unselect All — unselect all objects on the chart.
-   Unselect — unselect the selected object.
-   ![Undo Delete](/en/docs/mt5/client/img/undo_delete_icon.png "Undo Delete") Undo Delete — restore the last deleted object.
-   ![List of Expert Advisors](/en/docs/mt5/client/img/experts_list_icon.png "List of Expert Advisors") Expert List— open the ["Expert List"](/en/docs/mt5/client/charts_advanced/charts_objects_list#ea) window to manage Expert Advisors running on the chart.
-   ![Bar chart](/en/docs/mt5/client/img/bar_chart_icon.png "Bar chart") Bar chart — show the chart as a sequence of bars.
-   ![Candlesticks](/en/docs/mt5/client/img/candlestciks_icon.png "Candlesticks") Candlestick — show the chart as a sequence of Japanese candlesticks.
-   ![Line Chart](/en/docs/mt5/client/img/line_chart_icon.png "Line Chart") Line — show the chart as a broken line that connects close prices of bars.
-   Timeframes — select the chart timeframe. A click on this item opens a sub menu, where you can select one of the available timeframes.
-   Templates — managing [chart templates](/en/docs/mt5/client/charts_advanced/templates_profiles).
-   ![Refresh](/en/docs/mt5/client/img/refresh_icon.png "Refresh") Refresh — refresh the chart window. When you refresh the chart, the price data displayed on it are also recalculated based on one-minute data stored on the computer.
-   ![Docked](/en/docs/mt5/client/img/docked_icon.png "Docked") Docked — [dock/undock the chart window](/en/docs/mt5/client/charts#docked) from the main platform window.
-   Toolbar — show/hide the toolbar in the chart window. The command is only available for the charts, which were detached from the main platform window.
-   ![Grid](/en/docs/mt5/client/img/grid_icon.png "Grid") Grid — show/hide grid on the chart.
-   ![Auto Scroll](/en/docs/mt5/client/img/autoscroll_icon.png "Auto Scroll") Auto Scroll — enable/disable automatic chart scrolling to its beginning when new ticks are received.
-   ![Chart Shift](/en/docs/mt5/client/img/chart_shift_icon.png "Chart Shift") Chart Shift — enable/disable chart shift from the right side of the window.
-   ![One Click Trading](/en/docs/mt5/client/img/chart_oneclick_trading_context.png "One Click Trading") One Click Trading — show/hide the [one click trading panel](/en/docs/mt5/client/one_click_trading#chart_deal) on the chart.
-   ![Volumes](/en/docs/mt5/client/img/volumes_icon.png "Volumes") Volumes — show/hide real trade volumes for the charts of exchange instruments.
-   ![Tick Volumes](/en/docs/mt5/client/img/tick_volume_icon.png "Tick Volumes") Tick Volumes — show/hide tick volumes for the charts of Forex instruments.
-   ![Zoom In](/en/docs/mt5/client/img/zoom_in_icon.png "Zoom In") Zoom In — zoom in the chart.
-   ![Zoom Out](/en/docs/mt5/client/img/zoom_out_icon.png "Zoom Out") Zoom Out — zoom out the chart.
-   ![Delete Indicators Window](/en/docs/mt5/client/img/delete_indicator_window.png "Delete Indicators Window") Delete Indicator Window — delete the indicator subwindow. This command is only available in the context menu when called from the subwindow, in which the indicator is opened.
-   ![Step by Step](/en/docs/mt5/client/img/step_by_step_icon.png "Step by Step") Step by Step — move the chart bar by bar from right to left. This function is only available when the autoscroll feature is disabled.
-   ![Save As Picture](/en/docs/mt5/client/img/save_as_picture_icon.png "Save As Picture") Save As Picture — save the chart as a picture in a \*.png file. This command also allows to immediately publish a screenshot of the chart online using a special service of the [MQL5.community](https://www.mql5.com/ "MQL5.community") site and share it with other traders. See "[Publishing Charts Online](/en/docs/mt5/client/mql5_charts)" for details.
-   ![Properties](/en/docs/mt5/client/img/chart_properties_icon.png "Properties") Properties — open the [chart properties](/en/docs/mt5/client/charts_advanced/charts_settings) managing window.

## Chart Managing Using a Mouse [#](charts_manage#mouse)

A chart can be managed using a mouse:

-   click-and-hold anywhere in the chart window and then move the cursor horizontally to scroll the chart;
-   click-and-hold on the vertical scale of the chart and move the cursor vertically to change the vertical scale of the chart; double-click on the vertical scale of the chart to restore the chart scale;
-   click-and-hold on the horizontal chart scale (anywhere outside the [fast navigation bar](/en/docs/mt5/client/interface)) and move the cursor horizontally to change the chart scale;
-   right-click anywhere in the chart window to open the context menu of the chart (see below);
-   double-click on the elements of technical indicators (lines, signs, histogram bars, etc.) to call the indicator setup window;
-   right-click on elements of a technical indicator to call the context menu of the indicator;
-   depending on the [platform settings](/en/docs/mt5/client/settings#charts), a single or a double click on an [object](/en/docs/mt5/client/objects) (line studies, text or arrow) selects the object;
-   click-and-hold the selected object and drag to move it;
-   Ctrl + left-clicking on a selected trend line and then moving the cursor allows to draw a parallel trend line (create a channel);
-   hold down Ctrl and scroll the mouse wheel to scale the chart;
-   click with the mouse wheel on a chart tab in the switch panel closes the chart;
-   middle-click on the chart window to switch the cursor to the "crosshair" mode;
-   right-click on a selected object to open its context menu;
-   point your mouse to the Close price of a bar or to an element of an object or indicator to call a prompt.

## Chart Managing from Keyboard [#](charts_manage#keyboard)

Various chart manipulations can be performed using certain keys and key combinations:

-   Home — move the chart to the last bar;
-   End — move the chart to the first bar;
-   Page Up — move the chart at a one-window distance back;
-   Page Down — move the chart at a one-window distance forward;
-   Ctrl+I — open the window containing the list of indicators;
-   Ctrl+B — open the window containing the list of objects;
-   Alt+1 — show the chart as a sequence of bars;
-   Alt+2 — show the chart as a sequence of Japanese candlesticks;
-   Alt+3 — show the chart as a broken line that connects the Close prices of bars;
-   Ctrl+G — show/hide grid in the chart window;
-   "+" — zoom in the chart;
-   "\-" — zoom out the chart;
-   F12 — scroll the chart step by step (bar by bar);
-   F8 — open the properties window;
-   Backspace — delete the last added object from the chart;
-   Delete — delete all selected objects;
-   Ctrl+Z — cancel deletion of the last object.

## Fixed Chart Position [#](charts_manage#fixed)

Every chart has an icon — a gray triangle located in the bottom left corner of the window by default. Move the triangle on any bar to lock its position on the chart:

![Fixed chart position](/en/docs/mt5/client/img/fixed_chart_position.png "Fixed chart position")

The selected bar stays in this position when you zoom the chart. The position stays fixed until you change the [chart timeframe](/en/docs/mt5/client/charts#operations).

[Chart Print](/en/docs/mt5/client/charts_advanced/charts_print)

[Lists of Objects Applied](/en/docs/mt5/client/charts_advanced/charts_objects_list)