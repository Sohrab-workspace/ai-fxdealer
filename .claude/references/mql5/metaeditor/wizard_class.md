# Creating a class

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/wizard_class

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
            -   [Creating an EA template](/en/docs/mt5/metaeditor/wizard_ea)
            -   [Creating a ready-made Expert Advisor](/en/docs/mt5/metaeditor/wizard_ea_generate)
            -   [Creating an indicator](/en/docs/mt5/metaeditor/wizard_indicator)
            -   [Creating a script](/en/docs/mt5/metaeditor/wizard_script)
            -   [Creating a library](/en/docs/mt5/metaeditor/wizard_library)
            -   [Creating an include file](/en/docs/mt5/metaeditor/wizard_include)
            -   [Creating a class](/en/docs/mt5/metaeditor/wizard_class)
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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard)Creating a class

# Creating a class

A template is a basic source code of a class. It contains the standard program header, general properties and a workpiece for the class: class definition, a workpiece for public and private methods, constructor and destructor. When creating a class, you can specify its basic class which is also appropriately formatted in the template. The template is created in the MQL5/Include (or MQL4/Include) directory.

![Creating a class](/en/docs/mt5/metaeditor/img/wizard_class.png "Creating a class")

Fill in the following fields:

-   Class Name — name for a created class.
-   Include File — name of an mqh file to be created for describing a class, as well as the path to it, relative to /MQL5 (/MQL4) folder.
-   Base Class — if a created class is to be inherited from another one, specify this in the field. Next, select the inheritance type from the base class.
-   Author — author name.
-   Link — developer's email address or website.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Depending on the conditions of MQL4/MQL5 Wizard launch, the appropriate path is automatically substituted in the MQH file:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">If there are no open documents at the moment, /Include path is specified.</span></li><li class="p_tableatten"><span class="f_tableatten">If there are open documents, the path is similar to an active file's one.</span></li><li class="p_tableatten"><span class="f_tableatten">If MQL4/MQL5 Wizard is launched from the Navigator window, the path of the selected folder is substituted.</span></li></ul></td></tr></tbody></table>

Click Finish to complete template creation. A generated file is immediately opened for editing.

[Creating an include file](/en/docs/mt5/metaeditor/wizard_include)

[Developing programs](/en/docs/mt5/metaeditor/development)