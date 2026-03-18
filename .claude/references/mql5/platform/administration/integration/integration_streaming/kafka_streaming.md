# Configuring Data Export to Kafka in MetaTrader 5

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming

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
                    -   [Kafka Installation and Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install)
                    -   [Kafka Deployment in Amazon](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon)
                    -   [Kafka Streaming Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)[Event Streaming](/en/docs/mt5/platform/administration/integration/integration_streaming)Kafka Streaming Setup

# Configuring Data Export to Kafka in MetaTrader 5

Create a new streaming configuration:

![Create a data streaming configuration](/en/docs/mt5/platform/img/kafka_common.png "Create a data streaming configuration")

In the configuration, specify the following:

-   Enable — toggles the data streaming on or off.
-   Name — a custom name for the configuration (producer).
-   Type — the system to which data will be streamed. Currently, only Apache Kafka is supported.
-   Bootstrap servers — a comma-separated [list of Kafka cluster brokers](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#bootstrap). Each address must include the port. Only ASCII characters are allowed.
-   Login — [username](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#kafka_user) used to connect to the Kafka cluster. This user must be [pre-created](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#kafka_user) and granted the necessary permissions. Used during SASL authentication. Only ASCII characters are allowed.
-   Password — password for the specified Kafka cluster user. Only ASCII characters are allowed.
-   Security protocol — security protocol and the [authentication type](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#security_protocol) used by the Kafka server: SASL\_SSL/PLAIN, SASL\_SSL/SCRAM-SHA-256, SASL\_SSL/SCRAM-SHA-512.
-   CA Certificate — client certificate file that will be used for authentication when connecting to the Kafka cluster. For further details please refer to the section "[Working with Certificates](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#certificates)".
-   Topic prefix — prefix added to the beginning of [each topic name](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#topic_full_name). Only Latin letters, numbers, and the symbols '.', '-', '\_' are allowed.
-   Compression — used to reduce the size of JSON text data sent to Kafka. Supported algorithms include LZ4, Gzip, and zstd. The recommended option for optimal speed and compression is zstd. Compression applies only during transmission to the Kafka cluster. Within the cluster, data is repackaged based on topic settings. Consumers must support the compression type set at the topic level.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Do not change the configuration name while it is active. Doing so creates a duplicate configuration that begins sending messages to the same topics, resulting in data duplication.</span></li><li class="p_tableatten"><span class="f_tableatten">Changing the settings (Bootstrap servers, Login, Password, Security protocol, Certificate, Topic prefix, Compression) will recreate the producer with new parameters. Some messages in the sending queue may be lost during this process.</span></li></ul></td></tr></tbody></table>

### Full Topic Names [#](kafka_streaming#topic_full_name)

Platform events are streamed to Kafka cluster topics. The platform attempts to create topics automatically using the following naming convention: a [prefix](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#prefix) followed by a [name](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#topic_name) specified in the settings. They form the full name of the topic. If no prefix is set, the full topic name is just the topic name from the configuration. For example, if the prefix is 'platform1-' and the topic names are 'network' and 'groups', the topics will be created as 'platform1-network' and 'platform1-groups'.

The use of prefixes simplifies management of [permissions](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#acl) to create topic and write data to them. You can grant access by prefix instead of individual topics. Also prefixes are useful for isolating or segmenting data when streaming from multiple MetaTrader 5 platforms to a single Kafka cluster.

Kafka operates and supports streaming operations strictly with the full topic name. If a topic is missing, MetaTrader 5 will try to create it automatically. If you change the topic name or prefix during runtime, the platform will immediately attempt to create a new topic and continue streaming to it. If the platform's Kafka user lacks the necessary permissions for the new topic or prefix, you will see authorization errors in the trade server [logs](/en/docs/mt5/platform/administration/admin_network/network_journal).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Be sure to grant the appropriate prefix <a href="/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#acl" class="topiclink">permissions</a> to the user account that MetaTrader 5 will use to connect to Kafka. Without these permissions, the platform will not be able to automatically create topics or publish data to them.</span></li><li class="p_tableatten"><span class="f_tableatten">Permissions apply only to topics with the specified prefix. They do not affect any other topics, so there is no risk to the security of your other data in Kafka.</span></li></ul></td></tr></tbody></table>

### Working with Certificates [#](kafka_streaming#certificates)

When establishing a secure connection between the MetaTrader 5 platform and Kafka brokers over the TLS protocol, it is crucial to configure the [certificates](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#certificate) correctly. Any errors in the trust chain, use of unsupported formats, or invalid certificates will result in a connection failure, with the "SSL handshake failed" error in the trading server log.

If you are renting a Kafka cluster from [Confluent Cloud](https://www.confluent.io/resources/ebook/kafka-the-definitive-guide/), use the [Let's Encrypt root certificate](https://letsencrypt.org/certs/isrgrootx1.pem). If you are renting Kafka from [Amazon](https://aws.amazon.com/msk/), download the [Starfield Services Root CA - G2](https://www.amazontrust.com/repository/) root certificate.

Supported Certificate Formats

MetaTrader 5 supports certificates in the PEM text format (.pem, .crt, .cer). The binary DER format is not supported. The platform also supports the PKCS#12 format (.pfx). Certificate files may contain either a single certificate or a full certificate chain.

Trust Chain Requirements

When configured properly, each Kafka broker returns its own certificate along with any necessary intermediate certificates, but does not return the root certificate. Therefore, when [configuring a connection in MetaTrader 5](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#certificate), the root certificate must be specified manually. This is necessary to verify the server authenticity and to establish a complete chain of trust.

Diagnosing TLS Errors ("SSL handshake failed")

If the "SSL handshake failed" error appears in the trading server log when configuring the connection to Kafka, you should check the TLS connection using OpenSSL.

To do this, [download](https://github.com/openssl/openssl/wiki/Binaries) and install the appropriate OpenSSL version for your operating system. Then, check the TLS connection to the Kafka broker. Open PowerShell and run the following command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">.\openssl.exe s_client -connect &lt;kafka_broker&gt;:&lt;port&gt; -showcerts -CAfile my_certificate.pem</span></p></td></tr></tbody></table>

where:

-   <kafka\_broker>:<port> — the address and port of the Kafka broker.
-   my\_certificate.pem — the path to the root certificate (or chain of trust) that you intend to trust.

If theverification is successful, you will receive a response similar to the following:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">SSL handshake has read XXXX bytes and written XXX bytes</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Verification: OK</span></p></td></tr></tbody></table>

This indicates that the certificate is valid and the connection can be established using the specified file.

If the chain of trust is incomplete or invalid, you may encounter the following error:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">SSL handshake has read XXXX bytes and written XXX bytes</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Verification error: unable to get local issuer certificate</span></p></td></tr></tbody></table>

This typically means that either the root or intermediate certificate is missing, or an invalid certificate is used on the client side.

1\. Ensure that you are using the root certificate issued by the Certificate Authority (CA). Avoid using a server certificate file for connection.

2\. Verify that all intermediate certificates are present. Some Kafka brokers do not send intermediate certificates during the handshake, in which case the client (MetaTrader 5) cannot construct a complete chain of trust. To check, run the following command in PowerShell:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">.\openssl.exe s_client -connect &lt;kafka_broker&gt;:&lt;port&gt; -showcerts</span></p></td></tr></tbody></table>

This command should return the server certificate and one or more intermediate certificates. If intermediate certificates are missing, add them manually to the CAfile.

## Configuring Exported Data [#](kafka_streaming#topics)

After creating the configuration, navigate to the "Topics" section and select the data you wish to stream:

![Select the data be streamed to Kafka](/en/docs/mt5/platform/img/kafka_topics.png "Select the data be streamed to Kafka")

Add a topic and specify:

-   Name — the second part of the [full topic name](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#topic_full_name), which is added at the end. Only Latin letters, digits, and the symbols '.', '-', and '\_' are allowed.  
    A [prefix](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install) can also be included in the name. For more details on topic naming, refer to the section [Full Topic Names](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#topic_full_name).
-   Description — a description of the configuration.
-   Type — the type of data to be streamed to the topic:
    -   Configurations — changes to the corresponding platform settings.
    -   Ticks — [tick data](/en/docs/mt5/platform/administration/admin_ticks) and [trading statistics](/en/docs/mt5/platform/administration/admin_ticks#statistics).
    -   Trading — any changes in open orders, deals, and positions (creation, modification, deletion), changes to order history, and trade requests sent to the server.
    -   Trading accounts — creation, modification of personal details, and changes in the financial state of [trading accounts](/en/docs/mt5/platform/administration/admin_accounts). In the "Export" column, you can additionally specify which account data should be included, such as name, location (country, city, region, zip code), address, document number, email, phone number, and general data (other less important data: language, status, comment, MetaQuotes ID, etc.).
    -   Clients — creation, modification of personal data, linked accounts, documents, and other changes to the [client](/en/docs/mt5/platform/administration/clients) database. In the "Export" column, you can additionally specify which client data should be included, such as name, location (country, city, region, zip code), address, document number, email, phone number, and general data (other less important data: language, status, comment, MetaQuotes ID, etc.).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Ensure that the platform (producer) has the necessary <a href="/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#acl" class="topiclink">permissions</a> to create topics and write to them. Otherwise, authorization errors will appear in the trading server <a href="/en/docs/mt5/platform/administration/admin_network/network_journal" class="topiclink">log</a>.</span></p></td></tr></tbody></table>

## Event Filtering [#](kafka_streaming#data)

You can further filter the events to be streamed:

-   Trading operations (orders, deals, positions, requests) — by group
-   Price data — by instrument

To do this, configure the appropriate settings in the "Data" section:

![Set filters for streamed events](/en/docs/mt5/platform/img/kafka_data.png "Set filters for streamed events")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Each producer in the platform has a fixed memory limit for storing messages prior to transmission. This limit is set to 1 GB, which typically holds around 500,000 — 5,000,000 messages. If messages cannot be delivered for any reason and the queue reaches this limit, the system will automatically discard the oldest messages to make space for new ones. This results in message loss.</span></p></td></tr></tbody></table>

## Data Format [#](kafka_streaming#format)

All events are streamed to Kafka in JSON format, encoded in UTF-8. JSON is a widely supported data format used by many systems. For example, a tick data entry would appear as follows:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">{</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">"type": "tick",</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">"action": "add",</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">"records": [</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; {</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;"Symbol": "EURAUD",</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;"Time": "1743156690296",</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;"Bid": "1.71045",</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;"Ask": "1.71098",</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;"Last": "0.00000",</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;"Volume": "0"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; }</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">}</span></p></td></tr></tbody></table>

Description of data exports is provided in the [MetaTrader 5 Web API](https://support.metaquotes.net/en/docs/mt5/api/webapi_main) documentation, under the "Data Structure" sections of the relevant configurations and databases.

## Partitioning and Message Ordering [#](kafka_streaming#partitioning)

When streaming data to Kafka, the MetaTrader 5 platform uses key-based partitioning.

A deterministic key is applied for messages of the same type. This ensures that such messages are routed to the same Kafka partition, allowing consumers to receive the data in the exact order in which it was produced.

Kafka guarantees message ordering only within a single partition. The chosen partitioning strategy prioritizes data integrity and order. Under high load, this approach may reduce parallelism and increase the load on individual partitions.

## Recommendations [#](kafka_streaming#recommendations)

If you observe performance degradation during message transmission, check the network throughput and ensure sufficient disk space is available on each Kafka broker. If needed, configure data retention limits to enable automatic cleanup of topics in a timely manner.

Global retention settings can be adjusted via the log.retention.hours parameter (default is 168) in the server.properties file. To configure retention per topic, use the retention.ms parameter.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Closely monitor disk space across your Kafka cluster. If it becomes fully exhausted, individual brokers will begin to fail, ultimately leading to cluster-wide failure.</span></p></td></tr></tbody></table>

## Statistics and Monitoring [#](kafka_streaming#statistics)

In the "Overview" section, each producer has detailed metrics available to help monitor performance.

![Producer statistics](/en/docs/mt5/platform/img/kafka_statistics.png "Producer statistics")

The top part shows statistics for all producers.

-   Total delivered messages — number of messages successfully delivered from the platform to the Kafka cluster for the current calendar day.
-   Failed messages — number of messages that failed to be delivered during the current calendar day.
-   Message queue — number and size of messages (uncompressed data — key and JSON) currently pending delivery. Ideally, this should remain at 0/0. If the message queue is constantly growing, check your network throughput and the performance of your Kafka cluster: this may be caused by lack of disk space or high CPU usage. Consider adding more Kafka brokers to balance the load.
-   Message traffic — volume of message (uncompressed data — key and JSON) transmitted to the Kafka cluster today.
-   Message throughput — number of messages and total size of data (uncompressed data — key and JSON) transmitted per second.

Below the general overview, statistics are displayed for each trading server in the platform cluster. Additional metrics include:

-   Latency — measures message delivery time with confirmation. before sending a message to the Kafka cluster, the platform timestamps it at the moment it is queued. The message is sent to the Kafka cluster, after which the platform receives delivery confirmation. The platform then calculates the difference between the confirmation time and the timestamp to determine latency. N/A indicates latency cannot be calculated due to lack of connection or traffic.
-   Connection status — reflects connectivity to the Kafka cluster. "Connected" means the platform has established a connection with at least one [broker](/en/docs/mt5/platform/administration/integration/integration_streaming#terms).

The count of message delivery errors is displayed as a clickable link. Clicking it opens the corresponding trading server [log](/en/docs/mt5/platform/administration/admin_network/network_journal), filtered by the keyword Kafka. This will help you quickly locate relevant issues.

Each trading server's message delivery status is marked with a color:

-   Green — no delivery errors detected during the calendar day.
-   Yellow — no current errors, but some messages failed earlier in the day.
-   Red — unable to connect to the Kafka cluster, delivery errors are occurring in real-time, or messages are piling up in the queue and cannot be delivered for more than 60 seconds. Hover for a tooltip with details. For further investigation, request the trade server [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) using the keyword Kafka.
-   Gray — message streaming is disabled.

All statuses reset at the end of the calendar day, and are updated based on the current state.

Below these metrics, you can find graphical visualizations of message delivery performance.

[Kafka Deployment in Amazon](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon)

[Web Services](/en/docs/mt5/platform/administration/integration/integration_web_services)