# Monitor

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/toolbox/ug_toolbox_monitor

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
            -   [Monitor](/en/docs/mt4/administrator/toolbox/ug_toolbox_monitor)
            -   [Mailbox](/en/docs/mt4/administrator/toolbox/ug_toolbox_mailbox)
            -   [Journal](/en/docs/mt4/administrator/toolbox/ug_toolbox_journal)
            -   [Support](/en/docs/mt4/administrator/toolbox/ug_toolbox_support)
            -   [Articles](/en/docs/mt4/administrator/toolbox/toolbox_articles)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Toolbox](/en/docs/mt4/administrator/toolbox)Monitor

# Monitor

MetaTrader Server saves important parameters allowing to estimate the status of the trading server in the monitoring database every minute:

-   Connections  
    The amount of connections is the sum of all standard working connections of terminals and time connections established to make transactions, upload history or news. For the immovable market, a rather precise number of online users will be shown in this window.
-   Active Sockets  
    This rate shows the total number of connected TCP endpoints in the operating system (a TCP endpoint is a combination of the IP address and a port used). The rate includes half-open connections (when there is no connection already, but the socket is not closed by the operating system yet).  
    The number of active sockets is a good indicator for detecting DDoS attacks. For example, a sharp increase in the number of active sockets without an increase in the number of client connections, may indicate the start of a DDoS attack on the server. One should analyze the dynamics of this rate, not its absolute values.
-   Free Memory Capacity  
    It is very important that server possesses a large capacity of free memory: this enables to serve for a larger amount of simultaneously connected users and operate with large databases. If there is less than 100Mb of free memory, the chart will be colored with red.
-   Use of Processor  
    The total load of all accessible processors is measured. The speed of servicing for users and processing their trade operations depends on this parameter directly. If the load of the processor stably exceeds 50%, it is the high time to upgrade the computer. If it exceeds 85%, the chart is colored with red. But there is no reason to worry about non-permanent overloads.
-   Use of Network  
    The total load of the selected network interface is measured. The traffic of all programs launched on the computer must be considered. Unexpected loading jumps will indicate DoS attacks attempts.

Switching between charts is performed via context menu or by the "Space" button. Charts can be looked through every 5 minutes, every 15 minutes, or every 1 hour. All four charts can be saved as pictures using the context menu commands.

[Toolbox](/en/docs/mt4/administrator/toolbox)

[Mailbox](/en/docs/mt4/administrator/toolbox/ug_toolbox_mailbox)