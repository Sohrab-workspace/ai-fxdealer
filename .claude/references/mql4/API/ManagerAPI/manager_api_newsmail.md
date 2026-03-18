# Mail, News and Notifications

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_newsmail

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
        -   [Manager API](/en/docs/mt4/api/manager_api)
            -   [Application Development](/en/docs/mt4/api/manager_api/manager_api_dev)
            -   [Exported Functions and Factory](/en/docs/mt4/api/manager_api/manager_api_exported_factory)
            -   [Common Functions](/en/docs/mt4/api/manager_api/manager_api_common)
            -   [Connecting to the Server](/en/docs/mt4/api/manager_api/manager_api_connect)
            -   [Configuration Databases](/en/docs/mt4/api/manager_api/manager_api_config)
            -   [Server Management](/en/docs/mt4/api/manager_api/manager_api_server)
            -   [Price Data](/en/docs/mt4/api/manager_api/manager_api_chart)
            -   [Data Feeds](/en/docs/mt4/api/manager_api/manager_api_feeder)
            -   [Backup](/en/docs/mt4/api/manager_api/manager_api_backup)
            -   [Trading](/en/docs/mt4/api/manager_api/manager_api_trade)
            -   [Dealings](/en/docs/mt4/api/manager_api/manager_api_dealer)
            -   [Users](/en/docs/mt4/api/manager_api/manager_api_user)
            -   [Online Connections](/en/docs/mt4/api/manager_api/manager_api_online)
            -   [Symbols](/en/docs/mt4/api/manager_api/manager_api_symbol)
            -   [Mail, News and Notifications](/en/docs/mt4/api/manager_api/manager_api_newsmail)
                -   [MailSend](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_mailsend)
                -   [MailsRequest](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_mailsrequest)
                -   [MailLast](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_maillast)
                -   [NewsSend](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newssend)
                -   [NewsGet](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsget)
                -   [NewsTotal](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newstotal)
                -   [NewsTopicGet](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newstopicget)
                -   [NewsBodyRequest](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsbodyrequest)
                -   [NewsBodyGet](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsbodyget)
                -   [NotificationsSend](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_notificationssend)
            -   [Reports](/en/docs/mt4/api/manager_api/manager_api_report)
            -   [Summary Positions](/en/docs/mt4/api/manager_api/manager_api_summary)
            -   [Exposure](/en/docs/mt4/api/manager_api/manager_api_exposure)
            -   [Protocol Extension](/en/docs/mt4/api/manager_api/manager_api_extension)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Mail, News and Notifications

# Mail, News and Notifications

The MetaTrader 4 Manager API provides functions for working with internal mails and the news system in the platform. It also provides the possibility to send messages to clients' mobiles using MetaQuotes ID.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_mailsend" class="topiclink">MailSend</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sends an email via the internal mail system.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_mailsrequest" class="topiclink">MailsRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives emails from the internal mailing system of the platform.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_maillast" class="topiclink">MailLast</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives information about the last received email.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newssend" class="topiclink">NewsSend</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sends a newsletter to the news stream.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsget" class="topiclink">NewsGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives keys of all news.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newstotal" class="topiclink">NewsTotal</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets the total number of news received by the manager interface from the trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newstopicget" class="topiclink">NewsTopicGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets news headers by the index.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsbodyrequest" class="topiclink">NewsBodyRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Requests news body from a trade server by a key.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsbodyget" class="topiclink">NewsBodyGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets the news body using a key in pumping.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_notificationssend" class="topiclink">NotificationsSend</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sends push notifications to a list of MetaQuotes IDs and a list of logins.</span></p></td></tr></tbody></table>

[SymbolsGroupsGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgroupsget)

[MailSend](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_mailsend)