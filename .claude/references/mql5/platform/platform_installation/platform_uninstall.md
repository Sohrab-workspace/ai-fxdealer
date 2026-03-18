# Platform Uninstall

> Source: https://support.metaquotes.net/en/docs/mt5/platform/platform_installation/platform_uninstall

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Installation](/en/docs/mt5/platform/platform_installation)Platform Uninstall

# Platform Uninstall

To remove the entire platform or one of its components, start file uninstall.exe located in the program directory or execute the "Uninstall" command in the corresponding group of programs in the "Start" menu. The following window will appear after that:

![Platform uininstall](/en/docs/mt5/platform/img/platform_uninstall.png "Platform uininstall")

In the greeting window, read the deinstallation warning. If you are sure that want to continue the deinstallation process, press "Next".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When a platform is removed, configurations and databases are not removed on default. In order to perform the full removal, enable the corresponding option on the next deinstallation stage.</span></p></td></tr></tbody></table>

![Parameters of deinstallation](/en/docs/mt5/platform/img/platform_uninstall_settings.png "Parameters of deinstallation")

All currently installed platform components are shown in the left part of the window. Tick off ![Selected Server](/en/docs/mt5/platform/img/access_permit_icon.png "Selected Server") servers that you want to remove. Information about the component selected in the tree-like list is shown in the right part of the window. The following details are shown:

-   Server address — IP address of a selected server;
-   Server port — port of a selected server;
-   Server ID — ID of a selected server used for its internal identification;
-   Service name — name of the service, under which the server works in the operating system.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To delete the server configurations and data bases, select "Delete server data bases". Be maximally attentive with this option, because in this case data recovery will be impossible. However, if data bases were not deleted, the platform can be recovered then with all the data and configurations.</span></li><li class="p_tableatten"><span class="f_tableatten">The option of data base deletion is enabled separately for each separate server.</span></li></ul></td></tr></tbody></table>

After you press "Next" all the selected platform components will be deleted.

![Deinstallation completion](/en/docs/mt5/platform/img/platform_uninstall_finish.png "Deinstallation completion")

To complete the deinstallation process press "Done".

[Platform Moving](/en/docs/mt5/platform/platform_installation/platform_move)

[Platform Components](/en/docs/mt5/platform/components)