# Return Codes

> Source: https://support.metaquotes.net/en/docs/mt4/api/reference_retcodes

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
            -   [Successful completion](/en/docs/mt4/api/reference_retcodes/retcodes_successful)
            -   [Common errors](/en/docs/mt4/api/reference_retcodes/retcodes_common)
            -   [Account State](/en/docs/mt4/api/reference_retcodes/retcodes_account)
            -   [Trade Requests](/en/docs/mt4/api/reference_retcodes/retcodes_trade_request)
        -   [Server API](/en/docs/mt4/api/server_api)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)Return Codes

# Return Codes

The most of functions in the MetaTrader 4 API return a special code to notify of the results of their execution. To develop high-quality, stable software, the programmer should check the codes returned by the API method functions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Group of codes</span></p></th><th class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Range of values</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_retcodes/retcodes_successful" class="topiclink">Successful completion</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">0-1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned with the successful completion of an operation.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_retcodes/retcodes_common" class="topiclink">Common errors</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">2-63</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned when common errors occur.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_retcodes/retcodes_account" class="topiclink">Account State</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">64-127</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned when working with client records.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_retcodes/retcodes_trade_request" class="topiclink">Trade Requests</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">&gt;=128</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned when processing trade requests.</span></p></td></tr></tbody></table>

[TradeRestoreResult](/en/docs/mt4/api/reference_structures/structure_auxiliary/traderestoreresult)

[Successful completion](/en/docs/mt4/api/reference_retcodes/retcodes_successful)