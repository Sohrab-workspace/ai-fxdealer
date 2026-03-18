# Creation of Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/manager/account_create

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
            -   [Clients](/en/docs/mt5/manager/clients)
            -   [Online Accounts](/en/docs/mt5/manager/online_accounts)
            -   [Creation of Accounts](/en/docs/mt5/manager/account_create)
            -   [Importing Accounts](/en/docs/mt5/manager/account_import)
            -   [Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)
            -   [Push Notifications, SMS and Mail](/en/docs/mt5/manager/communication)
            -   [Account Overview](/en/docs/mt5/manager/account_overview)
            -   [Exposure](/en/docs/mt5/manager/account_exposure)
            -   [Personal Data](/en/docs/mt5/manager/account_personal)
            -   [Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)
            -   [Balance Operations](/en/docs/mt5/manager/account_balance)
            -   [Trading Operations](/en/docs/mt5/manager/account_trading)
            -   [Account History](/en/docs/mt5/manager/account_history)
            -   [Security and Certificates](/en/docs/mt5/manager/account_security)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Creation of Accounts

# Creation of Accounts

To create an account, select "![New Account](/en/docs/mt5/manager/img/new_account_icon.png "New Account") New Account" in the context menu or press Ctrl+N.

![Creating an account](/en/docs/mt5/manager/img/account_create.png "Creating an account")

For convenience, the account settings in the account creation window are divided into two blocks.

## Information

In this block, information about a client is set:

-   Preferred Login — account number. If you specify "next" instead of a number, the next available number is assigned to an account.
-   Group — group where the account will be created. Only a group available to a manager can be selected.
-   Preferred Client — the [client](/en/docs/mt5/manager/clients) to whom the account should be linked. Specify the ID, name or contact information in the Existing Client field and then click "Request". Then select the required client from the list.
-   Name — name of the account holder.
-   Last Name — second name of the account owner.
-   Middle Name — middle name of the account owner.
-   Company — name of the client's company.
-   E-Mail — e-mail address.
-   Phone — phone number.
-   Country — country of residence.
-   State — state (region) of residence.
-   City/Town — city/town of residence.
-   Zip code — zip or postal code.
-   Address — client's address.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/manager/account_personal" class="topiclink">Additional settings</a> can be configured for an account after creating it.</span></li><li class="p_tableatten"><span class="f_tableatten">Accounts are always created with a zero balance. To deposit funds, go to the <a href="/en/docs/mt5/manager/account_balance" class="topiclink">Balance</a> section of a created account.</span></li></ul></td></tr></tbody></table>

## Passwords

In this block, passwords are set. When you create an account, passwords are generated automatically, however they can be specified manually in the appropriate fields:

-   Master — master password for an account.
-   Investor — investor password (without the possibility of trading).
-   Phone — phone password used for identifying an account holder while performing trade operations over phone.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">All passwords, including master and investor, must contain four character types: lowercase letters, uppercase letters, numbers and symbols (#, @, !, etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings, while the lowest possible value is 8 characters. The maximum length is 16 characters.</span></p></td></tr></tbody></table>

After specifying all the data, click OK.

[Online Accounts](/en/docs/mt5/manager/online_accounts)

[Importing Accounts](/en/docs/mt5/manager/account_import)