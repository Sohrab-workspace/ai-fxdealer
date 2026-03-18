# IMTServerAPI::DealPerform

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealperform

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
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
                -   [Common Functions](/en/docs/mt5/api/imtserverapi/serverapi_common)
                -   [Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)
                -   [Clients](/en/docs/mt5/api/imtserverapi/serverapi_clients)
                -   [Users](/en/docs/mt5/api/imtserverapi/serverapi_users)
                -   [Online Connections](/en/docs/mt5/api/imtserverapi/serverapi_online)
                -   [Certificates](/en/docs/mt5/api/imtserverapi/serverapi_certificate)
                -   [Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)
                    -   [Orders](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order)
                    -   [Deals](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal)
                        -   [DealCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealcreate)
                        -   [DealCreateArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealcreatearray)
                        -   [DealSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealsubscribe)
                        -   [DealUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealunsubscribe)
                        -   [DealAdd](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealadd)
                        -   [DealAddBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealaddbatch)
                        -   [DealAddBatchArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealaddbatcharray)
                        -   [DealUpdate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealupdate)
                        -   [DealUpdateBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealupdatebatch)
                        -   [DealUpdateBatchArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealupdatebatcharray)
                        -   [DealDelete](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealdelete)
                        -   [DealDeleteBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealdeletebatch)
                        -   [DealGet](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealget)
                        -   [DealGetByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealgetbygroup)
                        -   [DealGetByGroupSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealgetbygroupsymbols)
                        -   [DealGetByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealgetbylogins)
                        -   [DealGetByLoginsSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealgetbyloginssymbol)
                        -   [DealGetByTickets](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealgetbytickets)
                        -   [DealSelectByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealselectbygroup)
                        -   [DealSelectByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealselectbylogins)
                        -   [DealPerform](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealperform)
                        -   [DealPerformCloseBy](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealperformcloseby)
                        -   [DealPerformBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealperformbatch)
                        -   [DealPerformBatchArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealperformbatcharray)
                    -   [Positions](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position)
                    -   [Trade Requests](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request)
                    -   [Request Processing](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_dealer)
                -   [History Data](/en/docs/mt5/api/imtserverapi/serverapi_chart)
                -   [Tick Data](/en/docs/mt5/api/imtserverapi/serverapi_ticks)
                -   [Depth of Market](/en/docs/mt5/api/imtserverapi/serverapi_book)
                -   [Mail Database](/en/docs/mt5/api/imtserverapi/serverapi_mail)
                -   [News Database](/en/docs/mt5/api/imtserverapi/serverapi_news)
                -   [Daily Reports](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily)
                -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_subscription)
                -   [Server Services](/en/docs/mt5/api/imtserverapi/serverapi_server_services)
                -   [Geo Services](/en/docs/mt5/api/imtserverapi/serverapi_geo)
                -   [Dataset](/en/docs/mt5/api/imtserverapi/serverapi_dataset)
                -   [Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)[Deals](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal)DealPerform

# IMTServerAPI::DealPerform

Perform a deal on the client's account. This method performs a market buy or sell operation on an account, as if it is performed by the client through the terminal. The only difference is that no trade request and no order is created to perform the deal, and thus routing rules are not applied to the operation. In all other respects, the behavior is the same: the deal execution result is applied to the position and the account trading state; commission is calculated and charged for the deal in accordance with the relevant account group settings.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::DealPerform</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;deal</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

deal

\[in/out\]  An object of the deal. The deal object must be first created using the [IMTServerAPI::DealCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealcreate) method.

Return Value

The [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code means that the deal has been successfully created. The object of the executed deal from the server base is added to 'deal'. If a deal could not be executed, the method returns a corresponding error code.

Note

A deal can only be performed on the account existing on the same server, on which the plugin is running.

The ticket of the deal being performed ([IMTDeal::DealSet](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_dealset)) must fall into the deals range of the trading server ([IMTConServerTrade::DealsRange\*](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_dealsrangeadd)), and must be greater than the last used ticket.

Note that the server allocates new tickets starting with the last used ticket in the range. For example, if you create a deal with ticket 5000, the server will allocate for further deals ticket numbers 5001, 5002 etc. (even if tickets below 5000 have not been used).

If the ticket is not specified in a deal, the server will automatically assign a ticket to such a deal.

If execution time ([IMTDeal::Time](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_time) or [IMTDeal::TimeMsc](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_timemsc)) is not specified in a deal, the server will automatically set the current time.

The deal integrity is checked during the operation. The following fields must be specified in such a deal:

-   [IMTDeal::Login](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_login)
-   [IMTDeal::Symbol](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_symbol)
-   [IMTDeal::Action](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_action) (only values IMTDeal::DEAL\_BUY and IMTDeal::DEAL\_SELL are allowed)
-   [IMTDeal::Volume](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_volume)
-   [IMTDeal::Price](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_price)
-   [IMTDeal::PositionID](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_positionid) (when closing a position on a hedging account)

You can additionally specify in a deal an individual margin recalculation rate ([IMTDeal::RateMargin](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_ratemargin)) and profit recalculation rate([IMTDeal::RateProfit](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_rateprofit)). If you do not specify them calculated rates will be used.

If commission ([IMTDeal::Commission](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_commission)) is specified in a deal, this commission will be applied to the trading account. However, it does not replace the commission charged in accordance with the trader's group settings ([IMTConGroup::Commission\*](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_commissionadd)). Therefore, the commission specified in the deal is summed up with the calculated commission.

The profit of a deal is always calculated by the server, even if you specify profit in the [IMTDeal::Profit](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_profit) field. The server automatically charges commission on a deal if necessary (in accordance with [commission settings](/en/docs/mt5/api/config_group/imtconcommission)).

It is not recommended to call IMTServerAPI::DealPerform from the following handlers: [IMTDealSink::OnDealAdd](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealadd), [IMTDealSink::OnDealUpdate](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealupdate) and [IMTDealSink::OnDealPerform](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealperform).

An example of closing positions (even if trading is disabled for an instrument)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #808080;">//|&nbsp;Closing&nbsp;client's&nbsp;all&nbsp;positions&nbsp;at&nbsp;the&nbsp;current&nbsp;price&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CPluginInstance::CloseAll(UINT64</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">login)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">IMTPositionArray*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">positions={0};</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">IMTDeal*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">={0};</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">IMTPosition*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">pos_tmp={0};</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTAPIRES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">res;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Check</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(m_api)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">positions=m_api-&gt;PositionCreateArray();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp=m_api-&gt;DealCreate();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">pos_tmp=m_api-&gt;PositionCreate();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_PARAMS);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Get&nbsp;positions</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(res=m_api-&gt;PositionGet(login,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">positions)!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogOK,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">L</span><span class="f_CodeExample" style="color: #008080;">"PositionGet&nbsp;failed&nbsp;[%d]"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">res);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_PARAMS);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogOK,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">L</span><span class="f_CodeExample" style="color: #008080;">"client&nbsp;'%I64u'&nbsp;has&nbsp;%d&nbsp;positions,&nbsp;try&nbsp;to&nbsp;close&nbsp;them"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">login,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">positions-&gt;Total());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">for</span><span class="f_CodeExample">(UINT</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">index=0;index&lt;positions-&gt;Total();index++)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">pos_tmp=positions-&gt;Next(index);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(pos_tmp)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Fill&nbsp;the&nbsp;deal&nbsp;object</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;Login(pos_tmp-&gt;Login());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;Symbol(pos_tmp-&gt;Symbol());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Set&nbsp;the&nbsp;direction&nbsp;of&nbsp;the&nbsp;closing&nbsp;deal&nbsp;depending&nbsp;on&nbsp;the&nbsp;position&nbsp;direction</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(pos_tmp-&gt;Action()</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">==</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">IMTPosition::POSITION_BUY)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;Action(IMTDeal::DEAL_SELL);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;Action(IMTDeal::DEAL_BUY);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Fill&nbsp;other&nbsp;deal&nbsp;parameters</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;Volume(pos_tmp-&gt;Volume());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;Price(pos_tmp-&gt;PriceCurrent());</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;PositionID(pos_tmp-&gt;Position());</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;Only&nbsp;filled&nbsp;for&nbsp;hedging&nbsp;accounts</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Close&nbsp;position&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(res=m_api-&gt;DealPerform(deal_tmp)!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">m_api-&gt;LoggerOut(MTLogOK,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">L</span><span class="f_CodeExample" style="color: #008080;">"DealPerform&nbsp;failed&nbsp;[%d]"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">res);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Clear&nbsp;objects</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(positions)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">positions-&gt;Release();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Clear&nbsp;objects</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(pos_tmp)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">pos_tmp-&gt;Release();</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Clear&nbsp;objects</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(deal_tmp)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">deal_tmp-&gt;Release();</span><br><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

[DealSelectByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealselectbylogins)

[DealPerformCloseBy](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealperformcloseby)