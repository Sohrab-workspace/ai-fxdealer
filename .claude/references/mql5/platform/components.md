# Platform Components

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)Platform Components

# Platform Components

The trading platform consists of the following components:

-   [Main Trade Server](/en/docs/mt5/platform/components/trade_server)  
    Besides the tasks of maintaining trading, this sever is designed for managing the entire platform. It means that the administrator of the main trade server can control the entire system.
-   [Trade Servers](/en/docs/mt5/platform/components/trade_server)  
    Besides the main trade server, the unlimited number of trade servers can be installed. They are intended for storing and managing all client and trade databases; trading activities are performed through them.
-   [Access Server](/en/docs/mt5/platform/components/access_server)  
    Access servers are proxy servers and firewalls of the system at the same time. They check clients' connections, collect authorization information and route clients' connections. Besides that access servers cache the largest part of all data transmitted to a client (including history data and terminal updates).
-   [History Server](/en/docs/mt5/platform/components/history_server)  
    History server receives, processes and stores price data, news and updates, and transmits them to other components of the system.
-   [Backup Server](/en/docs/mt5/platform/components/backup_server)  
    Backup servers create backups of both history and trade servers.
-   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)  
    Data feeds are special components of the platform that are implemented as separate executable files that enable the receipt of news and quotes from different providers.
-   [Gateways](/en/docs/mt5/platform/components/gateways)  
    Gateways are intended for integration of the MetaTrader 5 platform with ECNs and exchanges. Gateways allow bringing out trade operation to external systems as well as translating quotes and news from them.
-   [Administrator Terminal](/en/docs/mt5/platform/administrator)  
    This terminal enables the remote control of the entire MetaTrader 5 platform. It allows changing any platform settings, managing client and trade databases and perform other operation.
-   [Manager Terminal](/en/docs/mt5/platform/platform_installation/white_label)  
    This terminal is used for working with the broker's clients: managing databases, servicing trading operations, reporting and managing risks.
-   [Client Terminal for Windows](https://support.metaquotes.net/en/docs/mt5/client)  
    The trader's main workstation enabling traders to analyze quotes and to execute trading operations. It features algo trading and strategy testing facilities.
-   [Mobile Terminal for iOS](https://support.metaquotes.net/en/docs/mt5/iphone)  
    It enables traders to manage their trading accounts, to view symbol charts and to perform trading operations using iPhone or iPad.
-   [Mobile Terminal for Android](https://support.metaquotes.net/en/docs/mt5/android)  
    The terminal enables traders to manage their trading accounts, to view symbol charts and to perform trading operations using Android powered smartphones and tablets.
-   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)  
    MetaTrader 5 WebTerminal allows trading in the financial markets via a web browser. It works in all operating systems and browsers requiring no additional software.
-   [MetaTrader 5 API](https://support.metaquotes.net/en/docs/mt5/api)  
    It is a toolkit which allow further expansion of the platform capabilities, integration with other trading systems and back-office components, as well as platform customization for specific business needs.

## Interaction of Components

The MetaTrader 5 trading platform is a distributed system. It is divided into separate components that are connected to each other via the main trade server. Configurations of all the platform components are stored on the main server. Other components refer to the main trade server, read the configurations and operate then in accordance with them.

![The platform architecture](/en/docs/mt5/platform/img/architecture.png "The platform architecture")

The internal identification of servers is performed using IDs and passwords set during their [installation](/en/docs/mt5/platform/platform_installation). You can view or change identifiers and passwords in the ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#identifier) section. The main trade server identifies a component that has referred to it by its ID and passes to it configurations set for this component.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The minimal working configuration of the platform is the installed main trade server and an access server. The access server allows the connection to the main server using terminals (client, manager or administrator terminal).</span></p></td></tr></tbody></table>

[Platform Uninstall](/en/docs/mt5/platform/platform_installation/platform_uninstall)

[Trade Server](/en/docs/mt5/platform/components/trade_server)