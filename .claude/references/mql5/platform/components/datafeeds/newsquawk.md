# Newsquawk Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/newsquawk

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)Newsquawk

# Newsquawk Feeder

Data feed for receiving financial newsletters from the [Newsquawk](https://newsquawk.com/) company. Newsquawk provides real-time access to the most important financial news, filtering data streams from hundreds of sources, such as Reuters, Bloomber and Daily Mail, among others. Additionally, you can receive daily market overviews across various categories of financial instruments, including forex, metals, stocks and commodities.

## Preparation

Fill our a form on the [Newsquawk website](https://www.newsquawk.com/sign_up.html). The company offers a free one-week trial subscription. After registration, you will receive a login/password or key to your email, which will be required to set up the data feed in the platform.

The built-in data feed module is already available in your platform. No fee is charged for the module use.

## Configuring the Data Feed

Add a new data feed configuration via the [corresponding section](/en/docs/mt5/platform/administration/admin_feeds) of MetaTrader 5 Administrator:

![Create a data feed configuration and specify parameters](/en/docs/mt5/platform/img/data_feed_newsquawk.png "Create a data feed configuration and specify parameters")

Specify the following parameters:

-   Feed server — news provider's server address. The default address is https://newsquawk.com. In most cases, there is no need to change it.
-   Feed login — login for connection provided by Newsquawk upon subscription.
-   Password — password for connection provided by Newsquawk upon subscription.
-   Authorization Token — key for connection provided by Newsquawk upon subscription. You can use either this parameter or Login/Password, depending on the credentials provided.
-   Language — a two-letter language code in ISO 639 format that will be included in incoming news. For example, en, es, pt, etc. It will be used to filter news by language on the client terminal side. Fill in this parameter in accordance with the language selected during subscription, that is, the language in which you actually receive the news. To receive news in different languages, create separate data source configurations.
-   Process Updates — Newsquawk may update and supplement previously published news. The parameter determines whether the data feed will transmit such updates to the platform. On the MetaTrader 5 side, each update will create additional news; previously transmitted news will not be changed. The default is "Yes" meaning updates are transmitted.
-   News Category — the category to which newsletters from the data source will be assigned. The category name can then be used for specifying news to be delivered to certain client [groups](/en/docs/mt5/platform/administration/admin_groups).

Once the data feed is enabled, client terminals will start receiving newsletters. To check the data feed operation, request its [logs](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed).

[Alliance News Feeder](/en/docs/mt5/platform/components/datafeeds/alliancenewsfeeder)

[Remote Datafeed](/en/docs/mt5/platform/components/datafeeds/remote_datafeed)