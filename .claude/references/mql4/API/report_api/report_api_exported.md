# Exported Functions

> Source: https://support.metaquotes.net/en/docs/mt4/api/report_api/report_api_exported

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
            -   [Development of Reports](/en/docs/mt4/api/report_api/report_api_dev)
            -   [Exported Functions](/en/docs/mt4/api/report_api/report_api_exported)
                -   [RepGetVersion](/en/docs/mt4/api/report_api/report_api_exported/repgetversion)
                -   [RepGetModuleInfo](/en/docs/mt4/api/report_api/report_api_exported/repgetmoduleinfo)
                -   [RepGetGeneratorInfo](/en/docs/mt4/api/report_api/report_api_exported/repgetgeneratorinfo)
                -   [RepGenerateReport](/en/docs/mt4/api/report_api/report_api_exported/repgeneratereport)
            -   [CReport Methods](/en/docs/mt4/api/report_api/report_api_creport)
            -   [Auxiliary Functions](/en/docs/mt4/api/report_api/report_api_auxiliary)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Report API](/en/docs/mt4/api/report_api)Exported Functions

# Exported Functions

Each library of reports must export four functions that will be called by the manager terminal.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_exported/repgetversion" class="topiclink">RepGetVersion</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Returns the version of the library of reports.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_exported/repgetmoduleinfo" class="topiclink">RepGetModuleInfo</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Requests a text description of the report.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_exported/repgetgeneratorinfo" class="topiclink">RepGetGeneratorInfo</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Returns report description by the index.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_exported/repgeneratereport" class="topiclink">RepGenerateReport</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Launching the report generation.</span></p></td></tr></tbody></table>

[Development of Reports](/en/docs/mt4/api/report_api/report_api_dev)

[RepGetVersion](/en/docs/mt4/api/report_api/report_api_exported/repgetversion)