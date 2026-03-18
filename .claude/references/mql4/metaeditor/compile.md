# Compilation

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/compile

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Developing programs](/en/docs/mt4/metaeditor/development)Compilation

# Compilation

Compilation means converting a source code of an MQL4/MQL5 program into the machine language. The result is an executable program file (\*.EX4 or \*.EX5) that can be launched in a trading platform.

Compilation consists of several stages:

-   Lexical analysis
-   Syntax analysis
-   Semantic analysis
-   Code generation
-   Code optimization

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Any file (*.MQ4, *.MQ5 or *.MQH) can be compiled, but an executable file (*.EX4 or *.EX5) can be obtained only as a result of compiling a <a href="/en/docs/mt5/metaeditor/structure#main_file" class="topiclink">main</a> MQ4/MQ5 program file or <a href="/en/docs/mt5/metaeditor/projects" class="topiclink">project</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">The executable file is created in its own format hiding the original program algorithm.</span></li><li class="p_tableatten"><span class="f_tableatten">Compiled executable EX4/EX5 files can be distributed without source MQ4, MQ5 and MQH files. Debugging is not possible without them. It is also not recommended to distribute executable EX4/EX5 files obtained during a debugging process.</span></li></ul></td></tr></tbody></table>

To obtain an executable program file, open the [main](/en/docs/mt5/metaeditor/structure#main_file) source file or project via [Navigator](/en/docs/mt5/metaeditor/navigator) and click ![Compile](/en/docs/mt5/metaeditor/img/compile_icon.png "Compile") Compile in the [File](/en/docs/mt5/metaeditor/main_menu_file#compile) menu or F7. The compilation process protocol is displayed on the [Errors](/en/docs/mt5/metaeditor/toolbox#errors) tab of the Toolbox window. If compilation has passed with no errors, you can run the obtained program in the trading platform.

![Compilation of the program and displaying the results on the Errors tab](/en/docs/mt5/metaeditor/img/compilation.png "Compilation of the program and displaying the results on the Errors tab")

If there are errors or warnings, they are displayed on the Errors tab.

Compilation errors are marked with ![Error](/en/docs/mt5/metaeditor/img/error_icon.png "Error") both on the Errors tab and in the appropriate piece of code. No executable program file (\*.EX4 or \*.EX5) is created if they occur. To go to a string with an error, double-click on the error or click ![Go to Line](/en/docs/mt5/metaeditor/img/go_to_line_icon.png "Go to Line") Go to Line command in the context menu. The string and the column where an error is detected are displayed in the appropriate columns.

Warnings marked with ![Warning](/en/docs/mt5/metaeditor/img/warning_icon.png "Warning") icon indicate places of potential errors. These are the source code segments that can be misinterpreted (for example, an implicit value type change). You can go to such a code string exactly the same way as in case with errors.

![Information](/en/docs/mt5/metaeditor/img/info_icon.png "Information") icons stand for various info messages, for example, messages about include files the program accessed during compilation.

## Compilation mode [#](compile#mode)

The editor provides two compilation modes: with maximum code optimization and without optimization.

The time required to create an executable file is significantly reduced when optimization is disabled. Use this mode during the active development stage, when you need to quickly check the written code. Then, during the final program compilation, turn on the maximum optimization mode for the best performance.

To switch between the modes, use the "Build" menu or the compilation command menu on the toolbar:

![Control the compilation mode](/en/docs/mt5/metaeditor/img/compilation_mode.png "Control the compilation mode")

The "[Maximum optimization](/en/docs/mt5/metaeditor/projects#properties)" parameter in project settings performs the same function.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">The full description of the compilation errors is provided in the MQL4/MQL5 language help.</span></li><li class="p_tableatten"><span class="f_tableatten">In case of warnings, an executable file is generated. But the warnings should not be ignored since they indicate potential code errors.</span></li><li class="p_tableatten"><span class="f_tableatten">During the compilation, an executable file (*.EX4 or *.EX5) is generated in the same directory as the <a href="/en/docs/mt5/metaeditor/structure#main_file" class="topiclink">main source file</a> of the program (*.MQ4 or *.MQ5) or a <a href="/en/docs/mt5/metaeditor/projects" class="topiclink">project</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">metaeditor.exe can be used as an <a href="/en/docs/mt5/metaeditor/integration_ide" class="topiclink">external compiler in third-party IDEs</a>.</span></li></ul></td></tr></tbody></table>

## Compiling for processors with different architectures [#](compile#architecture)

Modern processors provide a set of advanced instructions which significantly accelerate mathematical calculations: [AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions), [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions), [AVX512](https://en.wikipedia.org/wiki/AVX-512), and [FMA3](https://en.wikipedia.org/wiki/FMA_instruction_set). These instructions are supported in the MQL5 compiler to enable the generation of more efficient and faster codes. The use of such instructions is optional:

-   If you are creating an application for yourself and you are sure that it will run on a processor that supports the desired architecture, you can compile it using advanced instructions. This will provide an increased performance.
-   If you are creating a program for public use or for sale, compile it with the basic instruction set in X64 Regular mode. This will ensure maximum compatibility of the application with user hardware.

To find out which instructions are supported on your processor, use the [CPU-Z free utility](https://www.cpuid.com/softwares/cpu-z.html). After installation, open the 'CPU' section and check the 'Instructions' field:

![Check which instructions your processor supports using CPU-Z](/en/docs/mt5/metaeditor/img/cpu_z.png "Check which instructions your processor supports using CPU-Z")

To select a processor architecture, use the compilation menu. Next, click 'Compile'. You can also specify the architecture in the [MetaEditor settings](/en/docs/mt5/metaeditor/settings#compiler) and in [separate project settings](/en/docs/mt5/metaeditor/projects#properties).

![Select the processor architecture for which the program will be compiled](/en/docs/mt5/metaeditor/img/compilation_architecture.png "Select the processor architecture for which the program will be compiled")

If the application is compiled for an architecture that is not supported by the user's processor, then an attempt to run it will cause the following message to be printed in the platform log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">your&nbsp;CPU&nbsp;architecture&nbsp;does&nbsp;not&nbsp;allow&nbsp;to&nbsp;run&nbsp;the&nbsp;file&nbsp;'&lt;file-name&gt;.ex5':&nbsp;AVX512&nbsp;required,&nbsp;you&nbsp;have&nbsp;AVX2&nbsp;only</span></p></td></tr></tbody></table>

Restrictions:

-   Programs compiled for processors with AVX512 are not yet supported in the [MQL5 Cloud Network](https://www.metatrader5.com/en/terminal/help/algotrading/strategy_optimization#cloud) and in the [built-in VPS](https://www.metatrader5.com/en/terminal/help/virtual_hosting).
-   Only files compiled under X64 Regular can be uploaded to the [Market](https://www.mql5.com/en/articles/385). This is required to ensure maximum application compatibility with user hardware.

[Styler](/en/docs/mt4/metaeditor/styler)

[MQL5 Cloud Protector: Advanced protection for programs](/en/docs/mt4/metaeditor/mql5_cloud_protector)