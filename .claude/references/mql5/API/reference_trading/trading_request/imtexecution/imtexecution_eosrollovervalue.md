# IMTExecution::EOSRolloverValue

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosrollovervalue

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)[Trade Requests](/en/docs/mt5/api/reference_trading/trading_request)[IMTExecution](/en/docs/mt5/api/reference_trading/trading_request/imtexecution)EOSRolloverValue

# IMTExecution::EOSRolloverValue

Set the rollover size for a position.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTExecution::EOSRolloverValue</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">value_long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Long&nbsp;position&nbsp;rollover</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">value_short</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Short&nbsp;position&nbsp;rollover</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTExecution.EOSRolloverValue</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">double</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">value_long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Long&nbsp;position&nbsp;rollover</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">double</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">value_short</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Short&nbsp;position&nbsp;rollover</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

value\_long

\[in\]  Long position rollover set in the client's deposit currency.

value\_short

\[in\]  Short position rollover set in the client's deposit currency.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

A symbol the rollover is accrued for is specified in the [IMTExecution::Symbol](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_symbol) field. Short and long position rollover values in the value\_long and value\_short parameters are specified in the client's deposit currency. These values ​​will be added to the current (existing) values ​​of position rollovers in the [IMTPosition::Storage](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_storage) field.

If a zero volume is specified in the [IMTExecution::DealVolume](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolume) field, specified rollover values are accrued to the positions regardless of their volumes. If a non-zero value is specified in [IMTExecution::DealVolume](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolume), the rollover is accrued proportionally: (Specified rollover \* Position volume) / (IMTExecution::DealVolume). In other words, we define the volume the specified rollover is applied to. To minimize errors, it is recommended to set rollovers based on 1 lot.

The accuracy of the currency used for rollover accrual is set in the [IMTExecution::Digits](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_digits) field.

Rollovers can be accrued to a certain client or a client group. First, it is checked whether [IMTExecution::Login](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_login) or [IMTExecution::ExternalAccount](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_externalaccount) field is filled in the trade execution. If yes, the accrual is performed for a client with a specified login or account in an external system. If not, the [IMTExecution::Group](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_group) field is checked. This is a field where a group or a mask for the groups, to which rollovers should be accrued, is specified.

[EOSRolloverValueShort](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_eosrollovervalueshort)

[ApiDataSet](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_apidataset)