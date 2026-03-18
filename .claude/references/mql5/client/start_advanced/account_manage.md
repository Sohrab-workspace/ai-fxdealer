# Manage Trading Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/account_manage

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Manage Trading Accounts

# Manage Trading Accounts

Traders can work with multiple accounts in one platform. These accounts can be opened with different brokers. Used accounts are stored and displayed in the Navigator window, they are grouped based on the name of the server they are open on.

## How to Switch between Accounts

To switch to another account, double-click on it in the Navigator.

![To manage a trading account, open its context menu in the Navigator](/en/docs/mt5/client/img/navigator_accounts_manage.png "To manage a trading account, open its context menu in the Navigator")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The trading platform can be configured to automatically disable trading after switching to another account. It helps protect against accidental deals performed by a trading robot working on that account. Enable the option <a href="/en/docs/mt5/client/settings#enable_ea" class="topiclink">"Disable automated trading when switching accounts"</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">For greater security, you can disable the function of authorization data storage on the hard disk (encrypted). This can be done by disabling the option <a href="/en/docs/mt5/client/settings#keep_personal" class="topiclink">"Keep personal settings and data at startup"</a>. You will need to manually enter the password every time you connect to the account.</span></li></ul></td></tr></tbody></table>

Demo accounts are marked by the icon ![Demo account](/en/docs/mt5/client/img/account_icon.png "Demo account"), live accounts have icon ![Live account](/en/docs/mt5/client/img/real_account_icon.png "Live account"). An unlimited number of demo accounts can be opened in the platform. However, live accounts cannot be opened here. They can only be opened by a brokerage company.

Account management functions are available in the context menu:

-   ![Open an Account](/en/docs/mt5/client/img/open_account_icon.png "Open an Account") Open an Account — [open](/en/docs/mt5/client/acc_open#demo) a demo account. The same action can be performed by pressing Insert.
-   ![Login to Trade Account](/en/docs/mt5/client/img/login_icon.png "Login to Trade Account") Login to Trade Account — [connect](/en/docs/mt5/client/authorization) to a trade server using the selected account. The same operation can be performed by double-clicking on an account, or by selecting it and pressing Enter.
-   ![Login to MQL5.community](/en/docs/mt5/client/img/login_mql5_icon.png "Login to MQL5.community") Login to MQL5.community — open trading platform [settings](/en/docs/mt5/client/settings#community) to login to [MQL5.community](https://www.mql5.com/ "MQL5.community") and access additional services.
-   ![Change Password](/en/docs/mt5/client/img/change_password_icon.png "Change Password") Change Password — open the [account password change](/en/docs/mt5/client/settings#password) window.
-   ![Delete](/en/docs/mt5/client/img/delete_account_icon.png "Delete") Delete — delete a selected account. The same action can be performed by pressing the Delete key.
-   ![Transfer Funds](/en/docs/mt5/client/img/transfer_funds_icon.png "Transfer Funds") Transfer Funds — [transfer funds](/en/docs/mt5/client/start_advanced/account_manage#transfer_funds) between accounts. This commands is only available in the context menu of the current account, if the transfer of funds is allowed on the trade server.
-   ![Add to Favorites](/en/docs/mt5/client/img/add_to_favourites_icon.png "Add to Favorites") Add to Favorites — add the selected account to Favorites for quick access.
-   ![Register as Signal](/en/docs/mt5/client/img/register_as_signal_icon.png "Register as Signal") Register as Signal — register the selected account in the [Signals service](https://www.mql5.com/en/signals "Trade Signals"). A click on this command opens a [signal creation page](/en/docs/mt5/client/signal_provider#add) on MQL5.community. The selected account and the right broker server are automatically specified in the registration form.
-   ![Register a virtual server](/en/docs/mt5/client/img/vh_icon.png "Register a virtual server") Register a virtual server — this is a command for [renting a virtual server](/en/docs/mt5/client/virtual_hosting) to provide round-the-clock operation of the platform. Unlike renting ordinary VDS or VPS from third-party companies, with Virtual Hosting you can choose a server that is the closest to your broker to minimize the network latency when sending orders from the platform to a trade server.

## Transferring Funds between Accounts [#](account_manage#transfer_funds)

The trading platform allows transferring money between accounts within the same trade server. Money can only be transferred from the currently [connected](/en/docs/mt5/client/authorization) account. Select it in the [Navigator](/en/docs/mt5/client/interface) window and choose "Transfer funds" from the context menu.

![Click Transfer Funds in the context menu and specify receiver's details](/en/docs/mt5/client/img/transfer_funds.png "Click Transfer Funds in the context menu and specify receiver's details")

In the dialog box, select the account to which you want to transfer funds. The transfer amount is specified in the deposit currency of the current account. It cannot exceed the current balance and the current amount of free margin of the account.

To transfer funds, a master password must be specified for both accounts. If [OTP authentication](/en/docs/mt5/client/start_advanced/otp) is used for the account, from which funds are transferred, the one-time password should be additionally specified.

Funds are transferred in the form of [balance operations](/en/docs/mt5/client/performing_deals#trade_history): a withdrawal operation on the current account and depositing operation on the recipient account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The money transfer option must be enabled on the trade server. Depending on the settings, there are some restrictions on the accounts, between which transfer is allowed. In particular, money transfer can be allowed only for accounts with identical names and emails.</span></li><li class="p_tableatten"><span class="f_tableatten">Funds can be transferred only within the same trading server and only between the accounts of the same type. From a real account funds can be transferred only to another real account, from a demo one - only to demo.</span></li><li class="p_tableatten"><span class="f_tableatten">The accounts, between which funds are transferred, must use the same deposit currency.</span></li></ul></td></tr></tbody></table>

## Automatic creation of new demo accounts to replace inactive ones [#](account_manage#auto)

When a user tries to connect to an expired demo account (for which the server returns the "Invalid account" error), the platform automatically opens a new demo account. The account is created on the same trade server (provided that the broker still allows opening demo accounts from the platform).

An expired demo account is deleted from the Navigator window, since it becomes useless: it cannot be used for connecting to the trades server (the account has been deleted on the broker server), while its trading history cannot be viewed. When an expired demo account is deleted, the following message is added to the [platform journal](/en/docs/mt5/client/start_advanced/journal): current demo account 'XXXX' was deleted on trade server, new demo will be allocated.

Thus, the platform helps traders to instantly start working with the account and eliminates the need to delete inactive and unnecessary data.

[Files and Folders](/en/docs/mt5/client/start_advanced/structure)

[Mailbox](/en/docs/mt5/client/start_advanced/mail)