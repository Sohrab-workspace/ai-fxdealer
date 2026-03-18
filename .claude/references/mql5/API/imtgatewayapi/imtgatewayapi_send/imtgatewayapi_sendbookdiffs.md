# IMTGatewayAPI::SendBookDiffs

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbookdiffs

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)[Quote and News Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send)SendBookDiffs

# IMTGatewayAPI::SendBookDiffs

Send the Depth of Market changes.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewayAPI::SendBookDiffs</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTBookDiff*&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">bookdiffs</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Depth&nbsp;of&nbsp;Market&nbsp;changes&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">bookdiffs_total</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;the&nbsp;elements&nbsp;in&nbsp;the&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewayAPI.SendBookDiffs</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTBook[]&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">bookdiffs</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Depth&nbsp;of&nbsp;Market&nbsp;changes&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewayAPI.SendBookDiff</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTBook&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">bookdiffs</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;single&nbsp;change&nbsp;of&nbsp;the&nbsp;depth&nbsp;of&nbsp;market</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

\*bookdiffs

\[in\]  A pointer to the array of the Depth of Market changes described by the [MTBookDiff](/en/docs/mt5/api/mtbook) structure.

bookdiffs\_total

\[in\]  Number of the elements in the bookdiffs array.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred which corresponds to the response code.

Note

This method sends the filled [MTBookDiff](/en/docs/mt5/api/mtbook) structures array to the trading platform.

Unlike the [IMTGatewayAPI::SendBooks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbooks) method, in the IMTGatewayAPI::SendBookDiffs method only Depth of Market changes are transferred instead of the whole data layer. Programmer have to define the difference between the current and the previous state of the Depth of Market, appropriately fill MTBookDiff structure and pass it using the SendBookDiffs method.

To reset the Depth of Market state, pass the Market Depth change in the SendBookDiffs method, with one element of the [ItemReset](/en/docs/mt5/api/mtbookitem#enbookitem) type.

For symbols with the depth of market support (changes of the market depth are transmitted for them using the [IMTGatewayAPI::SendBookDiffs](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbookdiffs) and [IMTGatewayAPI::SendBooks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbooks) methods), you don't need to transmit the Bid and Ask tick data using the [IMTGatewayAPI::SendTicks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendticks) method. These data is automatically formed by the history server on the basis of best Ask and Bid prices in the depth of market. However, for such symbols, you should send the Last price and Volume in the MTTick structure using the IMTGatewayAPI::SendTicks. These values are used for transmitting the information about deals performed in an external trading system to the MetaTrader 5 platform. Those prices are used for drawing charts. If the Last price is unavailable in the data source, use Bid price values for filling the corresponding field in MTTick.

In case the Gateway API applications doesn't call any quote sending functions ([IMTGatewayAPI::SendTicksStats](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendtickstats), [IMTGatewayAPI::SendTicks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendticks), [IMTGatewayAPI::SendBookDiffs](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbookdiffs) or [IMTGatewayAPI::SendBooks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbooks)) during 60 seconds, the following message will be printed in the gateway/data feed journal: "quotes stream stopped (no quotes during X sec)". This feature is aimed to help detecting the cause of no quotes problem. The message is printed one time until the flow of quotes is resumed.

## Filling MTBookDiff Structure

Each element of the aggregated depth of market is unique in type and price. The [MTBookDiff](/en/docs/mt5/api/mtbook) structure contains information about volume changes for a given type and price in the form of an array of MTBookItem [MTBookItem](/en/docs/mt5/api/mtbookitem) elements. One MTBookDiff structure contains changes only for one instrument, described in the 'symbol' value of the structure.

Depth of Market change element types are listed below together with the actions of a history server when getting the elements of a specified type for the aggregative Depth of Market generation:

-   ItemReset — a history server will clean up the aggregative Depth of Market by the specified symbol when getting the element with such a type.
-   ItemSell, ItemBuy — a history server will look for the aggregative Depth of Market element by its type and price specified in MTBookItem when getting the [MTBookItem](/en/docs/mt5/api/mtbookitem) structure with such a type. If the element is not found, then a new element (of MTBookItem type and price) is added to the aggregated depth of market. If the element is found in the aggregated depth of market, then element volume changes by the volume value, specified in the MTBookItem structure. In case a zero volume is indicated in the MTBookItem structure, the element found in the aggregative Depth of Market will be deleted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The volume of element change in the aggregated depth of market, described in MTBookItem, can be both positive and negative.</span></li><li class="p_tableatten"><span class="f_tableatten">The trading platform analyzes the items elements sent in the MTBookDiff structure strictly from the beginning to the end, consequently applying changes to the market depth.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">All the symbol prices delivered into the platform are rounded in accordance with the <a href="/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_digits" class="topiclink">IMTConSymbol::Digits</a> parameter of the symbol. When broadcasting prices with higher accuracy, different levels can be combined into one rounded level. To avoid collisions, set the precision of the symbols in accordance with the precision of transmitted data.</span></li></ul></td></tr></tbody></table>

Example

Let's analyze an example of how the difference between the Depths of Market at different time points is calculated:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" colspan="3"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Time point 1</span></p></th><th class="table" colspan="3"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Time point 2</span></p></th><th class="table" colspan="3"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Comparison result</span></p></th><th class="table" rowspan="2" style="width:241px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Comment</span></p></th></tr><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Price</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Size</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Price</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Size</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Price</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Size</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Sell</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32464</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">5</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sell</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32464</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">5</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sell</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32463</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">-3</span></p></td><td class="table" style="width:241px;"><p class="p_fortable"><span class="f_fortable">Bid volume with the price 1.32463 decreased by 3 lots.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Sell</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32463</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">6</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sell</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32463</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">3</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Buy</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32461</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table" style="width:241px;"><p class="p_fortable"><span class="f_fortable">Bid with the price 1.32461 disappeared from the Depth of Market.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Buy</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32461</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">3</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Buy</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32460</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">4</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Buy</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32459</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table" style="width:241px;"><p class="p_fortable"><span class="f_fortable">Bid with the price 1.32459 disappeared from the Depth of Market.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Buy</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32459</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Buy</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1.32460</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">4</span></p></td><td class="table" style="width:241px;"><p class="p_fortable"><span class="f_fortable">Bid with the price 1.32460 and the volume of 4 lots appeared in the Depth of Market.</span></p></td></tr></tbody></table>

[SendTicks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendticks)

[SendBooks](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send/imtgatewayapi_sendbooks)