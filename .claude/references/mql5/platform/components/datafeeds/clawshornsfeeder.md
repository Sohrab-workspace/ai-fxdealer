# Claws & Horns Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/clawshornsfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)Claws & Horns Feeder

# Claws & Horns Feeder

This data feed allows you to provide your clients with financial news and analytics from [Claws & Horns](https://www.clawshorns.com/):

-   economic calendar featuring all the important fundamental data
-   technical analysis
-   fundamental analysis
-   signals (market entry recommendations with entry/exit points that are updated throughout the day)
-   daily video podcasts with long-term outlook for the major currency pairs
-   daily analysis of Russian shares traded on the Moscow Exchange

Materials are provided in 15 languages, including Russian, English, Chinese, Spanish, French, German, etc.

Claws & Horns Feeder is free and included in the platform standard delivery. You can purchase subscription on the [Claws & Horns official website](https://www.clawshorns.com).

## Setup

Add the new Claws & Horns Feeder data source configuration via the [corresponding section](/en/docs/mt5/platform/administration/admin_feeds) of MetaTrader 5 Administrator:

![Claws & Horns Feeder setup](/en/docs/mt5/platform/img/clawshorns_common.png "Claws & Horns Feeder setup")

The following parameters should be specified on the [Common](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data source:

-   Module — ClawsHornsFeeder64.
-   Feed server — Claws & Horns server address. api.clawshorns.com is set by default. There is no need to change it.
-   Password — when purchasing the subscription, you receive a special ID (token) consisting of 32 symbols. Enter it here.

![Claws & Horns Feeder parameters](/en/docs/mt5/platform/img/clawshorns_param.png "Claws & Horns Feeder parameters")

On the ["Parameters"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab, you can also use an additional parameter "News Category" — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).

The client terminals will start receiving news right after enabling the data source. The data source [journal](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed) can be requested to check its operation.

[Financial Source News Feeder](/en/docs/mt5/platform/components/datafeeds/financialsourcenewsfeeder)

[UniNewsFeeder](/en/docs/mt5/platform/components/datafeeds/uninewsfeeder)