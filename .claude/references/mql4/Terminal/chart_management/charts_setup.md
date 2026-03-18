# Setup

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/chart_management/charts_setup

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Working with Charts](/en/docs/mt4/terminal/chart_management)Setup

# Setup

Appearance and properties of each chart in the terminal can be set up individually. To do so, one has to execute the ["Charts — Properties..." menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command, the chart context menu command of the same name, or press F8. These actions result in appearing of the "Properties" window that can be used for setting of the color of various elements of the chart (the "Colors") tab:

-   Background — chart background color;
-   Foreground — color of axes, scales, OHLC line;
-   Grid — chart grid color;
-   Bar Up — bar up, shades and fringing of the Bull Candle body;
-   Bar Down — bar down, shades and fringing of the Bear Candle body;
-   Bull candle — color of the Bull Candle body;
-   Bear candle — color of the Bear Candle body;
-   Line graph — line chart and doji;
-   Volumes — volumes and levels of open positions;
-   Ask line — color of the Ask line;
-   Stop levels — levels of [stop orders](/en/docs/mt4/terminal/positions/orders) (Stop Loss and Take Profit).

![chart_properties_colors](/en/docs/mt4/terminal/img/chart_properties_colors.png)

The changes made are automatically shown in the left part of the window in the preview chart. Except for manual setting of various color elements of the chart, one can choose pre-defined color diagrams in the field of the same name. There are three color diagrams available in the terminal: "Yellow on Black", "Green on Black", and "Black on White". After a color diagram has been chosen, the chart elements described above will change in the chart in the left part of the window. Custom color diagrams can be stored in [templates](/en/docs/mt4/terminal/chart_management/templates).

Other chart settings can be defined in this window, as well. To do so, one has to switch to the "Common" tab and select the desired options:

-   Offline chart — turn the chart offline. This option stops receiving and drawing of price data for the given chart. In future, after this option is disabled, price data will be drawn in the chart again. After the chart has been opened offline, (the ["File — Open offline" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command), this option will be enabled automatically.
-   Chart on foreground — place the chart in the "foreground". If this function is enabled, all [analytical objects](/en/docs/mt4/terminal/analytics) will be placed "under" the price chart.  
    This command is the same as that of ["Charts — Foreground chart"](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts).
-   Chart shift — shift the chart from the right border of the window to the shift mark. The chart shift mark (a gray triangle in the upper part of the window) can be moved with the mouse horizontally within 10 to 50% of the window size.  
    This option can also be enabled with the !["Chart Shift" Function](/en/docs/mt4/terminal/img/tb_charts_shift.png ""Chart Shift" Function") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) or by the ["Charts — Chart Shift" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command.
-   Chart autoscroll — allow/forbid to shift the chart to the left automatically after the new bar has started to form. If this option is enabled, the latest bar will always be shown in the chart.  
    This option can also be enabled by the !["Auto Scroll" Function](/en/docs/mt4/terminal/img/tb_charts_auto_scroll.png ""Auto Scroll" Function") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts) and by the ["Charts — Auto Scroll" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command.
-   Scale fix One to One — fix the chart scale as "one to one" (the size of one pip of the vertical axis in pixels is equal to the distance between the bars axes in pixels). At that, the "Scale fix" option will be enabled automatically, and a scroll bar will appear at the right side of the window that allows to move the chart vertically. This mode is necessary for precise constructions.
-   Scale fix — fix the current chart scale. If the scale has not been fixed, the chart will be automatically scaled vertically. This option disables automatic scaling and fixes the current scale. When this option is selected, the fields of additional scaling parameters "Fixed maximum" and "Fixed minimum" are activated.
-   Bar chart — display the chart as a sequence of bars.  
    This action can also be performed with the ![Bar Chart](/en/docs/mt4/terminal/img/tb_charts_bar_chart.png "Bar Chart") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), by the ["Charts — Bar Chart" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command or by pressing of [accelerating keys of Alt+1](/en/docs/mt4/terminal/overview/fast_nav#accelerators).
-   Candlesticks — display the chart as a sequence of candlesticks.  
    This action can also be performed with the ![Candlesticks](/en/docs/mt4/terminal/img/tb_charts_candlestick.png "Candlesticks") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), by the ["Charts — Candlesticks" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command, or by pressing of [accelerating keys of Alt+2](/en/docs/mt4/terminal/overview/fast_nav#accelerators).
-   Line chart — display the chart as a broken line that connects the points of bar close prices.  
    This action can also be performed by the ![Line Chart](/en/docs/mt4/terminal/img/tb_charts_line_chart.png "Line Chart") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts), by the ["Charts — Line Chart" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command, or by pressing of [accelerating keys of Alt+3](/en/docs/mt4/terminal/overview/fast_nav#accelerators).
-   Show OHLC — show/hide OHLC line. If this action is done, an additional data line will appear in the upper left part of the window. Except for symbol name and chart period, the latest bar prices are listed in it. Price are recorded in the following format: OPEN, HIGH, LOW and CLOSE (OHLC) — bar open price, the highest bar price, the lowest bar price, and bar close price, respectively. Thus, precise value of the latest bar can always be seen. This option influences the data line of sub-windows of indicators, as well.
-   Show Ask line — show/hide Ask price level of the latest quote. Bars are drawn and shown only on Bid prices in the terminal. However, at opening of long positions and closing of the short ones, the Ask price is always used. It is not shown in the chart in any way, so it cannot be seen. To control one's trading activities more precisely, one can enable the "Show Ask line" parameter. After this command has been executed, an additional horizontal line will appear in the chart that correspond with the Ask line of the latest bar.
-   Show period separators — show/hide period separators. Date and time of each bar are displayed on the horizontal axis of the chart. And this horizontal scale interval is the selected timeframe. The "Show period separators" option draws additional vertical lines in the chart that correspond with the larger period (timeframe) borders. So, daily separators will be drawn for charts with periods of M1 to H1, weekly ones — for H4, monthly ones — for D1, and yearly ones — for W1 and MN1.
-   Show grid — show/hide grid in the chart window.  
    The same actions can be performed by the chart context menu and ["Charts" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command of the same name, as well as by pressing of [accelerating keys of Ctrl+G](/en/docs/mt4/terminal/overview/fast_nav#accelerators).
-   Show volumes — show/hide the volume chart in the lower part of the window. This option does not function when the scale is fixed.  
    The same actions can be performed by the chart context menu and ["Charts" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command of the same name, as well as by pressing of [accelerating keys of Ctrl+L](/en/docs/mt4/terminal/overview/fast_nav#accelerators).
-   Show object descriptions — show/hide object descriptions in the chart. If this option is enabled and there are descriptions of objects imposed into the chart available, they will be shown directly in the chart.

![chart_properties_common](/en/docs/mt4/terminal/img/chart_properties_common.png)

[Chart Opening](/en/docs/mt4/terminal/chart_management/charts_open)

[Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)