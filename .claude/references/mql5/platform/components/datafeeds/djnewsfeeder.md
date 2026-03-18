# DJ News Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/djnewsfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)DJ News Feeder

# DJ News Feeder

DJ News Feeder (DJNewsFeeder.exe) is the news feeder from the world-famous news agency Dow Jones. Dow Jones Newswires include comprehensive reviews and analytical materials, macroeconomic events and speeches of officials, rolling market commentary and expert analysis, company reports, breaking news and much more.

## How it works

To start receiving news, you should request a subscription at [https://www.dowjones.com](https://www.dowjones.com). In a contract with the news provider, you will receive the port number for the data feed to listen to. Specify this port number in data feed settings. You should also receive the list of IP addresses, from which the new content will be provided. These addresses must also be specified in the data feed settings for additional security. Otherwise, the data feed will accept connections from any addresses at the specified port.

## Setup

![Common](/en/docs/mt5/platform/img/data_feeds_server_dj.png "Common")

Open the [Common](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) tab of the data feed settings and set the DowJonesNewsFeeder module.

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_dj.png "Parameters")

Additional settings should be configured in the [Parameters](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab:

-   Listening Port — the port number, at which the data feed will listen to connections from the data provider. Available in an agreement with the news provider.
-   White List — one or more IP addresses, from which connection to the data feed is allowed. If this parameter is not set, connection from any address is allowed.  
    If the exact IP address is not known, you can identify it by requesting the [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) of the history server or the [data feed](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed). The provider sends out news content, and if their address is not included in the list of allowed IPs, the data stream is blocked and an appropriate message is added to the journal. The logs also contain the address of the server, from which the data is sent. The log may look like this: address X.X.X.X is not white listed, disconnecting.
-   News Category — the category name for the newsletters received from the data feed. The category name can then be used for specifying news to be delivered to client [groups](/en/docs/mt5/platform/administration/admin_groups).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended that you specify the provider's IP address in the WhiteList parameter. This will increase the safety of operation.</span></p></td></tr></tbody></table>

[Dow Jones Prime Tass News Feeder](/en/docs/mt5/platform/components/datafeeds/djprimetassnewsfeeder)

[IQFeeder](/en/docs/mt5/platform/components/datafeeds/iqfeeder)