# MetaTrader 5 Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/metatrader5feeder

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
                -   [Dow Jones Prime Tass News Feeder](/en/docs/mt5/platform/components/datafeeds/djprimetassnewsfeeder)
                -   [DJ News Feeder](/en/docs/mt5/platform/components/datafeeds/djnewsfeeder)
                -   [IQFeeder](/en/docs/mt5/platform/components/datafeeds/iqfeeder)
                -   [MetaTrader 4 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader4feeder)
                -   [MetaTrader 5 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader5feeder)
                -   [Trading Central News Feeder](/en/docs/mt5/platform/components/datafeeds/tcnewsfeeder)
                -   [MetaTrader 5 UniFeeder](/en/docs/mt5/platform/components/datafeeds/metatrader5unifeeder)
                -   [Thomson Reuters Feeder](/en/docs/mt5/platform/components/datafeeds/thomsonreutersfeeder)
                -   [RSS News Feeder](/en/docs/mt5/platform/components/datafeeds/rssnewsfeeder)
                -   [IBTimes News Feeder](/en/docs/mt5/platform/components/datafeeds/ibtnewsfeeder)
                -   [ForexPros Feeder](/en/docs/mt5/platform/components/datafeeds/forexprosfeeder)
                -   [KnowledgeView News Feeder](/en/docs/mt5/platform/components/datafeeds/knowledgeviewnewsfeeder)
                -   [FXstreet Feeder](/en/docs/mt5/platform/components/datafeeds/fxstreetfeeder)
                -   [Financial Source News Feeder](/en/docs/mt5/platform/components/datafeeds/financialsourcenewsfeeder)
                -   [Claws & Horns Feeder](/en/docs/mt5/platform/components/datafeeds/clawshornsfeeder)
                -   [UniNewsFeeder](/en/docs/mt5/platform/components/datafeeds/uninewsfeeder)
                -   [Alliance News Feeder](/en/docs/mt5/platform/components/datafeeds/alliancenewsfeeder)
                -   [Newsquawk](/en/docs/mt5/platform/components/datafeeds/newsquawk)
                -   [Remote Datafeed](/en/docs/mt5/platform/components/datafeeds/remote_datafeed)
                -   [Universal DDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)MetaTrader 5 Feeder

# MetaTrader 5 Feeder

MetaTrader 5 Feeder is a data feed which enables the delivery of news, quotes and Market Depth data from any MetaTrader 5 servers.

This solution is built into the platform, which ensures minimal delays in quote delivery. To speed up data delivery, the data feed operates works in multiple streams, and also it automatically selects the best access points for connection.

## Setup

Contact the desired broker and agree on data delivery terms and conditions. To connect to the source broker, you will need a regular trading account (demo or real), with access to the required news and trading instruments. The data feed will create a client connection and will deliver data through this connection.

The data feed must be added via the [corresponding section](/en/docs/mt5/platform/administration/admin_feeds) of the administrator terminal.

![Common](/en/docs/mt5/platform/img/data_feeds_server_mt5.png "Common")

The following parameters should be specified on the ["Common"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data feed:

-   Module — MetaTrader5Feeder;
-   Feed server — address of the MetaTrader 5 server and the port number to connect to it (separated by a colon);
-   Feed login — login (account number) for the authorization on the server;
-   Password — password for the authorization. If the extended authorization mode is enabled on the server you are going to receive data from, you should use an investor password instead of the main one. Otherwise connection will be impossible.

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_mt5.png "Parameters")

The data feed features the following additional [parameters](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters):

-   Quotes Time Original — if "Yes", the datafeed itself sets the time for ticks considering the time zone of the recipient trade server. If the parameter is absent or set to "No", the time for ticks is set by the history server according to the trade time used.
-   Selftitled Translations — this parameter is used to prevent quotes from looping when connecting to the server on which the datafeed is installed. The default value is No. For more details please see [below](/en/docs/mt5/platform/components/datafeeds/metatrader5feeder#retranslation).
-   Symbols Update — mode applied to the import of trading instruments to the platform from an external source. If set to No (default), the data feed will only add symbols from the source server that do not yet exist in the platform. If set to Yes, the data feed will also update the settings of already existing symbols, which may affect the broadcasting of quotes (general description, currency data, accuracy, order book depth, tick value and size, accrued interest on bond, settlement price, price limits, splicing data, and quoting sessions). Settings are updated in real time. Quoting sessions are updated taking into account server time zones.  
    Symbol settings are only imported/updated, if the [appropriate option](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#import) is enabled in the data feed settings.
-   Symbols Path — path to import trading instruments to. If this parameter is absent (by default), the data feed will import trading instruments into the \\Preliminary subgroup with the trading option disabled. If this parameter has a non-empty value, the data feed will import trading instruments into the specified location.
-   News Category — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).
-   Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
-   Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
-   Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.

## Automatic Opening of Demo Accounts

The data feed is capable of automatic of opening of demo accounts on the source server.

If the account details (login and password) are not specified in the data feed settings or the account has become invalid (expired), the data feed will open a new demo account and will use it for connecting.

## Transferring quotes

For symbols with the [disabled market depth](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#dom) (on the external server side), MetaTrader 5 Feeder passes ticks with Bid and Ask prices.

For symbols with the enabled market depth, the data feed transfers the market depth changes as well as ticks with Last prices and volumes. Ticks containing only Bid and Ask price changes are not transferred. If the best supply and demand prices change in the market depth, the history server generates the necessary tick with Bid and Ask prices and adds it to the flow.

The data feed features the built-in switching mechanism to prevent the quote flow from stopping in case the external server stops transmitting the market depth changes. If not a single market depth change for a symbol arrives from the external system within 30 seconds, the data feed stops sorting out ticks having only Bid and Ask prices. In other words, it starts transferring to the platform both Last/Volume and Bid/Ask ticks.

The following entries are shown in the data feed journal when the market depth is no longer transmitted:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.09.12</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">15:20:25.412</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Feeder</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">books</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">stream</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">EURUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">stopped</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">(no</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">books</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">during</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">31</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">sec)</span><br><span class="f_CodeExample">2017.09.12</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">15:20:25.873</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Feeder</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">books</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">stream</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">USDJPY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">stopped</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">(no</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">books</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">during</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">31</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">sec)</span></p></td></tr></tbody></table>

If the flow is resumed:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.09.12</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">15:21:29.759</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Feeder</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">books</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">stream</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">EURUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">resumed</span><br><span class="f_CodeExample">2017.09.12</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">15:21:30.060</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Feeder</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">books</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">stream</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">USDJPY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">resumed</span></p></td></tr></tbody></table>

## Symbol masks and own price retranslation [#](metatrader5feeder#retranslation)

In [datafeed translation settings](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#translation), the "\*" mask can be used as the source symbol and as the destination symbol in the platform. For example, the settings Symbol="\*", Source="\*" mean that the names of the symbols will be used as they are provided in the external system. If the symbol is entitled EURUSD in the external system, then its data will be feed to the symbol with the same name on the trading platform side. The only situation in which such settings cannot be used is the connection of the data feed to the platform on which it is installed. In this case, receiving and feeding of quotes by the datafeed into the same symbols will lead to looping.

To avoid such situations, the datafeed provides the parameter "[Selftitled Translations](/en/docs/mt5/platform/components/datafeeds/metatrader5feeder#selftitled_translations)". If it is set to "No" (default) and the datafeed has a translation setting "\*" <- "\*", the datafeed will not start. An appropriate entry will be added into the journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">translation&nbsp;rule&nbsp;for&nbsp;symbols&nbsp;to&nbsp;themselves&nbsp;'*&nbsp;&lt;-&nbsp;*'&nbsp;not&nbsp;allowed&nbsp;but&nbsp;exists,&nbsp;remove&nbsp;this&nbsp;rule&nbsp;or&nbsp;allow&nbsp;it&nbsp;by&nbsp;'Selftitled&nbsp;Translations'&nbsp;parameter</span></p></td></tr></tbody></table>

Before enabling this parameter, make sure that the data feed is not connected to the same cluster on which it is running. Otherwise, this can lead to quote looping in the platform.

[MetaTrader 4 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader4feeder)

[Trading Central News Feeder](/en/docs/mt5/platform/components/datafeeds/tcnewsfeeder)