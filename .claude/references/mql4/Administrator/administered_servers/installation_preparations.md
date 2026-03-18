# System Preparation

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administered_servers/installation_preparations

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
            -   [Add or Remove Server](/en/docs/mt4/administrator/administered_servers/ug_server_add)
            -   [Login to Server](/en/docs/mt4/administrator/administered_servers/ug_server_login)
            -   [Change Password](/en/docs/mt4/administrator/administered_servers/ug_server_password)
            -   [System Requirements](/en/docs/mt4/administrator/administered_servers/requirements)
            -   [System Preparation](/en/docs/mt4/administrator/administered_servers/installation_preparations)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Managed Servers](/en/docs/mt4/administrator/administered_servers)System Preparation

# System Preparation

An important step which directly affects the security and stability of the trading platform, is the configuration and optimization of your computer with the operating system. This section covers the main features of this process:

-   [GUI customization](/en/docs/mt4/administrator/administered_servers/installation_preparations#graphics)
-   [Disabling server roles](/en/docs/mt4/administrator/administered_servers/installation_preparations#roles)
-   [Removing unnecessary programs](/en/docs/mt4/administrator/administered_servers/installation_preparations#programs)
-   [Configuring system updates](/en/docs/mt4/administrator/administered_servers/installation_preparations#update)
-   [Disabling time synchronization](/en/docs/mt4/administrator/administered_servers/installation_preparations#time)
-   [Configuring network connections](/en/docs/mt4/administrator/administered_servers/installation_preparations#network_connection)
-   [Configuring Windows Firewall](/en/docs/mt4/administrator/administered_servers/installation_preparations#firewall)
-   [Disabling sounds](/en/docs/mt4/administrator/administered_servers/installation_preparations#sound)
-   [Configuring general performance parameters](/en/docs/mt4/administrator/administered_servers/installation_preparations#performance)
-   [Configuring file deletion without moving them to the recycle bin](/en/docs/mt4/administrator/administered_servers/installation_preparations#recycle)
-   [Server Configurator](/en/docs/mt4/administrator/administered_servers/installation_preparations#configurator)
-   [Configuring remote access](/en/docs/mt4/administrator/administered_servers/installation_preparations#remote)
-   [Configuring antivirus software](/en/docs/mt4/administrator/administered_servers/installation_preparations#antivirus)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To complete the setup,you should restart the server.</span></li><li class="p_tableatten"><span class="f_tableatten">These instructions are recommendations, so you should use them at your own discretion and depending on your specific conditions and requirements.</span></li></ul></td></tr></tbody></table>

## Graphical interface [#](installation_preparations#graphics)

First, it is recommended to configure a graphical user interface of the operating system. Disable anti-aliasing, shadows, menus, transition effects, etc. These settings enable faster operations with the server in remote access mode.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Additionally, it is recommended to set a blank page as the home page in the Internet browser properties.</span></p></td></tr></tbody></table>

## Disabling server roles [#](installation_preparations#roles)

Disable all server roles using the "Server Manager". Launch the Server Manager from the Administration section and complete all steps by clicking Next, until you see the list of server roles. If any of the roles are active, select these roles and click Next. Skip the next step, where system components are configured, by clicking Next. At the confirmation step, check the list of roles to be removed and click Remove.

![Server role selection](/en/docs/mt4/administrator/img/configure_server_wizard_role.png "Server role selection")

## Removing unnecessary programs [#](installation_preparations#programs)

Uninstall all programs which may slow down the trading platform or may negatively affect its security:

-   Web server (Internet Information Server, Apache, etc.)
-   Mail server, DNS server, SNMP, etc.
-   Databases (Oracle, MSSQL, etc.)
-   Various development environment (IDE), compiler, etc.
-   Environments .NET and Java
-   Various control agents from the server manufacturer, usually this is a whole set of default programs, intended to remotely monitor the server.

Run the Add/Remove Programs wizard to remove programs. Go to Programs and Features and uninstall all the specified programs.

## Configuring system updates [#](installation_preparations#update)

In the control panel, enable automatic downloading of updates with manual confirmation of installation. The fully automated mode is not recommended as Windows server does not allow the selection of the day on which updates should be installed. We recommend installing the updates on weekends, when the server load is minimal.

![Auto update](/en/docs/mt4/administrator/img/configure_server_update.png "Auto update")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Make sure to install all operating system updates, before installing the platform.</span></p></td></tr></tbody></table>

## Disabling time synchronization [#](installation_preparations#time)

Time synchronization on the server where the platform is installed, must only be performed by the MetaTrader 4 trading server. Windows Time sync service must be disabled.

MetaTrader 4 time synchronization service verifies and corrects time (if necessary) once an hour.

To disable time synchronization in the operating system, open the "Date and Time" section in Control Panel. Navigate to the Internet Time tab, enter 127.0.0.1 in the "Server" field and uncheck the box next to automatic synchronization:

![Disabling time synchronization](/en/docs/mt4/administrator/img/configure_server_time.png "Disabling time synchronization")

## Configuring network connections [#](installation_preparations#network_connection)

Right-click on an active network connection and choose Properties:

![Configuring network connections](/en/docs/mt4/administrator/img/configure_server_connection.png "Configuring network connections")

In the Network tab, remove all components except TCP/IP v4 and TCP/IP v6. The list one can be unchecked, while it is not used by the platform.

## Configuring Windows Firewall [#](installation_preparations#firewall)

The Platform Installer automatically adds permissions for the required ports in Windows Firewall.

If your platform configuration needs an additional port, navigate to Control Panel — Windows Firewall — Advanced settings. Create a new inbound rule and select "Port":

![Create an inbound Firewall rule for a port](/en/docs/mt4/administrator/img/firewall_rule_create.png "Create an inbound Firewall rule for a port")

Next, specify the port number and select "Allow the connection":

![Configure an inbound Firewall rule for a port](/en/docs/mt4/administrator/img/firewall_rule_setup.png "Configure an inbound Firewall rule for a port")

Next, depending on your computer location, specify the profile for which the rule shall apply: domain, private network or public network. In the last step, give the rule a name.

## Disabling sounds [#](installation_preparations#sound)

Sound notifications will not be used om the server where the trading server is installed, and thus they should be disabled. Open Sounds in Control Panel:

![Disabling sounds](/en/docs/mt4/administrator/img/configure_server_sound.png "Disabling sounds")

In the list of sound schemes, select No Sound and click OK.

## Configuring general performance parameters [#](installation_preparations#performance)

Open the control panel, then System — System Properties — Advanced — Performance Options. On the Visual Effects tab, select "Adjust for best performance":

![Performance settings](/en/docs/mt4/administrator/img/configure_server_performance.png "Performance settings")

Navigate to the Advanced tab, click Change..., and set the initial paging file size to the maximum value.

![Adjusting the paging file](/en/docs/mt4/administrator/img/configure_server_swap.png "Adjusting the paging file")

Return to the System Properties — Advanced dialog and go to the Startup and Recovery settings:

![Startup and recovery settings](/en/docs/mt4/administrator/img/configure_server_startup.png "Startup and recovery settings")

Disable the "Display List of Operating Systems" option. In the Write Debugging Information item, select "None".

From the control panel, navigate to Hardware — Power Options. Select the high performance mode:

![Select the high performance mode in power settings](/en/docs/mt4/administrator/img/configure_server_power.png "Select the high performance mode in power settings")

## Configuring file deletion without moving them to the recycle bin [#](installation_preparations#recycle)

To delete files immediately, without moving to the recycle bin, click "Properties" in its context menu. Select "Don't move files to the Recycle Bin. Remove files immediately when deleted":

![Configuring file deletion without moving them to the recycle bin](/en/docs/mt4/administrator/img/configure_server_recycle.png "Configuring file deletion without moving them to the recycle bin")

## Server Configurator [#](installation_preparations#configurator)

The "Server Configurator" program is specially designed to facilitate the preliminary server configuration process, by automating manual operations concerning the termination of various services, system configuration via the registry, and deletion of temporary and unnecessary information from the disks. This program can be downloaded at [https://support.metaquotes.net/spfiles/srvcfg.exe](https://support.metaquotes.net/spfiles/srvcfg.exe). The program does not require installation, you just need to run the EXE file. Go through all the steps, setting all flags to on. For more details about Server Configurator please read the article "[How to use the Server Configurator](https://support.metaquotes.net/en/articles/15)".

## Configuring remote access [#](installation_preparations#remote)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Please keep the server remote access details in a safe place and do not share it with anyone without special need.</span></p></td></tr></tbody></table>

Disabling RDP access with blank password. Accounts for which blank password should not be able to remotely connect to the server. Open Control Panel— Administration — Local Policies — Security Options. Enable the option "Accounts: Limit local account use of blank passwords to console logon only".

![Disabling RDP access with blank password](/en/docs/mt4/administrator/img/rdp_settings_accounts.png "Disabling RDP access with blank password")

Changing standard port for remote connections. To protect the server from attacks targeting "well-know" port, we recommend changing the port for Desktop Protocol. Open regedit, go to HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp and find the Port Number parameter. Double click on it, select Decimal base and specify the desired port.

![Change the standard port for remote connection](/en/docs/mt4/administrator/img/rdp_settings_port.png "Change the standard port for remote connection")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The specified port must be allowed in <a href="/en/docs/mt4/administrator/administered_servers/installation_preparations#firewall" class="topiclink">Windows Firewall</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">To connect to the server remotely, specify the new port after the IP address separated by a colon. For example, 10.59.162.3:5000.</span></li></ul></td></tr></tbody></table>

Limitation of IP address list for remote connection. As an additional security measure, you can restrict the list of IP addresses that can be used to remotely connect to the server. For example, you can allow connection only from your office's IP addresses.

Open Windows Firewall and find "Remote Desktop - User Mode (TCP-In)" in the list of inbound rules. There can be several such rules depending on the number of network profiles. Open the one you need and go to Scope tab. In the "Remote IP address" section, select "These IP addresses" and add the necessary ones to the list:

![Limiting the list of IP addresses for remote connection](/en/docs/mt4/administrator/img/rdp_settings_ip.png "Limiting the list of IP addresses for remote connection")

## Configuring antivirus software [#](installation_preparations#antivirus)

If antivirus software is used on your server, add to its exclusions the MetaTrader 4 platform system process and its installation directory. Constant monitoring by antivirus software reduces platform performance.

Here is an example of adding exclusions in Windows Defender, which is a built-in antivirus software used on Windows Server 2016. Open Windows Settings — Updates and Security — Windows Defender. Go to "Exclusions" and click "Add an exclusion".

![Configuring exclusions in Windows Defender](/en/docs/mt4/administrator/img/windows_defender.png "Configuring exclusions in Windows Defender")

Select "Exclude folder" and choose the platform installation directory

![Adding an exclusion for the platform installation directory](/en/docs/mt4/administrator/img/windows_defender_folder.png "Adding an exclusion for the platform installation directory")

Click "Exclude process .exe, .com or .src". Specify the name of the trading server process in the window that opens. You can specify the name of the server executable (for example, mtsrv.exe) or the process name (for example, mtsrv).

![Add an exclusion for the platform installation process](/en/docs/mt4/administrator/img/windows_defender_process.png "Add an exclusion for the platform installation process")

[System Requirements](/en/docs/mt4/administrator/administered_servers/requirements)

[Server Administration Commands](/en/docs/mt4/administrator/server_commands)