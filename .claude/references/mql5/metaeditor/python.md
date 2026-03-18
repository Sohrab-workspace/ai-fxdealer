# Working with Python

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/python

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
            -   [Intelligent management](/en/docs/mt5/metaeditor/intelligent_management)
            -   [Find and replace](/en/docs/mt5/metaeditor/source_code_find)
            -   [Styler](/en/docs/mt5/metaeditor/styler)
            -   [Compilation](/en/docs/mt5/metaeditor/compile)
            -   [MQL5 Cloud Protector: Advanced protection for programs](/en/docs/mt5/metaeditor/mql5_cloud_protector)
            -   [Code debugging](/en/docs/mt5/metaeditor/debug)
            -   [Code profiling](/en/docs/mt5/metaeditor/profiling)
            -   [AI Assistant](/en/docs/mt5/metaeditor/ai_assistant)
            -   [Generating included code](/en/docs/mt5/metaeditor/generate_mqh)
            -   [Working with C++ DLL (integration with MS Visual Studio)](/en/docs/mt5/metaeditor/c_dll)
            -   [Working with Python](/en/docs/mt5/metaeditor/python)
            -   [OpenCL support](/en/docs/mt5/metaeditor/opencl)
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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[Developing programs](/en/docs/mt5/metaeditor/development)Working with Python

# Working with Python

The are a lot of machine learning, process automation, as well as data analysis and visualization libraries for the Python language. The advanced language possibilities can now be applied in the platform through the [Python integration module](https://www.mql5.com/en/docs/python_metatrader5).

-   Exchange data can be easily and quickly obtained from the trading platform and then analyzed using Python tools: hundreds of thousands of financial symbol ticks can be requested with one command
-   Obtain account trading state and trading history to calculate statistics
-   Perform trading operations following your own algorithm

Python scripts [run directly on platform charts](https://www.metatrader5.com/en/terminal/help/algotrading/trade_robots_indicators#python), similarly to regular MQL5 programs.

MetaEditor features special integrated functions for Python development: a wizard for creating blank scripts, the ability to run directly from the editor, output of messages and errors to the common log, and so on.

## Setup

To get started, specify the path to the Python executable in [MetaEditor settings](/en/docs/mt5/metaeditor/settings):

![Specify the path to the Python executable](/en/docs/mt5/metaeditor/img/python_settings.png "Specify the path to the Python executable")

If Python is not installed on your computer, click Install to download the installation file.

## Creating a script

Open [MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard) and select "Python Script". Next, specify the script name and select library dependencies to be included in the code.

![Creating a Python script](/en/docs/mt5/metaeditor/img/python_wizard.png "Creating a Python script")

Scripts can be created using the MQL5 Wizard, while you can instantly add required library dependencies in the code.

## Running the script

To run a script, press "Compile" (F7). This will open a trading platform, and the script will be launched on the current chart. Messages from the Python console (stdout, stderr) will be displayed under the [Errors](/en/docs/mt5/metaeditor/toolbox#errors) section.

![Running a script in the editor](/en/docs/mt5/metaeditor/img/python_compile.png "Running a script in the editor")

To enable the use of the MetaTrader 5 library, install it using the following command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">pip</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">install</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MetaTrader5</span></p></td></tr></tbody></table>

For Python integration details please read the relevant [documentation](https://www.mql5.com/en/docs/python_metatrader5).

[Working with C++ DLL (integration with MS Visual Studio)](/en/docs/mt5/metaeditor/c_dll)

[OpenCL support](/en/docs/mt5/metaeditor/opencl)