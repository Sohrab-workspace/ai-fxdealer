# How to Participate

> Source: https://support.metaquotes.net/en/docs/mt5/client/mql5cloud_install

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
            -   [How to Use](/en/docs/mt5/client/mql5cloud_use)
            -   [How to Participate](/en/docs/mt5/client/mql5cloud_install)
            -   [Price Calculation](/en/docs/mt5/client/mql5cloud_calculation)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)How to Participate

# How to Participate

By participating in the MQL5 Cloud Network you can earn providing the processing power of your computer. Install testing agents using a manager and specify your [MQL5.community](/en/docs/mt5/client/settings#community) account, to which the payment will be transferred. Agents automatically receive computation tasks, no further user action is required. You can control the amount of work done and payments in your MQL5.community profile.

## How to Install the Agent Manager [#](mql5cloud_install#install)

To join the MQL5 Cloud Network, you do not need to install the entire trading platform. [Download](https://download.terminal.free/cdn/web/metaquotes.software.corp/mt5/mt5tester.setup.exe) the special installer that lets you quickly and easily install the [MetaTester](/en/docs/mt5/client/metatester) application for managing remote agents on a computer.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To connect your agents to the MQL5 Cloud Network, the computer where the agents are installed must have at least 2048MB of RAM. Agents can be installed in 64 bit systems only.</span></p></td></tr></tbody></table>

![Installation of the agent manager](/en/docs/mt5/client/img/mql5cloud_install.gif "Installation of the agent manager")

The installation is a multi-step process:

-   Read the welcome message.
-   Read the license agreement. If you agree with the terms of the agreement, select "I accept the agreement terms" and click "Next." If you do not agree with the agreement, you should exit the installation program.
-   Specify the folder in which you want to install the application, and the folder to create the shortcuts in the Start menu. If you check the option "Don't create a Start Menu folder", program shortcuts will not be created.
-   Complete the installation. You can directly move to [agents setup](/en/docs/mt5/client/mql5cloud_install#setup) and open the [MQL5 Cloud Network](https://cloud.mql5.com/en "MQL5 Cloud Network") website.

## How to Install and Configure Agents [#](mql5cloud_install#setup)

To start providing your computing power in the MQL5 Cloud Network, [install](/en/docs/mt5/client/mql5cloud_install) and run the [MetaTester](/en/docs/mt5/client/metatester).

![Overview](/en/docs/mt5/client/img/metatester_overview.png "Overview")

To install agents, click the "Add" button on tab "Services". The MetaTrader 5 Agents Manager automatically determines the number of logical cores and installs the appropriate number of testing agents. By default, single password "MetaTester" is set for all agents. All agents are available in the local network at the same IP address, but each is assigned a separate port. If necessary, you can specify different port numbers or a password. These settings do not influence the use of the agents in the MQL5 Cloud Network.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To participate in MQL5 Cloud Network, the number of agents should not exceed the number of logical processor cores.</span></li><li class="p_tableatten"><span class="f_tableatten">To connect your agents to the MQL5 Cloud Network, the computer where the agents are installed must have at least 2048MB of RAM.</span></li><li class="p_tableatten"><span class="f_tableatten">If you access the Internet via a proxy server, specify its settings in the <a href="/en/docs/mt5/client/settings#proxy" class="topiclink">trading platform</a> or in Internet Explorer.</span></li></ul></td></tr></tbody></table>

![Services](/en/docs/mt5/client/img/metatester_services.png "Services")

On the "MQL5 Cloud Network" tab, check the box "Sell computing resources through a MQL5.community account", so that agents are available to all users of our network of distributed computing. To sell the processing resources of your agents to other users, you need to indicate a valid account at [MQL5.community](https://www.mql5.com/ "MQL5.community"). Payments for the used resources will be transfered to this account.

![MQL5 Cloud Network](/en/docs/mt5/client/img/metatester_cloud_network.png "MQL5 Cloud Network")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the MQL5.community account is invalid or not specified at all, the computational power of agents will be provided for free.</span></p></td></tr></tbody></table>

The last setting on the "Scheduler" tab allows you to set a schedule, specifying the time when your agents will be available on the MQL5 Cloud Network. For example, you can disable execution of tasks during working hours, if you need the computer power at this time.

![Scheduler](/en/docs/mt5/client/img/metatester_scheduler.png "Scheduler")

Configuration of agents is over. Now you can close the window of the MetaTrader 5 Agents Manager. Your agents run as services and do not require your attention. If necessary, you can anytime change their settings by running the MetaTrader 5 Strategy Tester from the Start menu or the desktop shortcut.

## Managing Agents on MQL5.community [#](mql5cloud_install#manage)

You can also manage your agents from your profile on the [MQL5.community](https://www.mql5.com/ "MQL5.community"). All the required information is available in the "Agents" section: computer configuration, IP address, rating, number of completed tasks and the amount of earnings.

![Managing agents through the MQL5.community profile](/en/docs/mt5/client/img/cloud_agents.png "Managing agents through the MQL5.community profile")

## Restrictions of Participation on MQL5 Cloud Network [#](mql5cloud_install#limits)

There are several limitations of participation on MQL5 Cloud Network:

-   An agent should have at least 768 MB of available physical memory to perform calculations.
-   To connect your agents to the MQL5 Cloud Network, the computer where the agents are installed must have at least 2048MB of RAM.
-   The agent's [productivity index (PR)](/en/docs/mt5/client/mql5cloud_calculation) should not be less than 50.
-   Agents installed on a virtual machine cannot participate in MQL5 Cloud Network.
-   Agents having [PR](/en/docs/mt5/client/mql5cloud_calculation) below 100 are not used in [genetic optimization](/en/docs/mt5/client/optimization_types) in order not to slow down the calculation process. The reason is that the calculation is performed by generations (256 passes). While one generation is not calculated, calculation of the next one cannot start. Even if a single pass out of 256 ones is calculated by a low PR agent, the total calculation speed is reduced.
-   An agent will not be able to receive new tasks from the MQL5 Cloud Network if the free disk space on the computer where the agent is installed falls below 500MB.
-   Agents do not receive tasks from the cloud network in case the PC they are installed at is powered by a battery (it refers to laptops).

## Command Line Configuration of Agents [#](mql5cloud_install#console)

MetaTester can be launched from the command line.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The command line does not allow to adjust the parameters of the agents connection to MQL5 Cloud Network including such parameter as MQL5.community account, to which the funds for the agents submission will be transferred. Such a possibility has not been provided to ensure safe operation with the computing network.</span></p><p class="p_tableatten"><span class="f_tableatten">Therefore, parameters of the agent participation on MQL5 Cloud Network should be additionally <a href="/en/docs/mt5/client/mql5cloud_install#setup" class="topiclink">configured</a> after their installation. To do this, run MetaTester, check the appropriate options and specify your account.</span></p></td></tr></tbody></table>

The following keys can be used for working with the agents in the command line mode:

-   /install /address:address:port /password:password — install the tester agent on a specified IP address and a port with a specified password. Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/install</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">address:</span><span class="f_CodeExample" style="color: #008000;">192.168.0.1</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #008000;">2000</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/password:akq1skdj</span></p></td></tr></tbody></table>

-   /uninstall /address:address:port — delete the tester agent that has been previously installed on a specified IP address and a port. Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/uninstall</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">address:</span><span class="f_CodeExample" style="color: #008000;">192.168.0.1</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #008000;">2000</span></p></td></tr></tbody></table>

-   /start /address:address:port — launch the agent that has been previously installed on a specified IP address and a port.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/start</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">address:</span><span class="f_CodeExample" style="color: #008000;">192.168.0.1</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #008000;">2000</span></p></td></tr></tbody></table>

-   /stop /address:address:port — stop the agent running at a specified IP address and a port.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/stop</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">address:</span><span class="f_CodeExample" style="color: #008000;">192.168.0.1</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #008000;">2000</span></p></td></tr></tbody></table>

-   /restart /address:address:port — restart the agent running at a specified IP address and a port.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/restart</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">address:</span><span class="f_CodeExample" style="color: #008000;">192.168.0.1</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #008000;">2000</span></p></td></tr></tbody></table>

-   /shutdown — stop all running agents.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/shutdwon</span></p></td></tr></tbody></table>

-   /autouninstall — remove all previously installed agents.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/autouninstall</span></p></td></tr></tbody></table>

-   /help or /? — call the help on command line launch.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">c:\&gt;metatester.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/?</span></p></td></tr></tbody></table>

[How to Use](/en/docs/mt5/client/mql5cloud_use)

[Price Calculation](/en/docs/mt5/client/mql5cloud_calculation)