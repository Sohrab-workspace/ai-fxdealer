# OTP — Authorization Using One-Time Password

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/userguide/otp

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Getting Started](/en/docs/mt4/terminal/userguide)OTP

# OTP — Authorization Using One-Time Password

Use of OTP (One Time Password) provides an additional level of security when working with trading accounts. The user is required to enter a unique one-time password every time to connect to an account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The use of the OTP should be enabled on a trade server.</span></li><li class="p_tableatten"><span class="f_tableatten">The use of the OTP can be forced on a trade server.</span></li></ul></td></tr></tbody></table>

One-time passwords are generated in the [mobile terminal for iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader4.com "mobile terminal for iPhone") and the [mobile terminal for Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader4.com "mobile terminal for Android").

## How to enable OTP

## To start using one-time passwords, you should bind your trading account with the password generator, which are the mobile terminals for iPhone and Android.

Go to the Settings of your mobile terminal and select OTP. For security reasons, when you first open this section, you will be required to set a four-digit password. The password must be entered every time you access the password generator.

![Set a password to access the OTP generator](/en/docs/mt4/terminal/img/otp_access_pass.png "Set a password to access the OTP generator")

In the window that opens, select "Bind to account".

![Bind the account to the OTP generator](/en/docs/mt4/terminal/img/otp_bind.png "Bind the account to the OTP generator")

Next, specify the name of the server on which the trading account was opened, the account number and the master password to it. The "Bind" should be kept enabled. It must be disabled, if you are going to unbind the specified account from the generator and stop using one-time passwords.

After you tap the "Bind" button located in the upper part of the window, your trading account will be bound to the generator, and an appropriate message will appear.

![Using OTP](/en/docs/mt4/terminal/img/otp_use.png "Using OTP")

Likewise, you can bind an unlimited number of accounts to the generator.

The one-time password is displayed at the top of the OTP section. Underneath, a blue bar visualizes the password lifetime. Once the password expires, it is no longer valid, and a new password will be generated.

Additional Commands:

-   Change Password — change the generator password.
-   Synchronize Time — synchronize the time of the mobile device with the reference server. Accuracy requirement is connected with the fact that the one-time password is bound with the current time interval, and this time should be the same on the client terminal and the server side.

## How to Use OTP in the Desktop Terminal

After binding a trading account to the generator, a one-time password will be additionally requested when connecting to it from the desktop terminal:

![Authorization using OTP](/en/docs/mt4/terminal/img/otp_login.png "Authorization using OTP")

[Authorization](/en/docs/mt4/terminal/userguide/authorization)

[Live Update](/en/docs/mt4/terminal/userguide/liveupdate)