# Financial Source News Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/financialsourcenewsfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)Financial Source News Feeder

# Financial Source News Feeder

Financial Source News Feeder enables the real-time delivery of news related to global currencies as well as trading analytics. In their [https://financialsource.co](https://financialsource.co) website, Forex News state that they aim to be the first to deliver forex news to users and bring high probability trading opportunities. Their professional analysts scour global newswires so you catch every currency move.

Financial Source news items are divided into the following categories: Central Banks, Market Insights, Must Read, Order Flow Levels and Risk Events. The size of news items ranges from brief informative reports to copyright analytical articles, which describe the full picture of the global market.

The data feed module is free and is included in the platform standard delivery package. To start receiving news, you should request a subscription via the [official website](https://financialsource.co/). After that you will be provided with an Authorization Token for the data feed configuration.

## Setup

Add the new Financial Source News Feeder configuration via the [corresponding section](/en/docs/mt5/platform/administration/admin_feeds) of MetaTrader 5 Administrator:

![Financial Source News Feeder setup](/en/docs/mt5/platform/img/financialsource_common.png "Financial Source News Feeder setup")

The following parameters should be specified on the [Common](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data source:

-   Module — ForexSourceNewsFeeder64.
-   Feed server — Financial Source server address. https://server.financialsource.co is set by default.

![Financial Source News Feeder parameters](/en/docs/mt5/platform/img/forexsource_param.png "Financial Source News Feeder parameters")

Specify the following settings in the Parameters tab:

-   Authorization Token — API Key, a special key to connect to the server. provided after subscribing to the news.
-   Language — the news language. For example, en for English, es for Spanish, it for Italian, ar for Arabic, ru for Russian, de for German. Please contact Financial Source for the full list of supported language. English is used by default.
-   Process Updates — the news items broadcasted by Financial Source may change over time. For example, they may be adjusted or clarified. If the parameter is set to "Yes", the data feed will process these changes and send new versions of these news items to the platform (earlier received news letters cannot be changed). If the parameter value is "No", the data feed will not process changes and this only initial news versions will be available in the trading platform. The default value is "Yes".
-   News Category — the category name for the newsletters received from the data feed. The category name can then be used for specifying news to be delivered to client [groups](/en/docs/mt5/platform/administration/admin_groups).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In order to receive news in several languages, create several data source configurations.</span></p></td></tr></tbody></table>

The client terminals will start receiving news right after enabling the data source. The data source [journal](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed) can be requested to check its operation.

[FXstreet Feeder](/en/docs/mt5/platform/components/datafeeds/fxstreetfeeder)

[Claws & Horns Feeder](/en/docs/mt5/platform/components/datafeeds/clawshornsfeeder)