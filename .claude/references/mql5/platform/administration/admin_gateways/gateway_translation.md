# Symbol and Price Translation

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateway_translation

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
                -   [Configuration of Gateways](/en/docs/mt5/platform/administration/admin_gateways/gateways_config)
                -   [Status](/en/docs/mt5/platform/administration/admin_gateways/gateway_status)
                -   [Journal of Gateways](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway)
                -   [Positions](/en/docs/mt5/platform/administration/admin_gateways/gateway_positions)
                -   [Setup of Routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_gateways/gateway_service)
                -   [Operation on Weekend](/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend)
                -   [Symbol and Price Translation](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Gateways](/en/docs/mt5/platform/administration/admin_gateways)Symbol and Price Translation

# Symbol and Price Translation

Gateways are able to import necessary sets of trading symbols, manage their settings, update them if necessary and provide quotes. Gateway settings allow you to easily change data passed from the external system:

-   Rename trading symbols
-   Convert quotes
-   Copy price data to different symbols

To do that, use settings on the [Translations](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#translation) tab.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To let a gateway manage settings of trading symbols on the MetaTrader 5 side, enable the <a href="/en/docs/mt5/platform/administration/admin_gateways/gateways_config#symbols" class="topiclink">"Allow importing symbols settings"</a> option.</span></p></td></tr></tbody></table>

## Renaming trading symbols

Data on any symbol can be passed from an external system to the MetaTrader 5 platform under any name. For example, if the symbol name in an external system is EURUSD\_ABC, and it is called EURUSD in the MetaTrader 5, enter EURUSD in the "Symbol" field and EURUSD\_ABC in the "Source" field.

![Renaming the symbol passed by the gateway](/en/docs/mt5/platform/img/translations_rename.png "Renaming the symbol passed by the gateway")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If another source of quotes is already specified in symbol settings (in its <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#source" class="topiclink">Source</a> field), this symbol cannot be specified as the receiver symbol. Also symbols with the disabled <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration" class="topiclink">Allow real-time quotes from data feeds</a> option cannot be specified as receivers. Conversion settings containing such symbols will be ignored by the platform.</span></p></td></tr></tbody></table>

Use the \* mask for renaming multiple symbols. For example, in order to add the .delayed suffix to all gateway symbols, specify:

![Renaming multiple symbols passed by the gateway](/en/docs/mt5/platform/img/translations_rename_mass.png "Renaming multiple symbols passed by the gateway")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Only simple masks with a single * symbol are supported. Settings with more complicated masks (for example, having two * or ! negation symbol) are ignored.</span></p></td></tr></tbody></table>

In order to duplicate data to different symbols on the MetaTrader 5 side, create several entries in the Translations section. In the example below, the entire available set of gateway symbols is passed to the platform in two instances: with the .1 and .2 suffixes.

![Duplicating symbols from an external system in the MetaTrader 5 platform](/en/docs/mt5/platform/img/translation_split.png "Duplicating symbols from an external system in the MetaTrader 5 platform")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">A gateway behavior changes depending on the translations configuration phase:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">The gateway has not yet imported symbols to the platform, while the translation parameters have already been set (for example, renaming) — when enabled, the gateway imports only renamed symbols.</span></li><li class="p_tableatten"><span class="f_tableatten">The gateway has not yet imported symbols to the platform and the translation parameters have not been set — when enabled, the gateway imports original symbols from the external system.</span></li><li class="p_tableatten"><span class="f_tableatten">The gateway has already imported original symbols, while the translation parameters have been set during operation — after saving the settings, the gateway imports a new set of symbols, broadcasts data and manages the settings for the both symbol sets.</span></li></ul></td></tr></tbody></table>

## Price translation

A gateway broadcasts a flow of quotes from an external trading system to the MetaTrader 5 platform and is able to change it on the fly. Clients receive prices according to the translation settings. However, while processing trading operations on the gateway and passing them back to the external system, initial (not transformed) prices are used.

If trading tool names in the platform are not different from the ones in the external system, simply specify a symbol name in the platform and translation value for Bid and Ask prices.

![Translating quotes](/en/docs/mt5/platform/img/translation_price.png "Translating quotes")

The above screenshot shows price conversion: at every tick, the Bid price will be reduced by 3 points, and the Ask price will be increased by 2 points. Below is a schematic example of the conversion:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">External system</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">ask price</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">ask price</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">External system</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">External system</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit execution</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit execution</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td></tr></tbody></table>

A broker gains 2 pips of profit in this example. The price is sent to the client terminal only after the correction, so the clients work only with the corrected prices. If no correction is set for a symbol, the client will work with the original prices submitted by an external system.

Using the previously described possibilities of symbols mass renaming and duplication, you are able to customize different flows of quotes. For example, original and converted ones:

![Creating two quote flows: original and converted](/en/docs/mt5/platform/img/translation_price_split.png "Creating two quote flows: original and converted")

The .wide suffix stands for converted quotes, while the .original stands for non-converted ones.

## Features of trade operations [#](gateway_translation#features)

If only one translation parameter or no parameters at all are set for a gateway, trades are conducted without any peculiarities since the platform is able to match symbols on its side with the ones at the external trading system.

If more than one translation parameter is set for the gateway, the platform attempts to match the symbols correctly. For example, the two translation parameters are set for the gateway:

![The EURUSD symbol has two translation settings in the external system: EURUSD.1 and EURUSD.2](/en/docs/mt5/platform/img/translations_trade_map.png "The EURUSD symbol has two translation settings in the external system: EURUSD.1 and EURUSD.2")

If an order is placed on the platform side, a symbol in the external system response is defined by the original order ticket. For example, a trader places an order #145269 Buy 1.00 EURUSD.2. It is sent to the external system as #145269 Buy 1.00 EURUSD. When receiving a response, the platform converts the symbol back to EURUSD.2 by the original order ticket.

However, there are some trading operations/events that are not preceded by placing an order on the trading platform side. For example, charging a variation margin in an external system. In that case, the platform cannot clearly define which of the two symbols the event is related to: EURUSD.1 or EURUSD.2.

In this situation, the platform attempts to select the correct symbol by its availability to certain accounts the event is related to. For example, if only EURUSD.2 is available for an account, the platform performs an operation for it. Availability of symbols for clients is defined on the [Symbols tab of the group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols).

If both symbols are available for the account, the operation is performed for the first one in the translation list. It is EURUSD.1 in our example.

Thus, if there are multiple translation settings, the following rule is used: trading operations are performed for the first symbol available for a client group. All subsequent translation settings are used only to pass price data.

The table below contains trading operations and events preceded by placing an order on MetaTrader 5 side, which means that symbols can be accurately matched for them regardless of the number of translation settings. For other operations, the platform attempts to define the necessary symbol by its availability for a client group.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">A symbol is accurately matched by an original order</span></p></th><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">A symbol is defined by its availability for a client</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Placing an order of any type</span></p><p class="p_fortable"><span class="f_fortable">Executing an order</span></p><p class="p_fortable"><span class="f_fortable">Rejecting an order</span></p><p class="p_fortable"><span class="f_fortable">Modifying an order</span></p><p class="p_fortable"><span class="f_fortable">Canceling an order</span></p><p class="p_fortable"><span class="f_fortable">Changing an order ID in an external system</span></p><p class="p_fortable"><span class="f_fortable">Closing a position by an opposite one</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Charging a variation margin</span></p><p class="p_fortable"><span class="f_fortable">Re-calculating a profit/loss by trades performed during the current session</span></p><p class="p_fortable"><span class="f_fortable">Removing intraday orders at the end of a trading session</span></p><p class="p_fortable"><span class="f_fortable">Executing a trade in an external system without an order</span></p><p class="p_fortable"><span class="f_fortable">Performing a repo trade</span></p><p class="p_fortable"><span class="f_fortable">A futures or option contract delivery date coming into effect</span></p><p class="p_fortable"><span class="f_fortable">Relocating a position to a new symbol with the same underlying asset</span></p><p class="p_fortable"><span class="f_fortable">Removing all active pending orders</span></p><p class="p_fortable"><span class="f_fortable">Charging rollovers for open positions</span></p></td></tr></tbody></table>

[Operation on Weekend](/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend)

[Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)