# IMTTickSink::OnTickStat

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_ticks/imtticksink/imtticksink_ontickstat

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
            -   [Trade](/en/docs/mt5/api/reference_trading)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
                -   [IMTTickSink](/en/docs/mt5/api/reference_ticks/imtticksink)
                    -   [OnTick](/en/docs/mt5/api/reference_ticks/imtticksink/imtticksink_ontick)
                    -   [OnTickStat](/en/docs/mt5/api/reference_ticks/imtticksink/imtticksink_ontickstat)
                    -   [HookTick](/en/docs/mt5/api/reference_ticks/imtticksink/imtticksink_hooktick)
                    -   [HookTickStat](/en/docs/mt5/api/reference_ticks/imtticksink/imtticksink_hooktickstat)
                -   [IMTChartSink](/en/docs/mt5/api/reference_ticks/imtchartsink)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Price Data](/en/docs/mt5/api/reference_ticks)[IMTTickSink](/en/docs/mt5/api/reference_ticks/imtticksink)OnTickStat

# IMTTickSink::OnTickStat

A handler of the event of update of the statistical information about a price.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTTickSink::OnTickStat</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;MTTickStat&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tstat</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;reference&nbsp;to&nbsp;a&nbsp;structure&nbsp;of&nbsp;the&nbsp;description&nbsp;of&nbsp;statical&nbsp;information</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTTickSink.OnTickStat</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickStat</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tstat</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;structure&nbsp;of&nbsp;the&nbsp;description&nbsp;of&nbsp;statical&nbsp;information</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

tstat

\[in\]  A reference to the structure that describes statistical price information ([MTTickStat](/en/docs/mt5/api/mttickstat)).

Note

The event is called after information is saved in the database for this symbol. This means that the statistical information has been received from the current data feed used for the symbol in accordance with the priority (as determined by the position of the data source (gateway/data feed) in the configuration list) and has passed all checks for correctness.

In Manager API, the event is only called for the symbols which have been added to the [list of selected symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected).

# IMTTickSink::OnTickStat

A handler of the event of update of the statistical price information with the specification of a data source.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTTickSink::OnTickStat</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;int</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">feeder</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;index&nbsp;of&nbsp;the&nbsp;data&nbsp;feed</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;MTTickStat&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tstat</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;reference&nbsp;to&nbsp;a&nbsp;structure&nbsp;of&nbsp;the&nbsp;description&nbsp;of&nbsp;statical&nbsp;information</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTTickSink.OnTickStat</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">int</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">feeder</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;index&nbsp;of&nbsp;the&nbsp;data&nbsp;feed</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTTickStat</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">tstat</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;structure&nbsp;of&nbsp;the&nbsp;description&nbsp;of&nbsp;statical&nbsp;information</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

feeder

\[in\]  The index of the data source, from which statical information is received.

tstat

\[in\]  A reference to the structure that describes statistical price information ([MTTickStat](/en/docs/mt5/api/mttickstat)).

Note

This method is used only in the MetaTrader 5 Server API and is called only on the history servers.

The event is called after information is saved in the database for this symbol. This means that the statistical information has been received from the current data feed used for the symbol in accordance with the priority (as determined by the position of the data source (gateway/data feed) in the configuration list) and has passed all checks for correctness.

## Identifying the data source based on the feeder index

The type of the data source, from which the information has been received, is determined in accordance with the constants defined in the [EnMTFeederConstants](/en/docs/mt5/api/mttick#enmtfeederconstants) enumeration:

-   The MT\_FEEDER\_DEALER (-1) value means that the information was added manually through a manager terminal or API.
-   A value from 0 to 63 (MT\_FEEDER\_OFFSET - 1) means that the information was received from a gateway.
-   A value of 64 (MT\_FEEDER\_OFFSET) or greater means that the information was received from a data feed.

After determining the type of data source ([gateway](/en/docs/mt5/api/config_gateway) or [data feed](/en/docs/mt5/api/config_datafeeds)), we can analyze a certain value. The index corresponds to the position of the data feed/gateway, from which the information was received, in the list of configurations at the time of tick arrival. For example, index 0 means that the information was received from the first gateway in the list of gateway configurations. Value of 65 means that the information was received from the second data feed in the list of data feed configurations.

[OnTick](/en/docs/mt5/api/reference_ticks/imtticksink/imtticksink_ontick)

[HookTick](/en/docs/mt5/api/reference_ticks/imtticksink/imtticksink_hooktick)