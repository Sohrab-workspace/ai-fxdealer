# Developing programs

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/development

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)Developing programs

# Developing programs

MetaEditor features tools for all stages of development: from creating a program template up to its compilation and debugging.

![MetaEditor has everything for developing programs: code writing help, debugging and profiling](/en/docs/mt5/metaeditor/img/development.png "MetaEditor has everything for developing programs: code writing help, debugging and profiling")

## Programming in MetaEditor is convenient

The editor provides plenty of built-in tools that simplify writing a source code:

-   [Auto completion](/en/docs/mt5/metaeditor/intelligent_management#substitute) — when you start entering the first characters of a function, the editor immediately offers suitable options
-   Signature [tips](/en/docs/mt5/metaeditor/intelligent_management#info) are displayed as soon as you start entering a function name
-   [Snippets](/en/docs/mt5/metaeditor/intelligent_management#snippet) for quick insertion of handlers and loops
-   [Styler](/en/docs/mt5/metaeditor/styler) for auto alignment of a source code
-   [Bookmarks](/en/docs/mt5/metaeditor/intelligent_management#bookmarks), [search](/en/docs/mt5/metaeditor/source_code_find) and other means for fast code navigation

## Compilation and protection

[Compilation](/en/docs/mt5/metaeditor/compile) means not only generating an executable file for launching in the trading platform. This is also a formidable protection of your intellectual property. All developed programs are reliably protected against decompilation. In addition, MetaEditor provides an additional file protection via [MQL5 Cloud Protector online service](/en/docs/mt5/metaeditor/mql5_cloud_protector).

## Searching for errors and optimizing programs

MetaEditor allows checking the program operation by steps (string by string) using the [built-in debugger](/en/docs/mt5/metaeditor/debug). You can check the program operation in real conditions by running it on a regular schedule, as well as in the strategy tester where you can quickly pass multiple market situations.

When working on financial markets, the operation speed is important. [The built-in code profiler](/en/docs/mt5/metaeditor/profiling) allows you to find slow functions and optimize a program for maximum speed.

## Additional features

MetaEditor does not limit you: you can write not only in MQL4/MQL5, but also in C++, as well as easily [import functions of third-party DLLs](/en/docs/mt5/metaeditor/c_dll). Your programs can use computational resources of video cards due to support for [OpenCL](https://www.khronos.org/opencl/).

MetaEditor provides access to the extensive [library of source codes](/en/docs/mt5/metaeditor/toolbox#codebase) and [articles](/en/docs/mt5/metaeditor/articles) helping you in mastering algorithmic trading.

[Creating a class](/en/docs/mt4/metaeditor/wizard_class)

[Intelligent management](/en/docs/mt4/metaeditor/intelligent_management)