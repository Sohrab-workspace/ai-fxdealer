# Security System

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/security

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Security System

# Security System

Particular attention is paid to the security of the trading platform. The following measures are undertaken to provide secure operation:

-   Data Encryption  
    Data exchange between the trading platform and the server is compressed and encrypted based on 128-bit keys.
-   Extended Authentication  
    The [extended authentication](/en/docs/mt5/client/start_advanced/extended_authorization) mode can be enabled on the server, which additionally improves account protection from unauthorized access.
-   Server Authentication  
    During [authentication](/en/docs/mt5/client/authorization), not only clients confirm their authenticity, but the trade server also undergoes authentication in the trading platform. This is to ensure that the trade server is the very server, which it claims to be.
-   Protection of Configuration Files  
    Connecting to a trade server using configuration files copied from the [/Config](/en/docs/mt5/client/start_advanced/structure#config) folder of another platform is impossible. All configuration files that store server connection settings and accounts are encrypted.
-   Protection of Passwords  
    All password entering fields are protected from being viewed using hacking programs.

## Security of Databases

All databases of the platform are encrypted and protected from use on other platforms.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Always keep account details in a safe place. If you move a platform from one computer to another, there is no possibility to use the information stored in it (accounts, emails, trade history). After authenticating on a server using an account, trade, mail and news databases are restored, but the account details can only be restored by contacting a broker.</span></p></td></tr></tbody></table>

-   Account Database  
    The database of [accounts](/en/docs/mt5/client/acc_open) ([/Config/accounts.dat](/en/docs/mt5/client/start_advanced/structure#accounts)) of a platform is bound to a user account in the operating system and computer configuration. If a user tries to authorize in the platform under a different user account in the operating system, or when the platform data are transferred to another computer, the entire database of accounts is deleted during the start of the platform. In this connection, you must keep the accounts details (login and password) in a separate safe place.
-   Information Databases  
    Mail, [trade](/en/docs/mt5/client/performing_deals#trade_history) and symbol databases are encrypted. They are automatically deleted at an attempt to move them and open in a different platform.

[Mailbox](/en/docs/mt5/client/start_advanced/mail)

[Live Update](/en/docs/mt5/client/start_advanced/autoupdate)