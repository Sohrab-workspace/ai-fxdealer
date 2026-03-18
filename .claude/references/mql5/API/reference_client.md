# Clients

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_client

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
                -   [IMTClient](/en/docs/mt5/api/reference_client/imtclient)
                -   [IMTClientArray](/en/docs/mt5/api/reference_client/imtclientarray)
                -   [IMTClientSink](/en/docs/mt5/api/reference_client/imtclientsink)
                -   [IMTComment](/en/docs/mt5/api/reference_client/imtcomment)
                -   [IMTCommentArray](/en/docs/mt5/api/reference_client/imtcommentarray)
                -   [IMTCommentSink](/en/docs/mt5/api/reference_client/imtcommentsink)
                -   [IMTDocument](/en/docs/mt5/api/reference_client/imtdocument)
                -   [IMTDocumentArray](/en/docs/mt5/api/reference_client/imtdocumentarray)
                -   [IMTDocumentSink](/en/docs/mt5/api/reference_client/imtdocumentsink)
                -   [IMTAttachment](/en/docs/mt5/api/reference_client/imtattachment)
                -   [IMTAttachmentArray](/en/docs/mt5/api/reference_client/imtattachmentarray)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)Clients

# Clients

The MetaTrader 5 Server API allows managing a client database on a trade server. Using the server API, you can add or remove records, edit data and handle database change events. Use the API to expand the standard functionality of client management system in the platform, or to integrate it with external CRM systems.

A detailed description of operations with clients is provided in the [MetaTrader 5 Administrator documentation](https://support.metaquotes.net/en/docs/mt5/platform/administration/clients).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The client database is maintained separately for each trading server in the cluster. This includes the client database and separate auxiliary databases of comments, documents and attachments. The plugin can only manage those clients that belong to <a href="/en/docs/mt5/api/serverapi_configure_plugin" class="topiclink">the server, on which the plugin is running</a>.</span></p></td></tr></tbody></table>

Operations with the clients are implemented via several interfaces which provide access to all client data and to additional database access possibilities:

-   [IMTClient](/en/docs/mt5/api/reference_client/imtclient) — full description of a client.
-   [IMTClientArray](/en/docs/mt5/api/reference_client/imtclientarray) — methods for efficient operations with client arrays.
-   [IMTClientSink](/en/docs/mt5/api/reference_client/imtclientsink) — handlers of client database change events.
-   [IMTComment](/en/docs/mt5/api/reference_client/imtcomment) — description of comments which can be added to clients and their documents.
-   [IMTCommentArray](/en/docs/mt5/api/reference_client/imtcommentarray) — methods for efficient operations with comment arrays.
-   [IMTCommentSink](/en/docs/mt5/api/reference_client/imtcommentsink) — handlers of comment database change events.
-   [IMTDocument](/en/docs/mt5/api/reference_client/imtdocument) — description of client documents.
-   [IMTDocumentArray](/en/docs/mt5/api/reference_client/imtdocumentarray) — methods for efficient operations with document arrays.
-   [IMTDocumentSink](/en/docs/mt5/api/reference_client/imtdocumentsink) — handlers of document database changes events.
-   [IMTAttachment](/en/docs/mt5/api/reference_client/imtattachment) — description of attachments used in documents and client comments.
-   [IMTAttachmentArray](/en/docs/mt5/api/reference_client/imtattachmentarray) — methods for efficient operations with attachment arrays.

[OnDailySync](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailysync)

[IMTClient](/en/docs/mt5/api/reference_client/imtclient)