# Deploying a Kafka Cluster in Amazon (MSK)

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)[Event Streaming](/en/docs/mt5/platform/administration/integration/integration_streaming)Kafka Deployment in Amazon

# Deploying a Kafka Cluster in Amazon (MSK)

Instead of setting up your own Kafka cluster, you can use a managed solution provided by [Amazon](https://aws.amazon.com/msk/). When configuring the cluster, consider the following recommendations:

-   Create a custom Kafka cluster in [KRaft](https://aws.amazon.com/blogs/big-data/introducing-support-for-apache-kafka-on-raft-mode-kraft-with-amazon-msk-clusters/) mode.
-   Disable TLS client authentication through AWS Certificate Manager (ACM). This option is currently not supported by MetaTrader 5.

Below is a detailed guide on how to deploy a Kafka cluster in Amazon. The setup includes the following configurations:

-   A Kafka cluster in KRaft mode (version 4.0) with two brokers.
-   SCRAM-SHA-512 authentication (Amazon MSK does not support SCRAM-SHA-256).
-   Creation of three users using an Access Control List (ACL):
    -   kafka\_admin / password\_kafka\_admin — Kafka cluster administrator (responsible for creating topics and users, and managing permissions)
    -   kafka\_producer / password\_kafka\_producer — responsible for sending messages
    -   kafka\_consumer / password\_kafka\_consumer — responsible for receiving messages
-   Automatic topic creation upon the first message write
-   Public access to the cluster via IP address

## 1\. Create a KMS Key for SCRAM Authentication [#](kafka_install_amazon#key)

Open the AWS KMS Console and create a Customer Managed Key (CMK). In Step 1, select the following options:

-   Key type — Symmetric
-   Key usage — Encrypt and decrypt
-   Key material origin — KMS
-   Regionality — Single-Region key

![Create a KMS key](/en/docs/mt5/platform/img/kafka_amazon_kms_key_1.png "Create a KMS key")

In step 2, set Alias to msk-default\_key:

![Create a KMS key](/en/docs/mt5/platform/img/kafka_amazon_kms_key_2.png "Create a KMS key")

In step 3, specify the administrator roles that will be allowed to manage this key. Select AWSServiceRoleForKafka. Also enable permission to delete the key.

![Create a KMS key](/en/docs/mt5/platform/img/kafka_amazon_kms_key_3.png "Create a KMS key")

Next, specify the administrator roles that will be allowed to perform cryptographic operations using this key. Select AWSServiceRoleForKafka.

![Create a KMS key](/en/docs/mt5/platform/img/kafka_amazon_kms_key_4.png "Create a KMS key")

In step 5, you can manually edit the key. This step can be skipped by clicking Next.

![Create a KMS key](/en/docs/mt5/platform/img/kafka_amazon_kms_key_5.png "Create a KMS key")

In the final step, review all key details and copy its ARN — it will be required when creating the cluster and users. Then click Finish to generate the key.

![Create a KMS key](/en/docs/mt5/platform/img/kafka_amazon_kms_key_6.png "Create a KMS key")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Use the same key for both the Kafka cluster and user SCRAM authentication.</span></p></td></tr></tbody></table>

## 2\. Basic Kafka Cluster Configuration [#](kafka_install_amazon#configuration)

During the initial deployment of the Kafka cluster, configure it with ACL checks disabled by setting the parameter allow.everyone.if.no.acl.found=true. Otherwise, it will be impossible to enable this setting later and grant administrative rights to the first user.

Open the 'MSK Cluster \\ Cluster Configuration' section and click 'Create cluster configuration'.

![Create a cluster configuration](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_1.png "Create a cluster configuration")

Assign a name to the configuration, e.g.: start. Then, set 'Broker type = Express brokers' and add the following two lines to the configuration code:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">auto.create.topics.enable=true</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">allow.everyone.if.no.acl.found=true</span></p></td></tr></tbody></table>

![Create a cluster configuration](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_2.png "Create a cluster configuration")

After specifying the parameters, click Create.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The permission to connect without ACL can only be set during cluster initialization and only through the parameter allow.everyone.if.no.acl.found=true. You will not be able to modify this parameter later.</span></p></td></tr></tbody></table>

## 3\. Creating the Kafka Cluster [#](kafka_install_amazon#cluster)

Open the 'MSK Clusters \\ Clusters' section and click 'Create cluster'.

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_3.png "Create a Kafka cluster")

In step 1, set the following parameters:

-   Cluster creation method — Custom create
-   Cluster name — kafka
-   Cluster type — Provisioned
-   Apache Kafka version — 4.0.x

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_4.png "Create a Kafka cluster")

Below that, specify:

-   Broker type — Standard brokers
-   Number of zones — 2
-   Brokers per zone — 1

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_5.png "Create a Kafka cluster")

In the 'Cluster configuration' field, select the [previously created](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#configuration) 'start' configuration. For 'Configuration revision', choose the latest configuration version if multiple are available. Then proceed to the next step.

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_6.png "Create a Kafka cluster")

In step 2, leave all settings as default.

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_7.png "Create a Kafka cluster")

In step 3, set:

-   Access control methods — SASL/SCRAM authentication
-   Encrypt data at rest — Use customer managed key. Next, select the [previously created](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#key) KMS (identifier).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">MetaTrader 5 does not support IAM and ACM (mTLS) authentication.</span></p></td></tr></tbody></table>

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_8.png "Create a Kafka cluster")

In step 4, leave all settings as default and proceed.

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_9.png "Create a Kafka cluster")

In the last step, review all previously defined parameters and click 'Create cluster'.

![Create a Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_create_cluster_10.png "Create a Kafka cluster")

## 4\. Creating Users with SCRAM Authentication [#](kafka_install_amazon#users)

Open 'AWS Console \\ Amazon MSK \\ User' and create three users:

-   kafka\_admin
-   kafka\_producer
-   kafka\_consumer

Next, define the authentication parameters for each user:

-   Password
-   Secret
-   Key

Below is an example for user kafka\_admin. The same steps should be repeated for the other two users.

Open the 'AWS Secrets Manager \\ Secrets' section and click 'Store a new secret'.

![Configuring user authentication](/en/docs/mt5/platform/img/kafka_amazon_secrets_1.png "Configuring user authentication")

Specify:

-   Secret type — Other type of secret
-   username — the username to configure, e.g., kafka\_admin.
-   password — the user's password, e.g., password\_kafka\_admin.
-   Encryption key  — the [previously create](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#key) KMS key.

![Configuring user authentication](/en/docs/mt5/platform/img/kafka_amazon_secrets_2.png "Configuring user authentication")

Assign a name to the secret. It must start with "AmazonMSK\_". This is necessary for proper association within the Amazon environment. For this case, we use AmazonMSK\_kafka\_admin.

![Configuring user authentication](/en/docs/mt5/platform/img/kafka_amazon_secrets_3.png "Configuring user authentication")

In step 3, leave all settings as default and proceed by clicking Next.

![Configuring user authentication](/en/docs/mt5/platform/img/kafka_amazon_secrets_4.png "Configuring user authentication")

In step 4, review all the settings and click 'Store'.

![Configuring user authentication](/en/docs/mt5/platform/img/kafka_amazon_secrets_5.png "Configuring user authentication")

Repeat the above process for kafka\_producer and kafka\_consumer.

## 5\. Linking Users to the Kafka Cluster [#](kafka_install_amazon#associate)

Open 'MSK Clusters \\ Clusters', select the previously created cluster named 'kafka', and click 'Associate secrets'.

![Linking Users to the Kafka Cluster](/en/docs/mt5/platform/img/kafka_amazon_associate_secrets_1.png "Linking Users to the Kafka Cluster")

Click 'Choose secrets' and select [previously created secrets](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#users). Then click 'Associate secrets'.

![Linking Users to the Kafka Cluster](/en/docs/mt5/platform/img/kafka_amazon_associate_secrets_2.png "Linking Users to the Kafka Cluster")

Verify that all three users are listed under the 'Associated secrets from AWS Secrets Manager' section.

## 6\. Launch an EC2 Instance for Cluster Configuration [#](kafka_install_amazon#ec2)

To connect to the Kafka cluster and perform the initial ACL setup, create a Linux virtual machine using [Amazon EC2](https://ru.wikipedia.org/wiki/Amazon_EC2) in the same VPC as your Kafka cluster.

Go to 'EC2 \\ Instances' and click 'Launch an instance'. Set the name (in this case 'console') and select the Amazon Linux AMI.

![Deploy EC2 service to set up a cluster](/en/docs/mt5/platform/img/kafka_amazon_ec2_1.png "Deploy EC2 service to set up a cluster")

Below — in the Key pair section — specify the name of the key to access the instance and click 'Create key pair'. Specify the following parameters:

-   Key pair name — kafka\_admin\_key.
-   Key pair type — RSA.
-   Private key format — .pem.

After that, click 'Create key pair' and save the resulting key file.

![Deploy EC2 service to set up a cluster](/en/docs/mt5/platform/img/kafka_amazon_ec2_2.png "Deploy EC2 service to set up a cluster")

Then click 'Launch instance'.

![Deploy EC2 service to set up a cluster](/en/docs/mt5/platform/img/kafka_amazon_ec2_3.png "Deploy EC2 service to set up a cluster")

Once the instance is running, an external IP address will be available for [connecting](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#connect_ec2).

![Deploy EC2 service to set up a cluster](/en/docs/mt5/platform/img/kafka_amazon_ec2_4.png "Deploy EC2 service to set up a cluster")

## 7\. Add Rule to the Security Group [#](kafka_install_amazon#security_group)

Add a rule to security group to allow the EC2 instance to connect to the Kafka cluster. Open the 'Properties' section of the cluster. Scroll to 'Network settings' and click the link under 'Security groups applied':

![Add Rule to the Security Group](/en/docs/mt5/platform/img/kafka_amazon_security_group_1.png "Add Rule to the Security Group")

In the 'Custom TCP' field, specify the security group name (found in the EC2 instance list in the 'Security group name' field). The system will automatically substitute the group ID instead of its name. Also, specify the port range: 9092-9096. Click 'Save rules'.

![Add Rule to the Security Group](/en/docs/mt5/platform/img/kafka_amazon_security_group_2.png "Add Rule to the Security Group")

## 8\. Connect to the EC2 Instance [#](kafka_install_amazon#connect_ec2)

Open PowerShell on your local machine and run the following command to connect to your EC2 instance:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ssh -i "C:\configs\kafka-admin-key.pem" ec2-user@&lt;YOUR_EC2_IP&gt;</span></p></td></tr></tbody></table>

Replace with the correct path to your .pem file and the external IP address of your EC2 instance, which you obtained when [creating](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#ec2) the instance.

Once connected, install required dependences:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo yum update -y</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo yum install java-17-amazon-corretto -y</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">wget https://downloads.apache.org/kafka/4.0.0/kafka_2.13-4.0.0.tgz</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">tar -xvzf kafka_2.13-4.0.0.tgz</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">cd kafka_2.13-4.0.0</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sudo yum install -y telnet nc</span></p></td></tr></tbody></table>

Verify the connection to the Kafka broker:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">nc -zv &lt;broker-address&gt; 9096</span></p></td></tr></tbody></table>

Note that in the connection verification command, a space (not a colon) is used between the address and port.

The broker address is available under 'View client information \\ Private endpoint'.

![Connect to the EC2 Instance](/en/docs/mt5/platform/img/kafka_amazon_ec2_connect_1.png "Connect to the EC2 Instance")

A successful connection means you can proceed to ACL configuration.

## 9\. Configuring ACL Permissions [#](kafka_install_amazon#acl)

Permissions are configured through the same PowerShell console.

Create the file config/kafka\_admin.properties:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">mkdir -p config</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">nano config/kafka_admin.properties</span></p></td></tr></tbody></table>

Add authentication settings and administrator details to it:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">security.protocol=SASL_SSL</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.mechanism=SCRAM-SHA-512</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username="kafka_admin" password="password_kafka_admin";</span></p></td></tr></tbody></table>

Grant administrator privileges:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 1]</span><span class="f_CodeExampleWrap">,</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 2]</span><span class="f_CodeExampleWrap"> --command-config config/kafka_admin.properties --add --allow-principal "User:kafka_admin" --operation All --topic '*' --group '*' --cluster</span></p></td></tr></tbody></table>

Add the Kafka broker addresses to the command. These can be found in the cluster properties as shown in the [previous stage](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#connect_ec2).

Next, create a producer account and grant appropriate permissions. Replace Kafka broker addresses in commands accordingly.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">bin/kafka-configs.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 1]</span><span class="f_CodeExampleWrap">,</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 2]</span><span class="f_CodeExampleWrap"> --command-config config/kafka_admin.properties --alter --add-config 'SCRAM-SHA-512=[password=password_kafka_producer]' --entity-type users --entity-name kafka_producer</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 1]</span><span class="f_CodeExampleWrap">,</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 2]</span><span class="f_CodeExampleWrap"> --command-config config/kafka_admin.properties --add --allow-principal "User:kafka_producer" --operation DESCRIBE --operation READ --operation WRITE --operation CREATE --operation DELETE --topic mt5- --resource-pattern-type prefixed</span></p></td></tr></tbody></table>

Next, create a consumer account and grant appropriate permissions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">bin/kafka-configs.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 1]</span><span class="f_CodeExampleWrap">,</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 2]</span><span class="f_CodeExampleWrap"> --command-config config/kafka_admin.properties --alter --add-config 'SCRAM-SHA-512=[password=password_kafka_consumer]' --entity-type users --entity-name kafka_consumer</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 1]</span><span class="f_CodeExampleWrap">,</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 2]</span><span class="f_CodeExampleWrap"> --command-config config/kafka_admin.properties --add --allow-principal "User:kafka_consumer" --operation DESCRIBE --operation READ --topic mt5- --resource-pattern-type prefixed</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">&nbsp;</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">bin/kafka-acls.sh --bootstrap-server </span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 1]</span><span class="f_CodeExampleWrap">,</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">[broker 2]</span><span class="f_CodeExampleWrap"> --command-config config/kafka_admin.properties --add --allow-principal "User:kafka_consumer" --operation READ --group mt5- --resource-pattern-type prefixed</span></p></td></tr></tbody></table>

Note that both producer and consumer commands grant [prefix](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#topic_full_name) permissions.

## 10\. Kafka Cluster Final Configuration [#](kafka_install_amazon#cluster_configuration)

Create a new cluster configuration, similar to what was done during the [initial setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#configuration) and enter the following parameters under 'Configuration properties \\ Code':

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">auto.create.topics.enable=true</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">default.replication.factor=2</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">min.insync.replicas=1</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">num.partitions=3</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">num.replica.fetchers=2</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">unclean.leader.election.enable=false</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">allow.everyone.if.no.acl.found=false</span></p></td></tr></tbody></table>

Note:

-   auto.create.topics.enable=true — allows MetaTrader 5 to automatically create [topics](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#topics).
-   default.replication.factor=2 — the value must match the number of brokers, otherwise Kafka will not be able to create topics automatically, since it will not be able to collect a quorum.
-   allow.everyone.if.no.acl.found=false — disables cluster access without explicit permission in ACL.

Save the new configuration as 'release'. Then, go to the cluster properties and change the configuration from 'start' to 'release'.

![Kafka Cluster Final Configuration](/en/docs/mt5/platform/img/kafka_amazon_cluster_configuration.png "Kafka Cluster Final Configuration")

## 11\. Enable Public Access to Kafka Cluster [#](kafka_install_amazon#public_access)

Only proceed with this step after ACL configuration is complete.

In the cluster properties, go to 'Network settings' and click 'Edit \\ Edit public access'.

![Enable public access to the Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_public_access_1.png "Enable public access to the Kafka cluster")

Enable 'Public access \\ Turn on' and save the changes.

![Enable public access to the Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_public_access_2.png "Enable public access to the Kafka cluster")

After enabling, public access endpoints will appear. These addresses are required to [connect MetaTrader 5](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming#bootstrap). Go to 'View client information' on the cluster page and navigate to 'Bootstrap servers' to find the addresses. Use the endpoints that support SASL/SCRAM.

![Enable public access to the Kafka cluster](/en/docs/mt5/platform/img/kafka_amazon_public_access_3.png "Enable public access to the Kafka cluster")

Next, add an inbound rule to the Kafka security group with the IP address of your MetaTrader 5 trading server. Go to the 'Properties' section and click the link in the 'Security groups applied' section.

![Add Rule to the Security Group](/en/docs/mt5/platform/img/kafka_amazon_security_group_1.png "Add Rule to the Security Group")

Next, add an inbound rule of the 'Custom TCP' type with your IP address and port range 9192-9196:

![Add Rule to the Security Group](/en/docs/mt5/platform/img/kafka_amazon_public_access_4.png "Add Rule to the Security Group")

## 12\. MetaTrader 5 Configuration [#](kafka_install_amazon#mt5)

to [configure](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming) Kafka connection on the platform side, use the following settings:

-   Login — kafka\_producer
-   Password — password\_kafka\_producer
-   Security — SASL\_SSL / SCRAM-SHA-512. Amazon MSK does not support SCRAM-256.
-   Certificate — download [Starfield Services Root CA - G2](https://www.amazontrust.com/repository/) and specify it here.
-   Topic prefix — mt5-.
-   Bootstrap servers — addresses obtained in the [public access enabling](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#public_access) step. If your trading platform is deployed within the same Amazon Virtual Private Server (VPS), use internal addresses from the 'Private Endpoint' field.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Once the connection between MetaTrader 5 and Kafka is successfully established, you may terminate the <a href="/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#ec2" class="topiclink">EC2 instance</a> and <a href="/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install_amazon#security_group" class="topiclink">disable the corresponding accesses</a>. It is only required for the initial setup. You now have direct public access to the Kafka cluster.</span></p></td></tr></tbody></table>

[Kafka Installation and Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_install)

[Kafka Streaming Setup](/en/docs/mt5/platform/administration/integration/integration_streaming/kafka_streaming)