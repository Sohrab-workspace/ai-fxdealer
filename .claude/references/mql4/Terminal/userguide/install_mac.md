# Install Terminal on Mac OS

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/userguide/install_mac

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Getting Started](/en/docs/mt4/terminal/userguide)Install on Mac OS

# Install Terminal on Mac OS

We provide a special installer for the trading platform on macOS. It is a full-fledged wizard that allows you to install the application natively. The installer performs all the required steps: it identifies your system, downloads and installs the latest [Wine](https://www.mql5.com/go?link=https://www.winehq.org/) version, configures it, and then installs the platform within it. All steps are completed in the automated mode, and you can start using the platform immediately after installation.

You can download the installer via this [link](https://download.terminal.free/cdn/web/metaquotes.software.corp/mt4/MetaTrader4.pkg.zip?utm_campaign=metatrader4.help) or via the Help menu in the trading platform.

## System Requirements

The minimum macOS version required to install the platform is Big Sur (11). The platform runs on all modern versions of macOS and supports all Apple processors, from M1 to the latest released versions.

## Preparation: Check the Wine version

If you are already using the trading platform on macOS, please check the current Wine version, which is displayed in the platform log upon startup:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2025.01.31&nbsp;12:40:45.967&nbsp;&nbsp;&nbsp;&nbsp;Windows&nbsp;10&nbsp;build&nbsp;18362&nbsp;on&nbsp;Wine&nbsp;</span><span class="f_CodeExample" style="background-color: #dce6f2;">8.0.1</span><span class="f_CodeExample">&nbsp;Darwin&nbsp;23.0.0,&nbsp;12&nbsp;x&nbsp;Intel&nbsp;Core&nbsp;i7-8750H&nbsp;&nbsp;@&nbsp;2.20GHz,&nbsp;AVX2,&nbsp;11&nbsp;/&nbsp;15&nbsp;Gb&nbsp;memory,&nbsp;65&nbsp;/&nbsp;233&nbsp;Gb&nbsp;disk,&nbsp;admin,&nbsp;GMT+2</span><br><span class="f_CodeExample">2025.01.31&nbsp;12:40:45.967&nbsp;&nbsp;&nbsp;&nbsp;MetaTrader&nbsp;4&nbsp;build&nbsp;1431&nbsp;started&nbsp;(MetaQuotes&nbsp;Software&nbsp;Corp.)</span></p></td></tr></tbody></table>

If your Wine version is below 8.0.1, we strongly recommend uninstalling the old platform along with the Wine prefix in which it is installed. Be sure to save all necessary files in advance, including templates, downloaded Expert Advisors, indicators, and others. You can uninstall the platform as usual by moving it from the "Applications" section to the Trash. The Wine prefix can be deleted using Finder. Select the "Go > Go to Folder" menu and enter the directory name: ~/Library/Application Support/.

![Go to the directory with the Wine prefix](/en/docs/mt4/terminal/img/macos_finder.png "Go to the directory with the Wine prefix")

Delete the following folders from this directory:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">~/Library/Application&nbsp;Support/Metatrader&nbsp;4</span><br><span class="f_CodeExample">~/Library/Application&nbsp;Support/net.metaquotes.wine.metatrader4</span></p></td></tr></tbody></table>

## Installation

The platform is installed like a standard macOS application. Run the downloaded file and follow the instructions. During the process, you will be prompted to install additional Wine packages (Mono, Gecko). Please agree to this as they are necessary for the platform functioning.

![Installing the trading platform in Mac OS](/en/docs/mt4/terminal/img/macos_pkg.png "Installing the trading platform in Mac OS")

## Terminal Data Directory

A separate virtual logical drive with the necessary environment is created for the trading platform 4 in Wine. The default path of the installed platform's data folder is as follows:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;~/Library/Application&nbsp;Support/net.metaquotes.wine.metatrader4/drive_c/Program&nbsp;Files/MetaTrader&nbsp;4&nbsp;</span></p></td></tr></tbody></table>

## Interface Language Settings

When installing the trading platform, Wine automatically adds support for the language (locale) currently set for macOS. In most cases, this is sufficient. If you wish to use a different language for the platform, switch the macOS language to the desired one before installation and restart your computer. Then, proceed with installing the platform. After the installation, you can set macOS to its original language.

[Install Terminal](/en/docs/mt4/terminal/userguide/installation)

[Install on Linux](/en/docs/mt4/terminal/userguide/install_linux)