# FTP

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/setup_publisher

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
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
            -   [Server](/en/docs/mt4/terminal/setup/setup_server)
            -   [Charts](/en/docs/mt4/terminal/setup/setup_charts)
            -   [Objects](/en/docs/mt4/terminal/setup/setup_objects)
            -   [Trade](/en/docs/mt4/terminal/setup/setup_trade)
            -   [Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts)
            -   [Notifications](/en/docs/mt4/terminal/setup/settings_notifications)
            -   [Email](/en/docs/mt4/terminal/setup/setup_email)
            -   [FTP](/en/docs/mt4/terminal/setup/setup_publisher)
            -   [Events](/en/docs/mt4/terminal/setup/setup_events)
            -   [Community](/en/docs/mt4/terminal/setup/settings_mql5community)
            -   [Signals](/en/docs/mt4/terminal/setup/settings_signals)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)FTP

# FTP

Terminal allows to publish reports about the account status in internet automatically. To do so, one has to set up internet connection parameters through FTP (File Transfer Protocol). This can be done in the "FTP" tab:

![FTP](/en/docs/mt4/terminal/img/options_ftp.png "FTP")

The following parameters are available on this tab:

-   FTP server — FTP server address the report to be sent to. Example: ftp.your\_domain\_name.com;
-   FTP path — name of the FTP server directory where the report will be placed. The path (starting with the root directory) for sending reports must be given in this field. Example: /report\_shots;
-   FTP login — login for authorization at the FTP server;
-   FTP password — password for access to the FTP server;
-   Passive mode — switch between active and passive mode of data transfer.  
    In active mode, a free port (from dynamic range of 1024 to 65535) is allotted in the client terminal to which the server will connect in order to set connection for transferring of data. The FTP server connects to the client's port with the given number using TCP port 20 from its part to transfer data. In passive mode, the server informs the client about the TCP port number (from the dynamic range of 1024 to 65535) to which the client can connect to set up data transfer.  
       
    The main difference between active and passive FTP mode is the part that opens connection for data transferring. In active mode, it is the client who has to accept connection from the FTP server. In passive mode, the client initiates connection, and the server accepts it.
-   Enable automatic publishing of reports via FTP — enable support reports publishing. If disabled, other fields are inaccessible;

-   Account — the account number the report for which should be published;
-   Refresh every — periodicity of sending reports to the web server (in minutes).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Reports of only active accounts can be published. If the account number given in this field does not match with the current one, the reports will not be published.</span></p></td></tr></tbody></table>

The "Test" button sends report about the current account status using the specified settings that allows to check their workability. If it has been tested successfully, the "OK" button must be pressed to activate these settings. If the test did not succeed, it is recommended to check all settings again and retest.

The client terminal publishes common reports on default. In order to publish a detailed report, you should rename the "StatementDetailed.htm" file located in the /TEMPLATES directory into "Statement.htm".

[Email](/en/docs/mt4/terminal/setup/setup_email)

[Events](/en/docs/mt4/terminal/setup/setup_events)