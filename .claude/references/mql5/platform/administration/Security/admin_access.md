# Firewall

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/security/admin_access

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Security](/en/docs/mt5/platform/administration/security)Firewall

# Firewall

The Firewall section is intended for setting up protection of the system from the access from undesirable IP addresses. If a group of addresses is blocked, no users (client, manager or administrator) from the address inside the specified range will be able to connect to the server. By default all addresses are allowed.

![Firewall](/en/docs/mt5/platform/img/access.png "Firewall")

Checking of any address is performed top-down. Each type of instructions is displayed with a special icon:

-   ![Block](/en/docs/mt5/platform/img/access_block_icon.png "Block") — blocked range of addresses;
-   ![Permit](/en/docs/mt5/platform/img/access_permit_icon.png "Permit") — allowed range of addresses;
-   ![Always permit](/en/docs/mt5/platform/img/access_always_permit_icon.png "Always permit") — range of addresses that are always allowed irrespective of blocking instructions and [antiflood control](/en/docs/mt5/platform/components/access_server/access_server_antiflood).

The last instruction is always applied to an address, irrespective of previous instructions, except for the addresses that are [always allowed](/en/docs/mt5/platform/administration/security/admin_access#action). Thus the position of an instruction in the list is an important condition in the limitation of access from IP addresses. Let's consider an example:

![Instruction example](/en/docs/mt5/platform/img/access_example.png "Instruction example")

In the above example, the allowing instruction (from 192.168.0.20 to 192.168.0.60) is located below the blocking one. This allows to enable access of a certain range within blocked addresses. Only the addresses 192.168.0.0 — 192.168.0.20 and 192.168.0.60 — 192.168.0.100 stay blocked. But if you change places of these instructions, the entire range 192.168.0.0 — 192.168.0.100 will be blocked.

To change positions of instructions in the list, use context menu commands "![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up" and "![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down", ore the same command in [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu or on toolbar [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Do not block address ranges, which include IP used for connecting by the administrator terminal. If such instructions become effective, you won't be able to connect to the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">In case of blocking your own IP address and inability to connect to the server via another administrator account the only way is to stop the main server service, delete the file configs\access.ini and then start the server again. Note that this will lead to deleting all previously created firewall configurations.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Instructions become effective as soon as you press "OK". But they are applied to new connections only. Current connections are not reset.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">You should carefully treat not only access blocking and allowing, but also the position of instructions in the list. Remember, only the last instruction concerning the IP address is applied to it, while all previous ones are ignored.</span></li></ul></td></tr></tbody></table>

## Adding and Modifying Instructions [#](admin_access#add_edit)

In order to add an instruction or modify an existing one, press "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" or "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit", respectively. They can be found in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu. After you press them, the following window will appear:

![Adding/editing instructions](/en/docs/mt5/platform/img/access_add_edit.png "Adding/editing instructions")

The following parameters should be specified in this window:

-   Action — select an action: always permit, permit or block the bellow range of IP addresses;
-   From — starting address of the range. The instruction will be effective starting from this address;
-   To — end address of the range. The instruction will be effective till this address;
-   Comment — a text comment to the instruction.

To finish adding or editing an instruction, press "OK". If you press "Cancel", the window will be closed while changes will not be saved.

A created instruction can be deleted using command "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete" of the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit#delete) menu, [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or the context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">For quick addition of instructions on any of IP addresses, insert it into the Comment field from the clipboard. After you press "Ok", it will be automatically added to fields "From" and "To".</span></li><li class="p_tableatten"><span class="f_tableatten">Additional general information about working with configuration records is given in the <a href="/en/docs/mt5/platform/administration/common_info/common_instructions" class="topiclink">"Working with Instructions"</a> section.</span></li></ul></td></tr></tbody></table>

## Context Menu [#](admin_access#context)

The context menu of Firewall contains the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new instruction;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit the selected instruction;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete the selected instruction;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move the selected instruction up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move the selected instruction down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) firewall settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) firewall settings to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table.

[Certificates](/en/docs/mt5/platform/administration/security/security_certificates)

[Anti DDoS Protection](/en/docs/mt5/platform/administration/security/network_anti_ddos)