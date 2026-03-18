# Live Update

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_live_update

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Live Update

# Live Update

MetaTrader LiveUpdate is a computer-based system providing secure and effective distribution of program updates of the whole information trading complex MetaTrader. The important features are: full automation of updating processes and minimum attention from trading server administrators. Security is provided with secure data transfer through shrinking algorithms, coding, and obligatory digital signature for each file. More datails about the LiveUpdate can be found in the article ["MetaTrader LiveUpdate Overview"](https://support.metaquotes.net/en/articles/3 "Article \"MetaTrader LiveUpdate Overview\"").

If automatic updates are enabled, the server checks and installs updates on Sundays 5 minutes after the Optimization time set in the [common settings](/en/docs/mt4/administrator/administration/ug_options#optimization) of the server. For critical updates one may need to start the updates manually. To do it, click "Tools — Start LiveUpdate"; make sure to set up [live update parameters](/en/docs/mt4/administrator/administration/ug_live_update) before doing it.

Updates are applicable to the following components of MetaTrader: MetaTrader Server (and all assisting modules), MetaTrader Data Center, MetaTrader Administrator, MetaTrader Manager and client terminals MetaTrader (including palm versions). To be sure that all components of the system are always updated, the adminstrator of the trading server has just to enable automatic downloading of updates. Unfortunately, updates cannot be downloaded in free mode and is only accessible for trading servers (according to the IP address lists) of our clients.

![Live Update](/en/docs/mt4/administrator/img/br_live_update.png "Live Update")

The LiveUpdate contains the following information:

-   Company — full and exact name of the company owning the specific program ("any" - for any owner);

-   Type — select type of the program (MetaTrader, Administrator, Manager, Data Center, MultiTerminal, Watch Dog). Set "any" for Administrator and Manager terminals, as well as for Data Centers;

-   Version — the number of the program version and build separated with a decimal point;

-   Path — the path to the folder containing a new version of the program.

When starting, all the programs of the complex (MetaTrader, Administrator, Manager, DataCenter, Client Terminal) call to the server and request the number of the latest program version, and, having found a new version, run Live Update module. When updating files, the digital signature of MetaQuotes Software Corp. is checked and the check sum of files are calculated, as well as automatic pumping in the case of disconnection. All this provides the precise updating file transferring.

[Backup](/en/docs/mt4/administrator/administration/ug_backup)

[Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)