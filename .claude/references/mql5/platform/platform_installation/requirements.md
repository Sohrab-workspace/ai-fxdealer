# System Requirements

> Source: https://support.metaquotes.net/en/docs/mt5/platform/platform_installation/requirements

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Installation](/en/docs/mt5/platform/platform_installation)System Requirements

# System Requirements

The MetaTrader 5 platform components are recommended to be installed on dedicated servers rented from hosting companies.

## Hardware

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:10%;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></th><th class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Minimum requirements</span></p></th><th class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Recommended requirements</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:10%;"><p class="p_fortable"><span class="f_fortable">CPU</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">AMD EPYC 4XXX or higher</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">AMD EPYC 7XXX or higher</span></p></td></tr><tr class="table"><td class="table" style="width:10%;"><p class="p_fortable"><span class="f_fortable">RAM</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">No less than 16GB</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">No less than 32GB</span></p></td></tr><tr class="table"><td class="table" style="width:10%;"><p class="p_fortable"><span class="f_fortable">Disk</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">RAID-1 array with 2 x 1 TB disks</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">RAID-1 array with two 1 TB SSD/NVMe disks for the trade server and the history server, RAID-1 array with 2 x 1 TB for backup servers</span></p></td></tr><tr class="table"><td class="table" style="width:10%;"><p class="p_fortable"><span class="f_fortable">Network</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">Both download and upload speed no less than 100 Mbps</span></p></td><td class="table" style="width:40%;"><p class="p_fortable"><span class="f_fortable">Both download and upload speed no less than 1 Gbps</span></p></td></tr><tr class="table"><td class="table" style="width:10%;"><p class="p_fortable"><span class="f_fortable">Operating System</span></p></td><td class="table" style="width:20%;"><p class="p_fortable"><span class="f_fortable">Windows Server 2022 Standard x64 or newer</span></p></td><td class="table" style="width:20%;"><p class="p_fortable"><span class="f_fortable">Windows Server 2025 Standard / Server Core edition</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The processor must support <a href="https://en.wikipedia.org/wiki/Advanced_Vector_Extensions" target="_blank" class="weblink">AVX2</a> instructions to enable platform installation.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Choose a server configuration depending on the number of clients, financial instruments and the density of quotes stream. When databases grow, causing an increased load on the trading platform, event the initially recommended configuration may be fail to cope with such load.</span></li><li class="p_tableatten"><span class="f_tableatten">Due to the fact that the backup server is basically a duplicate of the main trading server, it is desirable that the configuration of the backup server is similar or even identical to the configuration of the main server. It's not recommended to place the backup server at the same hosting company as the main server, as it may happen that the entire network of the provider will be unavailable. Locating the servers at different hosting companies increases data security and the resiliency of the system.</span></li><li class="p_tableatten"><span class="f_tableatten">History server processes and stores a huge volume of information. Due to this fact, important criteria for it are disk volume and disk read/write speed.</span></li></ul></td></tr></tbody></table>

## Additional Requirements

-   No third-party software for system time synchronization is allowed.
-   Use virtualization if you have control over the hypervisor and can ensure enough resources for the virtual machine running MetaTrader 5. At least 8 logical cores must be available to the virtual machine (virtual processors are specified here, unlike physical ones used for dedicated servers). The machine should support the Over-Provisioning technology and have the disk speed of no less than 30 MB/s.
-   Configure BIOS on the server to run low-latency applications: turn all the energy saving features off (including CPU C-state), configure memory settings to the 'High Performance' state.

## Recommended basic cluster configuration [#](requirements#recommended)

We recommend renting at least two servers. It is advisable to have servers that are physically located in different data centers. One server is to be used as the main one. The second server is used as the backup one. The main server data is to be replicated to it in real time. Thus, even if one of the hosting providers has troubles, you will be able to restore the platform on the backup server. This will allow you to minimize risks, while the probability of failure in both data centers is very small.

The following platform components should be installed on the main and backup servers:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Main server</span></p></th><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Standby server</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Main trade server</span></p><p class="p_fortable"><span class="f_fortable">History server</span></p><p class="p_fortable"><span class="f_fortable">Access server</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Backup server for the main trade server</span></p><p class="p_fortable"><span class="f_fortable">Backup server for the history server</span></p><p class="p_fortable"><span class="f_fortable">Access server</span></p></td></tr></tbody></table>

Components can be installed in different physical servers within one data center, in order to provide a greater platform performance.

![The recommended basic platform configuration](/en/docs/mt5/platform/img/platform_configuration_diagram.png "The recommended basic platform configuration")

In MetaTrader 5 Administrator, suggested configuration looks as follows:

![Recommended basic platform configuration](/en/docs/mt5/platform/img/platform_configuration_admin.png "Recommended basic platform configuration")

It is strongly recommended to install the history server close to trade servers in order to avoid delays when delivering quotes and sending trading operations to external systems through gateways.

[Platform Installation](/en/docs/mt5/platform/platform_installation)

[System Preparation](/en/docs/mt5/platform/platform_installation/installation_preparations)