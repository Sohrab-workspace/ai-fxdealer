# IMTManagerAPI::DealerBalance

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerbalance

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
            -   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
            -   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
            -   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
            -   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
            -   [.NET Implementation](/en/docs/mt5/api/managerapi_net)
            -   [Python Implementation](/en/docs/mt5/api/managerapi_python)
            -   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
            -   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
            -   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
                -   [Common Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_network)
                -   [Configuration Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config)
                -   [Selected Symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected)
                -   [Clients](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_clients)
                -   [Users](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user)
                -   [Online Connections](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_online)
                -   [Trade Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading)
                -   [History Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick)
                -   [Mail Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_mail)
                -   [News Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_news)
                -   [Trade Activity](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations)
                    -   [Dealing](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing)
                        -   [DealerConfirmCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerconfirmcreate)
                        -   [DealerUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerunsubscribe)
                        -   [DealerStart](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerstart)
                        -   [DealerStop](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerstop)
                        -   [DealerGet](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerget)
                        -   [DealerLock](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerlock)
                        -   [DealerAnswer](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealeranswer)
                        -   [DealerSend](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealersend)
                        -   [DealerBalance](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerbalance)
                        -   [DealerBalanceRaw](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerbalanceraw)
                    -   [Trade Requests](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_trading_request)
                    -   [Auxiliary Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_trade_auxiliary)
                    -   [Monitoring Account States](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_trade_account)
                -   [Market Depth](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_book)
                -   [Summary Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_summary)
                -   [Exposure](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_exposure)
                -   [Daily Reports](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_daily)
                -   [Settings Files](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)
                -   [ECN](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_geo)
            -   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
            -   [Interface of Manager API Events](/en/docs/mt5/api/imtmanagersink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Trade Activity](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations)[Dealing](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing)DealerBalance

# IMTManagerAPI::DealerBalance

Conduct balance operations on an account.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::DealerBalance</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">value</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Amount</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">type</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Type&nbsp;of&nbsp;operation</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">comment</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Comment</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT64&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal_id</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Deal&nbsp;ID</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.DealerBalance</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">double</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">value</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Amount</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">type</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Type&nbsp;of&nbsp;operation</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">comment</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Comment</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">out&nbsp;ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal_id</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Deal&nbsp;ID</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.DealerBalance</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">value</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Amount</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">type</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Type&nbsp;of&nbsp;operation</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">comment</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Comment</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\]  A login for conducting a balance operation.

value

\[in\]  The amount to add or subtract from an account. In order to deposit to the account, specify a positive value; to withdraw, specify a negative value.

type

\[in\]  Type of the balance operation. To pass the type, the following values of the [IMTDeal::EnDealAction](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_enum#endealaction) enumeration are used: DEAL\_BALANCE, DEAL\_CREDIT, DEAL\_CHARGE, DEAL\_CORRECTION, DEAL\_BONUS, DEAL\_COMMISSION, DEAL\_TAX, DEAL\_DIVIDEND, DEAL\_DIVIDEND\_FRANKED.

comment

\[in\]  A comment to a balance operation. The length of the comment is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

deal\_id

\[out\]  The ID of the deal in which a balance operation was executed.

Return Value

An indication of successful completion is the [MT\_RET\_REQUEST\_DONE](/en/docs/mt5/api/retcodes_trade_request) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

Balance operations are represented as [deals](/en/docs/mt5/api/reference_trading/trading_deal). The ID of the resulting deal is passed in the deal\_id parameter.

In case the deal type is incorrect, the code [MT\_RET\_ERR\_PARAMS](/en/docs/mt5/api/retcodes_common) is returned.

An amount of money accrued/withdrawn with a single operation cannot exceed 1000000000. In case this value is exceeded, the code [MT\_RET\_TRADE\_MAX\_MONEY](/en/docs/mt5/api/retcodes_trades) is returned.

An amount of withdrawal cannot exceed the current free margin (regardless of the balance operation type). In case this amount is exceeded the code [MT\_RET\_REQUEST\_NO\_MONEY](/en/docs/mt5/api/retcodes_trade_request) is returned.

An amount of withdrawal during a credit operation (TYPE=IMTDeal::DEAL\_CREDIT) cannot exceed the amount of previously issued credit assets. In case this amount is exceeded the code [MT\_RET\_REQUEST\_NO\_MONEY](/en/docs/mt5/api/retcodes_trade_request) is returned.

The free margin is not checked during a correction operation (TYPE=IMTDeal::DEAL\_CORRECTION). Be careful with withdrawal operations. If the client has open positions, and you deduct an amount greater than the free margin, Stop Out will trigger on the account.

An amount of withdrawal during any balance operation cannot exceed the current balance. In case this amount is exceeded the code [MT\_RET\_REQUEST\_NO\_MONEY](/en/docs/mt5/api/retcodes_trade_request) is returned.

Balance operations can also be conducted by sending [IMTRequest::TA\_DEALER\_BALANCE](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum) type requests to the requests queue using the [IMTManagerAPI::DealerSend](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealersend) method.

[DealerSend](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealersend)

[DealerBalanceRaw](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerbalanceraw)