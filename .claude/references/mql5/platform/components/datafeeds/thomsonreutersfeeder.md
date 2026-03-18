# Thomson Reuters Feeder

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/thomsonreutersfeeder

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)Thomson Reuters Feeder

# Thomson Reuters Feeder

Thomson Reuters Feeder is a data feed that enables receiving of financial information from Thomson Reuters ([http://thomsonreuters.com](https://thomsonreuters.com "Thomson Reuters")).

Information from this company is transferred through web services. In order to get an access to them, you will need to conclude a special agreement. Please contact the company representative in your region. The corresponding contact information can be found on the company's website mentioned above.

Once the agreement is concluded, a user is given an IP address, login and password to access the service, as well as a unique ID (AppID). All this information must be provided when setting up the data feed in the administrator terminal.

## Setup

![ThomsonReutersFeeder](/en/docs/mt5/platform/img/data_feeds_server_tr.png "ThomsonReutersFeeder")

On the "Common" tab of [data feed](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common), specify the following parameters:

-   Module — ThomsonReutersFeeder;
-   Feed server — address of the server of Thomson Reuters and port to connect to it separated with colon. A port that is used for connecting, must support connection through the secured https protocol (SSL), usually port 443 is used;
-   Feed login — login to authorize on the server;
-   Password — password for the authorization.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">IP address of the server, login and password are given when concluding the agreement.</span></li><li class="p_tableatten"><span class="f_tableatten">A port that is used for the connection must be allowed on the server where the data feed is installed.</span></li></ul></td></tr></tbody></table>

![Parameters](/en/docs/mt5/platform/img/data_feeds_parameters_tr.png "Parameters")

On the ["Parameters"](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) tab, specify one parameter — "Application ID". This parameter is a unique identifier of an application that connects to the server of Thomson Reuters. Its value is also given when concluding the agreement.

News can be filtered by categories (topics) using additional optional parameters Ignore Topics Codes and Allow Topics Codes. To allow news from specified categories and disable all other news, specify the codes of the desired categories in the Allow Topics Codes parameter, separated by commas. To disable selected categories and enable all others, specify the categories to disable in Ignore Topics Codes, separated by commas. In the above example, the following codes are specified in Ignore Topics Codes:

-   SPO: sport
-   MSIC: music news
-   BLG: blogs

In this case, the datafeed will receive all news letters, except those from the specified categories.

Please note that a news item can relate to several categories. If the news belongs to at least one of the categories specified in the parameter, it will be filtered out.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The full list of topic codes can be obtained from Thomson Reuters.</span></li><li class="p_tableatten"><span class="f_tableatten">News are filtered on Thomson Reuters side, the data feeds does not receive news by specified topics.</span></li></ul></td></tr></tbody></table>

Do not use the Language parameter to filter news. It won't affect the data feed. The filtration of news by language is set up in the [group configuration](/en/docs/mt5/platform/administration/admin_groups/groups_settings). Some news from Thomson Reuters may be transmitted without indication of the language. In this case the news will be passed to the terminals regardless of the languages specified in the group settings.

### Additional Settings

On the "Parameters" tab, you can specify additional settings:

-   News Category — the name of the category of news received from this data feed. Further this category name can be used to specify news to be received by separate [groups](/en/docs/mt5/platform/administration/admin_groups).
-   Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow.
-   Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
-   Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
-   Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.

[MetaTrader 5 UniFeeder](/en/docs/mt5/platform/components/datafeeds/metatrader5unifeeder)

[RSS News Feeder](/en/docs/mt5/platform/components/datafeeds/rssnewsfeeder)