# Code Profiling

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/development/profiling

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

# Code Profiling

Profiling is a process of gathering application features, such as an execution time of its individual fragments (functions, lines). MetaEditor has integrated means of code profiling allowing a programmer to optimize a source code.

Profiling can be performed on the normal chart of the trading platform, as well as using history data in the Strategy Tester. In the first case, a program is launched on a chart that is updated in real time. You can check the program behavior in real conditions. In the second case, the program is launched in the Strategy Tester in the visual mode. The advantage of this method is that you do not need to wait for real data from a trade server.

Many programs, especially indicators, only perform calculations at the arrival of a new tick (OnTick, OnCalculate). Thus, in order to evaluate performance, you have to wait for new ticks in real time. When profiling using history data, you can immediately provide the required load and test the program performance even on weekends when markets are closed.

## Profiling Launch

To launch code profiling, open an application source code (mq4 or mq5). In the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug) menu or on the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar, click "![Start Profiling on Real Data](/en/docs/mt5/metaeditor/img/start_profiling_icon.png "Start Profiling on Real Data") Start Profiling on Real Data" or "![Start Profiling on History Data](/en/docs/mt5/metaeditor/img/start_profiling_history_icon.png "Start Profiling on History Data") Start Profiling on History Data".

After that, a special program version for profiling will be compiled automatically. Depending on the selected profiling type, the program will be launched on a normal chart in the trading terminal or in the Strategy Tester (in the visual mode).

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">The application is launched on EURUSD H1 chart by default. To select another symbol and period, specify them on <a href="/en/docs/mt5/metaeditor/settings/settings_debug" class="topiclink">"Debugging"</a> tab of MetaEditor options.</span></p></td></tr></tbody></table>

After the application has been launched, you should work with it for some time using all its functions to the maximum possible extent. That is necessary to allow profiler to measure functions and application lines execution time.

Next, the profiling should be stopped using "![Stop profiling](/en/docs/mt5/metaeditor/img/stop_profiling_icon.png "Stop profiling") Stop profiling" command in the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug) menu or on the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">To get more accurate results of profiling, remove the program from the chart manually instead of using command "<img class="help" alt="Stop profiling" title="Stop profiling" width="10" height="10" src="/en/docs/mt5/metaeditor/img/stop_profiling_icon.png"> Stop profiling".</span></p></td></tr></tbody></table>

## View Profiling Results

After profiling completion, its results will be displayed in the special ["Profiler"](/en/docs/mt5/metaeditor/interface/toolbox/toolbox_profiler) tab of "Toolbox" window. Two modes of viewing the results are available. It is possible to switch between them using the context menu.

### "Functions by Calls" Mode

![Profiling results](/en/docs/mt5/metaeditor/img/toolbox_profiler.png "Profiling results")

In this mode, the profiling results are presented by functions:

-   Function — class function or method name.
-   Line — the line, at which the function is called. If the function is called at several locations of the application, its icon will be marked by the special symbol ![Expand](/en/docs/mt5/metaeditor/img/profiler_expand_icon.png "Expand"). Clicking on it will open the data on each call.
-   Count — number of function calls during the whole time of the application operation.
-   Time — function execution time in microseconds and percentage values relative to all functions execution time. Function execution time is a sum of execution times of all functions called within it.
-   Graph — functions execution time graph.

The functions types are displayed using the icons:

-   ![Custom function](/en/docs/mt5/metaeditor/img/function_icon.png "Custom function")—  custom function;
-   ![System function](/en/docs/mt5/metaeditor/img/function_system_icon.png "System function") — system function;
-   ![Event handling function](/en/docs/mt5/metaeditor/img/function_event_icon.png "Event handling function")— event handling function (On\*);
-   ![Class method](/en/docs/mt5/metaeditor/img/class_public_method_icon.png "Class method")— class method.

Apart from the mentioned functions types, the profiler also displays:

-   ![System function](/en/docs/mt5/metaeditor/img/function_system_icon.png "System function")@global\_initializations — data on all global variables initialization;
-   ![System function](/en/docs/mt5/metaeditor/img/function_system_icon.png "System function")@global\_deinitializations — data on all global variables deinitialization;

To view a function in a file, double left click on it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">The profiler displays only the functions that have been called during the application operation.</span></p></td></tr></tbody></table>

### "Functions by Lines" Mode

![Profiling results](/en/docs/mt5/metaeditor/img/toolbox_profiler_lines.png "Profiling results")

In this mode, the data on the application operation time is represented by lines. The lines are grouped by the application functions.

-   Function — function name.
-   Line — index of the line, for which the data is displayed. To view the data on each function line execution time, click the icon ![Expand](/en/docs/mt5/metaeditor/img/profiler_expand_icon.png "Expand").
-   Count — the number of times a code was executed in a specified line.
-   Time — code execution time in a specified line in microseconds and percentage values. Percentage values are displayed for each line relative to the function execution time. Percentage values for functions are displayed relative to the whole application execution time.
-   Graph — execution time graph.

To view a line in a file, double left click on it.

## Context menu

The following commands are available in the context menu:

-   Open — move to a line or a function in a source code file. The same action can be executed by double clicking or pressing Enter.
-   Expand All — expand all collapsed functions;
-   Collapse All — collapse all expanded functions;
-   Functions by Lines — switch to viewing profiling results [by lines](/en/docs/mt5/metaeditor/development/profiling#lines);
-   Functions by Calls — switch to viewing profiling results [by calls](/en/docs/mt5/metaeditor/development/profiling#calls);
-   Export — export profiling results in Open XML (MS Office Excel), HTML (Internet Explorer) or CSV (Text file).
-   Auto Arrange — enable/disable automatic sizing of fields. The same action can be done by pressing "A";
-   Grid — show/hide grid to separate fields. The same action can be done by pressing "G".