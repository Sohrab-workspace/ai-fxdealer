# IMTGatewayAPI::SymbolAddPreliminary

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symboladdpreliminary

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
                -   [History Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_ticks)
                -   [Users](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user)
                -   [Configuration Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config)
                    -   [Common](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_common)
                    -   [Data Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_datafeeds)
                    -   [Gateways](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_gateway)
                    -   [Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol)
                        -   [SymbolCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolcreate)
                        -   [SymbolSessionCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolsessioncreate)
                        -   [SymbolSubscribe](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolsubscribe)
                        -   [SymbolUnsubscribe](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolunsubscribe)
                        -   [SymbolAddPreliminary](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symboladdpreliminary)
                        -   [SymbolUpdate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolupdate)
                        -   [SymbolDelete](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symboldelete)
                        -   [SymbolTotal](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symboltotal)
                        -   [SymbolNext](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolnext)
                        -   [SymbolGet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolget)
                    -   [Groups](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_group)
                    -   [Time](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_time)
                    -   [Network](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_network)
                    -   [Spreads](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_spread)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)[Configuration Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config)[Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol)SymbolAddPreliminary

# IMTGatewayAPI::SymbolAddPreliminary

Add or update a preliminary configuration of a symbol.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewayAPI::SymbolAddPreliminary</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTConSymbol*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;symbol&nbsp;configuration</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewayAPI.SymbolAddPreliminary</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTConSymbol</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">symbol</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;symbol&nbsp;configuration</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

symbol

\[in\]  An object of the symbol configuration.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

## Symbol Adding Features

Process of the importing the symbols into the trading platform using this method has several peculiarities:

-   When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated (the list of parameters that can be updated is given below), otherwise a new entry is added. A key field for comparison is the name of the symbol [IMTConSymbol::Symbol()](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_symbol). When you try to add a completely identical record, no changes are made, and therefore the [IMTConSymbolSink::OnSymbolUpdate](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_onsymbolupdate) notification method is not called.
-   All symbols are added to the \\Preliminary\\ symbols subgroup. For example, if the path 'Metals\\Gold' ([IMTConSymol::Path](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_path)) is indicated in the added symbol parameter, the symbol will be added to the \\Preliminary\\Metals\\Gold group.
-   All symbols are imported with the trading possibility ([IMTConSymbol::TradeMode](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_trademode)) turned off.

Therefore, an administrator has to manually place a symbol into an appropriate group after the import and allow trading for it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For full control over symbols, use <a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolupdate" class="topiclink">IMTGatewayAPI::SymbolUpdate</a> method. It allows adding symbols to any group and changing any symbol parameters.</span></p></td></tr></tbody></table>

The below list includes all the symbol parameters that can be changed using this method. Other parameters cannot be modified.

-   [ISIN](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_isin)
-   [Description](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_description)
-   [International](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_international)
-   [Basis](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_basis)
-   [Source](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_source)
-   [Page](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_page)
-   [CurrencyBase](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_currencybase)
-   [CurrencyProfit](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_currencyprofit)
-   [CurrencyMargin](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_currencymargin)
-   [Color](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_color)
-   [ColorBackground](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_colorbackground)
-   [TickFlags](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tickflags)
-   [TickBookDepth](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tickbookdepth)
-   [FilterDiscard](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterdiscard)
-   [FilterSoft](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filtersoft)
-   [FilterSoftTicks](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filtersoftticks)
-   [FilterHard](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterhard)
-   [FilterHardTicks](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterhardticks)
-   [TradeFlags](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tradeflags)
-   [Spread](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_spread)
-   [SpreadBalance](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_spreadbalance)
-   [TickValue](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tickvalue)
-   [TickSize](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_ticksize)
-   [ContractSize](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_contractsize)
-   [GTCMode](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_gtcmode)
-   [CalcMode](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_calcmode)
-   [QuotesTimeout](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_quotestimeout)
-   [PriceSettle](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_pricesettle)
-   [PriceLimitMax](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_pricelimitmax)
-   [PriceLimitMin](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_pricelimitmin)
-   [TimeStart](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_timestart)
-   [TimeExpiration](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_timeexpiration)
-   [FillFlags](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_fillflags)
-   [ExpirFlags](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_expirflags)
-   [VolumeMin](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_volumemin)
-   [VolumeMax](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_volumemax)
-   [VolumeStep](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_volumestep)
-   [VolumeLimit](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_volumelimit)
-   [MarginCheckMode](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginflags)
-   [MarginInitial](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_margininitial)
-   [MarginMaintenance](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginmaintenance)
-   [MarginLong](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginlong)
-   [MarginShort](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginshort)
-   [MarginLimit](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginlimit)
-   [MarginStop](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginstop)
-   [MarginStopLimit](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginstoplimit)

[SymbolUnsubscribe](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolunsubscribe)

[SymbolUpdate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolupdate)