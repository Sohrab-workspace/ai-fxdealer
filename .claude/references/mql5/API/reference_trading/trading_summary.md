# Summary Positions

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_summary

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
                -   [General Principles](/en/docs/mt5/api/reference_trading/general_concept)
                -   [Orders](/en/docs/mt5/api/reference_trading/trading_order)
                -   [Deals](/en/docs/mt5/api/reference_trading/trading_deal)
                -   [Positions](/en/docs/mt5/api/reference_trading/trading_position)
                -   [Accounts](/en/docs/mt5/api/reference_trading/user_account)
                -   [Trade Requests](/en/docs/mt5/api/reference_trading/trading_request)
                -   [Summary Positions](/en/docs/mt5/api/reference_trading/trading_summary)
                    -   [IMTSummary](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary)
                    -   [IMTSummaryArray](/en/docs/mt5/api/reference_trading/trading_summary/imtsummaryarray)
                    -   [IMTSummarySink](/en/docs/mt5/api/reference_trading/trading_summary/imtsummarysink)
                -   [Assets](/en/docs/mt5/api/reference_trading/trading_exposure)
                -   [Daily Reports](/en/docs/mt5/api/reference_trading/trading_daily)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)Summary Positions

# Summary Positions

The MetaTrader 5 API allows receiving information about clients' summary positions, as well as summary hedging positions.

An important feature of working with summary positions is that they are bound to a certain trade server. Therefore, the application can only receive information about summary positions on the server to which this application is connected.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Hedging positions apply to all accounts in coverage* groups.</span></p></td></tr></tbody></table>

The following summary position interfaces are available:

-   [IMTSummary](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary)  
    An interface describing the summary position record of one symbol.
-   [IMTSummaryArray](/en/docs/mt5/api/reference_trading/trading_summary/imtsummaryarray)  
    An interface for working with the arrays of summary position records.
-   [IMTSummarySink](/en/docs/mt5/api/reference_trading/trading_summary/imtsummarysink)  
    An interface for handling events associated with changes in summary positions.

To help you understand the purpose of interfaces intended for working with positions, the below figure shows their compliance with the elements in the MetaTrader 5 Manager:

![Summary positions in the MetaTrader 5 Manager](/en/docs/mt5/api/img/summary.png "Summary positions in the MetaTrader 5 Manager")

The following elements are shown above:

1.  Symbol.
2.  The number of [client](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_positionclients) and [hedging](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_positioncoverage) positions.
3.  The volume of [client](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_volumebuyclients) and [hedging](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_volumebuycoverage) Buy positions.
4.  The weighted average price of [client](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_pricebuyclients) and [hedging](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_pricebuycoverage) Sell positions.
5.  The volume of [client](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_volumesellclients) and [hedging](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_volumesellcoverage) Buy positions.
6.  The weighted average price of [client](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_pricesellclients) and [hedging](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_pricesellcoverage) Sell positions.
7.  The [difference](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_volumenet) between the volumes of client Buy and Sell positions.
8.  The total profit (loss) of [client](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_profitclients) and [hedging](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_profitcoverage) positions.
9.  The [difference between total profits](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary/imtsummary_profituncovered) (losses) of client and hedging positions.

[ExternalRetcode](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_externalretcode)

[IMTSummary](/en/docs/mt5/api/reference_trading/trading_summary/imtsummary)