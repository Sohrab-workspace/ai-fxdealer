# Creating a Simple Report

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_simple_report

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
            -   [Purpose of the Report API](/en/docs/mt5/api/reportapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/reportapi_interaction)
            -   [Configuration of Reports](/en/docs/mt5/api/reportapi_configuration)
            -   [Request for Reports](/en/docs/mt5/api/reportapi_request)
            -   [Requirements for Modules](/en/docs/mt5/api/reportapi_requirements)
            -   [Creating a Simple Report](/en/docs/mt5/api/reportapi_simple_report)
            -   [Tabular Reports](/en/docs/mt5/api/reportapi_tables)
            -   [HTML Reports](/en/docs/mt5/api/reportapi_html)
            -   [Dashboards](/en/docs/mt5/api/reportapi_dashboards)
            -   [Templates](/en/docs/mt5/api/reportapi_html_template)
            -   [Charts](/en/docs/mt5/api/reportapi_html_charts)
            -   [Memory Management](/en/docs/mt5/api/reportapi_memory_management)
            -   [Multithreading](/en/docs/mt5/api/reportapi_multithreading)
            -   [Ready-made Examples](/en/docs/mt5/api/reportapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reportapi_entrypoints)
            -   [Report Plugin Interface](/en/docs/mt5/api/imtreportcontext)
            -   [Main Interface of Reports](/en/docs/mt5/api/imtreportapi)
            -   [Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)
            -   [Diagram Interfaces](/en/docs/mt5/api/reportapi_auxiliary)
            -   [Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)
            -   [Data Cache Interfaces](/en/docs/mt5/api/reportapi_cache)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)Creating a Simple Report

# Creating a Simple Report

Reports module written with the help of MetaTrader 5 Report API is a common dynamically downloaded library (DLL). The library can be 32-bit and 64-bit, depending on the bit characteristics of the server it is developed for.

Preparation for the plugin creation includes several stages:

-   [Creating a project in Microsoft Visual Studio](/en/docs/mt5/api/reportapi_simple_report#new_project)
-   [Project setup](/en/docs/mt5/api/reportapi_simple_report#settings)
-   [Specifying the information on the project](/en/docs/mt5/api/reportapi_simple_report#info)
-   [Including Report API in the project](/en/docs/mt5/api/reportapi_simple_report#include)
-   Entry Points
-   Report Class

## Creating a project in Microsoft Visual Studio [#](reportapi_simple_report#new_project)

The first step towards creating a plugin is to create a project in Microsoft Visual Studio. To do this, click New from the File menu:

![New project](/en/docs/mt5/api/img/report_new_project.png "New project")

The main parameters that you need to enter in the new project creation dialog:

-   Project types: Visual C++\\Win32;
-   Name: name of the plugin (in our example MyReportPlugin);
-   Location: directory where the project will be created. A project should be created close to the MetaTrader 5 Report API installation place, since later you will need to include its files in the project.

After you click OK, Application Wizard will open:

![Application Wizard](/en/docs/mt5/api/img/report_wizard.png "Application Wizard")

In the Wizard, go to the "Application Settings" tab. In this type, select "DLL" as the Application type. After you click "Finish", the project will be generated.

## Project setup [#](reportapi_simple_report#settings)

Before you begin to develop the report module, you must configure the project. To do this, click Properties in the Project menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The project is set up for version Release, Active (Win32).</span></p></td></tr></tbody></table>

### General

!["General" section settings](/en/docs/mt5/api/img/report_project_settings_general.png ""General" section settings")

The following key settings must be specified in the "General" section:

-   Character Set: Use Unicode Character Set. The Unicode symbols set must be selected, as MetaTrader 5 servers support only such projects.
-   Whole Program Optimization: Use Link Time Code Generation. This option should be used to speed up the application.

### C/C++

!["C/C++" section settings](/en/docs/mt5/api/img/report_project_settings_c.png ""C/C++" section settings")

The following key settings must be specified in the "C/C++" section:

-   Debug Information Format: Disabled. Debugging data must be turned off, as the Release-project is being configured.

### C/C++ | Optimization

!["Optimization" section settings](/en/docs/mt5/api/img/report_project_settings_c_optimization.png ""Optimization" section settings")

The following key settings must be specified in the "Optimization" subsection of the "C/C++" section:

-   Optimization: Maximum Speed (/O2). Install this option to speed up the application.
-   Inline Function Expansion: Any Suitable (/Ob2). Install this option to speed up the application.
-   Enable Intrinsic Functions: Yes (/Oi). Install this option to speed up the application.

### C/C++ | Code Generation

!["Code Generation" section settings](/en/docs/mt5/api/img/report_project_settings.png ""Code Generation" section settings")

The following settings must be specified in the "Code Generation" subsection of the "C/C++" section:

-   Enable C++ Exceptions: No. It is recommended to disable exceptions, to prevent the appearance of unhandled exceptions that lead to crash of the trading server.
-   Runtime Library: Multi-thread (/MT). To avoid problems, connected with different version of the CRT library (Common Runtime Library) or its absence, it is recommended to use the static linking of CRT - /MT. When debugging, use the Multi-threaded Debug (/MTd) parameter.
-   Buffer Security Check: No (/GS-). This option must be turned off to speed up the application.
-   Enable Function-Level Linking: No. This option must be turned off to speed up the application.
-   Enable Enhanced Instruction Set: Streaming SIMD Extension 2 (/arch:SSE2). SSE2 instructions set must be turned on to considerably speed up the application. This instructions set is supported by the most of the modern CPUs.

### C/C++ | Language

!["Language" section settings](/en/docs/mt5/api/img/report_project_settings_c_language.png ""Language" section settings")

The following key settings must be specified in the "Language" subsection of the "C/C++" section:

-   Enable Run-Time Type Info: No (/GR-). This option must be turned off, as in most cases runtime type identification (RTTI) is not used. RTTI support may slow down the program code execution.

### Linker | Debugging

!["Debugging" section settings](/en/docs/mt5/api/img/report_project_settings_linker_debugging.png ""Debugging" section settings")

The following key settings must be specified in the "Debugging" subsection of the "Linker" section:

-   Generate Debug Info: No. Debugging data generation must be turned off, as the Release version is being configured.

### Additional options for creating 64-bit plugins

If in addition to 32-bit version you are going to developed also a 64-bit plugin, you need to make additional configuration of the project. For this purpose, run Configuration Manager in the Build menu.

![Configuring 64-bit version](/en/docs/mt5/api/img/report_64bit_settings.png "Configuring 64-bit version")

In the window that appears, do the following:

-   In the "Active solution platform" field choose <New> .
-   In the resulting window, select x64 in the "Type or select the new platform" field, as shown above.
-   Press the OK button.

## Specifying the information on the project [#](reportapi_simple_report#info)

It is recommended to specify detailed information on the project plugin for your own convenience and also for the convenience of the future reports module users. To achieve this create the resource file using the "Add Resource" command in the "Project" menu. "Version" must be specified as the created resource type. After the "New" command execution the file will be opened where the information on a plugin and its developer must be specified.

## Including Report API in the project [#](reportapi_simple_report#include)

To work with the server API, you need to include its header file [MT5ReportAPI.h](/en/docs/mt5/api/files_folders_structure#include) in the project.

![Including Server API in the project](/en/docs/mt5/api/img/report_include_api.png "Including Server API in the project")

To do this, in the file stdafx.h of the project, set a relative path to it in the #include directive. In the example shown in the figure, the path "..\\..\\..\\API\\MT5APIReport.h" means that to find the header file, it is necessary to go three levels up and go to the API folder.

## Entry Points [#](reportapi_simple_report#entry)

The server plugin DLL must have two entry points (exported functions):

-   [MTReportAbout](/en/docs/mt5/api/reportapi_simple_report#mtreportabout)
-   [MTReportCreate](/en/docs/mt5/api/reportapi_simple_report#mtreportcreate)

### MTReportAbout [#](reportapi_simple_report#mtreportabout)

Point [MTReportAbout](/en/docs/mt5/api/reportapi_entrypoints/mtreportabout) provides the initial information about the report module to the server. It should be added to the file dllmain.cpp:

![Empty MTReportAbout entry point](/en/docs/mt5/api/img/example_mtreportabout.png "Empty MTReportAbout entry point")

The entry point is empty at the moment. Henceforth, this point must transfer the data (the [MTReportInfo](/en/docs/mt5/api/mtreportinfo) filled structure) on each report requested by an index.

### MTReportCreate [#](reportapi_simple_report#mtreportcreate)

Create an empty entry point [MTReportCreate](/en/docs/mt5/api/reportapi_entrypoints/mtreportcreate) like the previous one:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;Entry&nbsp;point&nbsp;MTReportCreate&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_Type">MTAPIENTRY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_Reserved">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_Functions">MTReportCreate</span><span class="f_CodeExample">(</span><span class="f_Reserved">const&nbsp;UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_Macros">index</span><span class="f_CodeExample">,</span><span class="f_Reserved">const&nbsp;UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_Macros">apiversion</span><span class="f_CodeExample">,</span><span class="f_Reserved">IMTReportContext</span><span class="f_CodeExample">**</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_Macros">context</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

Next, in the [MTReportCreate](/en/docs/mt5/api/reportapi_entrypoints/mtreportcreate) method, we need to create a report API class object that implements the [IMTReportContext](/en/docs/mt5/api/imtreportcontext) interface. Description of this process is available in the next section — ["Report Class"](/en/docs/mt5/api/reportapi_simple_report#report_class).

## Report Class [#](reportapi_simple_report#report_class)

After the [entry points](/en/docs/mt5/api/reportapi_simple_report#entry) are implemented create the report class that will implement the [IMTReportContext](/en/docs/mt5/api/imtreportcontext) interface responsible for the report generation.

### Adding a Class

Add a C++ class using the command "Add Class" in the "Project" menu:

![Adding a Class](/en/docs/mt5/api/img/report_add_class.png "Adding a Class")

Specify the following parameters in the class creation wizard:

-   Class name: CMyTableReport;
-   .h file: MyTableReport.h;
-   .cpp file: MyTableReport.cpp;
-   Base class: IMTReportContext;
-   Access: public.

The key point here is to specify the [IMTReportContext](/en/docs/mt5/api/imtreportcontext) base class.

### Class Implementation [#](reportapi_simple_report#implementation)

Two IMTReportContext interface methods must be set in the class:

-   [Release](/en/docs/mt5/api/imtreportcontext/imtreportcontext_release) — responsible for deleting a report object;
-   [Generate](/en/docs/mt5/api/imtreportcontext/imtreportcontext_generate) —  responsible for a report generation.

Besides, the report data must be described in the class using the [MTReportInfo](/en/docs/mt5/api/mtreportinfo) structure.

Describe necessary structures and methods in the MyTableReport.h file:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">#pragma&nbsp;once</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">class</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CMyTableReport</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">public</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTReportContext</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #0000ff;">private</span><span class="f_CodeExample">:</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">static</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTReportInfo</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">s_info;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Report&nbsp;data</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><br><span class="f_CodeExample" style="color: #0000ff;">public</span><span class="f_CodeExample">:</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Constructor/destructor</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">CMyTableReport(</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">virtual</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">~CMyTableReport(</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Get&nbsp;the&nbsp;report&nbsp;data</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">static</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Info(MTReportInfo&amp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">info)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">{</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">info=s_info;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">virtual</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Release(</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Report&nbsp;generation&nbsp;method</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">virtual</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">Generate(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">type,IMTReportAPI</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">*api);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">};</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

As seen in the above listing, in addition to the virtual Release and Generate methods we have created a private class member s\_info where the report data will be stored.

Besides, the additional Info method has been declared to transfer the report data to the server. This method will further be [called](/en/docs/mt5/api/reportapi_simple_report#info_call) in the dllmain.cpp file.

The next step is the filling the [MTReportInfo](/en/docs/mt5/api/mtreportinfo) structure and description of the abovementioned methods in the MyTableReport.cpp file:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;Plugin&nbsp;description&nbsp;structure&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTReportInfo</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CMyTableReport::s_info=</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">100,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTReportAPIVersion,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTReportInfo::IE_VERSION_ANY,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">L</span><span class="f_CodeExample" style="color: #a31515;">"My&nbsp;Table&nbsp;Report"</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">L</span><span class="f_CodeExample" style="color: #a31515;">"Copyright&nbsp;2001-2011,&nbsp;MetaQuotes&nbsp;Software&nbsp;Corp."</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">L</span><span class="f_CodeExample" style="color: #a31515;">"MetaTrader&nbsp;5&nbsp;Report&nbsp;API&nbsp;plug-in"</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">0,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTReportInfo::TYPE_TABLE,</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">},</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Parameters</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTReportParam::TYPE_GROUPS,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTAPI_PARAM_GROUPS,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">L</span><span class="f_CodeExample" style="color: #a31515;">"*"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">},</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">},1</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//&nbsp;Number&nbsp;of&nbsp;parameters</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">};</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;Constructor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample">CMyTableReport::CMyTableReport(</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;Destructor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample">CMyTableReport::~CMyTableReport(</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;Plugin&nbsp;release&nbsp;method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CMyTableReport::Release(</span><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">delete</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">this</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;Report&nbsp;generation&nbsp;method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CMyTableReport::Generate(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">type,IMTReportAPI</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">*api)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Checking&nbsp;for&nbsp;a&nbsp;pointer</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(!api)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_PARAMS);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

### The MTRepotInfo structure description [#](reportapi_simple_report#mtreportinfo)

Let's observe in details how the [MTReportInfo](/en/docs/mt5/api/mtreportinfo) structure is filled:

-   100 — report module version;
-   MTReportAPIVersion — MetaTrader 5 Report API version where the report module is compiled is transferred by this parameter;
-   MTReportInfo::IE\_VERSION\_ANY — Internet Explorer version necessary for the report operation. In the current case it is indicated that any version is suitable.
-   L"My Table Report" — reports module name;
-   L"Copyright 2001-2011, MetaQuotes Software Corp." — copyright;
-   L"MetaTrader 5 Report API plug-in" — reports module description;
-   0 — [databases snapshots](/en/docs/mt5/api/mtreportinfo#ensnapshots) modes are not used in the current example;
-   MTReportInfo::TYPE\_TABLE — type of report. In our case the chart is tabular;
-   { 0 } — reserved structure parameter, not filled;
-   { MTReportParam::TYPE\_GROUPS, MTAPI\_PARAM\_GROUPS, L"\*" } — [external parameters](/en/docs/mt5/api/mtreportparam) of a report generation that are set during a report request in MetaTrader 5 Manager. In the current case a list of groups may be set for a report. All groups is a default value (indicated by the "\*" symbol);
-   1 —  number of parameters.

The type of a report and its parameters are indicated as such for further use in the [tabular report](/en/docs/mt5/api/reportapi_tables) generation example.

Class constructor and destructor are implemented further.

### Implementation of the Release method [#](reportapi_simple_report#release)

Implementation of the Release method is simple, there is only deleting of an object using delete this.

### Implementation of the Generate method [#](reportapi_simple_report#generate)

At this stage Generate method realization contains only the checking of the transferred pointer to the [IMTReportAPI](/en/docs/mt5/api/imtreportapi) copy. In case the pointer is not valid, the [MT\_RET\_ERR\_PARAMS](/en/docs/mt5/api/retcodes_common) error code is returned.

Further, direct generation and requested report output will be implemented in this method.

### Filling of the exported functions

After the report class implementation the data on it must be transferred to the [MTReportAbout](/en/docs/mt5/api/reportapi_simple_report#mtreportabout) exported function. Also, a report module object copy in the [MTReportCreate](/en/docs/mt5/api/reportapi_simple_report#mtreportcreate) function must be created.

### Calling the Info method [#](reportapi_simple_report#info_call)

Calling the previously described Info virtual method must be described in the previously empty [MTReportAbout](/en/docs/mt5/api/reportapi_simple_report#mtreportabout) entry point of the dllmain.cpp file:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;The&nbsp;MTReportAbout&nbsp;entry&nbsp;point&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample">MTAPIENTRY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTReportAbout(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">index,MTReportInfo&amp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">info)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Checking&nbsp;the&nbsp;index</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(index==0)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">CMyTableReport::Info(info);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_OK);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Not&nbsp;found</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_NOTFOUND);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

Therefore, the CMyTableReport::Info method that transfers previously filled [report data](/en/docs/mt5/api/reportapi_simple_report#mtreportinfo) is executed by a server during the exported function calling.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The feature is that each dll report library may contain several reports numbered beginning from 0. When downloading the module, the MTReportAbout function is called by a server for each report transferring its index in the const UINT index parameter until the <a href="/en/docs/mt5/api/retcodes_common" class="topiclink">MT_RET_ERR_NOTFOUND</a> answer code is returned.</span></p><p class="p_tableatten"><span class="f_tableatten">In the current example the CMyTableReport::Info function transfers the data on the report having index 0.</span></p></td></tr></tbody></table>

### Create a copy of a reports module object [#](reportapi_simple_report#report_instance)

Report module object must be created in the [MTReportCreate](/en/docs/mt5/api/reportapi_simple_report#mtreportcreate) exported function of the dllmain.cpp file:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #008000;">//|&nbsp;The&nbsp;MTReportCreate&nbsp;entry&nbsp;point&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample">MTAPIENTRY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">MTReportCreate(</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">index,</span><span class="f_CodeExample" style="color: #0000ff;">const</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">apiversion,IMTReportContext</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">**context)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Check&nbsp;of&nbsp;parameters</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(!context)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_PARAMS);</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;checking&nbsp;the&nbsp;report&nbsp;index</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(index==0)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Creation&nbsp;of&nbsp;a&nbsp;copy</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">((*context=</span><span class="f_CodeExample" style="color: #0000ff;">new</span><span class="f_CodeExample">(std::nothrow)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CMyTableReport())==NULL)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_MEM);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Successful</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_OK);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Not&nbsp;found</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_NOTFOUND);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #008000;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

Explanation to the code:

-   The first step is a verification if there is a pointer where the pointer to the [IMTReportContext](/en/docs/mt5/api/imtreportcontext) resulting interface must be placed.
-   Then a copy of a reports module object is created for the report having the index 0 using the new command.
-   In case of a successful creation, [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) answer code is returned.
-   The server calls this entry point by the index for each report within the module during the generation start. Indexes of the available reports are specified by the [MTReportAbout](/en/docs/mt5/api/reportapi_simple_report#mtreportabout) entry point.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: when calling the new statement the std::nothrow argument is indicated. That allows to avoid an unprocessed exception in case of memory shortage for an object creation.</span></p><p class="p_tableatten"><span class="f_tableatten">It is strongly recommended to use "nothrow" wherever the memory is provided.</span></p></td></tr></tbody></table>

[Requirements for Modules](/en/docs/mt5/api/reportapi_requirements)

[Tabular Reports](/en/docs/mt5/api/reportapi_tables)