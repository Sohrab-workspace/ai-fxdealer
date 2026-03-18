# Account Overview

> Source: https://support.metaquotes.net/en/docs/mt5/manager/account_overview

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
            -   [Clients](/en/docs/mt5/manager/clients)
            -   [Online Accounts](/en/docs/mt5/manager/online_accounts)
            -   [Creation of Accounts](/en/docs/mt5/manager/account_create)
            -   [Importing Accounts](/en/docs/mt5/manager/account_import)
            -   [Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)
            -   [Push Notifications, SMS and Mail](/en/docs/mt5/manager/communication)
            -   [Account Overview](/en/docs/mt5/manager/account_overview)
            -   [Exposure](/en/docs/mt5/manager/account_exposure)
            -   [Personal Data](/en/docs/mt5/manager/account_personal)
            -   [Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)
            -   [Balance Operations](/en/docs/mt5/manager/account_balance)
            -   [Trading Operations](/en/docs/mt5/manager/account_trading)
            -   [Account History](/en/docs/mt5/manager/account_history)
            -   [Security and Certificates](/en/docs/mt5/manager/account_security)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Account Overview

# Account Overview

The Overview tab contains summary information about the account: [personal data](/en/docs/mt5/manager/account_personal), date of registration and last access to the account, as well as all the current trading status.

![Account overview: personal data and trading status](/en/docs/mt5/manager/img/account_view_overview.png "Account overview: personal data and trading status")

If you have an active [Finteza subscription](https://support.metaquotes.net/en/news/3420), this section can display data for user tracking: Visitor ID and Affiliate. For further details please visit the "[Analytics](/en/docs/mt5/manager/analytics#visitor)" section.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Last connection time and address data is updated once per hour.</span></p></td></tr></tbody></table>

## Open positions [#](account_overview#positions)

If an account has open positions, they are displayed first.

-   Symbol — financial instrument of an open position.
-   Time — time when a position was opened. The record has the format YYYY.MM.DD HH:MM (year.month.day hour:minute).
-   Type — position type: "Buy" — long, "Sell" — short.
-   Volume — volume of a trade operation (in lots or units).
-   Price — weight-average price of a position opening: (price of deal 1 \* volume of deal 1 + ... + price of deal N \* volume of deal N) / (volume of deal 1 + ... + volume of deal N). The accuracy of rounding of an average weighted price is equal to a number of decimal places in a symbol price plus three additional digits.
-   S/L — [stop loss](/en/docs/mt5/manager/trade_principles#stop_loss) level of the current position. If this order is not placed, a zero value is shown in the field.
-   T/P — [take profit](/en/docs/mt5/manager/trade_principles#take_profit) level of the current position. If this order is not placed, a zero value is shown in the field.
-   Price — current price of a financial symbol. Bid price is displayed for short positions, while Ask price is used for long ones. A price of the last performed deal (Last) is displayed for positions involving exchange symbols (both directions).
-   Swap — amount of swaps charged.
-   Profit — current financial result of a position calculated at a market price. A positive result indicates the profitability of a deal, while negative highlights its loss-making nature.

To open the [operation details](/en/docs/mt5/manager/edit_trades), click "View" or "Edit" (if you have enough permissions) in its context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When the current price nears the levels of stop loss and take profit, S/L and T/P fields are colored in red and green, respectively. A pending order trigger price is colored green as well. Highlighting turns on when a price nears closer than:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">100 points for symbols with 5 and 3 decimal places in quotes</span></li><li class="p_tableatten"><span class="f_tableatten">10 points for symbols with 2 and 4 decimal places in quotes</span></li></ul></td></tr></tbody></table>

## Account status [#](account_overview#account_state)

The following information is displayed in the account status bar:

-   Balance — account funds not considering results of currently open positions (deposit).
-   Credit — amount of funds provided to a client by a broker as a loan (sum of operations of [Credit and Bonus](/en/docs/mt5/manager/account_balance) types). The trading platform does not have a function of charging an interest for credit assets. Credit assets can be deposited and withdrawn at the [Balance](/en/docs/mt5/manager/account_balance) tab.
-   Commission (Blocked Commission) — commission by orders and positions accumulated during a day/month. Depending on the [client group settings](/en/docs/mt5/manager/groups#commission), preliminary commission calculation is performed during a day/month and an appropriate amount of money is blocked in the account and displayed here. Final commission calculation is performed at the end of a day/month and the appropriate sum is withdrawn from the account by a balance operation (displayed as a separate deal on the [History](/en/docs/mt5/manager/account_history) tab), while blocked funds are unblocked.  
    In case commission is charged immediately during a deal, its value is shown in the Commission field of the History tab.
-   Accumulated (Blocked Profit) — client group can be set up so that a profit earned by a trader during a day cannot be used for trading (it is not accounted in the free margin). At the end of a trading day, this profit is unblocked and deposited to the account balance. This field displays the current profit/loss obtained by a client during the day. The field is only displayed for accounts from groups where the risk account mode is "[for Retail Forex, CFD, Futures](/en/docs/mt5/manager/margin#risk)" (netting position accounting).
-   Equity — equity is calculated as Balance + Credit - Commission +/- Floating profit/loss - Blocked.
-   Margin — money required to cover open positions and pending orders.
-   Free Margin — free amount of money that can be used to maintain open positions. It is calculated as Equity - Margin. Depending on the client group settings, the equity value may or may not consider: floating profit, floating loss or floating profit and floating loss together;
-   Margin Level — percentage of an account equity to a margin volume (Equity / Margin \* 100).
-   Floating P/L — total financial result of all open positions including swaps. In case of a positive result, icon ![Balance increase](/en/docs/mt5/manager/img/balance_up_icon.png "Balance increase") is shown, in case of a negative one — ![Balance decrease](/en/docs/mt5/manager/img/balance_down_icon.png "Balance decrease").

## Exposure [#](account_overview#collateral)

The trading platform supports a special type of non-tradable assets, which can be used as client's assets to provide a required margin for open positions of other instruments. For example, a certain amount of gold in physical form can be available on a trader's account, which can be used as a margin (collateral) for open positions.

These instruments have [Collateral](/en/docs/mt5/manager/market_watch#calculation) calculation type. They have the following features:

-   Clients cannot perform any operations with them except closing. A position can be opened only by a manager.
-   No profit can be accrued for positions of these symbols, they have no stop loss or take profit.

Such assets are displayed as open positions. Their value is calculated by the formula: Contract size \* Lots \* Market Price \* Liquidity Rate.

-   Contract size — size of a contract
-   Lots — volume in lots
-   Market Price — current market price of a financial instrument
-   Liquidity Rate here means a share of an asset a broker allows to use for the margin

The Assets are added to the client's Equity and increase Free Margin, thus increasing the volumes of allowable trade operations on the account.

![Trader's assets](/en/docs/mt5/manager/img/account_assets.png "Trader's assets")

In the example above, a trader has 1 ounce of gold having the current market value of 1 212.01 USD. This value is added to the equity and the free margin

Collateral symbol settings on the server may allow clients and managers close such positions (Trade = Close only). In this case, a trader is able to convert the asset into the deposit currency at the current market rate and use that money for trading. Closing can be performed only if an asset/deposit currency conversion rate is present.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To delete a collateral position without crediting any profit, a manager should close the position at the zero price.</span></li><li class="p_tableatten"><span class="f_tableatten">To close a position with adding its value to a trader's balance, a manager should close it at the current market price.</span></li></ul></td></tr></tbody></table>

## Pending orders [#](account_overview#pending)

Below the line with the current status of the account, placed pending orders and requests pending [processing](/en/docs/mt5/manager/dealing) are shown:

-   Symbol — financial instrument of a pending order.
-   Order — ticket number (unique identifier) of a pending order.
-   ID — order ID in an external trading system.
-   Time — pending order placing time. The record has the format YYYY.MM.DD HH:MM (year.month.day hour:minute).
-   Type — [type of a pending order](/en/docs/mt5/manager/trade_principles#pending_order): "Sell Stop", "Sell Limit", "Buy Stop", "Buy Limit", "Buy Stop Limit" or "Sell Stop Limit".
-   Volume — volume requested in a pending order, and volume covered by a deal (in lots or units).
-   Price — pending order trigger price.
-   S/L — [stop loss order](/en/docs/mt5/manager/trade_principles#stop_loss) level. If this order is not placed, a zero value is shown in the field.
-   T/P — [take profit](/en/docs/mt5/manager/trade_principles#take_profit) order level. If this order is not placed, a zero value is shown in the field.
-   Price — current price of a financial symbol. Bid price is displayed for short orders, while Ask price is used for long ones. A price of the last performed deal (Last) is displayed for orders involving exchange symbols (both directions).
-   Comment — comment to a pending order.
-   State — current order status: "Started", "Placed" etc.

## Context menu [#](account_overview#context)

The context menu of an account status block allows performing the following commands:

-   New Order — go to the [Trade](/en/docs/mt5/manager/account_trading) tab to create a [new order](/en/docs/mt5/manager/positions#open) on the account.
-   Close Position — go to [closing](/en/docs/mt5/manager/positions#close) of a selected position on the Trade tab.
-   Modify or Cancel — go to [modifying or deleting](/en/docs/mt5/manager/orders#modify_delete) a selected pending order or to [modifying](/en/docs/mt5/manager/positions#modify) a selected position.
-   Activate — go to [activation](/en/docs/mt5/manager/orders#activate) of a selected pending order.
-   Edit — administrator command allowing you to [edit any parameters](/en/docs/mt5/manager/edit_trades) of a selected trade operation. The command is available if the manager account has the appropriate permissions.
-   Delete — administrator command allowing you to delete a selected trade operation. The command is available if the manager account has the appropriate permissions.
-   Volumes — open the submenu for selecting the units to display volumes (lots or amount).
-   Profit — open the submenu for selecting the units to display the profit (money or points).
-   Report — generate a report on client's trading positions in XML or HTML format.
-   Show Milliseconds — show time of trade operations with the millisecond precision.
-   Auto Arrange — if enabled, a size of columns is selected automatically.
-   Grid — show/hide the grid to separate columns.
-   Columns — open the submenu for selecting columns to show in the table.

[Push Notifications, SMS and Mail](/en/docs/mt5/manager/communication)

[Exposure](/en/docs/mt5/manager/account_exposure)