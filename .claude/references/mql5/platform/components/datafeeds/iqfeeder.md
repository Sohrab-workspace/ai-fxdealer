# IQFeeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/iqfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)IQFeeder

# IQFeeder

The IQFeeder is designed for receiving news and price data from [IQFeed](https://www.iqfeed.net). The company offers brokers a wide range of services:

-   Real-time quotes for financial instruments traded on the US and Canadian exchanges: NYSE, NASDAQ and Canadian Securities Exchange, among others
-   Real-time quotes for Forex instruments
-   Level II data (order book)
-   More than 700 market stats/breadth indicators, most of which are updated every second
-   Up to 180 calendar days of tick history
-   More than 11 years of one-minute historical data
-   Fundamental data on US stocks
-   Real-time news from leading agencies

IQFeeder is free and is included in the standard platform delivery package. You only need to subscribe for the data by contacting [IQFeed](https://www.iqfeed.net) and then to configure the data feed in the platform.

## How It Works

IQFeed provides a special software (IQFeed Client) that is responsible for information delivery from the provider to the local server where this software is installed. These data are translated to the history server via the IQFeeder data feed. Interaction between the data feed and the IQFeed client is implemented through the local IP address 127.0.0.1.

IQFeed Client is already available in the data feed. During data feed configuration in the platform, the required components will be installed automatically and thus no additional installation will be required.

## Setup

IQFeed provides data for a variety of trading instruments. In order to be able to receive relevant data, you need to [create corresponding symbols](/en/docs/mt5/platform/administration/admin_symbols). If you want to receive the order book in addition to quotes, enable the appropriate option in symbol settings:

![Enabling the Market Depth in trading symbol settings](/en/docs/mt5/platform/img/iq_feed_symbol_dom.png "Enabling the Market Depth in trading symbol settings")

Set a value other than "off" for the Market Depth parameter. If the initial depth of the Market Depth is different, the data feed will automatically align it with the value specified in the symbol settings in the platform. The price accuracy in the Market Depth will be automatically adjusted to the value specified in symbol settings.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:bottom;"><p class="p_tableatten"><span class="f_tableatten">If symbol names on you platform side differ from those available in IQFeed, you can match corresponding symbols in the data feed settings, under the "<a href="/en/docs/mt5/platform/administration/admin_feeds/feed_setup#translation" class="topiclink">Translation</a>" settings.</span></p></td></tr></tbody></table>

Once you have prepared the symbols, create a new [data feed configuration](/en/docs/mt5/platform/administration/admin_feeds) for IQFeeder.

![Server](/en/docs/mt5/platform/img/data_feeds_server_iq.png "Server")

The following parameters should be specified on the ["Common"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data feed:

-   Module — IQFeeder.
-   Feed server — 127.0.0.1, this address is used to implement connection between the data feed and the IQFeed client, it cannot be changed.
-   Feed login — login for connection, which is provided by IQFeed upon subscription
-   Password — password for connection, which is provided by IQFeed upon subscription.

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_iq.png "Parameters")

On the ["Parameters"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab, specify "Product ID" that was received from the news provider and additional settings (if needed).

-   News Category — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).
-   Product — product identifier. It is provided by IQ Feed upon subscription.
-   L2 Realtime — set "Yes" to be able to receive the Market Depth data. Access to the relevant data must be granted by your IQFeed subscription and the [Market Depth feature must be allowed](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#dom) in symbol settings on the platform side.
-   Download Tick History — if set to "Yes", the data feed will download the available tick history of trading instruments.
-   Download M1 History — if set to "Yes", the data feed will download the available one-minute history of trading instruments.
-   Download D1 History — if set to "Yes", the data feed will download the available daily history for trading instruments. If this parameter is enabled along with the "Download M1 History" option, the daily history will only be downloaded for the periods for which one-minute history is not available.
-   Admin Port, Lookup Port, L1 Port, L2 Port, History Port — the ports on which IQFeed Client waits for incoming connections to feed appropriate data (L1 and L2 prices, quoting history). The default values correspond to IQFeed Client ports.
-   Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow.
-   Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
-   Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
-   Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.

Before importing the price history, check the list of symbols configured in the data feed. If the data feed is allowed to download history, it will replace the history of all symbols within the platform, for which the data feed has permissions.

![Setup of symbol access for the data feed](/en/docs/mt5/platform/img/iq_feed_symbols.png "Setup of symbol access for the data feed")

[DJ News Feeder](/en/docs/mt5/platform/components/datafeeds/djnewsfeeder)

[MetaTrader 4 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader4feeder)