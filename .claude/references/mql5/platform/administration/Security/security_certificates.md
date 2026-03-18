# Certificates

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/security/security_certificates

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Security](/en/docs/mt5/platform/administration/security)Certificates

# Certificates

Security certificates are used for advanced authentication in the trading platform. This authentication type allows improving the system operation security. For more details please read a [separate section](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication).

Here you can configure certificates.

![Certificates](/en/docs/mt5/platform/img/certificates.png "Certificates")

Specify how certificates will be generated:

-   on the basis of license — by default, client certificates are generated on the basis of a license issued by MetaQuotes Software Corp. when you purchase the platform. The license file contains a unique certificate created for the brokerage company, based on which all client certificates are generated.
-   on the basis of certificate — a brokerage company can use its own certificate to generated client certificates. Upon the selection of this option a window for selecting of a pfx certificate opens. The certificate file must contain a private key. The certification issuer must be added to the [trusted](/en/docs/mt5/platform/administration/security/security_certificates#trusted) list.
-   disabled — this option disables the generation of certificates. However, this does not mean that the [extended authentication](/en/docs/mt5/platform/administration/admin_groups/groups_settings#authorization) will become unavailable. In this case, the client will not be able to receive a certificate automatically when connecting to the account. The brokerage company will need to issue a certificate to the user specifically (for example, on an e-token), and then link the certificate to an account in the trading platform. To link a certificate, import it via the [Security](/en/docs/mt5/platform/administration/admin_accounts/account_edit#security) tab of this account.

## Certificate Requirements

The following requirements must be fulfilled when using the company's own certificates:

-   The certification authority that issued the certificate must be added to the [trusted](/en/docs/mt5/platform/administration/security/security_certificates#trusted) list.
-   A certificate issued to a client must contain a private key.
-   The client must add the issued certificate to the /certificates folder of the terminal, install it to the operating system storage or upload it to an e-token.

## Trusted Authorities [#](security_certificates#trusted)

When authorizing on the server with a certificate, the certification authority is checked. Authorization is allowed only using certificates issued by trusted authorities. By default, such an authority is a certificate from the trading platform license that is used to generate client certificates.

To add a certification authority, click the appropriate button and specify the \*.cer or \*.crt file. If necessary, any of the previously added centers can be disconnected at any time.

[Security](/en/docs/mt5/platform/administration/security)

[Firewall](/en/docs/mt5/platform/administration/security/admin_access)