# Getting a User by Login

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_get

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
                -   [Users](/en/docs/mt5/api/webapi_main/webapi_users)
                    -   [Data Structure](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_data_structure)
                    -   [Add](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_add)
                    -   [Update](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_update)
                    -   [Delete](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_delete)
                    -   [Get by Login](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_get)
                    -   [Get by External Account](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_external_get)
                    -   [Get Multiple](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_get_batch)
                    -   [Check Password](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_pass_check)
                    -   [Change Password](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_pass_change)
                    -   [Get Trade State](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_account_get)
                    -   [Get Multiple Trade States](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_account_get_batch)
                    -   [Get List](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_logins)
                    -   [Get Total](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_total)
                    -   [Get Group](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_group)
                    -   [Update Certificate](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_cert_update)
                    -   [Get Certificate](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_cert_get)
                    -   [Delete Certificate](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_cert_delete)
                    -   [Confirm Certificate](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_cert_confirm)
                    -   [Get OTP Key](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_otp_secret_get)
                    -   [Set OTP Key](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_otp_secret_set)
                    -   [Sync with External System](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_external_sync)
                    -   [Check Balance](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_balance_check)
                    -   [Move to Archvie](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_archive)
                    -   [Get from Archive](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_archive_get)
                    -   [Get Multiple from Archive](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_archive_get_batch)
                    -   [Restore from Archive](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_restore)
                    -   [Get Backups List](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_backup_list)
                    -   [Get User from Backup](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_backup_get)
                    -   [Send Push Notifications](/en/docs/mt5/api/webapi_main/webapi_users/webapi_notifications_send)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)[Users](/en/docs/mt5/api/webapi_main/webapi_users)Get by Login

# Getting a User by Login

This request allows to get information about a client by the login.

Request format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;/api/user/get?login=login</span><br><span class="f_CodeExample">POST&nbsp;/api/user/get?login=login</span></p></td></tr></tbody></table>

Response format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;"retcode"&nbsp;:&nbsp;"code&nbsp;description",</span><br><span class="f_CodeExample">&nbsp;"answer"&nbsp;:&nbsp;{&nbsp;description&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

Example

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">//---&nbsp;request&nbsp;to&nbsp;the&nbsp;server</span><br><span class="f_CodeExample">GET&nbsp;/api/user/get?login=764636</span><br><span class="f_CodeExample">//---&nbsp;server&nbsp;response</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"answer"&nbsp;:&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"Login":&nbsp;"764636",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"Group":&nbsp;"demo\\forex",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"CertSerialNumber":&nbsp;"0",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"Rights":&nbsp;"6627",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"MQID":&nbsp;"F5986B14",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"Registration":&nbsp;"1527173711",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"LastAccess":&nbsp;"1527173713",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"LastPassChange":&nbsp;"1527173711",</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

## Request Parameters

-   login — the login of an account which should be obtained.

## Response Parameters

-   retcode — if successful, the command returns [a response code](/en/docs/mt5/api/retcodes_successful) 0. Otherwise, it will return an error code.
-   answer — user parameters in JSON format. The complete description of the passed client parameters is given in the ["Data structure"](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_data_structure) section.

## Note

Information about a user that can be obtained depends on access permissions of a manager account that is used for connection of the Web client. If the "Access to personal data of accounts" permission is absent", [some of the fields are not filled](/en/docs/mt5/api/webapi_preparing#private_info) in the server response.

Please pay attention to the [ApiData property](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_data_structure#apidata) use specifics. The following values are returned for each of the array elements (which are always 16):

-   The required fields AppID and ID, which only contain their values.
-   Fields ValueInt, ValueUInt and ValueDouble containing the corresponding presentation of the same binary value, which was written to the ApiData cell (via any type of API).

[Delete](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_delete)

[Get by External Account](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_external_get)