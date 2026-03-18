# Deals

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_deals

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Deals

# Deals

This section allows working with the entire history of deals executed by traders' orders, and balance operations.

![Deals](/en/docs/mt5/platform/img/deals.png "Deals")

Depending on points selected in the [context menu](/en/docs/mt5/platform/administration/admin_deals#context), various [information about deals](/en/docs/mt5/platform/administration/admin_deals#view) is shown here. Deals can be sorted out by any field by a left button click on the field name.

## Requesting Deals [#](admin_deals#request)

In order to view deals, a request should be constructed. A request can be performed:

-   By groups  
    To do it, select a group from the dropdown list.
-   By logins  
    Specify one or several account numbers separated by commas.
-   By tickets  
    To request deals by their number, specify one or several tickets separated by commas. Before deal tickets the # symbol should be specified.

Further the following request parameters can be specified:

-   Trading instruments for which deals will be requested. One symbol or a group of symbols can be selected from the list. Optionally, you can specify a comma separated list of trading instruments or groups of symbols. For example, Forex\\\*, CFD\\\*, Metals\\GOLD. Please note that filtering is performed on the server side, and not on the administrator terminal side. To obtain data on other instruments, send another request. The request is performed for all financial instruments by default.
-   You can specify one of predefined request periods using the ![Time Frame](/en/docs/mt5/platform/img/calendar.png "Time Frame") button: "Today", "Last 3 days", "Last week", "Last 3 months", "Last 6 months" and "All history".
-   You can set precise time limits of the request. Indicate them manually or using the calendar that is opened at a click on button ![Calendar](/en/docs/mt5/platform/img/calendar_button.png "Calendar").
-   Further you can specify from which database deals should be requested: current database or one of [backups](/en/docs/mt5/platform/administration/admin_deals#backup).

To perform the request, press the "Request" button or execute the "![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request" command of the [context menu](/en/docs/mt5/platform/administration/admin_deals#context).

## Viewing a Deal [#](admin_deals#view)

To start viewing or editing a deal, double click on  the selected deal in the list. The trading operation dialog is a fully-featured tool with a plethora of advanced features, such as the display of the structure of operations, visualization, tick history and logs.

![Deal](/en/docs/mt5/platform/img/deal_view.png "Deal")

### Account details [#](admin_deals#account_details)

The upper part of the dialog features brief information about the account, on which the operation was performed: name, login, groups and leverage. Click on this line to view [account details](/en/docs/mt5/platform/administration/admin_accounts/account_edit).

### Overview and related operations [#](admin_deals#connected_transactions)

This block displays all the related trading operations: the order as a result of which the deal was executed, the position affected by the deal, as well as which initiated the operation, the deals performed as a result of order execution and the final position. Thus you can easily access the entire chain of related actions. Select an operation from the tree and all relevant parameters will be instantly displayed in the bottom part.

### Trading operation details [#](admin_deals#details)

The following parameters are indicated for deals:

-   Login — [account](/en/docs/mt5/platform/administration/admin_accounts) number the deal has been performed on.
-   Creation time — time of deal execution.
-   Deal — a unique deal number.
-   Order — ticket (number) of the [order](/en/docs/mt5/platform/administration/admin_orders) the deal was executed on.
-   Position — ticket of the position that was opened or closed by this deal.
-   Action — deal type, and the direction of the deal relative to the current [position](/en/docs/mt5/platform/administration/admin_positions) of the account: in (entry), out (exit), in/out (position reverse) or out by (closing position with an opposite one). There are the following types of deals:
    -   Sell — selling a financial instrument.
    -   Buy — buying a financial instrument.
    -   Balance — top-up of balance via a manager terminal.
    -   Credit — crediting via a manager terminal.
    -   Charge — other financial operations on the account that do not belong to any of categories.
    -   Correction — manual correction of a client's balance.
    -   Bonus — accrual of bonuses. Operations of this type affect the credit assets of a client (["Credit"](/en/docs/mt5/platform/administration/admin_accounts/account_edit#personal) field).
    -   Commission — accrual of commission.
    -   Daily commission — deal of charging [commission](/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_calculation) at the end of a trading day.
    -   Monthly commission — deal of charging commission at the end of a month.
    -   Agent commission — deal of charging agent commission (used during an [instant charge](/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge)).
    -   Daily agent commission — deal of accruing agent commission at the end of a trading day.
    -   Monthly agent commission — deal of accruing agent commission at the end of a month.
    -   Interest rate — deal of [accruing annual interest](/en/docs/mt5/platform/administration/admin_groups/groups_settings#interest) at the end of a month.
    -   Canceled buy and Canceled sell — canceled deal. Such deal types are possible, for example, when working with an external trading system via a [gateway](/en/docs/mt5/platform/administration/admin_gateways). A deal can be canceled in an external trading system. In this case, the type of a previously performed deal in the platform (Buy or Sell) is changed to Canceled buy or Canceled sell respectively. At the same time, profit/loss of such a deal is reset. A client's position is then recalculated and an appropriate profit/loss is deposited/withdrawn in a separate balance deal. Deal cancellation does not entail changes in client orders history. Canceled buy and Canceled sell type deals do not participate in an account financial status calculation and are not considered in [positions recalculation](/en/docs/mt5/platform/administration/admin_accounts/account_edit#check_fix).
    -   Dividend — paying taxable dividends.
    -   Franked dividend — paying non-taxable dividends (tax is paid by a company, not a client).
    -   Tax — charging a tax.
    -   SO Compensation — negative balance [compensation](/en/docs/mt5/platform/administration/admin_groups/groups_settings#compensate) after a Stop Out.
    -   SO Credit Compensation — [resetting](/en/docs/mt5/platform/administration/admin_groups/groups_settings#so_credit) credit funds to zero after the negative balance compensation.
-   Volume — deal volume.
-   Closed volume — position volume closed by this deal. This field enables convenient working with reversal deals. In addition to the total volume of the executed deal, which is opposite to the current position, you can view the closed volume. This ability is especially useful if the initial reversed position is composed of several deals, and its total volume is not explicitly visible.
-   Symbol — [financial instrument](/en/docs/mt5/platform/administration/admin_symbols) of the deal.
-   Price — deal price.
-   Value — deal value in client deposit currency. The rate of conversion to deposit currency is shown in the "Margin rate" field. The field is used only for [Exchange\* calculation type](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation) symbols and groups with the ["for Stock Exchange, based on margin discount rates" risk management type](/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk).  
    In case of exchange risk accounting, each deal affects the account balance: the deal value is charged or deducted from the balance. In other words, the system uses the Value field here (not the Profit one, as is the case with OTC accounting). The same applies to [verifying the balance using the trading history](/en/docs/mt5/platform/administration/admin_accounts/account_edit#check_fix): the values of deals (rather than their results) are verified. Thus, if you change the deal price for some reason, make sure to update the Value field as well, since it is not recalculated automatically. Otherwise, the value change result is not displayed on the account balance after its verification and correction using the trading history.
-   Stop loss — the Stop Loss level. Stop Loss values for entry and reversal deals are set in accordance with the Stop Loss of orders, which initiated these deals. The Stop Loss values ​​of appropriate positions as of the time of position closing are used for exit deals.
-   Take profit — the Take Profit level. Take Profit values for entry and reversal deals are set in accordance with the Take Profit of orders, which initiated these deals. The Take Profit values ​​of appropriate positions as of the time of position closing are used for exit deals.
-   Reason — reasons for deal execution:
    -   Client — deal performed by a client manually through the client terminal.
    -   Expert — deal performed by a client with using an Expert Advisor.
    -   Dealer — deal performed by a dealer through the manager terminal.
    -   Stop loss — deal performed as a result of Stop Loss activation.
    -   Take profit — deal performed as a result of Take Profit activation.
    -   Stop out — deal performed when the client reached the [Stop out level](/en/docs/mt5/platform/administration/admin_groups/groups_settings#stopout).
    -   Rollover — deal performed when reopening a position for charging [swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps).
    -   External Client — deal performed by a client from an external trading system.
    -   Variation margin — deal performed for accruing variation margin. Such deals are executed in pairs: one deal closes an existing position in order to register the result (accrue the variation margin), the second deal re-opens the position with the same ticket, but at the new Close price. The position ticket is written to the "Position" field of both deals.
    -   Gateway — deal performed by a MetaTrader 5 gateway that had connected to the trading platform.
    -   Signal — deal performed as a result of copying a [trade signal](https://www.mql5.com/en/signals) according to a subscription in the client terminal.
    -   Settlement — deal performed as a result of performing operations connected with the settlement of a futures contract/option. Not used at the moment.
    -   Transfer — deal performed due to transferring a position at the settlement price to a new symbol with the same underlying asset. Not used at the moment.
    -   Synchronization — deal performed as a result of [synchronization](/en/docs/mt5/platform/administration/admin_accounts/account_edit#trade_accounts) of an account's trade state with an external system.
    -   External Service — deal performed from an external trading system for technical reasons (for example, to correct the trade state of a client).
    -   Mobile — the deal is conducted via the MetaTrader 5 mobile terminal for Android or iPhone.
    -   Web — the deal is conducted via the web terminal.
    -   Split — the deal is conducted as a result of a symbol split.
    -   Corporate action — deal created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.
    -   Migration — deal is created while importing clients' trading operations from the MetaTrader 4 server.
-   Expert ID — the identifier (magic number) of an Expert Advisor that has executed this deal in the client terminal.

-   Party ID — account number in the external system. This field is used for additional trade monitoring when operating as an Ultency liquidity provider.  
       
    To connect to a liquidity provider in Ultency, a broker is assigned a single omnibus account through which all client orders are routed. By default, the liquidity provider has no information about the initiators of trading operations on the broker's side. If necessary, brokers can optionally transmit the trading account number for each executed operation. This can be done by enabling the '[Send Party ID](/en/docs/mt5/platform/administration/ultency/ultency_connect#party_id)' option in connection settings.  
       
    The corresponding account numbers will be stored in the new 'Party ID' field in orders and deals routed to the provider. When reviewing trades on a broker's omnibus account, the liquidity provider will be able to distinguish between them.

-   Commission — commission charged for deal execution. The field is only used for the standard commission charged immediately. [Commission](/en/docs/mt5/platform/administration/admin_groups/groups_comissions) settings are specified for each group separately.
-   Fee — fee charged for deal execution. The field is used for the [Fee](/en/docs/mt5/platform/administration/admin_groups/groups_comissions#type) commission type.
-   Agent commission — agent commission fees for the deal. Parameters of [agent commissions](/en/docs/mt5/platform/administration/admin_groups/groups_comissions) are specified for each group separately.
-   Swap — charged swap.
-   Profit — profit gained from the deal.
-   Position price — [open price of a position](/en/docs/mt5/platform/administration/admin_positions#open_price), which has been closed by this deal. This field is filled for deals that have the "out" or "in/out" type.

-   Gateway Price — the gateways provide a built-in option to set [markups](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#translation) for the prices arriving from an external system. Markups apply not only to prices shown in Market Watch, but also to prices at which trades are executed on the platform side. The "Gateway price" field contains the actual price at which the deal was executed on the external system side (before markups). For further details, please read "[Gateway price, volume, and action](/en/docs/mt5/platform/administration/admin_deals#gateway)".
-   Gateway — direction and volume with which the deal is actually routed to an external trading system through the gateway. For further details, please read "[Gateway price, volume, and action](/en/docs/mt5/platform/administration/admin_deals#gateway)".
-   Raw profit — profit/loss of the committed deal. The profit/loss is represented in the [profit currency of the symbol](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_currency#profit_currency) the deal is performed by.

-   Comment — a comment to the deal. Additional information can be written in the comment field. For example, a comment indicating an account for whose trades an agent receives the commission is automatically added to the [agent commission](/en/docs/mt5/platform/administration/admin_groups/groups_comissions) deals;
-   External ID — a unique identifier of the deal in external systems.
-   Dealer ID — the number of the [dealer's](/en/docs/mt5/platform/administration/admin_managers#dealing_permission) account who processed this deal. "0" specified in this field means that the deal was processed without a dealer.
-   Modifications — if the deal is changed manually, this field displays who implemented the changes:
    -   Administrator — deal changed by an administrator.
    -   Manager — open price changed by a manager.
    -   Position — deal modification data was inherited from the position closed by that deal.
    -   Restore — deal restored.
    -   Admin API — deal changed via Manager API administrator interface.
    -   Manager API — deal changed via Manager API manager interface.
    -   Server API — deal changed via Server API.
    -   Gateway API — deal changed via Gateway API.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Deals that close <a href="/en/docs/mt5/platform/administration/admin_positions#modification" class="topiclink">positions</a> fully or partially inherit their modification flags. After closing, no separate entry about the position remains in the database. In order not to lose data on modifications, the flags are copied to the deal closing the position. In this case, the additional Position modification flag is added to the deal meaning that the flags were inherited from the position. When inheriting, the deal modification flags are not lost. Instead, they are added to the position flags.</span></li><li class="p_tableatten"><span class="f_tableatten">The deals changed by an administrator or manager, as well as restored deals are highlighted in the list in red.</span></li><li class="p_tableatten"><span class="f_tableatten">Use <a href="/en/docs/mt5/platform/administration/admin_reports/trade_modification_report" class="topiclink">Trade Modification Report</a> to obtain information about all modified trade operations.</span></li></ul></td></tr></tbody></table>

-   Profit rate — exchange rate of the deal profit currency to the trader's group [deposit currency](/en/docs/mt5/platform/administration/admin_groups/groups_settings#currency);
-   Margin rate — exchange rate of the margin currency to the trader's deposit currency. The value depends on the deal direction. For buy deals, it is the rate of margin currency selling for the deposit currency; for Buy deals it is the rate of currency margin buying for the deposit currency.
-   Market Bid — the market Bid price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.
-   Market Ask — the market Ask price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.
-   Market Last — the market Last price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.

If a manager's account has permissions to ["Change orders"](/en/docs/mt5/platform/administration/admin_managers#dealing_permission), any field in this window can be edited. After all changes have been made, press "Save".

### Gateway price, volume, and action [#](admin_deals#gateway)

A set of the fields  "Gateway price" and "Gateway" (direction and volume)  provides a clear and unambiguous description of how a deal is routed to an external system. Using these fields, you can implement various coverage strategies, including full, partial, and opposite.

The positions that are opened or modified as a result of external deal execution inherit the relevant properties. In the case of a position modification, the values are applied to the existing position. For example, a Buy 1.00 EURUSD at 1.12060 deal was opened in the platform. In the external system, the deal was covered by 30%:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution in an external system</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Deal in the platform</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Position in the platform</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway price</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12058 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12058 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12058 (external system price)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway volume</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway action</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td></tr></tbody></table>

The user then increased the position by opening another Buy 1.00 EURUSD at 1.12050 deal in the platform. In the external system, the deal was also covered by 30%:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution in an external system</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Deal in the platform (IMTDeal)</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Position in the platform</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway price</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12048 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12048 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12053 (weighted average price: (1.12058 * 0.3 + 1.12048 * 0.3)/(0.3 + 0.3))</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway volume</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">60 000 000 (0.6 lots, total volume)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway action</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td></tr></tbody></table>

The user then partially closed the position by executing a Sell 0.50 EURUSD at 1.12070 deal. The relevant part of the positions is closed in the external system:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution in an external system</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Deal in the platform (IMTDeal)</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Position in the platform</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway price</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12068 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12068 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12053 (weighted average price unchanged)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway volume</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">15 000 000 (0.15 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">15 000 000 (0.15 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">45 000 000 (0.45 lots, remaining volume in the external system)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway action</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Sell</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Sell</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Purchase (direction unchanged)</span></p></td></tr></tbody></table>

### Visualization [#](admin_deals#visualization)

In this section, execution of a trading operation is visualized on the tick chart of the appropriate symbol.

![Trading visualization](/en/docs/mt5/platform/img/order_visualization.png "Trading visualization")

### Nearest ticks before and after the operation [#](admin_deals#ticks)

When examining disputable situations with traders, it is often necessary to analyze quotes which were broadcasted at the trading operation execution time. The relevant quote data can be obtained in a couple of clicks. Open operation details and navigate to the "Ticks" section. The terminal will automatically request the quote history from the server for the entire day on which the operation was performed. The nearest quote to operation execution time will be automatically selected in the list of received quotes.

![Nearest ticks before and after the operation](/en/docs/mt5/platform/img/order_ticks.png "Nearest ticks before and after the operation")

### Operation journal [#](admin_deals#journal)

This is another tool to assist during the follow-up operation examination. There is no need to manually request [logs from the server](/en/docs/mt5/platform/administration/admin_network/network_journal) and to filter its records. Open operation details, navigate to the "Journal" section and the terminal will automatically request the necessary logs from the server, using ticket and time interval filters (from the operation date to the current day).

![Operation journal](/en/docs/mt5/platform/img/order_journal.png "Operation journal")

### Trading operation report [#](admin_deals#report)

The trading operation details available in the editing dialogs can be saved as a report. The report contains the entire chain of operations from an order to a position, visualization on a tick chart, extract from the server log and the trading account overall status.

To generate a file, click "Report" in the context menu in the "[Overview and related operations](/en/docs/mt5/platform/administration/admin_deals#connected_transactions)" section. Next, select data to be saved: account state, trading totals, logs, tick chart, etc.

![Trading operation report](/en/docs/mt5/platform/img/position_report.png "Trading operation report")

Select the path on the disk and click "Save".

## Backup Databases of Deals [#](admin_deals#backup)

[Backup copies](/en/docs/mt5/platform/components/backup_server/backup_server_features#file) are copies of the deal database at certain points in time. They are created daily on the [backup server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#enable_backups). To get the list of available backup copies, select "More backups..." and specify a time period:

![Period of backups](/en/docs/mt5/platform/img/backups_period.png "Period of backups")

After specifying a period the additional items will appear in the field of choosing database — all the backups made for the specified period of time. Then you should [request](/en/docs/mt5/platform/administration/admin_deals#request) deals from the selected database. Any deal can be restored to the current database using the "![Restore](/en/docs/mt5/platform/img/restore_icon.png "Restore") Restore" command of the context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Restored deals are not deleted from the backup databases.</span></p></td></tr></tbody></table>

## Context Menu [#](admin_deals#context)

The context menu of the "Deals" section contains the following commands:

-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — modify a selected order;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected order;
-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — execute a [request](/en/docs/mt5/platform/administration/admin_deals#request);
-   ![Restore](/en/docs/mt5/platform/img/restore_icon.png "Restore") Restore — restore a selected deal from a backup database to the current one. This command is active only if a backup database is currently requested;
-   Copy As — copy deals selected in the list:

-   ![Copy as lines](/en/docs/mt5/platform/img/copy_button.png "Copy as lines") Lines — copy entire selected information.
-   List of Logins — copy the list of logins only.
-   List of Tickets — copy the list of tickets only.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export — [export](/en/docs/mt5/platform/administration/common_info/export) requested orders as a \*.HTM, \*.HTML file or as a \*.CSV file;
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request the [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) entries by a selected deal;
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Show Milliseconds — show the time of trade operations with a millisecond precision;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with deals;
-   Columns — using this sub-menu, one can choose which [details of deals](/en/docs/mt5/platform/administration/admin_deals#view) will be displayed in the list.

[Orders](/en/docs/mt5/platform/administration/admin_orders)

[Positions](/en/docs/mt5/platform/administration/admin_positions)