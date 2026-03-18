# Export of Quotes

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/service/dde

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
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
            -   [Configuration at Startup](/en/docs/mt4/terminal/service/start_conf_file)
            -   [History Center](/en/docs/mt4/terminal/service/history_center)
            -   [Export of Quotes](/en/docs/mt4/terminal/service/dde)
            -   [Global Variables](/en/docs/mt4/terminal/service/global_variables)
            -   [Contract Specification](/en/docs/mt4/terminal/service/symbol_spec)
            -   [Languages Support](/en/docs/mt4/terminal/service/languages_support)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Tools](/en/docs/mt4/terminal/service)Export of Quotes

# Export of Quotes

Source data serving as a basis for the entire analytical work of the terminal user are those about security price changes. This information is provided by the brokerage company. Price data allow to draw symbol charts, research in financial markets, use various trading tactics, and make trade decisions. Quotes represent files with records in format of "SYMBOL, BID, ASK, DATE" (security symbol, bid price, ask price, date and time) and income in the terminal automatically as soon as connection to the server has been established.

The terminal allows to export the current quotes to other programs in the real-time mode through "DDE" (Dynamic Data Exchange) protocol. This is a protocol of operational systems of MS Windows used for dynamic data exchange among various applications. Quotes are given through DDE only at incoming of new ticks (ADVISE mode), but not immediately on request (REQUEST mode) where the latest price is shown. N/A is shown on the first REQUEST, and after the new price has been income, quotes will appear.

To activate the export of quotes from the terminal through DDE, one has to enable the "Enable DDE server" option in the [terminal settings](/en/docs/mt4/terminal/setup/setup_server).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: History Data cannot be exported through DDE protocol. The current quotes are exported only when the client terminal is online.</span></p></td></tr></tbody></table>

DDE request formats and their possible results by the example of "DDE-sample.xls" file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;BID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;request:&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;MT4|BID!USDCHF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result:&nbsp;&nbsp;1.5773</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;ASK&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;request:&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;MT4|ASK!USDCHF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result:&nbsp;&nbsp;1.5778</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;HIGH&nbsp;&nbsp;&nbsp;&nbsp;request:&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;MT4|HIGH!USDCHF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result:&nbsp;&nbsp;1.5801</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;LOW&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;request:&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;MT4|LOW!USDCHF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result:&nbsp;&nbsp;1.5741</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;TIME&nbsp;&nbsp;&nbsp;&nbsp;request:&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;MT4|TIME!USDCHF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result:&nbsp;&nbsp;21.05.02&nbsp;9:52</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;TIMESEC&nbsp;request:&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;MT4|TIME!USDCHF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result:&nbsp;&nbsp;21.05.02&nbsp;9:52:43</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;QUOTE&nbsp;&nbsp;&nbsp;request:&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;MT4|QUOTE!USDCHF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result:&nbsp;&nbsp;21.05.02&nbsp;9:52:43&nbsp;1.5773&nbsp;1.5778&nbsp;1.5776</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: For data to be shown properly in MS Excel, one has to enable "Tools — Options... — Translation — Translation formula entry" menu option of MS Excel.</span></p></td></tr></tbody></table>

[History Center](/en/docs/mt4/terminal/service/history_center)

[Global Variables](/en/docs/mt4/terminal/service/global_variables)