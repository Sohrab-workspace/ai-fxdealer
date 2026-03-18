# Extended Authentication

> Source: https://support.metaquotes.net/en/docs/mt5/client/start_advanced/extended_authorization

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)[For Advanced Users](/en/docs/mt5/client/start_advanced)Extended Authentication

# Extended Authentication

The trading platform provides an option of extended authentication using SSL certificates, which greatly increases the safety of the system. The extended authentication can be enabled on the server. When it is enabled, [the standard authentication](/en/docs/mt5/client/authorization) is still active. In any case, users need to enter their account details.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The authorization algorithm is generally accepted and secure. It is fully analogous to the SSL authentication.</span></li><li class="p_tableatten"><span class="f_tableatten">Connection between the client and server is established over a custom protocol with the encryption of all data transmitted.</span></li><li class="p_tableatten"><span class="f_tableatten">A public key can be freely distributed and used to verify the message signed using the secret key. It is guaranteed, that knowing a public key, it is impossible to compute the secret key within a reasonable time. The calculation of a secret key based on a public one, even on powerful modern computers, can take tens or even hundreds of years.</span></li></ul></td></tr></tbody></table>

## Order of Generating and Receiving a Certificate [#](extended_authorization#generation)

When trying to login using an account with the extended authentication, you will need to go through [standard authentication](/en/docs/mt5/client/authorization). After that, the trade server sends a request to the trading platform to generate two keys: private and public. The public key is sent to the trade server.

Based on the account data, the server generates a certificate and signs it with its private key (the server's private key signature guarantees that the certificate cannot be falsified). After that a window appears in the trading platform, in which you need to enter the password to protect the certificate:

![Before generating a certificate, a protective password needs to be specified](/en/docs/mt5/client/img/certificate_password.png "Before generating a certificate, a protective password needs to be specified")

The following fields and settings are available in this window:

-   Password — a password for the certificate installation;
-   Confirm password — confirmation of the password to avoid mistyping;
-   Add the certificate to the Windows storage — if this option is enabled, the certificate is automatically installed to the operating system storage. If you install the certificate to the system storage, then you can choose not to keep the PFX file of the certificate on the hard disk in the folder /platform\_folder/config/certificates. The platform checks the certificate in the system storage or in the specified folder on the hard disk.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The password for the certificate must contain at least two types of symbols (lower case, upper case, digits), and be at least 5 characters long.</span></p></td></tr></tbody></table>

After the required data are specified, press "Continue". The certificate is packed and protected by the specified password. The resulting certificate file \*.pfx is stored in [/platform\_folder/config/certificates](/en/docs/mt5/client/start_advanced/structure#certificate), from which it can be relocated later. The certificate files are named according to the following rule: Login\_ID\_Name.pfx, where:

-   Login is the account number;
-   ID is a short name of the company the account was opened in;
-   Name is the name of a client specified when creating the account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Even having access to the *.pfx file, the certificate cannot be used without the password.</span></li><li class="p_tableatten"><span class="f_tableatten">Certificates are generated only during the first account connection or when a certificate is intentionally reset on the server.</span></li><li class="p_tableatten"><span class="f_tableatten">The certificate is not required when connecting using an investor password.</span></li></ul></td></tr></tbody></table>

## Authentication [#](extended_authorization#authorization)

Further, each time you connect in the extended authentication mode, you will need to enter the certificate password together with the main account details:

![In the extended authentication mode additionally specify the certificate password](/en/docs/mt5/client/img/extended_authorization.png "In the extended authentication mode additionally specify the certificate password")

## Confirmation of Certificates [#](extended_authorization#confirm)

An additional mode of certificate confirmation can be enabled on the server to significantly increase the safety of the platform. Until the certificate is confirmed, connection is only possible in the investor mode without the possibility to trade.

In this mode, after a certificate is received, a special email is sent to the platform, describing actions to be taken to confirm the certificate (for example, call the number specified and confirm user identity). The email can be viewed on the [Mailbox](/en/docs/mt5/client/start_advanced/mail) tab of the Toolbox window.

Once the certificate is confirmed, a user can trade from this account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">For demo accounts, certificates are confirmed automatically straight after generation.</span></li><li class="p_tableatten"><span class="f_tableatten">After the certificate has been confirmed, it's necessary to reconnect using the account details.</span></li></ul></td></tr></tbody></table>

## Move Certificates to Another PC

To connect to an account with an extended authentication, a user requires a [certificate](/en/docs/mt5/client/start_advanced/extended_authorization#generation). To work with the account on several computers or on a new computer, you need to move/copy the certificate.

To move the certificate, copy its PFX file from [/platform\_folder/config/certificates](/en/docs/mt5/client/start_advanced/structure#certificate) of the source computer to the same folder on the target computer.

## Transferring the Certificates to a Mobile Device [#](extended_authorization#transfer_mobile)

If the certificate was requested and generated via the desktop platform, you should transfer it to your iPhone/iPad or Android device if you want to be able to enter your account via that device.

### Transfer

The certificate is transferred securely via a trading server:

-   First, the certificate is encrypted in the desktop platform: an account owner sets the password to encrypt the certificate using a reliable AES-256 algorithm. The password is not sent to the server ensuring that only the user knows it.
-   Next, the encrypted certificate is sent to the trade server where it is stored before receipt via a mobile platform (but no more than an hour).
-   In order to receive the certificate, the user should connect to the account via the mobile platform, After connecting, the user will be offered to import the certificate. To do this, they should enter the password that was used to encrypt the certificate in the desktop platform.

The certificate transfer is secure: the trading server is used solely as an intermediate storage, while encryption is performed at the user's side. The certificate password is not transferred or stored on the trade server.

### How to transfer the certificate

Connect to the account via the desktop platform and select "Transfer SSL certificate to mobile device" in its context menu:

![Transferring the certificate to a mobile device](/en/docs/mt5/client/img/transfer_certificate.png "Transferring the certificate to a mobile device")

Specify the master password of the account to confirm that it belongs to you. Next, set the password to be used to protect the certificate before sending it to the server or use an automatically generated random password. The password should consist of at least 8 digits.

After successfully sending the certificate to the server, open the mobile platform and connect to the account. You will be immediately offered to import the certificate. Agree and enter the password you have set during the transfer.

![Importing the certificate to a mobile device](/en/docs/mt5/client/img/transfer_certificate_import.png "Importing the certificate to a mobile device")

You can view the certificate in About – Certificates.

### Alternative transfer option

You can transfer the certificate manually:

-   iPhone/iPad — [via iTunes](https://www.metatrader5.com/en/mobile-trading/iphone/help/settings/settings_accounts/extended_authorization)
-   Android — [copying to a device](https://www.metatrader5.com/en/mobile-trading/android/help/settings_accounts/extended_authorization)

## View Certificates [#](extended_authorization#certificate_view)

To view a certificate used for the account in the [extended authentication](/en/docs/mt5/client/start_advanced/extended_authorization) mode click on "Certificate" on the [Server](/en/docs/mt5/client/settings#server) tab.

![Click on a certificate on the server tab to view its details](/en/docs/mt5/client/img/certificate_view.png "Click on a certificate on the server tab to view its details")

The following certificate details are displayed here:

-   Issued to — the account number and certificate holder name.
-   Issued by — the name of the company that issued the certificate.
-   Valid from — certificate validity period.

## Certificate Export [#](extended_authorization#export)

[The public part of the certificate](/en/docs/mt5/client/start_advanced/extended_authorization#generation) (without the private key) can be exported to a file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Do not submit your certificate pfx file containing the private key to anyone. This file is generated during the first connection in the <a href="/en/docs/mt5/client/start_advanced/extended_authorization" class="topiclink">extended authentication</a> mode and is stored in /platform_folder/config/certificates.</span></p></td></tr></tbody></table>

To export the public part of your certificate, move to the Details tab and click "Copy to File":

![To export the public part of the certificate, click Copy to File in Details](/en/docs/mt5/client/img/certificate_details.png "To export the public part of the certificate, click Copy to File in Details")

Follow the instructions of Certificate Export Wizard. Select the file format for export after the greeting message:

![Select the certificate file format to export](/en/docs/mt5/client/img/certificate_export.png "Select the certificate file format to export")

Specify a file name and complete the export process.

## Extended Authentication Restrictions

The extended authentication option cannot be used in the [web platform](https://www.mql5.com/en/articles/3024) and in the [Signals service](/en/docs/mt5/client/signals). If extended authentication is used on an account, you cannot connect to this account via the web platform or register it to provide trading signals. However, copying of signals to an account with extended authentication is possible.

[Platform Start](/en/docs/mt5/client/start_advanced/start)

[One Time Passwords - 2FA/TOTP](/en/docs/mt5/client/start_advanced/otp)