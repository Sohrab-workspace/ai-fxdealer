# Routing Conditions

> Source: https://support.metaquotes.net/en/docs/mt5/manager/ultency_routing/ultency_routing_conditions

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
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
            -   [Routing](/en/docs/mt5/manager/ultency_routing)
                -   [Conditions](/en/docs/mt5/manager/ultency_routing/ultency_routing_conditions)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Ultency](/en/docs/mt5/manager/ultency)[Routing](/en/docs/mt5/manager/ultency_routing)Conditions

# Routing Conditions

The routing rule settings specify a set of conditions defining which trade requests will be processed according to this rule.

![Conditions for a routing rule](/en/docs/mt5/manager/img/ultency_routing_conditions.png "Conditions for a routing rule")

## Comparison Types

Standard comparison types are available for all conditions:

-   Equal (=)
-   Not equal (!=)
-   Greater than (>)
-   Greater than or equal (>=)
-   Less than (<)
-   Less than or equal (<=)

For string conditions, such as country name, symbol, or email, the Match Mask condition is also available. Here you can specify strings with the "\*" mask. For example:

-   Condition "Symbol", value "Forex\\USD\*"  all symbols from the Forex group, where the underlying currency is USD.
-   Condition "Email", value "\*@mailbox.com" applies to all email addresses on the mailbox.com domain.

For login conditions, you can specify multiple values and value ranges. For example, Account\\Login = 100,102,107,120-130.

## Time [#](ultency_routing_conditions#time)

These parameters set date and time conditions. A rule will be triggered if a request arrives on the specified date or within the specified time range.

## Accounts [#](ultency_routing_conditions#accounts)

These settings specify conditions based on account parameters:

-   Login — the trading request was submitted from the specified account.
-   Group, Country, City, Language, Phone, Email, Color, Status, Company  the trading request was submitted from an account that belongs to the specified [group](/en/docs/mt5/manager/groups), [country](/en/docs/mt5/manager/account_personal), [city](/en/docs/mt5/manager/account_personal), etc.
-   Comment — the comment added by the client to the trading request (order).
-   Registration — the condition is set relative to the account creation date in the platform. Specify the date and the comparison type: equal to, less than, or greater than. Accordingly, the condition will trigger for accounts registered on the specified date, earlier or later than this date.
-   Last visit — the condition is set relative to the last connection of the account to the platform. Specify the date and the comparison type: equal to, less than or greater than. Accordingly, the condition will trigger for account connected on the specified date, earlier or later than this date.
-   Days since registration — the condition is set relative to the number of days that have passed since the account was created. The number of days is calculated based on the number of times the clock crosses midnight (00:00) since the event. The principle of operation and purpose of this condition are similar to the "Registration" condition.
-   Days since last login — the condition is set relative to the number of days that have elapsed since the last connection to the account. The number of days is calculated based on the number of times the clock crosses midnight (00:00) since the event. The principle of operation and purpose of this condition are similar to the "Last visit" condition.
-   Days since last trade activity — condition is set relative to the number of days that have elapsed since the last operation on the account. This considers any trading operations, commission charges, etc. Balance operations are not taken into account. In addition, the system checks if the account has any open positions or active pending orders. When using this condition, please note that newly registered accounts may also fall under this condition. For example, a trader may have created an account 1-2 days ago and has not yet performed any trading operations. If you set a condition based on the absence of trading activity in the last 180 days, this trader will also be included in the automation action. To avoid such situations, use the trading activity condition in conjunction with other conditions, such as "Registration" or "Days since registration".  
    The calculated number of days is rounded down. For example, if 5 days and 23 hours have passed since the event, this will be counted as 5 days.
-   Online — condition is set relative to the status of the account connection to the trade server. Possible values are "true" and "false", i.e. the account is either connected (any connection type: client terminal, mobile terminal, and so on) or not.
-   Leverage — the condition is set relative to the [account leverage](/en/docs/mt5/manager/account_tradeaccount). For example, the regulator's requirements have changed, and you need to disable trading with a leverage greater than 1:20 on accounts from the US. Set two conditions: "Country = USA", Leverage > 1:20. Assign the action "Decline" to this rule.
-   Balance — the condition is set relative to the current [account balance](/en/docs/mt5/manager/account_balance#account_state), the amount is indicated in the deposit currency.
-   Credit is similar to the "Balance" condition. In this case, the amount of [credit funds on the account](/en/docs/mt5/manager/account_balance#account_state) is checked.
-   Total positions — the condition is set by the number of open [positions](/en/docs/mt5/manager/account_trading) that currently exist on the account. This action allows you to control extremely active accounts. For example, set "Total positions > 100", "Group = real\\\*". Assign the action "Decline" to this rule.
-   Total orders — similar to the "Total positions" condition, it checks the number of active pending orders on the account.
-   Floating profit, Equity, Margin, Free margin, Margin level — these conditions are similar to the "Balance" condition. Appropriate [trading account states](/en/docs/mt5/manager/account_overview#account_state) are checked here.
-   Deposit currency — the request arrived from an account with the specified deposit currency.
-   Lead Source, Lead Campaign — [lead source and campaign](/en/docs/mt5/manager/account_personal#leadsource) parameters specified in the account.
-   Enabled — the condition is specified relative to the "[Enable this account](/en/docs/mt5/manager/account_tradeaccount#enable)" setting.
-   Trading enabled, Algo trading by Expert Advisors enabled — the conditions are set relative to the corresponding [trading settings](/en/docs/mt5/manager/account_tradeaccount).
-   Agent account — the condition is set relative to the [agent account](/en/docs/mt5/manager/account_tradeaccount#agent_account) specified in the trading account settings.
-   Own funds percentage — when trading, clients are able to use their own funds they deposited in their accounts, as well as the credit and bonuses provided by a broker. Both types of funds increase their Equity parameter. The "Own funds percentage" condition allows configuring the automation task depending on the own funds share on a client's account. 100% means the account has the client's funds only with no credit or bonuses. The value of 0% indicates that only credit and bonus funds are used for trading.  
    The value is calculated as (1 - (Credit / Equity)) \* 100.  
    The fractional part is rounded down during calculation: 1.5% becomes 1%, 0.9% becomes 0%. The parameter value cannot be greater than 100% or less than 0%. If an action is required after the client has spent all their funds, it is more efficient to use the "Own funds volume" condition.
-   Own funds volume — the parameter works similarly to the previous condition, although it applies an absolute own funds value rather than a relative one. Specified in the deposit currency. The calculation equation: Equity - Credit.

## Request [#](ultency_routing_conditions#request)

These settings define conditions based on the parameters of the trading request received from the client.

-   Symbol — a symbol or a group of symbols for which the rule will apply. You can use masks containing "\*" and "!" to define symbols.
-   Volume — the trade volume requested in the order (in lots). This parameter allows configuring rules based on the requested volume, for example, automatically processing requests with a volume of less than 1 lot.

-   Comment — allows comparing the request comment with a specified value. When condition "=" is specified, an exact match is checked. Condition ">" or ">=" searches for the specified substring in a comment line. Condition "<" or "<=" searches for the comment substring in the specified line.

-   Reason — the [reason](/en/docs/mt5/manager/edit_trades#reason) for the creation of the request: whether the order was submitted by a client, Expert Advisor, dealer, etc.

-   Price — the price in the request. In the Instant and Request [execution modes](/en/docs/mt5/manager/trade_principles#execution_type), this is the price specified by the trader in the order. In Market and Exchange modes, this is the current market price of the instrument. Since prices vary significantly between instruments, it is recommended to use this condition in combination with the "Symbol" condition. It can also be used to set the general price threshold. For example, you can decline all requests with a cost of less than one dollar.
-   Value — the value of the requested operation in the symbol's base currency. Value calculation depends on the symbol's [margin/profit calculation mode](/en/docs/mt5/manager/trading_advanced/margin_formula).

## Position [#](ultency_routing_conditions#position)

These settings define conditions based on the [parameters of the position](/en/docs/mt5/manager/edit_trades#position) affected by the received trading request.

-   Ticket — unique position ticket.
-   Volume — the current position volume for the symbol specified in the request.
-   Type — position type: buy or sell.
-   Open price — the weighted average price of the position opening: (price of deal 1 \* volume of deal 1 + ... + price of deal N \* volume of deal N) / (volume of deal 1 + ... + volume of deal N).

-   Current price — the price of the financial symbol for which the position has been opened, at the trigger activation time.
-   Current profit — the current floating profit from the position for which the request was received. Specified in the client's deposit currency.
-   Reason — [reason](/en/docs/mt5/manager/edit_trades#position_reason) for position opening.
-   Creation time — position opening time.
-   Days since creation — time passed since the position was opened.
-   Update time — time when the position was last modified (when its volume was changed).
-   Days since modification — the number of days passed since the last position modification (a change in its volume).
-   Expert ID — identifier (magic number) of an Expert Advisor by which a position was opened in the client terminal.
-   Comment — a text comment to the position.

## Order [#](ultency_routing_conditions#order)

These settings define conditions based on [order parameters](/en/docs/mt5/manager/edit_trades#order).

-   Ticket — the unique order ticket.
-   ID — order identifier in the external system.
-   Setup time — time of order placing by a client.
-   Days since setup — the number of days that have elapsed since the client placed the order. The calculated number of days is rounded down. For example, if the order was placed 3 days and 22 hours ago, this will be counted as 3 days.
-   Expiration time — order expiration date, if it was set by the client.
-   Type — order type: "Buy", "Sell", "Buy Limit", "Sell Limit", "Buy Stop", "Sell Stop", "Buy Stop Limit", "Sell Stop Limit" or "Close By".
-   Order price — price specified by the trader for the order execution.
-   Trigger price — this field is used for the "Buy Stop Limit" and "Sell Stop Limit" orders. It sets the price level at which the orders trigger and the relevant limit orders are placed.

-   Current price — the price of the financial symbol for which the order has been opened, at the request arrival time.

-   Stop Loss — the Stop Loss level.
-   Take Profit — the Take Profit level.
-   Initial volume — volume requested in the order.
-   Remained volume — if the order is not filled in the volume requested by the trader this field will display the remainder volume.
-   State — current order state: Started, Placed, Partially Filled, Rejected, Filled, etc.
-   Expert ID — identifier (magic number) of an Expert Advisor that placed the order in the client terminal.
-   Position — the ticket of the position that will be modified or closed as a result of the execution of this order.
-   Comment — a text comment to the order.
-   Contract size — the contract size of the symbol, for which an order was placed.
-   Currency — the deposit currency of the client who has placed the order.

[Routing](/en/docs/mt5/manager/ultency_routing)

[Subscriptions](/en/docs/mt5/manager/subscriptions)