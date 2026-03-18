# Profiler

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/interface/toolbox/toolbox_profiler

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
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

# Profiler

The application source code [profiling](/en/docs/mt5/metaeditor/development/profiling) results are displayed on this tab. Profiling allows to optimize a source code by finding the slowest fragments in it.

![Profiling results](/en/docs/mt5/metaeditor/img/toolbox_profiler.png "Profiling results")

Find detailed instructions on profiling in a [separate section](/en/docs/mt5/metaeditor/development/profiling).

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">This tab is not displayed before profiling launch using "<img class="help" alt="Start profiling" title="Start profiling" width="15" height="12" src="/en/docs/mt5/metaeditor/img/start_profiling_icon.png"> Start profiling" command in the <a href="/en/docs/mt5/metaeditor/interface/main_menu/main_menu_debug" class="topiclink">"Debug"</a> menu or on the <a href="/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard" class="topiclink">"Standard"</a> toolbar.</span></p></td></tr></tbody></table>

## Context menu

The following commands are available in the context menu:

-   Open — move to a line or a function in a source code file. The same action can be executed by double clicking or pressing Enter.
-   Expand All — expand all collapsed functions;
-   Collapse All — collapse all expanded functions;
-   Functions by Lines — switch to viewing profiling results [by lines](/en/docs/mt5/metaeditor/development/profiling#lines);
-   Functions by Calls — switch to viewing profiling results [by calls](/en/docs/mt5/metaeditor/development/profiling#calls);
-   Export — export profiling results in Open XML (MS Office Excel), HTML (Internet Explorer) or CSV (Text file).
-   Auto Arrange — enable/disable automatic sizing of fields. The same action can be done by pressing "A";
-   Grid — show/hide grid to separate fields. The same action can be done by pressing "G".