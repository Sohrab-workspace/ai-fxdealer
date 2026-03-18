# Fast Navigation

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/fast_nav

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)Fast Navigation

# Fast Navigation

There are various methods used in the Client Terminal to accelerate working. The following can be used for this purpose:

-   [fast navigation box](/en/docs/mt4/terminal/overview/fast_nav#fast_nav) — a small box that appears in the lower left corner of the chart and allows to manage it;
-   [accelerating (hot) keys](/en/docs/mt4/terminal/overview/fast_nav#accelerators) — key combinations that are intended for acceleration of working with various functions of the program.

## Fast Navigation Box [#](fast_nav#fast_nav)

The fast navigation box is used for quick switching among charts and/or among chart periods, as well as for quick scrolling of the chart to the selected date. The fast navigation box of the active chart can be opened with the Enter key, then the fast navigation box will appear in the lower left part of the chart window. One can also move the cursor to the lower left part of the chart window and double-click the left mouse button after the ![Fast navigation](/en/docs/mt4/terminal/img/cursor_fast_nav.png "Fast navigation") icon has appeared.

![Fast Navigation Box](/en/docs/mt4/terminal/img/win_fast_nav.png "Fast Navigation Box")

Format of commands in the fast navigation box:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Format</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">[time (hours:minutes)]</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">08:30; 8:30;</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">[date]</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">2004.10.16; 16.10.2004; 16.10.04;</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">[date and time]</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">2004.10.16 8:30; 16.10.2004 8:30; 16.10.04 8:30;</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">[symbol]</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">GBPUSD; EURUSD;</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">[chart period]</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">M1; M5; M15; M30; H1; H4; D1; W1; MN;</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">[symbol], [chart period]</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">GBPUSD, M30; EURUSD, D1;</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: It must be noted that only one of the above-listed commands can be executed in the fast navigation box.</span></p></td></tr></tbody></table>

To execute a command, one has to press the Enter key, and the Esc key - to close the box. To move the chart to a specific date and time, one has to input this date and time. For example, the command that allows to move to the bar received at 8:30 on October, 16 2004, will appear as "2004.10.16 08:30". Along with YYYY.MM.DD and DD.MM.YYYY formats, one can also use the DD.MM.YY format, but not the YY.MM.DD. The first zero in the time inputting can be skipped. For example, one can write "8:30" instead of "08:30". When changing a symbol, one should specify its full name. When specifying the chart period, one may skip the "M". At the "GBPUSD 30" command, as well as at the "GBPUSD M30", the symbol and period will respectively change for a 30-minutes chart of Great Britain Pound vs US Dollar.

## Hot Keys [#](fast_nav#accelerators)

Hot keys (accelerating keys) are keys and their combinations that allow to execute various commands fast and without using of menus or toolbars.

-   "Arrow Left" — chart scrolling to the left;
-   "Arrow Right" — chart scrolling to the right;
-   "Arrow Up" — fast chart scrolling to the left or, if the scale is defined, chart scrolling up;
-   "Arrow Down" — fast chart scrolling to the right or, if the scale is defined, chart scrolling down;
-   Numpad 5 — restoring of automatic chart vertical scale after its being changed. If the scale was defined, this hot key will return the chart into the visible range;
-   Page Up — fast chart scrolling to the left;
-   Page Down — fast chart scrolling to the right;
-   Home — move the chart to the start point;
-   End — move the chart to the end point;
-   "-" — chart zoom out;
-   "+" — chart zoom in;
-   Delete — delete all selected graphical objects;
-   Backspace — delete the latest objects imposed into the chart window;
-   Enter — open/close fast navigation window;
-   Esc — close the dialog window;
-   F1 — open this "Userguide";
-   F2 — open the ["History Center" window](/en/docs/mt4/terminal/service/history_center);
-   F3 — open the ["Global Variables" window](/en/docs/mt4/terminal/service/global_variables);
-   F4 — download [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor);
-   F6 — call the ["Tester" window](/en/docs/mt4/terminal/overview/strategy_tester) for testing the expert attached to the chart window;
-   F7 — call the properties window of the expert attached to their chart window in order to change settings;
-   F8 — call the [chart setup window](/en/docs/mt4/terminal/chart_management/charts_setup);
-   F9 — call the "New Order" window;
-   F10 — open the ["Popup prices"](/en/docs/mt4/terminal/overview/market_watch) window;
-   F11 — enable/disable the full screen mode;
-   F12 — move the chart by one bar to the left;

-   Shift+F12 — move the chart by one bar to the right;
-   Shift+F5 — switch to the previous profile;

-   Alt+1 — display the chart as a sequence of bars (transform into bar chart);
-   Alt+2 — display the chart as a sequence of candlesticks (transform into candlesticks);
-   Alt+3 — display the chart as a broken line (transform into line chart);
-   Alt+A — copy all test/optimization results into the clipboard;
-   Alt+W — call the chart managing window;
-   Alt+F4 — close the client terminal;
-   Alt+Backspace or Ctrl+Z — undo object deletion;

-   Ctrl+A — arrange all indicator windows heights by default;
-   Ctrl+B — call the "Objects List" window;
-   Ctrl+C or Ctrl+Insert — copy to the clipboard;
-   Ctrl+E — enable/disable expert advisor;
-   Ctrl+F — enable "Crosshair";
-   Ctrl+G — show/hide grid;
-   Ctrl+H — show/hide OHLC line;
-   Ctrl+I — call the "Indicators List" window;
-   Ctrl+L — show/hide volumes;
-   Ctrl+P — print the chart;
-   Ctrl+S — save the chart in a file having extensions: "CSV", "PRN", "HTM";
-   Ctrl+W or Ctrl+F4 — close the chart window;
-   Ctrl+Y— show/hide period separators;
-   Ctrl+Z or Alt+Backspace — undo the object deletion;
-   Ctrl+D — open/close the ["Data Window"](/en/docs/mt4/terminal/overview/data_window);
-   Ctrl+M — open/close the ["Market Watch" window](/en/docs/mt4/terminal/overview/market_watch);
-   Ctrl+N — open/close the ["Navigator" window](/en/docs/mt4/terminal/overview/navigator);
-   Ctrl+O — open the ["Setup" window](/en/docs/mt4/terminal/setup);
-   Ctrl+R — open/close the ["Tester" window](/en/docs/mt4/terminal/overview/strategy_tester);
-   Ctrl+T — open/close the ["Terminal" window](/en/docs/mt4/terminal/overview/terminal);
-   Ctrl+F5 — switch to the next [profile](/en/docs/mt4/terminal/chart_management/templates);
-   Ctrl+F6 — activate the next chart window;
-   Ctrl+F9 — open the "Terminal — Trade" window and switch the focus into it. After this, the trading activities can be managed with keyboard.

There is a feature allowing to defined hot keys for calling any element of the "Navigator" window, except for those of the "Accounts" group. To define a combination of keys to an element, one has to execute the "Define a hot key" command of its context menu. The defined hot keys are of higher priority being compared to those pre-defined. For example, Ctrl+O combination meant initially the calling of the [Terminal setup window](/en/docs/mt4/terminal/setup). If one defines calling of the [On Balance Volume](/en/docs/mt4/terminal/analytics/tech_indicators/on_balance_volume) indicator for the same combination, it will not be possible to call the terminal setup window by pressing of Ctrl+O.

[Search](/en/docs/mt4/terminal/overview/search)

[Working with Charts](/en/docs/mt4/terminal/chart_management)