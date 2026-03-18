# Custom Indicators

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/custom_indicators

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)Custom Indicators

# Custom Indicators

Custom indicator is a program independently developed in [MetaQuotes Language 4](/en/docs/mt4/terminal/autotrading/mql4) by the user and functioning as a technical indicator. Technical indicator is a mathematical transformation of security price and/or volume in order to forecast future price changes. The use of indicators allows to answer the question about whether the current trend will remain the same and where it will turn. Indicators are intended for relative simplifying of the complicated process of trading decision making. Algorithms of indicators are also used for development of trading tactics and expert advisors.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Custom indicators are intended only for analyzing of symbol price changes, but not for trading itself.</span></p></td></tr></tbody></table>

Working with custom indicators means:

-   [Creation of an Indicator](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_create)  
    To create and compile custom indicators, one has to use the built-in ["MetaEditor"](/en/docs/mt4/terminal/autotrading/metaeditor). It is a constituent of the client terminal and represents a convenient development environment of MQL4 programs.
-   [Indicator Setup](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_create)  
    Before using of custom indicators, one has to set them up first. Working parameters common for all indicators are defined in the [window of client terminal settings](/en/docs/mt4/terminal/setup/setup_experts). Besides, every indicator can have its own settings.
-   [Imposing of an Indicator](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_create)  
    Parameters of the indicator are calculated and the indicator itself is drawn when imposed into the chart.
-   [Deletion of an Indicator](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_create)  
    If there is no need of an indicator anymore, the indicator can be deleted from the chart.

### New technical analysis features

In the new terminal, the number of built-in technical indicators has been increased from 30 to 38, while the number of [drawing styles](https://www.mql5.com/en/docs/customind/indicators_examples) of custom indicators has been increased 3 times  from 6 to 18. The number of indicator buffers has been expanded from 8 to 512. The indicators themselves can be multi-colored.

### ![color_bb_atr](/en/docs/mt4/terminal/img/color_bb_atr.png)

For programmers, the new platform offers ample opportunities and unmatched convenience when developing indicators. MQL5 programs allow performing the efficient calculation of indicator buffers, set colors and display of individual chart elements, add the Chart object (OBJ\_CHART) to a symbol chart, draw on the canvas, manage an indicator using the keyboard and mouse, and much more.

With the indicators, the fifth generation platform's technical analysis features are endless.

[Results](/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_results)

[Creation](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_create)