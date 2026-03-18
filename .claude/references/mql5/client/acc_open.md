# Open an Account

> Source: https://support.metaquotes.net/en/docs/mt5/client/acc_open

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)Open an Account

# Open an Account

Two types of accounts are available in the trading platform: demonstration (demo) and real. Demo accounts provide the opportunity to work in a training mode without real money, allowing to test a trading strategy. They feature all the same functionality as the live ones. The difference is that demo accounts can be opened without any investment and, therefore, one cannot expect to profit from them.

## Demo Account Opening [#](acc_open#demo)

Click "![Open an Account](/en/docs/mt5/client/img/open_account_icon.png "Open an Account") Open an Account" in the [File](/en/docs/mt5/client/interface) menu or in the context menu of the Navigator window.

![Select a server to open an account](/en/docs/mt5/client/img/open_account_servers.png "Select a server to open an account")

The account opening procedure consists of several steps:

### Select a Server

A broker is selected during the first step. If the desired company is not shown in the list, please type its name and click "Find your broker". Alternatively, you can type the address of the server instead of the company name. Once you find the desired company, select it and click "Next".

If the brokers list becomes too long, you can delete unnecessary companies by pressing the "Delete" key.

### Account Type [#](acc_open#type)

Enter the details of your existing account or create a new one.

![Choose account type](/en/docs/mt5/client/img/getting_started.png)

Choose this option to [connect](/en/docs/mt5/client/authorization) to an existing trading account. You will need to specify the account number, the password and the server name.

Select this option to open a demo account. Demo accounts help users learn trading and test trading strategies. All trading operations only involve virtual money.

Select this option to request opening of a [real account](/en/docs/mt5/client/acc_open#real). Trading operations are performed using real money on such accounts, therefore you will need to provide broker detailed information about yourself, as well as ID and proof of address documents. The broker will check provided information and contact you to complete the account opening procedure.

### Personal Details

Enter your personal details:

![Personal details](/en/docs/mt5/client/img/open_account_details.png)

### Personal Details

-   First name — the name of the user consisting of at least two characters.
-   Second name — the second name (surname) of the user consisting of at least two characters.
-   Email — email address, e.g. "smith@company.net".
-   Phone — contact phone number in international format. Example: +74951234567.

### Account Parameters

-   Use hedge in trading — enable the option if you want to open an account with the [hedging position accounting system](/en/docs/mt5/client/general_concept#hedging), which allows having multiple open positions of the same symbol, including opposite positions. Otherwise an account with the [netting system](/en/docs/mt5/client/general_concept#netting) will be opened. The option affects account types available for selection.
-   Account Type — select a type from the drop down list.
-   Deposit — the initial deposit in the basic currency. Selected from a drop down list.
-   Currency — this field cannot be edited, the deposit currency is indicated here. This parameter depends on the account type specified.
-   Leverage — ratio between borrowed and owned funds for trading; Select one of the available variants from the drop down list.

Links to broker's agreements are shown in this block. Read them carefully. The number of links and types of agreements available depend on the selected broker.

If you agree with account opening terms and the broker's data protection policy, tick the appropriate box and click "Next". After that, the account will be created.

### Account Registration

Once an account is created on a selected server, details will be shown in the dialog window:

![Account connection details are provided in the last step](/en/docs/mt5/client/img/open_account_registration.png "Account connection details are provided in the last step")

The upper part of the window contains brief information about the account; the lower part shows its details:

-   Login — the number of the opened account.
-   Password — a password to access the account. This is a master password, which allows trading from this account.
-   Investor — investor password. The password allows connecting to the account to view its state and analyze price dynamics, but it does not allow trading.

A QR code is shown below, using which you can instantly connect to this account from the [mobile platform](/en/docs/mt5/client/mobile_trading). Open the mobile application, go to the "New account" section and click "Sign In with QR code". Point your camera at the QR code, and the trading account will be instantly connected, without the need to specify login, password and server values.

![Sign in with QR code](/en/docs/mt5/client/img/qr_code.png "Sign in with QR code")

After clicking Finish, the newly created account is automatically connected to the trade server. It also appears in the Accounts section of the [Navigator](/en/docs/mt5/client/interface) window. If you click Cancel in this window, connection to the trade server is not performed and the account is not added to the Navigator window, though it is already created. You can [connect](/en/docs/mt5/client/authorization) to the server later using the account details.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">If you have any problems with registration, please contact your broker's technical support team.</span></p></td></tr></tbody></table>

## Live Account Opening [#](acc_open#real)

Directly from the trading platform, you can send a request to open a live account, on which you can trading using real money. You will need to fill out a few simple forms, and to additionally provide documents to confirm your identity and address.

Choose the option "Open a real account for live trading" and specify the required data:

![A request to open a real account](/en/docs/mt5/client/img/real_account.gif "A request to open a real account")

Depending on broker's settings and applicable legislation, you can be requested to fill in information on employment, income and trading experience. In particular, such account opening requirements apply to MiFID regulated brokers (The Markets in Financial Instruments Directive).

![Extended real account opening form](/en/docs/mt5/client/img/real_account_additional.gif "Extended real account opening form")

Once you fill in all fields, a preliminary account with the zero balance will be opened for you on the broker's server. Although you cannot trade on a preliminary account, you can monitor price dynamics, perform technical analysis and test strategies.

Soon after opening the preliminary account, a representative of the brokerage company will contact you to finish the procedure of real account opening. After that the preliminary account is converted to the real one, and you can start trading from it.

An informational email is additionally sent to you via the internal mailing system when a preliminary account is opened.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Accounts in the <a href="/en/docs/mt5/client/interface" class="topiclink">Navigator</a> window are marked with appropriate icons depending on their type: <img class="help" alt="Demo account" title="Demo account" width="12" height="16" src="/en/docs/mt5/client/img/account_icon.png">— a demo account,<img class="help" alt="Preliminary account" title="Preliminary account" width="12" height="16" src="/en/docs/mt5/client/img/preliminary_account_icon.png">— a preliminary account,<img class="help" alt="Live account" title="Live account" width="12" height="16" src="/en/docs/mt5/client/img/real_account_icon.png">— a live account.</span></p></td></tr></tbody></table>

## Contest Accounts [#](acc_open#contest)

The platform features a special account type, which can be used for various trading contests and competitions. They operate similarly to demo accounts and are marked with a blue icon![Contest account](/en/docs/mt5/client/img/contest_account_icon.png "Contest account") in the [Navigator](/en/docs/mt5/client/interface) window. Such accounts can only be opened by a brokerage company. When you are connected to such an account, the "Contest account" title is displayed in the platform window header.

[User Interface](/en/docs/mt5/client/interface)

[Connect to an Account](/en/docs/mt5/client/authorization)