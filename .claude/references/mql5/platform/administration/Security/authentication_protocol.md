# MetaTrader 5 Authentication Protocols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/security/authentication_protocol

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
                -   [Certificates](/en/docs/mt5/platform/administration/security/security_certificates)
                -   [Firewall](/en/docs/mt5/platform/administration/security/admin_access)
                -   [Anti DDoS Protection](/en/docs/mt5/platform/administration/security/network_anti_ddos)
                -   [Authentication Protocols](/en/docs/mt5/platform/administration/security/authentication_protocol)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Security](/en/docs/mt5/platform/administration/security)Authentication Protocols

# MetaTrader 5 Authentication Protocols

All client connections in MetaTrader 5 (trader, manager and administrator) can use three types of authentication:

### 1\. Mandatory standard authentication

Standard authentication checks the client's password and is required for all types of accounts.

The client login is an unsigned integer number in the range between 1 and 18,446,744,073,709,551,615. The password is a string consisting of 8 to 16 characters. The minimum password length is configured in the [properties of the group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#minimum_password) to which the client belongs.

The system controls the complexity of all used passwords. A password must contain at least two of three types of characters: lowercase letters, uppercase letters and digits.

The password is stored on the trading platform as a hash of the password and additional data.

On user terminals, the password is protected with and encryption key, which is derived from the fingerprint of the client computer (processor serial code, hard drive, OS etc.). When migrating trading account configuration files to a different computer, saved passwords are automatically deleted, because the device fingerprint changes. All password fields are protected from being spied/copied/retrieved.

The entire authentication mechanism is implemented on the server side.

Authentication consists of three stages:

1.  A client is authenticated by the server. In response to an initialization command, the server sends to a terminal a random sequence, which should be signed by a client using a 128-bit key from the client password hash and then should be sent back to the server. The server performs similar actions on its side, compares signatures and verifies the client authenticity.
2.  A server is authenticated by the client. After completing the first step, the client checks if the client password is known to the server by generating and sending a random sequence, which is then signed by the server and checked.
3.  A channel encryption key is formed. If the first two steps are successfully completed, the server generates a 2048-bit channel encryption key as a derivative of a random value, the client password derivative and session data.

MD5, SHA256 and AES algorithms are used during standard authentication.

After a standard authentication procedure, an extended validation by SSL certificates and/or OTP (One Time Password) authentication can be performed. These three authentication methods can be all enabled to complement each other.

### 2\. Advanced Authentication

The server supports [advanced authentication](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication), which is completely analogous to the SSL authentication. This type of authentication uses SSL certificates in the PKCS#12 (.pfx) storage format for Microsoft Windows.

It supports both existing certificates issued by certificate authorities and certificates generated by the trade server.

On the client side, certificates can be stored in the file system, as well as installed in the standard Windows certificate store or in additional storage devices such as external eToken etc.

### 3\. One Time Password Authentication

The use of [one-time passwords](/en/docs/mt5/platform/administration/admin_groups/groups_settings#otp) can be additionally enabled. In this case, users are required to enter a special one-time password every time they connect to their accounts.

One-time passwords are generated in the MetaTrader 5 terminals for iOS or Android. The terminals generate one-time passwords using the HMAC/TOTP SHA-256 algorithm based on the OTP secret.

An issued one-time password is valid for 30 seconds. The server checks the sent one-time password using the OTP secret and the current time. Therefore< in order to provide a proper operation of the OTP authentication procedure, the mobile terminal and the trade server synchronize time with time servers.

An OTP secret is sent to a server over a 2048-bit key encrypted channel after a basic authentication, during the initial bounding of the mobile terminal to the trading account.

## Protocol of interaction between the system components

All components of the system communicate with each other using their own binary compressed and encrypted data channel with a 2048-bit key.

In addition, server components can use the following protocols:

-   An HTTPS protocol for receiving [platform updates](/en/docs/mt5/platform/administration/admin_update) from the https://updates.metaquotes.net website. The website certificate issued by Sectigo Limited is verified. All update components are signed by MetaQuotes Ltd certificate, which is validated by COMODO CA. The signature is validated in all platform components before the update.
-   TIME/NTP time synchronization protocols, if [time synchronization](/en/docs/mt5/platform/administration/admin_time) is enabled on the server.
-   SMTP and ESMTP if delivery of end-of-day client [trading reports](/en/docs/mt5/platform/components/trade_server/daily_reports) is enabled.

## Audit actions in the client and administrator consoles

All actions of the platform servers, as well as actions of traders, managers and administrators are logged on the server side and in terminals. All logs are provided with a built-in integrity control. If any of log entries is deleted or modified, the first modified position will be highlighted in red in the log viewing mode.

For each client connection, the following details are written to the log: time, IP address, terminal type, client's login and computer ID (CID — Computer ID derived from the computer software and hardware characteristics). Details of all performed operations are displayed in logs.

Last connection time and IP are written in the client record details on the server. After a successful authentication, the time and IP address of the previous successful connection are additionally recorded in the client terminal's local journal.

## Additional security options

A variety of additional security measures are available for all platform components:

1.  All MetaTrader 5 program components (.exe and .dll files) are provided with:
    -   MetaQuotes Ltd digital signature to guarantee authorship and the invariability of files;
    -   Built-in protection against modification, hacking or debugging.
2.  All databases of saved accounts (except authentication data, which is stored separately in the [credentials.dat](/en/docs/mt5/platform/components/trade_server/trade_server_structure) file) and trade operation history on the client side are encrypted using a key derived from the client computer, making it impossible to use these databases in case of possible hacking or migration to another computer.
3.  Server-side databases, including account and trade history databases, are not encrypted due to high performance requirements. Decryption during each database access would significantly slow down the platform performance, which is critical when handling trading operations. The only exceptions are the database with the account authentication data (passwords, OTP tokens, and SSL certificates), databases for [internal emails](/en/docs/mt5/platform/administration/mail), the [payment system](/en/docs/mt5/platform/administration/payments), and files used for [clients](/en/docs/mt5/platform/administration/clients) (documents submitted during account opening, files attached to comments, etc.). These databases are encrypted using a proprietary encryption algorithm based on [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).
4.  In addition to using a 2048-bit encrypted data transfer channel, each trading order is additionally signed using a derivative from the client's password. During advanced authentication, a private SSL key of the client's certificate is used in the signature.
5.  The server cluster is provided with a built-in [anti DoS and DDoS protection](/en/docs/mt5/platform/components/access_server/access_server_antiflood) based on the analysis of connection frequency and actions performed.
6.  The server cluster has its own configurable [firewall](/en/docs/mt5/platform/administration/security/admin_access) to control access to the cluster.
7.  Connection of all server components inside the MetaTrader 5 cluster is controlled based on the [IP address, login and password](/en/docs/mt5/platform/administration/admin_network/network_add_edit#identifier), similar to the standard authentication scheme.
8.  Each administrator/manager of the system is provided with an advanced [system of permissions](/en/docs/mt5/platform/administration/admin_managers#permissions) with a double control on the administrator/manager and the server side.
9.  Connection of the managers and administrators of the cluster can be [limited to a range of addresses](/en/docs/mt5/platform/administration/admin_managers#access_list) specified in the manager configuration settings.

[Anti DDoS Protection](/en/docs/mt5/platform/administration/security/network_anti_ddos)

[Automations](/en/docs/mt5/platform/administration/automation)