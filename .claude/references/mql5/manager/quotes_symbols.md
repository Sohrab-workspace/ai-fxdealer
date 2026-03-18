# Quoting and Symbol Management

> Source: https://support.metaquotes.net/en/docs/mt5/manager/quotes_symbols

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)Quoting and Symbol Management

# Quoting and Symbol Management

The Manager terminal allows [throwing in quotes to the price flow](/en/docs/mt5/manager/quotes_symbols#quotes), as well as change financial symbol settings. For example, a manager can expand a spread and a channel, within which the modification of stop levels is prohibited, when important economic news are released.

## Managing financial symbol settings [#](quotes_symbols#properties)

With appropriate rights, a manager can configure some financial symbol settings. Such rights can be given by a server administrator. To open the symbol settings window, click "![Properties](/en/docs/mt5/manager/img/properties_icon.png "Properties") Properties" in the context menu of the [Market Watch](/en/docs/mt5/manager/market_watch) window.

![Properties](/en/docs/mt5/manager/img/symbol_properties.png "Properties")

The following settings are available in this window:

-   Execution — [execution type](/en/docs/mt5/manager/trade_principles#execution_type) by symbol: Instant, Request or Exchange.
-   Background — background color of a symbol name. This will be the color of the symbol background in the [Market Watch](/en/docs/mt5/manager/market_watch) window.
-   Limit & stops level — channel of prices (in points) from the current price, inside which one cannot place [stop loss](/en/docs/mt5/manager/trade_principles#stop_loss), [take profit](/en/docs/mt5/manager/trade_principles#take_profit) and pending orders. If you try to place an order inside the channel, the server returns Invalid Stops and does not accept the order.
-   Spread — spread in points. If this field is set to "0", then the spread is considered to be floating, i.e., formed on the basis of quotes received from data feeds. If you set here a value other than "0", then the spread will be fixed and calculated for the symbol by using the "Spread balance" parameter.
-   Spread balance — if a fixed spread is set in the Spread field, using this function, you can set the direction and size of deviation of the symbol price (Bid + (Bid-Ask)/2) to form prices Bid and Ask. For example, if the spread is set equal to "3", and the balance spread "-2 bid/1 ask", then the Bid price will be equal to the symbol price - 2 points, and the price of Ask - an average price of the symbol + 1 point.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To change settings for several characters simultaneously, use <a href="/en/docs/mt5/manager/quotes_symbols#profile" class="topiclink">profiles</a>.</span></p></td></tr></tbody></table>

## Profiles [#](quotes_symbols#profile)

Profiles are sets of [symbols of financial instruments](/en/docs/mt5/manager/quotes_symbols#properties). They allow quickly switching between the settings of symbols when the market situation changes. The following symbol settings are saved in a profile:

-   Execution
-   Background
-   Limit & Stop levels
-   Spread
-   Spread balance

Working with profiles is carried out by using the Profiles command in the context menu of the [Market Watch](/en/docs/mt5/manager/market_watch) window.

To create a profile, configure symbols in the Market Watch window, and then click Profiles - Save As. The profile saves all the settings for all symbols present in the Market Watch window at the time of saving. To apply a profile, simply select it from the list of available (previously saved) ones:

![Saving the profile](/en/docs/mt5/manager/img/profile.png "Saving the profile")

Before applying the profile, a window with all the symbols and settings that it contains is displayed. Check them and click Apply.

## Quotes [#](quotes_symbols#quotes)

The Manager terminal allows throwing in quotes to the price flow translated from the server. To do this, click "![Quotes](/en/docs/mt5/manager/img/quotes_icon.png "Quotes") Quotes" in the context menu of the Market Watch window or press F4.

![Quotes](/en/docs/mt5/manager/img/quotes.png "Quotes")

This window contains the following settings and commands:

-   Track requests — if enabled, [at the receipt of a new trade request](/en/docs/mt5/manager/dealing) from a client, the symbol of the request will be pre-selected in the Quotes window. Tracking works only when the Quotes window is open.
-   Symbol — symbol, whose quote should be thrown in. To select a different symbol, click this field.
-   Bid — Bid price of the quote. The price can be changed with the help of arrows or manually.
-   Ask — Ask price of the quote. The price can be changed with the help of arrows or manually.
-   Last — price of the last committed transaction. The price can be changed with the help of arrows or manually.
-   Volume — volume of the last executed deal. The price can be changed with the help of arrows or manually.
-   Up — change Bid and Ask prices by one point up.
-   Down — change Bid and Ask prices by one point down.
-   Update — insert current prices to Ask and Bid fields.
-   Send — send a quote with specified prices to the price flow.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you hold one of the below buttons when clicking arrows, the price will change by a certain amount:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Holding Shift — by 5 points;</span></li><li class="p_tableatten"><span class="f_tableatten">Holding Ctrl — by 10 points;</span></li><li class="p_tableatten"><span class="f_tableatten">Holding Ctrl+Shift — by 50 points.</span></li></ul></td></tr></tbody></table>

[Queue of Trade Requests](/en/docs/mt5/manager/trade_queue)

[Summary Positions and Coverage](/en/docs/mt5/manager/summary_positions)