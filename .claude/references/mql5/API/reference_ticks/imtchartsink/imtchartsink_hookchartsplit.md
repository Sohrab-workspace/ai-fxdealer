# IMTChartSink::HookChartSplit

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_ticks/imtchartsink/imtchartsink_hookchartsplit

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
            -   [Trade](/en/docs/mt5/api/reference_trading)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
                -   [IMTTickSink](/en/docs/mt5/api/reference_ticks/imtticksink)
                -   [IMTChartSink](/en/docs/mt5/api/reference_ticks/imtchartsink)
                    -   [Enumerations](/en/docs/mt5/api/reference_ticks/imtchartsink/imtchartsink_enum)
                    -   [OnChartSplit](/en/docs/mt5/api/reference_ticks/imtchartsink/imtchartsink_onchartsplit)
                    -   [HookChartSplit](/en/docs/mt5/api/reference_ticks/imtchartsink/imtchartsink_hookchartsplit)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Price Data](/en/docs/mt5/api/reference_ticks)[IMTChartSink](/en/docs/mt5/api/reference_ticks/imtchartsink)HookChartSplit

# IMTChartSink::HookChartSplit

Price data split event handler. For further details about the split operation please refer to [MetaTrader 5 Administrator Help](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_charts/split_charts).

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTChartSink::HookChartSplit</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;new&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">old_shares</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;old&nbsp;shares</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">rounding_rule</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Rounding&nbsp;rule</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">datetime_from</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Beginning&nbsp;of&nbsp;split&nbsp;range</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">datetime_to</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;End&nbsp;of&nbsp;split&nbsp;range</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

news

\[in\]  The symbol for which the split is performed.

new\_shares

\[in\] Number of new shares. Shares are split/consolidated in a certain ratio, and their prices are also converted accordingly.

old\_shares

\[in\] Number of old shares. Shares are split/consolidated in a certain ratio, and their prices are also converted accordingly.

rounding\_rule

\[in\] The rounding rule in case the number of decimal places of a new price after conversion exceeds the value set in the symbol's Digits parameter ([IMTConSymbol::Digits](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_digits)). Specified by a value from the [IMTChartSink::EnSplitRounding](/en/docs/mt5/api/reference_ticks/imtchartsink/imtchartsink_enum#ensplitrounding) enumeration.

For example, when transforming the price of 35.15 with the ratio of 2:1, we obtain 17.575. When rounded down, the final price is 17.57, when rounded up, it is 17.58. The "Standard" rounding option (standard rounding to the nearest integer) is also available. For example, if the Digits is 2, the rounding is performed as follows: 17.234 -> 17.23, 17.235 -> 17.24.

datetime\_from

\[in\]  The beginning date of the time interval in which split will be performed. If the parameter is not set, the split will be performed for the entire symbol price history.

datetime\_to

\[in\]  The end date of the time interval in which split will be performed. If the parameter is not set, the split will be performed for the entire symbol price history.

Return Value

Return [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) to allow splitting or any other response code to deny the operation.

Note

The method is only used in the MetaTrader 5 Server API.

[OnChartSplit](/en/docs/mt5/api/reference_ticks/imtchartsink/imtchartsink_onchartsplit)

[Depth of Market](/en/docs/mt5/api/reference_dom)