# Live Update

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/live_update

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
            -   [Install Terminal](/en/docs/mt5/platform/administrator/getting_started/administrator_installation)
            -   [Start Terminal](/en/docs/mt5/platform/administrator/getting_started/launch)
            -   [Structure of Directories and Files](/en/docs/mt5/platform/administrator/getting_started/structure)
            -   [Add or Remove Servers](/en/docs/mt5/platform/administrator/getting_started/server_add_delete)
            -   [Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Getting Started](/en/docs/mt5/platform/administrator/getting_started)Live Update

# Live Update

A system of automatic updates is built into the terminal. It allows to get informed about and install new versions of the program promptly. This system is always enabled, it is impossible to disable it. Updating of all components of the trading platform can be managed at the ["Live Update"](/en/docs/mt5/platform/administration/admin_update) section.

## Updating Procedure

The terminal checks for new versions of the program when it connects to the server. If a new version of any of the terminal components has been discovered, it will be automatically downloaded in the background mode.

After all the updates have been downloaded, the below window offering to update the terminal will appear:

![Update](/en/docs/mt5/platform/img/live_update.png "Update")

One of the buttons must be pressed in this window:

-   Restart — if this button is pressed, window of the terminal will be closed, the terminal will be updated and automatically re-opened.
-   Later — in this case the window will be hidden and the terminal will be automatically updated during the next launch.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">All the stages of the updating are reflected in the administrator terminal <a href="/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal" class="topiclink">journal</a>. "LiveUpdate" is specified in the Server column of such entries.</span></li><li class="p_tableatten"><span class="f_tableatten">In case of unsuccessful updating (server connection lost) the next attempt is performed one hour later. In this case only missing data will be additionally downloaded.</span></li></ul></td></tr></tbody></table>

## Update in the Guest Mode

If an administrator terminal has been launched in the [guest mode](/en/docs/mt5/platform/administrator/getting_started/launch#guest) (if the OS user has insufficient rights), a window requesting the increase of the user's permissions will be shown at the attempt to update.

### Microsoft Windows XP

![Update in MS Windows XP](/en/docs/mt5/platform/img/live_update_xp.png "Update in MS Windows XP")

In this case you are requested to specify details of the administrator account with enough permission to write files into the terminal installation directory.

### Microsoft Windows Vista

![Update in MS Windows Vista](/en/docs/mt5/platform/img/live_update_vista.png "Update in MS Windows Vista")

Depending on the user's permissions in MS Windows Vista, it is necessary either to allow the operation (if a user is an administrator) or specify administrator's account details.

[Change Password](/en/docs/mt5/platform/administrator/getting_started/change_password)

[Uninstall Terminal](/en/docs/mt5/platform/administrator/getting_started/deinstallation)