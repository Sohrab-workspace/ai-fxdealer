# Extended Authentication Setup

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
                -   [Group Settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings)
                -   [Group Symbol Settings](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols)
                -   [Commission Settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions)
                -   [Group Types](/en/docs/mt5/platform/administration/admin_groups/group_types)
                -   [Import of Groups](/en/docs/mt5/platform/administration/admin_groups/group_import)
                -   [Extended Authentication Setup](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication)
                -   [Position Accounting Systems](/en/docs/mt5/platform/administration/admin_groups/group_position)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Groups](/en/docs/mt5/platform/administration/admin_groups)Extended Authentication Setup

# Extended Authentication Setup

To ensure a high level of account security, the trading platform is provided with an extended authentication feature. During extended authentication, an SSL certificate is required in addition to a login and password, in order to connect to an account. This certificate can be automatically [generated](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication#server_certificates) and issued to a client during first connection to the trade server. Also, you can use your [own certificate](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication#server_certificates): generate it using third-party software, issue it to the client, and then import to the account on the trade server side.

Extended authentication features:

-   Enabled in [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#authorization).
-   Used only as an addition to [standard authentication](/en/docs/mt5/platform/administrator/getting_started/server_connect). Users need to specify their account login and password in any case.
-   Works for all account types - client, manager and administrator.

## Extended Authentication Using Certificates Generated on the Server [#](group_extended_authentication#server_certificates)

The trading platform provides a mechanism for automatic generation of client certificates. A certificate can be generated:

-   on the basis of the certificate from the license of the trading platform. The license contains a certificate especially issued by MetaQuotes Software Corp. for each individual company.
-   on the basis of any other certificate that can be used to generate certificates. Such a certificate must contain a private key.

One of these options can be selected in the "[Certificates](/en/docs/mt5/platform/administration/security/security_certificates)" section. In any case, the following requirement must be met:

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Certification Authority that has issued the certificate used to generate the client certificates must be added to the <a href="/en/docs/mt5/platform/administration/security/security_certificates#trusted" class="topiclink">trusted CA list</a>. Such a mechanism prevents from the use of fake certificates issued by unknown authorities.</span></p></td></tr></tbody></table>

![Certificates](/en/docs/mt5/platform/img/start_certificates.png "Certificates")

### Configuration of the Client Group [#](group_extended_authentication#group)

To enable the extended authentication mode for a group of clients, go to its ["Common"](/en/docs/mt5/platform/administration/admin_groups/groups_settings#authorization) tab. In the "Authentication" field select "1024-bit RSA SSL Certificate" or "2048-bit RSA SSL Certificate". The 2048-bit encryption is more secure, but the generation of the certificate is slower. In most cases, a 1024-bit encryption is sufficient.

![Enabling extended authentication using platform generated SSL certificates](/en/docs/mt5/platform/img/group_rsa_certificate.png "Enabling extended authentication using platform generated SSL certificates")

### Confirmation of Certificates [#](group_extended_authentication#confirm)

For additional security, you can enable manual confirmation of certificates generated for clients ("Enable certificate confirming" option).

The first time a user connects in the extended authentication mode, a [certificate is generated](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication#generation). However, the below restrictions apply until the generated certificate is confirmed by a manager or an administrator:

-   The account cannot be used for connection in the administrator or manager terminal.
-   In the client terminal, connection is possible only in the "investor" mode, without the possibility to trade.

After generating a certificate, a [special email](/en/docs/mt5/platform/components/trade_server/mail_templates#certificate) is sent to the terminal describing the action to be taken to confirm the certificate (for example, call the specified number and identify personality). The email appears on the ["Mailbox"](/en/docs/mt5/platform/administration/mail) tab of the Toolbox window.

After a user performs the action described in the email, an administrator/manager can confirm the certificate on the ["Security"](/en/docs/mt5/platform/administration/admin_accounts/account_edit#security) tab of the account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">For demo groups certificates are confirmed automatically immediately after they are generated.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If during certificate confirmation the user is connected to a trade server using the client terminal, the user will need to re-connect in order to switch to the full-featured operation with an account (with an access to trading functionality).</span></li></ul></td></tr></tbody></table>

### Certificate Generation [#](group_extended_authentication#generation)

When connecting to the server in the extended authentication mode, the user first completes the [standard](/en/docs/mt5/platform/administrator/getting_started/server_connect) authentication procedure by specifying the login and password. The server checks if there is a certificate for this account. If a certificate is found, the extended authentication is performed (the client certificate is checked). If it is not found, a new certificate is generated.

The trade server sends to the terminal a request to generate two keys, including a [private](https://en.wikipedia.org/wiki/Public-key_cryptography) and a [public](https://en.wikipedia.org/wiki/Public-key_cryptography) key. The private key is used for decrypting server messages. It is not sent anywhere, and is only stored in the terminal (in an encrypted form, with reference to the hardware). The public key is sent to a trade server and is saved in the client record. The trade server will use the key to encrypt messages that are sent to the terminal.

Based on the account details (client's name and account number), the server generates [a public key certificate](https://en.wikipedia.org/wiki/Digital_signature) and signs it using its private key (which guarantees that the certificate cannot be falsified). This certificate is sent to the terminal. It will be used for authenticating the user on the server, and for encrypting data sent by the terminal to the server.

Next, the terminal packs the previously generated private key and the public key certificate received from the server into one file (container) [PFX certificate](https://en.wikipedia.org/wiki/PKCS_12). The PFX is additionally protected with a password. Thus, even having obtained a PFX certificate, attackers will not be able to use it.

The password for protecting the PFX certificate is set by the user in a special dialog:

![Certificate Password](/en/docs/mt5/platform/img/certificate_password.png "Certificate Password")

The following should be specified here:

-   Password — a password to install the certificate;
-   Confirm Password — confirmation of the password to avoid errors;
-   Add certificate to the Windows System Storage — if this option is enabled, the certificate is automatically added to storage of the operating system. If you install the certificate to the system storage, then you can choose not to keep the PFX file of the certificate on the disk in the folder /terminal\_data\_folder/config/certificates. The terminal always checks the certificate both in the system storage and in the specified folder on the disk.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The password set for a certificate must contain at least two types of characters (lower case, upper case, digits and special symbols) and be no less than 5 characters long.</span></p></td></tr></tbody></table>

PFX certificate protected by the specified password is saved in the directory [/profiles/server name/certificates](/en/docs/mt5/platform/administrator/getting_started/structure#certificates) of the administrator (manager) terminals (or in the directory /config/certificates/ of the client terminal) so that it can later be moved. The names of certificates are given according to the following rule: Login\_ID\_Name.pfx, where:

-   Login is the account number;
-   ID is the short name of the company in which the account has been opened;
-   Name is the name of the client specified when creating the account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Even having obtained the *.pfx file of the certificate, you cannot use it, if you do not know the password. The minimum password length is set in the <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#minimum_password" class="topiclink">group settings</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">Certificate is generated only during the first connection of an account or in case a certificate has been <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#authorization" class="topiclink">reset</a> on the server.</span></li><li class="p_tableatten"><span class="f_tableatten">The certificate is not required when connecting using an <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#invest" class="topiclink">investor password</a>.</span></li></ul></td></tr></tbody></table>

## Extended Authentication Using Custom Certificates [#](group_extended_authentication#custom_certificates)

The trading platform allows using custom client certificates for authentication, in case it is required by your company's security policy.

To use custom certificates, disable generation of certificates in the trading platform. In the "[Certificates](/en/docs/mt5/platform/administration/security/security_certificates)" select "Issue client certificates on the basis of:disabled".

![Generation of certificates disabled](/en/docs/mt5/platform/img/start_certificates_custom.png "Generation of certificates disabled")

The list of trusted certification authorities must contain only one CA that issues the company's certificates.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Automatic generation of certificates can be disabled only for separate groups. This can be done on the <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#authorization" class="topiclink">"Common"</a> tab of a group by setting RSA Custom in the "Authentication" field.</span></p></td></tr></tbody></table>

### Configuration of the Client Group

To enable the extended authentication mode using custom certificates for a group of clients, go to the ["Common"](/en/docs/mt5/platform/administration/admin_groups/groups_settings#authorization) tab of the group settings. In the "Authentication" field, select "Custom SSL Certificate".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If automatic generation of certificates is disabled for the entire platform in the "<a href="/en/docs/mt5/platform/administration/security/security_certificates" class="topiclink">Certificates</a>" section, any mode of extended authentication (1024-bit, 2048-bit or Custom SSL Certificate) allows the use of custom certificates.</span></p></td></tr></tbody></table>

![Enabling extended authentication using third-party SSL certificates](/en/docs/mt5/platform/img/group_custom_certificate.png "Enabling extended authentication using third-party SSL certificates")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_Normal"><span class="f_tableatten">The function of additional manual confirmation is not used for custom certificates. Confirmation is performed automatically during <a href="/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication#import" class="topiclink">import of the certificate</a> to a client account.</span></p></td></tr></tbody></table>

### Issuing Certificates to Clients

When using custom certificates, their distribution among clients is the entire responsibility of the company. Certificate files must be somehow passed to clients (for example, on a digital medium, including e-token).

To use the certificate for authentication, the client must do one of the following:

-   copy the certificate file to the directory [/profiles/server name/certificates](/en/docs/mt5/platform/administrator/getting_started/structure#certificates) of the administrator (manager) terminals or in the directory /config/certificates/ of the client terminal.
-   install the certificate in the operating system storage of the computer, from which the user will work with the trading platform.
-   connect the digital storage (e-token) to the computer.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">During authentication the terminal checks the described storages of terminals. It should be noted that the necessary certificate in the folder /certificates of the terminal is searched for by the account number specified in the certificate file name. The account number must be specified at the beginning of the certificate file name, for example, 10034_JohnSmith.pfx.</span></p><p class="p_tableatten"><span class="f_tableatten">This requirement does not apply to the certificates installed in the operating system storage or a portable storage.</span></p></td></tr></tbody></table>

### Import of a Certificate into a Client Account [#](group_extended_authentication#import)

With the extended authentication, the server compares the certificate of a user with the certificate matched to his or her account on the server. If automatic generation of certificates is used on the server, the issued certificates are automatically imported into the [account](/en/docs/mt5/platform/administration/admin_accounts).

When using custom certificates, it is necessary to import them into client accounts. To do this, go to the ["Security"](/en/docs/mt5/platform/administration/admin_accounts/account_edit#security) tab of the client account and use the import function:

![Import of a certificate](/en/docs/mt5/platform/img/account_import_certificate.png "Import of a certificate")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When importing a certificate, it is automatically confirmed. The function of additional confirmation is not used for custom certificates.</span></p></td></tr></tbody></table>

[Import of Groups](/en/docs/mt5/platform/administration/admin_groups/group_import)

[Position Accounting Systems](/en/docs/mt5/platform/administration/admin_groups/group_position)