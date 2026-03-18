# Creating a ready-made Expert Advisor

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/wizard_ea_generate

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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard)Creating a ready-made Expert Advisor

# Creating a ready-made Expert Advisor

[MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard) allows creating fully operational EAs based on the [standard library](https://www.mql5.com/en/docs/standardlibrary "standard library") supplied together with the trading platform. To do this, select "Expert Advisor (generate)" on the first page of MQL4/MQL5 Wizard.

## General parameters

![General parameters](/en/docs/mt5/metaeditor/img/wizard_ea_common.png "General parameters")

Fill in the following fields:

-   Name — EA name. The same name is assigned to an EA file. Here you can also change the path to a destination file. For example, create it in the new \\Experts subfolders.
-   Author — author name.
-   Link — developer's email address or website.

A set of mandatory parameters created by default is described below:

-   Symbol — specify a symbol the EA is to work on in the Value field. If "current", the EA works on any symbol. A chart symbol the EA is attached to is to be used as a working symbol.
-   TimeFrame — specify a period the EA is to work on in the Value field. If "current", the EA works on any chart period.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Expert Advisor does not run on charts with a symbol or a period other than the ones specified in its settings. In case of an incorrect symbol or period, the appropriate message is displayed in the platform log.</span></p></td></tr></tbody></table>

## Signals [#](wizard_ea_generate#signals)

Signal modules are selected at this stage. An EA makes trading decisions based on data received from them. 64 modules are available in total. You can add any combination of modules, as well as a few similar modules with different settings, to the EA.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The mechanism of making trade decisions is described in the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal#mechanism" target="_blank" class="weblink">MQL5 Reference</a>.</span></p></td></tr></tbody></table>

To add or change the module settings, click Add or Modify.

![Signals](/en/docs/mt5/metaeditor/img/wizard_ea_signal.png "Signals")

Specify signal module parameters:

-   Name — customizable (added) signal module. Signal source code files are located in the \\MQL5\\Include\\Expert\\Signal\\ directory. To open a [detailed description of a selected module](https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal), click "?".
-   Symbol is a working symbol whose price data are to be analyzed by the module.
-   Use current — when enabled, a [working symbol of the EA itself](/en/docs/mt5/metaeditor/wizard_ea_generate#symbol) is selected as a working module symbol.
-   TimeFrame — working period to be analyzed by the module. If "current", [the working period of the EA itself](/en/docs/mt5/metaeditor/wizard_ea_generate#timeframe) is selected as a working module period.

Each signal module has a certain set of built-in parameters:

-   Name — parameter name. For example, PeriodMA is a period of applied moving average.
-   Type — parameter variable type. For example, int means integer.
-   Value — default parameter value.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If the parameter is marked with <img class="help" alt="Active" title="Active" width="16" height="16" src="/en/docs/mt5/metaeditor/img/parameter_active_icon.png"> icon, it is available as an EA input variable. Such parameters can be changed during the EA operation and used when optimizing in the strategy tester. Double-click on the parameter to make it fixed (unavailable for modification when the Expert Advisor is running). Its icon turns gray — <img class="help" alt="Inactive" title="Inactive" width="16" height="16" src="/en/docs/mt5/metaeditor/img/parameter_inactive_icon.png">.</span></li><li class="p_tableatten"><span class="f_tableatten">Each module has its own Weight parameter. It defines the module signal weight considered when making the final decision on a trading operation. The mechanism of making trade decisions is described in <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal#mechanism" target="_blank" class="weblink">MQL5 Reference</a>.</span></li></ul></td></tr></tbody></table>

## Trailing [#](wizard_ea_generate#trailing)

At this stage, select the type of moving stop loss and take profit levels.

![Trailing](/en/docs/mt5/metaeditor/img/wizard_ea_trailing.png "Trailing")

Select a trailing type in the Name field. Source code files of the function data are located in the folder \[platform data directory\]\\MQL5\\Include\\Expert\\Trailing\\. Each type of trailing has its own set of parameters.

-   Name — parameter name.
-   Type — parameter variable type.
-   Value — default parameter value.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the parameter is marked with <img class="help" alt="Active" title="Active" width="16" height="16" src="/en/docs/mt5/metaeditor/img/parameter_active_icon.png"> icon, it is available as an EA input variable. Such parameters can be changed during the EA operation and used when optimizing in the strategy tester. Double-click on the parameter, to make it fixed (unavailable for modification when the Expert Advisor is running). Its icon turns gray — <img class="help" alt="Inactive" title="Inactive" width="16" height="16" src="/en/docs/mt5/metaeditor/img/parameter_inactive_icon.png">.</span></p></td></tr></tbody></table>

## Money management [#](wizard_ea_generate#mm)

At this stage, you should select a money management type for your EA.

![Money management](/en/docs/mt5/metaeditor/img/wizard_ea_mm.png "Money management")

Set a money management type in the Name field. Source code files of the function data are located in the folder \[platform data directory\]\\MQL5\\Include\\Expert\\Money\\. Each type of money management has its own set of parameters.

-   Name — parameter name.
-   Type — parameter variable type.
-   Value — default parameter value.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the parameter is marked with <img class="help" alt="Active" title="Active" width="16" height="16" src="/en/docs/mt5/metaeditor/img/parameter_active_icon.png"> icon, it is available as an EA input variable. Such parameters can be changed during the EA operation and used when optimizing in the strategy tester. Double-click on the parameter, to make it fixed (unavailable for modification when the Expert Advisor is running). Its icon turns gray — <img class="help" alt="Inactive" title="Inactive" width="16" height="16" src="/en/docs/mt5/metaeditor/img/parameter_inactive_icon.png">.</span></p></td></tr></tbody></table>

Click Finish to generate an MQ5 file of the EA. To obtain an executable EA file that can be run in the trading platform, [compile](/en/docs/mt5/metaeditor/compile) the obtained MQ5 file. To do this, click ![Compile](/en/docs/mt5/metaeditor/img/compile_icon.png "Compile") Compile or F7.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Special classes from the Standard library are used as signal, trailing and money management modules. In addition, you can write your own classes (as well as create them based on the existing ones). Place them in the following directories to make them available in MQL5 Wizard:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Signal modules: [platform directory]\MQL5\Include\Expert\Signal</span></li><li class="p_tableatten"><span class="f_tableatten">Trailing modules: [platform directory]\MQL5\Include\Expert\Trailing</span></li><li class="p_tableatten"><span class="f_tableatten">Money management modules: [platform directory]\MQL5\Include\Expert\Money</span></li></ul><p class="p_tableatten"><span class="f_tableatten">Find out more about creating your own modules in the article <a href="https://www.mql5.com/en/articles/226" target="_blank" class="weblink">"MQL5 Wizard: How to create a module of trading signals"</a>.</span></p></td></tr></tbody></table>

[Creating an EA template](/en/docs/mt5/metaeditor/wizard_ea)

[Creating an indicator](/en/docs/mt5/metaeditor/wizard_indicator)