# IMTExecution::DealVolume

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolume

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
                -   [General Principles](/en/docs/mt5/api/reference_trading/general_concept)
                -   [Orders](/en/docs/mt5/api/reference_trading/trading_order)
                -   [Deals](/en/docs/mt5/api/reference_trading/trading_deal)
                -   [Positions](/en/docs/mt5/api/reference_trading/trading_position)
                -   [Accounts](/en/docs/mt5/api/reference_trading/user_account)
                -   [Trade Requests](/en/docs/mt5/api/reference_trading/trading_request)
                    -   [IMTRequest](/en/docs/mt5/api/reference_trading/trading_request/imtrequest)
                    -   [IMTRequestArray](/en/docs/mt5/api/reference_trading/trading_request/imtrequestarray)
                    -   [IMTRequestSink](/en/docs/mt5/api/reference_trading/trading_request/imtrequestsink)
                    -   [IMTConfirm](/en/docs/mt5/api/reference_trading/trading_request/imtconfirm)
                    -   [IMTExecution](/en/docs/mt5/api/reference_trading/trading_request/imtexecution)
                        -   [Enumerations](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_enum)
                        -   [Release](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_release)
                        -   [Assign](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_assign)
                        -   [Clear](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_clear)
                        -   [Print](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_print)
                        -   [ID](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_id)
                        -   [ExternalID](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_externalid)
                        -   [ExternalAccount](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_externalaccount)
                        -   [Action](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_action)
                        -   [Datetime](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_datetime)
                        -   [DatetimeMsc](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_datetimemsc)
                        -   [Login](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_login)
                        -   [Group](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_group)
                        -   [Flags](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_flags)
                        -   [Symbol](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_symbol)
                        -   [SymbolNew](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_symbolnew)
                        -   [Digits](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_digits)
                        -   [Comment](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_comment)
                        -   [Order](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_order)
                        -   [OrderExternalID](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderexternalid)
                        -   [OrderType](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_ordertype)
                        -   [OrderVolume](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_ordervolume)
                        -   [OrderVolumeExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_ordervolumeext)
                        -   [OrderPrice](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderprice)
                        -   [OrderActivationFlags](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderactivationflags)
                        -   [OrderActivationMode](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderactivationmode)
                        -   [OrderTypeFill](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_ordertypefill)
                        -   [OrderTimeExpiration](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_ordertimeexpiration)
                        -   [OrderTypeTime](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_ordertypetime)
                        -   [OrderPriceTrigger](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderpricetrigger)
                        -   [OrderPriceSL](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderpricesl)
                        -   [OrderPriceTP](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderpricetp)
                        -   [DealExternalID](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealexternalid)
                        -   [DealAction](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealaction)
                        -   [DealVolume](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolume)
                        -   [DealVolumeExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolumeext)
                        -   [DealVolumeRemaind](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolumeremaind)
                        -   [DealVolumeRemaindExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolumeremaindext)
                        -   [DealPrice](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealprice)
                        -   [DealReason](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealreason)
                        -   [DealStorage](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealstorage)
                        -   [DealCommission](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealcommission)
                        -   [Position](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_position)
                        -   [PositionBy](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_positionby)
                        -   [PositionExternalID](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_positionexternalid)
                        -   [PositionByExternalID](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_positionbyexternalid)
                        -   [PositionPriceSL](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_positionpricesl)
                        -   [PositionPriceTP](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_positionpricetp)
                        -   [EOSSessionStart](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eossessionstart)
                        -   [EOSSessionEnd](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eossessionend)
                        -   [EOSPriceSettlement](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eospricesettlement)
                        -   [EOSProrfitRateBuy](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosprorfitratebuy)
                        -   [EOSProrfitRateSell](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosprorfitratesell)
                        -   [EOSProrfitRate](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosprorfitrate)
                        -   [EOSTickValue](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eostickvalue)
                        -   [EOSRolloverValueLong](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosrollovervaluelong)
                        -   [EOSRolloverValueShort](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosrollovervalueshort)
                        -   [EOSRolloverValue](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosrollovervalue)
                        -   [ApiDataSet](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidataset)
                        -   [ApiDataGet](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidataget)
                        -   [APIDataUpdate](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidataupdate)
                        -   [APIDataNext](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidatanext)
                        -   [APIDataRawSet](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidatarawset)
                        -   [APIDataRawGet](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidatarawget)
                        -   [APIDataRawMax](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidatarawmax)
                        -   [ApiDataClear](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidataclear)
                        -   [ApiDataClearAll](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidataclearall)
                        -   [PriceGateway](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_pricegateway)
                        -   [VolumeGatewayExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_volumegatewayext)
                        -   [ActionGateway](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_actiongateway)
                        -   [GatewayID](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_gatewayid)
                        -   [ExternalRetcode](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_externalretcode)
                -   [Summary Positions](/en/docs/mt5/api/reference_trading/trading_summary)
                -   [Assets](/en/docs/mt5/api/reference_trading/trading_exposure)
                -   [Daily Reports](/en/docs/mt5/api/reference_trading/trading_daily)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)[Trade Requests](/en/docs/mt5/api/reference_trading/trading_request)[IMTExecution](/en/docs/mt5/api/reference_trading/trading_request/imtexecution)DealVolume

# IMTExecution::DealVolume

Gets the deal volume in lots.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">UINT64&nbsp;&nbsp;</span><span class="f_Functions">IMTExecution::DealVolume</span><span class="f_CodeExample">()</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">ulong&nbsp;&nbsp;</span><span class="f_Functions">CIMTExecution.DealVolume</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Return Value

The deal volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

Note

The method operates with [the standard volume accuracy](/en/docs/mt5/api/features#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::DealVolumeExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolumeext) method.

# IMTExecution::DealVolume

Sets the deal volume in lots.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTExecution::DealVolume</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">volume</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Deal&nbsp;volume</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTExecution.DealVolume</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">volume</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Deal&nbsp;volume</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

volume

\[in\]  The deal volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

Return Value

An indication of a successful execution is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred, which corresponds to the response code.

Note

The method operates with [the standard volume accuracy](/en/docs/mt5/api/features#volume) (4 decimal places). For extended volume accuracy, use the [IMTExecution::DealVolumeExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolumeext) method.

If the order is created with the Fill or Kill ([IMTOrder::ORDER\_FILL\_FOK](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enorderfilling)) fill policy and with the Instant ([IMTConSymbol::EXECUTION\_INSTANT](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#enexecutionmode)) or Request ([IMTConSymbol::EXECUTION\_REQUEST](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#enexecutionmode)) execution mode, this order can only be filled in the specified volume and at the specified price. If you specify a smaller volume in the trade execution, the trading platform will reject the operation. In the Market ([IMTConSymbol::EXECUTION\_MARKET](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#enexecutionmode)) and Exchange ([IMTConSymbol::EXECUTION\_EXCHANGE](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#enexecutionmode)) execution modes, the price is not specified in the order and the required volume can be made up of several offers from the order book. Therefore, you can specify a lower volume in the trade execution for these modes.

[DealAction](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealaction)

[DealVolumeExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolumeext)