# Deposit/Withdrawal

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_balance

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
            -   [Getting Started](/en/docs/mt5/api/webapi_preparing)
            -   [Format of Commands](/en/docs/mt5/api/webapi_https)
            -   [Authentication](/en/docs/mt5/api/webapi_rest_authentication)
            -   [Escaping Special Characters](/en/docs/mt5/api/webapi_screening)
            -   [Maintaining Connections](/en/docs/mt5/api/webapi_pings)
            -   [Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)
            -   [Examples](/en/docs/mt5/api/webapi_examples)
            -   [Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)
                -   [Configuration Databases](/en/docs/mt5/api/webapi_main/webapi_config)
                -   [Trading](/en/docs/mt5/api/webapi_main/webapi_trading)
                    -   [Orders](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_orders)
                    -   [Deals](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_deal)
                    -   [Positions](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_positions)
                    -   [Trade Requests](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade)
                        -   [Data Structure](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_data_structure)
                        -   [Deposit/Withdrawal](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_balance)
                        -   [Calculate Conversion Rate for Buy](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_rate_buy)
                        -   [Calculate Conversion Rate for Sell](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_rate_sell)
                        -   [Check Margin](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_margin_check)
                        -   [Calculate Profit](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_profit)
                        -   [Send Request](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_dealer_send)
                        -   [Get Request Result](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_dealer_updates)
                -   [Users](/en/docs/mt5/api/webapi_main/webapi_users)
                -   [Clients](/en/docs/mt5/api/webapi_main/webapi_client)
                -   [Mail](/en/docs/mt5/api/webapi_main/webapi_mail)
                -   [News](/en/docs/mt5/api/webapi_main/webapi_news)
                -   [Prices](/en/docs/mt5/api/webapi_main/webapi_prices)
                -   [Daily Reports](/en/docs/mt5/api/webapi_main/webapi_daily)
                -   [Settings Files](/en/docs/mt5/api/webapi_main/webapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription)
                -   [Common Requests](/en/docs/mt5/api/webapi_main/webapi_common_request)
                -   [Outdated version of Rest API](/en/docs/mt5/api/webapi_main/webapi_old)
                -   [PHP Implementation of Protocol](/en/docs/mt5/api/webapi_main/php)
                -   [.NET Implementation of Protocol](/en/docs/mt5/api/webapi_main/net)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)[Trading](/en/docs/mt5/api/webapi_main/webapi_trading)[Trade Requests](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade)Deposit/Withdrawal

# Deposit/Withdrawal

This request allows to conduct balance operations on client accounts.

Request format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;/api/trade/balance?login=login&amp;type=type&amp;balance=sum&amp;comment=comment</span><br><span class="f_CodeExample">POST&nbsp;/api/trade/balance?login=login&amp;type=type&amp;balance=sum&amp;comment=comment</span></p></td></tr></tbody></table>

Response format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;"retcode"&nbsp;:&nbsp;"code&nbsp;description",</span><br><span class="f_CodeExample">&nbsp;"answer"&nbsp;:&nbsp;{&nbsp;"Ticket"&nbsp;:&nbsp;"ticket"&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

Example

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">//---&nbsp;request&nbsp;to&nbsp;the&nbsp;server</span><br><span class="f_CodeExample">GET&nbsp;/api/trade/balance?login=764636&amp;type=2&amp;balance=1000&amp;comment=onlinedeposit</span><br><span class="f_CodeExample">//---&nbsp;server&nbsp;response</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"answer"&nbsp;:&nbsp;{&nbsp;"Ticket"&nbsp;:&nbsp;"136623"&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

## Request Parameters

-   login — the login of an account for which a balance operation should be conducted.
-   type — type of the balance operation. Specified as a value of the [EnDealAction](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_enum#endealaction) enumeration:

-   2 — a balance operation.
-   3 — a credit operation.
-   4 — additional adding/withdrawing.
-   5 — corrective operations.
-   6 — adding bonuses.
-   balance — the amount to change the balance. To add money, set a positive value. To withdraw money, set a negative value.
-   comment — a comment to a balance operation. The maximum comment length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut
-   check\_margin — if the value of this parameter is 1, the free margin is checked before conducting the balance operation. If the amount withdraw is greater than the free margin value, error 10019 is returned. If the parameter is set to zero, the margin is not checked and the requested amount will be withdrawn even if it's greater then the free margin. If the parameter is not passed, the check is considered enabled.

## Response Parameters

-   retcode — if successful, the command returns [a response code](/en/docs/mt5/api/retcodes_successful) 0. Otherwise, it will return an error code.
-   ticket — ticket of a [deal](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_deal) the balance operation has been performed by.

## Notes

-   Balance operations are conducted as [deals](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_deal).
-   In case the deal type is incorrect, the code [3](/en/docs/mt5/api/retcodes_common) is returned.
-   An amount of money accrued/withdrawn with a single operation cannot exceed 1000000000. In case this value is exceeded, the code [4005](/en/docs/mt5/api/retcodes_trades) will be returned.
-   An amount of withdrawal cannot exceed the current free margin. In case this amount is exceeded the code [10019](/en/docs/mt5/api/retcodes_trade_request) is returned.
-   An amount of withdrawal during a credit operation (TYPE=3) cannot exceed the amount of previously issued credit assets. In case this amount is exceeded the code [10019](/en/docs/mt5/api/retcodes_trade_request) is returned.
-   An amount of withdrawal during any balance operation cannot exceed the current balance. In case this amount is exceeded the code [10019](/en/docs/mt5/api/retcodes_trade_request) is returned.

[Data Structure](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_data_structure)

[Calculate Conversion Rate for Buy](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_rate_buy)