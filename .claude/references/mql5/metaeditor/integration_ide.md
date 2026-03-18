# Integration with other IDEs

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/integration_ide

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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)Integration with other IDEs

# Integration with other IDEs

MetaEditor allows you to write code not only in MQL4 and MQL5. You can also edit and compile the C++ and Python source code. In addition, you can use MetaEditor as an [external compiler in other development environments](/en/docs/mt5/metaeditor/integration_ide#compiler).

## Editing C++ code and DLL compilation

When developing trading programs on MQL4/MQL5, you can easily use third-party C++ DLLs. You can edit C++ source code files (CPP and H) similarly to MQ4, MQ5 and MQH ones. These files in DLL can also be compiled directly from the editor. Microsoft Visual Studio installed on user's PC can be used for that. To compile, open the C++ file and press F7 (Compile command).

![Working with DLLs on C++](/en/docs/mt5/metaeditor/img/compile_dll.png "Working with DLLs on C++")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">MS Visual Studio compiler installed on a user's PC is used for compiling C++ source codes. MS Visual Studio 2008 and higher (including Express and Community versions) are supported.</span></li><li class="p_tableatten"><span class="f_tableatten">MS Visual Studio version (32 or 64-bit) should match MetaEditor version.</span></li></ul></td></tr></tbody></table>

MetaEditor also provides the ability to easily add exported DLL functions to MQL4/MQL5 file. Simply drag a DLL file from the [Navigator](/en/docs/mt5/metaeditor/navigator) window to the open MQ4, MQ5 or MQH file.

![Importing functions from DLL](/en/docs/mt5/metaeditor/img/dll_import.png "Importing functions from DLL")

## Using Python scripts

The are a lot of machine learning, process automation, as well as data analysis and visualization libraries for the Python language. The advanced language possibilities can now be applied in the platform through the [Python integration module](https://www.mql5.com/en/docs/python_metatrader5).

-   Exchange data can be easily and quickly obtained from the trading platform and then analyzed using Python tools: hundreds of thousands of financial symbol ticks can be requested with one command
-   Obtain account trading state and trading history to calculate statistics
-   Perform trading operations following your own algorithm

Python scripts [run directly on platform charts](https://www.metatrader5.com/en/terminal/help/algotrading/trade_robots_indicators#python), similarly to regular MQL5 programs.

MetaEditor features special integrated [functions for Python development](/en/docs/mt5/metaeditor/python): a wizard for creating blank scripts, the ability to run directly from the editor, output of messages and errors to the common log, and so on.

![Running a script in the editor](/en/docs/mt5/metaeditor/img/python_compile.png "Running a script in the editor")

## Compiling MQL programs in other development environments [#](integration_ide#compiler)

A MetaEditor executable file can be used as the compiler when working with a source code in external editors. The compiler is started from the command line, specifying the path and name of the file you want to compile:

-   metaeditor.exe /compile:"<full path to the source file>"
-   metaeditor64.exe /compile:"<full path to the source file\>"

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts\myscript.mq5"</span></p></td></tr></tbody></table>

### Mass compilation of files in a directory

For mass compilation, set the path to a folder rather than to a file. All source code files in the specified folder will be compiled. Subfolders are not included.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Re-compilation is not performed if a source file already has the appropriate compiled version.</span></p></td></tr></tbody></table>

The example below displays mass compilation for the \\MQL5\\Scripts folder

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts"</span></p></td></tr></tbody></table>

### Custom MQL5/MQL4 folder with include files

Programs can use include files (\*.mqh) and resource files (\*.bmp, \*.wav, \*.ex4, \*.ex5), which are located outside the working directory of the current platform (for example, in the \\MQL5 folder of another platform copy on the same computer). Specify the path to this folder using the "/include" key for correct compilation. During compilation, the files will be searched as follows:

-   Include files: \[specified directory\]\\include\\\[path from #include<...>\]
-   Resource files: \[specified directory\]\\\[path from #resource "..."\]

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts"&nbsp;/include:"C:\Program&nbsp;Files\TradingPlatform&nbsp;2\MQL5"</span></p></td></tr></tbody></table>

### Compilation log

Specify the additional /log key for more information about the compilation process. In this case, <source file name>.log compilation log file is created in the folder containing the source file.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts\myscript.mq5"&nbsp;/log</span><br><span class="f_CodeExample">Log&nbsp;file:&nbsp;C:\Program&nbsp;Files\TradingPlatform\MQL5\Script\myscript.log</span></p></td></tr></tbody></table>

### Syntax check

To check a program syntax without compilation, launch MetaEditor from the command line with the /s and /log keys (so that results of the check are displayed in the log file).

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts\myscript.mq5"&nbsp;/s&nbsp;/log</span><br><span class="f_CodeExample">File&nbsp;with&nbsp;the&nbsp;results&nbsp;of&nbsp;the&nbsp;check:&nbsp;C:\Program&nbsp;Files\TradingPlatform\MQL5\Script\myscript.log</span></p></td></tr></tbody></table>

[Settings](/en/docs/mt5/metaeditor/settings)

[Main menu](/en/docs/mt5/metaeditor/main_menu)