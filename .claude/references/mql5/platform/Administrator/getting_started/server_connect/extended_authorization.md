# Extended Authorization

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
            -   [Install Terminal](/en/docs/mt5/platform/administrator/getting_started/administrator_installation)
            -   [Start Terminal](/en/docs/mt5/platform/administrator/getting_started/launch)
            -   [Structure of Directories and Files](/en/docs/mt5/platform/administrator/getting_started/structure)
            -   [Add or Remove Servers](/en/docs/mt5/platform/administrator/getting_started/server_add_delete)
            -   [Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)
                -   [Extended Authorization](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization)
                -   [2FA/TOTP](/en/docs/mt5/platform/administrator/getting_started/server_connect/otp)
            -   [Change Password](/en/docs/mt5/platform/administrator/getting_started/change_password)
            -   [Live Update](/en/docs/mt5/platform/administrator/getting_started/live_update)
            -   [Uninstall Terminal](/en/docs/mt5/platform/administrator/getting_started/deinstallation)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
        -   [Terminal Settings](/en/docs/mt5/platform/administrator/settings)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Getting Started](/en/docs/mt5/platform/administrator/getting_started)[Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)Extended Authorization

# Extended Authorization

The trading platform offers the possibility of an extended authorization using SSL certificate which considerably increases the system security. The extended authorization is enabled in [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#authorization). If this connection mode is enabled, [standard authorization](/en/docs/mt5/platform/administrator/getting_started/server_connect) is still enabled too. It means that a user will have to enter account details in any authorization mode.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The authorization algorithm is generally accepted and secure. It is fully analogous to the SSL authorization. &nbsp;</span></li><li class="p_tableatten"><span class="f_tableatten">Connection between a terminal and a server is established by a custom protocol with the encryption of all the data transmitted.</span></li><li class="p_tableatten"><span class="f_tableatten">A public key can be freely distributed and used for verifying the message signed by the secret key. It is guaranteed that knowing a public key it is impossible to count the secret one within reasonable time. The calculation of a secret key based on a public one even with powerful computers can take tens or even hundreds of years.</span></li><li class="p_tableatten"><span class="f_tableatten">A detailed description of the entire process of the extended authorization is given in a <a href="/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication" class="topiclink">separate section</a>.</span></li></ul></td></tr></tbody></table>

## Generating and Getting a Certificate [#](extended_authorization#generation)

At the attempt to authorize through an account from a group with the enabled extended authorization, the [standard authorization](/en/docs/mt5/platform/administrator/getting_started/server_connect) must be performed first. After that a trade server sends a request to an administrator terminal for the generation of two keys: private and public. A public key is sent to a trade server.

Based on the account data, a server generates a certificate and signs it by its private key (signing of a certificate by a server's private key guarantees that the certificate can't be falsified). After that a window appears in the administrator terminal, where the password must be indicated to protect the certificate:

![Certificate Password](/en/docs/mt5/platform/img/certificate_password.png "Certificate Password")

The following fields and parameters are available in this window:

-   Password —  password for the certificate installation;
-   Confirm Password — password confirmation to eliminate errors;
-   Add certificate to the Windows System Storage — if this option is enabled, the certificate will be automatically added to the operating system storage.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The password for the certificate must contain at least two types of symbols (lower case, upper case, digits), and be at least 5 symbols long.</span></p></td></tr></tbody></table>

After all the required data are specified, press "Continue". After that the certificate is packed and protected by the specified password. The resulting \*.pfx file of the certificate is saved in [/profiles/server name/certificates](/en/docs/mt5/platform/administrator/getting_started/structure#certificates) of the administrator terminal to enable its further relocation. Certificate files are named according to the following rule: Login\_ID\_Name.pfx, where:

-   Login — account number;
-   ID — short company name where the account is opened;
-   Name — client's name specified during account creation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Even getting access to the *.pfx file one can't use the certificate without the password. The minimum length of a password is set in <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#minimum_password" class="topiclink">group settings</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">Generation of certificates is performed only during the first account connection or when a certificate was intentionally <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#authorization" class="topiclink">reset</a> on the server.</span></li><li class="p_tableatten"><span class="f_tableatten">The certificate is not required when connecting using an <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#invest" class="topiclink">investor password</a>.</span></li></ul></td></tr></tbody></table>

## Authorization [#](extended_authorization#authorization)

In further attempts to connect with the extended authorization, the certificate password will be required together with the main account details:

![Extended Authorization](/en/docs/mt5/platform/img/extended_authorization.png "Extended Authorization")

## Confirmation of Certificates [#](extended_authorization#confirm)

The additional mode of [certificate confirmation](/en/docs/mt5/platform/administration/admin_groups/groups_settings#confirm) can be enabled on a server — this considerably increases the platform operation security. Until the certificate is confirmed, connection using the account in a manager or administrator terminal is impossible, while connection in a client terminal can be established only in the investor mode without the possibility to trade.

In this mode, after a certificate is received, a [special email](/en/docs/mt5/platform/components/trade_server/mail_templates#certificate) is sent to the terminal describing actions that must be taken to confirm the certificate (for example, call at the specified number and identify a person). The email can be viewed on the ["Mailbox"](/en/docs/mt5/platform/administration/mail) tab of the "Toolbox" window.

Once a client or manager performs the actions specified in the email, the administrator can confirm the certificate of the account on the ["Security"](/en/docs/mt5/platform/administration/admin_accounts/account_edit#security) tab.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">For demo accounts the certificate confirmation is performed automatically, as soon as the certificate is generated.</span></li><li class="p_tableatten"><span class="f_tableatten">After the certificate has been confirmed, the reconnection using account details is necessary in the client terminal.</span></li></ul></td></tr></tbody></table>

[Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)

[2FA/TOTP](/en/docs/mt5/platform/administrator/getting_started/server_connect/otp)