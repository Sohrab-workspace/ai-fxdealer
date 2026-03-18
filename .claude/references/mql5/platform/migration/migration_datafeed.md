# Data Feeds

> Source: https://support.metaquotes.net/en/docs/mt5/platform/migration/migration_datafeed

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
            -   [General Settings](/en/docs/mt5/platform/migration/migration_general)
            -   [Financial Instruments](/en/docs/mt5/platform/migration/migration_symbols)
            -   [Trade Groups](/en/docs/mt5/platform/migration/migration_group)
            -   [Import of Accounts and Trades](/en/docs/mt5/platform/migration/migration_account_trade)
            -   [Manager Accounts](/en/docs/mt5/platform/migration/migration_manager)
            -   [Data Feeds](/en/docs/mt5/platform/migration/migration_datafeed)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Migration from MetaTrader 4](/en/docs/mt5/platform/migration)Data Feeds

# Data Feeds

Any sources of quotes and news used in the MetaTrader 4 platform can be easily moved to MetaTrader 5. There are three options to receive a stream of quotes:

-   From the MetaTrader 4 server having a trading account via [MetaTrader 4 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader4feeder).
-   From other data terminals via [UniDDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde).

Apart from quote and news already working in the MetaTrader 4 platform, you can receive data via the new feeders designed specifically for MetaTrader 5. You can find out the details in the [Data Feeds](/en/docs/mt5/platform/components/datafeeds) section.

## Receiving Quotes from the MetaTrader 4 Server

If both platforms work simultaneously, use [MetaTrader 4 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader4feeder) to receive quotes and news from the MetaTrader 4 server. Add the new [data source](/en/docs/mt5/platform/administration/admin_feeds):

![Receiving quotes and news via MetaTrader 4 Feeder](/en/docs/mt5/platform/img/data_feeds_common.png "Receiving quotes and news via MetaTrader 4 Feeder")

Select MetaTrader4Feeder in the Module field and enter server's IP address and port, as well as account login and password in the Feed server, Feed login and Password fields to connect to the MetaTrader 4 server.

MetaTrader 5 allows sorting out news by language. To do this, set the Language parameter on the Parameters tab:

![Receiving quotes and news via MetaTrader 4 Feeder](/en/docs/mt5/platform/img/data_feeds_parameters.png "Receiving quotes and news via MetaTrader 4 Feeder")

News coming from MetaTrader 4 servers can be in text or HTML formats. In case of a text format, setting the Language parameter is desirable for a proper language recognition and correct news display.

The news language in HTML format is automatically defined by the "charset" attribute built in the news. The language name is specified in the format that is standard for Windows operating systems without defining the dialectical features by geographic location, for example, English, Russian, etc.

## Receiving Quotes via UniDDE Connector

If your MetaTrader 4 server receives quotes via [UniDDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde), you can use MetaTrader5UniFeeder component to receive them in MetaTrader 5.

DDE Connector allows collecting quotes from various data sources that support the DDE (Dynamic Data Exchange) protocol. The feeder translates quotes received from it to the MetaTrader 5 History Server.

Add the necessary data source via the corresponding section of MetaTrader 5 Administrator:

![Receiving quotes via UniDDE Connector](/en/docs/mt5/platform/img/data_feeds_server_uni.png "Receiving quotes via UniDDE Connector")

Set the server address where UniDDE Connector is installed, as well as connection port and account preliminarily created in UniDDE Connector (login and password) in the source settings.

MetaTrader5UniFeeder allows receiving quotes for the symbol data not transmitted via UniDDE Connector. This is achieved by mathematical conversion of other symbols' quotes transmitted via UniDDE Connector. This method of calculation can be applied to non-freely convertible currencies with their exchange rates to the major world currencies defined by the central bank.

To receive quotes for such symbols, specify the quote calculation equations on the Parameters tab of a data source:

![Receiving quotes via UniDDE Connector](/en/docs/mt5/platform/img/data_feeds_parameters_uni.png "Receiving quotes via UniDDE Connector")

[Manager Accounts](/en/docs/mt5/platform/migration/migration_manager)

[App Store](/en/docs/mt5/platform/appstore)