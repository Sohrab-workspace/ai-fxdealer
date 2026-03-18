# Orders

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_order

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
                    -   [IMTOrder](/en/docs/mt5/api/reference_trading/trading_order/imtorder)
                    -   [IMTOrderArray](/en/docs/mt5/api/reference_trading/trading_order/imtorderarray)
                    -   [IMTOrderSink](/en/docs/mt5/api/reference_trading/trading_order/imtordersink)
                    -   [IMTHistorySink](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink)
                -   [Deals](/en/docs/mt5/api/reference_trading/trading_deal)
                -   [Positions](/en/docs/mt5/api/reference_trading/trading_position)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)Orders

# Orders

The MetaTrader 5 API allows managing a database of orders on a trade server. Using the API, you can modify and delete orders, as well as handle events of database modifications.

An important feature of working with orders is that they are bound to a certain trade server. Accordingly, an application can manage only those orders that belong to the server to which this application is connected.

The following order interfaces are available:

-   [IMTOrder](/en/docs/mt5/api/reference_trading/trading_order/imtorder)  
    An interface that provides access to all the main parameters of orders.
-   [IMTOrderArray](/en/docs/mt5/api/reference_trading/trading_order/imtorderarray)  
    An interface for working with the arrays of orders.
-   [IMTOrderSink](/en/docs/mt5/api/reference_trading/trading_order/imtordersink)  
    An interface for handling events associated with change of a database of open (active) orders.
-   [IMTHistorySink](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink)  
    An interface for handling events associated with change of a database of closed orders (history of orders).

To help you understand the purpose of interfaces intended for working with orders, the below figure shows their compliance with the elements in MetaTrader 5 Administrator:</t4>

![Working with orders in MetaTrader 5 Administrator](/en/docs/mt5/api/img/orders.png "Working with orders in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [The login of the client who has placed the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_login).
2.  [Ticket of the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_order).
3.  [Type of the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_type).
4.  [The symbol of an order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_symbol).
5.  [The price, at which the order is placed](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_priceorder).
6.  [The Stop Loss level](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_pricesl).
7.  [Comment to an order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_comment).
8.  [Expiration type](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_typetime).
9.  [Activation flags](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_activationflags).
10.  [Time of order placing](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_timesetup).
11.  [Initial volume of the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_volumeinitial).
12.  [Type of filling](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_typefill).
13.  [Order triggering price](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_pricetrigger).
14.  [The Take Profit level](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_pricetp).
15.  [Margin conversion rate](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_ratemargin).
16.  [Expiry time](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_timeexpiration).
17.  [Reason for placing the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_reason).
18.  [Order execution time](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_timedone).
19.  [The current price of the symbol, for which an order has been placed](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_pricecurrent).
20.  [The ID of the order in an external trading system](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_externalid).
21.  [The identifier (magic number) of the Expert Advisor that has placed an order in the client terminal](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_expertid).
22.  [Order state](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_state).
23.  [Unfilled volume of the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_volumecurrent).
24.  [The login of a dealer, who has processed the order](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_dealer).

[Position Accounting System](/en/docs/mt5/api/reference_trading/general_concept/group_position)

[IMTOrder](/en/docs/mt5/api/reference_trading/trading_order/imtorder)