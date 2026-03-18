# FXstreet Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/fxstreetfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)FXstreet Feeder

# FXstreet Feeder

FXstreet Feeder for MetaTrader 5 provides your clients with financial news, as well as the data on technical analysis from the [FXstreet.com](https://www.fxstreet.com/ "FXstreet.com") financial web portal. The news are provided in eight languages: English, Russian, Arabic, Chinese, German, Indonesian, Spanish and Turkish.

FXstreet Feeder is free and included in the platform standard delivery. Contact FXstreet.com to subscribe to the news. Contact details can be found on the web portal at ["Contact Us"](https://www.fxstreet.com/info/contact-us "Contact FXstreet.com") section.

## Setup

Add the new FXstreet Feeder data feed configuration via the [corresponding section](/en/docs/mt5/platform/administration/admin_feeds) of MetaTrader 5 Administrator:

![FXstreet Feeder Setup](/en/docs/mt5/platform/img/data_feeds_server_fxstreet.png "FXstreet Feeder Setup")

The following parameters must be specified on the ["Common"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup) tab of the data feed:

-   Module — FXstreetFeeder(64);
-   Feed server — FXstreet server address. subscriptions.fxstreet.com is set by default;
-   Feed login — login (or Client Key) for connection to FXstreet server. Submitted by FXstreet when concluding an agreement for providing news feed.

![FXstreet Feeder Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_fxstreet.png "FXstreet Feeder Parameters")

Specify additional settings in the [Parameters](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab:

-   Language — the language in which you wish to receive news. For each language, create a separate "Language" parameter with the appropriate value. For example, in order to receive news in English and Russian, you need to create two parameters: Language = english, Language = russian. If no language is specified, the datafeed will only deliver news in English.  
    The following languages are supported:
    -   arabic
    -   chinese
    -   english
    -   french
    -   german
    -   indonesian
    -   russian
    -   spanish
    -   thai
    -   tradchinese
    -   turkish
    -   japanese
    -   vietnamese
-   News Type — the type of news you wish to receive:
    -   News — standard subscription.
    -   FXBeat — news from famous Forex market participants featuring their personal opinion. To receive such newsletters, contact FXStreet.com for an appropriate subscription. FXStreet.com will provide a new Client Key or include the FXBeat subscription into the key your are using.
    -   Crypto — cryptocurrency market news.
-   News Category — the category name for the newsletters received from the data feed. The category name can then be used for specifying news to be delivered to client [groups](/en/docs/mt5/platform/administration/admin_groups).

The client terminals will start receiving news right after enabling the data feed. The data feed [logs](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed) can be requested to check its operation.

[KnowledgeView News Feeder](/en/docs/mt5/platform/components/datafeeds/knowledgeviewnewsfeeder)

[Financial Source News Feeder](/en/docs/mt5/platform/components/datafeeds/financialsourcenewsfeeder)