# Event Streaming

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_streaming

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)Event Streaming

# Event Streaming

Stream trading platform events to external systems such as [Apache Kafka](https://kafka.apache.org/) for real-time monitoring and advanced data analysis.

Apache Kafka is a scalable and reliable platform for data steam processing that enables efficient transmission, storage, and analysis of large volumes of information. Integration of MetaTrader 5 with Apache Kafka enables you to export a variety of events to the system:

-   Trading operations: all client trades, executed and unexecuted orders, position changes.
-   Price data: quotes financial instruments and pricing statistics received by the platform from gateways and data feeds.
-   Platform configuration changes: server settings, manager configurations, payment modules, and more.
-   Trading account changes: creation, personal data updates, and changes in financial status.
-   Client record updates: creation, updates to personal information, linked accounts, documents, and more.

This integration unlocks extensive opportunities for optimizing business processes:

<table class="help" cellspacing="0" cellpadding="0" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:0; border:none"><h3>Real-Time Analysis and Forecasting</h3><ul><li class="p_ol"><span class="f_ol">Detection of abnormal trading patterns</span></li><li class="p_ol"><span class="f_ol">Analysis of client behavior to identify potential risks</span></li><li class="p_ol"><span class="f_ol">Liquidity and risk management optimization</span></li></ul><h3>Enhanced Security</h3><ul><li class="p_ol"><span class="f_ol">Detection of suspicious trading activity</span></li><li class="p_ol"><span class="f_ol">Monitoring of anomalous system behavior</span></li><li class="p_ol"><span class="f_ol">Automated threat alerts</span></li></ul></td><td style="vertical-align:top; padding:0; border:none"><h3>Improved Customer Service Quality</h3><ul><li class="p_ol"><span class="f_ol">Monitoring of client trading activity</span></li><li class="p_ol"><span class="f_ol">Prompt response to unusual situations</span></li><li class="p_ol"><span class="f_ol">Analysis of user experience to enhance service quality</span></li></ul><h3>Integration with Other Systems</h3><ul><li class="p_ol"><span class="f_ol">Connection to BI analytics and machine learning tools</span></li><li class="p_ol"><span class="f_ol">Automated reporting and real-time data processing</span></li><li class="p_ol"><span class="f_ol">Integration with CRM systems and notification services</span></li></ul></td></tr></tbody></table>

## Key Terminology [#](integration_streaming#terms)

To work with Kafka, you need to be familiar with the key entities used in the system:

-   Broker — a Kafka server that processes message streams and manages their storage. A Kafka cluster can consist of multiple brokers to ensure scalability and fault tolerance.
-   Topic — a channel through which data is transmitted. All messages in Kafka are organized into topics, and producers publish messages to specific topics.
-   Partition — a section within a topic used to scale and parallelize data processing. Each topic consists of one or more partitions.
-   Replication Factor — the number of copies of each partition stored in the Kafka cluster to ensure data availability and fault tolerance. When Kafka writes messages to a topic, these messages are distributed across partitions. Each partition has a replication factor that determines how many copies are stored across different brokers. For example, a replication factor of 3 means each partition will have three copies on different brokers.
-   Producer — the component that publishes messages to a Kafka topic. In this case, it refers to the streaming configuration in the MetaTrader 5 platform.
-   Consumer — the component that reads (subscribes to) messages from a Kafka topic. These are external services that you can use for your business needs.
-   Controller — a server running a Kafka instance in controller mode. Controllers store metadata, broker information, and synchronize their state. Typically, three controllers are used per Kafka cluster, each located in a different availability zone to enhance fault tolerance. In earlier Kafka versions (prior to 2.8), ZooKeeper was used as the controller. It stored metadata about the cluster's state and message locations, enabling replication, fault tolerance, and sharding. In recent versions, Kafka can operate without ZooKeeper. Instead, the Kafka server in controller mode handles this. It implements a new metadata management mechanism known as KRaft. If you're planning to install a newer version of Kafka, you can use this mechanism to eliminate the dependency on a separate ZooKeeper service.

Once familiar with the terminology, proceed with system setup:

-   [Kafka Installation and Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install)
-   [Kafka Deployment in Amazon](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon)
-   [Kafka Streaming Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming)

[KYC](/en/docs/mt5/platform/administration/integration/integration_kyc)

[Kafka Installation and Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install)