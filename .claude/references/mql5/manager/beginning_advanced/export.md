# Data Export

> Source: https://support.metaquotes.net/en/docs/mt5/manager/beginning_advanced/export

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[For Advanced Users](/en/docs/mt5/manager/beginning_advanced)Data Export

# Data Export

[Online Users](/en/docs/mt5/manager/online_accounts), [Trading Accounts](/en/docs/mt5/manager/accounts), [Positions](/en/docs/mt5/manager/positions) and [Orders](/en/docs/mt5/manager/orders) sections provide the possibility to export information to external files to use it in other applications. Click ![Export...](/en/docs/mt5/manager/img/export_icon.png "Export...") Export... in the context menu of the respective section or in the [File menu](/en/docs/mt5/manager/main_menu#file). A window appears where you can specify the directory for saving the file and configure the export:

![Export settings](/en/docs/mt5/manager/img/export_settings.png "Export settings")

The following export options are available here:

-   All — export all information, regardless of the currently selected columns, except for the columns of the Account Columns menu in [server reports](/en/docs/mt5/manager/reports). The latter are exported only in Visible mode and only if enabled.
-   Visible — export only those columns that are currently enabled.
-   Selected — open the below described window to manually specify columns for export.

In the "Save as type" field, select the format of the destination file: \*.HTML or \*.CSV. Set the file name and click Save.

### Selecting columns to export

![Selecting the columns](/en/docs/mt5/manager/img/export_columns.png "Selecting the columns")

Available columns are located in the left part, selected ones are in the right part. The following commands are available in this window:

-   Add — add a selected column to selected ones. A similar action is performed by double-clicking the column.
-   Remove — remove a selected column from the list of selected ones. A similar action is performed by double-clicking the column. Some of the fields are required in export, they cannot be removed.
-   Up — move an added column upward relative to other columns. The order of selected columns determines the sequence of data in the exported file.
-   Down — move an added column downward relative to other columns.
-   Reset — return the default column settings.

[Auto Update](/en/docs/mt5/manager/beginning_advanced/liveupdate)

[Terminal Deinstallation](/en/docs/mt5/manager/beginning_advanced/deinstallation)