# Price Translations

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_translation

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
                -   [Forming Market Depth](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation)
                -   [Market Depth Journal](/en/docs/mt5/platform/administration/ecn/ecn_dom_journal)
                -   [Order Matching](/en/docs/mt5/platform/administration/ecn/ecn_matching)
                -   [Order Execution](/en/docs/mt5/platform/administration/ecn/ecn_execution)
                -   [Price Translations](/en/docs/mt5/platform/administration/ecn/ecn_translation)
                -   [Matching History](/en/docs/mt5/platform/administration/ecn/ecn_matching_history)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[ECN](/en/docs/mt5/platform/administration/ecn)Price Translations

# Price Translations

In the "Translations" section, you can configure translation of ECN symbol prices to other symbols. Markup settings can be automatically applied to such prices. This enables liquidity providing brokers to implement different ECN trading conditions for different client groups.

[Similar to gateways](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation), the ECN converts prices and trading requests.

For example, EURUSD.ECN data are forwarded to EURUSD.USR with the markups of -2/+2. Clients trade EURUSD.USR at converted prices. When forwarding orders from these clients back to external systems, the ECN will use original unchanged prices.

-   The gateway passes original prices from the external system to the ECN symbol EURUSD.ECN: 1.15651 / 1.15659
-   Translation of prices from EURUSD.ECN into EURUSD.USR with the conversion of -2/+2 is set up in ECN. Prices are converted to 1.15649 / 1.15661
-   The client places the EURUSD.USR Buy order at a price of 1.15661
-   The order is passed to the ECN for processing
-   The ECN converts the price to the original one 1.15659 and passes it to the external system
-   If the order is successfully executed in the external system, the ECN sends a response to the client, informing that the order was executed at the requested (converted) price of 1.15661

The broker earns the profit of 2 pips in this case.

![Price translation settings](/en/docs/mt5/platform/img/ecn_translation.png "Price translation settings")

The following settings are available:

-   Symbol — the symbols, to which data from the ECN symbol will be passed. Any non-ECN symbol or the source symbol can be specified here. If an ECN symbol has a translation setting, in which this symbol is specified as a target, a marked up price stream will be provided for such a symbol. If there are no such settings, the source price stream will be provided for the ECN symbol.
-   Source — the ECN symbol, which data will be passed.
-   Bid, Ask — the number of markup points to convert appropriate prices. A positive value increases the price, a negative one decrease it. The values ​​are specified in the source symbol price points.

You may use the mask "\*" in the source symbol names for mass translations and conversions. In this case, the translation affects all source-target pairs, in which the asterisk replaces the same set of characters. For example:

-   If symbols EURUSD.ECN, EURJPY.ECN, EURJPY.USR and EURGBP.USR exist in the platform, the rule EUR\*.ECN -> EUR\*.USR will create the translation EURJPY.ECN -> EURJPY.USR.
-   If symbols EURUSD.ECN, EURJPY.ECN, EURUSD.USR and EURJPY.USR exist in the platform, the rule \*.ECN -> \*.USR will create translations EURUSD.ECN -> EURUSD.USR and EURJPY.ECN -> EURJPY.USR.

If several symbols meeting one group rule have different number of decimal places in prices, different price markups will be applied to them in accordance with their specific accuracy. For example, if a symbol has 4 decimal places, the markup of "1" will change prices by 0.0001; for symbols with 5 decimal places the markup will be equal to 0.00001.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If several rules are configured for one target symbol, only the first rule in the list will be applied to it.</span></li><li class="p_tableatten"><span class="f_tableatten">Price markup settings are not applied for the ECN symbol, when translated to other symbols. For example, the rule is EURUSD.ECN -&gt; EURUSD.ECN, Bid -1, Ask +1. If EURUSD.ECN is used as a source in other translation rules, original prices without the markup will be translated from it.</span></li><li class="p_tableatten"><span class="f_tableatten">Translation rules can be changed without server restart. Changes take effect immediately after saving. If the rules for a specific symbol have changed, the Market Depth of such a symbol will be reset in accordance with the new settings.</span></li><li class="p_tableatten"><span class="f_tableatten">Translation rules only apply to data from gateways and datafeeds. Trade orders for source symbols placed by clients within the cluster are not passed to target symbols. In order to show cluster orders in the target symbol, set it as an ECN symbol and configure <a href="/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation#aggregation_rules" class="topiclink">aggregation rules</a> for it.</span></li></ul></td></tr></tbody></table>

## Features of trading operations [#](ecn_translation#features)

If only one translation parameter or no parameters at all are set for the ECN, trades are conducted without any peculiarities since the ECN is able to match symbols on its side with the ones in the external trading system.

If more than one translation parameter is set for the ECN, the platform attempts to match the symbols correctly. For example, the two translation parameters are set for the ECN:

-   EURUSD.ECN -> EURUSD.USR1
-   EURUSD.ECN -> EURUSD.USR2

If an order is placed on the platform side, a symbol in the external system response is defined by the original order ticket. For example, a trader places an order #145269 Buy 1.00 EURUSD.USR.2. It is sent to the external system as #145269 Buy 1.00 EURUSD. When receiving a response, the ECN converts the symbol back to EURUSD.USR2 by the original order ticket.

However, there are some trading operations/events that are not preceded by placing an order on the trading platform side. For example, charging a variation margin in an external system. In that case, the ECN cannot clearly define which of the two symbols the event is related to: EURUSD.USR1 or EURUSD.USR2.

In this situation, the ECN attempts to select the correct symbol by its availability to certain accounts the event is related to. For example, if only EURUSD.USR2 is available for an account, the ECN performs an operation for it. Availability of symbols for clients is defined on the ["Symbols" tab of the group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols).

If both symbols are available for the account, the operation is performed for the first one in the translation list. It is EURUSD.USR1 in our example.

Thus, if there are multiple translation settings, the following rule is used: trading operations are performed for the first symbol available for a client group. All subsequent translation settings are used only to pass price data.

## The general price translation scheme for ECN trading [#](ecn_translation#general)

The placing and execution price of the orders sent to the ECN is affected not only by the above translation settings. The following platform settings also affect the prices:

-   [Symbol spread settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#spread): both general settings and those specific of separate [client groups](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols).
-   [Translation settings](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#translation) specified in the gateways.
-   [Slippage settings](/en/docs/mt5/platform/administration/ecn/ecn_matching#filling) specified in the matching rules.

Consider an example of all price translations:

### 1\. The Client

The user creates a request based on the prices displayed in the terminal. For example, Buy Limit at 1.14059:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">11</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #008000;">26</span><span class="f_CodeExample">:57.369</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">Trades</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">'2002':</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">buy</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">limit</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1.00</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">EURUSD.ECN</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1.14059</span><br><span class="f_CodeExample">2019.01.04</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">11</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #008000;">26</span><span class="f_CodeExample">:57.370</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">Trades</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">'2002':</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">accepted</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">buy</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">limit</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1.00</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">EURUSD.ECN</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1.14059</span></p></td></tr></tbody></table>

### 2\. The Trade server

The Trade Server receives the request and forwards it to the ECN, in accordance with the [routing rule](/en/docs/mt5/platform/administration/ecn/ecn_matching#routing):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.530&nbsp;&nbsp;192.168.0.1&nbsp;&nbsp;'2002':&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;(1.14028&nbsp;/&nbsp;1.14050)</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.530&nbsp;&nbsp;192.168.0.1&nbsp;&nbsp;'2002':&nbsp;request&nbsp;transferred&nbsp;to&nbsp;dealers,&nbsp;rule&nbsp;'ECN'&nbsp;(buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059)</span></p></td></tr></tbody></table>

### 3\. The Trade server

[Spread balance](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_common) settings specified for the client group are applied to the request price. For example, the value of 2 bid / 2 ask is specified:

![Example of spread settings for the client group](/en/docs/mt5/platform/img/ecn_price_example_spread.png "Example of spread settings for the client group")

The price of 1.14059 is reduced by 2 points, to 1.14057.

### 4\. The Trade server

Also, [ECN price markup settings](/en/docs/mt5/platform/administration/ecn/ecn_translation) are applied to the request price. For example, Bid Markup = -4, Ask Markup = 4.

![Example of ECN price translation settings](/en/docs/mt5/platform/img/ecn_price_example_translation.png "Example of ECN price translation settings")

The price of 1.14057 is reduced by two more points, to 1.14053. A request with this price is sent to the ECN.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.531&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;request&nbsp;received&nbsp;(#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053)</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In this case, the Trade server performs the back translation — it reduces the Ask price instead of increasing it, because the client is already using the adjusted prices. 1.14053 is the initial price for the ECN.</span></p></td></tr></tbody></table>

### 5\. The ECN

The ECN places and order to be matched, at the price of 1.14053, confirms it and sends trade executions to the server, for creating the order in the database (similar to gateways):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.532&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;added</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.534&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;request&nbsp;answered&nbsp;-&nbsp;Placed&nbsp;(#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053)</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.536&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;request&nbsp;new&nbsp;order&nbsp;#417761</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.538&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;added&nbsp;order&nbsp;#417761,&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;&nbsp;at&nbsp;1.14053&nbsp;[based&nbsp;on&nbsp;order&nbsp;'']</span></p></td></tr></tbody></table>

### 6\. The Trade server

After receiving a request from the ECN, the trade server increases its price back to the client price of 1.14059. To the price of 1.14053, the server ads 2 points of the "Spread balance" specified in symbol settings for the client group and 4 points from ECN markup settings.

Thus, in the trade database and on the client side the order has the price adjusted in accordance with the group and ECN settings (1.14059). It corresponds to the quotes delivered to the client. However, the ECN itself uses the translated price (1.14053).  

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.535&nbsp;&nbsp;192.168.0.1&nbsp;&nbsp;'2002':&nbsp;order&nbsp;placed&nbsp;for&nbsp;execution&nbsp;[#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059],&nbsp;time&nbsp;4.22&nbsp;ms</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.536&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;request&nbsp;new&nbsp;due&nbsp;execution&nbsp;[request&nbsp;new&nbsp;order&nbsp;#417761],</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total&nbsp;time:&nbsp;5.84&nbsp;ms&nbsp;[route:&nbsp;0.26&nbsp;ms,&nbsp;ecn:&nbsp;5.26&nbsp;ms,&nbsp;ecn&nbsp;place:&nbsp;0.00&nbsp;ms,&nbsp;ecn&nbsp;match:&nbsp;0.00&nbsp;ms,&nbsp;ecn&nbsp;fill:&nbsp;0.00&nbsp;ms,&nbsp;apply:&nbsp;0.04&nbsp;ms]</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.538&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;placed&nbsp;due&nbsp;execution&nbsp;[added&nbsp;order&nbsp;#417761,&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;[based&nbsp;on&nbsp;order&nbsp;'']],</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total&nbsp;time:&nbsp;7.67&nbsp;ms&nbsp;[route:&nbsp;0.26&nbsp;ms,&nbsp;ecn:&nbsp;7.15&nbsp;ms,&nbsp;ecn&nbsp;place:&nbsp;0.00&nbsp;ms,&nbsp;ecn&nbsp;match:&nbsp;0.00&nbsp;ms,&nbsp;ecn&nbsp;fill:&nbsp;0.00&nbsp;ms,&nbsp;apply:&nbsp;0.04&nbsp;ms]</span></p></td></tr></tbody></table>

### 7\. The ECN

Using the converted price of 1.14053, the ECN matches the client order with an opposite request received from the gateway.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.539&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;matched&nbsp;1.00&nbsp;at&nbsp;1.14044,&nbsp;#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;vs&nbsp;sell&nbsp;limit&nbsp;10.00&nbsp;at&nbsp;1.14044&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;by&nbsp;rule&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.541&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417761&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;added&nbsp;(buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053)</span></p></td></tr></tbody></table>

### 8\. Gateway

The gateway receives the trade request from the ECN and adjusts it in accordance with the translation settings:

![Gateway settings example](/en/docs/mt5/platform/img/ecn_price_example_gateway.png "Gateway settings example")

The order price 1.14053 is reduced by 8 points to 1.14045. A request at this price is sent to the external system.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.550&nbsp;&nbsp;Gateway&nbsp;&nbsp;'141156':&nbsp;request&nbsp;#3090901&nbsp;received&nbsp;(#18446744072000000129&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD&nbsp;at&nbsp;1.14045)</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In this case, the gateway performs the back translation — it reduces the Ask price instead of increasing it, because the ECN is already using the adjusted prices. 1.14045 is the initial price for the external system.</span></p></td></tr></tbody></table>

### 9\. Gateway

After sending an order to the external system, the gateway generates an appropriate confirmation and a trade execution for the trading platform. The request price is again translated during this operation — it is increased by 8 points, to 1.140453 (the external system price is translated into MetaTrader 5 prices).

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.552&nbsp;&nbsp;Gateway&nbsp;&nbsp;'18446744073709551615':&nbsp;request&nbsp;#3090901&nbsp;answered&nbsp;-&nbsp;Placed&nbsp;(#18446744072000000129&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD&nbsp;at&nbsp;1.14045)</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.567&nbsp;&nbsp;Gateway&nbsp;&nbsp;execution&nbsp;sending&nbsp;complete&nbsp;-&nbsp;request&nbsp;new&nbsp;order&nbsp;#18446744072000000129</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.567&nbsp;&nbsp;Gateway&nbsp;&nbsp;execution&nbsp;sending&nbsp;complete&nbsp;-&nbsp;added&nbsp;order&nbsp;#18446744072000000129,&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD&nbsp;at&nbsp;1.14045&nbsp;[based&nbsp;on&nbsp;order&nbsp;'417762']</span></p></td></tr></tbody></table>

### 10\. The ECN

The ECN receives from the gateway the confirmation and trade executions having the price of 1.14053:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.552&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417761&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;confirmed:&nbsp;Placed&nbsp;(buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053)</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.553&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417761&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;order&nbsp;#18446744072000000129&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;placed&nbsp;for&nbsp;execution,&nbsp;time:&nbsp;11.89&nbsp;ms</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.567&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417761&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;order&nbsp;#18446744072000000129&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;request&nbsp;new&nbsp;due&nbsp;execution</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[request&nbsp;new&nbsp;order&nbsp;#18446744072000000129],&nbsp;time:&nbsp;0.07&nbsp;ms</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.568&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417761&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;order&nbsp;#18446744072000000129&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;placed&nbsp;due&nbsp;execution</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[added&nbsp;order&nbsp;#18446744072000000129,&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;[based&nbsp;on&nbsp;order&nbsp;'417762']],&nbsp;time:&nbsp;0.46&nbsp;ms</span></p></td></tr></tbody></table>

### 11\. Gateway

Suppose, the gateway received a notification from the external system that the order was actually executed at the price of 1.14043 (2 points lower than the initially requested price of 1.14045). The following execution is formed in this case:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.833&nbsp;&nbsp;Gateway&nbsp;&nbsp;execution&nbsp;sending&nbsp;complete&nbsp;-&nbsp;filled&nbsp;order&nbsp;#18446744072000000129,&nbsp;buy&nbsp;1.00&nbsp;EURUSD&nbsp;at&nbsp;1.14043&nbsp;[based&nbsp;on&nbsp;deal&nbsp;'129506']</span></p></td></tr></tbody></table>

### 12\. The ECN

The ECN matches the order at the price of 1.14051: the actual deal execution price (1.14043) is widened by 8 points in accordance with the gateway settings.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.841&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417761&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;order&nbsp;#18446744072000000129&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;/&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;filled&nbsp;due&nbsp;execution</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[filled&nbsp;order&nbsp;#18446744072000000129,&nbsp;buy&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14051&nbsp;[based&nbsp;on&nbsp;deal&nbsp;'129506']],&nbsp;time:&nbsp;6.87&nbsp;ms</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If several translation settings are specified for the same symbol in the gateway configuration and the gateway cannot determine which one to use for a particular request, the platform will try to determine it itself. For more information, see the <a href="/en/docs/mt5/platform/administration/admin_gateways/gateway_translation#features" class="topiclink">"Price and symbol translation"</a> section.</span></li><li class="p_tableatten"><span class="f_tableatten">Some gateways may not support trading operation price conversion options. This feature is determined by the developer. In this case, the price conversion settings will only affect the displayed quotes.</span></li></ul></td></tr></tbody></table>

### 13\. The ECN

When executing the order, the platform checks allowable [slippage in ECN symbol settings](/en/docs/mt5/platform/administration/ecn/ecn_matching#filling). Suppose, the values of 5 are set both for the profitable and losing slippage:

![Example of allowable slippage settings](/en/docs/mt5/platform/img/ecn_price_example_slippage.png "Example of allowable slippage settings")

The deal price of 1.14051 is 2 points better than 1.14053, which is within the allowable profitable slippage. In this case the order is executed at its initial price in the ECN, i.e 1.14053 (point 5):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.834&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;filled&nbsp;1.00&nbsp;at&nbsp;1.14053&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.836&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;filled&nbsp;order&nbsp;#417761,&nbsp;buy&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14053&nbsp;[based&nbsp;on&nbsp;deal&nbsp;'']</span></p></td></tr></tbody></table>

If the deal price exceeded the deviation, the ECN would execute the order in the platform at that specific price (1.14051).

### 14\. The Trade server

After request processing in the ECN, the price of 1.14053 is translated into the client price. The trade server increases it by 2 points in accordance with the "Spread balance" parameter of the client group and by 4 more points in accordance with the ECN translation settings (points 3 and 4). The resulting deal in the database will be formed at the price of  1.14059:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.836&nbsp;&nbsp;'2002':&nbsp;deal&nbsp;performed&nbsp;[#129507&nbsp;buy&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059]</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.836&nbsp;&nbsp;'2002':&nbsp;order&nbsp;performed&nbsp;buy&nbsp;1.00&nbsp;at&nbsp;1.14059&nbsp;[#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059]</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.836&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;filled&nbsp;due&nbsp;execution&nbsp;[filled&nbsp;order&nbsp;#417761,&nbsp;buy&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;[based&nbsp;on&nbsp;deal&nbsp;'']],&nbsp;time:&nbsp;0.25&nbsp;ms</span></p></td></tr></tbody></table>

### 15\. The Client

The client receives a deal at the price of 1.14059:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.01.04&nbsp;12:15:40.539&nbsp;&nbsp;&nbsp;&nbsp;Trades&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#417761&nbsp;buy&nbsp;limit&nbsp;1.00&nbsp;/&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;done&nbsp;in&nbsp;8.385&nbsp;ms</span><br><span class="f_CodeExample">2019.01.04&nbsp;12:15:41.836&nbsp;&nbsp;&nbsp;&nbsp;Trades&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;deal&nbsp;#129507&nbsp;buy&nbsp;1.00&nbsp;EURUSD.ECN&nbsp;at&nbsp;1.14059&nbsp;done&nbsp;(based&nbsp;on&nbsp;order&nbsp;#417761)</span></p></td></tr></tbody></table>

Thus, the price undergoes the following transformations during the entire order execution process:

-   1.14059 — the order price on the client and trade server sides
-   1.14053 — the order price in the ECN, which resulted from the order price conversion in accordance with the "Spread balance" specified for the trade group and the ECN markup
-   1.14045 — the order price at the gateway, which resulted from the reduction of the order price in ECN by the translation value specified in the gateway settings
-   1.14043 — the deal price at the gateway
-   1.14051 — the deal price in the ECN, which resulted from the increase of the actual deal execution price in the external system by the translation value specified in the gateway settings
-   1.14053 — the deal price at the gateway adjusted to the order price in accordance with the slippage settings
-   1.14059 — the deal price on the trade server and client side, which resulted from deal price increase by the "Spread balance" specified for the trade group and the ECN markup

The client placed an order at the price of 1.14059 and received its execution at the requested price. The real order execution price in the external system was 1.14043. The broker's profit was 16 points.

[Order Execution](/en/docs/mt5/platform/administration/ecn/ecn_execution)

[Matching History](/en/docs/mt5/platform/administration/ecn/ecn_matching_history)