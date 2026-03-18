# IP Access List

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_access

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)IP Access List

# IP Access List

The "IP Access List" section is intended for setting the fetch protection system. For example, you found out that some negative actions were made from one or several subnetworks. In such cases, you can block the entire subnetwork(s). If the access permission is needed for a part of IP-addresses included into the list of blocked ones, the instruction permitting the access must be located lower than that of blocking. When a group of addresses is blocked, no user (client, manager, administrator) can connect the server from any address inside the blocked group.

Up to 511 rules of access right limitation from different addresses. By default, all addresses are considered as permitted.

![Access Settings](/en/docs/mt4/administrator/img/br_access.png "Access Settings")

Each address check is made top-to-bottom. The last rule concerning the address should be applied to it regardless of former instructions. Thus, the position of each instruction in the list is a very important condition for access right limitation for IP-addresses. In the example given above, the permitting instruction is located lower than that of blocking and this allows to create a pass within the range of the blocked addresses. But the interchanging the instructions disables this pass since the latest access rule prescribes blocking the whole list. In this case, the permitting instruction will be simply ignored.

The "permit always" rule is applied irrespective of its position in the list. If this rule is met for an IP address, all further instructions will be ignored. Addresses marked as "permit always" are not check by the [Antiflood control](/en/docs/mt4/administrator/administration/ug_options#antiflood) system.

To configure the instruction location in the list, the context menu commands as "Move Up" and "Move Down" should be used, as well as the same commands in the "Edit" menu, and the following buttons of the toolbar: ![Move Up](/en/docs/mt4/administrator/img/ic_config_up.png "Move Up") and ![Move Down](/en/docs/mt4/administrator/img/ic_config_down.png "Move Down").

When adding or editing a rule (with the context menu "Add" and "Edit" commands, as well as the same commands of the "Edit" menu, and the following buttons of the toolbar: ![Add](/en/docs/mt4/administrator/img/ic_config_add.png "Add") and ![Edit](/en/docs/mt4/administrator/img/ic_config_edit.png "Edit")) the setting window will open:

![Access Settings](/en/docs/mt4/administrator/img/win_access.png "Access Settings")

-   Action — action applying to the given list of IP-addresses (Block — block access; Permit — permit access);
-   From — IP-address to be the first to which the given access rule will be applied;
-   To — IP-address to be the last to which the given access rule will be applied;
-   Comment — the text of comment.

The context menu "Delete" command, as well as the "Edit" menu command and the button of ![Delete](/en/docs/mt4/administrator/img/ic_config_delete.png "Delete") on the toolbar will delete the instruction selected.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Warnings:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Do not block the IP-addresses list including the IP-address used by the administrator when connecting to the server. After the access rules have come into effect, you will not be able to connect to the server.</span></li><li class="p_tableatten"><span class="f_tableatten">You should think over in detail both the rules of access blocking and permission, and their location in the list. Keep in mind that only the latest rule concerning the given address can apply to this address. All preceding rules will be — ignored.</span></li></ul></td></tr></tbody></table>

[Gateway](/en/docs/mt4/administrator/administration/gateway)

[Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)