# Web Services

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_web_services

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
                -   [Finteza Analytics](/en/docs/mt5/platform/administration/integration/integration_finteza)
                -   [Sponsored VPS](/en/docs/mt5/platform/administration/integration/integration_vps)
                -   [Mail Servers](/en/docs/mt5/platform/administration/integration/integration_mail)
                -   [SMS Gateways](/en/docs/mt5/platform/administration/integration/integration_sms)
                -   [Messengers](/en/docs/mt5/platform/administration/integration/integration_messenger)
                -   [KYC](/en/docs/mt5/platform/administration/integration/integration_kyc)
                -   [Event Streaming](/en/docs/mt5/platform/administration/integration/integration_streaming)
                -   [Web Services](/en/docs/mt5/platform/administration/integration/integration_web_services)
            -   [Security](/en/docs/mt5/platform/administration/security)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)Web Services

# Web Services

The trading platform offers extensive opportunities for integration with brokerage websites and web services, as well as for integration with additional service providers. This functionality is implemented via the [MetaTrader 5 Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi). By using integrations, you can create trader rooms on your website, to which data on trading operations will be sent from the platform, as well as implement registration, account top-up and other options.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The <a href="https://support.metaquotes.net/en/market/mt5/integration" target="_blank" class="weblink">App Store</a> features a plethora of ready-made web integration solutions from professional developers.</span></p></td></tr></tbody></table>

## SSL Certificates [#](integration_web_services#ssl)

Support for connection over HTTPS is implemented on access servers (HTTP is not connected). Therefore, they can act as a web server. This allows sending to a server [Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi_https) commands as usual GET and POST requests.

To enable connection to the access server via HTTPS, at least one of its [public addresses](/en/docs/mt5/platform/administration/admin_network/network_add_edit#public) must be associated with a certain domain, i.e. the host to which POST and GET requests will be implemented. For this purpose, the appropriate entry must be specified on the DNS server. For example, if you want to implement operation via the host abc.broker.com, the following entry should be added to DNS

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">abc.broker.com&nbsp;3600&nbsp;IN&nbsp;A&nbsp;XXX.XXX.XXX.XXX</span><br><span class="f_CodeExample">abc.broker.com&nbsp;3600&nbsp;IN&nbsp;AAAA&nbsp;XXXX:XXXX:X:XX:XX</span></p></td></tr></tbody></table>

Here XXX is the public IPv4 or IPv6 address of the Access server.

Since only protected TLS connections (HTTPS) are supported, an SSL certificate must be installed on the access server for the appropriate domain. Use the "Integration \\ Web Services \\ SSL Certificates" section to upload and manage certificates:

![Configuring SSL certificates for connecting to an access server via HTTPS](/en/docs/mt5/platform/img/network_add_ssl.png "Configuring SSL certificates for connecting to an access server via HTTPS")

There are three ways to upload a certificate to the platform:

-   Using a pre-made pfx file
-   By generating a self-signed certificate (can only be used for testing)
-   By generating a certificate via the [Let's Encrypt](https://letsencrypt.org/) service

The type of the certificate used is shown in a tooltip when you hover over its line.

SSL settings apply to all access servers. Changes in the list of certificates are applied instantly, so you do not need to restart the servers.

Connections from multiple domains can be supported on one server ([the SNI mode](https://en.wikipedia.org/wiki/Server_Name_Indication)). In this case, the corresponding SSL certificate must be installed for each of them. When connecting, the client specifies the address to connect to. The access server checks all installed certificates and automatically provides the necessary one to the client:

-   First, the server tries to find a certificate for an exact match domain.
-   If not, it tries to find the most suitable one using mask "\*".
-   If the certificate could not be found, the server returns the first certificate from the list.

After making changes to the list of certificates, click "Apply" on the toolbar.

One month before the certificate expiration date, its line is highlighted in red. The appropriate warning is displayed on the platform [start page](/en/docs/mt5/platform/administration/admin_start) as well.

### Adding a certificate from a PFX file [#](integration_web_services#pfx)

Click PFX and specify the path to the file. The certificate can be password protected. In this case, you will be prompted to enter the password.

### Adding a self-signed certificate [#](integration_web_services#selfsigned)

The trading platform allows the issuing of self-signed SSL certificates. Such certificates can be used to test applications written using the [MetaTrader 5 Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi). Unlike a certificate issued by a trusted authority, a self-signed certificate can be obtained instantly and free of charge. However, it cannot be used for operations in a real environment since the connection will not be trusted — for this reason, browsers and apps will return warnings.

Click "Add \\ Self-signed" and specify the domain, your company name, certificate expiration date, and encryption algorithm:

-   Elliptic Curve Cryptography (ECC) with a 256 or 384 bit key.
-   RSA with a 2048 or 4096 bit key

![Issuing a self-signed certificate](/en/docs/mt5/platform/img/self_signed_certificate.png "Issuing a self-signed certificate")

The generated certificate will be added to the platform. A self-signed certificate must be associated with at least one public address of any of your Access servers using a DNS record. For further details please read the [SSL certificates](/en/docs/mt5/platform/administration/integration/integration_web_services#ssl) section.

Self-signed certificates are not automatically renewed. Upon expiration, you need to generate and upload a new certificate.

### Adding a Let's Encrypt certificate [#](integration_web_services#letsencrypt)

[Let's Encrypt](https://letsencrypt.org/) is a certificate authority which enables free automatic issuing of SSL certificates. You can obtain a ready-made certificate from this service right in the platform. Let's Encrypt certificates are trusted by most browsers and operating systems. Accordingly, a non-trusted domain warning will not be displayed for your clients upon connection.

How the certificate is issued

1.  The platform makes the first request to Let's Encrypt and receives the initial data for issuing a certificate.
2.  The platform (its main trading server) generates keys for the new certificate. The private key is not transfered to Let's Encrypt, to Access servers or to anywhere else.
3.  For security purposes, Let's Encrypt verifies that the certificate is issued by the real domain owner. The service uses several confirmation methods to verify that: [https://letsencrypt.org/docs/challenge-types/](https://letsencrypt.org/docs/challenge-types/). MetaTrader 5 uses the TLS-ALPN-01 option:
    1.  A domain validation certificate is generated on the platform side and is distributed to all Access servers.
    2.  Using a separate SSL protocol, Let's Encrypt connects to port 443 on all IP addresses specified in the DNS for the domain name. Having connected, the service receives and checks the certificate which contains the verifiable data. It is very important that all IP addresses associated with the domain, point to the Access servers in your cluster. All Access servers must be operational and available for verification. They must be configured to listen and accept connections to port 443.
4.  The platform waits for Let's Encrypt to complete the verification. After successful verification, the platform receives the issued certificate. The certificate is installed in the platform

Preparing to receive the certificate

To issue a certificate, Let's Encrypt checks the IP addresses specified for your domain. Therefore, before proceeding with the certificate issuing, correctly configure the DNS server as described in the [SSL Certificates](/en/docs/mt5/platform/administration/integration/integration_web_services#ssl) section. All addresses must point exactly to the Access servers of your cluster.

Also please note that after you add a DNS record, it takes some time for them to propagate across the Internet. You can check which IP address a domain is pointing to using the "nslookup" command. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">nslookup&nbsp;abc.broker.com</span></p></td></tr></tbody></table>

Make sure that the domain is associated with the correct address and proceed to add the certificate in the platform. Click "Add \\ Let's Encrypt" and specify the domain, your company name, and the encryption algorithm:

-   Elliptic Curve Cryptography (ECC) with a 256 or 384 bit key.
-   RSA with a 2048 or 4096 bit key

Also make sure that the option "Issue a free and automatically renewable Let's Encrypt certificate" is enabled.

Domain name requirements:

-   The name must contain only ANSI letters and numbers, dots and dashes
-   Dots and dashes are allowed everywhere except at the line beginning and end
-   The name must not be an IP address

![Issuing a certificate via Let's Encrypt](/en/docs/mt5/platform/img/lets_encrypt_certificate.png "Issuing a certificate via Let's Encrypt")

The generated certificate will be added to the platform.

The Let's Encrypt certificate is valid for 90 days, but the platform will automatically renew it. A week before the certificate expires, the platform will send a request to the server and then will receive and install a new certificate.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Let's Encrypt has limits on the frequency and number of issued certificates. If the certificate generation fails, find out and fix the cause rather than trying again and again. Otherwise, the service may restrict your access.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Let's Encrypt does not support the <a href="/en/docs/mt5/platform/administration/security/network_anti_ddos" class="topiclink">Cloudflare service</a>. If you are using cloud protection for your access servers, Let's Encrypt will not be able to connect to them for domain verification.</span></li></ul></td></tr></tbody></table>

## Web Services [#](integration_web_services#web_service)

The platform allows the receiving and sending of [callback requests](https://en.wikipedia.org/wiki/Callback_\(computer_programming\)) from external services. They are used to notify the system about various external events.

For example, SMS providers CM.com and Vonage which are available for [integration](/en/docs/mt5/platform/administration/integration/integration_sms), can send notifications about message delivery statuses. The services need to know the address to which the messages should be sent. Such addresses are referred to as endpoints. Endpoints can be configured via the Web Services section.

Callback requests are received and processed by access servers. The access servers actually act as a web server. First, you should set a domain name for them. External services will access the platform at this address. Also, endpoint addresses for callback requests will be formed relative to this address. You should create a DNS record for the specified domain (bind the domain with a public IP address of the access server), as well as load the certificate to the platform, as described in the [SSL Certificates](/en/docs/mt5/platform/administration/integration/integration_web_services#ssl) section.

![Configuring endpoints for callback requests from web services](/en/docs/mt5/platform/img/web_services.png "Configuring endpoints for callback requests from web services")

### Request URLs

To maintain a transparent structure and to ensure further extensibility, all callback endpoints are named as follows: \[domain name\]/api/callback/\[integration section\]/\[unique part for a specific service\]. For example:

-   Endpoints for [messenger](/en/docs/mt5/platform/administration/integration/integration_messenger) and [SMS gateway](/en/docs/mt5/platform/administration/integration/integration_sms) integrations will start with \[domain name\]/api/callback/messenger/.

-   All endpoints for [payment system](/en/docs/mt5/platform/administration/payments) integrations will start with the path \[domain name\]/api/callback/payments/.

-   To run [automation](/en/docs/mt5/platform/administration/automation/automation_trigger#webcallback) tasks through external services, all endpoints will start from the path \[domain name\]/api/callback/automation/.

The platform only accepts requests with the specified URLs. The platform will nor process any other requests out of this list. This is necessary to ensure safety.

### Authorization for requests

As an additional security measure, authorization through [a manager account](/en/docs/mt5/platform/administration/admin_managers) can be enabled for each request. To do this, specify the relevant account login in the Manager field. Requests with additional authentication should have the following information in their header:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Authorization:&nbsp;BASIC&nbsp;BASE64_LOGIN_PASSWORD</span></p></td></tr></tbody></table>

where BASE64\_LOGIN\_PASSWORD is a sting in the BASE64 format with the login and password of the manager account specified as <login>:<password>. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">1000:Password</span></p></td></tr></tbody></table>

This string in the BASE64 format is shown below:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">MTAwMDpQYXNzd29yZA==</span></p></td></tr></tbody></table>

Accordingly, in the request header should be as follows

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Authorization:&nbsp;BASIC&nbsp;MTAwMDpQYXNzd29yZA==</span></p></td></tr></tbody></table>

If you leave the Manager field empty, the request will operate as before, without the additional authorization. The server will only check the list of allowed URLs and IP addresses.

### List of allowed IP addresses for requests

Set the IP addresses from which access servers will receive callback requests to specific endpoints. This is needed for added security. The default list contains only one entry "\* — 127.0.0.1". It allows requests to be received on any endpoints from the local machine.

Addresses can be specified in the following forms:

-   A comma separated list: 10.12.192.1, 10.12.192.6
-   A range: 10.12.192.1-10.12.192.110
-   Using a netmask: 192.168.0.0/16 or 2a00::0/16

The formats can be combined. For example: 10.12.192.1-10.12.192.110, 192.168.0.1

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">The list of allowed addresses is valid for all access servers.</span></p></th></tr></thead></table>

[Kafka Streaming Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming)

[Security](/en/docs/mt5/platform/administration/security)