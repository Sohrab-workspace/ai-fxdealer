# Adding a New Account

> Source: https://support.metaquotes.net/en/docs/mt4/manager/client_accounts/ug_new_accounts

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Client Accounts](/en/docs/mt4/manager/client_accounts)Adding a New Account

# Adding a New Account

MetaTrader Manager 4 allows manager to add a new account to an account group for which this manager has sufficient rights. The created accounts will have zero deposit which can be completed later. A new account can be added through "File - New Account..." menu command.

![Adding a New Account](/en/docs/mt4/manager/img/new_account.png "Adding a New Account")

It is necessary to fill out personal data of the account in the appearing window:

-   Group — the group to which the account belongs;
-   Predefined login — the account number. If this field has not been filled out when a new account is added, the server will fill it out automatically;
-   Name — the owner's name;
-   Status — resident/non-resident, the characteristic of a taxable person that is defined by the principle of his/her permanent residence;
-   Color — the color the information about the account will be displayed with in the dealer's window when a new trading request comes from the account owner;
-   City — city;
-   State — state (district, region, territory, etc.);
-   Country — country;
-   Address — residence address of the account owner;
-   Zip-code — postal code;
-   Email — emailing address;
-   Phone — telephone number.
-   Comment — the description;
-   ID number — SIN, TIN, ITN, or other identification data of the account owner;
-   Leverage — leverage;
-   Tax rate — tax rate;
-   Agent account — the account of the agent that services this trading account;
-   Allow to change password — allow/prohibit to change password;
-   Read only (without trading) — allow to trade or to watch charts only, without trading;
-   Send reports — send reports.

Passwords to access to the account must be given, as well:

-   Master — the main password of the account;
-   Investor — the investor password of the account to be used for account monitoring without permission to make transactions;
-   Phone — password for the account owner identification when trades are made by phone.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention! The main password and the investor password must be rather complex: at least 5 characters long and containing at least two of four character types (lowercase, uppercase, digits or <a href="https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters" target="_blank" class="weblink">special characters</a>). The maximum password length is 15 characters.</span></p></td></tr></tbody></table>

[Client Accounts](/en/docs/mt4/manager/client_accounts)

[Accounts](/en/docs/mt4/manager/client_accounts/ug_accounts)