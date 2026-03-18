# Creating a script

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/wizard_script

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)Creating a script

# Creating a script

A template is a basic source code of a script. It contains the standard program header, general properties and workpieces for the launch event handler — OnStart. A template is created in the directory corresponding to a program type — MQL5/Scripts (or MQL4/Scripts). When creating a template, you can define the program inputs beforehand.

![Creating a script](/en/docs/mt5/metaeditor/img/wizard_script.png "Creating a script")

Fill in the following fields:

-   Name — script name. The same name is assigned to a script file. Here you can also change the path to a destination file. For example, create it in the new \\Scripts sub-directory.
-   Author — author name.
-   Link — developer's email address or website.
-   Parameters — set of script input parameters (external variables).

To create a parameter, click Add and fill in three fields:

-   Name — input variable name
-   Type — type of an input variable selected from the list.
-   Initial value — initial value of a variable. It can be changed before a program launch or during operation.

Click Finish to complete template creation. A generated file is immediately opened for editing.

[Creating an indicator](/en/docs/mt4/metaeditor/wizard_indicator)

[Creating a library](/en/docs/mt4/metaeditor/wizard_library)