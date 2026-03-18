# Code debugging

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/debug

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Developing programs](/en/docs/mt4/metaeditor/development)Code debugging

# Code debugging

MetaEditor has a built-in debugger allowing you to check a program execution step by step (by individual functions). Place breakpoints in the code. These are the places where the program execution should be paused. Then launch the program on a regular chart or the [strategy tester](/en/docs/mt5/metaeditor/debug#history). As soon as the program reaches a breakpoint, it is paused. This allows you to see the values of calculated variables and then continue program execution step by step checking the execution algorithm.

-   [Presetting](/en/docs/mt5/metaeditor/debug#settings)
-   [Breakpoints](/en/docs/mt5/metaeditor/debug#breakpoint)
-   [Launching debugging](/en/docs/mt5/metaeditor/debug#start)
-   [Observed expressions](/en/docs/mt5/metaeditor/debug#watch)
-   [Viewing a call stack](/en/docs/mt5/metaeditor/debug#stack)
-   [Step-by-step debugging](/en/docs/mt5/metaeditor/debug#step)
-   [Pausing, resuming and ending debugging](/en/docs/mt5/metaeditor/debug#stop)
-   [Debugging on history](/en/docs/mt5/metaeditor/debug#history)

## Presetting [#](debug#settings)

Before debugging, set its general parameters in [MetaEditor settings](/en/docs/mt5/metaeditor/settings#debug). You can specify a symbol and a period of chart, on which the debugging of applications is to occur. Such a chart is temporarily created every time you start debugging and removed immediately after its completion.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">debug.tpl template located in the /profiles/templates folder of the trading platform is applied to a debugging chart.</span></p></td></tr></tbody></table>

## Breakpoints [#](debug#breakpoint)

A breakpoint is a command triggered when a program execution reaches a specified string. The command stops the execution at that string. Breakpoints allow examining a program behavior in a specified code area: view the variable values and the stack of functions. In the future, the debugging process can be resumed or terminated.

Before launching a debugging, set at least one breakpoint in the program code. To do this, double-click on the gray field to the left of the code line. You can also place a cursor on the line and click ![Toggle Breakpoint](/en/docs/mt5/metaeditor/img/breakpoint_icon.png "Toggle Breakpoint") Toggle Breakpoint in the [Debug](/en/docs/mt5/metaeditor/main_menu_debug#breakpoint) menu or F9. Breakpoints are disabled the same way.

![Enabled breakpoint](/en/docs/mt5/metaeditor/img/debug_breakpoint.png "Enabled breakpoint")

If you need to jump to the point, at which program execution stopped, double click on the function in the call stack viewing window. Also, using the window context menu, you can open the list of all breakpoints in the currently debugged program:

![Going to breakpoint](/en/docs/mt5/metaeditor/img/breakpoint_goto.png "Going to breakpoint")

You can jump to any breakpoint by double-clicking on it.

## Launching debugging [#](debug#start)

To run debugging, open the [main program file](/en/docs/mt5/metaeditor/structure#main_file) or a [project](/en/docs/mt5/metaeditor/projects). Debugging can be performed in two modes:

-   On real data. Debugging is launched by the ![Start/Resume debugging on real data](/en/docs/mt5/metaeditor/img/start_debug_icon.png "Start/Resume debugging on real data") Start on Real Data command in the [Debug](/en/docs/mt5/metaeditor/main_menu_debug#start) menu or F5. In this mode, the debugged program runs on a [special chart](/en/docs/mt5/metaeditor/debug#settings) in the trading platform. Debugging is performed in real conditions using price data arriving from the server.
-   On history. Debugging is launched by the ![Start on History Data](/en/docs/mt5/metaeditor/img/start_debug_history_icon.png "Start on History Data") Start on History Data command in the [Debug](/en/docs/mt5/metaeditor/main_menu_debug#start) menu or Ctrl+F5. A program in this mode is launched in the Strategy Tester. Use it to test program performance in any desired history interval, without waiting for specific market conditions. The non-visual testing mode is used by default to avoid extra resource usage while rendering graphic elements. The visual mode can be enabled in [MetaEditor settings](/en/docs/mt5/metaeditor/settings#debug).

As soon as the program execution in debugging mode reaches a breakpoint, it is paused. The line the execution is paused on is marked with the ![Triggered breakpoint](/en/docs/mt5/metaeditor/img/breakpoint_triggered_icon.png "Triggered breakpoint") icon. The [Debug](/en/docs/mt5/metaeditor/toolbox#debug) tab also appears in the Toolbox window. Its left part displays the function [call stack](/en/docs/mt5/metaeditor/debug#stack).

![Breakpoint triggering after launching debugging](/en/docs/mt5/metaeditor/img/debug_start.png "Breakpoint triggering after launching debugging")

## Observed expressions [#](debug#watch)

During debugging, the values of various expressions (variables) can be tracked on the current program execution step. The right part of the [Debug](/en/docs/mt5/metaeditor/toolbox#debug) tab of the Toolbox window displays the appropriate results. To track expression values, add it to the observed ones:

-   During the debugging, place the cursor on an expression in the source code and click ![Add Watch](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add Watch") Add Watch in the context menu.
-   Click ![Add](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add") Add in the context menu of the right part of the Debug tab. Enter the expression name in the newly appeared line.
-   To change the name of the tracked expression, double-click on it.

![Viewing the stack and expression values](/en/docs/mt5/metaeditor/img/debug_watch.png "Viewing the stack and expression values")

You can also enable automatic display of local variables in the debugger watchlist. The display can be enabled by the "Local" command of the context menu. As the debugger operation proceeds through the code, variables from the current scope are automatically displayed in the list.

In the expression observation window, you can perform simple mathematical calculations (addition, subtraction, multiplication and division), as well as view values ​​at specific array points, for example, by specifying A\[3\]\[4\] entry, where A is an array name, while 3 and 4 are positions in its dimensions. When adding objects to observed expressions, we can view the list of their members by specifying a full stop in the end or clicking Ctrl+Space:

![Inserting object members](/en/docs/mt5/metaeditor/img/debug_watch_autocomplete.png "Inserting object members")

To view the contents of an array or object, double-click on it in the observation window.

By default, integers are displayed in the observation window in decimal form. To display the value in binary or hexadecimal form, specify the comma-separated b or x modifier accordingly in the Expression field.

![Viewing expressions in binary and hexadecimal form](/en/docs/mt5/metaeditor/img/debug_watch_binary_hex.png "Viewing expressions in binary and hexadecimal form")

## Viewing a call stack [#](debug#stack)

Data for returning control from sub-programs (nested functions) to the program (main event handler OnInit, OnTick, etc.) is specified in the call stack. The stack allows you to track the entire sequence of an [event occurrence in the trading platform](https://www.mql5.com/en/docs/runtime/event_fire) up to calling a specific function.

The following data is displayed for each function:

-   File name the function is called from.
-   Function name.
-   Line number in the file where the function is called.

Step-by-step debugging

[Debug](/en/docs/mt5/metaeditor/main_menu_debug) menu or [Standard](/en/docs/mt5/metaeditor/toolbar_standard) toolbar commands are used for step-by-step debugging with the ability to view the call stack:

-   ![Step Into](/en/docs/mt5/metaeditor/img/step_into_icon.png "Step Into") Step Into — move one step of program execution accessing the called functions. The same action is performed by pressing F11.
-   ![Step Over](/en/docs/mt5/metaeditor/img/step_over_icon.png "Step Over") Step Over — move one step of program execution without accessing the called functions. The same action is performed by pressing F10.
-   ![Step Out](/en/docs/mt5/metaeditor/img/step_out_icon.png "Step Out") Step Out — execute a single step of a program one level higher. The same action is performed by pressing Shift+F11.

The step-by-step debugging commands can be used only after the program is paused in debug mode:

-   After a breakpoint is triggered.
-   After a program is paused manually by ![Pause](/en/docs/mt5/metaeditor/img/break_debug_icon.png "Pause") Pause command in the [Debug menu](/en/docs/mt5/metaeditor/main_menu_debug#break) or pressing Break.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Events continue occurring <a href="https://www.mql5.com/en/docs/runtime/event_fire" target="_blank" class="weblink" title="Events in the trading platform">in the trading platform</a> even if the program is at a breakpoint. All occurred events are placed in a queue and their processing using an expert is continued after the current event handler exits the code.</span></p></td></tr></tbody></table>

## Pausing, resuming and ending debugging [#](debug#stop)

Program is stopped automatically during debugging as soon as the execution reaches a string with a breakpoint installed. Debugging can also be managed manually:

-   Pausing execution  
    Program execution during debugging can be paused manually by using ![Pause](/en/docs/mt5/metaeditor/img/break_debug_icon.png "Pause") Pause command in the [Debug menu](/en/docs/mt5/metaeditor/main_menu_debug#break) or pressing Break. After pausing, you can apply step-by-step debugging commands.
-   Resuming execution  
    To resume the program execution after a pause, click ![Resume](/en/docs/mt5/metaeditor/img/start_debug_icon.png "Resume") Resume in the [Debug menu](/en/docs/mt5/metaeditor/main_menu_debug#start) or press F5.
-   Completing debugging  
    To stop debugging, click ![Stop](/en/docs/mt5/metaeditor/img/stop_debug_icon.png "Stop") Stop in the [Debug menu](/en/docs/mt5/metaeditor/main_menu_debug#stop) or press Shift+F5. The program is removed from a [special chart](/en/docs/mt5/metaeditor/debug#settings), on which it was launched for debugging, while the chart itself is closed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Debugging is impossible without source MQ4, MQ5 and MQH files.</span></li><li class="p_tableatten"><span class="f_tableatten">It is not recommended to distribute executable EX4/EX5 files obtained during a debugging process.</span></li></ul></td></tr></tbody></table>

## Debugging on history [#](debug#history)

Apart from real-time price data, debugging of trading robots and technical indicators can be performed on history as well. Any program can be tested on required history data without waiting for certain trading events in real time.

Debugging on history data runs in the visual testing mode in the Strategy Tester. An application is executed on a chart based on an emulated sequence of ticks in the tester or accumulated history ticks (received from a broker).

To start debugging on history, set testing parameters in [MetaEditor settings](/en/docs/mt5/metaeditor/settings#debug).

![Configuring debugging on history](/en/docs/mt5/metaeditor/img/debug_history_settings.png "Configuring debugging on history")

Set the breakpoints in the code, and then start the debugging using historical prices.

![Launching debugging on history](/en/docs/mt5/metaeditor/img/debug_history_run.png "Launching debugging on history")

This will initiate visual testing and the debugging process.

![Debugging on history](/en/docs/mt5/metaeditor/img/debug_history_running.png "Debugging on history")

[MQL5 Cloud Protector: Advanced protection for programs](/en/docs/mt4/metaeditor/mql5_cloud_protector)

[Code profiling](/en/docs/mt4/metaeditor/profiling)