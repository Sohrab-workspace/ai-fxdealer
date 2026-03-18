# UniNewsFeeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/uninewsfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)UniNewsFeeder

# UniNewsFeeder

UinNewsFeeder is a universal news feed applying the new UniNews protocol.

MetaQuotes Software Corp. has developed its own binary news transfer protocol allowing for high speed of broadcasting news to the MetaTrader 4/5 platforms. Further on, it will allow using news in algorithmic trading by accessing them via MQL5 and the strategy tester.

The new protocol will be of interest to news providers since the integration is completely ready on the side of all MetaTrader 4/5 brokers. The free UinNewsFeeder data feed is able to receive news from any source supporting the new protocol.

## Operation principles

UniNewsFeeder connects to the news provider server and requests news using keywords in multiple languages. First, the data feed receives news missed during its inactivity. After that, the news arrive in real time.

## Setup

Add the new UniNewsFeeder data feed configuration via [the corresponding section of](/en/docs/mt5/platform/administration/admin_feeds) the MetaTrader 5 Administrator:

![UniNewsFeeder setup](/en/docs/mt5/platform/img/uninewsfeeder_common.png "UniNewsFeeder setup")

The following parameters should be specified on the [Common](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data feed:

-   Module — UniNewsFeeder64.
-   Feed server — news provider server address.
-   Login — login for connecting to the news provider's server.
-   Password — password for connecting to the news provider's server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Connection data is provided by a news provider.</span></p></td></tr></tbody></table>

Set the news language and keywords for sorting the news on the [Parameters](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab.

![UniNewsFeeder parameters](/en/docs/mt5/platform/img/uninewsfeeder_param.png "UniNewsFeeder parameters")

Set the incoming news language in the Languages parameter. The list of languages, in which you want to receive news, is comma-separated. For example, "russian,english,italian". The default value is "any". In this case, the data feed receives news in all languages in the MetaTrader 5 platform. Ask your news provider for the list of available languages.

In the Keywords parameter, set the keywords to be used by the data feed to request news. The default value is "any" (no filtration). Each news provider can sort out news using keywords. Ask your news provider for the list of keywords.

On the ["Parameters"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab, you can also use an additional parameter "News Category" — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).

The client terminals will start receiving news right after enabling the data feed. The data feed [journal](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed) can be requested to check its operation.

[Claws & Horns Feeder](/en/docs/mt5/platform/components/datafeeds/clawshornsfeeder)

[Alliance News Feeder](/en/docs/mt5/platform/components/datafeeds/alliancenewsfeeder)