# Positions

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_position

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
                    -   [IMTPosition](/en/docs/mt5/api/reference_trading/trading_position/imtposition)
                    -   [IMTPositionArray](/en/docs/mt5/api/reference_trading/trading_position/imtpositionarray)
                    -   [IMTPositionSink](/en/docs/mt5/api/reference_trading/trading_position/imtpositionsink)
                -   [Accounts](/en/docs/mt5/api/reference_trading/user_account)
                -   [Trade Requests](/en/docs/mt5/api/reference_trading/trading_request)
                -   [Summary Positions](/en/docs/mt5/api/reference_trading/trading_summary)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)Positions

# Positions

The MetaTrader 5 API allows managing a database of positions on a trade server. Using the API, you can modify and delete positions, as well as handle events of changes in the database.

An important feature of working with positions is that they are bound to a certain trade server. Accordingly, an application can manage only those positions that belong to the server to which this application is connected.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">MetaTrader 5 API does not provide options for creating positions. That can lead to irreversible damage of the position database of a server.</span></p></td></tr></tbody></table>

The following position interfaces are available:

-   [IMTPosition](/en/docs/mt5/api/reference_trading/trading_position/imtposition)  
    An interface that provides access to all parameters of trade positions.
-   [IMTPositionArray](/en/docs/mt5/api/reference_trading/trading_position/imtpositionarray)  
    An interface for working with the arrays of positions.
-   [IMTPositionSink](/en/docs/mt5/api/reference_trading/trading_position/imtpositionsink)  
    An interface for handling events associated with change of a database of trade positions.

To help you understand the purpose of interfaces intended for working with positions, the below figure shows their compliance with the elements in MetaTrader 5 Administrator:

![Working with positions in MetaTrader 5 Administrator](/en/docs/mt5/api/img/positions.png "Working with positions in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [The login of the user who has opened the position](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_login).
2.  [Position type](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_action).
3.  [Symbol, for which the position is opened](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_symbol).
4.  [The Stop Loss level](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_pricesl).
5.  [Time of position opening](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_timecreate).
6.  [Position volume](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_volume).
7.  [The weighted average price of a position](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_priceopen).
8.  [The Take Profit level](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_pricetp).
9.  [The current profit/loss of a trade position](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_profit).
10.  [Position swap](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_storage).
11.  [A comment to a position](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_comment).
12.  [The current price of a position](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_pricecurrent).
13.  [The exchange rate of the margin currency to the deposit currency](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_ratemargin).
14.  [The login of a dealer, who has processed the order that opened the position](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_dealer).
15.  [Activation flags](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_activationflags).

[OnDealPerformCloseBy](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealperformcloseby)

[IMTPosition](/en/docs/mt5/api/reference_trading/trading_position/imtposition)