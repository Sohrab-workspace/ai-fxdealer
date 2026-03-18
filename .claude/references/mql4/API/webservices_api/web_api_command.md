# Commands

> Source: https://support.metaquotes.net/en/docs/mt4/api/webservices_api/web_api_command

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
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
            -   [Operation Principles](/en/docs/mt4/api/webservices_api/web_api_dev)
            -   [Example: Quotes on a Website](/en/docs/mt4/api/webservices_api/web_api_example)
            -   [Commands](/en/docs/mt4/api/webservices_api/web_api_command)
                -   [INFO](/en/docs/mt4/api/webservices_api/web_api_command/web_info)
                -   [QUIT](/en/docs/mt4/api/webservices_api/web_api_command/web_quit)
                -   [WAPUSER](/en/docs/mt4/api/webservices_api/web_api_command/web_wapuser)
                -   [WAPQUOTES](/en/docs/mt4/api/webservices_api/web_api_command/web_wapquotes)
                -   [QUOTES](/en/docs/mt4/api/webservices_api/web_api_command/web_quotes)
                -   [HISTORYNEW](/en/docs/mt4/api/webservices_api/web_api_command/web_historynew)
                -   [USERINFO](/en/docs/mt4/api/webservices_api/web_api_command/web_userinfo)
                -   [USERHISTORY](/en/docs/mt4/api/webservices_api/web_api_command/web_userhistory)
                -   [CONTESTTOP](/en/docs/mt4/api/webservices_api/web_api_command/web_contesttop)
                -   [CONTESTACCOUNT](/en/docs/mt4/api/webservices_api/web_api_command/web_contestaccount)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[WebServices API](/en/docs/mt4/api/webservices_api)Commands

# Commands

The following commands are provided in the MetaTrader 4 WebServices API:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Command</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_info" class="topiclink">INFO</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Getting the server description.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_quit" class="topiclink">QUIT</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Completing operation with a trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_wapuser" class="topiclink">WAPUSER</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Getting information about the user's account state and orders. It can be used for user authentication.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_wapquotes" class="topiclink">WAPQUOTES</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Getting quotes for a list of symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_quotes" class="topiclink">QUOTES</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Getting quotes for a list of symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_historynew" class="topiclink">HISTORYNEW</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Getting the price history over a specified period for a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_userinfo" class="topiclink">USERINFO</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Getting information about the user's account state, open and pending orders.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_userhistory" class="topiclink">USERHISTORY</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Receiving the history of trade operations for the specified period of time.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_contesttop" class="topiclink">CONTESTTOP</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Getting a list of the top positions of the contest.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/webservices_api/web_api_command/web_contestaccount" class="topiclink">CONTESTACCOUNT</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Registration of contest participant and opening a contest account for the user.</span></p></td></tr></tbody></table>

[Example: Quotes on a Website](/en/docs/mt4/api/webservices_api/web_api_example)

[INFO](/en/docs/mt4/api/webservices_api/web_api_command/web_info)