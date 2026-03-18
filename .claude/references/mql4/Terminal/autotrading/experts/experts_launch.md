# Launch

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/experts/experts_launch

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Expert Advisors](/en/docs/mt4/terminal/autotrading/experts)Launch

# Launch

After [general parameters](/en/docs/mt4/terminal/autotrading/experts/experts_setup) have been set up, experts can be launched. To do so, it is enough just to attach the expert to the chart. The "Attach to a chart" command of the ["Navigator — Expert Advisors" window](/en/docs/mt4/terminal/overview/navigator) context menu or double click with the left mouse button on the selected expert in the same window allows to impose it into the active chart.

![EA_add](/en/docs/mt4/terminal/img/ea_add.png)

"Drag'n'Drop" technique allows to impose the expert into any chart. At that, the window of the expert special settings will appear.

![ea_common](/en/docs/mt4/terminal/img/ea_common.png)

In its "Common" tab, it is possible:

-   Positions — select the direction of position opening:

-   -   Long&Short — in both directions;
    -   Only Long — only for buying;
    -   Only Short — only for selling.

-   Enable alerts — enable/disable the expert to alert;
-   Disable alert once hit — disable alerts after the first alert has been given;
-   Allow live trading — enable/disable live trading. Note that even if this option is enabled, the autotrading for the Expert Advisor may be disabled by the [general settings of the terminal](/en/docs/mt4/terminal/setup/setup_experts#enable_ea).
-   Allow DLL imports — enable/disable imports of functions from DLL files;
-   Allow import of external experts — enable/disable calling of functions from external experts;

-   Allow modification of Signals settings — this option allows/prohibits an MQL4 application [subscribing and unsubscribing from Signals](/en/docs/mt4/terminal/signals/signal_subscriber) as well as changing [the settings of signal copying](/en/docs/mt4/terminal/setup/settings_signals). The functions for working with the base of Signals from an MQL4 application allow performing your own analysis of the quality of signals, dynamically manage the subscription and adjust risks. More detailed information about the functions for managing the signals is provided in [MQL4 Reference](https://docs.mql4.com/signals).

External variables of the expert can be changed in the "Inputs" tab.

![ea_inputs](/en/docs/mt4/terminal/img/ea_inputs.png)

These are variables of extern class. To save an input, one has to double-click with the left mouse button on its value and write the new one. At that, one can change the value of each variable or download the set of inputs already saved (the "Load" button). One can save the current set of external variables using the button of the same name.

The "Reset" button returns all default settings. Parameters defined in the [terminal settings](/en/docs/mt4/terminal/autotrading/experts/experts_setup) are given in the "Common" tab. And parameters defined in the program source code are set as inputs. To attach the expert with the new parameters to a chart, one has to press "OK". To cancel the expert imposing, one has to press the button of the same name.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Only attached experts can be set up individually. However, while current executing, the window of the expert properties cannot be opened. This can be done only during intervals between calls of the start() function. At that, the expert will not be launched until its properties window is closed. If the expert inputs were changed, the expert will be re-initialized with its new inputs at pressing of "OK".</span></p></td></tr></tbody></table>

After an expert has been set up, it will be initialized and, as soon as a new tick incomes, execute. Expert is attached if its name and a smiley can be seen in the upper right corner of the chart. If live trading is disabled in the [expert settings](/en/docs/mt4/terminal/autotrading/experts/experts_setup), a L will appear instead of the smiley. A dagger (û) means that all experts are disabled.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Only one expert can be attached to a chart. If another expert is imposed, the previous one will be deleted from the chart.</span></p></td></tr></tbody></table>

[Setup](/en/docs/mt4/terminal/autotrading/experts/experts_setup)

[Shutdown](/en/docs/mt4/terminal/autotrading/experts/experts_remove)