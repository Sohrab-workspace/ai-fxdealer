# Shutdown

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/experts/experts_remove

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Expert Advisors](/en/docs/mt4/terminal/autotrading/experts)Shutdown

# Shutdown

To shut down an expert, one has to remove it from the chart. Expert must have been deinitialized before it is shut down. To remove an expert from the chart, one has to execute the [chart context menu](/en/docs/mt4/terminal/chart_management/charts_control) "Expert Advisors — Delete" command or attach another expert to the same chart. Besides, the expert can be removed from the chart at [profile or template](/en/docs/mt4/terminal/chart_management/templates) change.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">at client terminal shutdown, all experts are shut down, too;</span></li><li class="p_tableatten"><span class="f_tableatten">at chart closing, the expert attached to this chart will be shut down;</span></li><li class="p_tableatten"><span class="f_tableatten">at imposing of another expert, the previous one will be removed after confirmation;</span></li><li class="p_tableatten"><span class="f_tableatten">deletion of the expert from the <a href="/en/docs/mt4/terminal/overview/navigator" class="topiclink">"Navigator" window</a> does not shut down the expert of the same name imposed in the chart;</span></li><li class="p_tableatten"><span class="f_tableatten">disabling of experts in the <a href="/en/docs/mt4/terminal/setup/setup_experts" class="topiclink">client terminal settings</a> does not provide complete disabling of experts. This option stops launching of the start() function of each expert, but the init() will continue to execute.</span></li></ul></td></tr></tbody></table>

[Launch](/en/docs/mt4/terminal/autotrading/experts/experts_launch)

[Strategy Testing](/en/docs/mt4/terminal/autotrading/tester)