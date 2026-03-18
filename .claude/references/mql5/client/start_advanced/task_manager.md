# Task manager

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/task_manager

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
            -   [User Interface](/en/docs/mt5/client/interface)
            -   [Open an Account](/en/docs/mt5/client/acc_open)
            -   [Connect to an Account](/en/docs/mt5/client/authorization)
            -   [Deposits and withdrawals](/en/docs/mt5/client/payments)
            -   [Platform Settings](/en/docs/mt5/client/settings)
            -   [For Advanced Users](/en/docs/mt5/client/start_advanced)
                -   [Platform Installation](/en/docs/mt5/client/start_advanced/installation)
                -   [Installation on Mac OS](/en/docs/mt5/client/start_advanced/install_mac)
                -   [Installation on Linux](/en/docs/mt5/client/start_advanced/install_linux)
                -   [Platform Start](/en/docs/mt5/client/start_advanced/start)
                -   [Extended Authentication](/en/docs/mt5/client/start_advanced/extended_authorization)
                -   [One Time Passwords - 2FA/TOTP](/en/docs/mt5/client/start_advanced/otp)
                -   [Files and Folders](/en/docs/mt5/client/start_advanced/structure)
                -   [Manage Trading Accounts](/en/docs/mt5/client/start_advanced/account_manage)
                -   [Mailbox](/en/docs/mt5/client/start_advanced/mail)
                -   [Security System](/en/docs/mt5/client/start_advanced/security)
                -   [Live Update](/en/docs/mt5/client/start_advanced/autoupdate)
                -   [Platform Logs](/en/docs/mt5/client/start_advanced/journal)
                -   [Task Manager](/en/docs/mt5/client/start_advanced/task_manager)
                -   [Hot Keys](/en/docs/mt5/client/start_advanced/hotkeys)
                -   [Uninstalling the Platform](/en/docs/mt5/client/start_advanced/deinstallation)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Task Manager

# Task manager

The Task Manager enables monitoring of resources consumed by the platform. You can view the amount of memory consumed by charts, CPU resources used by Expert Advisors and other performance metrics. If you platform performance slows down, you can easily detect and fix the issues.

Use the "Tools" menu or the F2 key to launch the Task Manager.

![The Task Manager monitors the resources consumed by the platform](/en/docs/mt5/client/img/task_manager.png "The Task Manager monitors the resources consumed by the platform")

Different platform functions run on separate threads. The relevant thread statistics are presented in the Task Manager:

-   Summary — general statistics for all functions.
-   GUI — resources used by the main platform thread.
-   Experts/Scripts — resources used by each of the Expert Advisors running on the chart. If a program is running in the debug or profiling mode, the line will indicate 'debug' or 'profile', respectively.
-   Services — resources consumed by each active [service](/en/docs/mt5/client/trade_robots_indicators#service).
-   Symbol — resources used for calculations related to the specified financial instrument: recalculation of prices and profits for open positions and orders, display of charts, calculation of relevant indicators, etc.
-   Worker — platform system threads. These threads are used for service purposes, background calculations and others.
-   Thread Pool — used by the system to efficiently manage the application's worker threads.
-   System — resources consumed by the system and third-party DLLs.

The following metrics are measured for platform threads:

-   CPU, % — processor load by the specified process. If the total CPU load is high, while the process load is low, the computer resources must be consumed by some third-party application.
-   Cycles — the total number of computational cycles spent by the processor to service the process, per second. The higher this metric, the more actively the processor is used.
-   Context Switches — the number of [context switches](https://en.wikipedia.org/wiki/Context_switch). High values (1000 or more) may indicate too many active threads in the system. They are trying to access the CPU time, and the system has to switch too often between them, thus wasting resources. For further details please read the [Microsoft Documentation](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc938613\(v%3dtechnet.10\)).
-   Stack — the amount of used and allocated memory stack in kilobytes.
-   Kernel Time — kernel mode operating time. An increase in this metric compared to the time spent in user mode can indicate system-level issues: drivers problems, hardware errors or slow hardware. For further details please read the [\>Microsoft Documentation](https://docs.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode).
-   User Time — user mode operating time.
-   ID — thread identifier.

The window header displays summary statistics on resource usage by the platform:

-   The number of used threads.
-   The number of handles used by the platform. A handle is a pointer, which enables a program to access the allocated resource. The more handles a program uses, the more resources it consumes.
-   The amount of RAM consumed.

The task manager data is refreshed once a second. You may use the context menu to refresh the statistics manually.

The Task Manager enables the management of running MQL5 programs. Select a program in the list and use one of the commands on the right:

-   Show — go to the selected program in the Navigator. The same action can be performed by a double click on its line.
-   Properties — open the program [input parameters](/en/docs/mt5/client/trade_robots_indicators#input).
-   Remove — remove the MQL5 program from the chart.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To save resources and to optimize the platform working area, you can disable the MQL5 services which you do not use. For example, if you are not interested in <a href="/en/docs/mt5/client/autotrading#articles" class="topiclink">MQL5 programming languages</a> or in copy trading via the <a href="/en/docs/mt5/client/signals" class="topiclink">Signals</a> service, uncheck the relevant options in the <a href="/en/docs/mt5/client/settings#community" class="topiclink">settings</a> to hide these sections.</span></p></td></tr></tbody></table>

[Platform Logs](/en/docs/mt5/client/start_advanced/journal)

[Hot Keys](/en/docs/mt5/client/start_advanced/hotkeys)