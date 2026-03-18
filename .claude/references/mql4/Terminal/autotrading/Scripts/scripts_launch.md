# Launch

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/scripts/scripts_launch

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Scripts](/en/docs/mt4/terminal/autotrading/scripts)Launch

# Launch

After [general parameters](/en/docs/mt4/terminal/autotrading/scripts/scripts_setup) have been set up, the script can be launched. To do so, it is enough just to attach it to the chart. At that, of there is a "#property show\_inputs" instruction in the program source code, the script setup window will appear automatically.

![Script settings](/en/docs/mt4/terminal/img/script_settings.png "Script settings")

In the "Common" tab of this window, one can:

-   Positions — select direction of position opening:

-   -   Long&Short — both long and short;
    -   Only Long — only to buy;
    -   Only Short — only to sell.

-   Enable alerts — enable/disable script alerts;
-   Disable alert once hit — disable alerting after the first alert has been made;
-   Allow live trading — enable/disable live trading. Note that even if this option is enabled, the autotrading for the Expert Advisor may be disabled by the [general settings of the terminal](/en/docs/mt4/terminal/setup/setup_experts#enable_ea).
-   Allow DLL imports — enable/disable importing of functions from DLL files;
-   Allow import of external experts — enable/disable calling of functions from external experts.

-   Allow modification of Signals settings — this option allows/prohibits an MQL4 application [subscribing and unsubscribing from Signals](/en/docs/mt4/terminal/signals/signal_subscriber) as well as changing [the settings of signal copying](/en/docs/mt4/terminal/setup/settings_signals). The functions for working with the base of Signals from an MQL4 application allow performing your own analysis of the quality of signals, dynamically manage the subscription and adjust risks. More detailed information about the functions for managing the signals is provided in [MQL4 Reference](https://docs.mql4.com/signals).

External variables of the script can be changed in the "Inputs" tab. They are variables of extern class. To change a parameter, one has to double-click with the left mouse button on its value and write the new one. At that, one can change the value of each variable or download the set of inputs already saved before (the "Load" button). One can save the current set of inputs with the button of the same name.

The "Reset" button returns all default settings. Parameters defined in the [terminal settings](/en/docs/mt4/terminal/autotrading/scripts/scripts_setup) are set in the "Common" tab. And parameters set in the source code of the program are defined as inputs. The script with the defined parameters can be confirmed by pressing of "OK" and canceled by pressing of button of the same name.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Unlike those of <a href="/en/docs/mt4/terminal/autotrading/experts/experts_setup" class="topiclink">experts</a> or <a href="/en/docs/mt4/terminal/autotrading/experts/experts_setup" class="topiclink">custom indicators</a>, special properties of the script are set only at its launch.</span></p></td></tr></tbody></table>

Script will be launched immediately after that. Double click with the left mouse button on the selected script in the ["Navigator — Scripts" window](/en/docs/mt4/terminal/overview/navigator) or execution of the "Execute on Chart" command of the script context menu will attach the script to the active chart. The "Drag'n'Drop" technique will allow to attach the script to any chart. If the "Remove Script" command appears in the chart context menu, it means that script is working. This command is active only while this MQL4 program is working.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Only one script can be attached to a chart.</span></p></td></tr></tbody></table>

[Setup](/en/docs/mt4/terminal/autotrading/scripts/scripts_setup)

[Shutdown](/en/docs/mt4/terminal/autotrading/scripts/scripts_remove)