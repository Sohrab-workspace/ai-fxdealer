# Creation

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_create

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
            -   [Strategy Testing](/en/docs/mt4/terminal/autotrading/tester)
            -   [Indicator Testing](/en/docs/mt4/terminal/autotrading/tester_indicator)
            -   [Expert Optimization](/en/docs/mt4/terminal/autotrading/tester_optimization)
            -   [Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)
                -   [Creation](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_create)
                -   [Setup](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_setup)
                -   [Attaching to Chart](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_launch)
                -   [Remove](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_remove)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)Creation

# Creation

To create custom indicators, one has to use [MetaQuotes Language 4 (MQL4)](/en/docs/mt4/terminal/autotrading/mql4) and [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor). To launch the editor, one has to execute the "Create" command of the ["Navigator — Custom Indicators" window](/en/docs/mt4/terminal/overview/navigator) context menu, or the ["Tools — MetaQuotes Language Editor" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) command, or press F4 or the ![MetaEditor](/en/docs/mt4/terminal/img/tb_standard_metaeditor.png "MetaEditor") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard). At creation of the MQL4 program, the Experts Wizard that allows to create new MQL4 programs will open automatically. "Custom Indicator" must be selected in it as the object to be created,

![custom_ind_create](/en/docs/mt4/terminal/img/custom_ind_create.png)

and the necessary fields must be filled out:

![custom_ind_create_name](/en/docs/mt4/terminal/img/custom_ind_create_name.png)

-   Name — indicator name;
-   Developer — developer's name;
-   Link — the developer's web site;
-   Inputs — the list of indicator inputs. To add a new parameter, one has to press the "Add" button, and for deletion, one has to press the "Delete".

Then it is necessary to decide whether the new indicator will be created in a separate sub-window and what range it will have. Besides, it is necessary to define the amount and parameters of the indicator arrays. Values of their elements are used to draw lines in the chart. In other words, when indicator arrays are defined, the lines of the future indicator are defined, too. After that, the window of the new indicator with the defined settings will open. A file with the source code (\*.MQ4) of the indicator will be placed into the /EXPERTS/INDICATORS folder of the client terminal automatically. From this point onwards, one can start to write the text of the custom indicator.

After the indicator has been developed, it must be compiled. To do so, one has to execute the "File — Compile" editor menu command, press F9 or the ![Compile](/en/docs/mt4/terminal/img/tb_me_compile.png "Compile") button of the toolbar. After the indicator has been successfully compiled, an executable program file with \*.EX4 extension will be created to be automatically placed into the /EXPERTS/INDICATORS folder. The list of custom indicators can be viewed in the ["Navigator — Custom Indicators" window](/en/docs/mt4/terminal/overview/navigator) of the client terminal.

## Modifying of Custom Indicators

To start modifying of the existing indicator from terminal, one has to execute the "Modify" command of the ["Navigator — Custom Indicator" window](/en/docs/mt4/terminal/overview/navigator) context menu. At that, the [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor) will open where the selected indicator source code has already been downloaded. After this code has been changed, one will have to recompile it and get a new executable EX4 file. Otherwise, the previous, non-modified version of the indicator will be used in the terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If the indicator has been compiled with errors, it is impossible to attach it to the chart. At that, the indicator properties window will not appear, and a record about impossibility to open a file with an executable code will appear in the <a href="/en/docs/mt4/terminal/overview/terminal/terminal_experts" class="topiclink">experts journal</a>.</span></p></td></tr></tbody></table>

[Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)

[Setup](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_setup)