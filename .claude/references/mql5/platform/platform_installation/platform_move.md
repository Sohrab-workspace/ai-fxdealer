# Platform migration to new hardware

> Source: https://support.metaquotes.net/en/docs/mt5/platform/platform_installation/platform_move

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Installation](/en/docs/mt5/platform/platform_installation)Platform Moving

# Platform migration to new hardware

If you move the platform to other hardware/hosting provider, in addition to proper platform installation and configuration, it is important to perform a number of actions to ensure uninterrupted service for traders.

## Migration via a backup server

The back-up server replicates the main server data in real time and features its full copy. At any time you can switch to using it manually — this is a quick and automatic procedure. In addition to emergency cases, the procedure can be used for migrating servers to new hardware.

[Install the backup server](/en/docs/mt5/platform/platform_installation/installation#backup) on the computer, to which you plan to migrate the server. After installation, run it for a few days on the new hardware to make sure it operates well.

Restart the backup server right before you switch to it. This will help avoid loss of data [backed up once an hour](/en/docs/mt5/platform/components/backup_server/backup_server_features). As long as the server copies data, its icon will display ![Backup in process](/en/docs/mt5/platform/img/backup_server_backuping_icon.png "Backup in process")(the icon will look like![Backup in process](/en/docs/mt5/platform/img/backup_server_backuping_icon2.png "Backup in process")). Wait until the process is completed and run the "![Switch to backup server](/en/docs/mt5/platform/img/switch_to_bakcup_icon.png "Switch to backup server")Switch to backup server" command in the context menu:

![Switching to the backup server](/en/docs/mt5/platform/img/switching_to_backup.png "Switching to the backup server")

To avoid accidental switching, the platform requires an additional confirmation. In the dialog that appears, enter the required characters and click "Switch".

![Confirming the switching to the backup server](/en/docs/mt5/platform/img/switch_to_backup_confirm.png "Confirming the switching to the backup server")

After the procedure is complete, you will see that the main server and the backup server have swapped their places in the Network section:

Run the same procedure for all other history and trade servers. Then [install new backup servers](/en/docs/mt5/platform/platform_installation/installation#backup) and [access servers](/en/docs/mt5/platform/platform_installation/installation#access). This can be conveniently done using the [fast deployment](/en/docs/mt5/platform/platform_installation/deployer) procedure.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Desktop terminals receive up-to-date information about access points during each account connection. It is recommended to keep at least one old access point operating during 1-2 weeks after migrating the platform to other equipment/hosting provider, so that terminals can receive such information.</span></li><li class="p_tableatten"><span class="f_tableatten">Server migration must only be performed in non-trading hours. When switching to the backup server, it does not copy data which the main server continues to receive.</span></li><li class="p_tableatten"><span class="f_tableatten">In order to prevent important data from being lost, trading operations and changes in the client base are not allowed on the main server right after the start of switching to the backup server. The ban is valid for one minute. If the platform fails to switch to a backup server within this period, the ban is removed.</span></li></ul></td></tr></tbody></table>

## Platform activation after migration

When migration is complete, go to "Services" menu and click "Start Live Update". Go to the [App Store\\Licenses](https://support.metaquotes.net/en/market/licenses) section and make sure the activation is available in the list. Two types of platform [activations](/en/docs/mt5/platform/platform_installation/activation) are available: main and non-main.

-   Client terminals can only connect to a platform with the main activation.
-   To enable connections of client terminals to the platform, the platform sends information about its access points (installed access servers) to the server every hour. Information is sent to the server regardless of the activation type, but only access points of the main activation are transmitted to terminals.
-   Servers with non-main activation are not shown in the broker selection dialogs when opening accounts through terminals.

Thus, to ensure full-featured platform operation, you need to set the new activation as main. To do this, please contact [Service Desk](/en/docs/mt5/platform/support) after completing platform installation.

## Update of Installers

When switching an activation to the main type, support specialists will recompile the client terminal installer for you, i.e. they will include new access points. If you distribute the installer file by yourself, be sure to download its new version from the [Download](https://support.metaquotes.net/en/download) section and update the file on your resources.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_txt">To allow your traders to download the latest installer version any time, we recommend providing them direct terminal download links from the "Download" section. Thus, you will not need to update the files on your resources manually.</span></p></td></tr></tbody></table>

[Console Setup](/en/docs/mt5/platform/platform_installation/console_setup)

[Platform Uninstall](/en/docs/mt5/platform/platform_installation/platform_uninstall)