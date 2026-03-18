# Apache Kafka Server Installation and Setup

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)[Event Streaming](/en/docs/mt5/platform/administration/integration/integration_streaming)Kafka Installation and Setup

# Apache Kafka Server Installation and Setup

There are many ways to install and configure [Apache Kafka](https://kafka.apache.org/). In this article, we will demonstrate just one example. Instead of setting up your own server, you may use ready-to-use cloud-based solutions, such as:

-   [https://aws.amazon.com/msk/](https://aws.amazon.com/msk/)
-   [https://yandex.cloud/en/services/managed-kafka](https://yandex.cloud/en/services/managed-kafka)
-   [https://www.digitalocean.com/products/managed-databases-kafka](https://www.digitalocean.com/products/managed-databases-kafka)

Before beginning the installation, we also recommend reviewing the official documentation and other helpful resources about the system:

-   [https://kafka.apache.org/quickstart](https://kafka.apache.org/quickstart)
-   [https://www.confluent.io/resources/ebook/kafka-the-definitive-guide/](https://www.confluent.io/resources/ebook/kafka-the-definitive-guide/)

## Kafka Cluster Installation

As an example, let's consider the installation of a Kafka cluster consisting of three brokers. All brokers will be installed on a single physical machine running Ubuntu 22.04, each configured with a different IP address. It is assumed that the server is properly configured and accessible from the Internet on ports 9092 and 9093 at the address kafka.build.srv.com.

This machine will serve both as a broker and as the controller managing the entire cluster. Run the following scripts on each instance:

Install the required packages:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#update and install zip and jdk</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo apt-get update; echo Y|apt-get upgrade; echo Y|apt-get dist-upgrade; echo Y|apt-get autoremove</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo apt-get install unzip</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo apt-get install default-jdk -y</span></p></td></tr></tbody></table>

Create a user account under which Kafka services will operate:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#create kafka user</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo adduser --no-create-home &nbsp;--shell=/sbin/nologin --disabled-password --disabled-login --gecos "" kafka</span></p></td></tr></tbody></table>

Create directories for cluster installation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo mkdir /var/kafka</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo mkdir /var/kafka/kafka1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo mkdir /var/kafka/kafka1/logs</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo mkdir /var/kafka/kafka2</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo mkdir /var/kafka/kafka2/logs</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo mkdir /var/kafka/kafka3</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo mkdir /var/kafka/kafka3/logs</span></p></td></tr></tbody></table>

Download the latest Kafka distribution from [https://kafka.apache.org/downloads](https://kafka.apache.org/downloads) and extract it into three separate directories: kafka1, kafka2, and kafka3.

Set the Kafka user as the owner of each directory to allow modification of their contents:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo chown -R kafka:kafka /var/kafka</span></p></td></tr></tbody></table>

Generate a unique cluster ID. The ID is required to operate in Controller (Kraft) mode. You can use any sufficiently complex alphanumeric combination. This ID will be needed later during the configuration process.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/kafka1/bin# ./kafka-storage.sh random-uuid</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[unique cluster ID]</span></p></td></tr></tbody></table>

Issue an SSL certificate for the domain through which Kafka will be accessible, for example, using [Let's Encrypt](https://letsencrypt.org/). Copy the certificate file (CRT) and the private key (PFX) to the directory: /var/kafka/kafka1/config/kraft/keys. Next, create a certificate keystore:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">keytool -importkeystore -srckeystore </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[certificate.pfx]</span><span class="f_CodeExampleWrap"> -srcstoretype pkcs12 -srcstorepass </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[certificate password]</span><span class="f_CodeExampleWrap"> -destkeystore kafka.keystore.jks -deststoretype jks -deststorepass </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[keystore password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">keytool -keystore kafka.truststore.jks -alias CARoot -import -file </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[certificate.crt]</span><span class="f_CodeExampleWrap"> -storepass </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[keystore password]</span></p></td></tr></tbody></table>

Replace the placeholders with your actual values:

-   certificate.pfx — the filename of the certificate containing the private key
-   password certificate — the password protecting the certificate
-   keystore certificate — the password protecting the certificate keystore
-   certificate.crt — the filename of the certificate containing the private key

Then copy the following four files to /var/kafka/kafka1/config/kraft/:

1\. admin.properties — this file contains the main connection parameters for Kafka.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">bootstrap.servers=</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092, kafka2.build.srv.com:9092, kafka3.build.srv.com:9092</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">security.protocol=SASL_SSL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.mechanism=PLAIN</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">username="admin" password="TestAdmin"</span><span class="f_CodeExampleWrap">;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.keystore.location=/var/kafka/kafka1/config/kraft/keys/kafka.keystore.jks</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.keystore.password=</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[keystore password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.key.password=</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[certificate password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.truststore.location=/var/kafka/kafka1/config/kraft/keys/kafka.truststore.jks</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.truststore.password=hSFdoYWxJ3</span></p></td></tr></tbody></table>

Please note:

-   bootstrap.servers=kafka1.build.srv.com:9092, kafka2.build.srv.com:9092, kafka3.build.srv.com:9092 — these are the subdomains where the Kafka brokers will be running. Replace them with the appropriate addresses for your domains. These endpoints will be required when [configuring the connection to Kafka from MetaTrader 5](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming).
-   username="admin" password="TestAdmin" — these are the login and password of the administrator account, which you will use to connect to the Kafka server. You can replace these credentials with your own.
-   security.protocol=SASL\_SSL — the type of authentication that the Kafka server will use. You will need to specify it when [configuring the connection to Kafka from MetaTrader 5](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming).
-   ssl.keystore.password — the password for the certificate keystore
-   ssl.key.password — the password for the certificate

2\. jaas.conf — this file is used to define Kafka users.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">KafkaServer {</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp; &nbsp;org.apache.kafka.common.security.plain.PlainLoginModule required</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">//Cluster administrator login</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp; &nbsp;username="admin"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp; &nbsp;password="TestAdmin"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp; &nbsp;user_admin="TestAdmin"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">//Logins in the format of user_username="Password"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp; &nbsp;user_testconsumer="TestConsumer"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp; &nbsp;user_testproducer="TestProducer"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp; &nbsp;serviceName="kafka";</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">};</span></p></td></tr></tbody></table>

As an example, two users are created with the usernames testconsumer and testproducer. These accounts can be used to [connect to Kafka from MetaTrader 5](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming).

For the administrator account login and password, use the corresponding credentials from the admin.properties file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Usernames and passwords may only contain Latin letters, numbers, and the following symbols: "_", "-", and ".".</span></p></td></tr></tbody></table>

Copy a similar file to the remaining cluster nodes: /var/kafka/kafka2/config/kraft/ and /var/kafka/kafka3/config/kraft/.

3\. kafka1.service — this file defies the service configuration for Kafka.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">[Unit]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Requires=network.target</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">After=network.target</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">[Service]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Type=simple</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">User=kafka</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Environment=KAFKA_HEAP_OPTS="-Xmx1G -Xms1G -Djava.security.auth.login.config=/var/kafka/kafka1/config/kraft/jaas.conf"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Environment=KAFKA_JVM_PERFORMANCE_OPTS="-XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ExecStartPre=/bin/bash -c '/var/kafka/kafka1/bin/kafka-storage.sh format -t </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[unique cluster ID]</span><span class="f_CodeExampleWrap"> -c /var/kafka/kafka1/config/kraft/server.properties --ignore-formatted'</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ExecStart=/bin/bash -c '/var/kafka/kafka1/bin/kafka-server-start.sh /var/kafka/kafka1/config/kraft/server.properties'</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ExecStop=/var/kafka/kafka1/bin/kafka-server-stop.sh</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Environment="LOG_DIR=/var/kafka/kafka1/logs"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Restart=on-failure</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">LimitNOFILE=65536</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">[Install]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">WantedBy=multi-user.target</span></p></td></tr></tbody></table>

In the file, specify the unique cluster ID defined in the [previous steps](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#uuid).

Copy a similar file to the remaining cluster nodes: /var/kafka/kafka2/config/kraft/ and /var/kafka/kafka3/config/kraft/.

4\. server.properties — the detailed settings of the Kafka server.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Licensed to the Apache Software Foundation (ASF) under one or more</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># contributor license agreements. &nbsp;See the NOTICE file distributed with</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># this work for additional information regarding copyright ownership.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The ASF licenses this file to You under the Apache License, Version 2.0</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># (the "License"); you may not use this file except in compliance with</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># the License. &nbsp;You may obtain a copy of the License at</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; &nbsp;http://www.apache.org/licenses/LICENSE-2.0</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Unless required by applicable law or agreed to in writing, software</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># distributed under the License is distributed on an "AS IS" BASIS,</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># See the License for the specific language governing permissions and</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># limitations under the License.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># This configuration file is intended for use in KRaft mode, where</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Apache ZooKeeper is not present.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">############################# Server Basics #############################</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The role of this server. Setting this puts us in KRaft mode</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">process.roles=broker,controller</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The node id associated with this instance's roles</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">node.id=1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The connect string for the controller quorum</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">controller.quorum.voters=1@kafka1.build.srv.com:9093,2@kafka2.build.srv.com:9093,3@kafka3.build.srv.com:9093</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#controller.quorum.voters=1@localhost:9093</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">############################# Socket Server Settings #############################</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The address the socket server listens on.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Combined nodes (i.e. those with `process.roles=broker,controller`) must list the controller listener here at a minimum.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># If the broker listener is not defined, the default listener will use a host name that is equal to the value of java.net.InetAddress.getCanonicalHostName(),</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># with PLAINTEXT listener name, and port 9092.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; FORMAT:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; &nbsp; listeners = listener_name://host_name:port</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; EXAMPLE:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; &nbsp; listeners = PLAINTEXT://your.host.name:9092</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">listeners=EXTERNAL://kafka1.build.srv.com:9092,CONTROLLER://kafka1.build.srv.com:9093</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#listeners=PLAINTEXT://:9092,CONTROLLER://:9093</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Name of listener used for communication between brokers.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">inter.broker.listener.name=EXTERNAL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Listener name, hostname and port the broker or the controller will advertise to clients.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># If not set, it uses the value for "listeners".</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">advertised.listeners=EXTERNAL://kafka1.build.srv.com:9092</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#advertised.listeners=PLAINTEXT://localhost:9092,CONTROLLER://localhost:9093</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># A comma-separated list of the names of the listeners used by the controller.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># If no explicit mapping set in `listener.security.protocol.map`, default will be using PLAINTEXT protocol</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># This is required if running in KRaft mode.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">controller.listener.names=CONTROLLER</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Maps listener names to security protocols, the default is for them to be the same. See the config documentation for more details</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">listener.security.protocol.map=EXTERNAL:SASL_SSL,CONTROLLER:SASL_SSL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># SASL settings</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.enabled.mechanisms=PLAIN</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.mechanism.controller.protocol=PLAIN</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.mechanism.inter.broker.protocol=PLAIN</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">security.protocol=SASL_SSL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">authorizer.class.name=org.apache.kafka.metadata.authorizer.StandardAuthorizer</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">allow.everyone.if.no.acl.found=false</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">super.users=User:admin</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Specify the service name for SASL (even if PLAIN is used; this parameter is required for correct operation)</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.kerberos.service.name=kafka1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># SSL/TLS Settings</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.keystore.location=/var/kafka/kafka1/config/kraft/keys/kafka.keystore.jks</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.keystore.password=</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[keystore password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.key.password=</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[certificate password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.truststore.location=/var/kafka/kafka1/config/kraft/keys/kafka.truststore.jks</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.truststore.password=</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[keystore password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># TLS between brokers and clients</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#security.inter.broker.protocol=SSL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssl.client.auth=required</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The number of threads that the server uses for receiving requests from the network and sending responses to the network</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">num.network.threads=3</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The number of threads that the server uses for processing requests, which may include disk I/O</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">num.io.threads=8</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The send buffer (SO_SNDBUF) used by the socket server</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">socket.send.buffer.bytes=102400</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The receive buffer (SO_RCVBUF) used by the socket server</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">socket.receive.buffer.bytes=102400</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The maximum size of a request that the socket server will accept (protection against OOM)</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">socket.request.max.bytes=104857600</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">############################# Log Basics #############################</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># A comma separated list of directories under which to store log files</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">log.dirs=/var/kafka/kafka1/logs/kraft-combined-logs</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The default number of log partitions per topic. More partitions allow greater</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># parallelism for consumption, but this will also result in more files across</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># the brokers.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">num.partitions=3</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The number of threads per data directory to be used for log recovery at startup and flushing at shutdown.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># This value is recommended to be increased for installations with data dirs located in RAID array.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">num.recovery.threads.per.data.dir=1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">############################# Internal Topic Settings &nbsp;#############################</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The replication factor for the group metadata internal topics "__consumer_offsets" and "__transaction_state"</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># For anything other than development testing, a value greater than 1 is recommended to ensure availability such as 3.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">offsets.topic.replication.factor=1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">transaction.state.log.replication.factor=1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">transaction.state.log.min.isr=1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">############################# Log Flush Policy #############################</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># Messages are immediately written to the filesystem but by default we only fsync() to sync</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># the OS cache lazily. The following configurations control the flush of data to disk.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># There are a few important trade-offs here:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; &nbsp;1. Durability: Unflushed data may be lost if you are not using replication.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; &nbsp;2. Latency: Very large flush intervals may lead to latency spikes when the flush does occur as there will be a lot of data to flush.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># &nbsp; &nbsp;3. Throughput: The flush is generally the most expensive operation, and a small flush interval may lead to excessive seeks.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The settings below allow one to configure the flush policy to flush data after a period of time or</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># every N messages (or both). This can be done globally and overridden on a per-topic basis.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The number of messages to accept before forcing a flush of data to disk</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#log.flush.interval.messages=10000</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The maximum amount of time a message can sit in a log before we force a flush</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#log.flush.interval.ms=1000</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">############################# Log Retention Policy #############################</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The following configurations control the disposal of log segments. The policy can</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># be set to delete segments after a period of time, or after a given size has accumulated.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># A segment will be deleted whenever *either* of these criteria are met. Deletion always happens</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># from the end of the log.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The minimum age of a log file to be eligible for deletion due to age</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">log.retention.hours=168</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># A size-based retention policy for logs. Segments are pruned from the log unless the remaining</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># segments drop below log.retention.bytes. Functions independently of log.retention.hours.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">#log.retention.bytes=1073741824</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The maximum size of a log segment file. When this size is reached a new log segment will be created.</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">log.segment.bytes=1073741824</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># The interval at which log segments are checked to see if they can be deleted according</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap"># to the retention policies</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">log.retention.check.interval.ms=300000</span></p></td></tr></tbody></table>

Replace the domain addresses with your own in the parameters controller.quorum.voters, listeners, and advertised.listeners.

Copy a similar file to the remaining cluster nodes: /var/kafka/kafka2/config/kraft/ and /var/kafka/kafka3/config/kraft/, replacing the following lines:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">node.id=</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">...</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">listeners=EXTERNAL://kafka</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">1</span><span class="f_CodeExampleWrap">.build.srv.com:9092,CONTROLLER://kafka</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">1</span><span class="f_CodeExampleWrap">.build.srv.com:9093</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">...</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">advertised.listeners=EXTERNAL://kafka</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">1</span><span class="f_CodeExampleWrap">.build.srv.com:9092</span></p></td></tr></tbody></table>

Replace the server number with the corresponding one: 2 and 3.

Next, create a symlink kafka1.service -> /etc/systemd/system and start the cluster node:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">systemctl daemon-reload</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">systemctl start kafka1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">systemctl start kafka2</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">systemctl start kafka3</span></p></td></tr></tbody></table>

After completing the setup, you can start working with the server: create topics, connect to brokers, and transmit data.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any changes to the configuration files require a sequential start of the cluster nodes.</span></p></td></tr></tbody></table>

## Configure Producer Permissions [#](kafka_install#acl)

To manage system access in Kafka, an Access Control List (ACL) is used. This list defines all users and their corresponding permissions.

MetaTrader 5 acts as a producer, and it requires appropriate permissions — specifically, the ability to create and modify topics. Since the platform exports a [wide variety of data](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#topics) into different topic, assigning permissions for each individual topic would be impractical. Instead, you can configure permissions once for all topics with a specific prefix. For example, MT5-. When [setting up data streaming in MetaTrader 5](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#prefix), you can specify this prefix so that all topic names generated by the platform begin with it.

Earlier we [creates the user testproducer](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#kafka_user). Now, assign permissions for this user to work with all topics that have the MT5- prefix using the following commands:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/kafka1/bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092</span><span class="f_CodeExampleWrap"> --command-config /var/kafka/kafka1/config/kraft/admin.properties --add --allow-principal User:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">testroducer</span><span class="f_CodeExampleWrap"> --operation </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">READ</span><span class="f_CodeExampleWrap"> --topic </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">MT5-</span><span class="f_CodeExampleWrap"> --resource-pattern-type prefixed</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/kafka1/bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092</span><span class="f_CodeExampleWrap"> --command-config /var/kafka/kafka1/config/kraft/admin.properties --add --allow-principal User:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">testroducer</span><span class="f_CodeExampleWrap"> --operation </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">WRITE</span><span class="f_CodeExampleWrap"> --topic </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">MT5-</span><span class="f_CodeExampleWrap"> --resource-pattern-type prefixed</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/kafka1/bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092</span><span class="f_CodeExampleWrap"> --command-config /var/kafka/kafka1/config/kraft/admin.properties --add --allow-principal User:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">testroducer</span><span class="f_CodeExampleWrap"> --operation </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">CREATE</span><span class="f_CodeExampleWrap"> --topic </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">MT5-</span><span class="f_CodeExampleWrap"> --resource-pattern-type prefixed</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/kafka1/bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092</span><span class="f_CodeExampleWrap"> --command-config /var/kafka/kafka1/config/kraft/admin.properties --add --allow-principal User:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">testroducer</span><span class="f_CodeExampleWrap"> --operation </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">DELETE</span><span class="f_CodeExampleWrap"> --topic </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">MT5-</span><span class="f_CodeExampleWrap"> --resource-pattern-type prefixed</span></p></td></tr></tbody></table>

In this example, the permissions are configured on the kafka1 server. If needed, you can change this to another server. The following options are specified:

-   User — the username to which the permission is granted.
-   \--operation — the type of permission being granted. READ — read access, WRITE — write access, CREATE — permission to create topics, DELETE — permission to delete topics.
-   \--topic — the topic prefix for which the permission is granted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Be sure to grant the appropriate permissions to the user account that MetaTrader 5 will use to connect to Kafka. Without these permissions, the platform will not be able to automatically create topics or publish data to them.</span></li><li class="p_tableatten"><span class="f_tableatten">Permissions apply only to topics with the specified prefix. They do not affect any other topics, so there is no risk to the security of your other data in Kafka.</span></li></ul></td></tr></tbody></table>

## Create Consumer Groups [#](kafka_install#consumer-group)

A Consumer Group is a collection of one or more consumers that collaboratively consume messages from one or more topics. The main purpose of using consumer groups is to scale out message consumption and manage how messages are distributed among consumers in the group.

To create a consumer group and add a user to it, use the following command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/kafka1/bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092</span><span class="f_CodeExampleWrap"> --command-config /var/kafka/</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1</span><span class="f_CodeExampleWrap">/config/kraft/admin.properties --add --allow-principal User:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">testconsumer</span><span class="f_CodeExampleWrap"> --operation </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">READ</span><span class="f_CodeExampleWrap"> --group </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">test-consumer-group</span></p></td></tr></tbody></table>

In this example, the permissions are configured on the kafka1 server. If needed, you can change this to another server. The following options are specified:

-   User — the username to be added to the consumer group.
-   \--operation — the type of permission being granted. In this case, only READ.

-   \--group — the name of the consumer group.

You must also grant the user read access to the topics. As with producers, this is done by assigning permissions to topics with a specific prefix:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/kafka1/bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092</span><span class="f_CodeExampleWrap"> --command-config /var/kafka/kafka1/config/kraft/admin.properties --add --allow-principal User:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">testconsumer</span><span class="f_CodeExampleWrap"> --operation </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">READ</span><span class="f_CodeExampleWrap"> --topic </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">MT5-</span><span class="f_CodeExampleWrap"> --resource-pattern-type prefixed</span></p></td></tr></tbody></table>

## Create Topics [#](kafka_install#create_topic)

When exporting data, the platform creates topics automatically. To create a topic manually, use the following command:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">/var/kafka/</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1</span><span class="f_CodeExampleWrap">/bin/kafka-topics.sh --create --topic </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">test-topic</span><span class="f_CodeExampleWrap"> --partitions 3 --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092</span><span class="f_CodeExampleWrap"> --replication-factor 3 --command-config /var/kafka/</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1</span><span class="f_CodeExampleWrap">/config/kraft/admin.properties</span></p></td></tr></tbody></table>

In the example, the topics are created on the kafka1 server. If needed, you can change this to another server. The following options are specified:

-   \--topic — the name of the topic
-   partitions 3 — the number of [partitions](/en/docs/mt5/platform/administration/integration/integration_streaming#terms) in the topic
-   replication-factor 3 — the [replication factor](/en/docs/mt5/platform/administration/integration/integration_streaming#terms) for partitions

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For topics created automatically by the platform, Kafka's default parameters are used (e.g., replication count, compression, etc.). Modifying these parameters is the responsibility of the system administrator. However, you can predefine these settings at the topic prefix level to ensure consistent configuration across all automatically created topics.</span></p></td></tr></tbody></table>

## Install a GUI for Kafka Administration [#](kafka_install#gui)

By default, Kafka is a command-line service. For easier configuration and data management, you can install an additional component that provides a graphical interface. We recommend using the open-source project Provectus Kafka UI: [https://github.com/provectus/kafka-ui](https://github.com/provectus/kafka-ui).

As an example, we will install the UI on the kafka1 server. Create a directory named kafka-ui for the installation and navigate into it:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">mkdir -p /var/kafka/kafka1/kafka-ui</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">cd /var/kafka/kafka1/kafka-ui</span></p></td></tr></tbody></table>

Download the latest version of kafka-ui:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">wget https://github.com/provectus/kafka-ui/releases/download/v0.7.2/kafka-ui-api-v0.7.2.jar</span></p></td></tr></tbody></table>

In the kafka-ui directory, create a file named application.yml:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">mcedit /var/kafka/kafka1/kafka-ui/application.yml</span></p></td></tr></tbody></table>

Add the following content into the file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">dynamic.config.enabled: true</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">logging:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;level:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">root:INFO</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;com.provectus:DEBUG</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;reactor.netty.http.server.AccessLog:INFO</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;org.hibernate.validator:WARN</span></p></td></tr></tbody></table>

For convenience, create a bash script start.sh:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">mcedit /var/kafka/kafka1/kafka-ui/start.sh</span></p></td></tr></tbody></table>

Add the following content into the file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">KAFKA_UI=kafka-ui-api-v0.7.2.jar</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">java --add-opens java.rmi/javax.rmi.ssl=ALL-UNNAMED -jar $KAFKA_UI</span></p></td></tr></tbody></table>

Add permission to execute the script:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">chmod +x /var/kafka/kafka1/kafka-ui/start.sh</span></p></td></tr></tbody></table>

Run the script:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">./start.sh</span></p></td></tr></tbody></table>

Open your Kafka server page in the browser and specify port 8080. In our example: http://kafka1.build.srv.com:8080.

Click 'Configure new cluster':

![Configure new cluster](/en/docs/mt5/platform/img/kafka_ui_new_cluster.png "Configure new cluster")

Enter the following values:

-   Bootstrap servers — kafka1.build.srv.com, kafka2.build.srv.com, kafka3.build.srv.com. Ports 9092.
-   Truststore Location — the path to the [.pfx certificate file](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#certificate) on your local machine. When you click 'Submit', the certificate will be uploaded into the truststore.
-   Truststore password — the password for the certificate.
-   Security Protocol — SASL\_SSL.
-   sasl.mechanism — PLAIN.
-   ssl.keystore.location — the path to the [.crt certificate file](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#certificate) on your local machine.
-   ssl.keystore.password — the password for the [SSL certificate](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#certificate) issued for your Kafka servers.

When you click 'Submit', the certificates will be uploaded to the truststore.

![Configure the cluster](/en/docs/mt5/platform/img/kafka_ui_cluster_settings.png "Configure the cluster")

After saving the settings, you will see your cluster appear in the Kafka UI.

Next, enable authentication. Stop the kafka-ui application by pressing Ctrl+C. Edit the dynamic configuration file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">mcedit /var/kafka/kaka1/kafka-ui/dynamic-config.yml</span></p></td></tr></tbody></table>

Replace the file contents with the following:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">auth:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">type:login_form</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">spring:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;security:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;user:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">name:admin</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">password:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[password for UI access]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">kafka:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;clusters:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;- bootstrapServers: </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">kafka1.build.srv.com:9092,kafka2.build.srv.com:9092,kafka3.build.srv.com:9092</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;name: 'kafka.build.srv.com'</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;properties:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp;security.protocol:SSL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp;ssl.keystore.password:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[certificate password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp;ssl.keystore.location:/var/kafka/kafka1/kafkaui/uploads/kafka.keystore.jks-1724165427</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;readOnly: false</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp;ssl:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp; &nbsp; &nbsp;enabled: true</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">truststoreLocation:/var/kafka/kafka1/kafkaui/uploads/kafka.truststore.jks-1724165395</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">truststorePassword:</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[truststore password]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">rbac:</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;roles: []</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">webclient: {}</span></p></td></tr></tbody></table>

Specify here:

-   The password for the admin account, which will be used to connect to the interface
-   The list of servers in your Kafka cluster
-   The password for the [SSL certificate](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install#certificate)
-   The password for the certificate truststore

Next, configure the kafka-ui service. In the /etc/systemd/system/ directory, create a file named kafka-ui.service:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">mcedit /etc/systemd/system/kafka-ui.service</span></p></td></tr></tbody></table>

Copy the following content into the file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">[Unit]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Description = kafka-ui</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Requires=network.target</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">After=network.target</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">[Service]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">RemainAfterExit=true</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Type=simple</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">User=kafka</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">WorkingDirectory=/var/kafka/kafka1/kafkaui/</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ExecStart=/bin/bash -c '/var/kafka/kafka1/kafka-ui/start.sh'</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">Restart=on-failure</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">RestartSec=5s</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">[Install]</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">WantedBy=multi-user.target</span></p></td></tr></tbody></table>

Run the service:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo systemctl daemon-reload</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo systemctl enable kafka-ui.service</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo systemctl start kafka-ui.service</span></p></td></tr></tbody></table>

You can now connect to Kafka through the web interface at: http://kafka1.build.srv.com:8080/.

[Event Streaming](/en/docs/mt5/platform/administration/integration/integration_streaming)

[Kafka Deployment in Amazon](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon)