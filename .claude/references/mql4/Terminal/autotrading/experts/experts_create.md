# Creation

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/experts/experts_create

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
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
            -   [Where to Get Trade Robots and Indicators](/en/docs/mt4/terminal/autotrading/charts_analysis_get_indicators)
            -   [MQL4](/en/docs/mt4/terminal/autotrading/mql4)
            -   [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor)
            -   [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts)
                -   [Creation](/en/docs/mt4/terminal/autotrading/experts/experts_create)
                -   [Setup](/en/docs/mt4/terminal/autotrading/experts/experts_setup)
                -   [Launch](/en/docs/mt4/terminal/autotrading/experts/experts_launch)
                -   [Shutdown](/en/docs/mt4/terminal/autotrading/experts/experts_remove)
            -   [Strategy Testing](/en/docs/mt4/terminal/autotrading/tester)
            -   [Indicator Testing](/en/docs/mt4/terminal/autotrading/tester_indicator)
            -   [Expert Optimization](/en/docs/mt4/terminal/autotrading/tester_optimization)
            -   [Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)
            -   [Scripts](/en/docs/mt4/terminal/autotrading/scripts)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Expert Advisors](/en/docs/mt4/terminal/autotrading/experts)Creation

# Creation

To create experts, one has to use [MetaQuotes Language 4 (MQL4)](/en/docs/mt4/terminal/autotrading/mql4) and [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor). To launch the expert editing program, one has to execute the "Create" command of the ["Navigator — Expert Advisors" window](/en/docs/mt4/terminal/overview/navigator) context menu, or the ["Tools — MetaQuotes Language Editor" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) command, or press F4 or the ![MetaEditor](/en/docs/mt4/terminal/img/tb_standard_metaeditor.png "MetaEditor") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).

![ea_create_navigator](/en/docs/mt4/terminal/img/ea_create_navigator.png)

After that, the Expert Creation Wizard will be opened automatically that allows to immediately start working at a new MQL4 program. One has to flag the "Expert Advisor" as a type of object to be created and fill out the following fields:

-   Name — expert name;
-   Developer — the developer's name;
-   Link — link to the developer's site;
-   Inputs — the list of expert inputs. To add a new parameter, one has to press the "Add" button or the "Delete" button to delete a parameter.

After that the new expert window with the defined inputs will open in editor. The source file (\*.MQ4) of the expert will be saved in the /EXPERTS folder of the client terminal automatically. At this moment, one can start to write the expert code.

After the expert development has been completed, it must be compiled. To do so, one has to execute the "File — Compile" command in the expert editor, or press F5 or the ![Compile](/en/docs/mt4/terminal/img/tb_me_compile.png "Compile") button of the toolbar. As a result of successful compilation an executable program file with \*.EX4 extension will be created and saved in the /EXPERTS folder automatically. The list of compiled experts can be viewed in the ["Navigator — Expert Advisors" window](/en/docs/mt4/terminal/overview/navigator) in the client terminal. If the expert has not been compiled successfully, its icon will be gray. This means that this expert cannot be used.

## Editing of Experts

To start editing of the existing expert from the terminal, one has to execute the "Modify" command of the ["Navigator — Expert Advisors" window](/en/docs/mt4/terminal/overview/navigator) context menu. At that, the experts editor will open where the source code of the selected expert. After the expert source code has been modified, one has to recompile it and get a new executable EX4 file. Otherwise, terminal will use the previous version of the expert, the non-modified one.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If the expert has not been compiled successfully, its icon will be gray. This means that this expert cannot be used.</span></p></td></tr></tbody></table>

[Expert Advisors](/en/docs/mt4/terminal/autotrading/experts)

[Setup](/en/docs/mt4/terminal/autotrading/experts/experts_setup)