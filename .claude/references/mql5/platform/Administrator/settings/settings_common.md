# Common

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/settings/settings_common

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
        -   [Terminal Settings](/en/docs/mt5/platform/administrator/settings)
            -   [Common](/en/docs/mt5/platform/administrator/settings/settings_common)
            -   [Support](/en/docs/mt5/platform/administrator/settings/settings_support)
            -   [Events](/en/docs/mt5/platform/administrator/settings/settings_events)
            -   [Confirmations](/en/docs/mt5/platform/administrator/settings/settings_confirmations)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Terminal Settings](/en/docs/mt5/platform/administrator/settings)Common

# Common

The "Common" tab contains the connection settings of the administrator terminal and the settings of receiving news.

![Common](/en/docs/mt5/platform/img/settings_common.png "Common")

The following options are present here:

-   Enable proxy server — enable [connection](/en/docs/mt5/platform/administrator/getting_started/server_connect) to administrated servers through a proxy server. If this option is checked, the "Proxy..." button becomes active. Using it one can set up connection to administered servers through a [proxy server](/en/docs/mt5/platform/administrator/settings/settings_common#proxy).
-   Enable news — this option allows to enable or disable [news](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news). If it is disabled, news won't come to the terminal;
-   Languages — this option allows to filter news by their language. The window of choosing the [news language](/en/docs/mt5/platform/administrator/settings/settings_common#news_language) will appear as soon as the "Change" button is pressed. If the "Any language" parameter is indicated in this field then all news items will come to the terminal regardless of their language.
-   Save files to — the directory, to which files received via [internal email system](/en/docs/mt5/platform/administration/mail) will be saved. When you open an attached file, the terminal checks its extension and the corresponds of file contents to this extension. If the file type is allowed and its contents are checked, the terminal will open the file and save it to the specified directory. Otherwise, a warning will be displayed, notifying that the file may harm the computer, and the file will not be saved. The following file types are allowed: PNG, JPG/JPEG, BMP, ZIP, 7Z, GIF, DOC, XLS, DOCX, XSLX, ODT, RTF, CSV, TXT, LOG.  
    If a file with the same name and a different content exists in the directory, the manager's login and email arrival date/time up to a second will be added to the saved file name: \[login\]-\[file name\]-\[date and time\].\[extension\]. For example, the log file 20170501.log will be saved as 1001-20170501-20170502-170038.log.  
    By default, files are saved to C:\\Users\\\[Windows username\]\\Downloads\\MetaTrader. You can change the directory by clicking on "Browse".

## Setting Up Connection through Proxy Server [#](settings_common#proxy)

![Proxy Server](/en/docs/mt5/platform/img/proxy_server.png "Proxy Server")

In the "Proxy Server" window it is necessary to specify the following parameters:

-   Server — IP address and server port number separated by a colon are specified here. To the right of this field the type of proxy server is selected: HTTP, SOCKS4 or SOCKS5. In HTTP mode NTLM authorization is also supported;
-   Login — account to access the proxy server. If login is not needed, the field should be empty
-   Password — password to access the proxy server. If password is not needed, the field should be empty.

In order to verify the correctness of the settings of connection to the proxy server, press the "Test" button. In case of receiving the message that the settings are correct it is necessary to press the "OK" button to save the settings. The error message indicates that the proxy server is set up incorrectly. To find out the reason, contact the system administrator or internet provider.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The proxy server settings affect the connection to all the administered servers in the terminal.</span></p></td></tr></tbody></table>

## Selecting News Language [#](settings_common#news_language)

In order to select only necessary languages of incoming news, the "Change" button should be pressed against the corresponding field. After that the following window will be opened:

![Language Selection](/en/docs/mt5/platform/img/options_select_language.png "Language Selection")

The left part of the window contains available languages, the right part - selected ones. In order to add a language, double-click on it or select it and press "Insert". Use "Remove" for removing languages from the list of selected ones. The "Reset" button returns default values. If "Any language" is indicated in the "News language" field, all news independent of the language will be received in the terminal.

[Terminal Settings](/en/docs/mt5/platform/administrator/settings)

[Support](/en/docs/mt5/platform/administrator/settings/settings_support)