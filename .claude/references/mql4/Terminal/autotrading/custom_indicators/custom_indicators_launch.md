# Attaching to Chart

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_launch

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)Attaching to Chart

# Attaching to Chart

After [general setup](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_setup) has been completed, one can attach custom indicators to the chart. A custom indicator can be imposed into the active chart by a double click with the left mouse button on it in the ["Navigator — Custom Indicators" window](/en/docs/mt4/terminal/overview/navigator) or by execution of the context menu command "Attach to a chart". The "Drag'n'Drop" technique allows to impose the analytical tool into any chart. At that, the setup window will appear automatically that has several tabs:

-   Common  
    Import from DLLs and MQL4 can be managed in the "Common" tab. Besides, if indicator is drawn in a separate window, one can set up its range from here. To do so, one has to flag the corresponding options and set the desired values in the fields.

-   Allow DLL imports — enable/disable imports of functions from DLL files;
-   Allow import of external experts — enable/disable calling of functions from external experts;
-   Allow modification of Signals settings — this option allows/prohibits an MQL4 application [subscribing and unsubscribing from Signals](/en/docs/mt4/terminal/signals/signal_subscriber) as well as changing [the settings of signal copying](/en/docs/mt4/terminal/setup/settings_signals). The functions for working with the base of Signals from an MQL4 application allow performing your own analysis of the quality of signals, dynamically manage the subscription and adjust risks. More detailed information about the functions for managing the signals is provided in [MQL4 Reference](https://docs.mql4.com/signals).

-   Inputs  
    External variables that can be managed directly from the terminal are grouped in the "Inputs" tab. To modify the desired variable, one has to double-click on its value in the table and write a new one.
-   Colors  
    The "Colors" tab is intended for managing the indicator elements to be shown in the screen. Besides colors, one can also modify thickness and style of lines.
-   Levels  
    Horizontal lines at any level can be set from the "Levels" tab in the indicator window. To create a new level, one has to press the "Add" button, and to delete it, one has to press the "Delete" button. Colors, thickness and style of levels can also be changed from this tab.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: This tab is not available for indicators drawn directly in the price chart.</span></p></td></tr></tbody></table>

-   Visualization  
    One can limit the use of an indicator by timeframes in the "Visualization" tab. This can be useful if the same indicator must have different settings for different timeframes. One can, for example, impose two copies of the same indicator with different settings into the same chart and limit their use by timeframes: the first indicator will work only for smaller timeframes, and the second one will do for larger timeframes. The "Show in the Data Window" option allows to hide/show data about the given indicator in the [Data Window](/en/docs/mt4/terminal/overview/data_window).

![custom_ind_settings](/en/docs/mt4/terminal/img/custom_ind_settings.png)

Immediately after that, recalculation if the indicator values and drawing thereof in the chart will start. Custom indicators, like technical ones, can be drawn in a separate indicator window with its own vertical scale (for example, MACD) or imposed directly into the price chart (for example, Moving Average).

[Setup](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_setup)

[Remove](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_remove)