# How to Use

> Source: https://support.metaquotes.net/en/docs/mt5/client/mql5cloud_use

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)How to Use

# How to Use

[The MQL5 Cloud Network](https://cloud.mql5.com/en "Official site of the MQL5 Cloud Network") allows you to quickly optimize your Expert Advisors using the power of thousands of computers. The network combines remote agents and distributes optimization tasks among them. The Strategy Tester connects to the cloud network through multiple access points, which are distributed on a territorial basis (e.g., MQL5 Cloud Europe).

## Features of the MQL5 Cloud Network [#](mql5cloud_use#cloud_features)

-   The entire power of the MQL5 Cloud Network is used only for [complete slow optimization](/en/docs/mt5/client/optimization_types).
-   During [genetic optimization](/en/docs/mt5/client/optimization_types), only agents of one access point are used. It is connected with the specific features of the genetic algorithm.
-   The genetic optimization mode is automatically enabled when the total number of optimization steps exceeds 100 million.
-   MQL5 Cloud Network can be used in 64 bit systems only.
-   In addition to using the MQL5 Cloud Network, you can provide your CPU computing power in the network. To install the remote agents and include them into the network, use a special utility [MetaTester](/en/docs/mt5/client/metatester).
-   Read more about the MQL5 Cloud Network on [the official site](https://cloud.mql5.com/en "MQL5 Cloud Network").

## Payments for the Use of the MQL5 Cloud Network [#](mql5cloud_use#cloud_pay)

Using agents of the MQL5 Cloud Network is paid. The formula for calculating the cost is described in [a separate section](/en/docs/mt5/client/mql5cloud_calculation). The current MQL5.community account balance is displayed above the list of cloud agents. To use MQL5 Cloud Network a user need to have at least 1 US dollar on the MQL5.community account.

It is not possible to calculate the final cost of testing/optimization through the MQL5 Cloud Network.

There is no physical possibility to calculate the time and CPU resources required to conduct a test. The system cannot know which calculations your program uses. The exact amount of resources consumed by the testing or optimization process can only be evaluated after process completion. Also, please note that computational tasks are submitted into the network in batches (hundreds or thousands of tasks in a batch), and not one at a time.

Therefore, even when the system detects that your budget has been totally spent, it can still have calculations running on a number of tasks. The tasks cannot be stopped in the middle and thus the system has to complete them. Once the calculation is complete, the system will deduct the final cost from your balance.

All the details about your tasks performed using the Cloud Network are available on the [Agents \\ Tasks](/en/docs/mt5/client/mql5cloud_use#report) page of your profile.

## Enabling MQL5 Cloud Network [#](mql5cloud_use#cloud_enable)

To use the network agents, enable them using command "![Enable](/en/docs/mt5/client/img/enable_agent_icon.png "Enable") Enable" in the context menu of the Agents tab of your Strategy Tester. Since the MQL5 Cloud Network is a paid service, a user must have an account at the [MQL5.community](https://www.mql5.com/ "MQL5.community") website, through which all the accounting operations are performed. Account details are specified on the [MQL5.community](/en/docs/mt5/client/settings#community) tab of the platform settings.

If you do not specify the details of your MQL5.community account before enabling the MQL5 Cloud Network agents, you will be offered to do this.

![Enabling MQL5 Cloud Network](/en/docs/mt5/client/img/tester_cloud_enable.png "Enabling MQL5 Cloud Network")

If you have not registered on the website, use the [new account creation](https://www.mql5.com/en/auth_register) link.

## Starting Calculations Using the MQL5 Cloud Network [#](mql5cloud_use#cloud_start)

Like with a conventional optimization, you need to set all the testing options and Expert Advisor input parameters. On the Agents tab, you can monitor how the Strategy Tester distributes tasks to available agents. The number of available and currently used agents is displayed for each access point.

![Running distributed computing using the MQL5 Cloud Network Agents](/en/docs/mt5/client/img/cloud_start.png "Running distributed computing using the MQL5 Cloud Network Agents")

Traders may need to run hundreds of thousands of optimization passes in a reasonable time. With the multi-threaded Strategy Tester and the MQL5 Cloud Network, in one hour you can complete the calculations that would require a few days without the network. The computing power of thousands of cores is available straight on the trading platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">There are limitations for each optimization pass. During optimization, the Expert Advisor cannot write more than 4GB of information to disk and use more than 4GB of RAM. If the limit is exceeded, the network agent will not be able to complete the calculation correctly, and you will not receive the result. However, you will be charged for all the time spent on the calculations.</span></p></td></tr></tbody></table>

## Task Execution Reports [#](mql5cloud_use#report)

The details of the calculations performed using the MQL5 Cloud Network are available in your MQL5.community profile.

![Task execution reports](/en/docs/mt5/client/img/cloud_tasks.png "Task execution reports")

The report displays information about the tested Expert Advisors, the number of test runs and the amount of money spent.

[MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)

[How to Participate](/en/docs/mt5/client/mql5cloud_install)