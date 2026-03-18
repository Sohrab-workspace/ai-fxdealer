# Gateway

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/gateway

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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Gateway

# Gateway

MetaTrader 4 platform features the built-in gateway allowing users to arrange Straight Through Processing (STP) of trade operations on any external MetaTrader 4 trading server. The gateway is easily configured providing maximum security and performance.

## How the Gateway Works

MetaTrader 4 Gateway has two main tasks: passing the quotes and moving trade operations to MetaTrader 4 external server. This is performed via a special account opened on MetaTrader 4 external server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The gateway can simultaneously work with several MetaTrader 4 external servers.</span></p></td></tr></tbody></table>

### Passing Quotes from MetaTrader 4 External System

The quotes received from the gateway:

-   Are not subject to the filtration rules configured for the appropriate symbols. The quotes received from an external server are supposed to be filtered already;
-   Passed "as is" considering spread settings on a quote account;
-   Have the highest priority over any data sources working in your trading platform. [Priority of quotes](/en/docs/mt4/administrator/administration/gateway#quotes) received via different account gateways is defined by the account's position in the list;
-   Can be transformed (expanded) when being submitted to your trading platform.

### Transferring Trade Operations to MetaTrader 4 External System

MetaTrader 4 gateway transfers trade operations to an external server, as well as receives and displays their handling results. Operations are transferred via one or several trade accounts opened at MetaTrader 4 external server.

Operations containing only market orders are transferred to an external server by the gateway:

-   opening a position;
-   complete or partial closing of a position;
-   complete or partial closing of a position by an opposite one.

Placed pending orders, as well as Stop Loss, Take Profit and Stop Out ones are processed on MetaTrader 4 platform side. During their activation, the appropriate market order is transferred to an external system.

The gateway does not support closing multiple positions using opposite ones (Multiple Close By). Such requests are rejected automatically.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Both local and external MetaTrader 4 servers should have build 480 or higher to use the gateway.</span></p></td></tr></tbody></table>

## Purchasing the Gateway

The gateway works in demo mode handling the first 100 trade requests after launching the server in case the license is absent (the server service should be re-launched manually in order to reset). The appropriate license should be purchased to experience a full-scale functionality of MetaTrader 4 gateway. You can place your order in [Buy section of the technical support website](https://support.metaquotes.net/ru/buy "Move to Buy section of the technical support website") or send a request via [Service Desk](/en/docs/mt4/administrator/toolbox/ug_toolbox_support#service_desk).

After purchasing the gateway, your MetaTrader 4 platform license will be updated via [LiveUpdate](/en/docs/mt4/administrator/administration/ug_live_update) system. No additional actions are required after that, you will be able to start working immediately.

## Gateway Setup

Gateway settings are divided in three groups:

-   Gateway Account — configuring connection to transfer the quotes and display trade operations;
-   Gateway Markups — configuring the symbols, for which the gateway will transfer the quotes, as well as configuring conversion of the quotes transferred via the gateway and used for performing trade operations;
-   Gateway Rules — configuring trade requests routing to the gateway.

![Gateway Settings](/en/docs/mt4/administrator/img/gateway.png "Gateway Settings")

### Gateway Accounts [#](gateway#account)

One or several accounts should be configured for the gateway operation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any change in configuration of accounts (adding, changing or deleting) leads to entire reconnection of all accounts. At the same time, all currently handled requests will be rejected. Therefore, we do not recommend you to change account parameters during active trading.</span></p></td></tr></tbody></table>

The account is used both for passing trade operations to an external server and for passing the quotes (if Feed quotes option is enabled in the settings).

Create a new configuration in Gateway Account section:

![Configuring a trade account](/en/docs/mt4/administrator/img/trade_account.png "Configuring a trade account")

Specify the following parameters for an account:

-   Enable — enable an account. When disabling a trade account, trade requests transferred to an external server via the trade account according to the [routing rules](/en/docs/mt4/administrator/administration/gateway#route) are not handled. They are rejected instead.
-   Feed quotes — if enabled, the quotes from an external trade server are passed via this account. The list of symbols the quotes are passed for is configured in [Markups](/en/docs/mt4/administrator/administration/gateway#price) section.
-   Name — name for configuring an account.
-   Address — MetaTrader 4 external server address for connection. The address is specified as an IP address or a domain name and a port.
-   Login — number of an account on the external server, using which connection is performed. All trading symbols, for which you are going to transfer the quotes and perform trade operations, should be available for the account.
-   Password — password for connecting to the specified account. The account's Master password should be specified, since that account is used for trading.
-   Notify logins — this field allows specifying up to 8 comma-separated account logins, to which gateway operation error reports will be sent via the internal email system. Accounts having administrator or manager rights, as well as ordinary trade accounts can be specified here.

Quotes transfer features:

The quotes passed by the gateway have the highest priority over any [data feeds](/en/docs/mt4/administrator/administration/ug_data_feeds) used on the trade server. Several accounts can be used simultaneously for passing the quotes via the gateway. Priority of the quotes is defined by the account's position in the list. Quotes from the first account in the list have the highest priority.

This does not mean that the quotes arrive only from a single account. The server always receives the quotes from all accounts with "Feed quotes" option enabled. This solution allows to instantly switch to other accounts in case of malfunctions.

For example, several accounts provide quotes for one symbol from different servers — priority defines what account should be used. If the required information is not received from the current account within a certain time interval (specified in Common section — [Feeder Switch Timeout](/en/docs/mt4/administrator/administration/ug_options#feeder_switch) field), the server will automatically switch to the next account that supplies data on the same symbol. However, once data are received from an account with a higher priority, the server switches to the use of its data.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">After account priority (position in the list) is changed, quote flow is automatically switched according to the new priorities.</span></p></td></tr></tbody></table>

When a quote flow is switched from one account to another, the following entry is displayed in the server journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Gateway</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">GOLD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">activation</span></p></td></tr></tbody></table>

The digit indicates the number of the account that is now used for passing the quotes for the specified symbol (0 stands for the first account in the list, 1 — for the second one, etc.). In order to find out what account occupied the specified position in the list, examine the previous gateway initialization entry:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Gateway&nbsp;0:&nbsp;account&nbsp;'Demo'&nbsp;uses&nbsp;'123456'&nbsp;at&nbsp;demo.metaquotes.net:443&nbsp;initialized</span></p></td></tr></tbody></table>

The entry contains the account configuration name, account name, as well as the address of the external server connection is performed to.

Other features:

-   If a price spreading is configured at an external server for an account, extended prices will be transferred via the gateway.
-   Quotes transferred by the gateway are not subject to the filtration rules configured for the appropriate symbols. The quotes received from an external server are supposed to be filtered already.

-   Quotes transferred by the gateway are not affected by the spread settings of the symbol ([Spread by default](/en/docs/mt4/administrator/administration/ug_symbols#setup_symbol) and [Spread balance](/en/docs/mt4/administrator/administration/ug_symbols#setup_symbol)).

### Gateway Markups [#](gateway#price)

The section is used for:

-   setting the list of symbols the gateway passes the quotes for;
-   setting the rules of changing symbol names;
-   setting the rules of correcting the prices passed by the gateway.

Any changes in price correction settings (adding, changing, deleting) are applied immediately and do not require additional server restart.

Create a new configuration:

![Configuring symbols and price corrections](/en/docs/mt4/administrator/img/gateway_price.png "Configuring symbols and price corrections")

Specify the following parameters:

-   Enable — enable symbol configuration. If the setting is disabled, the gateway will not accept quotes for the specified symbols.
-   Source — symbols on MetaTrader 4 external server. Symbols can be specified the following way:

-   as a symbols group name (Securities), for example, Forex;
-   as a comma-separated list of symbol names, for example EURUSD, USDJPY, GBPJPY;
-   as symbol masks, for example EUR\*, USD\*, \*JPY (all symbols starting from EUR and USD, as well as symbols ending in JPY).

-   Symbol — this setting allows changing symbol names in case they differ at the external server. Suppose that the symbol is called EURUSD on MetaTrader 4 external server, while it should correspond with EURUSD.gw symbol in your platform. In this case, EURUSD should be specified in Source field, while EURUSD.gw should be entered in Symbol field given that the symbol exists in your platform. If names should be changed, setup is performed symbol-by-symbol. Otherwise, leave the field empty.
-   Bid markup — bid markup on the local server relative to the external one should be specified in points. For example, if -2 is set, 1.3320 quote will be transferred to your platform if 1.3322 is received from the gateway. Markup can be either positive or negative.
-   Ask markup — as in the case with Bid markup, Ask price markup can be specified here.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">Correction settings features:</span></p><p class="p_txt"><span class="f_txt">If names should be changed, setup is performed symbol-by-symbol.</span></p><p class="p_txt"><span class="f_txt">Symbols should not cross in the settings. This should be especially considered when using '*' mask.</span></p><p class="p_txt"><span class="f_txt">If price correction is not configured, clients will work using external server's prices.</span></p><p class="p_txt"><span class="f_txt">Example of <a href="/en/docs/mt4/administrator/administration/gateway#correction" class="topiclink">price correction</a> is shown below.</span></p></td></tr></tbody></table>

Let's consider some configuration examples.

Setting the list of symbols the quotes from the gateway are passed for:

![Setting the symbols for passing the quotes](/en/docs/mt4/administrator/img/gateway_markup_quotes.png "Setting the symbols for passing the quotes")

All fields except Source remain empty.

Changing the symbol name:

![Changing the symbol name](/en/docs/mt4/administrator/img/gateway_markup_transform.png "Changing the symbol name")

Only Source (initial name on the external server) and Symbol (final name on the local server) fields are filled.

Correcting the prices passed from the external server:

![Correcting the prices passed from the external server](/en/docs/mt4/administrator/img/gateway_markup_price.png "Correcting the prices passed from the external server")

Source symbol, as well as Bid and Ask price correction value are set.

### Gateway Rules [#](gateway#route)

The section is implemented for configuring the rules of handling trade requests by MetaTrader 4 gateway.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any changes in configuring the gateway rules (adding, changing, deleting) are applied immediately and do not require additional server restart.</span></p></td></tr></tbody></table>

![Setting gateway rules](/en/docs/mt4/administrator/img/gateway_route.png "Setting gateway rules")

The following parameters are set up for each rule:

-   Enable — enable the rule.
-   Symbol — trade symbols, for which trade requests should be transferred to the gateway according to the rule. Symbols can be specified the following way:

-   as a symbols group name (Securities), for example, Forex;
-   as a comma-separated list of symbol names, for example EURUSD, USDJPY, GBPJPY;

-   using the "\*" mask and the negation sign "!". For example EUR\*, USD\*, \*JPY (all symbols starting with EUR and USD, as well as symbols ending in JPY) or EUR\*,!EURUSD (all symbols starting with EUR, except for EURUSD).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The "*" mask and the negation sign "!" can only be used in symbol names. Using "*" and "!" in symbol groups (Securities) is not allowed.</span></p></td></tr></tbody></table>

-   Group — group of clients whose trade requests should be transferred to the gateway. Similar to the symbols, the groups can be specified in a comma-separated way using "\*" mask and "!" negation symbol. You can also specify here certain logins separated by comma.
-   Account — [gateway trade account](/en/docs/mt4/administrator/administration/gateway#account), through which trade operations are transferred to the external system. When changing trade account configuration name, the gateway routing rules should also be changed properly. The number of the account (in the gateway account list) used for passing a certain trade operation is specified in the server journal. In the example below, number 2 is specified meaning the third account in the list.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Gateway</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">2:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">stp</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">on</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'2698810'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'200'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">order</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">was</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">opened</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">#29045766</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">buy</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1.00</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">GBPCHF</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1.51195</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">sl:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0.00000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">tp:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0.00000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">in</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">117</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">msc</span></p></td></tr></tbody></table>

-   Max. deviation — maximum permissible deviation of prices. It is used in the following cases:

-   If Market Execution mode is used at a local server, while Instant Execution one - at an external server, trade requests are shown in Instant Execution mode with allowable deviation specified in this parameter;
-   If Instant Execution mode is used at an external server, while Stop Loss, Take Profit or Stop Out are activated on a local server, appropriate market orders are transferred to the external server in Instant Execution mode with allowable deviation specified in this parameter. The larger the parameter value, the higher the probability that the order will be executed after the first activation without a requote from the external server's side. On the other hand, increasing this parameter may cause too large deviation of the order execution price from its activation price.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">Following the Rules:</span></p><p class="p_txt"><span class="f_txt">The rules of processing gateway requests are of higher priority in comparison with automation settings in the client group parameters. It means that even if "automatic only" is set in the client group settings for this group of trading symbols but a trade request corresponds with one of the gateway rules, it will be processed by the gateway.</span></p><p class="p_txt"><span class="f_txt">Rules are executed from top downwards according to their sequence in "Gateway Rules" section. If a received request corresponds to the conditions of the top rule, it is handled under this rule, otherwise conditions of the second rule are checked, and so on.</span></p><p class="p_txt"><span class="f_txt">When checking and processing requests, the gateway receives control before plugin hooks shown below. The following hooks are not called for trade requests corresponding to the gateway rules:</span></p><ul><li class="p_txt"><span class="f_txt">MtSrvTradeRequestApply</span></li><li class="p_txt"><span class="f_txt">MtSrvTradeRequestRestore</span></li><li class="p_txt"><span class="f_txt">MtSrvTradeStopsFilter</span></li><li class="p_txt"><span class="f_txt">MtSrvTradeStopsApply</span></li><li class="p_txt"><span class="f_txt">MtSrvTradePendingsFilter</span></li><li class="p_txt"><span class="f_txt">MtSrvTradePendingsApply</span></li><li class="p_txt"><span class="f_txt">MtSrvTradeStopoutsFilter</span></li><li class="p_txt"><span class="f_txt">MtSrvTradeStopoutsApply</span></li></ul></td></tr></tbody></table>

Processing Dealer's Trades

Dealers can trade on behalf of traders using the MetaTrader 4 Manager terminal. Of all the trading operations available to the dealer, only four operations can be sent to an external server through a gateway:

-   Opening an Order
-   Closing an Order
-   Closing an Order by an Opposite One
-   Pending Order Activation

It is specified in the gateway rules, whether such operations should be sent to an external server or they should be processed locally. Gateway rules contain a selectable option "Process dealer's trades".

It should be noted that dealer's operation do not have execution type: Instant, Request or Market. The dealer always sends trading orders with a specified price. Respectively, [slippage](/en/docs/mt4/administrator/administration/gateway#slippage) is checked the same way as it is done when pending orders and stop orders (Stop Loss, Take Profit and Stop Out) trigger.

Dealer's trade operations sent through the gateway appear in the server log as follows:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2014.11.26&nbsp;13:07:14.724 &nbsp; &nbsp; &nbsp; &nbsp;192.168.0.1 &nbsp; &nbsp; &nbsp; &nbsp;'1':&nbsp;open&nbsp;order&nbsp;for&nbsp;'759535'&nbsp;buy&nbsp;1.00&nbsp;GBPUSD&nbsp;at&nbsp;1.57241&nbsp;sl:&nbsp;0.00000&nbsp;tp:&nbsp;0.00000&nbsp;(&nbsp;1.57223&nbsp;/&nbsp;1.57241&nbsp;)&nbsp;</span><br><span class="f_CodeExample">2014.11.26&nbsp;13:07:14.755&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gateway&nbsp;6:&nbsp;stp&nbsp;on&nbsp;'254'&nbsp;for&nbsp;'759535'&nbsp;-&nbsp;request&nbsp;price&nbsp;for&nbsp;10.00&nbsp;GBPUSD</span><br><span class="f_CodeExample">2014.11.26&nbsp;13:07:14.880&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gateway&nbsp;6:&nbsp;stp&nbsp;on&nbsp;'254'&nbsp;for&nbsp;'759535'&nbsp;-&nbsp;answer&nbsp;prices&nbsp;for&nbsp;10.00&nbsp;GBPUSD&nbsp;-&nbsp;1.57223&nbsp;/&nbsp;1.57241&nbsp;in&nbsp;125&nbsp;msc</span><br><span class="f_CodeExample">2014.11.26&nbsp;13:07:14.880&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gateway&nbsp;6:&nbsp;stp&nbsp;on&nbsp;'254'&nbsp;for&nbsp;'759535'&nbsp;-&nbsp;order&nbsp;by&nbsp;request&nbsp;buy&nbsp;10.00&nbsp;GBPUSD&nbsp;at&nbsp;1.57241&nbsp;sl:&nbsp;0.00000&nbsp;tp:&nbsp;0.00000</span><br><span class="f_CodeExample">2014.11.26&nbsp;13:07:15.005&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gateway&nbsp;6:&nbsp;stp&nbsp;on&nbsp;'254'&nbsp;for&nbsp;'759535'&nbsp;-&nbsp;order&nbsp;was&nbsp;opened&nbsp;:&nbsp;#59812&nbsp;buy&nbsp;10.00&nbsp;GBPUSD&nbsp;at&nbsp;1.57241&nbsp;sl:&nbsp;0.00000&nbsp;tp:&nbsp;0.00000&nbsp;in&nbsp;125&nbsp;msc</span></p></td></tr></tbody></table>

Explanation:

-   The dealer with login "1" opened an order for user '759535' at a price of 1.57241.
-   Since the symbol goes with the Request execution type, the gateway has requested prices from the external server.
-   The external server has returned prices 1.57223 / 1.57241.
-   The order has been executed at the price of 1.57241.

Coverage Percentage

The deal volume coverage percentage on an external server is set in Covered volume field. The volume passed to an external server is displayed in the separate order field — [Gateway lots](/en/docs/mt4/administrator/administration/ug_orders).

Volume calculation when opening: the volume is calculated according to the specified percentage. The total value is normalized (rounded mathematically) considering the minimum and maximum volumes, as well as the allowable volume step on an external server.

Volume calculation when closing: the volume is calculated according to the specified percentage. An attempt is made to close the exact same volume on the external server (considering the minimum and maximum volumes, as well as the allowable volume step).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Position on the external server is not closed till the corresponding client's position remains open on the local trade server.</span></p></td></tr></tbody></table>

If the appropriate volume part cannot be closed on the external server (for example, the volume is less than the minimum allowable amount), the client's request is confirmed without passing to the external server.

In order to keep the volume proportions when passing the orders to the external system, the following rules should be considered when setting the coverage percentage:

-   The minimum volume of orders after applying the coverage percentage should be greater than or equal to the minimum allowed volume on the external server.
-   The maximum volume of orders after applying the coverage percentage should be less than or equal to the maximum allowed volume on the external server.
-   Volume change step after applying the coverage percentage should be greater than or equal to the volume step on the external server.

Let's consider several examples.

The minimum volume and volume step are equal to 0.1 lots on the local and external servers. Coverage percentage is equal to 50%.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Client's action</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Client's total position</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Gateway's action</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Total position on the external server</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Open 1 lot</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1 lot</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Open 0.5 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.5 lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.5 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.5 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.2 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.3 lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.4 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots (bringing the initial volume of 0.05 to the minimum volume and step)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.2 lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.3 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots (bringing the initial volume of 0.05 to the minimum volume and step)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.2 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Operation is not passed, since the position is not closed yet at the client's side.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Operation is not passed, since the position is not closed yet at the client's side.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td></tr></tbody></table>

The minimum volume and volume step are equal to 0.1 lots on the local and external servers. Coverage percentage is equal to 10%.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Client's action</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Client's total position</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Gateway's action</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Total position on the external server</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Open 1 buy lot</span></p><p class="p_fortable"><span class="f_fortable">Open 0.5 sell lot</span></p><p class="p_fortable"><span class="f_fortable">Open 0.1 sell lot</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1 buy lot</span></p><p class="p_fortable"><span class="f_fortable">0.5 sell lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Open 0.1 buy lots</span></p><p class="p_fortable"><span class="f_fortable">Open 0.1 sell lot</span></p><p class="p_fortable"><span class="f_fortable">Open 0.1 sell lot</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 buy lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.5 sell lots by the opposite 1 buy lot</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.5 buy lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 sell lots by the opposite 0.1 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 lots by the opposite 0.5 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.4 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 sell lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.4 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Operation is not passed, since the position has already been closed on the external server.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td></tr></tbody></table>

The minimum volume and volume step are equal to 0.1 lots on the local and external servers. Coverage percentage is equal to 10%.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Client's action</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Client's total position</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Gateway's action</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Total position on the external server</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Open 0.3 buy lots</span></p><p class="p_fortable"><span class="f_fortable">Open 0.1 sell lot</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.3 buy lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Open 0.1 buy lots</span></p><p class="p_fortable"><span class="f_fortable">Open 0.1 sell lot</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 buy lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.2 buy lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 buy lots</span></p><p class="p_fortable"><span class="f_fortable">0.1 sell lots</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.2 buy lots by the opposite 0.1 sell lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.1 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 sell lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Close 0.1 buy lots</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Operation is not passed, since the position has already been closed on the external server.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">None</span></p></td></tr></tbody></table>

Maximum slippages

This group of parameters allows setting slippages occurring during the processing of market and pending orders:

-   Profitable — maximum allowed deviation of a client request price from an external server one towards the client's profit. The maximum allowable request volume (in lots), for which that deviation is acceptable, is specified in "at most" field.
-   Losing — maximum allowed deviation of a client request price from an external server one towards the client's loss. The maximum allowable request volume (in lots), for which that deviation is acceptable, is specified in "at most" field.

Deviations for market orders:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:181px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution type on the local server</span></p></th><th class="table" style="width:176px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution type on the external server</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:181px;"><p class="p_fortable"><span class="f_fortable">Request Execution</span></p></td><td class="table" style="width:176px;"><p class="p_fortable"><span class="f_fortable">Request Execution</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No deviations are used. The price is requested directly from an external server considering necessary changes (Markups).</span></p><p class="p_fortable"><span class="f_fortable">Please note that you can work via STP gateway in Request Execution mode only if it is installed both on external and local servers.</span></p></td></tr><tr class="table"><td class="table" style="width:181px;"><p class="p_fortable"><span class="f_fortable">Market Execution</span></p></td><td class="table" style="width:176px;"><p class="p_fortable"><span class="f_fortable">Any execution type</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No deviations are used. Order execution price is defined by the external server (considering necessary changes specified in "Markups" section).</span></p></td></tr><tr class="table"><td class="table" style="width:181px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Instant Execution</span></p></td><td class="table" style="width:176px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Instant Execution</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The deviations are managed the following way:</span></p><ul><li class="p_fortable"><span class="f_fortable">Client request price is brought in line with external server's one considering Markups settings.</span></li><li class="p_fortable"><span class="f_fortable">The difference between the received price (transformed client price) and the current market price at an external server is calculated.</span></li><li class="p_fortable"><span class="f_fortable">Direction of the price deviation is checked.</span></li><li class="p_fortable"><span class="f_fortable">If deviation has occurred towards the client's profit, it is compared to Profitable value. Suppose that the client's buy price is 1.0000, while the market one is 1.0005. Thus, the client's buy operation could have been better (cheaper) than the current market one's - deviation towards the client's profit.</span></li><li class="p_fortable"><span class="f_fortable">If deviation has occurred towards the client's loss, it is compared to Losing value. Suppose that the client's buy price is 1.0005, while the market one is 1.0000. Thus, the client's buy operation could have been worse (more expensive) than the current market one's - deviation towards the client's loss.</span></li><li class="p_fortable"><span class="f_fortable">If the deviation is less or equal to the value specified in the settings and the order volume is less or equal to the appropriate "at most" value, the request in Instant Execution mode with the external server's current market price is sent to the external server.</span></li><li class="p_fortable"><span class="f_fortable">Otherwise, the client's request is requoted. External server's current prices brought in line with Markups values are used for requoting.</span></li></ul></td></tr><tr class="table"><td class="table" style="width:181px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Instant Execution</span></p></td><td class="table" style="width:176px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Market Execution</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Checking a trade request price deviation from the server's current market one is performed just before a trading order is sent to an external server in Market Execution mode. Checking is carried out in the same way as in the previous case (using instant execution on both servers).</span></p><p class="p_fortable"><span class="f_fortable">Please note that the actual execution price on the external server can differ from the price at the moment the check was performed.</span></p></td></tr></tbody></table>

Deviations for pending orders, Stop Loss, Take Profit and Stop Out:

Execution of pending and stop orders (Stop Loss, Take Profit and Stop Out) is checked by the local trade server's prices. An appropriate market request is sent to an external server after an order activation.

In Request Execution and Market Execution modes, sending of a market order to the server is performed in the standard way - with a preliminary request for a price and without specifying a price respectively. In case of Instant Execution mode, the current market price on an external server is specified in the placed order. Acceptable deviation is additionally set in the order according to Max. deviation field in the gateway settings. The larger the value, the lower the probability of receiving a requote. However, the actual execution price can deviate from the requested one to a greater extent. The value should be selected based on a symbol's volatility.

If the market order is executed successfully, the gateway calculates the difference between the actual order execution price on an external server and the client order one. The obtained value is then compared with the specified allowable deviations:

-   If deviation has occurred towards the client's profit, it is compared to Profitable value. Suppose that the client buy order's price is 1.0000, while the price of the market order execution on the external server is 1.0005. Thus, the client's buy operation could have been more expensive at the current market price - deviation towards the client's profit.
-   If deviation has occurred towards the client's loss, it is compared to Losing value. Suppose that the client buy order's price is 1.0005, while the price of the market order execution on the external server is - 1.0000. Thus, the client's buy operation could have been cheaper at the current market price - deviation towards the client's loss.

If the deviation is less or equal to the value specified in the settings and the order volume is less or equal to the appropriate "at most" value, the client order's price is used as the order execution price at the local server side. Otherwise, the actual execution price of an appropriate market order at an external server is specified as an execution price in the order.

Let's consider the more detailed example of sending an order in Instant Execution mode. Markups are considered to be equal to 0 (not used) for more convenience:

-   Buy Limit 1.00 EURUSD order at 1.0000 has been activated.
-   At the moment the market order is sent to an external server, the current market price there is 1.0003. Thus, the gateway sends Buy 1.00 EURUSD 1.0003 market order in Instant Execution mode. The allowable deviation value is additionally added to that order from the gateway settings (suppose that Max. deviation = 10).
-   The price at the external server is 1.0004 at the moment of execution. It falls into the specified deviation value, and the order is successfully executed.
-   As the price in the client' order is better than the actual execution one, Profitable deviation value is checked (suppose that Profitable = 5, at most = 5).
-   The difference between the client's and the actual execution prices falls into the permissible deviation.
-   The order's initial price (1.0000) is set as an order execution price at the local server's side.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">After creating all the rules, the gateway is ready for work. You can check the gateway operation by viewing the server journal. Request journal logs using "Gateway:" keyword in "Journal" section of MetaTrader 4 Administrator.</span></p></td></tr></tbody></table>

## Correcting Prices in the Gateway [#](gateway#correction)

Price correction is set in [Gateway Markup section](/en/docs/mt4/administrator/administration/gateway#price).

Double correction of prices occurs when trade requests are sent from a client to the server and back:

1.  Price correction according to the settings in [Gateway Markup section](/en/docs/mt4/administrator/administration/gateway#price).
2.  Price correction according to the spreading settings for a client group on your server.

Example:

The following price correction is set for EURUSD symbol in the gateway settings: Bid = -1, Ask = 1. Price spreading of 2 points is set for the same symbol for a client. Thus:

-   Price received by the gateway from the external server: 1.32272 / 1.32280
-   Price corrected according to the gateway correction settings: 1.32271 / 1.32281
-   Price received by the client after spreading: 1.32270 / 1.32282

The client sends the request at the received price in Instant Execution mode: Buy EURUSD 1.00 at 1.32282. When the request is sent to the external server, reverse correction of the price occurs. Therefore, the external server receives the request for executing operation at the price of 1.32280. After opening a position, the price of the coverage position will be better than the client's one by 2 pips.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The difference between the order's open/close price on the local and external servers is displayed in special order fields — <a href="/en/docs/mt4/administrator/administration/ug_orders" class="topiclink">Open price delta</a> and <a href="/en/docs/mt4/administrator/administration/ug_orders" class="topiclink">Close price delta</a>.</span></p></td></tr></tbody></table>

## Managing Compatibility of Trading Symbol Settings [#](gateway#control)

The gateway controls compatibility of symbol settings when transferring trade operations to MetaTrader 4 external server. In case of incompatibility, the trade request is rejected and the appropriate entry appears in the server journal.

The following parameters are controlled:

-   The gateway requires compliance of execution types for similarly-named trading symbols or the symbols compared via Gateway Markup. The following cases are regarded as exceptions:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="vertical-align:middle; width:149px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution type on the local server</span></p></th><th class="table" style="vertical-align:middle; width:165px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution type on the external server</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="vertical-align:middle; width:149px;"><p class="p_fortable"><span class="f_fortable">Market Execution</span></p></td><td class="table" style="vertical-align:middle; width:165px;"><p class="p_fortable"><span class="f_fortable">Any</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The gateway automatically uses the symbol's execution type specified for a symbol on MetaTrader 4 external server.</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:149px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Instant Execution</span></p></td><td class="table" style="vertical-align:middle; width:165px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Market Execution</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The gateway automatically uses the symbol's execution type specified for a symbol on external server.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Before sending a request, the check is performed to ensure that deviation of the request price from the current market prices corresponds to the highest value specified in the <a href="/en/docs/mt4/administrator/administration/gateway#route" class="topiclink">gateway rule</a>, as well as to the maximum deviation value specified by the client in the request.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">If deviation has occurred towards the client's profit, the deviation specified in the gateway settings is checked. If deviation has occurred towards the client's loss, the deviation specified by the client when sending the order is checked.</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle; width:149px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Instant Execution</span></p></td><td class="table" style="vertical-align:middle; width:165px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Instant Execution</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Request volume threshold value for moving from Instant Execution to Request Execution is additionally checked. If a request has a volume that is enough for switching to Request Execution mode on only one of the servers (local or external one), this request is rejected.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">If Instant or Request execution modes coincide on both servers at the specified volume, the request will be executed.</span></p></td></tr></tbody></table>

-   Trading should be enabled for the symbol on the external server.
-   Number of digits in symbol's price should be the same on both servers.
-   Tick size should be the same on both servers.
-   Tick price should be the same on both servers.
-   Contract size should be the same on both servers.
-   Initial margin on the external server should not exceed the one on the local server.
-   Maintenance margin on the external server should not exceed the one on the local server.
-   Hedged margin on the external server should not exceed the one on the local server.
-   Margin multipliers should be the same on both servers.
-   Margin calculation mode should be the same on both servers.
-   Margin calculation currency should be the same on both servers.
-   Profit calculation mode should be the same on both servers.
-   In order to close the opposite orders (Close by) on the external server, the appropriate option in the group symbol settings should be enabled.

## Handling Market Requests

Market requests handling passes the following stages:

1.  Request is checked for compliance with [the gateway rules](/en/docs/mt4/administrator/administration/gateway#route). If all the requirements are met, it is blocked in the requests' queue.
2.  Multiple Close By requests are immediately rejected.
3.  Requests related to pending orders, as well as Stop Loss and Take Profit orders (creation, modification and deletion) are automatically confirmed (not transferred to the external system).
4.  Changing a symbol name according to the settings in [Gateway Markup section](/en/docs/mt4/administrator/administration/gateway#price).
5.  Checking [trade symbol parameters on](/en/docs/mt4/administrator/administration/gateway#control) your own and on an external MetaTrader 4 server.
6.  Price correction according to the settings in [Gateway Markup section](/en/docs/mt4/administrator/administration/gateway#price).
7.  If local symbol's execution mode is Market Execution, it is changed according to the external server's execution mode.
8.  The request is handled on the external server and is accompanied by logging.
9.  Prices are corrected for the obtained result according to the gateway settings and spreading at client's side.
10.  Client's request is confirmed or rejected depending on handling results on the external server.

The structure of handling market requests is shown below.

![Handling market requests](/en/docs/mt4/administrator/img/gateway_market_request.png "Handling market requests")

## Handling Activation of Pending Orders, Stop Orders and Stop Outs

The following actions are performed when pending orders, Take profits, Stop Losses and Stop Outs are activated:

1.  A server defines order activation and notifies the gateway in the same way as this is done by MtSrvTradePendingsApply, MtSrvTradeStopsApply and MtSrvTradeStopoutsApply hooks. The gateway forms the request in its internal queue.
2.  Request is checked for compliance with [the gateway rules](/en/docs/mt4/administrator/administration/gateway#route).
3.  Changing a symbol name according to the settings in [Gateway Markup section](/en/docs/mt4/administrator/administration/gateway#price).
4.  Checking [trade symbol parameters on](/en/docs/mt4/administrator/administration/gateway#control) your own and on an external MetaTrader 4 server.
5.  Price correction according to the settings in [Gateway Markup section](/en/docs/mt4/administrator/administration/gateway#price).
6.  If local symbol's execution mode is Market Execution, it is changed according to the external server's execution mode.
7.  The request is handled on the external server and is accompanied by logging. If the request has been rejected or requoted, the activated order is not processed till the next activation.
8.  Prices are corrected for the obtained result according to the gateway settings and spreading at client's side.
9.  The activated client's order is converted to the position (for pending orders) or closes a client's position (in case of SL-TP and Stop-Out).

Handling activation of pending orders, stop orders and Stop Outs is shown below.

![Handling activation of pending orders, Take Profit, Stop Loss and Stop Out](/en/docs/mt4/administrator/img/gateway_pending.png "Handling activation of pending orders, Take Profit, Stop Loss and Stop Out")

## Ongoing Maintenance

An abnormal situation may occur during the operation of the gateway. A position which no longer exists on the external server can be still available on the trader's account. In this case, it will be impossible to close it.

To solve the issue, open the relevant position on the external server manually by connecting to the [gateway account](/en/docs/mt4/administrator/administration/gateway#account) via the client terminal. The position volume should be set taking into account the "[Coverage percent](/en/docs/mt4/administrator/administration/gateway#coverage)" parameter specified for the gateway. Next, copy the open position ticket into the "Gateway order" field of the client [order](/en/docs/mt4/administrator/administration/ug_orders#deal) on your trading platform side. Also specify the position volume in the "Gateway lots" field.

After that, the position can be normally closed on your platform side. The corresponding position on the external server will also be closed.

[Common](/en/docs/mt4/administrator/administration/ug_options)

[IP Access List](/en/docs/mt4/administrator/administration/ug_access)