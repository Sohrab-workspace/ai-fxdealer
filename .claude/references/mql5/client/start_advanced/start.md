# How to Start the Trading Platform

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/start

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Platform Start

# How to Start the Trading Platform

After installation, a group of programs of the trading platform is added to the Start menu, and the program shortcut is created on the desktop. Use them to run the platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Two copies of the platform cannot run from the same directory. If you need to run multiple copies at the same time, install the appropriate number of programs in different directories.</span></p></td></tr></tbody></table>

There are two main modes of trading platform start, as well as some [additional](/en/docs/mt5/client/start_advanced/start#command_line) methods.

## Main Mode [#](start#guest)

Starting from MS Windows Vista, applications installed to Program Files are not allowed to store their data in the installation folder on default. All data should be stored in a separate Windows user directory.

Thus, if the platform is installed in the Program Files directory and user rights to write to that directory are limited, it is run in the main mode. The main mode is also used in the following situations:

-   If the UAC (User Activity Control) system is enabled.
-   If remote connection to a computer is used (RDP, Remote Desktop Protocol).

In this mode, the editable files of the platform are stored in a specific Windows user directory, and the immutable files are stored in Program Files. Immutable files include executables of the platform, of MetaEditor, standard sounds, etc. Editable files are:

-   all platform settings, configuration files;
-   all the databases (price history);
-   platform and expert [journals](/en/docs/mt5/client/start_advanced/journal);
-   all profiles.

All the editable files of the platform are stored in the following directories (depending on the operating system used):

Microsoft Windows XP SP3:

-   C:\\Documents and Settings\\username\\Application Data\\MetaQuotes\\Terminal\\instance\_id\\

Microsoft Windows Vista and higher:

-   C:\\Users\\username\\AppData\\Roaming\\MetaQuotes\\Terminal\\instance\_id\\

Here 'C' is the logical drive letter on which Windows is installed, "username" is the account name in the operating system under which the platform has been installed, "instance\_id" is a unique identifier generated based on the path to the directory where the platform is installed.

For quick access to these folders, use the command "![Open data folder](/en/docs/mt5/client/img/terminal_data_icon.png "Open data folder") Open Data Folder" in the [File](/en/docs/mt5/client/interface) menu. Each data folder contains a special text file origin.txt. This file contains the path to the platform installation folder, which corresponds to this data directory.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">In the main mode, the catalog where editable files are stored is different for each Windows account.</span></li><li class="p_tableatten"><span class="f_tableatten">A detailed description of the platform file structure and their purpose is given in the <a href="/en/docs/mt5/client/start_advanced/structure" class="topiclink">appropriate section</a>.</span></li></ul></td></tr></tbody></table>

## Portable Mode

When installed to Program Files, the platform works in the main mode described above on default. All the platform data are stored in a special Windows user directory. However you can force the platform to store its data in the installation folder. To do it, run the platform in the portable mode. To use this mode, start the platform from the command line with the additional [/portable](/en/docs/mt5/client/start_advanced/start#portable) key. For example, "C:\\Program Files\\MyTerminal\\terminal.exe /portable".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To run the platform in the Portable mode, the following conditions must be met:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">If the platform is installed in the Program Files folder, the user must have administrator rights on the computer. In addition, UAC (User Account Control) must be disabled in the operating system.</span></li><li class="p_tableatten"><span class="f_tableatten">If the platform is installed in any other folder, the user must have permission to write data to that folder.</span></li></ul></td></tr></tbody></table>

## Running from the Command Line [#](start#command_line)

The trading platform can be run manually with predefined parameters. This can be done by using different keys for starting from a command line and alternative [configuration files](/en/docs/mt5/client/start_advanced/start#configuration_file).

The platform can be run with the keys from the command line. Specify there a path to the executable platform file (path to the file\\terminal.exe) and after a space add one or several of the below keys:

-   /login:login number — running a platform under a certain [account](/en/docs/mt5/client/acc_open). For example, terminal.exe / login:100000.
-   /config:path to a configuration file — running a platform with an alternative configuration file. For example, terminal.exe /config:c:\\myconfiguration.ini. The default configuration file is [common.ini](/en/docs/mt5/client/start_advanced/structure#common).
-   /profile:profile name — running the platform with a definite [profile](/en/docs/mt5/client/charts_advanced/templates_profiles#profiles). The profile must be pre-created and located in the [/profiles/charts/](/en/docs/mt5/client/start_advanced/structure#profiles) of the platform. For example, terminal.exe /profile:Euro.
-   /portable — set the platform to run in the [Portable mode](/en/docs/mt5/client/start_advanced/start). Running in this mode may be needed if the platform was earlier launched in the [main mode](/en/docs/mt5/client/start_advanced/start#guest). To run the platform in the portable mode, the operating system user requires appropriate permissions.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the key assignment is set incorrectly (invalid login, profile name or configuration file), the default value will be used.</span></p></td></tr></tbody></table>

## Running with a Custom Configuration File [#](start#configuration_file)

The trading platform can be run with a custom set of parameters. Create your own configuration file based on the default [common.ini](/en/docs/mt5/client/start_advanced/structure#common). To start the platform with a custom configuration file, run the following command in the [command line](/en/docs/mt5/client/start_advanced/start#command_line):

path\_to\_platform\\terminal64.exe /config:c:\\myconfiguration.ini

where "c:\\myconfiguration.ini" is the path to the custom configuration file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Custom configuration files are used in the "read only" mode during the work of the platform. Changes in settings made from the platform interface are not written to the used custom configuration file.</span></p></td></tr></tbody></table>

The configuration file parameters are divided into several blocks and correspond to the settings on [platform configuration](/en/docs/mt5/client/settings) window tabs. Below are the most important settings in the configuration file:

### \[Common\]

Common platform settings similar to the [Server](/en/docs/mt5/client/settings#server) tab:

-   Login — account number. The platform tries to read additional authorization information from a configuration file (server, password and certificate password specified in the parameters described below). If the authorization information for the account is not specified, the platform tries to read it from its own account database;
-   Server — address and port number of a trade server separated with a colon;
-   Password — password for connecting to the account specified in the Login parameter;
-   CertPassword — certificate password. This parameter is required if the [extended authentication](/en/docs/mt5/client/start_advanced/extended_authorization) mode is enabled for the account. If the used certificate is not installed in the operating system storage, its file should be placed in platform\_folder/config/certificates/;
-   ProxyEnable — allow (1) or prohibit (0) connection through a proxy server;
-   ProxyType — type of a proxy server: 0 (SOCKS4), 1 (SOCKS5), 2 (HTTP);
-   ProxyAddress — IP address and port of the proxy server separated by a colon;
-   ProxyLogin — login for authorizing on a proxy server;
-   ProxyPassword — password for authorizing on a proxy server;
-   KeepPrivate — saving the password between connections: 1 — to save, 0 — not to save.
-   NewsEnable — enable (1) or disable (0) news letters;
-   CertInstall —  install (1) or do not install (0) new certificates in the system storage (for [extended authentication](/en/docs/mt5/client/start_advanced/extended_authorization)).
-   MQL5Login — account on [MQL5.community](https://www.mql5.com/ "MQL5.community").
-   MQL5Password — password for the specified account on [MQL5.community](https://www.mql5.com/ "MQL5.community").

### \[Charts\]

[Chart](/en/docs/mt5/client/settings#charts) settings:

-   ProfileLast —  the name of the current [profile](/en/docs/mt5/client/charts_advanced/templates_profiles#profiles);
-   MaxBars — the maximum number of bars in a chart;
-   PrintColor — chart print mode: 1 — color printing, 0 — black-and-white printing;
-   SaveDeleted — save (1) or not (0) [deleted chart](/en/docs/mt5/client/charts_advanced/charts_deleted) to reopen later.

### \[Experts\]

[Expert Advisor](/en/docs/mt5/client/settings#ea) settings:

-   AllowLiveTrading — enable (1) or disable (0) automated trading using [Expert Advisors](/en/docs/mt5/client/trade_robots_indicators).
-   AllowDllImport — DLL import allowed (1) or not (0);
-   Enabled — enable or disable use of Expert Advisors;
-   Account — disable (1) or not (0) Expert Advisors when connecting with a different [account](/en/docs/mt5/client/acc_open);
-   Profile — disable (1) or not (0) Expert Advisors after change after change of the active [profile](/en/docs/mt5/client/charts_advanced/templates_profiles#profiles).

### \[Objects\]

[Object](/en/docs/mt5/client/settings#charts) settings:

-   ShowPropertiesOnCreate — show (1) or do not show (0) properties of objects being created;
-   SelectOneClick — select (1) or not (0) objects at a single mouse click;
-   MagnetSens — docking sensitivity of objects;

### \[Email\]

[Email](/en/docs/mt5/client/settings#mail) settings:

-   Enable — enable (1) or disable (0) use of email;
-   Server — address of the SMTP server;
-   Auth — encrypted information for authentication on the mail server;
-   Login — login for the SMTP server;
-   Password — password for the SMTP server;
-   From — sender's name and address;
-   To — recipient's name and address.

### \[StartUp\]

Settings of [Expert Advisors](/en/docs/mt5/client/settings#ea) and [scripts](/en/docs/mt5/client/autotrading#type), that open automatically when you start the platform:

-   Expert — file name of the [Expert Advisor](/en/docs/mt5/client/trade_robots_indicators) that opens automatically when you start the platform. The Expert Advisor runs on the chart that opens in accordance with the Symbol and Period parameters. If the Symbol parameter is not set, no additional chart will be opened in the platform. The Expert Advisor will run on the first chart of the current [profile](/en/docs/mt5/client/charts_advanced/templates_profiles#profiles) in this case. If the current profile has no charts, the Expert Advisor will not be started. If the Expert parameter is not set, no Expert Advisors will be started.
-   Symbol — the symbol of the [chart](/en/docs/mt5/client/charts) that opens straight after the platform start. An Expert Advisor or a script will be added to this chart. No information about this additional chart will be saved as the platform is closed. During the next start of the platform without the configuration file, this chart will not be opened. If this parameter is not set, no additional chart will be opened.
-   Period — the [timeframe](/en/docs/mt5/client/charts#operations) of the chart, to which an Expert Advisor or a script will be added (any of the 21 periods available in the platform). If the parameter is not set, default H1 is used.
-   Template — the name of the [template](/en/docs/mt5/client/charts_advanced/templates_profiles) to be applied to the chart.
-   ExpertParameters — the name of the file that contains Expert Advisor [parameters](/en/docs/mt5/client/trade_robots_indicators#run). The file must be located in the folder MQL5\\presets of the [platform data directory](/en/docs/mt5/client/start_advanced/structure). If this parameter is not set, default settings will be used.
-   Script — the name of the [script](/en/docs/mt5/client/autotrading#type) that opens automatically when you start the platform. Scripts are run by the same rules as Expert Advisor.
-   ScriptParameters — the name of the file that contains script [parameters](/en/docs/mt5/client/trade_robots_indicators#run). The file must be located in the folder MQL5\\presets of the [platform data directory](/en/docs/mt5/client/start_advanced/structure). If this parameter is not set, default settings will be used.

-   ShutdownTerminal — enable/disable trading platform shutdown upon completion of script operation (0 — disable, 1 — enable). If this parameter is not set, the value "0" is used (shutdown disabled). The parameter is used for scripts only, other program types are not supported.

### \[Tester\]

Parameters of [testing](/en/docs/mt5/client/testing) that starts automatically when you run the platform:

-   Expert — the file name of the Expert Advisor that will automatically run in the testing (optimization) mode. If this parameter is not present, testing will not run.
-   ExpertParameters — the name of the file that contains Expert Advisor [parameters](/en/docs/mt5/client/trade_robots_indicators#run). This file must be located in the MQL5\\Profiles\\Tester folder of the platform installation directory.
-   Symbol — the name of the symbol that will be used as the [main testing symbol](/en/docs/mt5/client/testing#settings). If this parameter is not added, the last selected symbol in the tester is used.
-   Period — testing chart period (any of the 21 periods available in the platform). If the parameter is not set, default H1 is used.
-   Login — this parameter communicates to the Expert Advisor the value of an account, on which testing is allegedly performed. The need for this parameter is set in the source [MQL5 code](/en/docs/mt5/client/autotrading#mql5) of the Expert Advisor (in the AccountInfoInteger function).
-   Model — [tick generation mode](/en/docs/mt5/client/testing#settings) (0 — "Every tick", 1 — "1 minute OHLC", 2 — "Open price only", 3 — "Math calculations", 4 — "Every tick based on real ticks"). If this parameter is not specified, Every Tick mode is used.
-   ExecutionMode — trading mode emulated by the strategy tester (0 — normal, -1 — with a random delay in the execution of trading orders, >0 — trade execution delay in milliseconds, it cannot exceed 600 000).
-   Optimization — enable/disable [optimization](/en/docs/mt5/client/strategy_optimization), its type (0 — optimization disabled, 1 — "Slow complete algorithm", 2 — "Fast genetic based algorithm", 3 — "All symbols selected in Market Watch").
-   OptimizationCriterion — [optimization criterion](/en/docs/mt5/client/optimization_types#criterion): (0 — the maximum balance value, 1 — the maximum value of product of the balance and profitability, 2 — the product of the balance and expected payoff, 3 — the maximum value of the expression (100% - Drawdown)\*Balance, 4 — the product of the balance and the recovery factor, 5 — the product of the balance and the Sharpe Ratio, 6 — a custom optimization criterion received from the OnTester() function in the Expert Advisor), 7 — the maximum of complex criterion.
-   FromDate — starting date of the [testing range](/en/docs/mt5/client/testing#settings) in format YYYY.MM.DD. If this parameter is not set, the date from the corresponding field of the strategy tester will be used.
-   ToDate — end date of the [testing range](/en/docs/mt5/client/testing#settings) in format YYYY.MM.DD. If this parameter is not set, the date from the corresponding field of the strategy tester will be used.
-   ForwardMode — [forward testing](/en/docs/mt5/client/testing#forward) mode (0 — off, 1 — 1/2 of the testing period, 2 — 1/3 of the testing period, 3 — 1/4 of the testing period, 4 — custom interval specified using the ForwardDate parameter).
-   ForwardDate — starting date of forward testing in the format YYYY.MM.DD. The parameter is valid only if ForwardMode=4.
-   Report — the name of the file to save the report on [testing](/en/docs/mt5/client/testing#result) or [optimization](/en/docs/mt5/client/strategy_optimization#result) results. The file is created in the trading platform directory. You can specify a path to save the file, relative to this directory, for example, \\reports\\tester.htm. The subdirectory where the report is saved should exist. If no extension is specified in the file name, the ".htm" extension is automatically used for testing reports, and ".xml" is used for optimization reports. If this parameter is not set, the testing report will not be saved as a file. If forward testing is enabled, its results will be saved in a separate file with the ".forward" suffix. For example, tester.forward.htm.
-   ReplaceReport — enable/disable overwriting of the report file (0 — disable, 1 — enable). If overwriting is forbidden and a file with the same name already exists, a number in square brackets will be added to the file name. For example, tester\[1\].htm. If this parameter is not set, default 0 is used (overwriting is not allowed).
-   ShutdownTerminal — enable/disable platform shutdown after completion of testing (0 — disable, 1 — enable). If this parameter is not set, the "0" value is used (shutdown disabled). If the testing/optimization process is manually stopped by a user, the value of this parameter is automatically reset to 0.
-   Deposit — initial deposit for testing optimization. The amount is specified in the account deposit currency. If the parameter is not specified, a value from the appropriate field of the [strategy tester](/en/docs/mt5/client/testing#settings) is used.
-   Currency — deposit currency for testing/optimization purposes. Specified as a three-letter name, e.g. EUR, USD, CHF etc. Please note that cross rates for converting profit and margin to the specified deposit currency must be available on the account, to ensure proper testing. If the parameter is not specified, a value from the appropriate field of the [strategy tester](/en/docs/mt5/client/testing#settings) is used.
-   Leverage — leverage for testing/optimization. For example, 1:100. If the parameter is not specified, a leverage from the appropriate field of the [strategy tester](/en/docs/mt5/client/testing#settings) is used.
-   UseLocal — enable/disable the use of [local agents](/en/docs/mt5/client/strategy_optimization#agents) for testing and optimization (0 — disable, 1 — enable). If the parameter is not specified, current platform settings are used.
-   UseRemote — enable/disable use of [remote agents](/en/docs/mt5/client/strategy_optimization#farm) for testing and optimization (0 — disable, 1 — enable). If the parameter is not specified, current platform settings are used.
-   UseCloud — enable/disable use of agents from the [MQL5 Cloud Network](/en/docs/mt5/client/strategy_optimization#cloud) (0 — disable, 1 — enable). If the parameter is not specified, current platform settings are used.
-   Visual — enable (1) or disable (0) the visual test mode. If the parameter is not specified, the current setting is used.
-   Port — the port, on which the [local testing agent](/en/docs/mt5/client/strategy_optimization#agents) is running. The port should be specified for the parallel start of testing on different agents. For example, you can run parallel tests of the same Expert Advisor with different parameters. During a single test port can be omitted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/client/testing#inputs" class="topiclink">Input parameters</a> from the file specified in ExpertParameters are used for testing/optimization.</span></li><li class="p_tableatten"><span class="f_tableatten">If the ExpertParameters setup is not available, <a href="/en/docs/mt5/client/testing#inputs" class="topiclink">parameters</a> from the file Expert_name.set located in [platform_folder]\MQL5\Profiles\Tester are used. The last specified set of input parameters of an Expert Advisor is automatically saved in this file.</span></li><li class="p_tableatten"><span class="f_tableatten">If there is no such file, then the default parameters specified in the Expert Advisor code are used for testing. Optimization is not possible.</span></li><li class="p_tableatten"><span class="f_tableatten">To create or edit the set of parameters, select the Expert Advisor on the <a href="/en/docs/mt5/client/testing#settings" class="topiclink">Settings</a> tab of the strategy tester, and specify input parameters and their modification range on the <a href="/en/docs/mt5/client/testing#inputs" class="topiclink">corresponding tab</a>.</span></li></ul></td></tr></tbody></table>

### Example of a Configuration File

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">[Common]</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Login=1000575</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ProxyEnable=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ProxyType=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ProxyAddress=192.168.0.1:3128</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ProxyLogin=10</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ProxyPassword=10</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">KeepPrivate=1</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">NewsEnable=1</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">CertInstall=1</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">[Charts]</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ProfileLast=Euro</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">MaxBars=50000</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">PrintColor=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">SaveDeleted=1</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">[Experts]</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">AllowLiveTrading=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">AllowDllImport=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Enabled=1</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Account=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Profile=0</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">[Objects]</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ShowPropertiesOnCreate=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">SelectOneClick=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">MagnetSens=10</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;+------------------------------------------------------------------------------+</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;| &nbsp;Running an EA and/or script on the specified chart at the platform start&nbsp; &nbsp; |</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;+------------------------------------------------------------------------------+</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">[StartUp]</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The Expert Advisor is located in platform_data_directory\MQL5\Experts\Examples\MACD\</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Expert=Examples\MACD\MACD Sample</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- EA start parameters are available in platform_data_directory\MQL5\Presets\</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ExpertParameters=MACD Sample.set</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The script is located in platform_data_directory\MQL5\Scripts\Examples\ObjectSphere\</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Script=Examples\ObjectSphere\SphereSample</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Symbol chart, which will be opened when you start the platform, and EA and/or script will run on it</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Symbol=EURUSD</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Chart timeframe, which will be opened when you start the platform, and EA and/or script will run on it</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Period=M1</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The template to apply to a chart is located in platform_installation_directory\Profiles\Templates</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Template=macd.tpl</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Set automatic platform shutdown upon completion of script operation</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ShutdownTerminal=1</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;+------------------------------------------------------------------------------+</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;| Start Expert Advisor testing or optimization &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;+------------------------------------------------------------------------------+</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">[Tester]</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The Expert Advisor is located in platform_data_directory\MQL5\Experts\Examples\MACD\</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Expert=Examples\MACD\MACD Sample</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The Expert Advisor parameters are available in platform_installatoin_directory\MQL5\Profiles\Tester\</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ExpertParameters=macd sample.set</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The symbol for testing/optimization</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Symbol=EURUSD</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The timeframe for testing/optimization</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Period=M1</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Emulated account number</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Login=123456</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Initial deposit</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Deposit=10000</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Leverage for testing</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Leverage=1:100</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- The "All Ticks" mode</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Model=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Execution of trade orders with a random delay</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ExecutionMode=1</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Genetic optimization</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Optimization=2</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Optimization criterion - Maximum balance value</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">OptimizationCriterion=0</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Dates of beginning and end of the testing range</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">FromDate=2011.01.01</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ToDate=2011.04.01</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Custom mode of forward testing</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ForwardMode=4</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Start date of forward testing</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ForwardDate=2011.03.01</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- A file with a report will be saved to the folder platform_installation_directory</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">Report=test_macd</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- If the specified report already exists, it will be overwritten</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ReplaceReport=1</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">;--- Set automatic platform shutdown upon completion of testing/optimization</span></p><p class="p_fortable"><span class="f_fortable" style="font-family: 'Courier New',Courier,monospace;">ShutdownTerminal=1</span></p></td></tr></tbody></table>

[Installation on Linux](/en/docs/mt5/client/start_advanced/install_linux)

[Extended Authentication](/en/docs/mt5/client/start_advanced/extended_authorization)