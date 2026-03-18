# MetaTrader 5 UniFeeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/metatrader5unifeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)MetaTrader 5 UniFeeder

# MetaTrader 5 UniFeeder

MetaTrader 5 UniFeeder is the data feed that enables receipt of quotes from the special utility — Universal DDE Connector. This solution is built into the platform, which ensures minimal delays in quote delivery.

## How It Works

Universal DDE Connector allows collecting quotes from different data feeds that support the DDE (Dynamic Data Exchange) protocol. The feeder translates quotes received from it to the MetaTrader 5 history server. More details about the Universal DDE Connector are given in a [separate section](/en/docs/mt5/platform/components/datafeeds/unidde).

## Setup

The data feed must be added via the [corresponding section](/en/docs/mt5/platform/administration/admin_feeds) of the administrator terminal.

![MetaTrader 5 UniFeeder](/en/docs/mt5/platform/img/data_feeds_server_uni.png "MetaTrader 5 UniFeeder")

The following parameters should be specified on the ["Common"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data feed:

-   Module — UniFeeder;
-   Feed server — address of the server where the Universal DDE Connector is installed and [port](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_setup#port) for connecting to it, separated by a colon;
-   Feed login — [account](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_setup#account), pre-created in the Universal DDE Connector;
-   Password — password of the account.

### Synthetic Quotes

MetaTrader 5 UniFeeder allows receiving quotes on symbols, whose data are not translated through Universal DDE Connector. This is achieved by way of mathematical conversion of other symbols' quotes translated through Universal DDE Connector. Such a calculation method can be applied to non-convertible currencies, whose exchange rate relative to convertible currencies is set by the central bank.

The calculation formulas for the quotes should be specified on the ["Parameters"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab of the data feed:

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_uni.png "Parameters")

Two fields are available here:

### Parameter

In the "Parameter" field, you should specify the symbol name and its price (Bid or Ask), that will be calculated according to the formula specified in the next field. The symbol name and the price type should be separated by a point, for example: GOLDVND.ask.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Symbol whose quotes are calculated must be present in the <a href="/en/docs/mt5/platform/administration/admin_symbols" class="topiclink">"Symbols"</a> section. Make sure that the two names match.</span></li><li class="p_tableatten"><span class="f_tableatten">Calculation of both Bid and Ask prices is required for all symbols.</span></li></ul></td></tr></tbody></table>

### Value

In this field the calculation formula should be specified. You may use:

-   Symbols — any symbol, whose quotes are received from Universal DDE Connector can be used for calculations. But only one symbol for one formula can be used. Do not forget to specify the price type to use (Bid or Ask). For example, EURUSD.bid.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A symbol that is used for calculation must exist in the trading platform. In addition, it must be added to the <a href="/en/docs/mt5/platform/administration/admin_feeds/feed_setup#symbols" class="topiclink">list of symbols</a>, the quotes for which are translated by the data feed.</span></p></td></tr></tbody></table>

-   Simple mathematical calculations — multiplication (\*), division (/), addition (+) and subtraction (-).
-   Brackets — you can use brackets "()" to define the calculation order.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">You cannot use negative numbers in formulas. Thus "-3 + 5" is incorrect. The correct expression will be "5 - 3".</span></li><li class="p_tableatten"><span class="f_tableatten">The separator of the integer and fractional part in formulas is also a point, irrespective of the operating system settings.</span></li><li class="p_tableatten"><span class="f_tableatten">Only one symbol, whose quotes are received from Universal DDE Connector can be used in every formula.</span></li><li class="p_tableatten"><span class="f_tableatten">Synthetic quotes calculated from other symbols cannot be used in formulas.</span></li></ul></td></tr></tbody></table>

## Additional Settings

On the "Parameters" tab, you can specify additional settings:

-   News Category — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).
-   Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow.
-   Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
-   Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
-   Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.

[Trading Central News Feeder](/en/docs/mt5/platform/components/datafeeds/tcnewsfeeder)

[Thomson Reuters Feeder](/en/docs/mt5/platform/components/datafeeds/thomsonreutersfeeder)