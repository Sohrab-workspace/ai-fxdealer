# Auto Update

> Source: https://support.metaquotes.net/en/docs/mt5/manager/beginning_advanced/liveupdate

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
            -   [Installing the Terminal](/en/docs/mt5/manager/beginning_advanced/installation)
            -   [Files and Folders](/en/docs/mt5/manager/beginning_advanced/structure)
            -   [Extended Authentication](/en/docs/mt5/manager/beginning_advanced/extended_authorization)
            -   [One Time Passwords - 2FA/TOTP](/en/docs/mt5/manager/beginning_advanced/otp)
            -   [Auto Update](/en/docs/mt5/manager/beginning_advanced/liveupdate)
            -   [Data Export](/en/docs/mt5/manager/beginning_advanced/export)
            -   [Terminal Deinstallation](/en/docs/mt5/manager/beginning_advanced/deinstallation)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[For Advanced Users](/en/docs/mt5/manager/beginning_advanced)Auto Update

# Auto Update

The system of the live update is embedded in the Manager terminal. It provides timely updates to new versions. This system cannot be disabled.

## Updating procedure

When connecting to a trade server, the system checks for updates of the terminal. If the terminal update is found, it will be automatically downloaded in the background mode.

The updates are downloaded to the following default folder (depending on the operating system used):

Microsoft Windows XP SP3:

-   C:\\Documents and Settings\\username\\Application Data\\MetaQuotes\\WebInstall

Microsoft Windows Vista and higher:

-   C:\\Users\\username\\AppData\\Roaming\\MetaQuotes\\WebInstall

Here "C" is the letter of a logical disk, where the operating system is installed, "username" is an account in the operating system, under which the terminal has been installed. Downloaded updates are available to all platforms, the updates are not re-downloaded for other instance of the platform.

After the update is downloaded, the following dialog appears prompting you to update the terminal:

![Update](/en/docs/mt5/manager/img/live_update.png "Update")

Click one of the buttons:

-   Restart — the terminal window is closed, it is updated and the terminal is re-opened automatically.
-   Later — the dialog is hidden and the terminal is updated during its further start.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">All the update stages are reflected in the <a href="/en/docs/mt5/manager/toolbox#journal" class="topiclink">journal</a> of the Manager terminal. LiveUpdate is specified in the Server column of such entries.</span></li><li class="p_tableatten"><span class="f_tableatten">If the platform update fails (connection to server is lost), the next attempt is made after one hour. Only missing data is downloaded during this attempt.</span></li></ul></td></tr></tbody></table>

## Update in the guest mode

If the Manager terminal was launched in the [guest mode](/en/docs/mt5/manager/start#guest) (if the OS user has not enough rights), and you try to upgrade the terminal, a window asking you to increase the user's rights appears.

### Microsoft Windows XP

![Live Update in MS Windows XP](/en/docs/mt5/manager/img/live_update_xp.png "Live Update in MS Windows XP")

In this case, you should specify the details of the administrator account that has sufficient rights to write files in the directory of the terminal installation.

### Microsoft Windows Vista

![Live Update in MS Windows Vista](/en/docs/mt5/manager/img/live_update_vista.png "Live Update in MS Windows Vista")

Depending on the user's rights in MS Windows Vista, you must either give permission to perform the operation (if the user is an administrator), or specify the details of the administrator's account.

[One Time Passwords - 2FA/TOTP](/en/docs/mt5/manager/beginning_advanced/otp)

[Data Export](/en/docs/mt5/manager/beginning_advanced/export)