# Positions

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_positions

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Positions

# Positions

This section allows working with all current positions of your traders.

![Positions](/en/docs/mt5/platform/img/positions.png "Positions")

Depending  on the items chosen in the context menu, different [information about positions](/en/docs/mt5/platform/administration/admin_positions#view) is displayed here. Positions can be sorted out by any field. To do it, click on its name.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The trading platform supports two position accounting systems: <a href="/en/docs/mt5/platform/administration/admin_groups/group_position" class="topiclink">netting and hedging</a>.</span></p></td></tr></tbody></table>

## Requesting Positions [#](admin_positions#request)

To view current positions, compose a request in the line located in the lower part of the section. The request can be performed:

-   By Groups  
    To do it, select a group from the dropdown list.
-   By Logins  
    To do it, should specify one or several logins separated with commas.

To request all positions, specify the asterisk (\*).

Further the following request parameters can be specified:

-   Trading instruments for which positions will be requested. One symbol or a group of symbols can be selected from the list. Optionally, you can specify a comma separated list of trading instruments or groups of symbols. For example, Forex\\\*, CFD\\\*, Metals\\GOLD. Please note that filtering is performed on the server side, and not on the administrator terminal side. To obtain data on other instruments, send another request. The request is performed for all financial instruments by default.
-   Further you can specify from which database positions should be requested: current database or one of [backups](/en/docs/mt5/platform/administration/admin_positions#backup). To perform the request, press the "Request" button or execute the "![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request" command of the [context menu](/en/docs/mt5/platform/administration/admin_positions#context).

## Viewing a Position [#](admin_positions#view)

To view or to edit a position, double-click on it in the list. The trading operation dialog is a fully-featured tool with a plethora of advanced features, such as the display of the structure of operations, visualization, tick history and logs.

![Position viewing](/en/docs/mt5/platform/img/position_view.png "Position viewing")

### Account details [#](admin_positions#account_details)

The upper part of the dialog features brief information about the account, on which the operation was performed: name, login, groups and leverage. Click on this line to view [account details](/en/docs/mt5/platform/administration/admin_accounts/account_edit).

### Overview and related operations [#](admin_positions#connected_transactions)

This block shows the orders and deals related to the selected position, i.e. the entire history of position opening and change. Thus you can easily access the entire chain of related actions. Select an operation from the tree and all relevant parameters will be instantly displayed in the bottom part.

### Trading operation details [#](admin_positions#details)

The following parameters are indicated for positions:

-   Login — [account](/en/docs/mt5/platform/administration/admin_accounts) number the position was opened on.
-   Position — ticket (unique number) of the position. Usually, a position ticket matches the [ticket of the order](/en/docs/mt5/platform/administration/admin_orders) used to open the position. The exceptions are positions re-opened as a result of service operations or opened without placing an order. The tickets may be different for positions having the following [opening reasons](/en/docs/mt5/platform/administration/admin_positions#reason):
    -   Rollover — charging swaps with position re-opening
    -   Split — re-opening a position after a split
    -   Variation margin — re-opening a position after charging a variation margin
    -   Synchronization — opening a position when synchronizing with an external system (without a previous order)
    -   Transfer — relocating a position with a calculated price to a new symbol with the same underlying asset

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Tickets of positions having other opening reasons match initial orders.</span></p><p class="p_tableatten"><span class="f_tableatten">A position ticket changes when it is reversed in a single <a href="/en/docs/mt5/platform/administration/admin_deals#action" class="topiclink">in/out deal</a> (used in the <a href="/en/docs/mt5/platform/administration/admin_groups/group_position" class="topiclink">netting mode</a>).</span></p></td></tr></tbody></table>

-   Open Time — time when the position was opened.
-   Update Time — last position modification time (when its volume was changed). This is actually the time of the last deal for the financial instrument which corresponds to this position. This time does not change when Stop Loss or Take Profit is modified or when the position is edited via the Administrator terminal or API.
-   Type — type of the position - buy or sell.
-   Symbol — [symbol](/en/docs/mt5/platform/administration/admin_symbols) the position was opened for.
-   Volume — the current position volume in lots.

-   Gateway Price — the gateways provide a built-in option to set [markups](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#translation) for the prices arriving from an external system. Markups apply not only to prices shown in Market Watch, but also to prices at which trades are executed on the platform side. The "Gateway price" field contains the actual price at which the position was opened on the external system side (before markups). For further details, please read "[Gateway price, volume, and action](/en/docs/mt5/platform/administration/admin_positions#gateway)".
-   Gateway — direction and volume with which the position is actually routed to an external trading system through the gateway. For further details, please read "[Gateway price, volume, and action](/en/docs/mt5/platform/administration/admin_positions#gateway)".

-   Reason — reasons for position opening:
    -   Client — opened by a client manually through the client terminal.
    -   Expert — opened by a client with using an Expert Advisor.
    -   Dealer — opened by a dealer through the manager terminal.
    -   Stop loss — not used for positions.
    -   Take profit — not used for positions.
    -   Stop out — not used for positions.
    -   Rollover — opened when reopening a position for charging [swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps).
    -   External Client — opened by a client from an external trading system.
    -   Variation margin — not used for positions.
    -   Gateway — opened by a MetaTrader 5 gateway that had connected to the trading platform.
    -   Signal — opened as a result of copying a [trade signal](https://www.mql5.com/en/signals) according to a subscription in the client terminal.
    -   Settlement — opened as a result of performing operations connected with the settlement of a futures contract/option. Not used at the moment.
    -   Transfer — opened due to transferring a position at the settlement price to a new symbol with the same underlying asset. Not used at the moment.
    -   Synchronization — opened as a result of [synchronization](/en/docs/mt5/platform/administration/admin_accounts/account_edit#trade_accounts) of an account's trade state with an external system.
    -   External Service — opened from an external trading system for technical reasons (for example, to correct the trade state of a client).
    -   Mobile — position opened via the MetaTrader 5 mobile terminal for Android or iPhone.
    -   Web — position opened via the web terminal.
    -   Split — position opened as a result of a symbol split.
    -   Corporate action — position created as a result of a corporate action, such as consolidating or renaming securities, transferring a client to a different account, etc. API applications set this flag for service operations so that the platform does not account for such corporate actions in commission calculations.
    -   Migration — position opened as a result of import of clients' trading operations from the MetaTrader 4 server.
-   Price — weight-average price of the position opening: (price of deal 1 \* volume of deal 1 + ... + price of deal N \* volume of deal N) / (volume of deal 1 + ... + volume of deal N). The accuracy of rounding of the average weighted price is equal to the number of decimal places in the symbol price plus three additional digits.  
       
    The weighted average price is calculated sequentially, as the position increases or is partially closed. For example, a client trading in a netting group has executed the following series of trades:  
       
    1\. Buy 0.01 EURUSD at 1.10050 (In)  
    2\. Buy 0.02 EURUSD at 1.10052 (In)  
    3\. Sell 0.02 EURUSD at 1.10067 (Out)  
    4\. Buy 0.01 EURUSD at 1.10056 (In)  
       
    At each step, the following value will be displayed in the position open price:  
       
    1\. The value of 1.10050 as is, since the position entry was performed in one trade  
    2\. When the position is increased, the weighted average open price is calculated: (1.10050 \* 0.01 + 1.10052 \* 0.02) / (0.01 + 0.02) = 1.10051333  
    3\. After partial closing of the position (0.02 lots out of 0.03 are closed), the client is left with a 0.01-lot position with the open price of 1.10051333  
    4\. When the position is further increased, the new weighted average price is calculated taking into account the previous calculated one: (1.10051333 \* 0.01 + 1.10056 \* 0.01) /  (0.01 + 0.01) = 1.10053666‬  
     
-   Stop Loss — the Stop Loss level of the position.
-   Take Profit — the Take Profit level of the position.
-   Profit — the current profit on this position. The profit does not include swap and commission.
-   Current Price — the current price of the symbol of the position.
-   Swap — swaps charged.
-   Margin Rate — exchange rate of the [margin currency](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_currency#margin_currency) to the trader's [deposit currency](/en/docs/mt5/platform/administration/admin_groups/groups_settings#currency). It is usually calculated and registered at the moment when a position is opened or its volume is modified. The rate can be recalculated at the end of the trading day if the relevant option is enabled in [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula#recalculate_margin).

-   Profit rate — exchange rate of the position profit currency to the trader's group [deposit currency](/en/docs/mt5/platform/administration/admin_groups/groups_settings#currency).

-   Comment — a comment to the position. A comment to a position is inherited from the last [deal](/en/docs/mt5/platform/administration/admin_deals) by the symbol of the position.
-   Expert — the identifier (magic number) of an Expert Advisor that has opened this position in the client terminal.
-   ID — a unique identifier of the position in external systems;
-   Dealer — the login of a dealer (gateway) that processed an order, which opened the position. If "0" is specified in this field, it means that the order was processed without a dealer.
-   Disable activation — additional conditions (flags), with which [order](/en/docs/mt5/platform/administration/admin_orders#activation) activation is prohibited. The flags can be set by Gateway API when orders are sent to an external system. For example, if activation of stop loss and take profit must be controlled by an external system, a flag disabling activation on the MetaTrader 5 side can be set for the order. Order flags are inherited by positions created upon order execution. Available flags:
    -   Limit — no processing of limit level hitting.
    -   Stop — no processing of stop level hitting.
    -   Stop Limit — no processing of stop limit level hitting.
    -   SL — no processing of Stop Loss activation.
    -   TP — no processing of Take Profit activation.
    -   Stop Out — no processing of Stop Out activation.
    -   Expiration — no processing of expired order cancellation.
-   Modifications — if the position is changed manually, this field displays who implemented the changes:
    -   Administrator — position changed by an administrator.
    -   Manager — open price changed by a manager.
    -   Restore — position restored.
    -   Admin API — position changed via Manager API administrator interface.
    -   Manager API — position changed via Manager API manager interface.
    -   Server API — position changed via Server API.
    -   Gateway API — position changed via Gateway API.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/platform/administration/admin_deals#modification" class="topiclink">Deals</a> that close positions fully or partially inherit their modification flags. After closing, no separate entry about the position remains in the database. In order not to lose data on modifications, the flags are copied to the deal closing the position. In this case, the additional Position modification flag is added to the deal meaning that the flags were inherited from the position. When inheriting, the deal modification flags are not lost. Instead, they are added to the position flags.</span></li><li class="p_tableatten"><span class="f_tableatten">The positions changed by an administrator or manager, as well as restored positions are highlighted in the list in red.</span></li><li class="p_tableatten"><span class="f_tableatten">Use <a href="/en/docs/mt5/platform/administration/admin_reports/trade_modification_report" class="topiclink">Trade Modification Report</a> to obtain information about all modified trade operations.</span></li></ul></td></tr></tbody></table>

### Gateway price, volume, and action [#](admin_positions#gateway)

A set of the fields  "Gateway price" and "Gateway" (direction and volume)  provides a clear and unambiguous description of how a position is routed to an external system. Using these fields, you can implement various coverage strategies, including full, partial, and opposite.

The fields are filled in [deals](/en/docs/mt5/platform/administration/admin_deals) that are created in the platform as a result of trade execution in an external system. The same values are also inherited by the position that is opened or modified as a result of the deal execution. In the case of a position modification, the values are applied to the existing position. For example, a Buy 1.00 EURUSD at 1.12060 deal was opened in the platform. In the external system, the deal was covered by 30%:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution in an external system</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Deal in the platform</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Position in the platform</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway price</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12058 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12058 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12058 (external system price)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway volume</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway action</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td></tr></tbody></table>

The user then increased the position by opening another Buy 1.00 EURUSD at 1.12050 deal in the platform. In the external system, the deal was also covered by 30%:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution in an external system</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Deal in the platform (IMTDeal)</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Position in the platform</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway price</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12048 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12048 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12053 (weighted average price: (1.12058 * 0.3 + 1.12048 * 0.3)/(0.3 + 0.3))</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway volume</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">30 000 000 (0.3 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">60 000 000 (0.6 lots, total volume)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway action</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Buy</span></p></td></tr></tbody></table>

The user then partially closed the position by executing a Sell 0.50 EURUSD at 1.12070 deal. The relevant part of the positions is closed in the external system:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Field</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution in an external system</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Deal in the platform (IMTDeal)</span></p></th><th class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Position in the platform</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway price</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12068 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12068 (external system price)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">1.12053 (weighted average price unchanged)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway volume</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">15 000 000 (0.15 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">15 000 000 (0.15 lots)</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">45 000 000 (0.45 lots, remaining volume in the external system)</span></p></td></tr><tr class="table"><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Gateway action</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Sell</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Entry for Sell</span></p></td><td class="table" style="width:25%;"><p class="p_fortable"><span class="f_fortable">Purchase (direction unchanged)</span></p></td></tr></tbody></table>

### Visualization [#](admin_positions#visualization)

In this section, execution of a trading operation is visualized on the tick chart of the appropriate symbol.

![Trading visualization](/en/docs/mt5/platform/img/order_visualization.png "Trading visualization")

### Nearest ticks before and after the operation [#](admin_positions#ticks)

When examining disputable situations with traders, it is often necessary to analyze quotes which were broadcasted at the trading operation execution time. The relevant quote data can be obtained in a couple of clicks. Open operation details and navigate to the "Ticks" section. The terminal will automatically request the quote history from the server for the entire day on which the operation was performed. The nearest quote to operation execution time will be automatically selected in the list of received quotes.

![Nearest ticks before and after the operation](/en/docs/mt5/platform/img/order_ticks.png "Nearest ticks before and after the operation")

### Operation journal [#](admin_positions#journal)

This is another tool to assist during the follow-up operation examination. There is no need to manually request [logs from the server](/en/docs/mt5/platform/administration/admin_network/network_journal) and to filter its records. Open operation details, navigate to the "Journal" section and the terminal will automatically request the necessary logs from the server, using ticket and time interval filters (from the operation date to the current day).

![Operation journal](/en/docs/mt5/platform/img/order_journal.png "Operation journal")

### Trading operation report [#](admin_positions#report)

The trading operation details available in the editing dialogs can be saved as a report. The report contains the entire chain of operations from an order to a position, visualization on a tick chart, extract from the server log and the trading account overall status.

To generate a file, click "Report" in the context menu in the "[Overview and related operations](/en/docs/mt5/platform/administration/admin_positions#connected_transactions)" section. Next, select data to be saved: account state, trading totals, logs, tick chart, etc.

![Trading operation report](/en/docs/mt5/platform/img/position_report.png "Trading operation report")

Select the path on the disk and click "Save".

## Backup Databases of Positions [#](admin_positions#backup)

[Backup copies](/en/docs/mt5/platform/components/backup_server/backup_server_features#file) are copies of the position database at certain points in time. They are created daily on the [backup server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#enable_backups). To get the list of available backup copies, select "More backups..." and specify a time period:

![Period of backups](/en/docs/mt5/platform/img/backups_period.png "Period of backups")

After specifying a period the additional items will appear in the field of choosing database — all the backups made for the specified period of time. Then you should [request](/en/docs/mt5/platform/administration/admin_deals#request) positions from the selected database. Any position can be restored to the current database using the "![Restore](/en/docs/mt5/platform/img/restore_icon.png "Restore") Restore" command of the context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Restored positions are not deleted from the backup databases.</span></li><li class="p_tableatten"><span class="f_tableatten">When a position is restored, the deals that formed the position are not restored.</span></li></ul></td></tr></tbody></table>

## Context Menu [#](admin_positions#context)

The context menu of this section contains the following commands:

-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — open a selected position for editing;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected position;
-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — [request](/en/docs/mt5/platform/administration/admin_positions#request) positions;
-   ![Restore](/en/docs/mt5/platform/img/restore_icon.png "Restore") Restore — restore a selected position from a backup database to the current one. This command is active only if a backup database is currently requested;
-   Copy As — copy positions selected in the list:

-   ![Copy as lines](/en/docs/mt5/platform/img/copy_button.png "Copy as lines") Lines — copy entire selected information.
-   List of Logins — copy the list of logins only.
-   List of Tickets — copy the list of tickets only.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export — [export](/en/docs/mt5/platform/administration/common_info/export) requested positions as a \*.HTM, \*.HTML file or as a \*.CSV file;
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Show Milliseconds — show the time of trade operations with a millisecond precision;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with positions;
-   Columns — using this sub-menu, one can choose which [details of positions](/en/docs/mt5/platform/administration/admin_positions#view) will be displayed in the list.

[Deals](/en/docs/mt5/platform/administration/admin_deals)

[Gateways](/en/docs/mt5/platform/administration/admin_gateways)