# Macros

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_macros

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
                -   [Common Settings](/en/docs/mt5/platform/administration/automation/automation_common)
                -   [Triggers](/en/docs/mt5/platform/administration/automation/automation_trigger)
                -   [Conditions](/en/docs/mt5/platform/administration/automation/automation_condition)
                -   [Actions](/en/docs/mt5/platform/administration/automation/automation_action)
                -   [Macros](/en/docs/mt5/platform/administration/automation/automation_macros)
                -   [Statistics](/en/docs/mt5/platform/administration/automation/automation_statistics)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Automations](/en/docs/mt5/platform/administration/automation)Macros

# Macros

Automation actions for [sending various messages](/en/docs/mt5/platform/administration/automation/automation_action#message) (SMS, Push, emails) and [web requests](/en/docs/mt5/platform/administration/automation/automation_action#external) support macros. They allow substituting different data depending on a recipient (account) and a triggered event. For inserting, set the macro name between #..# or use the context menu.

![Use the context menu to insert macros](/en/docs/mt5/platform/img/automation_macros.png "Use the context menu to insert macros")

All available macros are divided into several categories depending on what information they provide in the text.

## Trading Account [#](automation_macros#account)

These macros substitute message recipient's [account data](/en/docs/mt5/platform/administration/admin_accounts/account_edit).

-   Login (#LOGIN#) — email/message receipient's account number.
-   Full Name (#USERNAME#) — recipient's first and last name.
-   First Name (#USER\_FIRST\_NAME#) — recipient's first name.
-   Last Name (#USER\_LAST\_NAME#) — recipient's last name.
-   Middle Name (#USER\_MIDDLE\_NAME#) — recipient's middle name.
-   Currency (#USER\_CURRENCY#) — recipient's deposit currency. It is defined by the user's [group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#currency).
-   Company (#USER\_COMPANY#) — name of a company a user belongs to. It is defined by the user's [group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#company).
-   Creation Date (#USER\_CREATION\_DATE#) — account creation date.
-   Registration date (#USER\_REGISTRATION\_ELAPSED#) — the number of days that have elapsed since account creation.
-   Last Access Time (#USER\_LASTTIME#) — last account access time.
-   Days since last login (#USER\_LASTTIME\_ELAPSED#) — the number of days that have elapsed since the last connection to the account.
-   Online status (#USER\_ONLINE\_STATUS#) — the status of account connection to the trade server: Online or Offline.
-   Language (#USER\_LANGUAGE#) — user's language.
-   Status (#USER\_STATUS#) — user status (resident/non-resident).
-   ID Number (#USER\_ID#) — user's document ID.
-   Email (#USER\_EMAIL#) — user's email.
-   Group (#USER\_GROUP#) — user's group.
-   Previous (#USER\_GROUP\_PREVIOUS#) — the macro is only used with the "[Trade account group change](/en/docs/mt5/platform/administration/automation/automation_trigger#account)". Use it to get the group from which the account was transfered.
-   Phone (#USER\_PHONE#) — user's phone number.
-   Country (#USER\_COUNTRY#) — user's country.
-   City (#USER\_CITY#) — user's city.
-   State (#USER\_STATE#) — user's region.
-   Zip Code (#USER\_ZIP\_CODE#) — user's zip code.
-   Address (#USER\_ADDRESS#) — user address.
-   Comment (#USER\_COMMENT#) — comment to a user account.
-   Bank Account (#USER\_BANK\_ACCOUNT#) — bank account number specified in the account.
-   Agent (#USER\_AGENT\_ACCOUNT#) — agent account number specified in the account.
-   Balance (#USER\_BALANCE#) — recipient's balance.
-   Credit (#USER\_CREDIT#) — credit funds on the recipient's account.
-   Equity (#USER\_EQUITY#) — account equity.
-   Leverage (#USER\_LEVERAGE#) — account leverage.
-   Margin (#USER\_MARGIN#) — amount of funds reserved on the account as margin.
-   Free Margin (#USER\_MARGIN\_FREE#) — amount of free margin.
-   Margin Level (#USER\_MARGIN\_LEVEL#) — margin level.
-   Position Total (#USER\_POSITIONS\_TOTAL#) — number of open positions on the account when sending a message.
-   Orders Total (#USER\_ORDERS\_TOTAL#) — current number of active pending orders on the account when sending a message.
-   Profit (#USER\_PROFIT#) — floating profit on the account when sending a message.
-   Lead Source (#USER\_LEAD\_SOURCE#) — lead source specified in the account.
-   Lead Campaign (#USER\_LEAD\_CAMPAIGN#) — marketing campaign which led to opening the account.
-   Color (#USER\_COLOR#) — the color by which the client's requests to execute trading operations will be displayed in the Manager terminal.
-   Full JSON (#USER\_JSON#) — complete data on user account in JSON format.
-   Own funds percentage (#USER\_OWN\_FUNDS\_PERCENT#) — client's funds share consisting of money the client deposited to their account. The calculation equation: (1 - (Credit / Equity)) \* 100. Find out more in the [Conditions](/en/docs/mt5/platform/administration/automation/automation_condition#own_funds) section.
-   Own funds volume (#USER\_OWN\_FUNDS\_VOLUME#) — client's funds volume consisting of money the client deposited to their account. The calculation equation: Equity - Credit.
-   IP address (#USER\_IP\_ADDRESS#) — address connection to the trade server was established from. Use the macro with triggers from the [Connections](/en/docs/mt5/platform/administration/automation/automation_trigger#connection) section.
-   Client ID (#CLIENT\_ID#) — the unique identifier of the [client](/en/docs/mt5/platform/administration/clients) with whom the trading account is associated.

## Manager [#](automation_macros#manager)

These macros are used in a text to substitute the [data of a manager account](/en/docs/mt5/platform/administration/admin_managers) with which the event is associated. Used only with triggers from the [Managers](/en/docs/mt5/platform/administration/automation/automation_trigger#managers) section.

-   Login (#MANAGER\_LOGIN#) — the account of the manager who performed the action.

## Group [#](automation_macros#group)

These macros substitute target account [group data](/en/docs/mt5/platform/administration/admin_groups/groups_settings).

-   Name (#GROUP\_NAME#) — group name.
-   Currency (#GROUP\_CURRENCY#) — group deposit currency.
-   Company (#GROUP\_COMPANY#) — [name of a company](/en/docs/mt5/platform/administration/admin_groups/groups_settings#company) a group belongs to.
-   Email (#GROUP\_EMAIL#) — company email.
-   Support Email (#GROUP\_EMAIL\_SUPPORT#) — company technical support team email.
-   Site (#GROUP\_SITE#) — company website.
-   Support Site (#GROUP\_SITE\_SUPPORT#) — company support website.
-   Margin Call (#GROUP\_MARGIN\_CALL#) — [margin call level](/en/docs/mt5/platform/administration/admin_groups/groups_settings#margin) set for the group.
-   Stop Out (#GROUP\_STOP\_OUT#) — stop out level set for the group.
-   Full JSON (#GROUP\_JSON#) — full group description in JSON format.

## Client [#](automation_macros#client)

These macros substitute recipient's [client data](/en/docs/mt5/platform/administration/clients).

-   Title (#CLIENT\_TITLE#) — title: Mr. or Mrs.
-   First Name (#CLIENT\_FIRST\_NAME#) — client's first name.
-   Last Name (#CLIENT\_LAST\_NAME#) — client's last name.
-   Middle Name (#CLIENT\_MIDDLE\_NAME#) — client's middle name.
-   Gender (#CLIENT\_GENDER#) — client's gender.
-   Birthday (#CLIENT\_BIRTDAY#) — client's birthday.
-   Language (#CLIENT\_LANGUAGE#) — client's language.
-   Email (#CLIENT\_EMAIL#) — client's email.
-   Phone (#CLIENT\_PHONE#) — client's phone number.
-   Messengers (#CLIENT\_MESSENGERS#) — client's messenger list.
-   External ID (#CLIENT\_EXTERNAL\_ID#) — client ID in an external system.
-   Country (#CLIENT\_COUNTRY#) — client's country.
-   State (#CLIENT\_STATE#) — client's region.
-   City (#CLIENT\_CITY#) — client's city.
-   Zip Code (#CLIENT\_ZIP\_CODE#) — client's zip code.
-   Address (#CLIENT\_ADDRESS#) — client's address.
-   Nationality (#CLIENT\_NATIONALITY#) — client's citizenship.
-   Tax ID (#CLIENT\_TAX\_ID#) — client's tax ID.
-   Type (#CLIENT\_TYPE#) — client type.
-   Status (#CLIENT\_STATUS#) — client status.
-   Manager (#CLIENT\_MANAGER#) — responsible [manager](/en/docs/mt5/platform/administration/admin_managers) login.
-   Lead Source (#CLIENT\_LEAD\_SOURCE#) — lead source specified in client record.
-   Lead Campaign (#CLIENT\_LEAD\_CAMPAIGN#) — marketing campaign which led to creating the client.
-   Introducer (#CLIENT\_INTRODUCER#) — login (trading account) of the user, who introduced the client.
-   Full JSON (#CLIENT\_JSON#) — full client description in JSON format.

## Position [#](automation_macros#position)

These macros substitute in a text [data of positions](/en/docs/mt5/platform/administration/admin_positions), a change in which caused the automation task trigger (triggers from the "[Positions](/en/docs/mt5/platform/administration/automation/automation_trigger#position)" section).

-   Login (#POSITION\_LOGIN#) — the number of the [account](/en/docs/mt5/platform/administration/admin_accounts) the position as opened on.
-   Ticket (#POSITION\_TICKET#) — unique position identifier.
-   Symbol (#POSITION\_SYMBOL#) — [symbol](/en/docs/mt5/platform/administration/admin_symbols) the position was opened for.
-   Volume (#POSITION\_VOLUME#) — position volume in lots.
-   Type (#POSITION\_TYPE#) — position type: buy or sell.
-   Open price (#POSITION\_PRICE\_OPEN#) — weight-average price of the position opening: (price of deal 1 \* volume of deal 1 + ... + price of deal N \* volume of deal N) / (volume of deal 1 + ... + volume of deal N).
-   Current price (#POSITION\_PRICE\_CURRENT#) — current price of the financial symbol for which the position has been opened, at the trigger activation time.
-   Profit (#POSITION\_PROFIT#) — profit of a position at the trigger activation time.
-   Reason (#POSITION\_REASON#) — [reason](/en/docs/mt5/platform/administration/admin_positions#reason) for opening the position.
-   Creation time (#POSITION\_TIME\_CREATE#) — position opening time.
-   Update time (#POSITION\_TIME\_UPDATE#) — time when the position was last modified (when its volume was changed).

-   Dealer (#POSITION\_DEALER#) — the login of the dealer who confirmed or placed the order (deal), which caused the position to open.

-   Expert (#POSITION\_EXPERT#) — identifier (magic number) of an Expert Advisor by which a position was opened in the client terminal.
-   Comment (#POSITION\_COMMENT#) — a text comment to a position.

-   Storage (#POSITION\_STORAGE#) — swap charges.
-   Stop Loss (#POSITION\_PRICE\_SL#) —  position Stop Loss level
-   Take Profit (#POSITION\_PRICE\_TP#) — position Take Profit level.
-   Profit rate (#POSITION\_RATE\_PROFIT#) — profit currency to deposit currency conversion rate.
-   Margin rate (#POSITION\_RATE\_MARGIN#) — margin currency to deposit currency conversion rate.

-   Full JSON (#POSITION\_JSON#) — full description of the position in JSON format.

## Deal [#](automation_macros#deal)

These macros substitute in a text [data of a deal](/en/docs/mt5/platform/administration/admin_deals), an execution of which caused the automation task trigger (triggers from the "[Positions](/en/docs/mt5/platform/administration/automation/automation_trigger#position)" section).

-   Login (#DEAL\_LOGIN#) — the number of the [account](/en/docs/mt5/platform/administration/admin_accounts), on which the deal was executed.
-   Ticket (#DEAL\_TICKET#) — unique deal identifier.
-   Symbol (#DEAL\_SYMBOL#) — [financial instrument](/en/docs/mt5/platform/administration/admin_symbols) for which the deal was executed.
-   Volume (#DEAL\_VOLUME#) — deal volume in lots.
-   Type (#DEAL\_TYPE#) — [deal type](/en/docs/mt5/platform/administration/admin_deals#action): Sell, Buy, Balance etc.
-   Direction (#DEAL\_ENTRY#) — direction of a deal relative to the current [position](/en/docs/mt5/platform/administration/admin_positions): entry ("in"), exit ("out"), reversal ("in/out") or close by ("out by").
-   Price (#DEAL\_PRICE#) — deal execution price.
-   Profit (#DEAL\_PROFIT#) — the profit received from the deal.
-   Reason (#DEAL\_REASON#) — [reason](/en/docs/mt5/platform/administration/admin_deals#reason) for deal execution.
-   Time (#DEAL\_TIME#) — deal execution time.

-   Dealer (#DEAL\_DEALER#) — the login of the dealer who confirmed or placed the order, which caused the deal to execute.

-   Expert (#DEAL\_EXPERT#) — identifier (magic number) of an Expert Advisor by which the deal was executed in the client terminal.
-   Comment (#DEAL\_COMMENT#) — a text comment to a deal.

-   Commission (#DEAL\_COMMISSION#) — commission charged for deal execution.
-   Fee (#DEAL\_FEE#) — [Fee](/en/docs/mt5/platform/administration/admin_groups/groups_comissions#type) commission type.
-   Storage (#DEAL\_STORAGE#) — swap charges.
-   Closed volume (#DEAL\_VOLUME\_CLOSED#) — position volume closed by this deal.
-   Stop Loss (#DEAL\_PRICE\_SL#) — deal Stop Loss level.
-   Take Profit (#DEAL\_PRICE\_TP#) — deal Take Profit level.
-   Raw profit #DEAL\_PROFIT\_RAW# — profit/loss obtained from the execution of the deal, in the instrument's profit currency.
-   Profit rate (#DEAL\_RATE\_PROFIT#) — profit currency to deposit currency conversion rate.
-   Margin rate (#DEAL\_RATE\_MARGIN#) — margin currency to deposit currency conversion rate.
-   Market Bid (#DEAL\_PRICE\_MARKET\_BID#) — market Bid price as at the time the deal is executed by the server.
-   Market Ask (#DEAL\_PRICE\_MARKET\_ASK#) — market Ask price as at the time the deal is executed by the server.
-   Market Last (#DEAL\_PRICE\_MARKET\_LAST#) — market Last price as at the time the deal is executed by the server.

-   Full JSON (#DEAL\_JSON#) — full description of the deal in JSON format.

## Orders [#](automation_macros#order)

These macros are substitute [parameters of the order](/en/docs/mt5/platform/administration/admin_orders), with which the automation task triggering is associated ("[Scheduled account database processing](/en/docs/mt5/platform/administration/automation/automation_trigger#trade_processing)").

-   Ticket (#ORDER\_TICKET#) — the unique order number.
-   External order ID (#ORDER\_ORDER\_ID#) — order identifier in an external trading system.
-   Login (#ORDER\_LOGIN#) — the number of the [account](/en/docs/mt5/platform/administration/admin_accounts) on which the order was placed.
-   Symbol (#ORDER\_SYMBOL#) — the [financial instrument](/en/docs/mt5/platform/administration/admin_symbols) for which the order was placed.
-   Setup time (#ORDER\_TIME\_SETUP#) — time of order placing by a client.
-   Days since setup (#ORDER\_TIME\_SETUP\_ELAPSED#) — the number of days that have elapsed since the client placed the order.

-   Done time (#ORDER\_TIME\_DONE#) — order execution time.

-   Expiration time (#ORDER\_TIME\_EXPIRATION#) — order expiration date, if it was set by the client.
-   Type (#ORDER\_TYPE#) — order type: "Buy", "Sell", "Buy Limit", "Sell Limit", "Buy Stop", "Sell Stop", "Buy Stop Limit", "Sell Stop Limit" or "Close By".
-   Order price (#ORDER\_PRICE\_ORDER#) — price specified by trader for execution of the order.
-   Trigger price (#ORDER\_PRICE\_TRIGGER#) — this field is used for the "Buy Stop Limit" and "Sell Stop Limit" orders. It sets the price level at which the orders trigger and the relevant limit orders are placed.
-   Stop Loss (#ORDER\_PRICE\_SL#) — the Stop Loss level.
-   Take Profit (#ORDER\_PRICE\_TP#) — the Take Profit level.
-   Initial volume (#ORDER\_VOLUME\_INITIAL#) — volume requested in the order.
-   Remained volume (#ORDER\_VOLUME\_CURRENT#)— if the order is not filled in the volume requested by trader this field will display the remainder volume.
-   State (#ORDER\_STATE#) — current state of the order (filled, rejected, partially filled, expired, etc.).

-   Dealer (#ORDER\_DEALER#) — login of the dealer who confirmed or placed the order.

-   Expert ID (#ORDER\_EXPERT#) — identifier (magic number) of an Expert Advisor which placed the order in the client terminal.
-   Position (#ORDER\_POSITION\_ID#) — ticket of the position opened, modified or closed due to this order.
-   Comment (#ORDER\_COMMENT#) — a text comment to the order.
-   Contract size (#ORDER\_CONTRACT\_SIZE#) — the contract size of the symbol, for which an order was placed.
-   Currency (#ORDER\_CURRENCY#) — the deposit currency of the client who has placed the order.

-   Margin rate (#ORDER\_RATE\_MARGIN#) — margin currency to deposit currency conversion rate.

-   Full JSON (#ORDER\_JSON#) — full description of the order in JSON format.

## Payments [#](automation_macros#payments)

These macros substitute data about an [internal payment transaction](/en/docs/mt5/platform/administration/payments/payments_operations) performed on the account: Used only with the triggers from the [Payments](/en/docs/mt5/platform/administration/automation/automation_trigger#payments) section.

-   Action (#PAYMENT\_ACTION#) — the type of transaction: deposit or withdrawal.
-   Amount (#PAYMENT\_AMOUNT#) — the transaction amount requested by the client. Specified in the deposit currency.
-   Currency (#PAYMENT\_CURRENCY#) — the transaction currency.
-   Commission (#PAYMENT\_COMMISSION#) — the commission charged by the broker in accordance with the [settings](/en/docs/mt5/platform/administration/payments/payments_wallets#commissions).
-   Wallet Amount (#PAYMENT\_WALLET\_AMOUNT#) — the amount of the transaction on the side of the payment provider. It is specified in the currency selected by the user on the client terminal side when making the operation.
-   Wallet Currency (#PAYMENT\_WALLET\_CURRENCY#) — the currency of the transaction on the payment provider's side.
-   Wallet Commission (#PAYMENT\_WALLET\_COMMISSION#) — the payment provider's fee for the transaction.
-   Description (#PAYMENT\_DESCRIPTION#) — additional information about the transaction. Can be filled in by payment systems or manually by managers.
-   Manager (#PAYMENT\_MANAGER#) — the login and name of the manager who [processed the transaction](/en/docs/mt5/platform/administration/payments/payments_processing). It is filled only for manually processed transactions.
-   Type (#PAYMENT\_TYPE#) — the payment method type: card, bank transfer, etc.
-   Provider type (#PAYMENT\_PROVIDER\_TYPE#) — the type of the payment provider (gateway).
-   Provider name (#PAYMENT\_PROVIDER\_NAME#) — the name of the payment provider configuration under which the payment was made.
-   Client IP (#PAYMENT\_CLIENT\_IP#) — the IP address from which the payment was requested.
-   Client IP (#PAYMENT\_CLIENT\_TYPE#) — the IP address from which the payment was requested.
-   Deal ticket (#PAYMENT\_CLIENT\_DEAL#) — the ticket of the balance operation through which funds are credited to or debited from the trading account.
-   External ID (#PAYMENT\_EXTERNAL\_ID#) — the transaction identifier on the payment provider's side.
-   External error code (#PAYMENT\_EXTERNAL\_ERROR\_CODE#) — the error code that occurred on the provider's side.
-   External error description (#PAYMENT\_EXTERNAL\_ERROR\_DESC#) — a description of the error that occurred on the provider's side.
-   Error code (#PAYMENT\_ERROR\_CODE#) — the error code that occurred on the platform side.
-   Error description (#PAYMENT\_ERROR\_DESC#) — a description of the error that occurred on the platform side.

## Finance [#](automation_macros#finance)

These macros substitute data about a [balance operation](/en/docs/mt5/platform/administration/admin_deals#action) executed on the account:

-   Amount (#FINANCE\_AMOUNT#) — operation amount.
-   Currency (#FINANCE\_CURRENCY#) — the currency in which the operation was performed.
-   Comment (#FINANCE\_COMMENT#) — a text comment to a balance transaction.

-   Manager (#FINANCE\_MANAGER#) — the login of the manager who performed the financial transaction.

-   Action (#FINANCE\_ACTION#) — deal type: Buy, Sell, balance or credit operation, etc.

## Server [#](automation_macros#server)

These macros substitute target account [server data](/en/docs/mt5/platform/administration/admin_network/network_add_edit).

-   ID (#SERVER\_ID#) — server ID
-   Type (#SERVER\_TYPE#) — server type as a string. For example, "Main Trade Server".
-   Name (#SERVER\_NAME#) — server name specified in the configuration.
-   Public name (#SERVER\_PUBLIC\_NAME#) — public name of the broker's server (platform) which is displayed in client terminals.
-   Connection state (#SERVER\_CONNECTED#) — the state of server connection to the main trade server at the time the trigger is activated. If the server is connected, the value is 'true'; otherwise it is 'false'.

-   Current server ID (#SERVER\_CURRENT\_ID#) — the identifier of the trade server on which the automation task was triggered. For further details please read the "[Conditions](/en/docs/mt5/platform/administration/automation/automation_condition#current_server)" section.
-   Current server type (#SERVER\_CURRENT\_TYPE#) — the type of trading server on which the automation task was triggered: main or additional.
-   Current server state (#SERVER\_CURRENT\_CONNECTED#) — the state of the trade server on which the automation task was triggered. Available values: Not set — the server does not reboot; Restart — a regular reboot has been started, Stop — the server service is stopped, LiveUpdate — the server service is stopped due to a platform update.
-   Current server connected (#SERVER\_CURRENT\_STATE#) — the state showing the connection between the trade server on which the automation task was triggered and the main server of the platform.

## Gateway [#](automation_macros#gateway)

These macros substitute [data of a gateway](/en/docs/mt5/platform/administration/admin_gateways), which the automation task is related with ([Gateway connection/disconnection](/en/docs/mt5/platform/administration/automation/automation_trigger#platform) triggers).

-   Gateway name (#GATEWAY\_NAME#) — the name of the gateway configuration.
-   Gateway ID (#GATEWAY\_ID#) — the identifier specified in the gateway configuration.
-   Connection status (#GATEWAY\_CONNECTED#) — the state of gateway connection to the platform at the trigger activation time. If the gateway is connected, 'true' is added; otherwise, false.

## Data feed [#](automation_macros#datafeed)

These macros substitute [data of a data feed](/en/docs/mt5/platform/administration/admin_feeds), which the automation task is related with ([Data feed connection/disconnection](/en/docs/mt5/platform/administration/automation/automation_trigger#platform) triggers).

-   Data feed name (#DATAFEED\_NAME#) — the name of the data feed configuration.
-   Connection status (#DATAFEED\_CONNECTED#) — the state of data feed connection to the platform at the trigger activation time. If the data feed is connected, 'true' is added; otherwise, false.

## Prices [#](automation_macros#prices)

These macros substitute data of the symbol to which the automation task trigger is related ("[Prices](/en/docs/mt5/platform/administration/automation/automation_trigger#price)" triggers).

-   Symbol (#PRICES\_SYMBOL#) — the name of the financial instrument for which the event triggered.
-   Last tick time (#PRICES\_LASTTIME#) — time of the last received quote of the symbol for which a trigger was activated.

## Performance [#](automation_macros#performance)

These macros substitute [server monitoring data](/en/docs/mt5/platform/administration/admin_network/network_monitoring) at the moment of trigger activation.

-   Total CPU (#MONITOR\_CPU#) — total CPU load.
-   Process CPU (#MONITOR\_CPU\_PROCESS#) — CPU usage by the server process.
-   Process Threads (#MONITOR\_CPU\_PROCESS\_THREADS#) — number of threads used by the server process.
-   Process Handles (#MONITOR\_HANDLES\_PROCESS#) — number of descriptors (handles) used by the server process.
-   Free Memory (#MONITOR\_MEMORY\_FREE#) — free RAM.
-   Process Memory (#MONITOR\_MEMORY\_PROCESS#) — amount of RAM allocated by the server process.
-   Free Disk Space (#MONITOR\_DISK\_FREE#) — amount of free disk space.
-   Disk Read Speed (#MONITOR\_DISK\_SPEED\_READ#) — speed ​​of data reading in MB/s.
-   Disk Write Speed (#MONITOR\_DISK\_SPEED\_WRITE#) — speed ​​of data writing in MB/s.
-   Disk Queue Length (#MONITOR\_DISK\_QUEUE\_LENGTH#) — disk queue length.
-   Network Connections (#MONITOR\_NETWORK\_CONNECTIONS#) — total amount of all standard operating terminal connections and temporary connections made for executing trades, downloading history or news.
-   Network Connections Blocked (#MONITOR\_NETWORK\_BLOCKED#) — number of connections blocked by the antiflood control or by the built-in firewall.
-   Network Sockets (#MONITOR\_NETWORK\_SOCKETS#) — number of active sockets.
-   Network Traffic In (#MONITOR\_NETWORK\_TRAFFIC\_IN#) — incoming traffic in Mbit/s.
-   Network Traffic Out (#MONITOR\_NETWORK\_TRAFFIC\_OUT#) — outgoing traffic in Mbit/s.
-   Network Retransmits (#MONITOR\_NETWORK\_RETRANSMIT#) —  number of retransmitted packets.
-   Total CPU DPC (#MONITOR\_CPU\_DPC#) — CPU load when handling deferred procedure calls.
-   Total CPU Interrupts (#MONITOR\_CPU\_INTERRUPTS#) — CPU load when handling interruptions from devices.

## External [#](automation_macros#external)

These macros are used for triggers that run automation tasks upon requests received from [external systems](/en/docs/mt5/platform/administration/automation/automation_trigger#external).

-   Web callback URL (#WEBCALLBACK\_URL#) — URL of the [callback request](/en/docs/mt5/platform/administration/automation/automation_trigger#webcallback) which has run the automation task.

## Message [#](automation_macros#messages)

These macros substitute data of the internal email which the user interacts with. Use them with triggers from the [Messages](/en/docs/mt5/platform/administration/automation/automation_trigger#messages) section.

-   Sender login (#MESSAGE\_FROM#) — the account number of the user who sent the email.
-   Sender name (#MESSAGE\_FROM\_NAME#) — the name of the user who sent the email.
-   Recipient login (#MESSAGE\_TO#) — the account number of the email recipient.
-   Recipient name (#MESSAGE\_TO\_NAME#) — the name of the email recipient.
-   Subject (#MESSAGE\_SUBJECT#) — email subject.

-   Body (#MESSAGE\_BODY#) — email body including the HTML markup or the contents of the message sent via the SMS provider or instant messenger.

-   Address (#MESSAGE\_ADDRESS#) — recipient's email address or phone number.
-   Provider name (#MESSAGE\_PROVIDER\_NAME#) — the configuration name of the [SMS provider](/en/docs/mt5/platform/administration/integration/integration_sms), [instant messenger](/en/docs/mt5/platform/administration/integration/integration_messenger) or [mail server](/en/docs/mt5/platform/administration/integration/integration_mail) via which the message was sent.
-   Provider balance (#MESSAGE\_PROVIDER\_BALANCE#) — remaining balance with your [SMS provider](/en/docs/mt5/platform/administration/integration/integration_sms#statistics).

## Connection [#](automation_macros#connection)

These macros are used to display information about the connected client based on their IP address. Use them with triggers from the [Connection](/en/docs/mt5/platform/administration/automation/automation_trigger#connection) category.

-   IP address (#CONNECTION\_IP#) — client's IP address.
-   Country (#CONNECTION\_COUNTRY#) — the country in which the IP address is located.
-   City (#CONNECTION\_CITY#) — the city in which the IP address is located.
-   ASN (#CONNECTION\_ASN#) — the Autonomous System Number (ASN) to which the IP address belongs.
-   ISP (#CONNECTION\_ISP#) — the name of the internet service provider that owns the IP address.
-   Additional flags (#CONNECTION\_FLAGS#):
    -   Datacenter — the address belongs to a data center.
    -   TOR — the address belongs to the [TOR](https://ru.wikipedia.org/wiki/Tor) network.
    -   Proxy — the address is a proxy server.
    -   VPN — the address is a VPN server.
    -   Attacker — the address was involved in various attacks, such as spam, password brute-forcing, DDoS, etc.
    -   Botnet — the address belongs to a botnet.

## Time [#](automation_macros#time)

These macros substitute trigger activation time in the message text:

-   Trading time — time used in the platform, taking into account its [settings](/en/docs/mt5/platform/administration/admin_time).
-   Local time — time used in the computer on which the platform is installed.
-   UTC time — [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) time.

## KYC [#](automation_macros#kyc)

These macros substitute KYC check results in the message text: Only used with the [relevant triggers](/en/docs/mt5/platform/administration/automation/automation_trigger#kyc).

-   #KYC\_STATE\_CODE# — check status code.
-   #KYC\_STATE\_DESC# — check status description.

The possible codes and their descriptions are as follow

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">#KYC_STATE_CODE#</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">#KYC_STATE_DESC#</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">STATUS_INIT</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Initiated</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">STATUS_QUEUED</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Queued</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">STATUS_APPROVED</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Approved</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">STATUS_DECLINED</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Declined</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">STATUS_EXPIRED</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Expired</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_GENERAL</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">General error</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_CONNECTION</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Connection error</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_AUTH</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Auth error</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_INTERNAL</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Internal error</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_DOC_DUPLICATE</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Duplicate document (image, video) was uploaded. Exact equality is taken into account</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_DOC_TOO_MANY</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Applicant contains too many documents. Adding new ones is not allowed</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_DOC_TOO_BIG</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Uploaded file is too big (more than 64MB)</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_DOC_EMPTY</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Uploaded file is empty (0 bytes)</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_DOC_CORRUPTED</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">File is corrupted or incorrect format (e.g. PDF file is uploaded as JPEG)</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:194px;"><p class="p_fortable"><span class="f_fortable">ERROR_DOC_FORMAT</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Unsupported file format (e.g. a TIFF image)</span></p></td></tr></tbody></table>

## Automations [#](automation_macros#automation)

These macros substitute a description of an event which led to [trigger](/en/docs/mt5/platform/administration/automation/automation_trigger) activation.

### Trigger Name (#CONDITION#)

This macro substitutes a description of all [trigger conditions](/en/docs/mt5/platform/administration/automation/automation_condition) in one line. Conditions are separated by semicolons.

All comparison operations other than "equal" feature:

-   Condition name
-   Fixed level (actual value at the moment of trigger activation)
-   Comparison type
-   Condition activation threshold (condition value)

Examples:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Platform\CPU</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Total</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">7.5%</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1%</span><br><span class="f_CodeExample">Platform\CPU</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Total</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">7.5%</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1%;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Platform\Disk</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">queue</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">100</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">10;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Platform\Server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">ID</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">3</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span></p></td></tr></tbody></table>

"Equal" comparison operations feature:

-   Condition name
-   Fixed level

Examples:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Platform\CPU</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Total</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">7.5%</span><br><span class="f_CodeExample">Platform\CPU</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Total</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">7.5%;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Platform\Disk</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">queue</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">10;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Platform\Server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">ID</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">3</span></p></td></tr></tbody></table>

### Condition Threshold (#CONDITION\_LEVEL#)

The list of semi-colon separated trigger condition values. For example, the objective has two conditions:

-   Platform\\Disk Queue Length > 10
-   Platform\\CPU > 70%

The macro displays the string "10 ; 70%".

### Condition Value (#CONDITION\_VALUE#)

The list of actual values of tracked conditions recorded at the trigger time. For example, the objective has two conditions:

-   Platform\\Disk Queue Length > 10. At the time of triggering, the actual disk queue length was 50.
-   Platform\\CPU > 70%. At the moment of triggering, the actual CPU load was 85%.

The macro displays the string "50 ; 85%".

### Action Date and Time (#DATETIME#), Action Time (#TIME#), Action Date (#DATE#)

These macros display the trigger activation date and time. Examples:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2020.10.16&nbsp;15:05:14</span><br><span class="f_CodeExample">15:05:14</span><br><span class="f_CodeExample">2020.10.16</span></p></td></tr></tbody></table>

### Trigger Name (#TRIGGER\_NAME#), Trigger Type (#TRIGGER\_TYPE#)

These macros display [automation task name](/en/docs/mt5/platform/administration/automation/automation_common) and [activated trigger type](/en/docs/mt5/platform/administration/automation/automation_trigger).

-   Schedule/Scheduled event
-   Connection/Login
-   Connection/First login
-   Connection/Logout
-   Accounts/New trade account
-   Finance/Deposit
-   Finance/First deposit
-   Finance/Withdrawal
-   Finance/First withdrawal
-   Finance/Credit
-   Finance/First credit
-   Finance/Credit out
-   Finance/First credit out
-   Trade/Margin call
-   Trade/Stop out
-   Price/Gap started
-   Price/Gap finished
-   Platform/Performance monitor
-   Platform/Server connect to Main server
-   Platform/Server disconnect from Main server

### Action Name (#ACTION\_NAME#), Action Type (#ACTION\_TYPE#)

These macros display the name and type of a [performed action](/en/docs/mt5/platform/administration/automation/automation_action).

[Actions](/en/docs/mt5/platform/administration/automation/automation_action)

[Statistics](/en/docs/mt5/platform/administration/automation/automation_statistics)