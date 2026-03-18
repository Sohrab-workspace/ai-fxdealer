# MetaTrader 5 Gateway to MetaTrader 4

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/gateways/metatrader4gateway

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
                -   [MOEXFX](/en/docs/mt5/platform/components/gateways/moex_fx)
                -   [MOEX Securities](/en/docs/mt5/platform/components/gateways/moex_securities)
                -   [MOEX Derivatives](/en/docs/mt5/platform/components/gateways/moex_derivatives)
                -   [DGCX](/en/docs/mt5/platform/components/gateways/dgcx)
                -   [MetaTrader 5](/en/docs/mt5/platform/components/gateways/metatrader5gateway)
                -   [MetaTrader 4](/en/docs/mt5/platform/components/gateways/metatrader4gateway)
                -   [Integral](/en/docs/mt5/platform/components/gateways/integral)
                -   [Currenex](/en/docs/mt5/platform/components/gateways/currenex)
                -   [Euronext FX](/en/docs/mt5/platform/components/gateways/euronextfx)
                -   [Cboe FX](/en/docs/mt5/platform/components/gateways/cboefx)
                -   [LMAX Global](/en/docs/mt5/platform/components/gateways/lmax)
                -   [FXCM PRO](/en/docs/mt5/platform/components/gateways/fxcmpro)
                -   [Borsa Istanbul](/en/docs/mt5/platform/components/gateways/borsa)
                -   [Interactive Brokers](/en/docs/mt5/platform/components/gateways/interactive_brokers)
            -   [Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Gateways](/en/docs/mt5/platform/components/gateways)MetaTrader 4

# MetaTrader 5 Gateway to MetaTrader 4

The gateway allows any brokerage firm to integrate with larger brokers and liquidity providers using the MetaTrader 4 trading platform. You will be able to minimize your risk and receive potential profit from each trade operation of a client due to markups. All you need to do is select a liquidity provider and perform a simple gateway configuration.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="https://support.metaquotes.net/en/market/product/267" target="_blank" class="weblink">Order MetaTrader 5 Gateway to MetaTrader 4</a></span></p></td></tr></tbody></table>

## How the Gateway Works

The gateway acts as an intermediary between the two platforms by converting trade requests of brokerage clients into requests to the external MetaTrader 4 trading platform, receiving answers and sending them back to clients.

The [routing rules](/en/docs/mt5/platform/components/gateways/metatrader4gateway#routing) allow configuring the broker's server in such a way that the clients' trade requests are sent to the gateway. Depending on the order type, each request is handled differently:

-   Market orders are passed to the gateway directly.
-   All pending orders are not passed to the gateway by default. They are handled within the trading platform instead. An appropriate market request is sent to the gateway immediately after activation.
-   Take Profit, Stop Loss and Stop Out orders are handled and stored on the MetaTrader 5 platform side. The appropriate market operation is sent to the external platform right after activation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The gateway is already included in the MetaTrader 5 platform and can be used in demo mode, which allows performing not more than 100 trading operations for a work session (until restart). The full version should be purchased separately.</span></li><li class="p_tableatten"><span class="f_tableatten">The gateway transmits quotes from the external MetaTrader 4 platform.</span></li></ul></td></tr></tbody></table>

## Requirements [#](metatrader4gateway#wl)

For proper operation of the gateway and correct accounting of funds, it is necessary to ensure that the symbol on the broker's server have the same trading settings as the remote MetaTrader 4 platform. The symbol's trading parameters can be set in the symbols setup dialog. The following symbol settings should be the same:

-   The mode of [order execution](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution) by a symbol
-   [Number of digits](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common) after the decimal point
-   [Type of calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation) of margin requirements and profit on a symbol
-   [The price of one point](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade) of the price change, except for instruments with the Forex calculation mode
-   [Size of one point](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade), except for instruments with the Forex calculation mode
-   For the Request execution mode, the [mode of order confirmation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution) should be enabled

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A trade account should be created on MetaTrader 4 external server, on behalf of which all client trade operations passed through the gateway are performed.</span></p></td></tr></tbody></table>

## Gateway Configuration

MetaTrader 5 Gateway to MetaTrader 4 is a separate MetaTrader4Gateway64.exe file that uses Gateway API for its operation. The gateway is distributed as part of the MetaTrader 5 platform and located in \[history server installation directory\]\\gateway\\.

To start working, add [the new gateway configuration](/en/docs/mt5/platform/administration/admin_gateways):

![Configuring the gateway](/en/docs/mt5/platform/img/mt4gateway_common.png "Configuring the gateway")

Set the following parameters on the "Common" tab:

-   ID — set the identifier of the dealer, from whose name the requests routed to the gateway are confirmed.
-   Module — select MetaTrader4Gateway64 in the list of available modules and load its default settings.
-   Trading server — MetaTrader 4 external server IP address and port trade requests are sent to.
-   Trading login — index of a trade account opened at MetaTrader 4 external server. This is the account, at which client trading operations passed through the gateway are performed.
-   Password — password for connecting to an account at MetaTrader 4 external server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">ID value must be unique in the field of manager logins and gateway identifiers. Usually, this field is filled out automatically by an acceptable default value.</span></p></td></tr></tbody></table>

Now, go to the "Parameters" tab.

![Gateway parameters](/en/docs/mt5/platform/img/mt4gateway_param.png "Gateway parameters")

The following additional parameters are available for the gateway:

-   Quotes Time Original — if the value is Yes, the gateway sets the time of ticks on its own considering a time zone of a recipient trading server. If No, or the parameter is absent, the time of ticks is set by the history server according to its own trading time.
-   News Category — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).
-   Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow.
-   Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
-   Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
-   Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.

Use the Groups tab to select the group of clients, whose orders and positions will be available to the gateway.

![Configuring the groups](/en/docs/mt5/platform/img/mt4gateway_groups.png "Configuring the groups")

The Symbols tab allows you to configure the list of symbols, according to which the gateway will process trade operations and transmit the quotes.

![Configuring the symbols](/en/docs/mt5/platform/img/mt4gateway_symbols.png "Configuring the symbols")

MetaTrader 5 Gateway to MetaTrader 4 supports the import of symbols and their settings from an external trading server. If the option "Allow importing symbol settings" is enabled, the import of symbols from an external server will be performed. All symbols available for an account used for connection (specified in "Trading server" field of the Common tab) are imported. The symbols are imported to Symbols/Preliminary/ subgroup according to their hierarchy at the external server.

-   The symbols imported by the gateway are put to the \\Preliminary symbols subgroup. All symbols have trading ability disabled. System administrator must relocate imported symbols to the proper subgroup and allow trading for them.
-   After symbols are relocated and trading abilities are enabled, the main trading server must be restarted.
-   In case the gateway transmits configuration for the symbol that is already present in the platform, the existing symbol settings are not updated. Configuration of such a symbol is skipped.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The gateway supports conversion of symbols and quotes. For details, please view the <a href="/en/docs/mt5/platform/administration/admin_gateways/gateway_translation" class="topiclink">Symbol and Price Translation</a> section.</span></p></td></tr></tbody></table>

## Configuring trade requests routing [#](metatrader4gateway#routing)

After adding a new gateway, configure [routing](/en/docs/mt5/platform/administration/requests_routing) so that the clients' requests are routed to this gateway. Select "Process to dealers" as an action in the common rule settings. Assign this routing rule for all requests and orders. In additional conditions, indicate groups of clients, whose requests will be passed to the gateway.

![Configuring routing](/en/docs/mt5/platform/img/mt4gateway_routing.png "Configuring routing")

Add the previously created gateway at the Dealers tab.

After the correct execution of the steps described above, the gateway is launched and ready to work. The result of the gateway operation is reflected in its [journal](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway).

## Formation and Correction of Prices [#](metatrader4gateway#markup)

MetaTrader 5 Gateway to MetaTrader 4 translates the price flow from an external MetaTrader 5 platform, just like the data feeds do. The priority of quotes from the gateway is higher than the priority of quotes from a data feed. If quotes for a symbol are available both from the gateway and data feed, a client will receive the quotes from the gateway.

The gateway performs all trading operations considering the price correction. To set correction for each individual symbol, go to the Translations tab in the gateway settings and enter the appropriate values:

![Correction parameters](/en/docs/mt5/platform/img/mt4gateway_translations.png "Correction parameters")

In this example, the following corrections are specified for EURUSD: for each tick the Bid price will be reduced by 3 points, and the Ask price will be increased by 3 points.

A price is given to the broker's client only after the correction, so the clients work only with the corrected prices. If no correction is set for a symbol, the client will work with the original prices of the liquidity provider.

## Example

All trade operations performed by the gateway are included in the gateway journal. For example, using the client terminal we buy EURUSD 1.0. After processing the request, the following entries will appear in the journal of the MetaTrader 5 Gateway:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">'1002':&nbsp;request&nbsp;#1179132&nbsp;received&nbsp;(#2073&nbsp;instant&nbsp;buy&nbsp;1.00&nbsp;EURUSD&nbsp;at&nbsp;1.31237)</span><br><span class="f_CodeExample">'1002':&nbsp;request&nbsp;#1179132&nbsp;answered&nbsp;-&nbsp;Done&nbsp;at&nbsp;1.312370&nbsp;(#1002&nbsp;instant&nbsp;buy&nbsp;1.00&nbsp;EURUSD&nbsp;at&nbsp;1.31237)(based&nbsp;on&nbsp;#2448959,&nbsp;#2448959,&nbsp;1.31198&nbsp;/&nbsp;1.31212)</span></p></td></tr></tbody></table>

Let's consider the contents of the logs in more detail.

A request with the ID # 1179132 is received from the broker's client with the account 1002. Corresponding to this request, on the broker's server there is the client's order with the ID # 2073 to Buy one lot of EURUSD at the price of 1.31237.

To the request ID #1179132, the broker's client with the account 1002 receives a reply that the request has been executed (Done), with the request execution price 1.312370. In addition, the original order of the client is specified. The last part of the message contains the parameters of the trading operation on the remote platform. In particular, upon the client's request, generated order # 2448959, deal # 2448959, with the actual execution prices: Sell - 1.31198, Buy - 1.31212. In this case, this means that the client's Buy has been executed at 1.31212 on the external trading platform.

On this basis, we can calculate the profit from the price difference:

The broker's profit = 1.31237 - 1.31212 = 0.00025.

## Simulating the Netting Accounting System on MetaTrader 4

MetaTrader 4 trading platform supports only the [hedging accounting system](/en/docs/mt5/platform/administration/admin_groups/group_position#hedging). This system allows you to have unlimited number of trading positions on a single financial instrument. In addition to hedging, MetaTrader 5 supports the [netting](/en/docs/mt5/platform/administration/admin_groups/group_position#netting) system. This system is used on exchanges allowing a trader to have only one cumulative position at a symbol. Making a trade on the same instrument may change the existing position's volume, close it completely or reverse it.

If netting is used on MetaTrader 5 side, the gateway will try to simulate it on MetaTrader 4 external server.

The gateway automatically assigns an identification number to an account in the external server in the account settings of each client whose trades are passed to the external server (in case the number has not been already specified manually).

![ID in the external system](/en/docs/mt5/platform/img/mt4gateway_external.png "ID in the external system")

The ID is used as a magic number for all client orders (positions) passed to the external system. When a client's market transaction is sent to the MetaTrader 4 external server, the gateway additionally sends the command to close all opposite positions (Multiple close by) with the same magic number on the same symbol. Thus, only one resulting position remains at the external system for a single symbol.

[MetaTrader 5](/en/docs/mt5/platform/components/gateways/metatrader5gateway)

[Integral](/en/docs/mt5/platform/components/gateways/integral)