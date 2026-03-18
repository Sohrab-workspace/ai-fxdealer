# Trading Central News Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/tcnewsfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)Trading Central News Feeder

# Trading Central News Feeder

Trading Central News Feeder is a data feed that enables receiving of analytical information on financial instruments from Trading Central ([www.tradingcentral.com](https://www.tradingcentral.com "Trading Central")). The basic activity of this company is the technical analysis trading recommendations sent by this company are based on.

Trading Central uses a FTP server to store data. In order to get access to these data, you should contact this company. To know the contact information, please visit the company's official website mentioned above. After you conclude an agreement, you are provided with the IP address of the FTP server, as well with the login and password for accessing it. Besides you will need to provide the IP address of your server (access server) in order for them to add it to the list of allowed addresses.

After that the data feed needs to be correctly set up via the administrator terminal:

![TCNewsFeeder](/en/docs/mt5/platform/img/data_feeds_server_tc.png "TCNewsFeeder")

The following parameters should be specified on the ["Common"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data feed:

-   Module — TCNewsFeeder;
-   Feed server — address of the FTP server of Trading Central an a port to connect to it (separated by a colon). The data feed also supports connection via secure SFTP protocol. If you wish to use it, specify the protocol in the address, for example: sftp://sftp.tradingcentral.com. The connection address and the used protocol are determined by agreement with Trading Central.
-   Feed login — login to authorize on the server;
-   Password — password for the authorization.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For the data feed to work, one should allow ports 20 and 21 on the computer where it is installed. They are necessary to work with FTP server.</span></p></td></tr></tbody></table>

After you connect to the FTP server, the data feed starts downloading all available data. After the data re received, it removes them from the FTP server. Further connections to the server are established once in five minutes for checking and downloading new data.

Analytical information that comes from the data feed consists of several elements: the news body with a chart, signals on indicators and signals on Japanese candlesticks. The latter two elements are released not so often as news, so they are inserted only if necessary.

If the data feed operation is terminated, news can be received without the signals for some time, because the earlier signals have been deleted upon receipt already, while new haven't been received yet. While the data feed is operating, it keeps the last four signals in its memory, and inserts them to corresponding news on currency pairs.

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_tcn.png "Parameters")

The data feed features the following additional [parameters](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters):

-   News Category — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).
-   News Request Period — the period of checking and downloading new information in seconds.

[MetaTrader 5 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader5feeder)

[MetaTrader 5 UniFeeder](/en/docs/mt5/platform/components/datafeeds/metatrader5unifeeder)