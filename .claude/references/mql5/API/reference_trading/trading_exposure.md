# Assets

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_exposure

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
                -   [Assets](/en/docs/mt5/api/reference_trading/trading_exposure)
                    -   [IMTExposure](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure)
                    -   [IMTExposureArray](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposurearray)
                    -   [IMTExposureSink](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposuresink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)Assets

# Assets

The MetaTrader 5 API allows receiving information about clients' exposure and company's hedged assets.

An important feature of working with assets is that they are bound to a certain trade server. Therefore, the application can only receive information about the exposure of client and coverage\* account groups on the server to which this application is connected.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Hedging positions apply to all accounts in coverage* groups.</span></p></td></tr></tbody></table>

The following exposure interfaces are available:

-   [IMTExposure](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure)  
    An interface describing the record of one asset.
-   [IMTExposureArray](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposurearray)  
    An interface for working with the arrays of asset records.
-   [IMTExposureSink](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposuresink)  
    An interface for handling events associated with exposure modification.

To help you understand the purpose of interfaces intended for working with exposure, the below figure shows their compliance with the elements in MetaTrader 5 Manager:

![Exposure in MetaTrader 5 Manager](/en/docs/mt5/api/img/exposure.png "Exposure in MetaTrader 5 Manager")

The following elements are shown above:

1.  [Asset name](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure/imtexposure_symbol).
2.  [The volume of client assets](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure/imtexposure_volumeclients).
3.  [The volume of coverage assets](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure/imtexposure_volumecoverage).
4.  [Conversion rate](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure/imtexposure_pricerate) of as asset to a selected currency.
5.  [Net total](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure/imtexposure_volumenet) of assets in the selected currency.

[OnSummaryUpdate](/en/docs/mt5/api/reference_trading/trading_summary/imtsummarysink/imtsummarysink_onsummaryupdate)

[IMTExposure](/en/docs/mt5/api/reference_trading/trading_exposure/imtexposure)