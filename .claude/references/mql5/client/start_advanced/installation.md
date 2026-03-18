# Platform Installation

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/installation

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Platform Installation

# Platform Installation

To install the trading platform download the mt5setup.exe installer and run it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">This is a web installer. This means that most of the components will be downloaded from the Internet during installation.</span></li><li class="p_tableatten"><span class="f_tableatten">The installer determines the bit characteristics of the operating system and installs the appropriate version of the platform;</span></li><li class="p_tableatten"><span class="f_tableatten">The platform can run under Microsoft Windows 2008/7/8/10/11. A processor with SSE2 support (Pentium 4/Athlon 64 or higher) is also required. Other hardware requirements depend on specific platform use conditions — load from running MQL5 applications, number of active instruments and charts, etc.&nbsp;</span></li></ul></td></tr></tbody></table>

Review the software description and the end-user license agreement. If you agree with all terms of the agreement, click on the "Next" button. If you do not agree with the Agreement, exit the installation program.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A click on "Next" starts the background download of the platform distribution package from one of the developer's servers. A server that is closest to the user is chosen for downloading.</span></p></td></tr></tbody></table>

![Follow the wizard step to install the platform](/en/docs/mt5/client/img/setup_wizard.gif "Follow the wizard step to install the platform")

Click "Settings" to select installation options:

-   Installation folder — the directory you want to install the trading platform to. You can specify a different directory, by setting the path to it manually, or by clicking the "Browse" button.
-   Program group — the name of the program group that will be created in the Start menu.
-   Open MQL5.community — open the most popular traders' community website after installation. [MQL5.community](/en/docs/mt5/client/mql5community) features multiple useful services, from automated copy trading to the possibility of purchasing ready-made trading robots from the Market and running them 24/7 on a virtual platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The platform can be installed over an existing one. All the previous platform settings are preserved, except for the default <a href="/en/docs/mt5/client/charts_advanced/templates_profiles#profiles" class="topiclink">profiles</a> and <a href="/en/docs/mt5/client/charts_advanced/templates_profiles" class="topiclink">templates</a>, and the standard set of <a href="/en/docs/mt5/client/autotrading" class="topiclink">MQL5-programs</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">If you need to work with multiple accounts simultaneously, install the appropriate number of platforms in different directories.</span></li></ul></td></tr></tbody></table>

Click "Next" to start the installation. When finished, click "Finish" and [run](/en/docs/mt5/client/start_advanced/start) the platform.

## Beta Installation [#](installation#beta)

You can use the /beta key for the terminal installation file, which allows downloading the beta version. In normal mode, the release version should be installed first, which can then be updated till a beta version. By skipping this step, you can save time and traffic. Installation start example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">C:\mt5setup.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/beta</span></p></td></tr></tbody></table>

To update an already installed platform up to beta build, navigate to Help — Check Desktop Updates — Latest Beta Version.

## Installation in automatic mode [#](installation#auto)

The platform can be installed in the automatic mode, without additional actions required from the user. When the installer is launched with the /auto key, installation settings will not be shown to the user, and the terminal will be installed at the standard path with the standard Start menu folder name for the program.

You can specify another directory for the platform installation in automatic mode using the additional key /path:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">C:\mt5setup.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/auto&nbsp;/path:"C:\Program&nbsp;Files\MyFolder"</span></p></td></tr></tbody></table>

[For Advanced Users](/en/docs/mt5/client/start_advanced)

[Installation on Mac OS](/en/docs/mt5/client/start_advanced/install_mac)