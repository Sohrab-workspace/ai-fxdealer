# Auxiliary Functions

> Source: https://support.metaquotes.net/en/docs/mt4/api/report_api/report_api_auxiliary

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
            -   [Auxiliary Functions](/en/docs/mt4/api/report_api/report_api_auxiliary)
                -   [UserRecordGet](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_userrecordget)
                -   [SymbolGet](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_symbolget)
                -   [GroupGet](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_groupget)
                -   [GetCmd](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_getcmd)
                -   [Decimals](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_decimals)
                -   [ToSym](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tosym)
                -   [ToSymExt](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tosymext)
                -   [ToMoney](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tomoney)
                -   [ToVolume](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tovolume)
                -   [NormalizeDouble](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_normalizedouble)
                -   [FormatDateTime](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_formatdatetime)
                -   [FormatOrderReason](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_formatorderreason)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Report API](/en/docs/mt4/api/report_api)Auxiliary Functions

# Auxiliary Functions

The functions described in this section are not actually part of Report API. It is implemented in order to facilitate routine operations when generating reports. The description and implementation of these functions is available in report examples files ReportsPLugin.cpp and ReportsPLugin.h in \[Manager terminal installation directory\]\\Reports\\ReportAPI.zip. If you want to use the functions, copy these files and include them into your project.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_userrecordget" class="topiclink">UserRecordGet</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Receives the description of the client account with the specified login.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_symbolget" class="topiclink">SymbolGet</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Receives symbol description by its name.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_groupget" class="topiclink">GroupGet</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Receives group description by its name.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_getcmd" class="topiclink">GetCmd</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Receives a text description of a trade operation by the type of a trading command.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_decimals" class="topiclink">Decimals</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Gets a multiplier to convert the floating-point number to an integer by the number of decimal places in this number.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tosym" class="topiclink">ToSym</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Converts a floating point number (price) to a string. Used for outputting prices in reports.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tosymext" class="topiclink">ToSymExt</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Converts a floating point number (price) to a string, while truncating zeros in the decimal part of the number. Used for outputting prices in reports.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tomoney" class="topiclink">ToMoney</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Converts a floating point number (price) to a string while controlling the string length. Used for outputting monetary units in reports.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_tovolume" class="topiclink">ToVolume</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Converts a floating point number (price) to a string. Used for outputting operation volume (in lots) in reports.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_normalizedouble" class="topiclink">NormalizeDouble</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Rounds a floating-point number to a specified precision.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_formatdatetime" class="topiclink">FormatDateTime</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Converts a UNIX time to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_formatorderreason" class="topiclink">FormatOrderReason</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Receives a text description of a trade operation reason by type.</span></p></td></tr></tbody></table>

[WriteHeader](/en/docs/mt4/api/report_api/report_api_creport/creport_writeheader)

[UserRecordGet](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_userrecordget)