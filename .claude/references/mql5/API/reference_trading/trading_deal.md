# Deals

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_deal

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
                    -   [IMTDeal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal)
                    -   [IMTDealArray](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray)
                    -   [IMTDealSink](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)Deals

# Deals

The MetaTrader 5 API allows managing a database of deals on a trade server. Using the Manager API, you can modify and delete deals, as well as handle events of changes in the database of deals.

An important feature of working with deals is that they are bound to a certain trade server. Accordingly, an application can manage only those deals that belong to the server to which this application is connected.

The following deal interfaces are available:

-   [IMTDeal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal)  
    An interface that provides access to all the main parameters of deals.
-   [IMTDealArray](/en/docs/mt5/api/reference_trading/trading_deal/imtdealarray)  
    An interface for working with the arrays of deals.
-   [IMTDealSink](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink)  
    An interface for handling events associated with changes in the database of deals.

To help you understand the purpose of the interfaces intended for working with deals, the below figure shows their compliance with the elements in MetaTrader 5 Administrator:</t4>

![Working with deals in MetaTrader 5 Administrator](/en/docs/mt5/api/img/deals.png "Working with deals in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [The login of a client who has executed a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_login).
2.  [The ticket of a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_deal).
3.  [Type of action](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_action) and [direction](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_entry) of a deal.
4.  [The symbol, for which a deal is executed](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_symbol).
5.  [The reason for deal execution](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_reason).
6.  [The ticket of the order, as a result of which a deal was executed](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_order).
7.  [Time of a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_time).
8.  [Volume of a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_volume).
9.  [Price of a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_price).
10.  [The identifier (magic number) of the Expert Advisor that has performed the trade in the client terminal.](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_expertid)
11.  [Commission from a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_commission).
12.  [Swap size](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_storage).
13.  [The amount of profit/loss of a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_profit).
14.  [The price of the position that was closed by this deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_priceposition);
15.  [The profit/loss from a deal in the symbol profit currency](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_profitraw);
16.  [Comment to a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_comment).
17.  [The ID of a deal in an external trading system](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_externalid).
18.  [The login of a dealer, who has processed a deal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_dealer).
19.  [Profit ratio](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_rateprofit).
20.  [Margin ratio](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_ratemargin).

[OnHistorySync](/en/docs/mt5/api/reference_trading/trading_order/imthistorysink/imthistorysink_onhistorysync)

[IMTDeal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal)