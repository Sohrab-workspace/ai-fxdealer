# Accounts

> Source: https://support.metaquotes.net/en/docs/mt4/manager/client_accounts/ug_accounts

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
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
            -   [Adding a New Account](/en/docs/mt4/manager/client_accounts/ug_new_accounts)
            -   [Accounts](/en/docs/mt4/manager/client_accounts/ug_accounts)
            -   [Online](/en/docs/mt4/manager/client_accounts/ug_online)
            -   [Orders](/en/docs/mt4/manager/client_accounts/ug_orders)
            -   [Sending Notifications](/en/docs/mt4/manager/client_accounts/push_notifications)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Client Accounts](/en/docs/mt4/manager/client_accounts)Accounts

# Accounts

The "Accounts" section is intended for managing all accounts of the system.

![Accounts](/en/docs/mt4/manager/img/br_accounts.png "Accounts")

To make the process more convenient, all accounts are accumulated in a table having adjustable cells. By default, the following fields are shown:

-   Login — the account number;
-   Name — the name of the account owner;
-   Group — the group in which the account is located;
-   City — city;
-   Email — email address;
-   Balance — balance;

Context menu allows to execute the following commands:

-   New Account — create a new account;
-   Account Details — open the window of account details;
-   Email — send a message to the client using internal email;
-   Journal — switch to the "Journal" tab to request logs for the selected account;
-   Group Operation — operation on a selected group of accounts;
-   Find — find the account in the list of accounts;
-   Copy — copy the selected accounts from the list into the clipboard;
-   Save — save the unprocessed report on the accounts;
-   Auto Arrange — automatic arrangement of column size when the window size is changed;
-   Grid — hide/show the grid to separate columns;
-   Columns — select columns to be shown.

## Personal data of the account (Personal tab) [#](ug_accounts#personal)

The personal data of the account are located in "Personal" tab:

![Account Settings](/en/docs/mt4/manager/img/win_account_modify.png "Account Settings")

-   Enable — enable/disable the account;
-   Registration date — the account registration date;
-   MetaQuotes ID is a unique identifier assigned to each user during installation of the MetaTrader 4 for [iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=download&utm_source=metatrader4.help "iPhone") or [Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=download&utm_source=metatrader4.help "Android"). This identifier is used like a phone number. By specifying MetaQuotes ID in the desktop terminal settings, a user can send notifications about various trad events on their mobile devices. MetaQuotes is also supported by [MQL5.community](https://www.mql5.com/ "MQL5.community"): by specifying the identifier in profile, a user can receive important notifications from the website and communicate with other members of the community via private messages. For more information please refer to the article [MetaQuotes ID in MetaTrader Mobile Terminal](https://www.mql5.com/en/articles/476 "Article MetaQuotes ID in MetaTrader Mobile Terminal").  
    MetaQuotes ID is added to the client record on the server side, once the client specifies it in the terminal settings. To [send a message](/en/docs/mt4/manager/client_accounts/push_notifications) to the client, click "Notification".
-   Name — the name of the account owner;
-   Phone password — password the account owner to be identified with when trading by phone;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To view the phone password, click the left mouse-button on this field.</span></p></td></tr></tbody></table>

-   City — city;
-   State — state (district, region, territory, etc.);
-   Country — country;
-   Address — the account owner's residence address;
-   Zip-code — zip-code;
-   Phone — telephone number;
-   Email — email address;
-   ID number — SIN, TIN, ITN, or other identification data of the account owner;
-   Status — resident/non-resident, the characteristic of a taxable person that is defined by the principle of his/her permanent residence;
-   Color — the color the information about the account will be displayed with in the [dealer's window](/en/docs/mt4/manager/request_processing/ug_dealing#color) when a new trading request comes from the account owner;
-   Group — the group to which the account belongs;
-   Comment — description;
-   Leverage — leverage;
-   Tax rate — tax rate;
-   Agent account — the account number of the agent servicing for this trading account;

-   LeadSource — this field is used for marketing campaigns allowing you to track where a client came from.  To receive the data, add the following to the client or mobile platform download link:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">https://download.terminal.free/cdn/web/metaquotes.software.corp/mt4/mt4setup.exe</span><span class="f_CodeExample" style="background-color: #dce6f2;">?utm_campaign=YourLeadSource</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt4/ios</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_campaign=YourLeadSource</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt4/android</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_campaign=YourLeadSource</span></p></td></tr></tbody></table>

where YourLeadSource is a name of a campaign. In the "server" parameter of the mobile platform links, enter the list of your servers to be shown to traders when they open an account.

When opening a demo account and connecting to any trading account via the terminal downloaded using such a link, utm\_campaign value is set in a client record at the server side.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention! An agent's clients should not necessarily have the same deposit currency as the agent account. Currency is converted according to the current exchange rates.</span></p></td></tr></tbody></table>

-   Enable one-time password — use of OTP (one-time password) provides an additional level of security when working with trading accounts. The user is required to enter a unique one-time password every time to connect to an account. One-time passwords are generated in the [mobile terminal for iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=download&utm_source=metatrader4.help "mobile terminal for iPhone") and the [mobile terminal for Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=download&utm_source=metatrader4.help "mobile terminal for Android"). Using this option, you can enable/disable the OTP use for individual clients in the group. If use of OTP is disabled for a group, enabling this option does not have any effect.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_ol">The instructions for using one-time password are provide in the client terminal user guide.</span></li><li class="p_tableatten"><span class="f_tableatten">One-time passwords are available only for client accounts. OTP authorization is currently not available for the manager and administrator terminals.</span></li></ul></td></tr></tbody></table>

-   Allow to change password — allow/prohibit to change password;
-   Read only (without trading) — allow to trade or to watch charts only, without trading;
-   Send reports — send reports.

### Account Commands

-   Journal — request server journal for the account.
-   Email — send a message to the account via the internal mail system.
-   Update — save changes made to the account on the server.
-   Notification — send a [push notification](/en/docs/mt4/manager/client_accounts/push_notifications) to the client. Inactive until MetaQuotes ID is filled.

## Account Security (Security tab) [#](ug_accounts#security)

![Security tab](/en/docs/mt4/manager/img/account_security.png "Security tab")

The "Security" tab makes it possible to check Master password of the account and to change the Master/Investor password of the account, as well.

There is an opportunity to reset the secret key of the account on the server for the accounts from the group having authorization via one-time passwords enabled. A secret key is required when using a custom generator of one-time passwords. This functionality is under development.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Password must be rather complex: at least 5 characters long and containing at least two of three character types (lowercase, uppercase, digits or <a href="https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters" target="_blank" class="weblink">special characters</a>). The maximum password length is 15 characters.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Once the password is changed, the connection of the account to the trader server is reset. A reconnection with the new password is required.</span></li></ul></td></tr></tbody></table>

## Group Operations [#](ug_accounts#group_op)

Group operations allow to work using a group of accounts selected in the table in "Accounts" section (not to be confused with account groups like demoforex, contest, etc.), but not separate accounts. To do so, it is necessary to execute "Group Operations" command of the context menu. All group operations are shown in the same window:

![Group Operations](/en/docs/mt4/manager/img/group_operation.png "Group Operations")

-   Set Group — move accounts to another group (demoforex, contest, etc.) that is chosen in the "Group" field;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Transferring accounts between groups with different deposit currency is only possible if the accounts have zero balance and credit.</span></li><li class="p_tableatten"><span class="f_tableatten">An account is immediately moved from one group to another one even if there are open orders and positions (server restart is not required) on condition that the groups have the same deposit currency. After transferring, connections of all active terminals with the corresponding logins are terminated in order to apply trading group settings on the client terminal's side.</span></li></ul></td></tr></tbody></table>

-   Set Leverage — set another leverage size specified in the "Leverage" field;
-   Enable — enable accounts;
-   Disable — disable accounts. This option applies only to newly connected accounts, but not to those having already been connected before. At this, the icons of the corresponding accounts become gray;
-   Delete — delete accounts. Remember that the accounts having open positions can not be deleted.

[Adding a New Account](/en/docs/mt4/manager/client_accounts/ug_new_accounts)

[Online](/en/docs/mt4/manager/client_accounts/ug_online)