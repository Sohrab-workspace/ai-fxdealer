# Sending the news

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_send

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
                -   [News](/en/docs/mt5/api/webapi_main/webapi_news)
                    -   [Data Structure](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_data_structure)
                    -   [Send News](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_send)
                    -   [Get News Without Body](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_get)
                    -   [Get News With Body](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_body_request)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)[News](/en/docs/mt5/api/webapi_main/webapi_news)Send News

# Sending the news

This request is used for sending news to clients via the internal system of the platform.

Request format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">POST&nbsp;/api/news/send?subject=header&amp;category=category&amp;language=language&amp;priority=priority</span><br><span class="f_CodeExample">{&nbsp;news&nbsp;text&nbsp;}</span></p></td></tr></tbody></table>

Response format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{&nbsp;"retcode"&nbsp;:&nbsp;"code&nbsp;description"&nbsp;}</span></p></td></tr></tbody></table>

Example

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">//---&nbsp;request&nbsp;to&nbsp;the&nbsp;server</span><br><span class="f_CodeExample">POST&nbsp;/api/news/send?subject=Price%20Alert&amp;category=Technical%20Analysis&amp;language=0&amp;priority=0</span><br><span class="f_CodeExample">\&lt;html\&gt;\&lt;body\&gt;EURUSD&nbsp;reached&nbsp;1.12399\&lt;\/body\&gt;\&lt;\/html\&gt;</span><br><span class="f_CodeExample">//---&nbsp;server&nbsp;response</span><br><span class="f_CodeExample">{&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done"&nbsp;}</span></p></td></tr></tbody></table>

## Request Parameters

-   subject — news subject.
-   category — the category the news belongs to. To specify a subcategory use a backlash "\\". For example, "Economy\\World".
-   language — the language in the LANGID format used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (value from Prim.lang.identifier). The zero value means that the news has no language binding.
-   priority — priority of the news. 0 — normal news, 1 — high-priority news.

The news body is passed as an additional body of the request command in the Unicode format. You may use HTML to format news.

## Response Parameters

-   retcode — if successful, the command returns [a response code](/en/docs/mt5/api/retcodes_successful) 0. Otherwise, it will return an error code.

[Data Structure](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_data_structure)

[Get News Without Body](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_get)