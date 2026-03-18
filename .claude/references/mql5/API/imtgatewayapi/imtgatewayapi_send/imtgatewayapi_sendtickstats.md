# IMTGatewayAPI::SendTickStats

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendtickstats

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
            -   [Interaction of the Platform and Gateway API](/en/docs/mt5/api/gatewayapi_interaction)
            -   [Trade Operations in Gateway API](/en/docs/mt5/api/gatewayapi_trade_processing)
            -   [Development and Debugging of Gateways](/en/docs/mt5/api/gatewayapi_develop_gateway)
            -   [Symbol and Price Translation](/en/docs/mt5/api/gatewayapi_translation)
            -   [Development of Data Feeds](/en/docs/mt5/api/gatewayapi_develop_datafeed)
            -   [.NET Implementation](/en/docs/mt5/api/gatewayapi_net)
            -   [Exported Functions](/en/docs/mt5/api/gatewayapi_exported)
            -   [CMTGatewayAPIFactory](/en/docs/mt5/api/cmtgatewayapifactory)
            -   [Main Interface](/en/docs/mt5/api/imtgatewayapi)
                -   [Enumerations](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_enum)
                -   [Common Functions](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_common)
                -   [Server](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_server)
                -   [External Connection State](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state)
                -   [Client Connection](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_client)
                -   [Quote and News Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send)
                    -   [SendTickStats](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendtickstats)
                    -   [SendTicks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendticks)
                    -   [SendBookDiffs](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbookdiffs)
                    -   [SendBooks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbooks)
                    -   [SendNews](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendnews)
                    -   [SendEconomicEvents](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendeconomicevents)
                -   [History Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_ticks)
                -   [Users](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user)
                -   [Configuration Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config)
                -   [Trade Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading)
                -   [Trade Requests](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request)
                -   [Gateway Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols)
                -   [Processing Trade Requests](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing)
                -   [Controlling Positions in External System](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_position_control)
                -   [Controlling Orders in External System](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_order_control)
                -   [Synchronizing Trading Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control)
                -   [Mail Database](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_mail)
                -   [User Settings](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_settings)
            -   [Event Interface](/en/docs/mt5/api/imtgatewaysink)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)[Quote and News Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send)SendTickStats

# IMTGatewayAPI::SendTickStats

Sending statistical information about a financial instrument.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewayAPI::SendTickStats</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickStat*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">stats</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Statistical&nbsp;data&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">stats_total</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;the&nbsp;elements&nbsp;in&nbsp;the&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewayAPI.SendTickStats</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickStat[]&nbsp;</span><span class="f_Param">stats&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Statistical&nbsp;data&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewayAPI.SendTickStat</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickStat&nbsp;&nbsp;&nbsp;</span><span class="f_Param">stats&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;single&nbsp;description&nbsp;of&nbsp;statistical&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

stats

\[in\]  A pointer to the statistical data array described by the [MTTickStat](/en/docs/mt5/api/mttickstat) structure.

stats\_total

\[in\]   Number of the elements in the stats array.

Return Value

An indication of a successful execution is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred, which corresponds to the response code.

Note

This method sends the filled [MTTickStat](/en/docs/mt5/api/mttickstat) structures array to the trading platform.

In case the Gateway API applications doesn't call any quote sending functions ([IMTGatewayAPI::SendTicksStats](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendtickstats), [IMTGatewayAPI::SendTicks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendticks), [IMTGatewayAPI::SendBookDiffs](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbookdiffs) or [IMTGatewayAPI::SendBooks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbooks)) during 60 seconds, the following message will be printed in the gateway/data feed journal: "quotes stream stopped (no quotes during X sec)". This feature is aimed to help detecting the cause of no quotes problem. The message is printed one time until the flow of quotes is resumed.

The history server calculates some statistics based on tick data. When sending MTTickStat, the following values are ignored:

-   bid\_high
-   bid\_low
-   ask\_high
-   ask\_low

The following values are also ignored if the charts for the trading symbol are constructed using Bid prices ([IMTConSymol::CHART\_MODE\_BID\_PRICE](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#enchartmode)):

-   last\_high
-   last\_low
-   vol\_high, vol\_high\_ext
-   vol\_low, vol\_low\_ext

[Quote and News Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send)

[SendTicks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendticks)