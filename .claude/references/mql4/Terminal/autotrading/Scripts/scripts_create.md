# Creation

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/scripts/scripts_create

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
            -   [Scripts](/en/docs/mt4/terminal/autotrading/scripts)
                -   [Creation](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)
                -   [Setup](/en/docs/mt4/terminal/autotrading/scripts/scripts_setup)
                -   [Launch](/en/docs/mt4/terminal/autotrading/scripts/scripts_launch)
                -   [Shutdown](/en/docs/mt4/terminal/autotrading/scripts/scripts_remove)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Scripts](/en/docs/mt4/terminal/autotrading/scripts)Creation

# Creation

To create a script, one has to use [MetaQuotes Language 4 (MQL4)](/en/docs/mt4/terminal/autotrading/mql4) and [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor). To launch the experts editing program, one has to execute the "Create" command of the ["Navigator — Scripts" window](/en/docs/mt4/terminal/overview/navigator) context menu, or the ["Tools — MetaQuotes Language" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) command, or press F4 or the ![MetaEditor](/en/docs/mt4/terminal/img/tb_standard_metaeditor.png "MetaEditor") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard). At an MQL4 program creation, Expert Creation Wizard will open automatically that allows to create new MQL4 programs promptly. "Script" must be selected in it as the object to be created,

![script_create](/en/docs/mt4/terminal/img/script_create.png)

and all necessary fields must be filled out:

![script_create_name](/en/docs/mt4/terminal/img/script_create_name.png)

-   Name — script name;
-   Developer — developer's name;
-   Link — the developer's web-site.

After that, the new script window will open in the editor. File containing the script source code (\*.MQ4) will be placed into the /EXPERTS/SCRIPTS folder of the client terminal automatically. Then one can start to write the source code of the program.

After the script has been created, it must be compiled. To do so, one has to execute the "File — Compile" menu command in the experts editor, press F5 or the ![Compile](/en/docs/mt4/terminal/img/tb_me_compile.png "Compile") button in the toolbar. After the script has been successfully compiled, the executable file with \*.EX4 extension will be created and placed into the /EXPERTS/SCRIPTS folder automatically. The list of all scripts can be viewed in the ["Navigator — Scripts" window](/en/docs/mt4/terminal/overview/navigator) of the client terminal.

## Editing of Scripts

To start editing of the existing script from the terminal, one has to execute the "Modify" command of the ["Navigator — Scripts" window](/en/docs/mt4/terminal/overview/navigator) context menu. At that, the experts editor with the selected script source code already downloaded will open. After the source code has been modified, one has to recompile it and get a new executable EX4 file. Otherwise, the previous, non-modified version of the MQL4 program will be used in the terminal.

[Scripts](/en/docs/mt4/terminal/autotrading/scripts)

[Setup](/en/docs/mt4/terminal/autotrading/scripts/scripts_setup)