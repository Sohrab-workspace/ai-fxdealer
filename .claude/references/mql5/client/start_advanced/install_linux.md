# How to Install the Platform on Linux

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/install_linux

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Installation on Linux

# How to Install the Platform on Linux

The platform runs on Linux using [Wine](https://www.winehq.org/). Wine is a free compatibility layer that allows application software developed for Microsoft Windows to run on Unix-like operating systems.

We have prepared a special script to make the installation process as simple as possible. The script will automatically detect your system version, it supports Ubuntu, Debian, Linux Mint and Fedora distributions. Based on it, it will download and install the appropriate Wine package. After that, it will download and run the platform installer.

To start the installation, open the command line (Terminal) without the administrator privileges (no sudo) and specify the relevant command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">wget&nbsp;https://download.terminal.free/cdn/web/metaquotes.software.corp/mt5/mt5linux.sh&nbsp;;&nbsp;chmod&nbsp;+x&nbsp;mt5linux.sh&nbsp;;&nbsp;./mt5linux.sh</span></p></td></tr></tbody></table>

This command downloads the script, makes it executable and runs it. You only need to enter your account password to allow installation.

![Installing Wine and the platform with a single command](/en/docs/mt5/client/img/linux_command_line.png "Installing Wine and the platform with a single command")

If you are prompted to install additional Wine packages (Mono, Gecko), please agree, as these packages are required for platform operation. The MetaTrader 5 installer will launch after that, proceed with the standard steps. Once the installation is complete, restart your operating system, and the platform is ready to go.

![The platform is ready to run on Linux](/en/docs/mt5/client/img/linux_terminal.png "The platform is ready to run on Linux")

## Install updates in a timely manner

It is highly recommended to always use the latest versions of the operating system and Wine. Timely updates increase platform operation stability and improve performance.

To update Wine, open a command prompt and type the following command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">sudo&nbsp;apt&nbsp;update&nbsp;;&nbsp;sudo&nbsp;apt&nbsp;upgrade</span></p></td></tr></tbody></table>

For further information, please visit the [official Wine website](https://wiki.winehq.org/Download).

## Platform Data Directory

Wine creates a separate virtual logical drive with the necessary environment for every installed program. The default path of the installed platform data folder is as follows:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Home&nbsp;directory\.mt5\drive_c\Program&nbsp;Files\MetaTrader&nbsp;5</span></p></td></tr></tbody></table>

Use the platform on Linux: install with a single command and enjoy all the platform features.

[Installation on Mac OS](/en/docs/mt5/client/start_advanced/install_mac)

[Platform Start](/en/docs/mt5/client/start_advanced/start)