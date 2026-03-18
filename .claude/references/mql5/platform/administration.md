# Administration

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)Platform Setup

# Administration

The administration of the online trading platform includes managing of not only the trade server but also of the intermediate components (access points, backup servers, history server, etc.). The administration is divided into categories represented as a tree-like list in the left part of the [MetaTrader 5 Administrator](/en/docs/mt5/platform/administrator):

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; width:242px; padding:5px; border:none"><p class="p_fortable"><img class="help" alt="Administration" title="Administration" width="250" height="1286" src="/en/docs/mt5/platform/img/tree.png"></p></td><td style="vertical-align:top; padding:5px; border:none"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><ul><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_start" class="topiclink">Start Page</a> — general information about the platform, live update settings</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_network" class="topiclink">Network Cluster</a> — settings of platform components</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/integration" class="topiclink">Integrations</a> — configuring mail servers, messengers and access to Finteza analytics</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/automation" class="topiclink">Automations</a> — configuring scenario-based automated actions</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/security/security_certificates" class="topiclink">Certificates</a> — configuring certificates for extended authentication</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/security/admin_access" class="topiclink">Firewall</a> — configuring access by IP addresses</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/security/network_anti_ddos" class="topiclink">Anti DDoS Protection</a> — integration with external protection providers</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_time" class="topiclink">Time</a> — general time settings of the server and setting of trade time</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_holidays" class="topiclink">Holidays</a> — holiday settings</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/leverages" class="topiclink">Leverages</a> — floating margin settings</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_groups" class="topiclink">Groups</a> — account group settings</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups" class="topiclink">Allocations</a> — configuring the opening of demo and preliminary accounts through client terminals</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/clients" class="topiclink">Clients</a> — working with customer data, documents and accounts</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_managers" class="topiclink">Managers</a> — administration of manager accounts</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_accounts" class="topiclink">Trade Accounts</a> — working with accounts</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_accounts/corporate_links" class="topiclink">Corporate links</a> — adding custom links to the client terminals</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_positions" class="topiclink">Positions</a> — working with positions</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_orders" class="topiclink">Orders</a> — working with orders</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_deals" class="topiclink">Deals</a> — working with deals</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/payments" class="topiclink">Payments</a> — integration with payment systems</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">Gateways</a> — administration of gateways that provide interaction with exchanges</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/ultency" class="topiclink">Ultency Matching Engine</a> — administration of Ultency, a liquidity integration and order matching engine</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_feeds" class="topiclink">Data Feeds</a> — configuring quotes and news sources</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_plugins" class="topiclink">Plugins</a> — modules of expanding the platform functionality</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_reports" class="topiclink">Reports</a> — report settings</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/ecn" class="topiclink">ECN</a> — configuring the built-in electronic communication network</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/requests_routing" class="topiclink">Routing</a> — rules of processing of coming trade requests</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/fund_etf" class="topiclink">Funds &amp; ETF</a> — controlling fund settings: commissions, managers, investors</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_symbols" class="topiclink">Symbols</a> — configuring financial instruments</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/spreads" class="topiclink">Spreads</a> — configuring margin requirements for positions in spread</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_charts" class="topiclink">1 Minute History Charts</a> — working with price data stored at the server</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_ticks" class="topiclink">Bid/Ask/Last Ticks</a> — viewing tick data</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_synchronization" class="topiclink">Synchronization</a> — configuring synchronization with other MetaTrader servers</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/subscriptions" class="topiclink">Subscriptions</a> — configuring subscriptions for additional trader services</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/mail" class="topiclink">Mailbox</a> — built-in email system for communicating with traders and colleagues</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_update" class="topiclink">Live Update</a> — configuring automatic updating of the system components</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/support" class="topiclink">Support Center</a> — this section offers help for the MetaTrader 5 platform users: articles, news, answers to frequently asked questions and a possibility to contact the technical support team directly</span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/appstore" class="topiclink">App Store</a> — store of additional components for the trading platform: gateways, liquidity, CRM and others</span></li></ul></td></tr></tbody></table>

[Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)

[General Information](/en/docs/mt5/platform/administration/common_info)