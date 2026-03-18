# Debugging

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/development/debug

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

# Debugging

It's hard to eliminate errors when writing considerably complicated programs. MetaEditor offers you the built-in debugger to help you solve this problem. The debugging of applications consists in the possibility of the step-by-step program execution, calculating local variables, setting at breakpoints in a preset location.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:middle; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">In order to start debugging, the window of the <a href="/en/docs/mt5/metaeditor/development/development_projects#main_file" class="topiclink">main file</a> of the project must be active (*.MQ4 or *.MQ5). In order to debug include files (*.MQH), it's necessary to start the debugging of the file, into which they are included.</span></p></td></tr></tbody></table>

Further the debugging process is described in details:

-   [Presetting](/en/docs/mt5/metaeditor/development/debug#settings)
-   [Breakpoints](/en/docs/mt5/metaeditor/development/debug#breakpoint)
-   [Start of Debugging](/en/docs/mt5/metaeditor/development/debug#start)
-   [Watching Expressions](/en/docs/mt5/metaeditor/development/debug#watch)
-   [Viewing Stack of Calls](/en/docs/mt5/metaeditor/development/debug#stack)
-   [Step-By-Step Debugging](/en/docs/mt5/metaeditor/development/debug#step)
-   [Breaking, Continuing, Stopping Debugging](/en/docs/mt5/metaeditor/development/debug#stop)
-   [Debugging on History Data](/en/docs/mt5/metaeditor/development/debug#history)

## Presetting

Before you start the program debugging, it's necessary to check its parameters in the ["Debugging"](/en/docs/mt5/metaeditor/settings/settings_debug) tab of the MetaEditor options window. In this window you can specify a symbol and a chart period, in which the debugging of applications will be performed. Such a chart will be temporarily created each time when debugging is started, and it will be deleted after the debugging completion.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">The "debug.tpl" template located in the /profiles/templates folder of the client terminal is applied to a chart created for debugging.</span></p></td></tr></tbody></table>

## Breakpoints

A breakpoint is a command that triggers when the program execution is passed to an indicated line and stops the program in this location. Breakpoints allow analyzing the program behavior in a selected location: viewing values of variables, stack of functions. After that the debugging process can be continued or completed.

Before you start debugging, place such breakpoints in necessary code positions. To do this, click twice by the left mouse-button on the gray field near the left border of the code line. You can also place the mouse cursor in the necessary line and execute the "![Toggle Breakpoint](/en/docs/mt5/metaeditor/img/breakpoint_icon.png "Toggle Breakpoint") Toggle Breakpoint" command of the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug#breakpoint) menu or in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#breakpoint) toolbar, or you can press the "F9" key. Breakpoints are disabled the same way.

![Breakpoint](/en/docs/mt5/metaeditor/img/debug_breakpoint.png "Breakpoint")

If you need to jump to the breakpoint, at which program execution stopped, double click on the function in the call stack viewing window. Also, using the window context menu, you can open the list of all breakpoints in the currently debugged program:

![Go to breakpoint](/en/docs/mt5/metaeditor/img/breakpoint_goto.png "Go to breakpoint")

You can jump to any breakpoint by double-clicking on it.

## Start of Debugging

To start the debugging process, it's necessary to open a program file, selecting it in the ["Navigator"](/en/docs/mt5/metaeditor/interface/navigator) window. After that execute the "![Start Debugging](/en/docs/mt5/metaeditor/img/start_debug_icon.png "Start Debugging") Start Debugging" command in the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug#start) menu or in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar, or press the "F5" key. After that the program to debug will be attached to a [special chart](/en/docs/mt5/metaeditor/development/debug#settings) in the trading terminal. As soon as the program execution reaches the line with the first breakpoint, it will be stopped. The point where the execution is stopped will be changed into ![Triggered Breakpoint](/en/docs/mt5/metaeditor/img/breakpoint_triggered_icon.png "Triggered Breakpoint"). Besides, the ["Debugging"](/en/docs/mt5/metaeditor/interface/toolbox/toolbox_debug) tab will appear in the "Toolbox" window. In its left part the [stack of function call](/en/docs/mt5/metaeditor/development/debug#stack) will be shown.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">The debugging of applications is performed in real conditions using the price data received from server. A special temporary chart that is created for debugging doesn't have any differences from the ordinary charts opened in the client terminal.</span></p></td></tr></tbody></table>

## Watching Expressions

In the process of debugging you can watch values of different expressions (variables) obtained at this program execution stage. For these purposes the right part of the ["Debug"](/en/docs/mt5/metaeditor/interface/toolbox/toolbox_debug) tab in the "Toolbox" window is used. An expression can be added in the following ways:

-   During debugging, call a context menu on a necessary expression and select the "![Add Watch](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add Watch") Add Watch" command or press the "Shift+F9" key combination;
-   In the right part of the "Debug" tab in the "Toolbox" window call the context menu and execute the "![Add](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add") Add" command or press the "Insert" key. After that a new line will appear, and in its "Expression" field your should enter the name of a watched parameter.
-   In order to change the name of a watched expression, it's necessary to click twice by the left mouse button on its name or select it and execute the "Edit" command of the context menu or press "F2".

![Viewing stack and expressions](/en/docs/mt5/metaeditor/img/debug_watch.png "Viewing stack and expressions")

In the expressions watching window, you can conduct simple mathematical calculations (addition, subtraction, multiplication and division), as well as view values in certain array points. For example, you can indicate a record like A\[3\]\[4\], where A is the name of an array, 3 and 4 are positions in its dimensions. When adding objects to observed expressions, the list of its members can be shown by adding a point at their end or pressing "Ctrl+Space":

![Inserting object members](/en/docs/mt5/metaeditor/img/debug_watch_autocomplete.png "Inserting object members")

By default, integer numbers are displayed in the watch window in the decimal format. To display them in the binary or hexadecimal format, specify a comma separated modifier b or x respectively in the Expression field:

![Watching values in binary or hexadecimal format](/en/docs/mt5/metaeditor/img/debug_watch_binary_hex.png "Watching values in binary or hexadecimal format")

## Viewing Stack of Calls

The left part of the ["Debug"](/en/docs/mt5/metaeditor/interface/toolbox/toolbox_debug) tab in the "Toolbox" window allows viewing stacks. Here the following components are shown:

-   Name of a file, from which a function is called;
-   Function name;
-   Number of a line in the file, where this function is called.

When the debugging process is started, only the address of a called function, at which a breakpoint has triggered, is shown in this window.

Step-By-Step Debugging

For the step-by-step debugging with the viewing of calls stack, commands of the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug) menu or of the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar are used:

-   ![Step Into](/en/docs/mt5/metaeditor/img/step_into_icon.png "Step Into") Step Into — go one step of the program execution, entering called functions. The same action can be performed by pressing the "F11" key.
-   ![Step Over](/en/docs/mt5/metaeditor/img/step_over_icon.png "Step Over") Step Over — go one step of the program execution, not entering called functions. The same action can be performed by pressing "F10".
-   ![Step Out](/en/docs/mt5/metaeditor/img/step_out_icon.png "Step Out") Step Out — go to the execution of a program step one level higher. The same action can be performed pressing "Shift+F11".

For executing the above commands, the debugging process must be stopped. This is done automatically when program execution reaches a breakpoint. Also debugging can be suspended manually by pressing "![Break Debugging](/en/docs/mt5/metaeditor/img/break_debug_icon.png "Break Debugging") Break Debugging" in the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug#break) menu or in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar, or by pressing the "Break" key.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">When an application is at a break point, occurring of events continues. At that all of them are placed into a queue, and their handling by Expert Advisor will be continued after exiting the code of the current event handle.</span></p></td></tr></tbody></table>

## Breaking, Continuing, Stopping Debugging

The breaking of the program debugging process is done automatically, when it reaches a line with a breakpoint. However, the debugging process can be managed manually:

-   Breaking  
    The execution of program while debugging it can be broken manually using the "![Break Debugging](/en/docs/mt5/metaeditor/img/break_debug_icon.png "Break Debugging") Break Debugging" command in the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug#break) menu or in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar, or pressing the "Break" key. After that you can executed the step-by-step debugging.
-   Continuing  
    In order to continue the running of program in the debugging mode after it is broken automatically or manually, execute the "![Continue Debugging](/en/docs/mt5/metaeditor/img/start_debug_icon.png "Continue Debugging") Continue Debugging" command in the ["Debug"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug#start) menu or in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar of the same name, or press "F5".
-   Stopping  
    In order to stop debugging, it's necessary to execute the "![Stop Debugging](/en/docs/mt5/metaeditor/img/stop_debug_icon.png "Stop Debugging") Stop Debugging" command in the ["Debug menu"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug#stop) or in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar, or press "Shift+F5". After the program is stopped, it is removed from the [special chart](/en/docs/mt5/metaeditor/development/debug#settings), to which it was attached for debugging, and the chart is closed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:middle; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">Debugging is impossible without the source MQ4, MQ5 and MQH files. It is also recommended not to distribute EX4/EX5 files obtained in the result of debugging.</span></p></td></tr></tbody></table>

## Debugging on History Data

Trading robots and technical indicators can be debugged not only on real time updated price data, but also using history prices. A program operation can be tested on a required history interval. Debugging runs in the Strategy Tester in the visual testing mode.  A chart for debugging is based on a sequence of ticks emulated in the tester.

To start debugging on history data, configure testing parameters in the [MetaEditor settings](/en/docs/mt5/metaeditor/settings/settings_debug).

![Setup of Debugging on history](/en/docs/mt5/metaeditor/img/debug_history_settings.png "Setup of Debugging on history")

Set breakpoints in the code program and start testing on history data.

![Starting Debugging on history](/en/docs/mt5/metaeditor/img/debug_history_run.png "Starting Debugging on history")

This will initiate visual testing and the debugging process.

![Debugging on history](/en/docs/mt5/metaeditor/img/debug_history_running.png "Debugging on history")