# Global Variables

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/service/global_variables

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
        -   [Tools](/en/docs/mt4/terminal/service)
            -   [Configuration at Startup](/en/docs/mt4/terminal/service/start_conf_file)
            -   [History Center](/en/docs/mt4/terminal/service/history_center)
            -   [Export of Quotes](/en/docs/mt4/terminal/service/dde)
            -   [Global Variables](/en/docs/mt4/terminal/service/global_variables)
            -   [Contract Specification](/en/docs/mt4/terminal/service/symbol_spec)
            -   [Languages Support](/en/docs/mt4/terminal/service/languages_support)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Tools](/en/docs/mt4/terminal/service)Global Variables

# Global Variables

Several [experts](/en/docs/mt4/terminal/autotrading/experts) can be launched in the client terminal at the same time. Sometimes, there is a need them to interchange with information. To provide possibility of prompt transfer of moderate amounts of information among experts, as well as organize conflict-free simultaneous working of several experts, there are global variables in the terminal. Unlike variables claimed at a global level in the expert source code and available only within the corresponding module, global variables exsist independently on experts. Their values are saved between terminal launches, unlike those of variables claimed at a global level (they are set at every [expert launch](/en/docs/mt4/terminal/autotrading/experts/experts_launch) and lost at [expert remove](/en/docs/mt4/terminal/autotrading/experts/experts_remove)). Global variables are available within four weeks since their last call from experts or manual modifying.

There is a special window in terminal that manages global variables. It can be opened by execution of the ["Tools — Global Variables" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) command or by pressing of F3. All global variables, their values and times of their last calls are listed in a table in this window. Using buttons located in the right part of the window, one can add a new global variable or delete an existing one. To change the name or value of a global variable, one has to double-click with the left mouse button on the corresponding cell of the table. The last call time will be changed automatically for this variable.

[Export of Quotes](/en/docs/mt4/terminal/service/dde)

[Contract Specification](/en/docs/mt4/terminal/service/symbol_spec)