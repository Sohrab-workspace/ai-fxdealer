# Setting Up Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)[Universal DDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde)Setting Up Symbols

# Setting Up Symbols

Universal DDE Connector uses the standard DDE protocol (Dynamic Data Exchange) for accepting quotes from any data source that supports this protocol. During installation of UniDDE, a set of symbols is created, which are configured for receiving quotes from the MetaTrader 4 client terminal. In order to start translating quotes from a client terminal, start it and enable option "Allow DDE Server".

-   Adding a symbol  
    In order to add a new symbol, enter its name in field "New Symbol", and then press "Add".
-   Editing a symbol  
    In order to change symbol settings, click twice on it in the list or execute the "Edit" command of the context menu.
-   Deleting a symbol  
    In order to delete a symbol, select it in the list and press "Delete" or execute the same command of the context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">After adding a symbol, restart UniDDE. Close it using the command of its context menu called by a right click on the icon in the area of notifications. Closing of the UniDDE window does not stop its running, and only minimizes it to the area of notifications.</span></p></td></tr></tbody></table>

## Symbol Setup

When adding or editing a symbol, a window of its setting appears:

![Symbol settings](/en/docs/mt5/platform/img/unidde_symbol.png "Symbol settings")

Settings in this window are divided into several blocks:

### Common parameters

-   Symbol — name of the symbol in Latin letters up to 15 symbols long. A [symbol](/en/docs/mt5/platform/administration/admin_symbols) of the same name must be created on the MetaTrader 5 server. The symbol name should not necessarily be the same as the symbol name on the data source;
-   Digits — the number of decimal places. The parameter value must be the same as the [analogous symbol parameter](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#digits) on the MetaTrader 5 server;
-   Spread — automatically set spread. Setup of this option is possible only if one price Bid or Ask is received;
-   Force Precision — force transformation of prices like 12345 to 1.2345 if data are received without a separator.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/platform/administration/admin_symbols" class="topiclink">A symbol</a> with exactly the same name must be created on the MetaTrader 5 server.</span></p></td></tr></tbody></table>

### DDE Link

In this block parameters of quote receiving from a supplier are configured.

-   Server — name of the source server in the DDE protocol. The most popular data sources can be selected from the list here. Other symbol settings corresponding to it will be set up automatically.
-   Bid topic, Bid item — settings for receiving Bid prices;
-   Ask topic, Ask item, Use — settings for receiving Ask prices. In the "Use" field you can enable/disable direct collection of these data. In this case the Ask price will be calculated automatically based on the value specified in field "Spread";
-   Volume topic, Volume item, Use — parameters for receiving the Ask price. In the "Use" field you can enable/disable direct collection of these data;
-   Bank topic, Bank item, Use — parameters for receiving information about the bank that issued the prices. In the "Use" field you can enable/disable direct collection of these data;
-   List of banks — the list of banks, from which quotes are allowed (separated by commas). Tick off "Auto" to enable the automatic bank selection mode. The auto-selection of banks is described in the section about [filtration](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Data receiving parameters are set up automatically is you select a server of one of suppliers in the "Server" filed.</span></li><li class="p_tableatten"><span class="f_tableatten">Contact the supplier for parameters of data receipt.</span></li><li class="p_tableatten"><span class="f_tableatten">Often, for futures instruments the Last price (price of the last executed deal) is translated. In this case symbols in UniDDE are configured manually so that the Last price is translated as Bid, and Ask is calculated based on tis price and spread settings.</span></li></ul></td></tr></tbody></table>

### Filtration

Filtration parameters for received quotes is set up here.

-   Auto limit — value of the [maximally allowed deviation](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration#auto_limit) of a new price from the previous one in percents. If the difference between the new price and the previous one exceeds the specified limit, the new price is filtered away (is not passed to the server). This allows to prevent the accidental price substitution for different symbols (for example : USDJPY instead of USDCHF);
-   Automatic filter — enable/disable the automatically adjustable quote filtration. This mode is described in the section devoted to [filtration](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration#white_noise).
-   Accept bid/ask independently — by default, quotes are sent to clients (MetaTrader5UniFeeder) only if Bid has changed. The change of Ask is preserved in such a case, but quotes are not sent to client connection until Bid is updated. This tick allows to disable this behavior and translate new prices when Ask is updated.
-   Use specific time session — use separate time periods. If this option is enabled, fields "Session from" and "To" become active. There you can set time limits for translating symbol quotes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Option "Accept bid/ask independently" cannot be enabled for Forex symbols. Quotes where only Ask has changed are considered incorrect and are filtered out by the server. This can create additional load.</span></p></td></tr></tbody></table>

## Applying Profiles

A number of ready parameters for receiving quotes from different data feeders are available in UniDDE. To quickly switch between providers, you can use the special command "Apply template..." in the context menu of the symbols list.

![Parameters templates](/en/docs/mt5/platform/img/unidde_templates.png "Parameters templates")

Select here a necessary quote provider. To save the current set of symbols and their parameters, press "Save symbols...".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When you change the provider, parameters of all symbols in the list are changed. So be careful using this procedure. In some systems, parameters of symbols may differ, and some of them can stop working when you change the provider.</span></li><li class="p_tableatten"><span class="f_tableatten">Each time you change provider, a backup copy of the previous state (file with SYM extension) is created in the "backup" folder located in the UniDDE installation directory. To restore the list of symbols, only use command "Load symbols..." and specify a required file.</span></li></ul></td></tr></tbody></table>

[Installation and Setup](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_setup)

[Filtration of Quotes](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration)