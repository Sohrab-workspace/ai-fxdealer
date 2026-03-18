# MetaTester and Remote Agents

> Source: https://support.metaquotes.net/en/docs/mt5/client/metatester

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
            -   [Expert Advisors and Custom Indicators](/en/docs/mt5/client/trade_robots_indicators)
            -   [Where to Find Trading Robots and Indicators](/en/docs/mt5/client/algotrading_get_ea_indicator)
            -   [How to Create an Expert Advisor or an Indicator](/en/docs/mt5/client/autotrading)
            -   [Strategy Testing](/en/docs/mt5/client/testing)
            -   [How the Tester Downloads Historical Data](/en/docs/mt5/client/test_preparation)
            -   [Strategy Optimization](/en/docs/mt5/client/strategy_optimization)
            -   [Testing Features](/en/docs/mt5/client/testing_features)
            -   [Testing Report](/en/docs/mt5/client/testing_report)
            -   [Testing Visualization](/en/docs/mt5/client/visualization)
            -   [Journal of Testing](/en/docs/mt5/client/tester_journal)
            -   [Optimization Types](/en/docs/mt5/client/optimization_types)
            -   [Real and Generated Ticks](/en/docs/mt5/client/tick_generation)
            -   [MetaTester and Remote Agents](/en/docs/mt5/client/metatester)
            -   [Global Variables](/en/docs/mt5/client/service_global)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)MetaTester and Remote Agents

# MetaTester and Remote Agents

Expert Advisors are tested and optimized using the so called agents, which are separate services on a computer for performing calculations. The agents can be local and remote.

Local agents are created automatically on the computer where the trading platform is installed. The number of local agents is equal to the number of logical cores.

A remote agent is a specialized service installed on a computer and used for testing and optimizing Expert Advisors in the strategy tester. The unlimited number of such agents can be connected to a platform. Use of remote agents considerably speeds up optimization of strategies, because each run is performed as a separate process on a separate agent. The process of remote agent connection to a strategy tester is described in a [separate section](/en/docs/mt5/client/strategy_optimization#farm).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Remote agents can be connected to the global cloud computing network <a href="/en/docs/mt5/client/mql5cloud" class="topiclink">MQL5 Cloud Network</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">Remote agents can only be used in 64-bit systems.</span></li></ul></td></tr></tbody></table>

Remote agents are installed as separate services in the operating system using the special application "metatester.exe" located in the trading platform installation folder.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To save traffic and disk space, as well as for security reasons:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">messages of Expert Advisors (Print() function), as well as messages about trade operations are not added to the Journal;</span></li><li class="p_tableatten"><span class="f_tableatten">DLL call is prohibited on remote agents.</span></li></ul></td></tr></tbody></table>

## Files and Folders [#](metatester#structure)

To store the service information, MetaTester creates the "Tester" folder in the directory where the application is located. It contains the following folders and files:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders and Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th><th class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Sub-folders</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" rowspan="2" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Agent-IP-address-port</span></p></td><td class="table" rowspan="2"><p class="p_fortable"><span class="f_fortable">The folders are created for each agent of the tester. The folder name contains the IP address and port number the agent runs on.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">logs</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The agent operation logs are stored in this folder.</span></p></td></tr><tr class="table"><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">bases</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">History data used by the agent are stored in this folder.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Manager</span></p></td><td class="table" colspan="3"><p class="p_fortable"><span class="f_fortable">This directory contains MetaTester component logs.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Log files of agents are automatically deleted two days or if their size exceeds 1 gigabyte.</span></p></td></tr></tbody></table>

## Working with MetaTester [#](metatester#setup)

In order to share the calculation powers of your computer with a trading platform over a local network or Internet, install remote agents. Agents can be installed and managed using the special utility MetaTester. It is available in the default standard trading platform package. Run metatester.exe from the platform installation folder.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Testing agents can be installed on any computer separately from the trading platform. To do this, copy and run the metatester64.exe file on the required computer. Service files and folders are installed to the directory where the MetaTester application is located. The metatester64.exe file is both the installer and the executable file required for the operation of agents.</span></li><li class="p_tableatten"><span class="f_tableatten">Agents can only be installed and used in 64-bit systems.</span></li></ul></td></tr></tbody></table>

The window of the MetaTester application consists of several tabs:

-   [Overview](/en/docs/mt5/client/metatester#overview)
-   [Services](/en/docs/mt5/client/metatester#services)
-   [MQL5 Cloud Network](/en/docs/mt5/client/metatester#cloud_network)
-   [Scheduler](/en/docs/mt5/client/metatester#scheduler)

### Overview [#](metatester#overview)

![Overview](/en/docs/mt5/client/img/metatester_overview.png "Overview")

This tab displays helpful information about the use of agents. It also displays statistics on the number of tests performed using the agents and the time spent on them. The statistical data are available for two agent operation modes:

-   Local statistics  
    In the local mode, agents are used as service installed in a computer. The specified address and password are used for connecting to them.
-   MQL5 Cloud Network statistics  
    In this mode, the agents work within the special [MQL5 Cloud Network](/en/docs/mt5/client/metatester#cloud_network).

### Services [#](metatester#services)

![Services](/en/docs/mt5/client/img/metatester_services.png "Services")

On this tab you can manage agents on your computer. To install testing agents specify the following:

-   Agents — number of agents you want to install. It is recommended to install as many agents as there are logical processor cores.
-   Password — password for connection to agents. The password must be specified when you [add agents](/en/docs/mt5/client/strategy_optimization#farm) in the strategy tester.
-   TCP Ports — the range of ports (or one port to install one agent) the agents will work on. The port number must also be specified when connecting to agents from the strategy tester.

To install the agents click Add. Agents are installed at the IP address specified at the top of the tab. Use this address to connect to the agents.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To install and manage agents, a user needs administrator permissions on the system.</span></p></td></tr></tbody></table>

The list of installed agents is displayed at the bottom of the window:

-   Service — the name of the service, under which the agent is running in the operating system. The name is assigned automatically;
-   Port — the number of the port the agent is operating on;
-   Passes — number of testing passes performed by the agent;
-   Traffic In/Out — amount of incoming and outgoing traffic of the agent;
-   Cloud — network connection state. This option allows to ensure that agents can receive tasks from the cloud computing network.
-   State — the currents state of the agent: running or stopped.

### Context menu

Installed agents can be managed using the context menu commands:

-   ![Start](/en/docs/mt5/client/img/metatester_start_icon.png "Start") Start — start the selected agent;
-   ![Stop](/en/docs/mt5/client/img/metatester_stop_icon.png "Stop") Stop — stop the selected agent process. The appropriate service in the system is also stopped, and connecting to the agent is impossible;
-   ![Restart](/en/docs/mt5/client/img/metatester_restart_icon.png "Restart") Restart — stop and then restart a selected agent;
-   ![Refresh](/en/docs/mt5/client/img/refresh_icon.png "Refresh") Refresh — refresh the list of installed agents;
-   ![Export](/en/docs/mt5/client/img/export_icon.png "Export") Export — export agent settings to a \*.mt5 file. These settings can be [imported](/en/docs/mt5/client/strategy_optimization#farm_impexp) to the trading platform for connection to installed agents.
-   ![Delete](/en/docs/mt5/client/img/delete_icon.png "Delete") Delete — delete the selected agent.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you close the MetaTester window, running agents are not stopped. To stop an agent, execute the appropriate command in its context menu.</span></p></td></tr></tbody></table>

### MQL5 Cloud Network [#](metatester#cloud_network)

The MQL5 Cloud Network is a special system designed to integrate remote agents into a single cloud network. Its key advantages are:

-   The possibility to provide your own agents and use third-party computing power for free or on a commercial basis.
-   No need to set up network access for agents — MetaTester and MQL5 Cloud Network automatically organize access and distribute incoming tasks among agents.
-   Convenient control of agents from the [MQL5.community](https://www.mql5.com) user profile.

![MQL5 Cloud Network](/en/docs/mt5/client/img/metatester_cloud_network.png "MQL5 Cloud Network")

The tab contains an option for managing use in the distributed computing MQL5 Cloud Network: Sell computing resources via an MQL5.community account.

By enabling this option, a user consents to allow use of his or her remote agents via the MQL5 Cloud Network. Each agent service will be available in the network in accordance with a preset [scale](/en/docs/mt5/client/metatester#scheduler).

When connected to the MQL5 Cloud Network, the agent is still available for normal remote connections using [IP address and password](/en/docs/mt5/client/metatester#services).

To provide the computing power of agents as a paid service, specify your [MQL5.community](https://www.mql5.com) account in the appropriate field. Fees for the use of your agents are transferred to the specified account via the internal MQL5.community payment system.

If you do not have an account, you may create one by clicking "Register a new MQL5.community account..."

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Be careful when indicating your valid account, otherwise, in case of an error, the agent services will be provided to other users for free.</span></li><li class="p_tableatten"><span class="f_tableatten">You can monitor the availability of your agents in the network and manage them on the "Agents" tab of your MQL5.community profile.</span></li></ul></td></tr></tbody></table>

### Scheduler [#](metatester#scheduler)

![Scheduler](/en/docs/mt5/client/img/metatester_scheduler.png "Scheduler")

On this tab you can set a schedule for managing the availability of your remote agents in the [MQL5 Cloud Network](/en/docs/mt5/client/metatester#cloud_network).

The hours when the agents are available are colored blue, the unavailable hours are light-colored. To switch between working and non-working hours click on the appropriate square. To mark all hours of a certain day, click on the asterisk at the end of a row.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">This schedule does not influence the availability of agents for a normal remote connection using <a href="/en/docs/mt5/client/metatester#services" class="topiclink">IP address and password</a>.</span></p></td></tr></tbody></table>

## Console Commands [#](metatester#console)

To work with agents through the command line, use the console commands of the metatester.exe file:

-   /install /address:address:port /password:password — install an agent at the specified IP address and port with the specified password. For example, metatester.exe /install /address:192.168.0.1:1950 /password:gj1sfj;
-   /uninstall /address:address:port — delete the agent installed at the specified IP address and port;
-   /start /address:address:port — start the service of the agent installed at the specified IP address and port;
-   /stop /address:address:port — stop the service of the agent installed at the specified IP address and port;
-   /restart /address:address:port — restart the service of the agent installed at the specified IP address and port;
-   /help — open help of the console commands.

To delete an agent using the command line, you can also execute the following commands:

-   sc stop "agent name" (this action is required if the agent is running);
-   sc delete "agent name"

For example, to delete the already stopped agent "MetaTester-1", you should execute the following command:

sc delete "MetaTester-1".

[Real and Generated Ticks](/en/docs/mt5/client/tick_generation)

[Global Variables](/en/docs/mt5/client/service_global)