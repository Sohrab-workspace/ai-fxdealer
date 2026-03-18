# Install Terminal on Linux

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/userguide/install_linux

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
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
            -   [Install Terminal](/en/docs/mt4/terminal/userguide/installation)
            -   [Install on Mac OS](/en/docs/mt4/terminal/userguide/install_mac)
            -   [Install on Linux](/en/docs/mt4/terminal/userguide/install_linux)
            -   [Terminal Start and Data Structure](/en/docs/mt4/terminal/userguide/start_comm)
            -   [Opening of Accounts](/en/docs/mt4/terminal/userguide/open_an_account)
            -   [Authorization](/en/docs/mt4/terminal/userguide/authorization)
            -   [OTP](/en/docs/mt4/terminal/userguide/otp)
            -   [Live Update](/en/docs/mt4/terminal/userguide/liveupdate)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Getting Started](/en/docs/mt4/terminal/userguide)Install on Linux

# Install Terminal on Linux

The terminal runs on Linux using [Wine](https://www.winehq.org/). Wine is a free compatibility layer that allows application software developed for Microsoft Windows to run on Unix-like operating systems.

We have prepared a special script to make the installation process as simple as possible. The script will automatically detect your system version, based on which it will download and install the appropriate Wine package. After that, it will download and run the platform installer.

To start the installation, open the command line (Terminal) and specify the relevant command:

For Ubuntu:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">wget&nbsp;https://download.terminal.free/cdn/web/metaquotes.software.corp/mt4/mt4ubuntu.sh&nbsp;;&nbsp;chmod&nbsp;+x&nbsp;mt4ubuntu.sh&nbsp;;&nbsp;./mt4ubuntu.sh</span></p></td></tr></tbody></table>

For Debian:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">wget&nbsp;https://download.terminal.free/cdn/web/metaquotes.software.corp/mt4/mt4debian.sh&nbsp;;&nbsp;chmod&nbsp;+x&nbsp;mt4debian.sh&nbsp;;&nbsp;./mt4debian.sh</span></p></td></tr></tbody></table>

This command downloads the script, makes it executable and runs it. You only need to enter your account password to allow installation.

![Installing Wine and the terminal with a single command](/en/docs/mt4/terminal/img/linux_command_line.png "Installing Wine and the terminal with a single command")

If you are prompted to install additional Wine packages (Mono, Gecko), please agree, as these packages are required for platform operation. The installer will launch after that. Once you complete the standard steps, the platform is ready to go.

![The platform is ready to run on Linux](/en/docs/mt4/terminal/img/linux_terminal.png "The platform is ready to run on Linux")

## Install updates in a timely manner

It is highly recommended to always use the latest versions of the operating system and Wine. Timely updates increase platform operation stability and improve performance.

To update Wine, open a command prompt and type the following command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">sudo&nbsp;apt&nbsp;update&nbsp;;&nbsp;sudo&nbsp;apt&nbsp;upgrade</span></p></td></tr></tbody></table>

For further information, please visit the [official Wine website](https://wiki.winehq.org/Download).

## Terminal Data Directory

Wine creates a separate virtual logical drive with the necessary environment for every installed program. The default path of the installed terminal data folder is as follows:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Home&nbsp;directory\.mt4\drive_c\Program&nbsp;Files\MetaTrader&nbsp;4</span></p></td></tr></tbody></table>

Use the terminal on Linux: install with a single command and enjoy all the platform features.

[Install on Mac OS](/en/docs/mt4/terminal/userguide/install_mac)

[Terminal Start and Data Structure](/en/docs/mt4/terminal/userguide/start_comm)