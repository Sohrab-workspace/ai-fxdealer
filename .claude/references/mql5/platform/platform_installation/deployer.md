# Fast Deployment

> Source: https://support.metaquotes.net/en/docs/mt5/platform/platform_installation/deployer

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Installation](/en/docs/mt5/platform/platform_installation)Fast Deployment

# Fast Deployment

The fast deployment function simplifies installation of the platform's additional components. During a conventional server installation, you should specify its settings twice: during the installation itself and when creating its configuration via the Administrator terminal. Instead, you can first create a correct server configuration and then receive a setup file with all the previously specified settings.

Before the deployment, configure the server network parameters: ID and password to be used by other cluster components for connection to the new server, as well as IP addresses to be used by the new server for sending and receiving data. All these parameters, as well as data for connecting to the platform's main server, are specified in the installation package. Thus, all remaining cluster components are able to connect to the new server immediately after the installation allowing you to manage the server via the Administrator terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The function of deployment is available only for access, backup and additional trade servers.</span></p></td></tr></tbody></table>

## Creating and Configuring the Server

Create a server configuration in the [Network](/en/docs/mt5/platform/administration/admin_network) section by clicking ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add. Specify an ID and a password to be used by other cluster components for connection to the new server on the [Common](/en/docs/mt5/platform/administration/admin_network/network_add_edit#common) tab. Specify IP addresses to be used by the new server to send and receive data on the [Network](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) tab.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Make sure that your <a href="/en/docs/mt5/platform/platform_installation/installation_preparations#network_connection" class="topiclink">network parameters</a> are properly configured and all <a href="/en/docs/mt5/platform/platform_installation/installation_preparations#firewall" class="topiclink">required ports</a> are open, because instant connection to all required servers within the cluster will be needed during deployment.</span></p><p class="p_tableatten"><span class="f_tableatten">If any of the MetaTrader 5 cluster components needs to be deployed on a different subnet (different from the net where the main trade server and the history server are installed), the main and history servers must be accessible via the Internet. Otherwise, the installed component will not be able to connect to these servers.</span></p></td></tr></tbody></table>

![Server Settings](/en/docs/mt5/platform/img/deploy_configure.png "Server Settings")

The created server will be marked by a gray icon (for example,![Inactive server](/en/docs/mt5/platform/img/server_inactive_icon.png "Inactive server")), which means that the server service is not running in the operating system. In our case, such a service is simply not installed.

## Deployment

Click "![Deploy...](/en/docs/mt5/platform/img/deploy_icon.png "Deploy...") Deploy..." in the new server context menu:

![Deploy Server](/en/docs/mt5/platform/img/deploy_menu.png "Deploy Server")

This will open the deployment dialog. Click Deploy and select a folder where the setup file is to be saved.

![Server Deployment](/en/docs/mt5/platform/img/deploy.png "Server Deployment")

A file of the following form will be saved to the specified folder: Deploy\_ID\_ServerName.exe. Here ID is the [internal ID](/en/docs/mt5/platform/administration/admin_network/network_add_edit#identifier) of the server, ServerName — name of the server. Copy the file to the required computer, to the directory from which the installed server will operate. After that run it from the command line with the /install key. For example:

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_CodeExample"><span class="f_CodeExample">D:\MetaTrader&nbsp;5&nbsp;Platform\Backup&nbsp;History\Deploy_5_Backup_Server.exe&nbsp;/install</span></p></td></tr></tbody></table>

The file will install the server with the parameters pre-configured in the MetaTrader 5 Administrator. The results of deployment are written in a text file Deploy\_ID\_ServerName.txt, located in the same directory.

![Starting Deployment](/en/docs/mt5/platform/img/deploy_cmd.png "Starting Deployment")

During installation, the availability of a network connection to the main and historical servers of the platform is checked. When installing a backup server, the system additionally checks the connection to the primary server. If the connection cannot be established, the installation is aborted and the relevant message is added to the log. To ignore errors and to install the component anyway, restart the installer with the additional /nochecks switch.

After installation you can [configure other parameters of the server](/en/docs/mt5/platform/administration/admin_network/network_add_edit).

## Additional Parameters of Installation

The deployer file can be run with additional parameters specified in the command line:

-   /nogui — in an operating system with UAC (User Account Control) enabled, running the deployer file may require higher privilege (administrator rights) and evoke a window with the corresponding request. When running the deployer file with this parameter, an attempt to acquire higher privilege is not made.
-   /main:address:port — using this parameter, you can redefine the address of the main trade server in the configuration of the server installed.
-   /history:address:port — using this parameter, you can redefine the address of the history server in the configuration of the server installed.
-   /name:name — using this parameter, you can define a short name of the service of the server installed.
-   /display:display — using this parameter, you can define a full name of the service of the server installed.
-   /desc:description — using this parameter, you can define a description of the service of the server installed.

An example of running the file with additional parameters: Deploy\_5\_AccessSever.exe /install /main:192.168.1.135:433 /name:mt5accesssrv.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The server will be automatically configured according to the settings specified for it in the administrator terminal.</span></li><li class="p_tableatten"><span class="f_tableatten">The server is installed in the folder, from which the deployer was started.</span></li><li class="p_tableatten"><span class="f_tableatten">After deploying a server you should <a href="/en/docs/mt5/platform/administration/admin_network/restart" class="topiclink">restart</a> the main trade server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If a component is installed in another subnetwork (different from the one, where the main trade and the history servers are installed), the main trade server and the history server must be accessible via the Internet. Otherwise, the newly installed component will not be able to connect to them.</span></li><li class="p_tableatten"><span class="f_tableatten">In case of deploying a trade server, a manager account is created on it. It is required for the first connection to the server. The account login and password are saved in the log file of the server (/Logs folder). The log record looks as following: default manager with login '1000' and password 'lfd5fircvs' added</span></li></ul></td></tr></tbody></table>

## Removing the Server

To remove the service of the installed server from the operating system, you can use the corresponding [console command](/en/docs/mt5/platform/platform_installation/console_setup) of the server (/uninstall). After that, the folder where the server was installed, can be removed physically from the disk.

[White Label](/en/docs/mt5/platform/platform_installation/white_label)

[Console Setup](/en/docs/mt5/platform/platform_installation/console_setup)