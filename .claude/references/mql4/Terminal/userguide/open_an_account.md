# Opening of Accounts

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/userguide/open_an_account

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Getting Started](/en/docs/mt4/terminal/userguide)Opening of Accounts

# Opening of Accounts

Terminal allows to work with two types of accounts: [demo accounts](/en/docs/mt4/terminal/userguide/open_an_account#open_demo) and [real accounts](/en/docs/mt4/terminal/userguide/open_an_account#open_real). Demo accounts enable working under training conditions, without real money on them, but they allow to work out and test trading strategy very well. They possess all the same functionality as the real ones. The distinction consists in that demo accounts can be opened without any investments, though one cannot count on any profit from them.

## Opening of a Demo Account [#](open_an_account#open_demo)

A demo account can be opened by the ["File —](/en/docs/mt4/terminal/overview/main_menu/main_menu_file)![open_account_icon](/en/docs/mt4/terminal/img/open_account_icon.png) [Open an Account"](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) menu command or by the same command of the ["Navigator — Accounts" window](/en/docs/mt4/terminal/overview/navigator) context menu. Besides, the terminal will offer to open a demo account at the first program start to begin working immediately.

The process of opening an account consists of several steps:

### Selecting Server

![open_account_servers](/en/docs/mt4/terminal/img/open_account_servers.png)

The first stage of account opening is selection of a server to connect to. Addresses of available servers, their names and ping are listed there. The most preferable is the server having the lowest ping. To perform additional checking the ping, you should press the "Scan" button. After that the ping information becomes refreshed.

Also in this window you can add a new server to connect to. To do it, press the "![Add new server](/en/docs/mt4/terminal/img/add_server_icon.png "Add new server") add new server" button or the "Insert" key. A server can be specified in different ways:

-   Write its address and port separated with a colon. For example, 192.168.0.100:443;
-   Write its domain name and port separated with a colon. For example, mt.company.com:443;
-   Write an accurate name of a brokerage company.

As soon as you specify a server, press "Enter". To delete a server, select it and press the "Delete" key.

### Account type [#](open_an_account#type)

At this stage a user can specify details of an existing trade account or start creating a new one.

![Account Type](/en/docs/mt4/terminal/img/open_account_type.png "Account Type")

This window contains three options:

-   Existing trade account — if this option is chosen, it is necessary to fill out the "Login" and "Password" fields with the corresponding account details. A server selected at the previous step is displayed below these fields. You will be authorized at the specified server using the specified account as soon as you press the "Done" button.
-   New demo account — if you choose this option and press the "Next" button, you will go to the creation of a new demo account.
-   New real account — if you choose this option you will pass to specifying personal details for sending a request to open a real account.

### Personal Details

The next stage of opening an account is specifying personal details:

![open_account_details](/en/docs/mt4/terminal/img/open_account_details.png)

The following data will be requested to open an account:

-   Name — the user's full name.
-   E-Mail — email address.
-   Phone — contact telephone number.
-   Account Type — account type to be selected from the list defined by the brokerage company.
-   Deposit — the amount of the initial deposit in terms of the basic currency. The minimum amount is 10 units of the specified currency.
-   Currency — the basic currency of the deposit to be set automatically depending on the account type selected.
-   Leverage — the ratio between the borrowed and owned funds for trading.

To activate the "Next" button and continue registration, it is necessary to flag "I agree to subscribe to your newsletters".

After the registration has successfully completed, a window will appear that contains information about the open account: "Login" — the account number, "Password" — the password for access, "Investor" — the investor's password (connection mode in which it is possible to check the account status, analyze the price dynamics, etc., but no trading is allowed).

![open_account_registration](/en/docs/mt4/terminal/img/open_account_registration.png)

After registration has been completed, the new account will appear in the ["Navigator — Accounts" window](/en/docs/mt4/terminal/overview/navigator), and it is ready to work with. At that, the server sends a message to the terminal containing login and passwords of this newly opened account. This message can be found in the ["Terminal — Mailbox" window](/en/docs/mt4/terminal/overview/terminal/terminal_mailbox). Besides, after the account has been successfully registered, it will be [authorized](/en/docs/mt4/terminal/userguide/authorization) automatically.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If any problems occur at the account opening, technical support service of the brokerage company should be asked for help.</span></p></td></tr></tbody></table>

## Opening of a Real Account [#](open_an_account#open_real)

Real accounts, unlike demo accounts, cannot be opened from the terminal. They can only be opened by brokerage companies under certain terms and conditions. Real accounts are marked correspondingly in the ["Navigator — Accounts" window](/en/docs/mt4/terminal/overview/navigator). To start working with them, one must perform [authorization](/en/docs/mt4/terminal/userguide/authorization).

[Terminal Start and Data Structure](/en/docs/mt4/terminal/userguide/start_comm)

[Authorization](/en/docs/mt4/terminal/userguide/authorization)