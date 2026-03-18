# Installing and Setting Up

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/unidde/unidde_setup

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)[Universal DDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde)Installation and Setup

# Installing and Setting Up

In order to start installing the Universal DDE Connector, download it from the [technical support website](https://support.metaquotes.net/spfiles/datafeeds/uniddesetup9.exe "Download UniDDE") of MetaQuotes Software Corp. After that start the executable file and perform the simple installation procedure. As soon as the installation is over, start UniDDE.

To prepare UniDDE for connecting MetaTrader5UniFeeder to it, a some configurations are required.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">After you set up UniDDE, you'll need to <a href="/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols" class="topiclink">set up symbols</a> for translating quotes.</span></p></td></tr></tbody></table>

![Universal DDE Connector](/en/docs/mt5/platform/img/unidde.png "Universal DDE Connector")

## Account Setup [#](unidde_setup#account)

During the program installation, one account for accessing from a local computer is created. To enable connection of MetaTrader5UniFeeder to UniDDE an account must be opened - execute the "Add" command in the context menu of the accounts block:

![Accounts](/en/docs/mt5/platform/img/unidde_accounts.png "Accounts")

After you press it, a new line will appear, where you should enter the following data:

-   Login — login for access;
-   Password — password for access;
-   IP Access List — list of allowed IP addresses, separated by commas. Connection using the above specified login and password will be possible only from the specified IP addresses.

Date and time of the last access to UniDDE from a specified account is displayed in column "Last Access".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To provide higher security, besides accounts with the allowed IP addresses, UniDDE provides the permanent control of all connections with automatic blocking to prevent DoS attacks. In real-time mode, all network connections are analyzed, and if a non-standard activity is detected. the IP address is automatically closed for 5 minites.</span></p></td></tr></tbody></table>

## Setup of Connection Port [#](unidde_setup#port)

Port specification is also required for connecting MetaTrader5UniFeeder. By default port 2222 is used, but you can change it in field "Server port".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The specified port must be open on the server where UniDDE is installed.</span></p></td></tr></tbody></table>

## Setup of Tick Storage

Universal DDE Connector allows storing tick data received from data sources. To do it, tick off field "Save Ticks History". Tick data are saved in file universalddeconnector.ticks, which is located in the UniDDE installation directory.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When selecting the option of saving of tick data, you should watch the file size they are stored in. If ticks are saved for a long time period and for a great number of symbols, the file size can reach tens of gigabytes.</span></p></td></tr></tbody></table>

## Journal

Results of connecting to a quotes feeder or of the connection of MetaTrader5UniFeeder, as well as other important messages about the operation of UniDDE are reflected in the journal. To open it, press "Journal". All messages are displayed as a table with the following fields:

-   Time — date and time of message creation;
-   IP — IP address the message is connected with. For example, the IP address of MetaTrader5UniFeeder when it is connected to UniDDE;
-   Message — text of the message.

[Universal DDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde)

[Setting Up Symbols](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols)