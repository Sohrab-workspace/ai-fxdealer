# Connect to Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_connect

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
            -   [Install Terminal](/en/docs/mt5/platform/administrator/getting_started/administrator_installation)
            -   [Start Terminal](/en/docs/mt5/platform/administrator/getting_started/launch)
            -   [Structure of Directories and Files](/en/docs/mt5/platform/administrator/getting_started/structure)
            -   [Add or Remove Servers](/en/docs/mt5/platform/administrator/getting_started/server_add_delete)
            -   [Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)
                -   [Extended Authorization](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization)
                -   [2FA/TOTP](/en/docs/mt5/platform/administrator/getting_started/server_connect/otp)
            -   [Change Password](/en/docs/mt5/platform/administrator/getting_started/change_password)
            -   [Live Update](/en/docs/mt5/platform/administrator/getting_started/live_update)
            -   [Uninstall Terminal](/en/docs/mt5/platform/administrator/getting_started/deinstallation)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
        -   [Terminal Settings](/en/docs/mt5/platform/administrator/settings)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Getting Started](/en/docs/mt5/platform/administrator/getting_started)Connect to Server

# Connect to Server

To start administering a server, one should connect to it. The "![Connect](/en/docs/mt5/platform/img/connect_button.png "Connect") Connect" command of the ["File"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_file#connect) menu, the similar command of the [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) and the corresponding command of the context menu are used for it. Once one of them is pressed the following window will appear:

![Authorization](/en/docs/mt5/platform/img/authorization.png "Authorization")

The window contains the following fields:

-   Server — this field contains the server the connection to which will be performed. From the list here one can choose any server from those [added](/en/docs/mt5/platform/administrator/getting_started/server_add_delete) to the terminal.
-   Login — administrator account (login), using which the connection to the server will be performed. If such an account has not been created on the server, connection is impossible.
-   Password — administrator password.
-   Save Password —  save password between program restarts.

In order to connect to a server, one should press the "Login" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">To be able to connect to a server, one should first <a href="/en/docs/mt5/platform/administrator/getting_started/server_add_delete" class="topiclink">add</a> it to the administrator terminal.</span></li><li class="p_tableatten"><span class="f_tableatten">In case the mode of extended authorization is enabled for <a href="/en/docs/mt5/platform/administration/admin_groups" class="topiclink">managers</a>, the procedure of additional authorization is conducted.</span></li><li class="p_tableatten"><span class="f_tableatten">If the connection to the administered servers is performed through a proxy server, it is necessary to <a href="/en/docs/mt5/platform/administrator/settings/settings_common#proxy" class="topiclink">set up the terminal</a> in the corresponding way.</span></li></ul></td></tr></tbody></table>

If the authorization is successful, the connection icon ![Connected](/en/docs/mt5/platform/img/status_bar_connected.png "Connected") appears in the [status bar](/en/docs/mt5/platform/administrator/interface/status_bar), as well as two following entries appear in the [journal](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal):

1.  'login number' authorized on 'server name';
2.  'login number' configuration synchronized with 'server name'.

After the successful authorization you can start administering the server. If any problems occur while connecting to the server and you don't get one of the messages mentioned above, you should check the correctness of all specified connection settings, address and port of the server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">While performing <a href="/en/docs/mt5/platform/platform_installation/installation#full" class="topiclink">full installation</a> of the platform one <a href="/en/docs/mt5/platform/administration/admin_managers" class="topiclink">administrator account</a> with login "1001" and random password is automatically created.</span></p></td></tr></tbody></table>

If there are several [trade servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server) within the platform, note that different accounts are used to connect to each of them.

An administrator connected to the main trade server can set up the whole trading platform and manage trade databases and account databases of this server. The main server administrator configures [groups](/en/docs/mt5/platform/administration/admin_groups), [symbols](/en/docs/mt5/platform/administration/admin_symbols), [security settings](/en/docs/mt5/platform/administration/security/admin_access), etc.

Administrator of additional trade servers do not have an access to the platform settings, but they can manage trade and account databases of their specific servers.

## Forced Change of Password [#](server_connect#change_password)

After authorizing you may be asked to change master password to your account. The forced change of password can be enabled in the [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#change_password) or in the [account settings](/en/docs/mt5/platform/administration/admin_accounts/account_edit#change_password). The procedure of master password changing, whether at first login or periodically, increases the security of working.

![Changing Master Password](/en/docs/mt5/platform/img/change_master_password.png "Changing Master Password")

Type a new password in the "New password" field and them type it again in the "Confirm password" field. The new password must comply with the following requirements:

-   It must be no shorter than the length requirement displayed in the password change dialog. The minimum number of characters is determined by [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#minimum_password), while the lowest possible value is 8 characters. The maximum length is 16 characters.

-   It must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj.

-   It should not be the same as the previous password.

[Add or Remove Servers](/en/docs/mt5/platform/administrator/getting_started/server_add_delete)

[Extended Authorization](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization)