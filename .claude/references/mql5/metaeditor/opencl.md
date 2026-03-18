# OpenCL support

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/opencl

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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[Developing programs](/en/docs/mt5/metaeditor/development)OpenCL support

# OpenCL support

MQL5 language supports [OpenCL](https://www.khronos.org/opencl/). This is an open standard for the development of programs related to parallel computing on graphics processors and CPUs.

Modern video cards contain hundreds of small specialized processors that can simultaneously perform simple mathematical operations with incoming data streams. OpenCL organizes parallel computing and provides greater speed for a certain class of tasks.

Support for OpenCL allows you to use parallel computing on video cards in your trading programs.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To perform calculations, a video card with support for standard OpenCL 1.1 or above is required. Calculations can also be performed on Intel CPUs. They support OpenCL emulation mode.</span></p></td></tr></tbody></table>

Materials on developing MQL5 programs with OpenCL:

-   [Working with OpenCL (MQL5 Reference)](https://www.mql5.com/en/docs/opencl)
-   [How to install and use OpenCL for calculations](https://www.mql5.com/en/articles/690)
-   [OpenCL: The bridge to parallel worlds](https://www.mql5.com/en/articles/405)
-   [OpenCL: From naive towards more insightful programming](https://www.mql5.com/en/articles/407)

[Working with Python](/en/docs/mt5/metaeditor/python)

[Working with SQL data bases](/en/docs/mt5/metaeditor/database)