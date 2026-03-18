# Security and Certificates

> Source: https://support.metaquotes.net/en/docs/mt5/manager/account_security

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Security and Certificates

# Security and Certificates

The Manager terminal allows you to control account security: passwords and certificates for connecting to the server. Security and Certificates tabs are used for that.

## Security [#](account_security#security)

From this tab, you can manage different account passwords.

![Security](/en/docs/mt5/manager/img/account_view_security.png "Security")

Up to four types of passwords can be used for each account.

-   Master password provides full access to an account including trading functions.
-   Investor password provides access to an account without the ability to perform trades.
-   Web API password is required if the account is used for authorization via the web client written using [MetaTrader 5 Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi).
-   Phone password is used to identify an account holder while performing trade operations over phone.

To check or change a Master, Investor or Web API password, type it in the Password field. Then click Change or Check depending on the required action. Password check results are shown in a separate window after clicking Check. They are also displayed in the [Manager terminal journal](/en/docs/mt5/manager/toolbox#journal).

To create a random master password, click Generate. Next, select Change to assign the created password to your account. You can set other passwords in the same way. After generating the password, copy it into the required field.

To view a phone password, set the mouse cursor to Password field. To change it, specify a new one and click Update.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Master, investor, and Web API passwords must contain four character types: lowercase letters, uppercase letters, numbers and <a href="https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters" target="_blank" class="weblink">symbols</a> (#, @, !, etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings, while the lowest possible value is 8 characters. The maximum length is 16 characters.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Once a password is changed, the connection of an account to a trade server is reset. A reconnection with the new password is required.</span></li></ul></td></tr></tbody></table>

## Credentials [#](account_security#credentials)

This section is intended for managing advanced authentication settings, including secret keys for generating [one-time passwords](/en/docs/mt5/manager/beginning_advanced/otp) and [certificates](/en/docs/mt5/manager/beginning_advanced/extended_authorization) used for connections. Users can use separate keys (generators) and certificates for different account access modes:

-   Owner — full access to the account, including the ability to change credentials.
-   Trader — access limited to trading operations on the account and viewing its financial status.

![Credentials](/en/docs/mt5/manager/img/account_credentials.png "Credentials")

### OTP secret key

The key is a link between the account and the [one-time password generator](/en/docs/mt5/manager/beginning_advanced/otp) it is bound to. The key is a sequence of 16 characters generated based on the data about the device the MetaTrader 5 mobile platform is installed on.

Each account can be bound to only one password generator. When trying to rebind the account to a new generator, a one-time code from the previous generator should be entered.

If a user no longer has access to the bound password generator (for example, the mobile device is lost), the current OTP secret key can be deleted. In this case, account authorization via one-time passwords is disabled and the user is able to bind the account to the new generator.

If the user has forgotten the password for the password generator (PIN) while using the same mobile device, they may simply reinstall the mobile platform and rebind the account to the generator. No one-time password is required when rebinding an account to the generator on the same device.

### Certificates [#](account_security#certificate)

If [advanced authentication](/en/docs/mt5/manager/beginning_advanced/extended_authorization) using certificates is enabled for the account, the certificate details will be displayed here.

-   Certificate — information about the certificate if it has been generated or imported for the account. The certificate details include the account number, the owner name and the name of a Certificate Authority that issued the certificate. A window containing detailed information about the certificate will be opened if you click on the certificate name.

-   Confirm — enable additional [certificate confirmation](/en/docs/mt5/manager/beginning_advanced/extended_authorization#confirm) for a client group. This improves the work safety. It is impossible to log in using a certificate until it is confirmed. After a client performs necessary actions, a manager can confirm his/her certificate with this command.
-   Reset — reset a [certificate](/en/docs/mt5/manager/beginning_advanced/extended_authorization) if it has already been generated or imported for an account. It will become impossible to log in using this certificate. If certificates are generated on the server, a new one is assigned during the next account connection.
-   Import — import a certificate for an account. When clicking the button, the window for setting a certificate file (\*.cer, \*.crt) appears. The public part of a certificate is imported to the platform. When authorizing on the server, the client's certificate is compared to the one downloaded to the database. The presence of a private key in the client's certificate is additionally checked. The import function is provided for the possibility of using custom mechanisms for generating certificates.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you reset a certificate, the previously issued one becomes invalid. The next time you connect, the process of new certificate <a href="/en/docs/mt5/manager/beginning_advanced/extended_authorization#generation" class="topiclink">generation</a> and <a href="/en/docs/mt5/manager/beginning_advanced/extended_authorization#authorization" class="topiclink">authorization</a> with its help will be performed.</span></p></td></tr></tbody></table>

[Account History](/en/docs/mt5/manager/account_history)

[Trading Operations](/en/docs/mt5/manager/trading)