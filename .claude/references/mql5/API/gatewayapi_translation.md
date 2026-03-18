# Symbol and Price Translation

> Source: https://support.metaquotes.net/en/docs/mt5/api/gatewayapi_translation

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)Symbol and Price Translation

# Symbol and Price Translation

Gateways are able to import necessary sets of trading symbols, manage their settings, update them if necessary and provide quotes. Gateway settings allow you to easily change data passed from the external system:

-   Rename trading symbols
-   Convert quotes
-   Copy price data to different symbols

The settings are available on the Translations tab of each gateway in the administrator terminal. In API, they are represented by the [IMTConGatewayTranslate](/en/docs/mt5/api/config_gateway/imtcongatewaytranslate) interface.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To let a gateway manage the settings of trading tools on MetaTrader 5 side, enable the "Allow importing symbols settings" option (<a href="/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_enum#engatewayflags" class="topiclink">IMTConGateway::GATEWAY_FLAG_IMPORT_SYMBOLS</a>).</span></p></td></tr></tbody></table>

## Renaming trading symbols

Data on any symbol can be passed from an external system to the MetaTrader 5 platform under any name. For example, if the symbol name in an external system is EURUSD\_ABC, and it is called EURUSD in the MetaTrader 5, enter EURUSD in the "Symbol" field and EURUSD\_ABC in the "Source" field.

![Renaming the symbol passed by the gateway](/en/docs/mt5/api/img/translations_rename.png "Renaming the symbol passed by the gateway")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If another source of quotes is already specified in symbol settings (<a href="/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_source" class="topiclink">IMTConSymbol::Source</a>), this symbol cannot be specified as the receiver symbol. Also symbols with the disabled delivery of real-time quotes from data feeds (<a href="/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#entickflags" class="topiclink">IMTConSymbol::TICK_REALTIME</a>) cannot be specified as receivers. Conversion settings containing such symbols will be ignored by the platform.</span></p></td></tr></tbody></table>

Use the \* mask for renaming multiple symbols. For example, in order to add the .delayed suffix to all gateway symbols, specify:

![Renaming multiple symbols passed by the gateway](/en/docs/mt5/api/img/translations_rename_mass.png "Renaming multiple symbols passed by the gateway")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Only simple masks with a single * symbol are supported. Settings with more complicated masks (for example, having two * or ! negation symbol) are ignored.</span></p></td></tr></tbody></table>

In order to duplicate data to different symbols on the MetaTrader 5 side, create several entries in the Translations section. In the example below, the entire available set of gateway symbols is passed to the platform in two instances: with the .1 and .2 suffixes.

![Duplicating symbols from an external system in the MetaTrader 5 platform](/en/docs/mt5/api/img/translation_split.png "Duplicating symbols from an external system in the MetaTrader 5 platform")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">A gateway behavior changes depending on the translations configuration phase:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">The gateway has not yet imported symbols to the platform, while the translation parameters have already been set (for example, renaming) — when enabled, the gateway imports only renamed symbols.</span></li><li class="p_tableatten"><span class="f_tableatten">The gateway has not yet imported symbols to the platform and the translation parameters have not been set — when enabled, the gateway imports original symbols from the external system.</span></li><li class="p_tableatten"><span class="f_tableatten">The gateway has already imported original symbols, while the translation parameters have been set during operation — after saving the settings, the gateway imports a new set of symbols, broadcasts data and manages the settings for the both symbol sets.</span></li></ul></td></tr></tbody></table>

## Price translation

A gateway broadcasts a flow of quotes from an external trading system to the MetaTrader 5 platform and is able to change it on the fly. Clients receive prices according to the translation settings. However, while processing trading operations on the gateway and passing them back to the external system, initial (not transformed) prices are used.

If trading tool names in the platform are not different from the ones in the external system, simply specify a symbol name in the platform and translation value for Bid and Ask prices.

![Translating the quotes](/en/docs/mt5/api/img/translation_price.png "Translating the quotes")

The above screenshot shows price conversion: at every tick, the Bid price will be reduced by 3 points, and the Ask price will be increased by 2 points. Below is a schematic example of the conversion:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">External system</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">ask price</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">ask price</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">External system</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">External system</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit execution</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit execution</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td></tr></tbody></table>

A broker gains 2 pips of profit in this example. The price is sent to the client terminal only after the correction, so the clients work only with the corrected prices. If no correction is set for a symbol, the client will work with the original prices submitted by an external system.

Using the previously described possibilities of symbols mass renaming and duplication, you are able to customize different flows of quotes. For example, original and converted ones:

![Creating two quote flows: original and converted](/en/docs/mt5/api/img/translation_price_split.png "Creating two quote flows: original and converted")

The .wide suffix stands for converted quotes, while the .original stands for non-converted ones.

## Features of trade operations

If only one translation parameter or no parameters at all are set for a gateway, trades are conducted without any peculiarities since the platform is able to match symbols on its side with the ones at the external trading system.

If more than one translation parameter is set for the gateway, the platform attempts to match the symbols correctly. For example, the two translation parameters are set for the gateway:

![The EURUSD symbol has two translation settings in the external system: EURUSD.1 and EURUSD.2](/en/docs/mt5/api/img/translations_trade_map.png "The EURUSD symbol has two translation settings in the external system: EURUSD.1 and EURUSD.2")

If an order is placed on the platform side, a symbol in the external system response is defined by the original order ticket. For example, a trader places an order #145269 Buy 1.00 EURUSD.2. It is sent to the external system as #145269 Buy 1.00 EURUSD. When receiving a response, the platform converts the symbol back to EURUSD.2 by the original order ticket.

However, there are some trading operations/events that are not preceded by placing an order on the trading platform side. For example, charging a variation margin in an external system. In that case, the platform cannot clearly define which of the two symbols the event is related to: EURUSD.1 or EURUSD.2.

In this situation, the platform attempts to select the correct symbol by its availability to certain accounts the event is related to. For example, if only EURUSD.2 is available for an account, the platform performs an operation for it. Availability of symbols for clients is defined on the Symbols tab of the group settings ([IMTConGroup::Symbol\*](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_symboladd)).

If both symbols are available for the account, the operation is performed for the first one in the translation list. It is EURUSD.1 in our example.

Thus, if there are multiple translation settings, the following rule is used: trading operations are performed for the first symbol available for a client group. All subsequent translation settings are used only to pass price data.

The table below contains trading operations and events ([trade execution types](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_enum#entradeexecutions)) preceded by placing an order on MetaTrader 5 side, which means that symbols can be accurately matched for them regardless of the number of translation settings. For other operations, the platform attempts to define the necessary symbol by its availability for a client group.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">A symbol is accurately matched by an original order</span></p></th><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">A symbol is defined by its availability for a client</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">TE_ORDER_NEW_REQUEST</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_NEW</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_FILL</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_REJECT</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_MODIFY_REQUEST</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_MODIFY</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_MODIFY_REJECT</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_CANCEL_REQUEST</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_CANCEL</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_CANCEL_REJECT</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_CHANGE_ID</span></p><p class="p_fortable"><span class="f_fortable">TE_ORDER_CLOSE_BY</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">TE_DEAL_EXTERNAL</span></p><p class="p_fortable"><span class="f_fortable">TE_DEAL_REPO</span></p><p class="p_fortable"><span class="f_fortable">TE_EOS_CANCEL_DAILY_ORDERS</span></p><p class="p_fortable"><span class="f_fortable">TE_EOS_VARIATION_MARGIN</span></p><p class="p_fortable"><span class="f_fortable">TE_EOS_VARIATION_MARGIN</span></p><p class="p_fortable"><span class="f_fortable">TE_EOS_SETTLEMENT</span></p><p class="p_fortable"><span class="f_fortable">TE_EOS_TRANSFER</span></p><p class="p_fortable"><span class="f_fortable">TE_EOS_CANCEL_ALL_ORDERS</span></p><p class="p_fortable"><span class="f_fortable">TE_EOS_ROLLOVER</span></p></td></tr></tbody></table>

[Development and Debugging of Gateways](/en/docs/mt5/api/gatewayapi_develop_gateway)

[Development of Data Feeds](/en/docs/mt5/api/gatewayapi_develop_datafeed)