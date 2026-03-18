# Creating an indicator

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/wizard_indicator

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)Creating an indicator

# Creating an indicator

A template is a basic source code of an indicator. It contains the standard program header, general properties and workpieces for the main event handlers: value re-calculation (OnCalculate) and indicator launch (OnInit). A template is created in the directory corresponding to a program type — MQL5/Indicators (or MQL4/Indicators). When creating a template, you can define the program inputs beforehand, as well as add them to the workpiece code for additional event handlers and graphical constructions.

![Creating an indicator](/en/docs/mt5/metaeditor/img/wizard_indicator.png "Creating an indicator")

Fill in the following fields:

-   Name — indicator name. The same name is assigned to its file. Here you can also change the path to a destination file. For example, create it in the new \\Indicators subfolder.
-   Author — author name.
-   Link — developer's email address or website.
-   Parameters — set of indicator input parameters (external variables).

The input parameters are "input" class variables. To create a parameter, click Add and fill in three fields:

-   Name — input variable name.
-   Type — input variable type.
-   Initial value — initial value of a variable. It can be changed before a program launch or during operation.

## Even handlers [#](wizard_indicator#events)

Next, select additional [event handlers](https://www.mql5.com/en/docs/basis/function/events). The workpieces for them are to be inserted into the EA template. OnCalculate handler is mandatory, so you can only select its type, but not delete it.

To view an extended handler description, move the cursor over it.

![Select event handlers](/en/docs/mt5/metaeditor/img/wizard_indicator_events.png "Select event handlers")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Selected handlers are added in addition to the main ones — OnInit and OnCalculate.</span></p></td></tr></tbody></table>

## Display parameters [#](wizard_indicator#plots)

![Creating an indicator](/en/docs/mt5/metaeditor/img/wizard_indicator_2.png "Creating an indicator")

The following parameters are specified at this stage:

-   Indicator in separate window — display indicator in a separate window. If disabled, the indicator is applied to the main chart window.
-   Minimum — lower limit of the vertical scale of indicator values. The parameter is used only when displaying the indicator in a separate window.
-   Maximum — upper limit of the vertical scale of indicator values. The parameter is used only when displaying the indicator in a separate window.

In Plots section, you can specify graphical indicator constructions: name, type (for example, line or histogram) and color. In the indicator code, the corresponding properties of constructions, as well as buffers for values are added.

Click Finish to complete template creation. A generated file is immediately opened for editing.

[Creating a ready-made Expert Advisor](/en/docs/mt4/metaeditor/wizard_ea_generate)

[Creating a script](/en/docs/mt4/metaeditor/wizard_script)