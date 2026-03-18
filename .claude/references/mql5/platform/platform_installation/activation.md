# Activation

> Source: https://support.metaquotes.net/en/docs/mt5/platform/platform_installation/activation

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
            -   [System Requirements](/en/docs/mt5/platform/platform_installation/requirements)
            -   [System Preparation](/en/docs/mt5/platform/platform_installation/installation_preparations)
            -   [Installation](/en/docs/mt5/platform/platform_installation/installation)
            -   [Activation](/en/docs/mt5/platform/platform_installation/activation)
            -   [White Label](/en/docs/mt5/platform/platform_installation/white_label)
            -   [Fast Deployment](/en/docs/mt5/platform/platform_installation/deployer)
            -   [Console Setup](/en/docs/mt5/platform/platform_installation/console_setup)
            -   [Platform Moving](/en/docs/mt5/platform/platform_installation/platform_move)
            -   [Platform Uninstall](/en/docs/mt5/platform/platform_installation/platform_uninstall)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Installation](/en/docs/mt5/platform/platform_installation)Activation

# Activation

A license given for [installation](/en/docs/mt5/platform/platform_installation) with the platform distribution is non-activated and has several limitations:

-   Only one trade server (main) can be installed in the system;
-   Not more than 100 users can be created;
-   Not more than 5 groups can be created, including four groups created on default.

After installing the platform and [connecting](/en/docs/mt5/platform/administrator/getting_started/server_connect) to the server via the administrator terminal, go to the [start page](/en/docs/mt5/platform/administration/admin_start) and click on "Activate now":

![License Activation](/en/docs/mt5/platform/img/activate_license.png "License Activation")

For launching the activation process, you can also use the "![Activate](/en/docs/mt5/platform/img/activate_icon.png "Activate") Activate" command of the [Services](/en/docs/mt5/platform/administrator/interface/main_menu/menu_services) menu. The following actions are performed during activation:

-   A request is sent to the update server of the developer company;
-   In case of successful license checking, a new activated license is generated; it is bound to the configuration of server where the platform is installed;
-   Activated [license](/en/docs/mt5/platform/components/trade_server/trade_server_structure#license) is sent back to the trade server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The number of license activations is limited. Normally, up to five activations are allowed for one license.</span></p></td></tr></tbody></table>

## Activation Management [#](activation#manage)

To view your activations, visit the "[App Store\\Licenses](https://support.metaquotes.net/en/market/licenses)" section of the technical support website:

![Information about activated licenses](/en/docs/mt5/platform/img/activation_servers.png "Information about activated licenses")

A list of activations of each platform license contains the following data:

-   Server name — the name displayed in client terminals (in the program name, in the Navigator window, etc.). The first part of the name is taken from the appropriate [White Label](/en/docs/mt5/platform/platform_installation/white_label), the second one is used from platform settings (specified on the [start page](/en/docs/mt5/platform/administration/admin_start)).
-   IP — the IP address from which the platform was activated.
-   Build — current platform build. If the build is shown in red, this means there is a [new version](/en/docs/mt5/platform/administration/admin_update) available for the platform. We recommend installing the latest version to ensure the operation stability and to access all the new features of the platform.
-   Created — platform activation date.
-   Last active — the date of the last platform data update (including the platform build). Platforms send related service information to the server every 24 hours, during [optimization time](/en/docs/mt5/platform/administration/admin_network/network_add_edit#optimization). The last activity time is updated each time the data is sent. If no data is received for one month, the date is shown in red, which is a warning about server inactivity. If a platform does not update data for three months, it is automatically removed from the list of available servers in terminals, as well as ["Signals"](https://www.mql5.com/en/signals) and ["Virtual Hosting"](https://www.mql5.com/en/vps) services.

Two types of platform [activations](/en/docs/mt5/platform/platform_installation/activation) are available: main (shown in bold) and non-main.

-   Client terminals can only connect to a platform with the main activation.
-   To enable connections of client terminals, the platform sends information about its access points (installed access servers) to the update server every hour. Information is sent to the server regardless of the activation type, but only access points of the main activation are transmitted to terminals.
-   Servers with non-main activation are not shown in the broker selection dialogs when opening accounts through terminals.

To set a platform activation as main, please contact [Service Desk](/en/docs/mt5/platform/support).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If you move the platform to another server and activate it, the new activation will appear in the list as non-main. As soon as you complete the platform preparation, be sure to contact <a href="/en/docs/mt5/platform/support" class="topiclink">Service Desk</a> to change the activation to main. Otherwise, traders may have problems connecting to the new server, since access points will not be known to client terminals.</span></li><li class="p_tableatten"><span class="f_tableatten">Desktop terminals receive up-to-date information about access points during each account connection. It is recommended to keep at least one old access point operating during 1-2 weeks after migrating the platform to other equipment/hosting provider, so that terminals can receive such information.</span></li><li class="p_tableatten"><span class="f_tableatten">Activation is bound to server hardware. In case you change computer configuration, a new activation from the same IP address can appear in the list. If the list of access points has not changed, this will not affect operation with client terminals. However, we recommend that you contact the support team to switch the new activation to the main one.</span></li></ul></td></tr></tbody></table>

Outdated activation can be removed by clicking![Delete](/en/docs/mt5/platform/img/activation_delete_button.png "Delete"). If you do not have enough permissions to delete activations or do not see the server management section, please contact [Service Desk](https://support.metaquotes.net/en/servicedesk).

[Installation](/en/docs/mt5/platform/platform_installation/installation)

[White Label](/en/docs/mt5/platform/platform_installation/white_label)