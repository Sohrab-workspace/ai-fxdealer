# CReport Methods

> Source: https://support.metaquotes.net/en/docs/mt4/api/report_api/report_api_creport

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
            -   [CReport Methods](/en/docs/mt4/api/report_api/report_api_creport)
                -   [Report](/en/docs/mt4/api/report_api/report_api_creport/creport_report)
                -   [GenerateHTML](/en/docs/mt4/api/report_api/report_api_creport/creport_generatehtml)
                -   [GenerateCSV](/en/docs/mt4/api/report_api/report_api_creport/creport_generatecsv)
                -   [GetInfo](/en/docs/mt4/api/report_api/report_api_creport/creport_getinfo)
                -   [Total](/en/docs/mt4/api/report_api/report_api_creport/creport_total)
                -   [Startup](/en/docs/mt4/api/report_api/report_api_creport/creport_startup)
                -   [WriteHeader](/en/docs/mt4/api/report_api/report_api_creport/creport_writeheader)
            -   [Auxiliary Functions](/en/docs/mt4/api/report_api/report_api_auxiliary)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Report API](/en/docs/mt4/api/report_api)CReport Methods

# CReport Methods

The CReport is not actually part of Report API. It has been additionally implemented as a report development example. The description and implementation of CReport is available in report example files Report.cpp and Report.h \[Manager terminal installation directory\]\\Reports\\ReportAPI.zip. If you want to use CReport, copy these files and include them into your project.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_creport/creport_report" class="topiclink">Report</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Calls the report generation by index in the HTML or CSV format.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_creport/creport_generatehtml" class="topiclink">GenerateHTML</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">The virtual method of report generation in the HTML format.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_creport/creport_generatecsv" class="topiclink">GenerateCSV</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">The virtual method of report generation in the CSV format.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_creport/creport_getinfo" class="topiclink">GetInfo</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Gets a report description by the index.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_creport/creport_total" class="topiclink">Total</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Gets the total number of reports in a DLL.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_creport/creport_startup" class="topiclink">Startup</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Checks the report parameters and opens the file of the generated report.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_creport/creport_writeheader" class="topiclink">WriteHeader</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Writes to a HTML file the header and styles required for a correct display of values when the report is opened.</span></p></td></tr></tbody></table>

[RepGenerateReport](/en/docs/mt4/api/report_api/report_api_exported/repgeneratereport)

[Report](/en/docs/mt4/api/report_api/report_api_creport/creport_report)