# Generating include files

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/generate_mqh

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Developing programs](/en/docs/mt4/metaeditor/development)Generating included code

# Generating include files

MetaEditor provides the function for generating include files (\*.mqh) from exported functions of the current file. It makes it easy to give other users access to your functions without disclosing their source code. To do this, simply provide a generated mqh file and a closed EX4/EX5 file where the functions are implemented.

## Generation process

Open an MQ4/MQ5 file and click ![Generate mqh file](/en/docs/mt5/metaeditor/img/generate_mqh_icon.png "Generate mqh file") Generate Include File in the [Tools](/en/docs/mt5/metaeditor/main_menu_tools) menu. An mqh file is generated the following way:

-   The current open file contains all functions with the [export](https://www.mql5.com/en/docs/basis/function/export) post-modifier.
-   The include file with the [#import](https://www.mql5.com/en/docs/basis/preprosessor/import) directive and the description of detected functions is generated.
-   If no export function found, an appropriate message is displayed.
-   If a source file is located in the /Libraries folder, the module name in the #import directive has a relative path from the /Libraries directory. If a file is located in another directory, only a name of an EX4/EX5 file is substituted to #import.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the current file is an include one (*.mqh), generation command does not work.</span></p></td></tr></tbody></table>

## Generation path

The directory the mqh file is created in depends on the source file location:

-   If the current file is located in the /Libraries directory or in one of its sub-directories, the include file is generated directly in the /Include folder.
-   If a source file is located in some other directory, an include file is generated at the same location.

[AI Assistant](/en/docs/mt4/metaeditor/ai_assistant)

[Working with C++ DLL (integration with MS Visual Studio)](/en/docs/mt4/metaeditor/c_dll)