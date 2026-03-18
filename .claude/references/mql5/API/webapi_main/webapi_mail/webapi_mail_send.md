# Sending an Email

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_send

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
                -   [Clients](/en/docs/mt5/api/webapi_main/webapi_client)
                -   [Mail](/en/docs/mt5/api/webapi_main/webapi_mail)
                    -   [Data Structure](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_data_structure)
                    -   [Send Mail](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_send)
                    -   [Get Mail Without Body](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_get)
                    -   [Get Mail With Body](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_body_request)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)[Mail](/en/docs/mt5/api/webapi_main/webapi_mail)Send Mail

# Sending an Email

This request is used for sending emails via the internal mailing system of the trading platform.

Request format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">POST&nbsp;/api/mail/send?to=login&amp;subject=subject&amp;from_name=name</span><br><span class="f_CodeExample">{&nbsp;email&nbsp;text&nbsp;}</span></p></td></tr></tbody></table>

Response format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{&nbsp;"retcode"&nbsp;:&nbsp;"code&nbsp;description"&nbsp;}</span></p></td></tr></tbody></table>

Example

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">//---&nbsp;request&nbsp;to&nbsp;the&nbsp;server</span><br><span class="f_CodeExample">POST&nbsp;/api/mail/send?to=764636&amp;subject=Welcome&amp;from_name=John%20Smith</span><br><span class="f_CodeExample">\&lt;html\&gt;\&lt;body\&gt;Welcome&nbsp;to&nbsp;MetaTrader&nbsp;5\&lt;\/body\&gt;\&lt;\/html\&gt;</span><br><span class="f_CodeExample">//---&nbsp;server&nbsp;response</span><br><span class="f_CodeExample">{&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done"&nbsp;}</span></p></td></tr></tbody></table>

## Request Parameters

-   to — the login of the email recipient. You may use the mask "\*" as well as specify login ranges in this parameter. Example:

-   to=\* — the email will be sent to all clients
-   to=demo\*,preliminary — the email will be sent to all clients from groups "demo" and "preliminary".
-   to=100-250,5000-7500 — the email will be sent to all clients from groups "demo" and "preliminary".
-   subject — email subject.
-   from\_name — the name of the email sender. Optional parameter.

The email body is passed as an additional body of the request command in the Unicode format. You may use HTML to format emails. The body length must be no more than 8192 characters (16 KB).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Emails are sent only to the accounts which are available to the manager account used for Web API <a href="/en/docs/mt5/api/webapi_rest_authentication#client_start" class="topiclink">connection</a> the to the trade server. Available client groups are defined by the "Groups" parameter in the <a href="/en/docs/mt5/api/webapi_preparing#manager_configuration" class="topiclink">manager account settings</a>.</span></p></td></tr></tbody></table>

## Response Parameters

-   retcode — if successful, the command returns [a response code](/en/docs/mt5/api/retcodes_successful) 0. Otherwise, it will return an error code.

[Data Structure](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_data_structure)

[Get Mail Without Body](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_get)