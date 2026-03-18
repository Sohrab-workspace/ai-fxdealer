# UniFeeder Protocol

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/unidde/unidde_protocol

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
                    -   [Installation and Setup](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_setup)
                    -   [Setting Up Symbols](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols)
                    -   [Filtration of Quotes](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration)
                    -   [UniFeeder Protocol](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_protocol)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)[Universal DDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde)UniFeeder Protocol

# UniFeeder Protocol

The general features of the UniFeeder protocol are provided below to help you understand its operation principles.

-   The data feed establishes TCP connections with a data source.
-   The data feed reads the data line by line. The "\\r\\n" sequence serves as a line separator.
-   Authorization:
    -   After connection is established, the data feed waits for a login request from the data source. The line containing "Login: " is expected, for example, "Login :\\n\\r". The "waiting login request" entry appears in the Journal while waiting for the request.
    -   After the request is received, the "login request received" entry appears in the Journal, and the data feed sends the line with the login to the data source, for example, "user\_test\\r\\n".
    -   The data feed waits for the password request from the data source. The line containing "Password: " is expected. The "login sent \[%S\], waiting password request" entry appears in the Journal while waiting for the request.
    -   After the request is received, the "password request received" entry appears in the Journal, and the data feed sends the line with the password to the data source, for example, "password\\r\\n".
    -   The data feed waits for the notification of successful authorization. The line containing "Access granted" is expected. The "password sent, waiting access confirmation" entry appears in the Journal while waiting for the request.
    -   After receiving the notification, the "Login: '%S' successful" entry appears in the Journal.
    -   The data feed sends the line containing the symbols, for which it is allowed to send quotes. The line looks as follows "> Symbols:USDRUB,EURUSD,EURRUB\\r\\n".
    -   The data feed switches to the data receipt mode (quotes and news).
-   Data receipt:
    -   The data feed reads the data line by line. The "\\r\\n" serves as a line separator.
    -   The lines beginning with ">" or "<" reserved characters are skipped, except for the lines beginning with "< News".
    -   If the "< News\\r\\n" line is received, the data feed switches to news receipt mode:
        -   After the "< News\\r\\n" line, the data feed reads the NewsTopic structure (read MetaTrader 4 API documentation for more details).
        -   Next, the data feed reads the news body. The size of the news body is set in bytes in the NewsTopic::len field.
        -   After reading the body, the news is sent to the platform, while the data feed continues the data receipt.
    -   If the line does not begin with "<" or ">", it is deemed to be a tick line.
        -   The tick line format: "<Symbol name> <bid> <ask>\\r\\n". Example: "USDJPY 1.0106 1.0099\\r\\n".
        -   If bid or ask is less than zero, or bid exceeds ask, the tick is skipped and the "failed to parse tick, invalid bid/ask" entry appears in the Journal.

Below is an example of the network exchange dump. The data sent by the data feed is shown in red:

<table class="help" cellspacing="0" cellpadding="10" border="0" style="width:100px; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:10px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">Welcome</span><br><span class="f_CodeExample">Login:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="background-color: #ff0000;">test_user</span><br><span class="f_CodeExample">Password:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="background-color: #ff0000;">test_password</span><br><span class="f_CodeExample">Access</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">granted</span><br><span class="f_CodeExample">USDJPY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">4.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">19.0000</span><br><span class="f_CodeExample">GBPUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">8.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">19.0000</span><br><span class="f_CodeExample">USDCHF</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">15.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">16.0000</span><br><span class="f_CodeExample">USDCHF</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">6.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">25.0000</span><br><span class="f_CodeExample">USDJPY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">6.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">17.0000</span><br><span class="f_CodeExample">GBPUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">6.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">21.0000</span><br><span class="f_CodeExample">USDCHF</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">7.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">24.0000</span><br><span class="f_CodeExample">USDJPY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">9.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">14.0000</span><br><span class="f_CodeExample">GBPUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">9.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">18.0000</span><br><span class="f_CodeExample">USDCHF</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">9.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">22.0000</span><br><span class="f_CodeExample">USDJPY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">5.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">18.0000</span><br><span class="f_CodeExample">GBPUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">4.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">23.0000</span><br><span class="f_CodeExample">USDCHF</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">7.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">24.0000</span><br><span class="f_CodeExample">USDJPY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">7.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">16.0000</span><br><span class="f_CodeExample">GBPUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">13.0000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">14.0000</span></p></td></tr></tbody></table>

[Filtration of Quotes](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration)

[Gateways](/en/docs/mt5/platform/components/gateways)