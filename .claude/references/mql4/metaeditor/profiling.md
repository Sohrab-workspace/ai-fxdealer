# Code profiling

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/profiling

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
        -   [Launch](/en/docs/mt4/metaeditor/open)
        -   [Settings](/en/docs/mt4/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt4/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt4/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt4/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt4/metaeditor/workspace)
        -   [Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt4/metaeditor/development)
            -   [Intelligent management](/en/docs/mt4/metaeditor/intelligent_management)
            -   [Find and replace](/en/docs/mt4/metaeditor/source_code_find)
            -   [Styler](/en/docs/mt4/metaeditor/styler)
            -   [Compilation](/en/docs/mt4/metaeditor/compile)
            -   [MQL5 Cloud Protector: Advanced protection for programs](/en/docs/mt4/metaeditor/mql5_cloud_protector)
            -   [Code debugging](/en/docs/mt4/metaeditor/debug)
            -   [Code profiling](/en/docs/mt4/metaeditor/profiling)
            -   [AI Assistant](/en/docs/mt4/metaeditor/ai_assistant)
            -   [Generating included code](/en/docs/mt4/metaeditor/generate_mqh)
            -   [Working with C++ DLL (integration with MS Visual Studio)](/en/docs/mt4/metaeditor/c_dll)
            -   [Working with Python](/en/docs/mt4/metaeditor/python)
            -   [OpenCL support](/en/docs/mt4/metaeditor/opencl)
        -   [Working with SQL data bases](/en/docs/mt4/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt4/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt4/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt4/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt4/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt4/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt4/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt4/metaeditor/video_guides)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Developing programs](/en/docs/mt4/metaeditor/development)Code profiling

# Code profiling

Profiling means collecting program parameters during its execution. During a profiling, the execution time and the number of calls of individual functions and program code lines are measured. With this tool, the programmer is able to find and optimize the slowest code sections.

Profiling can be performed on the normal chart of the trading platform, as well as using history data in the Strategy Tester. In the first case, a program is launched on a chart that is updated in real time. You can check the program behavior in real conditions. In the second case, the program is launched in the Strategy Tester in the visual mode. The advantage of this method is that you do not need to wait for real data from a trade server or occurrence of certain trading conditions.

Many programs, especially indicators, only perform calculations at the arrival of a new tick (OnTick, OnCalculate). Thus, in order to evaluate performance, you have to wait for new ticks in real time. When profiling using history data, you can immediately provide the required load and test the program performance even on weekends when markets are closed.

## How profiling works

The "Sampling" method is used for profiling. The profiler pauses the operation of an MQL program (~10 000 times per second) and collects statistics on how many times a pause occurred in a particular code part. This includes analyzing call stacks to determine the "contribution" of each function to the total code execution time. At the end of profiling, you receive information about how many times execution was paused and how many times each of the functions appeared on the call stack:

-   Total CPU \[unit,%\] — how many times the function appeared in the call stack.
-   Self CPU \[unit of measurement,%\] — the number of "pauses" which occurred directly within the specified function. This variable is crucial in identifying bottlenecks: according to statistics, pauses occur more often where more processor time is required.

Sampling is a lightweight and accurate method. Unlike other methods, sampling does not make any changes to the analyzed code, which could affect its running speed.

## Profiling settings

By default a program is run on the current open chart for profiling. If profiling is performed on historical data, the current settings of the strategy tester are used. You can use [MetaEditor Options](/en/docs/mt5/metaeditor/settings#debug) to set specify any other chart or to redefine some of the tester settings.

![Debugging](/en/docs/mt5/metaeditor/img/settings_debug.png "Debugging")

The same setting section allows enabling or disabling function [inlining](https://en.wikipedia.org/wiki/Inline_expansion) during compilation. During inlining, the function code is added directly to call its call site, which enables significant program acceleration in come cases. However, this procedure makes the profiling of functions difficult. In order to obtain a report on "pure" functions, you can disable inlining.

This option only disables explicit inlining. The functions which are implicitly generated by the compiler may still be used. Such functions are displayed with the \[inlined\] prefix.

Code optimization mode can be disabled in order to include more details in the profiling report. Code speed without optimization can be several times slower, but this mode provides a wider code coverage. Please note that code bottlenecks can be imprecise without optimization.

The optimization management option is also available under [project settings](/en/docs/mt5/metaeditor/projects#properties).

-   If optimization is disabled in the project, then the new option is ignored and optimization will always be disabled for profiling (including inlining operations).
-   If optimization is enabled in the project, then the new option will be taken into account during profiling compilation.

## Launching profiling [#](profiling#start)

Open a program's source code (MQ4 or MQ5). In the [Debug](/en/docs/mt5/metaeditor/main_menu_debug) menu or [Standard](/en/docs/mt5/metaeditor/toolbar_standard) toolbar, press "![Start profiling on real data](/en/docs/mt5/metaeditor/img/start_profiling_icon.png "Start profiling on real data") Start profiling on real data" or "![Start profiling on history data](/en/docs/mt5/metaeditor/img/start_profiling_history_icon.png "Start profiling on history data") Start profiling on history data".

After that, a special program version for profiling will be compiled automatically. Depending on the selected profiling type, the program will be launched on a normal chart in the trading platform or in the Strategy Tester.

![Launching profiling on a chart in the trading platform](/en/docs/mt5/metaeditor/img/profiling.png "Launching profiling on a chart in the trading platform")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">By default, an application is launched on EURUSD H1. To launch it on another symbol or period, specify them on the <a href="/en/docs/mt5/metaeditor/settings#debug" class="topiclink">Debug</a> tab in the MetaEditor settings.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The non-visual tester mode is always used for profiling on history. The visual mode is practically useless, since resources are consumed by rendering rather than by MQL program calculations.</span></li></ul></td></tr></tbody></table>

After the launch, work with the application for some time to try all its features to the maximum. This is necessary in order for the profiler to measure the execution time of all program's functions and lines.

Then stop profiling: delete program from the chart or click ![Stop Profiling](/en/docs/mt5/metaeditor/img/stop_profiling_icon.png "Stop Profiling") Stop Profiling of the [Debug](/en/docs/mt5/metaeditor/main_menu_debug) menu or in the [Standard](/en/docs/mt5/metaeditor/toolbar_standard) toolbar.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For more accurate profiling results, it is recommended to manually remove the program from the chart instead of using the <img class="help" alt="Stop Profiling" title="Stop Profiling" width="10" height="10" src="/en/docs/mt5/metaeditor/img/stop_profiling_icon.png"> Stop Profiling command.</span></p></td></tr></tbody></table>

## Viewing the profiling results

After profiling is finished, the results are displayed in the [Profiler](/en/docs/mt5/metaeditor/toolbox#profile) tab of the Toolbox window. The results are additionally displayed directly in the code: lines with the appropriate functions are highlighted. The brighter the highlighting, the longer it took to complete the function. This features enables a quick and visual spotting of program bottlenecks.

The profiling report is presented as functions or program lines, for each of which there are two indicators available:

-   Total CPU \[unit,%\] — how many times the function appeared in the call stack.
-   Self CPU \[unit of measurement,%\] — the number of "pauses" which occurred directly within the specified function. This variable is crucial in identifying bottlenecks: according to statistics, pauses occur more often where more processor time is required.

The value is displayed as an absolute quantity and as a percentage of the total quantity.

By default, the list shows large functions located at the top levels. Double-click on the line to switch to smaller functions.

![Profiling results](/en/docs/mt5/metaeditor/img/toolbox_profiler.png "Profiling results")

The profiling report can be viewed in two modes: by calls and by lines. The second method allows exploring code with maximum detail and to identify not only the slowest functions, but also the slowest parts of such functions. Use the context menu to switch between modes.

For convenience, various elements of the MQL language are displayed as icons in the report:

-   ![Custom function](/en/docs/mt5/metaeditor/img/function_icon.png "Custom function")— a custom function.
-   ![System function](/en/docs/mt5/metaeditor/img/function_system_icon.png "System function") — a system function.
-   ![Event handling function](/en/docs/mt5/metaeditor/img/function_event_icon.png "Event handling function")— an event handling function (On\*).
-   ![Class method](/en/docs/mt5/metaeditor/img/class_public_method_icon.png "Class method")— a class method.
-   ![Protected class method](/en/docs/mt5/metaeditor/img/class_method_protected_icon.png "Protected class method")— a protected class method.

In addition to these types of functions, the profiler displays:

-   ![System function](/en/docs/mt5/metaeditor/img/function_system_icon.png "System function")@global\_initializations — data on the initialization of all global variables.
-   ![System function](/en/docs/mt5/metaeditor/img/function_system_icon.png "System function")@global\_deinitializations — data on the deinitialization of all global variables.

To view the line number and path to the file where the function is located, hover the mouse cursor over the appropriate line in the report. To view a function in a file, double-click on it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The profiler displays not all functions but only the ones called during the program operation.</span></p></td></tr></tbody></table>

## Context menu [#](profiling#context)

The following commands are available in the context menu:

-   Open — go to a line or a function in a source code file. The same can be done by double-clicking or pressing Enter.
-   Expand All — expand all collapsed functions.
-   Collapse All — collapse all expanded functions.
-   Functions by Lines — view the profiling results by lines.
-   Functions by Calls — view the profiling results by calls.
-   Export — export profiling results in Open XML (MS Office Excel), HTML (Internet Explorer) or CSV (Text file).
-   Auto Arrange — enable/disable automatic sizing of fields. The same action is performed by pressing A.
-   Grid — show/hide grid to separate fields. The same action is performed by pressing G.

[Code debugging](/en/docs/mt4/metaeditor/debug)

[AI Assistant](/en/docs/mt4/metaeditor/ai_assistant)