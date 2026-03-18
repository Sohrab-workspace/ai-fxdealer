# Charts

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/main_menu/main_menu_charts

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
            -   [Main Menu](/en/docs/mt4/terminal/overview/main_menu)
                -   [File](/en/docs/mt4/terminal/overview/main_menu/main_menu_file)
                -   [View](/en/docs/mt4/terminal/overview/main_menu/main_menu_view)
                -   [Insert](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert)
                -   [Charts](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts)
                -   [Tools](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools)
                -   [Window](/en/docs/mt4/terminal/overview/main_menu/main_menu_window)
                -   [Help](/en/docs/mt4/terminal/overview/main_menu/main_menu_help)
            -   [Toolbars](/en/docs/mt4/terminal/overview/toolbars)
            -   [Market Watch](/en/docs/mt4/terminal/overview/market_watch)
            -   [Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)
            -   [Data Window](/en/docs/mt4/terminal/overview/data_window)
            -   [Navigator](/en/docs/mt4/terminal/overview/navigator)
            -   [Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)
            -   [Client terminal](/en/docs/mt4/terminal/overview/terminal)
            -   [Tester](/en/docs/mt4/terminal/overview/strategy_tester)
            -   [Search](/en/docs/mt4/terminal/overview/search)
            -   [Fast Navigation](/en/docs/mt4/terminal/overview/fast_nav)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Main Menu](/en/docs/mt4/terminal/overview/main_menu)Charts

# Charts

Commands managing the chart and technical indicators imposed in it are collected in the "Charts" menu.

![chart_menu](/en/docs/mt4/terminal/img/chart_menu.png)

The following commands are available in this menu:

-   Indicators List — call window managing indicators imposed in the active chart. The full list of indicators imposed (including [Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)) is given in the window appeared. Having selected an indicator, one can change its settings or remove it from the chart.  
    The same action can be performed by the chart context menu command of the same name or by accelerating keys of Ctrl+I;
-   Objects — call sub-menu managing imposed objects. The following commands are available in the sub-menu:

-   -   Objects List — call window managing the imposed objects. Objects include line studies, signs, shapes, and texts. The selected object can be modified (the "Edit" button) or deleted by pressing of the button of the same name in this window. Besides, the "Show" command moves the active chart to the imposed object location;
    -   Delete Last — delete the last imposed object from the chart.  
        The same action can be performed by pressing the Backspace button;
    -   Delete All Selected — delete all selected objects from the chart window.  
        The same action can be performed by pressing the Delete button;
    -   Delete All Arrows — delete all objects from the chart window;
    -   Unselect All — unselect all the objects imposed in the chart;
    -   Undo Delete — return the deleted object back into the chart.  
        The same action can be performed by accelerating keys of Ctrl+Z;

-   Bar Chart — display the chart as a sequence of bars.  
    Execution of this command is the same as pressing of the ![Bar Chart](/en/docs/mt4/terminal/img/tb_charts_bar_chart.png "Bar Chart") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) or accelerating keys of Alt+1;
-   Candlesticks — display the chart as a sequence of "candlesticks".  
    Execution of this command is the same as pressing of the ![Candlesticks](/en/docs/mt4/terminal/img/tb_charts_candlestick.png "Candlesticks") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) or accelerating keys of Alt+2;
-   Line Chart — display the chart as a broken line connecting close prices of bars.  
    Execution of this command is the same as pressing of the ![Line Chart](/en/docs/mt4/terminal/img/tb_charts_line_chart.png "Line Chart") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) or accelerating keys of Alt+3;
-   Foreground Chart — put the chart as a "foreground". If this function is enabled, all analytical objects (technical indicators and graphical objects) will be placed "behind the chart", not over it;
-   Timeframes — choose the chart timeframe. After this command has been executed, a sub-menu will appear where the active chart timeframe can be selected.  
    The chart timeframe can also be changed with help of the ["Timeframes" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_periodicity);
-   Template — call the template managing sub-menu. From this sub-menu, one can impose any template into the active chart. Moreover, a new template can be stored based on the active chart, or an existing one can be deleted. More details about working with templates can be found in the ["Profiles and Templates"](/en/docs/mt4/terminal/chart_management/templates) section.  
    The sub-menu managing templates can also be called by pressing of the ![Profiles](/en/docs/mt4/terminal/img/tb_charts_template.png "Profiles") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts)or by the [chart context menu](/en/docs/mt4/terminal/chart_management/charts_control#context) command of the same name;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The DEFAULT template cannot be deleted.</span></p></td></tr></tbody></table>

-   Refresh — refresh history data. At that, all missing data within the existing history will be downloaded. The same action can be performed by the chart context menu command of the same name.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: History outside the range of the existing data will not be added.</span></p></td></tr></tbody></table>

-   Grid — show/hide grid in the chart window.  
    The same actions can be performed by the [chart context menu](/en/docs/mt4/terminal/chart_management/charts_control#context) command of the same name and by pressing of the accelerating keys of Ctrl+G;
-   Volumes — show/hide volumes in the chart.  
    The same actions can be performed by the [chart context menu](/en/docs/mt4/terminal/chart_management/charts_control#context) command of the same name or by pressing of accelerating keys of Ctrl+L;
-   Auto Scroll — enable/disable automatic shifting of the chart to the left after a new bar has started to form. If this option is enabled, the last bar will always be shown in the chart.  
    Execution of this command is the same as pressing of the !["Auto Scroll" function](/en/docs/mt4/terminal/img/tb_charts_auto_scroll.png ""Auto Scroll" function") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts);
-   Chart Shift — shift the chart from the left window border to the shift label of the chart. The shift label of the chart (a grey triangle in the upper part of the window) can be moved with the mouse horizontally within 10 to 50% of the window size.  
    Execution of this command is the same as pressing of the !["Chart Shift" function](/en/docs/mt4/terminal/img/tb_charts_shift.png ""Chart Shift" function") button of the ["Charts"](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) toolbar;
-   Zoom In — zoom in the chart.  
    The same action can be performed by pressing of the "+" key or the ![Zoom In](/en/docs/mt4/terminal/img/tb_charts_zoom_in.png "Zoom In") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), as well as by moving the cursor to the right, the left mouse button being pressed on the horizontal scale;
-   Zoom Out — zoom out the chart.  
    The same action can be performed by pressing of the "-" key or the ![Zoom Out](/en/docs/mt4/terminal/img/tb_charts_zoom_out.png "Zoom Out") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), as well as by moving the cursor to the left, the left mouse button being pressed on the horizontal scale;
-   Step by Step — shift the chart by one bar to the left.  
    The same action can be performed by pressing of F12;
-   Properties... — setting up the chart parameters. At this command execution, the [chart setup window](/en/docs/mt4/terminal/chart_management/charts_setup) will appear.  
    The same actions can be performed by the chart context menu command of the same name or by pressing of F8.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The most of the "Charts" menu commands are duplicated in the <a href="/en/docs/mt4/terminal/overview/toolbars/toolbars_charts" class="topiclink">toolbar</a> of the same name and in the <a href="/en/docs/mt4/terminal/chart_management/charts_control#context" class="topiclink">chart context menu</a>.</span></p></td></tr></tbody></table>

[Insert](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert)

[Tools](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools)