# Common settings

> Source: https://support.metaquotes.net/en/docs/mt4/manager/getting_started/ug_setup

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
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
            -   [General](/en/docs/mt4/manager/getting_started/userguide)
            -   [Common settings](/en/docs/mt4/manager/getting_started/ug_setup)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Getting Started](/en/docs/mt4/manager/getting_started)Common settings

# Common settings

The setup of client terminal are made in the "Tools — Options..." menu and include setting the following parameters:

-   [connection to the server (Server tab)](/en/docs/mt4/manager/getting_started/ug_setup#server)
-   [coverage of client positions (Coverage tab)](/en/docs/mt4/manager/getting_started/ug_setup#coverage)
-   [dealer operations (Dealer tab)](/en/docs/mt4/manager/getting_started/ug_setup#dealer)
-   [automatic processing of requests (Automation tab)](/en/docs/mt4/manager/getting_started/ug_setup#automation)
-   [signaling about system events (Events tab)](/en/docs/mt4/manager/getting_started/ug_setup#events)

## Setting connection to the server (Server tab) [#](ug_setup#server)

![Server tab](/en/docs/mt4/manager/img/options_server.png "Server tab")

It is necessary to give the trade server address, login, and password in the "Server" tab. The "Delete account" button allows to delete manager login from the saved logins list. After the connection to the server has been established, the "Change password" button allows to change the current password. If advanced security applies to the group of the manager being connected, it is necessary to descibe the path to RSA keys, as well. For the purpose of providing with additional security, keys can be located on a portable data medium, for example, on a flash-memory card.

The following additional parameters of connection can be set in the "Server" tab:

-   Save account information — save login, password, and internal mails between connections to the server;
-   Hide online users — hide online users;
-   Save week ticks — if you enable this option, the manager terminal will collect tick data by symbols weekly in the ticks.raw file. At the end of a week the data from it will be written to a file of weekly ticks YYYY.MM.DD.ticks, and the file will be cleaned to collect information for the next week. If the option is disabled, only last 2000 ticks will be stored, weekly data won't be saved.

## Coverage of client positions (Coverage tab) [#](ug_setup#coverage)

MetaTarder Manager 4 allows to cover client positions and exposure.

See ["Risk Management - Coverage"](/en/docs/mt4/manager/risk_management/ug_coverage#setup) for more detailed information.

## Dealer operation settings (Dealer tab) [#](ug_setup#dealer)

![Dealer Tab](/en/docs/mt4/manager/img/options_dealer.png "Dealer Tab")

The following parameters of dealer operations can be set in the "Dealer" tab:

-   Automatic dealer connecting — connect dealer automatically after manager authorization;
-   Reject modification of occupied orders — reject modification of orders with crossed Stop Loss/Take Profit level and pending orders queueing up for activation;
-   Throw in prices at request answer — input quotations when answering a request;
-   Multiple execution of requests of the same type — when confirming the request, automatically execute queued requests of the same type, with the same operation, for the same symbol, on a smaller or equal volume, at the equal or worse prices;
-   Force switch to dealer window on new request — force switch to dealer window on new request;
-   Show user id on receiving request — show account ID in the customer's details field on receiving a request;
-   Freeze the price of the selected order at stopout — freeze the price of the selected most losing order at stopout. When a stopout occurs, the MetaTrader 4 Manager chooses the client's most losing order and places it in the list of triggered orders on the ["Dealer"](/en/docs/mt4/manager/request_processing/ug_dealing) tab. If this option is enabled, the price of the most losing order selected should be frozen as of the stopout, i.e., the close price and the profit don't change at the arriving of a new ticks. At the same time, if the price goes against the dealer, he or she can close the given order at the price most beneficial to him/her. If the price goes against the client, the dealer can close the order at the price as of the stopout, which wouldn't allow the client to lose more. If the dealer closes another order during stopout, it is necessary to delete the selected order from the list of triggered orders on the "Dealer" tab in order to unfreeze the price of the selected losing order.

The Confirm n points setting controls what price will be automatically substituted into the dealer's quotes box if the request price for a symbol in the Instant Execution mode differs from the current market price. If the request price differs from the current one not in favor of the client, the request price will be substituted in the quotes box. If the dealer presses the "Confirm" button without changing of the price, the position will be opened at a price worse than the market one. If the request price differs from the current one not in favor of the dealer, but keeps within the value given in settings, the request price will be substituted in the quotes box. If the dealer presses the "Confirm" button without changing of price, the position will be opened at a price better than the market one. It means, in settings, the amount of points that the dealer can present to the client and, thus, prevent against multiple requotes. If the request price differs from the current one not in favor of the dealer and does not keep within the value given in the settings, the current price will be substituted into the quotes box. At that, if the dealer presses the "Confirm" button without changing of the price, the client will receive the suggestion to requote or a position will be opened, if the new price keeps within the maximal deviation given by the client in the terminal at sending off the request. In any case, the dealer can change price that will be automatically substituted into the quotes box and give the own prices.

## Setting automatic request processing (Automation tab) [#](ug_setup#automation)

MetaTarder Manager 4 allows a connected dealer to confirm trade requests of necessary types automatically.

See ["Request Processing - Automation"](/en/docs/mt4/manager/request_processing/ug_automation) for more detailed information.

## Notification on system events (Events tab) [#](ug_setup#events)

![Events tab - notification on system events](/en/docs/mt4/manager/img/options_events.png "Events tab - notification on system events")

The "Events" tab allows to setup system events notification. The "Enable" flag permits using events notification in the terminal. The predefined system event is placed in the "Event" field, and the file - in the "Action" field. System events are:

-   Connect — connection to the server;
-   Disconnect — disconnection from the server;
-   Email — receiving emails;
-   Timeout — timeout and errors when executing operations;
-   OK — successful execution of the operation;
-   Request — receiving a new request by the dealer;
-   SL / TP — crossing the Stop-Loss or Take-Profit level of the order;
-   Pending Order — pending order activation;
-   Margin Call — the account has crossed the Margin-Call level;
-   Requote — a dealer has proposed a new quote for a trade operation.

[General](/en/docs/mt4/manager/getting_started/userguide)

[Client Accounts](/en/docs/mt4/manager/client_accounts)