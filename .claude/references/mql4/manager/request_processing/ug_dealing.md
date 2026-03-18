# Dealer

> Source: https://support.metaquotes.net/en/docs/mt4/manager/request_processing/ug_dealing

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
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
            -   [Dealer](/en/docs/mt4/manager/request_processing/ug_dealing)
            -   [Automation](/en/docs/mt4/manager/request_processing/ug_automation)
            -   [Queue, Dealing, Margin Calls Windows](/en/docs/mt4/manager/request_processing/ug_win_queue)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Request Processing](/en/docs/mt4/manager/request_processing)Dealer

# Dealer

The window of request processing ("Dealer" tab) allows to process trading requests of the clients.

The dealer can be connected by a toolbar command or through dealer's context menu Connect. The dealer can be disconnected by Disconnect command. If the [Automatic dealer connecting](/en/docs/mt4/manager/getting_started/ug_setup#server) option is enabled the dealer will automatically be connected when manager terminal connects to the server.

![Dealer](/en/docs/mt4/manager/img/br_dealer.png "Dealer")

The quotation window is located on the top part of the request processing window. The quotation window contains the field of detailed information about the income request, the quotation field, and the button of reply to the request. Information about a client from whom a request has come is located to the left of the quotation field.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><a name="color" class="hmanchor"></a><span class="f_tableatten">Information about a client is displayed in the color specified in the <a href="/en/docs/mt4/manager/client_accounts/ug_accounts#color" class="topiclink">account details</a>. The color representation can be used, for example, for marking "suspicious" clients.</span></p></td></tr></tbody></table>

Information about an incoming request is displayed to the right of the quotation field. Window of account management will open when the field of detailed information about the request is clicked. The current market prices are substituted in the quotation field when this field is klicked on. Arrow buttons shift the prices in the quotation field to be returned to the client when replying to the request.

The dealer can reply to the request with three commands:

-   Return returnes the request to the request queue, i.e. allows the request to go through; at this, another connected dealer may take the request from the queue;
-   Send / Confirm replies to the client's request with a confirmation; at this, if prices have been shifted in the Instant execution mode the client will receive "Requote";
-   Reject replies with a rejection to the client's request.

The processed clients' requests are displayed in the request log [Dealing](/en/docs/mt4/manager/request_processing/ug_win_queue#dealing).

When confirming the request, there is a possibility to automatically execute queued requests of the same type, with the same operation, for the same symbol, on a smaller or equal volume, at the equal or worse prices. To do so, it is necessary to enable Multiple Execution mode in the dealer's toolbar or in the context menu of the dealer's window. The more detailed information about the automatical requests execution is published at the [Support Center](https://support.metaquotes.net), the [Multiple Requests Processing in MetaTrader 4](https://support.metaquotes.net/en/articles/56) article.

When quotations are shifted as a reply to the client's request, there is a possibility to push new quotations into the quotation flow from data feeders. To do so, it is necessary to enable Throw in Prices mode in the dealer's toolbar or in the context menu of the dealer's window.

## Order Lists

Three order lists are located below the quotation window.

The upper list includes all open orders of the account by which the request has come.

The lower list includes open orders having exceeded Stop Loss or Take Profit levels, pending orders for activation, as well as the most detrimental clients' orders being in the stop-out state according to their margin requirements (orders having started). According to the type of the order having started, the fields of "S / L" or "T / P" are highlighted in red for orders having stops activated, "Price" - for pending orders, or "Profit" - for orders by Stop Out. If the price rolls back from the level at which the order could be activated, the data of the field are highlighted in yellow. At this, the possiblity remains to execute the order at the price of activation or to delete the order from the list manually with the help of the Remove context menu command.

The list of orders started is sorted by their proximity to the market. Automation mode being enabled, the started orders will be executed automatically. If the automation is disabled the started orders must be executed manually, the order window being opened by double clicking the left mouse button.

The last list includes 256 orders most proximate to the market, this list can be hidden or shown with Show All Orders context menu command. Take Profit and Stop Loss fields of positions as well as Price field of pending orders are highlighted with different colors depending on the distance to the current market price:

-   A triggered level is highlighted in red.
-   If the distance to the current price is 50 points or less, the level is highlighted in pink.
-   If the distance to the current price is 100 points or less, the level is highlighted in yellow.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The specified highlight distance is used for symbols with five- and three-digit quotes. For symbols with four- and two-digit quotes the highlight distance is ten times less.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If the spread of a symbol is greater than 20 (or 200 for three- and five-digit quotes), the distance to the current market price is calculated in ticks instead of points. Tick size is calculated as spread/10.</span></li></ul></td></tr></tbody></table>

[Request Processing](/en/docs/mt4/manager/request_processing)

[Automation](/en/docs/mt4/manager/request_processing/ug_automation)