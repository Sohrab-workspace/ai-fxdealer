# Chart Management

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/chart_management/charts_control

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
            -   [Chart Opening](/en/docs/mt4/terminal/chart_management/charts_open)
            -   [Setup](/en/docs/mt4/terminal/chart_management/charts_setup)
            -   [Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)
                -   [Lists of Objects Applied](/en/docs/mt4/terminal/chart_management/charts_control/charts_objects_list)
            -   [Publishing Charts Online](/en/docs/mt4/terminal/chart_management/mql5_charts)
            -   [Quick Trading](/en/docs/mt4/terminal/chart_management/chart_trading)
            -   [Charts Print](/en/docs/mt4/terminal/chart_management/charts_print)
            -   [Deleted Charts](/en/docs/mt4/terminal/chart_management/charts_deleted)
            -   [Templates and Profiles](/en/docs/mt4/terminal/chart_management/templates)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Working with Charts](/en/docs/mt4/terminal/chart_management)Chart Management

# Chart Management

Charts allow to analyze price changes at the market and are used for graphical analysis, building of various [indicators](/en/docs/mt4/terminal/analytics/tech_indicators) and [line studies](/en/docs/mt4/terminal/analytics/objects_control/line_studies). Charts are a very valuable instrument for analyzing of financial markets, that is why a great attention is paid to them. Chart management means:

-   Chart Type  
    A symbol chart can be of three types:

-   -   Bar Chart — the sequence of bars.  
        To make a chart of this type, one has to press the ![Bar Chart](/en/docs/mt4/terminal/img/tb_charts_bar_chart.png "Bar Chart") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), [accelerating keys of Alt + 1](/en/docs/mt4/terminal/overview/fast_nav#accelerators), the corresponding option of the [Charts Setup](/en/docs/mt4/terminal/chart_management/charts_setup#common) window, or execute the ["Charts — Bar Chart" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command.
    -   Candlesticks — the sequence of candlesticks.  
        To make a chart of this type, one has to press the !["Candlesticks" Chart](/en/docs/mt4/terminal/img/tb_charts_candlestick.png ""Candlesticks" Chart") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), [accelerating keys of Alt + 2](/en/docs/mt4/terminal/overview/fast_nav#accelerators), the corresponding option of the [Charts Setup](/en/docs/mt4/terminal/chart_management/charts_setup#common) window, or execute the ["Charts — Candlesticks" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command.
    -   Line Chart — a broken line connecting the bar close prices.  
        To make a chart of this type, one has to press the ![Line Chart](/en/docs/mt4/terminal/img/tb_charts_line_chart.png "Line Chart") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), [accelerating keys of Alt + 3](/en/docs/mt4/terminal/overview/fast_nav#accelerators), the corresponding option of the [Charts Setup](/en/docs/mt4/terminal/chart_management/charts_setup#common) window, or execute the ["Charts — Line Chart" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command.

-   Saving  
    The client terminal allows to save history data of the active chart as a text file in formats of "CSV", "PRN", and "HTM".  
    To save them in one of these ways, one has to execute the ["File— Save As" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command or press accelerating keys of Ctrl + S. Besides, the chart can be saved as a picture in BMP or GIF format. To do so, one has to execute the ["File—Save As Picture..." menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command. The same actions can be performed by the chart context menu command of the same name.
-   Print  
    To print the active chart in color, one has to flag "Color print" in the chart settings, then execute the ["File — Print..." menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command, the chart context menu command of the same name, press the ![Print](/en/docs/mt4/terminal/img/tb_standard_print.png "Print") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard) or accelerating keys of Ctrl+P. If the "Color Print" is disabled, or there is no color printer available, the chart will bee printed as black-and-white.
-   Full Screen  
    Execution of the ["View — Full Screen" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_view) command or pressing of F11 will switch the chart to the full screen mode. Only chart windows, [main menu](/en/docs/mt4/terminal/overview/main_menu) and chart switching bar will remain in the display. One can return to the initial mode using the same command.
-   Attaching of MQL4 Programs  
    Before MQL4 starts to execute, it must be attached to the chart. To do so, one has to select the desired MQL4 program in the ["Navigator" window](/en/docs/mt4/terminal/overview/navigator) and double-click on it or execute the "Attach to a chart" command of the context menu. The "Drag'n'Drop" technique can be used, as well.
-   Working with Indicators  
    Indicator is a mathematical manipulation with price and/or volumes of a security in order to forecast future price changes. Decisions about how and when to open or close a position are made on basis of signals from technical indicators. Indicators can be imposed into a chart by the ["Insert — Indicators" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert) commands or those of indicators managing sub-menu that can be opened by pressing of the ![Indicators](/en/docs/mt4/terminal/img/tb_charts_indicators.png "Indicators") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts). The "Drag'n'Drop" technique allows to impose indicators from the ["Navigator" window](/en/docs/mt4/terminal/overview/navigator) into any open window, as well. The list of indicators imposed into the chart can be viewed in the ["Data Window"](/en/docs/mt4/terminal/overview/data_window) by executing of the ["Charts — Indicators List" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command, the chart context menu command of the same name, or by pressing accelerating keys of Ctrl+I.  
    More details about working with technical indicators can be found in the [section of the same name](/en/docs/mt4/terminal/analytics/tech_indicators).
-   Working with Objects  
    To analyze the market, one can impose various graphical objects into the chart. To do it, one has to use the ["Insert" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert) commands or buttons of the ["Line Studies" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_line_studies). [Line Studies](/en/docs/mt4/terminal/analytics/objects_control/line_studies), geometrical shapes, signs, and texts, are grouped in the menu.  
    More details can be found in the ["Graphical Objects" section](/en/docs/mt4/terminal/analytics/objects_control).
-   Period Change  
    The client terminal allows to use nine different data periods, from a minute to a month long. This variety of periods is necessary for analyzing the market with technical indicators and line studies.  
    The desired period of the chart can be chosen with help of the ["Period" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_periodicity), the ![Chart Period](/en/docs/mt4/terminal/img/tb_charts_period.png "Chart Period") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), the ["Charts — Period" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts), or by executing of the chart context menu command.
-   Zooming  
    Charts can be zoomed horizontally, increasing or decreasing thereby the amount of bars shown in the screen simultaneously.  
    To do it, one can use the buttons of ![Zoom In](/en/docs/mt4/terminal/img/tb_charts_zoom_in.png "Zoom In")/![Zoom Out](/en/docs/mt4/terminal/img/tb_charts_zoom_out.png "Zoom Out") of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), keys of "+"/"-", the commands of "Zoom In"/"Zoom Out" of the chart context menu and of the ["Charts" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts).  
    To zoom out a chart vertically, one can hold any point of vertical axis with the left mouse button and move it down. Double click on vertical axis or pressing of "5" in the keypad restores the scale.  
       
    Besides, the chart can be zoomed precisely by defining of upper and lower borders in the [Charts Setup](/en/docs/mt4/terminal/chart_management/charts_setup#common) window with the "Scale fix" option. The "Scale fix One to One" option of the same window allows to set the "one-to-one", i.e., one pip of vertical axis will correspond with one bar of the horizontal one.
-   Scrolling, Auto Scrolling, and Shifting of the Chart  
    Scrolling is moving of price data to the right/left in the chart that can be performed by cursory keys of the keyboard. Besides, the chart can be scrolled with F12 (the "Step by Step" mode — scrolling the chart by one bar to the left) or Shift+F12 (scrolling the chart by one bar to the right), or with the mouse: one moves the cursor to the right/left when holding the left mouse button pressed on any point of the chart. Using the [fast navigation box](/en/docs/mt4/terminal/overview/fast_nav#fast_nav), one can have shown the necessary area of the chart having specified the specific date and time. If the chart has been scrolled to the area where there are no price data, the missing bars will be downloaded automatically.  
       
    If the chart scale has been fixed, it can be scrolled vertically, as well. To do so, one has to move the mouse up/down while holding the slider on the vertical scale. To get the chart back into the visibility range, one has to press "5" in the keypad or double-click in the area of the chart price scale.  
       
    Auto scroll is intended for users to have the latest bars before their eyes constantly. If this option is enabled, the chart will be automatically scrolled to its end part. This function can be enabled by pressing of the ![Auto Scroll](/en/docs/mt4/terminal/img/tb_charts_auto_scroll.png "Auto Scroll") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) or by the ["Charts — Auto Scroll" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command.  
       
    The "Chart Shift" option shifts the latest bar from the right screen border to the chart shift mark. The chart shift mark (a gray triangle in the upper part of the window) can be moved horizontally with the mouse within 10 to 50% of the window size. The chart shift can be enabled by the ![Chart Shift](/en/docs/mt4/terminal/img/tb_charts_shift.png "Chart Shift") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) or by the ["Charts — Chart Shift" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command.
-   Chart Positioning  
    Normally, the chart datum point is located in the left part of the window. The specific time bar is anchored to it that can be moved through scrolling or with the use of fast navigation box. When a timeframe is changed, there will be an attempt to calculate the new anchoring bar corresponding with that of the previously used timeframe. I.e., the timeframe that is the nearest to this given point will be shown at the left side of the window. The datum point (a gray triangle at the lower border of the chart) can be moved within the chart window using the mouse. It appears only if the "Auto Scroll" is disabled. This mechanism is convenient when analyzing a certain period of time for different timeframes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Positioning does not work if the "Auto Scroll" option is enabled.</span></p></td></tr></tbody></table>

-   Working with Templates  
    Templates represent the chart window parameters stored in the memory. The following is saved in a template: chart type, period, scale, all settings of line studies, technical and custom indicators, and experts. Templates allow to unify the appearance of many charts easily and fast.  
    The menu that manages templates can be called by the ["Charts — Template" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command, the chart context menu command of the same name and the ![Chart Templates](/en/docs/mt4/terminal/img/tb_charts_template.png "Chart Templates") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts). The "Save Template..." menu command allows to store a new template, and that of "Remove Template" — to delete an existing one.  
    More details can be found in the ["Templates and Profiles" section](/en/docs/mt4/terminal/chart_management/templates).
-   Working with Profiles  
    Profiles represent a convenient way of working with chart groups. At opening of a profile, each chart with all its settings will be found in the same place where it was when the profile was being stored.  
    The menu that manages profiles can be opened by the ["File — Profiles" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command, by pressing of the ![Profile](/en/docs/mt4/terminal/img/tb_standard_profile.png "Profile") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard), or by clicking with the mouse in the status bar containing the name of the current profile.  
    More details can be found in the ["Templates and Profiles" section](/en/docs/mt4/terminal/chart_management/templates).
-   Data Updating  
    Data must be updated if any errors or "holes" occur in the price chart. In order to update the price data, one has to execute the ["Charts — Refresh" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command or the chart context menu command of the same name. After all these actions have been performed, the missing bars will be downloaded from the server automatically and drawn in the chart.

## Use of Mouse

The chart is directly managed with the mouse as follows:

-   clicking with the left mouse button on any point in the chart window and holding of it with the subsequent horizontal moving of the cursor result in the chart scrolling;
-   clicking with the left mouse button on the chart vertical scale and holding of it with the subsequent vertical moving of the cursor result in vertical chart scaling, and the double click with the mouse on the chart vertical scale will rescale the chart;
-   clicking with the left mouse button on the chart horizontal scale (but not the [fast navigation box](/en/docs/mt4/terminal/overview/fast_nav#fast_nav)) and holding of it with the subsequent horizontal moving of the cursor will result in the chart rescaling;
-   clicking with the right mouse button on any point in the chart window results in calling of the chart context menu (described below);
-   double-clicking with the left mouse button on elements of technical indicators (lines, signs, histogram bars, etc.) calls the setup window of the corresponding indicator;
-   clicking with the right mouse button on elements of a technical indicator calls the context menu of the indicator;
-   single or double, depending on the [terminal settings](/en/docs/mt4/terminal/setup/setup_objects), clicking with the left mouse button on an object ([line studies](/en/docs/mt4/terminal/analytics/objects_control/line_studies), [texts or arrows](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert)) will select the object;
-   clicking with the left mouse button on the selected object and holding of it with the subsequent moving allows to move the selected object;
-   Ctrl + clicking with the left mouse button on a selected trend line with the subsequent moving allows to draw a parallel trend line (create a channel);

-   click with the mouse wheel on a chart tab in the switch panel closes the chart;

-   clicking with the middle mouse button in the chart window switches cursor to the "crosshair" mode;
-   clicking with the right mouse button on a selected object will open its context menu;
-   placing of cursor on the bar close price or on an element of an object or indicator will call the prompt.

## Chart Management with Context Menu Commands [#](charts_control#context)

Some commands of the context menu are intended for chart management:

-   Expert Advisors — sub-menu that manages [expert advisors](/en/docs/mt4/terminal/autotrading/experts). Expert advisor is an MQL4 program that is executed with every new tick and allows to automate analytical and trading activities. Commands that manage the expert imposed into the chart are grouped in this menu, too. Using this sub-menu, one can change the expert properties, remove it, or start [testing it](/en/docs/mt4/terminal/autotrading/tester).  
    More details are given in the ["Expert Advisors" section](/en/docs/mt4/terminal/autotrading/experts).
-   Remove Script — remove an executable [script](/en/docs/mt4/terminal/autotrading/scripts). Script is a program written in [MetaQuotes Language 4 (MQL4)](/en/docs/mt4/terminal/autotrading/mql4) and intended for a single performing of some actions.
-   Indicators List — window that manages [technical indicators](/en/docs/mt4/terminal/analytics/tech_indicators) attached to the chart window. Technical indicator is a mathematical manipulation of the symbol price and/or volumes in order to forecast future price changes. On signals received from technical indicators, decisions are made about how and when to open or close a position.
-   Objects List — window that manages [graphical objects](/en/docs/mt4/terminal/analytics/objects_control). Graphical objects are those objects in the terminal that are imposed manually. They are intended for analytical purposes.
-   Timeframes — sub-menu that manages the chart periods.  
    Periods of charts can also be managed by the ["Charts" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) and [toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_periodicity) commands of the corresponding names.
-   Template — sub-menu that manages [templates](/en/docs/mt4/terminal/chart_management/templates). Template is a set of chart window parameters that can be used for other charts.  
    This sub-menu can also be called by the ["Chart" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command of the same name.
-   Refresh — refresh history data. At that, all data missing within the available history and new ones will be downloaded.  
    The same action can be performed by the ["Charts" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command of the same name.
-   Auto Arrange — set the height of all indicators windows as default.  
    The same action can be performed by pressing of accelerating keys of Ctrl+A.
-   Grid — show/hide grid.  
    The same action can be performed by the "Charts" menu command of the same name or by pressing of accelerating keys of Ctrl+G.
-   Volumes — show/hide volumes chart.  
    The same actions can be performed by the "Charts" menu command of the same name or by pressing of accelerating keys of Ctrl+L.
-   Zoom In — zoom in the chart horizontally by one step.  
    The chart can also be zoomed in by the ["Charts" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command of the same name, by pressing of "+" or the ![Zoom In](/en/docs/mt4/terminal/img/tb_charts_zoom_in.png "Zoom In") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts).
-   Zoom Out — zoom out the chart by one step.  
    The chart can also be zoomed out by the ["Charts" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command of the same name, by pressing of "-" or the ![Zoom Out](/en/docs/mt4/terminal/img/tb_charts_zoom_out.png "Zoom Out") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts).
-   Delete Indicator Window — delete indicator window from the chart. Some indicators are drawn in special sub-windows and have their own scaling. This command allows to delete such a sub-window.  
    More details about working with technical indicators can be found in the [corresponding section](/en/docs/mt4/terminal/analytics/tech_indicators).
-   Save As Picture — save the chart as a picture (GIF or BMP).  
    The same action can be performed by the ["File — Save As Picture..." menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command.
-   Print Preview — preview the chart image before printing.  
    The same action can be performed by the ["File — Print Preview" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command or by pressing of the ![Print Preview](/en/docs/mt4/terminal/img/tb_standard_print_prev.png "Print Preview") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Print... — print the chart. If the "Color print" option is checked in the [program settings](/en/docs/mt4/terminal/setup/setup_charts), chart can be printed in color.  
    The same action can be performed by the ["File — Print..."](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) menu command, accelerating keys of Ctrl+P, or the ![Print Chart](/en/docs/mt4/terminal/img/tb_standard_print.png "Print Chart") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Properties... — call the [charts setup window](/en/docs/mt4/terminal/chart_management/charts_setup).  
    The same action can be performed by pressing of F8.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The "Expert Advisors" sub-menu, as well as the commands of "Remove Script", "Indicators List", and "Objects List" are activated only if the corresponding objects have been imposed into the chart.</span></p></td></tr></tbody></table>

[Setup](/en/docs/mt4/terminal/chart_management/charts_setup)

[Lists of Objects Applied](/en/docs/mt4/terminal/chart_management/charts_control/charts_objects_list)