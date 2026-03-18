# KnowledgeView News Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/knowledgeviewnewsfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)KnowledgeView News Feeder

# KnowledgeView News Feeder

KnowledgeView News Feeder is designed to receive news from [KnowledgeView](https://www.knowledgeview.co.uk/), a partner of [Dow Jones](https://www.dowjones.com/). It allows to receive news in real time in three languages: Arabic, Farsi and Turkish.

If you want to start getting the news, you need to contact KnowledgeView or Dow Jones to sign the agreement. The contact information can be found on the official websites of these companies: [Offices](https://www.knowledgeview.co.uk/aboutus/offices "Offices") section of the KnowledgeView official web site and [Contact Us](https://www.dowjones.com/contactus/contactus.aspx?sect= "Contact Us") section of the Dow Jones official web site. After concluding the contract you will receive the parameters for connecting a data feed to KnowledgeView server: address, login, password and additional Filter parameter.

## Setup

Add the new KnowledgeView News Feeder data feed configuration via the [corresponding section of the administrator terminal](/en/docs/mt5/platform/administration/admin_feeds).

![Common](/en/docs/mt5/platform/img/data_feeds_server_kw.png "Common")

The following parameters must be specified on the ["Common"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup) tab of the data feed:

-   Module — KnowledgeViewNewsFeeder(64);
-   Feed server — KnowledgeView server web address. The default web address is http://fareeda.info/newsbrowser/api.
-   Feed login — login for connection to KnowledgeView server;
-   Password — password for connection to KnowledgeView server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Address, login and password are submitted by KnowledgeView during the agreement conclusion. A separate login and password are submitted for each news language. Thus, you should create several configurations for that data feed to get news in several languages simultaneously.</span></p></td></tr></tbody></table>

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_kw.png "Parameters")

Specify the following parameters in the [Parameters](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab:

-   News Request Period — intervals to check and download new data in seconds. The data feed receives all available news during the first connection. After that, the latest news are checked at the specified intervals. The lower the value, the faster the news will appear in the platform. But this will increase the network load. The default value is 60 seconds.
-   News Filter — the value is provided by KnowledgeView upon the execution of an agreement. Separate Filter parameter value is specified for each news language in the same way as it is done with a login and a password.
-   News Max — the maximum number of news items which can received by the data feed. If this parameter value is low while "News Request Period" is large, some of the news items provided by the source can be lost. The default value is 128.
-   News Category — the category name for the newsletters received from the data feed. The category name can then be used for specifying news to be delivered to client [groups](/en/docs/mt5/platform/administration/admin_groups).

If the Filter value is incorrect, the data feed will not be able to connect to the server. These parameters can be checked in the [data feed log](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2012.03.28&nbsp;09:59:59&nbsp;&nbsp;&nbsp;Gateway&nbsp;&nbsp;&nbsp;datafeed&nbsp;initialized,&nbsp;connecting&nbsp;to&nbsp;http://fareeda.info/newsbrowser/api</span><br><span class="f_CodeExample">2012.03.28&nbsp;09:59:59&nbsp;&nbsp;&nbsp;Gateway&nbsp;&nbsp;&nbsp;available&nbsp;datafeed&nbsp;filter:&nbsp;'Forex&nbsp;Turkish'</span><br><span class="f_CodeExample">2012.03.28&nbsp;09:59:59&nbsp;&nbsp;&nbsp;Gateway&nbsp;&nbsp;&nbsp;available&nbsp;datafeed&nbsp;filter:&nbsp;'Forex&nbsp;Turkish&nbsp;-&nbsp;month'</span><br><span class="f_CodeExample">2012.03.28&nbsp;09:59:59&nbsp;&nbsp;&nbsp;Gateway&nbsp;&nbsp;&nbsp;specified&nbsp;filter&nbsp;'Turkish'&nbsp;is&nbsp;incorrect,&nbsp;check&nbsp;datafeed&nbsp;parameters</span><br><span class="f_CodeExample">2012.03.28&nbsp;09:59:59&nbsp;&nbsp;&nbsp;Gateway&nbsp;&nbsp;&nbsp;filter&nbsp;checking&nbsp;failed</span></p></td></tr></tbody></table>

In addition to the entries indicating the errors in the filter specification, the data feed log also displays available filter values (the entries of "available datafeed filter" type). The terminal will start receiving news right after the successful connection.

[ForexPros Feeder](/en/docs/mt5/platform/components/datafeeds/forexprosfeeder)

[FXstreet Feeder](/en/docs/mt5/platform/components/datafeeds/fxstreetfeeder)