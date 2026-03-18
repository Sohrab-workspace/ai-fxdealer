# Accounts

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_accounts

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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
                -   [Group Operations](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations)
                -   [Account Restore](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore)
                -   [Account Archive](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_archive)
                -   [Account Redirection](/en/docs/mt4/administrator/administration/ug_accounts/account_allocation_url)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Accounts

# Accounts

The "Accounts" section is intended to manage accounts of the system. Account are represented as a table. Use the "Columns" sub-menu of the context menu, to adjust fields displayed in it.

![Accounts](/en/docs/mt4/administrator/img/br_accounts.png "Accounts")

The "Request" button and the corresponding context menu command allow to request the accounts of a specific group or those of all groups simultaneously. The parameters of the request should be indicated in "Group" and "Database" fields. As a request parameter in the "Group" field you can indicate both a group or a group wildcard (like a file wildcard). For example, if you need to find all accounts of all demo groups you can write in this field "demo\*" as a request. Also you may indicate a list of logins, commas being delimitors. In the "Database" field, you can specify either the current database or an archive or backup one.

To find the required client's account by a certain given criterion among the results of a request from data base, use the "Find" window (press "Ctrl+F" to show this window).

The "Delete Account" command will delete the account selected. "Group Operations" — allows to execute [group operations](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations).

The "New Account" command will allocate new account. The "Edit Account" command allows to edit an account.

## Personal data of the account (Personal tab) [#](ug_accounts#personal)

When having executed the "Edit Account" context menu commands, the account parameter window will appear. The personal data of the account are located in "Personal" tab:

![Account Settings](/en/docs/mt4/administrator/img/win_account_modify.png "Account Settings")

-   Enable enables/disables the account;
-   Registration date is the date the account was registered;
-   MetaQuotes ID is a unique identifier assigned to each user during installation of the MetaTrader 4 for [iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=download&utm_source=metatrader4.help "iPhone") or [Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=download&utm_source=metatrader4.help "Android"). This identifier is used like a phone number. By specifying MetaQuotes ID in the desktop terminal settings, a user can send notifications about various trade events on their mobile devices. MetaQuotes is also supported by [MQL5.community](https://www.mql5.com/ "MQL5.community"): by specifying the identifier in profile, a user can receive important notifications from the website and communicate with other members of the community via private messages. For more information please refer to the article [MetaQuotes ID in MetaTrader Mobile Terminal](https://www.mql5.com/en/articles/476 "Article MetaQuotes ID in MetaTrader Mobile Terminal").  
    MetaQuotes ID is added to the client record on the server side, once the client specifies it in the terminal settings.
-   Login is the account number (it appears only in the window of account creation. Once an account has been created Login can not be changed). If this field is not filled out when adding an account, the server will fill it out automatically;
-   Name is the account holder's name;
-   Phone password is a password for the account holder's identification when trading by telephone;
-   City is location of the holder;
-   State is a state (region, other political subdivision);
-   Country is the account holder's country;
-   Address is the account holder's mailing address;
-   Zip-code is the account holder's zip-code or postal code;
-   Phone is the account holder's telephone number;
-   Email is the account holder's email;
-   ID number is the account holder's SIN, TIN, ITN, or other identification number;
-   Status is the field where you should indicate resident/non-resident;
-   Color is the color the information about the account will be displayed with in the dealer's window when a new trading request comes from the account owner;
-   Group is a group to which the account belongs;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Transferring the account from one group to another is impossible if deposit currencies are different in these groups.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">An account is immediately moved from one group to another one even if there are open orders and positions (server restart is not required) on condition that the groups have the same deposit currency. After transferring, connections of all active terminals with the corresponding logins are terminated in order to apply trading group settings on the client terminal's side.</span></li></ul></td></tr></tbody></table>

-   Comment is a description;
-   Leverage is a leverage;
-   Tax rate is a tax on the amount obtained at calculation of interests charged on free assets (annual interest). Collected monthly at charging of the annual interest;
-   Agent account is the account number of agent servicing for the selected account;

-   LeadSource — this field is used for marketing campaigns allowing you to track where a client came from.  To receive the data, add the following to the client or mobile platform download link:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">https://download.terminal.free/cdn/web/metaquotes.software.corp/mt4/mt4setup.exe</span><span class="f_CodeExample" style="background-color: #dce6f2;">?utm_campaign=YourLeadSource</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt4/ios</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_campaign=YourLeadSource</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt4/android</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_campaign=YourLeadSource</span></p></td></tr></tbody></table>

where YourLeadSource is a name of a campaign. In the "server" parameter of the mobile platform links, enter the list of your servers to be shown to traders when they open an account.

When opening a demo account and connecting to any trading account via the terminal downloaded using such a link, utm\_campaign value is set in a client record at the server side.

-   Allow to change password is the field where you can permit/prohibit changing password;

-   Enable one-time password — using this option, you can disable the OTP use for individual clients in the group. If use of OTP is [disabled for a group](/en/docs/mt4/administrator/administration/ug_groups#otp), enabling this option does not have any effect.

-   Read only (without trading) is the field where you can permit trading or reading charts only;
-   Send reports — enable/disable sending of [daily and monthly reports](/en/docs/mt4/administrator/administration/ug_groups#group_reports) to this account. If sending of reports is disabled, reports for this client are still generated.

The "Update" command updates personal data of an account on the server.

## Account Orders (Trades tab) [#](ug_accounts#trades)

![Trades tab](/en/docs/mt4/administrator/img/account_trades.png "Trades tab")

The "Trades" tab allows to request the client's order list. Double click on the transaction opens the [window of transaction details](/en/docs/mt4/administrator/administration/ug_orders#deal). If you check the "Open only" field and press the "Refresh" button, only open trades of this account will be represented on the tab.

## Account Security (Security tab) [#](ug_accounts#security)

![Security tab](/en/docs/mt4/administrator/img/account_security.png "Security tab")

The "Security" tab makes it possible to check Master password of the account and to change the Master/Investor password of the account, as well.

There is an opportunity to reset the secret key of the account on the server for the accounts from the group having authorization via [one-time passwords](/en/docs/mt4/administrator/administration/ug_groups#otp) enabled. A secret key is required when using a custom generator of one-time passwords. This functionality is under development.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Password must be rather complex: at least 5 characters long and containing at least two of three character types (lowercase, uppercase, digits or <a href="https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters" target="_blank" class="weblink">special characters</a>). The maximum password length is 15 characters.</span></li><li class="p_tableatten"><span class="f_tableatten">Once the password is changed, the connection of the account to the trader server is reset. A reconnection with the new password is required.</span></li></ul></td></tr></tbody></table>

[Plugins](/en/docs/mt4/administrator/administration/ug_plugins)

[Group Operations](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations)