# General Principles

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/general_concept

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
                    -   [Types of Orders](/en/docs/mt5/api/reference_trading/general_concept/order_types)
                    -   [Types of Execution](/en/docs/mt5/api/reference_trading/general_concept/execution_types)
                    -   [State of Orders](/en/docs/mt5/api/reference_trading/general_concept/order_state)
                    -   [Fill Policy](/en/docs/mt5/api/reference_trading/general_concept/fill_policy)
                    -   [Position Accounting System](/en/docs/mt5/api/reference_trading/general_concept/group_position)
                -   [Orders](/en/docs/mt5/api/reference_trading/trading_order)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)General Principles

# General Principles

Before you begin to study trading functions of the Server API, you must have a clear understanding of the basic terms: [order](/en/docs/mt5/api/reference_trading/trading_order), [deal](/en/docs/mt5/api/reference_trading/trading_deal) and [position](/en/docs/mt5/api/reference_trading/trading_position).

-   Order  
    An order is an instruction for a broker to buy or sell a financial instrument. There are two main [types of orders](/en/docs/mt5/api/reference_trading/general_concept/order_types): market and pending. In addition, there are special Take Profit and Stop Loss orders.
-   Deal  
    A Deal is a fact of buying or selling a symbol. Buying is executed at the demand price (Ask), and Sell is performed at the supply price (Bid). A deal can be opened as a result of execution of a market order or triggering of a pending order. Keep in mind that in some cases, execution of an order can result in several deals.
-   Position  
    A position is a market obligation, i.e. the number of bought or sold contracts of a financial instrument. A long position is financial security bought expecting the security price go higher. A short position is an obligation to supply a security expecting the price will fall in future.

## Interrelation of orders, deals and positions

The platform allows you to easily track how a position was opened or how a deal was performed. Each trading operation has its unique ID called a "ticket". Each order and deal receive a ticket relating to their relevant position. Each deal receives a ticket of an order, by which it was concluded.

If a position was affected by multiple deals, for example in the case of a partial closing or increasing volumes, each of the deals feature the position's ticket. This makes it easy to track the entire history of the position as a whole.

If trading operations are sent to an exchange or a liquidity provider, they additionally feature an ID from an external system. This allows additional tracking of the interrelation of operations away from the platform.

![The history of opening a position can be tracked by tickets](/en/docs/mt5/api/img/operation_connnection.png "The history of opening a position can be tracked by tickets")

## General Scheme of Trade Operations

-   From the client terminal, an order is sent to a broker to execute a deal with the specified parameters.
-   On the server, correctness of an order is checked (correctness of prices, availability of funds on the account, etc.).
-   Orders that have passed the check wait to be processed on the trade server. Then the order can be:

-   executed (in one of automatic [execution](/en/docs/mt5/api/reference_trading/general_concept/execution_types) modes or by a dealer)
-   canceled upon expiry
-   rejected (e.g. when money is not enough or there is no suiting offer in the market; or rejected by the dealer)
-   canceled by a trader;
-   Execution of a market order or triggering of a pending order results in a deal;
-   If there are no positions for a symbol, conclusion of a deal results in opening of a position. If there is a position for the symbol, the deal will lead to increase or reduction of the position volume, its closure or reversal.

![Scheme of trade operations](/en/docs/mt5/api/img/trading_scheme.png "Scheme of trade operations")

Scheme of trade operations

[Trade](/en/docs/mt5/api/reference_trading)

[Types of Orders](/en/docs/mt5/api/reference_trading/general_concept/order_types)