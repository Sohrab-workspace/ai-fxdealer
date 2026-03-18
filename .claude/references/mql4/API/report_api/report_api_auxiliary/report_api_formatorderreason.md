# FormatOrderReason

> Source: https://support.metaquotes.net/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_formatorderreason

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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Report API](/en/docs/mt4/api/report_api)[Auxiliary Functions](/en/docs/mt4/api/report_api/report_api_auxiliary)FormatOrderReason

# FormatOrderReason

Receives a text description of a trade operation reason by type.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">LPSTR&nbsp;&nbsp;</span><span class="f_Functions">ToMoney</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">char&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">reason</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reason</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">char*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">sz</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Buffer</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">maxchars</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Maximum&nbsp;string&nbsp;length</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

reason

\[in\]  Reason for a trade operation. Corresponds to [TradeRecord::reason](/en/docs/mt4/api/reference_structures/structure_trade/traderecord).

sz

\[in\]  A pointer to the buffer to which the resulting string will be added. It is used for intermediate calculations.

maxchars

\[in\]  The maximum length of the resulting string.

Return Value

If successful, it returns the description of the reasons for the operation as a string. In case of failure, it returns NULL.

[FormatDateTime](/en/docs/mt4/api/report_api/report_api_auxiliary/report_api_formatdatetime)

[WebServices API](/en/docs/mt4/api/webservices_api)