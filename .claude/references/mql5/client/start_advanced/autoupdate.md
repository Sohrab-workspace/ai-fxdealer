# Live Update

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/autoupdate

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Live Update

# Live Update

A system of automatic updates is built into the platform. It provides timely updates to new versions. This system can not be deactivated.

## Updating Procedure

Upon connecting to a trade server, the system checks for the platform updates. If a new version of any of the platform components is found, it is automatically downloaded in the background mode.

The updates are downloaded to the following default folder C:\\Users\\username\\AppData\\Roaming\\MetaQuotes\\WebInstall. Here "C" is the letter of a logical disk, where the operating system is installed, "username" is the account in the operating system, under which the platform has been installed. Downloaded updates are available to all platforms, the updates are not re-downloaded for other instance of the platform.

After the update is downloaded, the following dialog appears prompting you to update the platform:

![A click on Restart closes the platform, updates and then re-starts it](/en/docs/mt5/client/img/live_update.png "A click on Restart closes the platform, updates and then re-starts it")

Click one of the buttons:

-   Restart — the windows of the platform and [MetaEditor](/en/docs/mt5/client/autotrading#metaeditor) (if t is open) are closed, the components are updated, and the platform is then restarted.
-   Later — it hides the dialog, and the platform is updated automatically later with the next start.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">All the update stages appear in the trading platform <a href="/en/docs/mt5/client/start_advanced/journal" class="topiclink">Journal</a>. "LiveUpdate" is specified in the Source column of such logs.</span></li><li class="p_tableatten"><span class="f_tableatten">If the platform update fails (connection to server is lost), the next attempt will be made after one hour. Only missing data will be downloaded during this attempt.</span></li></ul></td></tr></tbody></table>

## Updating with UAC Enabled

If the UAC (User Account Control) system is enabled on the computer or the user does not have sufficient rights in the OS, a dialog requesting to confirm/increase the user's permissions appears at the attempt to update.

![To update the platform in MS Windows Vista with UAC enabled, specify administrator account details](/en/docs/mt5/client/img/live_update_vista.png "To update the platform in MS Windows Vista with UAC enabled, specify administrator account details")

Depending on the user's permissions in MS Windows, it is necessary either to allow the operation (if a user is an administrator) or specify administrator account details.

## Updating Manuals [#](autoupdate#help_update)

All user manuals (this User Guide, MetaEditor and MQL5 references) are updated separately. No more than once every two weeks, when a manual is opened, the system checks for its new version. If one is found, the following dialog appears, prompting to download it:

![Click Yes to download the latest Help version](/en/docs/mt5/client/img/update_help.png "Click Yes to download the latest Help version")

Click Yes to download the new version of the specified manual. To cancel the update, click No or close the window.

[Security System](/en/docs/mt5/client/start_advanced/security)

[Platform Logs](/en/docs/mt5/client/start_advanced/journal)