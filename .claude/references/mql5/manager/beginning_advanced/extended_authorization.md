# Extended Authentication

> Source: https://support.metaquotes.net/en/docs/mt5/manager/beginning_advanced/extended_authorization

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
            -   [Installing the Terminal](/en/docs/mt5/manager/beginning_advanced/installation)
            -   [Files and Folders](/en/docs/mt5/manager/beginning_advanced/structure)
            -   [Extended Authentication](/en/docs/mt5/manager/beginning_advanced/extended_authorization)
            -   [One Time Passwords - 2FA/TOTP](/en/docs/mt5/manager/beginning_advanced/otp)
            -   [Auto Update](/en/docs/mt5/manager/beginning_advanced/liveupdate)
            -   [Data Export](/en/docs/mt5/manager/beginning_advanced/export)
            -   [Terminal Deinstallation](/en/docs/mt5/manager/beginning_advanced/deinstallation)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[For Advanced Users](/en/docs/mt5/manager/beginning_advanced)Extended Authentication

# Extended Authentication

The trading platform provides the option of extended authorization using SSL certificates, which greatly increases the safety of the system. The extended authentication can be enabled on the server. When it is enabled, [the standard authorization](/en/docs/mt5/manager/connect) is still active. In any case, users need to enter their account details.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The authorization algorithm is standard and highly reliable, it is completely similar to SSL authentication.</span></li><li class="p_tableatten"><span class="f_tableatten">Connection between the client and server is held over its own protocol with the encryption of all data transmitted.</span></li><li class="p_tableatten"><span class="f_tableatten">A public key can be freely distributed and used to authenticate the message, which is signed using a secret key. It is guaranteed that knowing the public key, it is impossible to compute the secret key within a reasonable time. Calculation of the secret key based on the public one, even on powerful up-to-date computers, can take tens or hundreds of years.</span></li></ul></td></tr></tbody></table>

## Generating and receiving a certificate [#](extended_authorization#generation)

When trying to authorize using an account with the extended authorization enabled, you will need to go through [standard authorization](/en/docs/mt5/manager/connect) first. After that, the trade server sends a request to the manager terminal to generate two keys: private and public. The public key is sent to the trade server.

Based on the account data, the server generates a certificate and signs it with its private key (the server's private key signature guarantees that the certificate cannot be falsified). After that, a window appears in the terminal, in which you need to specify a password to protect the certificate:

![Certificate password](/en/docs/mt5/manager/img/certificate_password.png "Certificate password")

The following fields and settings are available in this window:

-   Password — password for the certificate installation;
-   Confirm password — confirmation of the password to avoid mistyping;
-   Add the certificate to the Windows storage — if enabled, the certificate is automatically installed to the operating system storage. If you install the certificate to the system storage, you can choose not to keep the PFX file of the certificate on the hard disk in \[terminal folder\]/base/\[server name\]/certificates. The terminal checks the certificate in the system storage or in the specified folder on the hard disk.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A password set to the certificate should contain at least two types of characters (lower case letters, upper case letters, numbers or special characters) and consist of not less than five characters.</span></p></td></tr></tbody></table>

After all of the required data are specified, tap Continue. After that, the certificate is packed and protected by the specified password. The resulting \*.pfx file of the certificate is saved in [\[terminal folder\]/bases/\[server name\]/certificates](/en/docs/mt5/manager/beginning_advanced/structure#certificate) to enable its further transfer. Names to the certificate files are assigned according to the following rule: Login\_ID\_Name.pfx, where:

-   Login is an account number;
-   ID — short name of a company an account was created in;
-   Name — name of a manager specified when creating an account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Even getting *.pfx file of the certificate, one will not be able to use it without the password.</span></li><li class="p_tableatten"><span class="f_tableatten">Certificates are generated only the first time an account is connected, or if the certificate was intentionally reset on the server.</span></li><li class="p_tableatten"><span class="f_tableatten">The certificate is not checked, if an <a href="/en/docs/mt5/manager/account_security#invest" class="topiclink">Investor Password</a> is used.</span></li></ul></td></tr></tbody></table>

## Authentication [#](extended_authorization#authorization)

Further, each time you connect in the extended authentication mode, you will need to enter the certificate password together with the main account details:

![Extended authentication](/en/docs/mt5/manager/img/extended_authorization.png "Extended authentication")

## Confirmation of certificates [#](extended_authorization#confirm)

An additional mode of certificate confirmation can be enabled on the server - this greatly increases the safety of the platform. Connection will be impossible until the generated certificate is confirmed.

In this mode, after a certificate is received, a special letter is sent to the terminal, describing actions to be taken to confirm the certificate (for example, call the number specified and confirm your identity). The letter can be viewed on the [Mailbox](/en/docs/mt5/manager/communication#mailbox) tab of the Toolbox window.

Once the certificate is confirmed, the manager can connect to the server and start working.

## Moving certificates to another computer

To connect to an account with an extended authentication, a user requires a certificate. To work with the account on several computers or on a new computer, you need to move/copy the certificate.

To move the certificate, copy its pfx file from \[terminal folder\]/bases/\[server name\]/certificates of a source computer to the same folder on a target computer.

[Files and Folders](/en/docs/mt5/manager/beginning_advanced/structure)

[One Time Passwords - 2FA/TOTP](/en/docs/mt5/manager/beginning_advanced/otp)