# Managers

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_managers

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Managers

# Managers

Users opened in the "manager" group have special rights for administering the system (changing accounts, quoting clients, report generation, etc.).

![Managers' Access Rights](/en/docs/mt4/administrator/img/br_managers.png "Managers' Access Rights")

By default, there is only one manager's account in the system having the "Administrator" right (full access the server settings).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">When setting the server, one administrator's account will automatically be created (Login: 1; Password: manager). After having been authorized for the first time, it is necessary to change the password or to create a new administrator's account, and to remove the current one.</span></li><li class="p_tableatten"><span class="f_tableatten">Considerable increase in the number of administrators can influence the velocity of performing trade operations. That is why it is not recommended to create managers' accounts that will not be used in the future.</span></li></ul></td></tr></tbody></table>

Newly created accounts have no rights for operating in the system initially. To enable the manager's account operation, it is necessary to indicate its rights obviously. The "Add" and "Edit" context menu commands, the corresponding commands of the "Edit" menu, and the ![Add](/en/docs/mt4/administrator/img/ic_config_add.png "Add") and ![Edit](/en/docs/mt4/administrator/img/ic_config_edit.png "Edit") buttons of the toolbar will activate the manager's account setting window.

![Manager's Account Setting](/en/docs/mt4/administrator/img/win_managers.png "Manager's Account Setting")

It is necessary to indicate the manager's login and email in the internal mailing system. In the field named "Available data", there can be specified the maximum amount of days for which the manager will be allowed to request history reports for closed trades, daily reports and server journal. It is also necessary to indicate the list of the clients' groups to be processed separated by commas in the "Groups" field. As a group name, you can indicate the template using the wildcard characters "\*" and "!". For example, the "demo\*" template means that the manager administers all the groups the names which begin with "demo...": "demoforex", "democfd", "demo-jp". If you specify ",!demo\*, \*," then the manager will be able to administer all groups except the ones that begin with "demo...".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The list of groups is only applied for connections via manager terminals. Managers connected via the administrator terminal have access to all groups.</span></p></td></tr></tbody></table>

The additional information about using the mask is given at the [Support Center](https://support.metaquotes.net), [FAQ](https://support.metaquotes.net/en/faq/916) section.

The use of "IP Filter" allows to limit the IP addresses range from which this manager can connect to the server. Using this option, you can, for example, limit the dealers' connections from any addresses beyond your office of local network.

The "Role" field allows manager to play a role: a certain set of rights and requests routing. The "Save As" button allows saving the current set of rights and routing table for securities as a certain manager's role. The "Delete" button removes the selected role of a manager.

Access rights define the block of actions available for the manager:

-   Manager — rights for adding, editing, and removing the clients' accounts. If this right is enable, the manager is able to see the personal details of users (as if the "Personal details" right is enabled);
-   Supervise Trades — rights for watching open positions;
-   Administrator — total access to the server settings;
-   Accountant — a right for performing financial transactions (transferring, crediting, withdrawing) towards clients' accounts;
-   Reports — a right for requesting and receiving various reports concerning clients' operations;
-   Risk Manager — a right to get information about total clients' positions and the company's coverage;
-   Internal Mail System — a right for sending emails via internal mailing system;
-   Journals — a right for requesting and receiving the initial logs of the system operation as a whole;
-   Send News — a right for sending messages in the news flow;
-   Market Watch — a right for sending the own quotes to the data flow, changing spreads and types of performing operations;
-   Connections — an access right for statistics of connected users;
-   Personal details — a right to see personal details of acoounts;
-   Configure server plugins — a right to configure server plugins;
-   Automatic server reports — a right to receive automatic server reports (Log Analyser reports etc.);
-   Dealer — a right for processing clients' requests and performing trade operations on their accounts;
-   Edit/Delete Trades — a special right given to the dealer for changing and deleting clients' open positions (this opportunity is potentially dangerous).

-   Push notifications — a right to send push notifications to clients' mobile devices using the manager terminal. Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 4 Mobile for [iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=download&utm_source=metatrader4.help "iPhone") and [Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=download&utm_source=metatrader4.help "Android"). Detailed information is provided in the manager terminal user guide.

The Routing Table for Securities is intended for separation of manager's rights from those of the dealer based on the instrument group and the lot size. For example, when servicing for a group of real accounts, a manager can only operate with Forex instruments, and another one can only with CFD. Or, when servicing for the same account group, with the same financial instrument, a dealer can service all requests having up to five lots in total (Minimum Lots: 0; Maximum Lots: 5), and another one can with the range between five and ten lots (Minimum Lots: 5; Maximum Lots: 10). The latter one will watch all operations (including those below five lots being serviced by the former dealer), but she/he will process only her/his operations.

Names of instrument groups to be processed by the manager are marked with "Yes" in the "Use" column in the list at the bottom of the window. This allows to configure managers' operations in the most detailed way.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">When creating/setting a manager's account, it is necessary to indicate only the instrument groups which can be processed with the accounts to be serviced by this manager. If, for example, there is a group of real Forex accounts, you should not assign a manager to service it if this manager only operates with CFD instruments.</span></li><li class="p_tableatten"><span class="f_tableatten">Account groups having no one "attached" dealer (a manager having the Dealer right) operate in automatic mode. When a request from a client comes in the server will decide how to process this request. If it finds just one dealer in the list who has this client's group indicated, it sends this request to this dealer. A frequent mistake in settings is that manager accounts are created in which many user groups are indicated (including demoforex groups) and for which the Dealer right is enabled. As a result, the server considers these groups to have a "manual" dealer and tries to re-send the request to this dealer.</span></li></ul></td></tr></tbody></table>

[Group Types](/en/docs/mt4/administrator/administration/ug_groups/group_types)

[Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)