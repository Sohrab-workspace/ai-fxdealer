# Mail, News and Notifications

> Source: https://support.metaquotes.net/en/docs/mt4/api/server_api/server_api_mail_news

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
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
            -   [Development of Plugins](/en/docs/mt4/api/server_api/server_api_dev)
            -   [Common Functions](/en/docs/mt4/api/server_api/server_api_common)
            -   [Configuration Databases](/en/docs/mt4/api/server_api/server_api_config)
            -   [Users](/en/docs/mt4/api/server_api/server_api_user)
            -   [Trading](/en/docs/mt4/api/server_api/server_api_trading)
            -   [Price Data](/en/docs/mt4/api/server_api/server_api_chart)
            -   [Mail, News and Notifications](/en/docs/mt4/api/server_api/server_api_mail_news)
                -   [MailSend](/en/docs/mt4/api/server_api/server_api_mail_news/cserverinterface_mailsend)
                -   [NewsSend](/en/docs/mt4/api/server_api/server_api_mail_news/cserverinterface_newssend)
                -   [NotificationsSend](/en/docs/mt4/api/server_api/server_api_mail_news/cserverinterface_notificationssend)
            -   [Daily Reports](/en/docs/mt4/api/server_api/server_api_reference_daily)
            -   [Server Services](/en/docs/mt4/api/server_api/server_api_server_services)
            -   [Hooks](/en/docs/mt4/api/server_api/server_api_hook)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Server API](/en/docs/mt4/api/server_api)Mail, News and Notifications

# Mail, News and Notifications

The MetaTrader 4 Server API contains functions for working with internal mails and the news system in the platform. It also provides the possibility to send messages to clients' mobiles using MetaQuotes ID.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_mail_news/cserverinterface_mailsend" class="topiclink">MailSend</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sends an email via the internal mail system.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_mail_news/cserverinterface_newssend" class="topiclink">NewsSend</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sends a newsletter to the news stream.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_mail_news/cserverinterface_notificationssend" class="topiclink">NotificationsSend</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sends push notifications to mobile devices.</span></p></td></tr></tbody></table>

[HistoryTicksGet](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyticksget)

[MailSend](/en/docs/mt4/api/server_api/server_api_mail_news/cserverinterface_mailsend)