# IMTNewsSink::OnNews

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_news/imtnewssink/imtnewssink_onnews

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
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
                -   [IMTNews](/en/docs/mt5/api/reference_news/imtnews)
                -   [IMTNewsSink](/en/docs/mt5/api/reference_news/imtnewssink)
                    -   [OnNews](/en/docs/mt5/api/reference_news/imtnewssink/imtnewssink_onnews)
                    -   [HookNews](/en/docs/mt5/api/reference_news/imtnewssink/imtnewssink_hooknews)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[News Database](/en/docs/mt5/api/reference_news)[IMTNewsSink](/en/docs/mt5/api/reference_news/imtnewssink)OnNews

# IMTNewsSink::OnNews

A handler of the event of news receiving.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTNewsSink::OnNews</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTNews*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">news</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;news&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTNewsSink.OnNews</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTNews</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">news</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;News&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

news

\[in\]  A pointer to the news object.

Note

In Manager API, only the news header without the body is received in the IMTNewsSink::OnNews event. To request the news body, call the [IMTManagerAPI::NewsBodyRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_news/imtmanagerapi_newsbodyrequest) method while passing to the method the news ID ([IMTNews::ID](/en/docs/mt5/api/reference_news/imtnews/imtnews_id)) from the event.

In Server API, full newsletters with headers and bodies are received in the IMTNewsSink::OnNews event.

[IMTNewsSink](/en/docs/mt5/api/reference_news/imtnewssink)

[HookNews](/en/docs/mt5/api/reference_news/imtnewssink/imtnewssink_hooknews)