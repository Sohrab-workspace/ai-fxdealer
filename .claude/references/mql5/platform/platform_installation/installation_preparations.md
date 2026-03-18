# System Preparation

> Source: https://support.metaquotes.net/en/docs/mt5/platform/platform_installation/installation_preparations

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Installation](/en/docs/mt5/platform/platform_installation)System Preparation

# System Preparation

An important issue that directly affects the security and stability of the trading platform is the configuration and optimization of your computer with the operating system. This section highlights the main stages of the process:

-   [Configuring the user interface](/en/docs/mt5/platform/platform_installation/installation_preparations#graphics)
-   [Disabling server roles](/en/docs/mt5/platform/platform_installation/installation_preparations#roles)
-   [Removing unneeded programs](/en/docs/mt5/platform/platform_installation/installation_preparations#programs)
-   [Configuring system updates](/en/docs/mt5/platform/platform_installation/installation_preparations#update)
-   [Disabling time synchronization](/en/docs/mt5/platform/platform_installation/installation_preparations#time)
-   [Configuring network connections](/en/docs/mt5/platform/platform_installation/installation_preparations#network_connection)
-   [Configuring Windows firewall](/en/docs/mt5/platform/platform_installation/installation_preparations#firewall)
-   [Disabling sounds](/en/docs/mt5/platform/platform_installation/installation_preparations#sound)
-   [Configuring general performance parameters](/en/docs/mt5/platform/platform_installation/installation_preparations#performance)
-   [Configuring files deletion without moving them to the Recycle Bin.](/en/docs/mt5/platform/platform_installation/installation_preparations#recycle)
-   [Configuring remote access](/en/docs/mt5/platform/platform_installation/installation_preparations#remote)
-   [Configuring antivirus software](/en/docs/mt5/platform/platform_installation/installation_preparations#antivirus)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">After completing configurations, restart the server.</span></li><li class="p_tableatten"><span class="f_tableatten">Please note that these are only recommendations. Use them at your discretion depending on your specific circumstances and needs.</span></li></ul></td></tr></tbody></table>

## Graphical interface [#](installation_preparations#graphics)

First, it is recommended to configure a graphical user interface of the operating system. You should disable anti-aliasing, shadows, menus, transition effects, etc. These settings allow for fast working with the server in remote access.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Additionally, set blank page as a home page in the Internet Explorer options.</span></p></td></tr></tbody></table>

## Disabling server roles [#](installation_preparations#roles)

Disable unnecessary server roles using the server configuration wizard. Launch it via the Administration section and pass through all the steps clicking Next till you see the list of server roles. If there is any active role, select it and click "Next." Skip the next step for configuring the system components by clicking Next. Check the list of removed roles on the confirmation step and click Remove.

![Selecting a server role](/en/docs/mt5/platform/img/configure_server_wizard_role.png "Selecting a server role")

## Removing unneeded programs [#](installation_preparations#programs)

Uninstall any unnecessary programs that can slow down the trading platform or disrupt its security:

-   Web server (Internet Information Server, Apache, etc.);
-   Mail server, DNS server, SNMP, etc.;
-   Databases (Oracle, MSSQL, etc.);
-   Various development environments (IDE), compilers, etc.;
-   .NET and Java environments;
-   Various control agents from the server manufacturer (usually, this is an entire set of default programs) designed to remotely monitor the server.

Launch the wizard for installing and deleting programs. Move to "Uninstall or change a program" and remove unnecessary programs. Remove programs as you see fit depending on your needs and resource efficiency.

## Configuring system updates [#](installation_preparations#update)

Enable auto update with manual installation confirmation in the Control Panel. Fully automated mode is not recommended since Windows does not allow selecting the update installation day. It is recommended to install updates on weekends when the server load is minimal.

![Auto update](/en/docs/mt5/platform/img/configure_server_update.png "Auto update")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Before installing the platform, you should install all necessary updates for your operating system.</span></p></td></tr></tbody></table>

## Disabling time synchronization [#](installation_preparations#time)

System time synchronization should be performed only by the MetaTrader 5 main trade server on the server where the trading platform is installed. Windows Time should be disabled.

The MetaTrader 5 built-in time synchronization service verifies and corrects time (if necessary) once per hour.

In order to disable time synchronization in the operating system, open the "Date and Time" section of the Control Panel. Go to the "Internet Time" tab, enter 127.0.0.1 to the Server field and unflag the automated synchronization:

![Disabling time synchronization](/en/docs/mt5/platform/img/configure_server_time.png "Disabling time synchronization")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the address of the time synchronization server is not specified in the <a href="/en/docs/mt5/platform/administration/admin_time" class="topiclink">time settings</a> of the platform, the Windows Time service is automatically disabled in the operating system when MetaTrader 5 servers are launched.</span></p></td></tr></tbody></table>

## Configuring network connections [#](installation_preparations#network_connection)

Right-click on the active network connection and select Properties:

![Configuring network connections](/en/docs/mt5/platform/img/configure_server_connection.png "Configuring network connections")

On the Networking tab, remove all components except for TCP/IP v4, TCP/IP v6 and Link-Layer Topology Discovery\* protocols. They are helpful when configuring the routing.

## Configuring Windows firewall [#](installation_preparations#firewall)

The [platform installer](/en/docs/mt5/platform/platform_installation) (including the one used during the [quick deployment](/en/docs/mt5/platform/platform_installation/deployer)) automatically adds permissions for the necessary ports to the Windows firewall.

If an additional port should be opened for your platform configuration, go to the Control Panel — Windows Firewall — Additional settings. Create a new inbound rule and select:

-   Program — in case you want to allow connections for a specific application, for example a gateway.
-   Port — if you want to open certain ports regardless of an application.

![Creating an inbound rule for a port in the firewall](/en/docs/mt5/platform/img/firewall_rule_create.png "Creating an inbound rule for a port in the firewall")

Next, set the port number and select "Allow the connection":

![Configuring an inbound rule for a port in the firewall](/en/docs/mt5/platform/img/firewall_rule_setup.png "Configuring an inbound rule for a port in the firewall")

Depending on the location of your PC, specify the profile the rule is applied for: domain, private network or public network. At the last stage, enter a name for the rule.

For each component of the platform, the list of ports that should be allowed is different:

### Access Server

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Ports for outgoing connections</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Reason</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Ports, on which <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server" class="topiclink">trade servers</a> work.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Access servers rout clients' connections to trade servers. In case with the main trade server, additionally configuration files are updated and <a href="/en/docs/mt5/platform/administration/admin_time#synchronization" class="topiclink">time is synchronized</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Port, a <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server" class="topiclink">history server</a> works on.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receiving news, quotes and <a href="/en/docs/mt5/platform/administration/admin_update" class="topiclink">updates</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Port 443.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Connection to MetaQuotes' Updates server (https://updates.metaquotes.net).</span></p></td></tr><tr class="table"><td class="table" style="width:301px; background-color:#DBE9F9;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Ports for incoming connections</span></p></td><td class="table" style="background-color:#DBE9F9;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Reason</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Port the access server works on (<a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit#network" class="topiclink">Bindings</a>).</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">These ports will be listened to for receiving clients' connections.</span></p></td></tr></tbody></table>

### Backup Server

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Ports for outgoing connections</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Reason</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Port of the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server" class="topiclink">main trade server</a>.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Through the main server, configuration files are updated, as well time is synchronized.</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Port of the server, whose <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#backup" class="topiclink">backups are made</a>.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Backup copying of the server data.</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Port, on which a <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server" class="topiclink">history server</a> works.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receiving updates.</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Ports, on which <a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">gateways</a> are running.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Backing up gateway data.</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable">Port 443.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Connection to MetaQuotes' Updates server (https://updates.metaquotes.net).</span></p></td></tr><tr class="table"><td class="table" style="width:301px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit#network" class="topiclink">Access server</a> ports</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Monitoring the availability of the backup server if <a href="/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto" class="topiclink">automatic switch</a> to the backups server is enabled.</span></p></td></tr></tbody></table>

### Trading Server

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Ports for outgoing connections</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Reason</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port 25.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sending <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports" class="topiclink">reports</a> to the mail server.</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port 37.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_time#synchronization" class="topiclink">Time synchronization</a> by the TIME protocol (for the main server).</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port 123.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Time synchronization by the NTP protocol (for the main server).</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port of the main trade server.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receipt of configuration files and time synchronization (for servers other than the main).</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port, on which a history server works.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receiving quotes and updates.</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Ports, on which <a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">gateways</a> are running.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Work with gateways: receiving quotes, trading.</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port 443.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Connection to MetaQuotes' Updates server (https://updates.metaquotes.net).</span></p></td></tr><tr class="table"><td class="table" style="width:303px; background-color:#DBE9F9;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Ports for incoming connections</span></p></td><td class="table" style="background-color:#DBE9F9;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Reason</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port where the trade server works.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">This port is required for the main trade server to connect all other components. For non-main servers it is required for connecting access servers.</span></p></td></tr></tbody></table>

### History Server

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Ports for outgoing connections</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Reason</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port 443.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Connection to MetaQuotes' Updates server (https://updates.metaquotes.net).</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port of the main trade server.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receipt of configuration files and time synchronization.</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Ports, on which data feeds work.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Ports for <a href="/en/docs/mt5/platform/administration/admin_feeds" class="topiclink">data feeds</a> that establish connection to remote servers. For example, <a href="/en/docs/mt5/platform/components/datafeeds/metatrader4feeder" class="topiclink">MetaTrader4Feeder</a> (port 443 is used on default) and <a href="/en/docs/mt5/platform/components/datafeeds/tcnewsfeeder" class="topiclink">TCNewsFeeder</a> (FTP ports 20 or 21 are used on default).</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Ports, on which remote data feeds work.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Port numbers depend on the <a href="/en/docs/mt5/platform/components/datafeeds/remote_datafeed" class="topiclink">data feeds</a> that are connected.</span></p></td></tr><tr class="table"><td class="table" style="width:303px; background-color:#DBE9F9;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Ports for incoming connections</span></p></td><td class="table" style="background-color:#DBE9F9;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Reason</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Port, on which the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server" class="topiclink">history server</a> works.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">This port is required for connecting other components of the platform.</span></p></td></tr><tr class="table"><td class="table" style="width:303px;"><p class="p_fortable"><span class="f_fortable">Ports, on which data feeds work.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Ports, on which <a href="/en/docs/mt5/platform/administration/admin_feeds" class="topiclink">data feeds</a> work, that receive external connections from remote servers. For example, <a href="/en/docs/mt5/platform/components/datafeeds/djprimetassnewsfeeder" class="topiclink">DJPrimeTassNewsFeeder</a> (port 20000 is used on default).</span></p></td></tr></tbody></table>

## Disabling sounds [#](installation_preparations#sound)

Disable sounds for the server the trading server is installed at. Open the Sound section in the Control Panel:

![Disabling sounds](/en/docs/mt5/platform/img/configure_server_sound.png "Disabling sounds")

Select "No Sounds" in the list of sound schemes and click OK.

## Configuration general performance parameters [#](installation_preparations#performance)

Open the Control Panel — System — System Properties — Advanced — Performance settings. Select "Adjust for best performance" on the "Visual Effects" tab:

![Performance settings](/en/docs/mt5/platform/img/configure_server_performance.png "Performance settings")

On the Advanced tab, click Change and enter the value of the initial swap file size equal to its maximum value.

![Configuring the swap file](/en/docs/mt5/platform/img/configure_server_swap.png "Configuring the swap file")

Return to the System Properties — Advanced and open the startup and recovery settings:

![Startup and recovery settings](/en/docs/mt5/platform/img/configure_server_startup.png "Startup and recovery settings")

Disable the "Time to display list of operating systems" option. Set "Write debugging information" to None.

From the control panel, navigate to Hardware — Power Options. Select maximum performance mode:

![Select maximum performance mode in power settings](/en/docs/mt5/platform/img/configure_server_power.png "Select maximum performance mode in power settings")

## Configuring files deletion without moving them to the Recycle Bin [#](installation_preparations#recycle)

In order to ensure the files are deleted immediately, click Properties in the bin's context menu. Select "Don't move files to the Recycle Bin. Remove files immediately when deleted":

![Configuring files deletion without moving them to the Recycle Bin](/en/docs/mt5/platform/img/configure_server_recycle.png "Configuring files deletion without moving them to the Recycle Bin")

## Server Configurator [#](installation_preparations#configurator)

The "Server Configurator" program is specially designed to facilitate the server preliminary configuration process by automating the manual work of terminating various services, system configuration via the registry and deleting temporary and unnecessary information from the disks. You can download this utility from the following link [https://support.metaquotes.net/spfiles/srvcfg.exe](https://support.metaquotes.net/spfiles/srvcfg.exe). The program does not require installation, it can be simply launched through the EXE file. Go through all the steps enabling all the flags. A more detailed description of the Server Configurator can be found in the article "[Using the Server Configurator](https://support.metaquotes.net/en/articles/15)".

## Configuring remote access [#](installation_preparations#remote)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Keep the data for the remote access to the server in a safe place and do not disclose them to anyone without particular reason.</span></p></td></tr></tbody></table>

Blocking RDP connections for accounts having no password. Accounts with no entry password should not have permission for remote access to the server. Open the Control Panel — Administrative Tools — Local Security Policy — Security Options. Enable the parameter "Accounts: Limit local account use of blank passwords to console logon only".

![Blocking RDP connections for accounts having no password](/en/docs/mt5/platform/img/rdp_settings_accounts.png "Blocking RDP connections for accounts having no password")

Changing a standard port for remote connection. In order to protect against the attacks monitoring "well-known" ports, change the port for the Remote Desktop Protocol. Open the registry editor (regedit), go to HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp and find the Port Number parameter. Double-click on it, select the decimal system in the new window and set the necessary port as the value.

![Changing the standard port for remote connection](/en/docs/mt5/platform/img/rdp_settings_port.png "Changing the standard port for remote connection")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The specified port should be permitted in the <a href="/en/docs/mt5/platform/platform_installation/installation_preparations#firewall" class="topiclink">Windows Firewall</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">In order to remotely connect to the server, specify the new port after an IP address separated by a colon. For example, 10.59.162.3:5000.</span></li></ul></td></tr></tbody></table>

Limitation of IP address list for remote connection. As an additional security measure, you can restrict the list of IP addresses that can be used to remotely connect to the server. For example, you can allow connection only from your office's IP addresses.

Open Windows Firewall and find "Remote Desktop - User Mode (TCP-In)" in the list of inbound rules. There may be several such rules depending on the number of network profiles. Open the one you need and go to Scope tab. In the "Remote IP address" section, select "These IP addresses" and add the necessary ones to the list:

![Limiting the list of IP addresses for remote connection](/en/docs/mt5/platform/img/rdp_settings_ip.png "Limiting the list of IP addresses for remote connection")

## Configuring antivirus software [#](installation_preparations#antivirus)

If antivirus software is used on your server, add to its exclusions the system processes of the MetaTrader 5 platform, as well as its installation directory. Constant monitoring by antivirus software reduces platform performance.

Here is an example of adding exclusions in Windows Defender, which is a built-in antivirus software used on Windows Server 2016. Open Windows Settings — Updates and Security — Windows Defender. Go to "Exclusions" and click "Add an exclusion".

![Configuring exclusions in Windows Defender](/en/docs/mt5/platform/img/windows_defender.png "Configuring exclusions in Windows Defender")

Select "Exclude folder" and choose the platform installation directory.

![Adding an exclusion for the platform installation directory](/en/docs/mt5/platform/img/windows_defender_folder.png "Adding an exclusion for the platform installation directory")

Click "Exclude process .exe, .com or .src". Specify the name of the platform component process in the window that opens. You can specify the name of the server executable file (for example mt5trade64.exe) or the name of the process (for example mt5msrv).

![Add an exclusion for the platform installation process](/en/docs/mt5/platform/img/windows_defender_process.png "Add an exclusion for the platform installation process")

Similar exclusions should be added for all installed components of the cluster. The default names of the services are:

-   mt5msrv — the main trade server
-   mt5tsrv — an additional trade server
-   mt5asrv — an access server
-   mt5bsrv — a backup server
-   mt5hsrv — a history server

If several components of the same type are installed, a digit is added to the service name. For example, mt5tsrv5. The list of installed processes can be viewed in the task manager.

[System Requirements](/en/docs/mt5/platform/platform_installation/requirements)

[Installation](/en/docs/mt5/platform/platform_installation/installation)