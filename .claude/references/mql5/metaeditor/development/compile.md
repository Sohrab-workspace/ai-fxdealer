# Compiling

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/development/compile

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

# Compiling

Compilation is the process of translating the source code of a MQL4/MQL5 program into the machine language. This process consists of several stages:

-   Lexical scan;
-   Parsing;
-   Semantic analysis;
-   Code generation;
-   Code optimization.

A successful compilation results in the creation of an executable file (\*EX4 or \*.EX5) of a program that can be started in the client terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:middle; padding:8px; border:none"><ul><li><span class="f_tableatten">Any file (*.MQ4, *.MQ5 or *.MQH) can be compiled, but an executable file (*.EX4 or *.EX5) can be generated only as a result of the compilation of the <a href="/en/docs/mt5/metaeditor/development/development_projects#main_file" class="topiclink">main</a> MQ4 or MQ5 file of a program.</span></li><li><span class="f_tableatten">An executable file is created in its own closed format which hides the source algorithm of a program.</span></li><li><span class="f_tableatten">Compiled executable EX4/EX5 files can be distributed without source MQ4, MQ5 or MQH files. Debugging is impossible without them. It is recommended not to distribute EX4/EX5 files obtained in the result of debugging.</span></li></ul></td></tr></tbody></table>

In order to start compilation, open the source file through the ["Navigator"](/en/docs/mt5/metaeditor/interface/navigator) window and execute the "![Compile](/en/docs/mt5/metaeditor/img/compile_icon.png "Compile") Compile" command in the ["File"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_file#compile) menu or in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#compile) toolbar, or you can press the "F7" key.

The report of the compilation process will be shown in the ["Errors"](/en/docs/mt5/metaeditor/interface/toolbox/toolbox_errors) tab of the "Toolbox" window. If there are no errors in this tab, you can start the program in the client terminal. Error and warning messages are marked by special icons near their descriptions:

![Errors](/en/docs/mt5/metaeditor/img/toolbox_errors.png "Errors")

Compilation errors are marked by ![Error](/en/docs/mt5/metaeditor/img/error_icon.png "Error") icons both in the "Errors" tab and in the code. If such errors occur, an executable program file (\*.EX4 or \*.EX5) won't be generated. In order to move to the line with the error, click twice with the left mouse-button on the line, or execute the "![Go to line](/en/docs/mt5/metaeditor/img/go_to_line_icon.png "Go to line") Go to line" command in the context menu. The number of the line and column, where an error has been found, is shown in corresponding columns.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:middle; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">The full description of compilation errors is given in the Help topics to the MQL4/MQL5 language.</span></p></td></tr></tbody></table>

The appearance of alerts denoted by the ![Warning](/en/docs/mt5/metaeditor/img/warning_icon.png "Warning") icon point to places where errors can occur. I.e. the compiler points to parts of a source code, that could be incorrectly interpreted (for example, implicit change of a value type). You can go to such code lines the same as to lines with errors.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">It is possible that you do not process warnings. But it is not recommended, because they indicate potential places where errors can occur.</span></p></td></tr></tbody></table>

Besides, various informational messages are shown in the journal. They are marked by icons ![Information](/en/docs/mt5/metaeditor/img/info_icon.png "Information"). They can show, for example, include files, to which a program referred during compilation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:middle; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">An executable file (*.EX4 or *.EX5) generated after a successful compilation, is located in the same place, where the <a href="/en/docs/mt5/metaeditor/development/development_projects#main_file" class="topiclink">main file</a> of the program source code (*MQ4. or *.MQ5) is located.</span></p></td></tr></tbody></table>

## Compilation from the Command Line

A MetaEditor executable file can be used as the compiler when working with a source code in external editors. The compiler is started from the command line, specifying the path and name of the file you want to compile:

-   metaeditor.exe /compile:"<full path to the source file>"
-   metaeditor64.exe /compile:"<full path to the source file\>"

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; background-color:#dbe9f9; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts\myscript.mq5"</span></p></td></tr></tbody></table>

### Mass compilation of files in a directory

For mass compilation, set the path to a folder rather than to a file. All source code files in the specified folder will be compiled. Subfolders are not included.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">Re-compilation is not performed if a source file already has the appropriate compiled version.</span></p></td></tr></tbody></table>

The example below displays mass compilation for the \\MQL5\\Scripts folder.

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; background-color:#dbe9f9; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts"</span></p></td></tr></tbody></table>

### Custom MQL5/MQL4 folder with include files

Programs can use include files (\*.mqh) and resource files (\*.bmp, \*.wav, \*.ex4, \*.ex5), which are located outside the working directory of the current platform. (for example, in the \\MQL5 folder of another platform copy on the same computer). Specify the path to this folder using the "/include" key for correct compilation. During compilation, the files will be searched as follows:

-   Include files: \[specified directory\]\\include\\\[path from #include<...>\]
-   Resource files: \[specified directory\]\\\[path from #resource "..."\]

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; background-color:#dbe9f9; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts"&nbsp;/include:"C:\Program&nbsp;Files\TradingPlatform&nbsp;2\MQL5"</span></p></td></tr></tbody></table>

### Compilation log

Specify the additional /log key for more information about the compilation process. In this case, <source file name>.log compilation log file is created in the folder containing the source file.

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; background-color:#dbe9f9; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts\myscript.mq5"&nbsp;/log</span><br><span class="f_CodeExample">Log&nbsp;file:&nbsp;C:\Program&nbsp;Files\TradingPlatform\MQL5\Script\myscript.log</span></p></td></tr></tbody></table>

### Syntax check

To check a program syntax without compilation, launch MetaEditor from the command line with the /s and /log keys (so that results of the check are displayed in the log file).

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; background-color:#dbe9f9; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th></tr></thead><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample">"C:\Program&nbsp;Files\TradingPlatform\metaeditor64.exe"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/compile:"C:\Program&nbsp;Files\TradingPlatform\MQL5\Scripts\myscript.mq5"&nbsp;/s&nbsp;/log</span><br><span class="f_CodeExample">File&nbsp;with&nbsp;the&nbsp;results&nbsp;of&nbsp;the&nbsp;check:&nbsp;C:\Program&nbsp;Files\TradingPlatform\MQL5\Script\myscript.log</span></p></td></tr></tbody></table>