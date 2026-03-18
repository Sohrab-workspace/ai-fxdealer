# Live Update

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/userguide/liveupdate

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Getting Started](/en/docs/mt4/terminal/userguide)Live Update

# Live Update

A system of automatic updates is built into the terminal. It allows to get informed about and install new versions of the program promptly. This system is always enabled, it is impossible to disable it.

## Updating Procedure

The terminal checks for new versions of the program when it connects to the server. If a new version of any of the terminal components has been discovered, it will be automatically downloaded in the background mode. At that, the following entry will be displayed in the terminal journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">10:13:37.730</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">LiveUpdate:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">new</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">version</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">4.00</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">build</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1340</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span></p></td></tr></tbody></table>

On default, the updates are downloaded to the following folder: C:\\Users\\username\\AppData\\Roaming\\MetaQuotes\\WebInstall

Here "C" is the letter of a logical disk, where the operating system is installed, "username" is the account in the operating system, under which the terminal has been installed. Downloaded updates are available for all terminals, the updates are not re-downloaded for other instances of terminals.

After all the updates have been downloaded, the below entry will appear in the terminal journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">10:14:17.180&nbsp;LiveUpdate:&nbsp;finished</span></p></td></tr></tbody></table>

To apply the updates, the terminal should be restarted.

## Updating with UAC Enabled

If the UAC (User Account Control) system is enabled on the computer or the user does not have sufficient rights in th OS, a window requesting confirmation/increase of the user's permissions will be shown at the attempt to update.

![Update in MS Windows Vista](/en/docs/mt4/terminal/img/live_update_vista.png "Update in MS Windows Vista")

Depending on the user's permissions in Windows, it is necessary either to allow the operation (if a user is an administrator) or specify administrator account details.

[OTP](/en/docs/mt4/terminal/userguide/otp)

[Client Terminal Settings](/en/docs/mt4/terminal/setup)