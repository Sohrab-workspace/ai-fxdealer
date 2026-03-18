# Dealing — Processing Client's Trade Requests

> Source: https://support.metaquotes.net/en/docs/mt5/manager/dealing

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
            -   [Dealing](/en/docs/mt5/manager/dealing)
            -   [Accounts with Margin Call/Stop Out](/en/docs/mt5/manager/margin_calls)
            -   [Queue of Trade Requests](/en/docs/mt5/manager/trade_queue)
            -   [Quoting and Symbol Management](/en/docs/mt5/manager/quotes_symbols)
            -   [Summary Positions and Coverage](/en/docs/mt5/manager/summary_positions)
            -   [Exposure](/en/docs/mt5/manager/exposure)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)Dealing

# Dealing — Processing Client's Trade Requests

Dealing — one of the main functions of the Manager terminal. Managers can process trading requests from clients: confirm and reject them and issue prices for execution of trades.

To process trade requests, select "![Start Dealing](/en/docs/mt5/manager/img/start_dealing_icon.png "Start Dealing") Start Dealing" in the [File](/en/docs/mt5/manager/main_menu#file) menu or on the toolbar. After that, the Manager terminal starts accepting trade requests from clients from the general queue of trade requests. Dealers receive requests only from the clients available to them. While a request is processed by one dealer, another one cannot receive and process it. Dealers have a certain time to process a request. This time is set in the [Manager terminal](/en/docs/mt5/manager/settings#timeout) settings. It is shown in the quotation field. If the dealer does not process a request within the specified time, it is rejected automatically.

When a request is received, a dealer immediately sees the current trading account status including open positions and pending orders. Besides, the dealer sees the list of orders located close to the market price that can be triggered soon.

![Processing trade requests by a dealer](/en/docs/mt5/manager/img/dealing.png)

### Client data

Account number, as well as client's name and group are displayed for each incoming request.

### Request data

A type (for example, instant sell, request buy), volume, trading symbol name and price (if a request is set at a constant price) are displayed for each request.

### Quote field

The main part of the quote field contains Bid and Ask prices as of the moment a request was accepted for processing. Using arrow buttons you can change the price, at which the request will be processed. Large buttons change both prices, small ones — individually. If you enable ["Throw in prices at request answer](/en/docs/mt5/manager/settings#prices), specified prices are automatically thrown to a price flow when confirming a request.

Remaining time for a request processing. If the dealer does not answer within the specified time, the request is rejected automatically. The response time is set in the [Manager terminal settings](/en/docs/mt5/manager/settings#timeout). Price, volume or time, at which an alert is triggered.

Here you can set a volume used to execute an incoming request. This allows for partial execution of orders.

This field is available only if the execution order from the trader indicates the [execution policy](/en/docs/mt5/manager/trade_principles#fill_policy) that allows the execution of the order in an incomplete volume.

In this field, a dealer can indicate a reason for the refusal in the order execution. The comment is displayed in the order placing window in the client terminal. The maximum comment length is 32 symbols.

Buttons for answering a trade request:

-   Confirm — confirm request execution at prices and for the volume specified in the quoting field.
-   Reject — reject the request; in this case the request is not executed and deleted from the queue, while a trader will receive an appropriate warning in the terminal.

The current state of the account, a request from which is currently being processed: [open positions](/en/docs/mt5/manager/positions), [account state](/en/docs/mt5/manager/account_overview#state), [pending](/en/docs/mt5/manager/orders) and unprocessed orders (including the request that is currently being processed). Double-click a position or an order to move to the account dialog.

The context menu allows to configure display: volumes (lots or units) and profits (money or points), enable columns auto sizing etc.

Orders and positions located close to the market price and may soon be triggered. More details are provided below.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Account information is displayed in the color specified in its <a href="/en/docs/mt5/manager/account_tradeaccount#color" class="topiclink">settings</a>. The background color allows the dealer to identify a trader when processing a trade request. For example, color can highlight potential frauds or important clients.</span></li><li class="p_tableatten"><span class="f_tableatten">The dealing section, as well as buttons for connecting by the dealer in the <a href="/en/docs/mt5/manager/main_menu" class="topiclink">main menu</a> and on the <a href="/en/docs/mt5/manager/toolbar" class="topiclink">toolbar</a> may not be present if the manager account has no Dealer permission. This permission can be granted by a trade server administrator.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Left-clicking on the quoting field substitutes the current market price of the instrument.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">It is possible to quickly change the price value by a certain amount by holding Ctrl or Shift, while pressing arrows: Shift — by 5 points, Ctrl — by 10 points, Ctrl+Shift — by 50 points.</span></li></ul></td></tr></tbody></table>

## Trade request data [#](dealing#requests_info)

Upon receiving a request, the Manager terminal displays its details (type, volume and price) to a dealer. Examples of all possible request types are provided below.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Request type</span></p></th><th class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Example</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Interpretation</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Request of Quotes</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Request of quotes in the Request <a href="/en/docs/mt5/manager/trade_principles#execution_type" class="topiclink">execution mode</a>.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">prices for EURUSD 1.00</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Request of prices to execute a trade operation on 1 lot of EURUSD.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Request Confirmation</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">The option of additional order confirmation can be enabled in symbol settings. Upon receiving quotes from a dealer in the Request execution mode and agreeing to them, a trader sends a request to execute a deal. The dealer should re-confirm execution of this request (specifying execution mode, deal direction, volume, symbol and price).</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">request sell 1.00 EURUSD at 1.22788</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Request to sell one lot of EURUSD at 1.22788.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Instant Order</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Order confirmation in the instant execution mode.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">instant sell 1.00 EURUSD at 1.22788 sl: 1.22000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Request to sell one lot of EURUSD at price 1.22788 with Stop Loss level equal to 1.22000.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Market Order</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Order confirmation in the market execution mode.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">market sell 1.00 EURUSD</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Request to sell one lot of EURUSD.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Exchange Order</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Order confirmation in the exchange execution mode.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">exchange sell 1.00 EURUSDl</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Request to sell one lot of EURUSD.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Placing a Pending Order</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Placing a <a href="/en/docs/mt5/manager/trade_principles#pending_order" class="topiclink">pending order</a>.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">buy limit 1.00 EURUSD at 1.22000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Placing a pending order Buy Limit for one lot of EURUSD at level 1.22000.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Position Modification (S/L, T/P)</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Request to change levels of <a href="/en/docs/mt5/manager/trade_principles#stop_loss" class="topiclink">stop loss</a> or <a href="/en/docs/mt5/manager/trade_principles#take_profit" class="topiclink">take profit</a>.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">modify buy 1.00 EURUSD (sl: 1.22000, tp: 0.00000)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Changing levels of stop loss and take profit of a position for buying one lot of EURUSD to 1.22000 and 0.00000, respectively.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Pending order modification</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Request to <a href="/en/docs/mt5/manager/orders#modify_delete" class="topiclink">modify</a> a pending order.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">modify #123456 buy limit 1.00 EURUSD at 1.23000 (sl: 1.22000, tp: 0.00000)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Modify the Buy Limit order of one lot of EURUSD with unique number 123456. The order is placed at price 1.23000 with stop loss level at 1.22000 and no take profit level.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Deleting a Pending Order</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Request to <a href="/en/docs/mt5/manager/orders#modify_delete" class="topiclink">delete</a> a pending order.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">cancel #123456 buy limit 1.00 EURUSD at 1.23000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the Buy Limit order of one lot of EURUSD with unique number 123456 that was placed at level 1.23000.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Pending Order Activation</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/manager/orders#activate" class="topiclink">Activation</a> of a pending order, when conditions specified in it occur ("activate", unique number of the order).</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">activate #123456 buy limit 1.00 EURUSD at 1.23000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Activate the Buy Limit order of one lot of EURUSD with unique number 123456, at price 1.23000.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Activation of Stop Loss</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Activation of an order to close a position when a stop loss level is reached.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">activate stop loss buy 1.00 EURUSD (sl: 1.23000)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close a position to buy one lot of EURUSD at stop loss price 1.23000.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Activation of</span><br><span class="f_fortable">Take Profit</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Activation of an order to close a position when a take profit level is reached.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">activate take profit buy 1.00 EURUSD (sl: 1.23000)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close a position to buy one lot of EURUSD at take profit price 1.23000.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Activation of a</span><br><span class="f_fortable">Stop Limit order</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Activation of a stop limit order Buy Stop Limit or Sell Stop Limit.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">activate stop-limit order #123456 buy stop limit 1.00 EURUSD at 1.23000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Place the Buy Limit order for one lot of EURUSD at level 1.23000 based on the activated Buy Stop Limit order with unique number 123456.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Deleting a Pending order by Stop Out</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Deleting a pending order when a client reaches a stop out level.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">delete stop-out order #123456 buy limit 1.00 EURUSD at 1.23000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the Buy Limit order placed for one lot of EURUSD at level 1.23000 with the unique number 123456.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable">Position Closing by Stop Out</span></p></td><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">Closing a position when a client reaches a stop out level.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">close stop-out position buy 1.00 EURUSD at 1.23000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close a position to buy one lot of EURUSD at price 1.23000.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In the Manager terminal, you can set up <a href="/en/docs/mt5/manager/dealing#automation" class="topiclink">automatic processing</a> of some of the requests listed above.</span></p></td></tr></tbody></table>

## Orders and positions closest to the market [#](dealing#closest_orders)

Under the field displaying the state of an account, you can see the list of orders and positions that are closest to the market. Thus, a dealer always has data on orders that may trigger in the near future.

![Orders and positions closest to the market](/en/docs/mt5/manager/img/dealer_close_to_market.png "Orders and positions closest to the market")

This list displays positions, whose [stop loss](/en/docs/mt5/manager/trade_principles#stop_loss) and [take profit](/en/docs/mt5/manager/trade_principles#take_profit) levels are closest to the market prices of the corresponding symbols. Also, it displays pending orders, whose trigger prices are closest to the market prices.

Take profit and stop loss fields of positions as well as the Price field of pending orders are highlighted with different colors depending on the distance to the current market price.

-   For trading positions, Take Profit levels are highlighted in green and Stop Loss levels in red if:

-   the distance between the level and the current price is 100 points or less for instruments with 5 decimal places,
-   the distance between the level and the current price is 10 points or less for instruments with 3 decimal places.

If the distance between the level and the current price is 0 (i.e., the level has been triggered), it is highlighted in yellow.

For pending orders, the trigger price is highlighted in green if:

-   the distance between the order price and the current price is 100 points or less for instruments with 5 decimal places,
-   the distance between the order price and the current price is 10 points or less for instruments with 3 decimal places.

Stop Loss and Take Profit levels for pending orders are not highlighted.

If the distance between the pending order price and the current price is 0 (i.e., the order has been triggered), it is highlighted in yellow.

-   For instruments with 5 decimal places: if the distance to the current price is 100 points or less, Take Profit levels are highlighted in green and Stop Loss levels in red.
-   For instruments with 3 decimal places: if the distance to the current price is 10 points or less, Take Profit levels are highlighted in green and Stop Loss levels in red.

The Profit field is also highlighted in red if the account is under stop out.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The specified highlight distances are used for symbols with five- and three-digit quotes. For symbols with four- and two-digit quotes, the highlight distance is ten times less.</span></p></td></tr></tbody></table>

## Automatic processing of trade requests [#](dealing#automation)

In the Manager terminal, you can enable automatic processing of trade requests of certain types. You can set types of requests and volume limitations in the terminal settings on the [Automation](/en/docs/mt5/manager/settings#automation) tab.

![Configuring and enabling auto processing of requests](/en/docs/mt5/manager/img/automation.png "Configuring and enabling auto processing of requests")

For quick enabling/disabling the automatic processing mode, use the "![Automation](/en/docs/mt5/manager/img/automation_button.png "Automation") Automation" button on the [toolbar](/en/docs/mt5/manager/toolbar).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">After you enable the automatic processing, you should manually handle the current request. Only after that, the automatic processing is started.</span></p></td></tr></tbody></table>

## Additional dealer tools [#](dealing#additional)

The context menu of the Dealing section allows you to quickly manage terminal settings related to processing trade requests:

![Additional dealer settings and tools](/en/docs/mt5/manager/img/dealing_additional.png "Additional dealer settings and tools")

The following commands are available here:

-   ![Automation](/en/docs/mt5/manager/img/automation_button.png "Automation") Automation — enable/disable [auto processing](/en/docs/mt5/manager/dealing#automation) of trade requests.
-   ![Correct Prices](/en/docs/mt5/manager/img/correct_prices_icon.png "Correct Prices") Correct Prices — [automatically throw in quotes](/en/docs/mt5/manager/settings#prices) to a price flow when replying to a trade request. The prices, at which a request is executed, are thrown to the flow.
-   Switch on Request — automatically switch to the dealer window when a new trade request arrives.
-   ![Open Logs Folder](/en/docs/mt5/manager/img/open_data_folder_button.png "Open Logs Folder") Open Logs Folder — open the folder storing the [trade request processing journal](/en/docs/mt5/manager/dealing#journal) (dealing.log).

## Dealing log [#](dealing#journal)

The Manager terminal keeps track of processed requests and records information about dealer's actions in a special log.

![Dealing log](/en/docs/mt5/manager/img/toolbox_dealing.png "Dealing log")

The log displays trade processing time, dealer's and client's logins, [request](/en/docs/mt5/manager/dealing#requests_info) and answer descriptions. The possible answers are:

-   Done — request was executed at a specified price.
-   Rejected — request was rejected.
-   Prices — specified prices were suggested to the trader for executing the request.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Server time is displayed in the dealer's journal entries.</span></li><li class="p_tableatten"><span class="f_tableatten">Dealer's journal entries are stored in a <a href="/en/docs/mt5/manager/beginning_advanced/structure#dealing" class="topiclink">separate file</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If a manager has Supervisor permission (granted in the Administrator terminal) while not connected as a dealer, this tab displays results of processing requests by other dealers. Managers are able to track processing requests coming from client groups available for them.</span></li></ul></td></tr></tbody></table>

Journal entries are highlighted in different colors depending on how a request is processed by a dealer:

-   Orders triggered in worse conditions than the current market ones (buying above the current price, selling below it) are highlighted in green.
-   Rejected requests are displayed in yellow.
-   Orders triggered in better conditions than the current market ones (buying below the current price, selling above it) are highlighted in red.
-   Orders triggered at a requested price are highlighted in white.

The log's context menu allows [viewing an account](/en/docs/mt5/manager/account_overview), open the dealer's log folder (dealing.log), as well as configure the tab view.

[Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)

[Accounts with Margin Call/Stop Out](/en/docs/mt5/manager/margin_calls)