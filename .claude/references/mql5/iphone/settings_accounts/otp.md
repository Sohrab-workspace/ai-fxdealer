# OTP — Authentication Using One Time Password

> Source: https://support.metaquotes.net/en/docs/mt5/iphone/settings_accounts/otp

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
        -   [Getting Started](/en/docs/mt5/iphone/getting_started)
        -   [Quotes](/en/docs/mt5/iphone/quotes)
        -   [Depth of Market](/en/docs/mt5/iphone/depth_of_market)
        -   [Chart](/en/docs/mt5/iphone/chart)
        -   [Trade](/en/docs/mt5/iphone/trade)
        -   [History](/en/docs/mt5/iphone/history)
        -   [Accounts](/en/docs/mt5/iphone/settings_accounts)
            -   [Demo Account Opening](/en/docs/mt5/iphone/settings_accounts/account_open)
            -   [Live Account Opening](/en/docs/mt5/iphone/settings_accounts/account_real)
            -   [Account Connection](/en/docs/mt5/iphone/settings_accounts/account_connect)
            -   [Deposits and withdrawals](/en/docs/mt5/iphone/settings_accounts/payments)
            -   [Extended Authentication](/en/docs/mt5/iphone/settings_accounts/extended_authorization)
            -   [Managing Passwords](/en/docs/mt5/iphone/settings_accounts/account_passwords)
            -   [OTP](/en/docs/mt5/iphone/settings_accounts/otp)
        -   [Mailbox](/en/docs/mt5/iphone/settings_mail)
        -   [News](/en/docs/mt5/iphone/settings_news)
        -   [Messages](/en/docs/mt5/iphone/settings_messages)
        -   [Push Notifications](/en/docs/mt5/iphone/push)
        -   [Settings](/en/docs/mt5/iphone/settings)
        -   [iPad Version](/en/docs/mt5/iphone/ipad)
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

[MetaTrader 5](/en/docs/mt5)[iPhone/iPad](/en/docs/mt5/iphone)[Accounts](/en/docs/mt5/iphone/settings_accounts)OTP

# OTP — Authentication Using One Time Password

Use of OTP (one-time password) provides an additional level of security when working with trading accounts. The user is required to enter a unique one-time password every time to connect to an account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The use of OTP should be enabled on a trade server.</span></li><li class="p_tableatten"><span class="f_tableatten">The forced use of OTP can also be enabled on a trade server.</span></li></ul></td></tr></tbody></table>

One-time passwords are generated in the [mobile platform for iPhone](https://download.terminal.free/cdn/mobile/mt5/ios?hl=ru&utm_campaign=metaquotes.download&utm_source=www.metatrader5.com "mobile platform for iPhone") and [mobile platform for Android devices](https://download.terminal.free/cdn/mobile/mt5/android?hl=ru&utm_campaign=metaquotes.download&utm_source=www.metatrader5.com "mobile platform for Android").

## How to Enable OTP

To use One Time Passwords, you should bind your trading account with the password generator, which is the mobile platform for iPhone or Android devices.

Go to mobile platform Settings and select OTP. For security reasons, when you first open this section, you will be required to set a four-digit password. The password must be entered every time to access the password generator.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you forgot your password to the password generator but still use the same mobile device, reinstall the mobile platform and rebind your account to the generator. If you no longer have access to the mobile device, contact your broker to reset the binding to the password generator.</span></p></td></tr></tbody></table>

![Set a password to access the OTP generator](/en/docs/mt5/iphone/img/otp_access_pass.png "Set a password to access the OTP generator")

In the window that opens, select "Bind to account".

![Bind the account to the OTP generator](/en/docs/mt5/iphone/img/otp_bind.png "Bind the account to the OTP generator")

Next, specify the name of the server on which the trading account was opened, the account number and the master password to it. Keep the "Bind" option enabled. Disable it, if you are going to unbind the specified account from the generator and stop using One Time Passwords.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you rebind your account to another password generator, you need to enter a one-time password from the previously used generator. If you do not have access to it (for example, your mobile device is lost), contact your broker to reset the binding.</span></p></td></tr></tbody></table>

Tapping on the "Bind" button located at the top of the window binds the trading account to the generator. An appropriate message appears after that.

![Using OTP](/en/docs/mt5/iphone/img/otp_use.png "Using OTP")

Likewise, an unlimited number of accounts can be bound to the generator.

The one-time password is displayed at the top of the OTP section. A blue bar below visualizes the password lifetime. Once the password expires, it is no longer valid, and a new password will be generated.

Additional Commands:

-   Change Password — change the generator password.
-   Synchronize Time — synchronize the time of the mobile device with the reference server. Accuracy requirement is connected with the fact that the one-time password is bound with the current time interval, and this time should be the same on the platform and the server side.

## How to Use OTP in the Desktop Platform

After linking to the generator, each time you attempt to connect to your account via the desktop or web platform, or through another mobile application, you will be prompted to enter a one-time password:

![Authorization using OTP](/en/docs/mt5/iphone/img/otp_login.png "Authorization using OTP")

[Managing Passwords](/en/docs/mt5/iphone/settings_accounts/account_passwords)

[Mailbox](/en/docs/mt5/iphone/settings_mail)