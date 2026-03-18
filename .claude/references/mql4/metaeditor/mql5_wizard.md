# MQL4/MQL5 Wizard

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/mql5_wizard

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
            -   [Creating an EA template](/en/docs/mt4/metaeditor/wizard_ea)
            -   [Creating a ready-made Expert Advisor](/en/docs/mt4/metaeditor/wizard_ea_generate)
            -   [Creating an indicator](/en/docs/mt4/metaeditor/wizard_indicator)
            -   [Creating a script](/en/docs/mt4/metaeditor/wizard_script)
            -   [Creating a library](/en/docs/mt4/metaeditor/wizard_library)
            -   [Creating an include file](/en/docs/mt4/metaeditor/wizard_include)
            -   [Creating a class](/en/docs/mt4/metaeditor/wizard_class)
        -   [Developing programs](/en/docs/mt4/metaeditor/development)
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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)MQL4/MQL5 Wizard

# MQL4/MQL5 Wizard

MQL4/MQL5 Wizard allows you to quickly create program templates and ready-made trading robots.

With the MQL4/MQL5 Wizard, a trader can develop Expert Advisors even without programming skills. All that is needed to do is to select trading signals for an Expert Advisor, money management and trailing stop algorithms. The Expert Advisor code will be generated automatically based on selected parameters.

In addition, the MQL4/MQL5 Wizard allows to create MQL4/MQL5 programs templates simplifying the work of a programmer. A template is a file designed for writing a source code. After it has been created, it is automatically placed in an appropriate directory, depending on the selected program type. During the creation, a user can select event handlers that will be added to the template. This reduces time spent on routine tasks when creating programs.

The Wizard also allows you to create [projects](/en/docs/mt5/metaeditor/projects) — apart from a source code file (a template or a ready-made EA), an MQPROJ project set file is generated as well.

To launch MQL4/MQL5 Wizard, click ![New](/en/docs/mt5/metaeditor/img/new_icon.png "New") New in the [File](/en/docs/mt5/metaeditor/main_menu_file) menu or [toolbar](/en/docs/mt5/metaeditor/toolbar_standard).

![MQL Wizard](/en/docs/mt5/metaeditor/img/mql5_wizard.png "MQL Wizard")

The first step of working with the Wizard is the selection of the created project type:

-   [Expert Advisor (template)](/en/docs/mt5/metaeditor/wizard_ea)  
    Create a template of an Expert Advisor allowing to fully automate analytical and trading activity for effective trading on financial markets.
-   [Expert Advisor (generate)](/en/docs/mt5/metaeditor/wizard_ea_generate)  
    Generate ready-made Expert Advisor based on the [standard library](https://www.mql5.com/en/docs/standardlibrary "standard library") by selecting trading signals, money management and trailing stop algorithms for it.
-   [Custom Indicator](/en/docs/mt5/metaeditor/wizard_indicator)  
    Generate a template for writing a custom technical indicator for the prices dynamics analysis.
-   [Script](/en/docs/mt5/metaeditor/wizard_script)  
    Generate a template for writing a script - a program for a one-time execution of any actions.
-   [Library](/en/docs/mt5/metaeditor/wizard_library)  
    Generate a template for writing a library of functions that can be used in various applications.
-   [Include (\*.mqh)](/en/docs/mt5/metaeditor/wizard_include)  
    Generate a template of an included file. Such files contain some definite functions used in various applications.
-   [New Class](/en/docs/mt5/metaeditor/wizard_class)  
    Generate a template of an included file for a class description. Classes can be used during the development of various programs.

[External Subversion client](/en/docs/mt4/metaeditor/mql5storage_svn_client)

[Creating an EA template](/en/docs/mt4/metaeditor/wizard_ea)