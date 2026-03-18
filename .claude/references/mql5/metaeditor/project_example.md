# Example of developing a program

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/project_example

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
        -   [Launch](/en/docs/mt5/metaeditor/open)
        -   [Settings](/en/docs/mt5/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt5/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt5/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt5/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt5/metaeditor/workspace)
        -   [Projects and MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt5/metaeditor/development)
        -   [Working with SQL data bases](/en/docs/mt5/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt5/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt5/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt5/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt5/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt5/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt5/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt5/metaeditor/video_guides)
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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)Example of developing a program

# Example of developing a program

Thanks to [MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard), you only need a few minutes to create a simple program. The current example will display "Hello World" entry in the platform log.

Launch MQL4/MQL5 Wizard using the ![New](/en/docs/mt5/metaeditor/img/new_icon.png "New") New command in the [File](/en/docs/mt5/metaeditor/main_menu_file) menu or in the [Standard](/en/docs/mt5/metaeditor/toolbar_standard) toolbar. Set Script as a program type at the first step.

![Creating a script in the Wizard](/en/docs/mt5/metaeditor/img/example_wizard_script.png "Creating a script in the Wizard")

Next, set the script name. If you want to create the script file in a separate subfolder rather than in the Scripts root directory, add the folder name in the Name field. For example, "Scripts\\Script Example\\Script Example". After clicking Finish, the "Script Example.mq5" script file is generated in the "Scripts\\Script Example\\" directory.

Add the "Print("Hello World!);" string to the generated file and save the changes (Ctrl+S). Perform compilation to turn the initial file into the one that can be launched in the trading platform. Click ![Compile](/en/docs/mt5/metaeditor/img/compile_icon.png "Compile") Compile in the [File](/en/docs/mt5/metaeditor/main_menu_file#save) menu or in the [toolbar](/en/docs/mt5/metaeditor/toolbar_standard). The compilation result is displayed in the [Errors](/en/docs/mt5/metaeditor/toolbox#errors) tab of the Toolbox window:

![Script compilation](/en/docs/mt5/metaeditor/img/example_compile.png "Script compilation")

As a result of compilation, ScriptExample.ex5 executable script file is created in the same directory where the source file is located.

The [debugging mode](/en/docs/mt5/metaeditor/debug) allows you to check the execution of a program in steps. If necessary, set [breakpoints](/en/docs/mt5/metaeditor/debug#breakpoint)  — strings/functions, at which the program execution is paused. To do this, double-click the left mouse button to the left of the required line. Then click "![Start debugging](/en/docs/mt5/metaeditor/img/start_debug_icon.png "Start debugging") Start debugging" in the [Debug](/en/docs/mt5/metaeditor/main_menu_debug#start) menu or on the [toolbar](/en/docs/mt5/metaeditor/toolbar_standard).

![Launching debugging](/en/docs/mt5/metaeditor/img/example_start_debug.png "Launching debugging")

The script is launched on a temporary chart in the trading platform, while the script operation result — "Hello World!" entry appears in the experts log:

![Debugging the script](/en/docs/mt5/metaeditor/img/example_debug.png "Debugging the script")

To finish debugging, press "![Stop debugging](/en/docs/mt5/metaeditor/img/stop_debug_icon.png "Stop debugging") Stop debugging".

After completing all the steps, you can run the script in the trading platform. To open it, click ![Trading terminal](/en/docs/mt5/metaeditor/img/terminal_icon.png "Trading terminal") Trading Terminal in the [Tools](/en/docs/mt5/metaeditor/main_menu_tools) menu or F4.

[Working with machine learning models](/en/docs/mt5/metaeditor/machine_learning)

[MetaEditor environment folders](/en/docs/mt5/metaeditor/structure)