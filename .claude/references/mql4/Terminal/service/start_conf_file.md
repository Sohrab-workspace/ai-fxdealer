# Configuration at Startup

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/service/start_conf_file

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
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
            -   [Configuration at Startup](/en/docs/mt4/terminal/service/start_conf_file)
            -   [History Center](/en/docs/mt4/terminal/service/history_center)
            -   [Export of Quotes](/en/docs/mt4/terminal/service/dde)
            -   [Global Variables](/en/docs/mt4/terminal/service/global_variables)
            -   [Contract Specification](/en/docs/mt4/terminal/service/symbol_spec)
            -   [Languages Support](/en/docs/mt4/terminal/service/languages_support)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Tools](/en/docs/mt4/terminal/service)Configuration at Startup

# Configuration at Startup

The client terminal can be launched with some predefined settings. For this purpose, the configuration file name will be passed to the client terminal as a parameter.

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;terminal.exe&nbsp;config\start.ini</span><br><span class="f_CodeExample">&nbsp;&nbsp;terminal.exe&nbsp;test1.txt</span><br><span class="f_CodeExample">&nbsp;&nbsp;terminal.exe&nbsp;"C:\Program&nbsp;Files\Client&nbsp;Terminal\config\settings25.ini"</span></p></td></tr></tbody></table>

If the full path to the file (Drive:\\SubDirectory\\FileName) is not given, the file will be searched for in the client terminal's [data folder](/en/docs/mt4/terminal/userguide/start_comm#data_folder). The configuration file contains lines of the following appearance:

\[Parameter\] = \[Value\]

Comments start with a semicolon (;) and are not processed.

The configuration file parameters can be divided into several groups: common settings, proxy server settings ([the "Server" tab in the terminal settings](/en/docs/mt4/terminal/setup/setup_server)), FTP settings ([the "Publisher" tab in the server settings](/en/docs/mt4/terminal/setup/setup_publisher)), EA settings ([the "Expert Advisors" tab in the server settings](/en/docs/mt4/terminal/setup/setup_experts)), the expert or script single-launch settings, settings of the Strategy Tester launch.

## Common Settings

-   Profile — the subdirectory name in the /profiles directory. The charts will be opened in the client terminal according to the given profile. If this parameter is not specified, the current profile will be opened.
-   MarketWatch — file name (the \\symbolsets directory) that contains the symbol list to be shown in the Market Watch window. A file like this can be obtained using the window context menu command of the ["Market Watch - Sets - Save As..."](/en/docs/mt4/terminal/overview/market_watch).
-   Login — the number of the account to connect to at startup. If this parameter is not specified, the current login will be used.
-   Password — the password that allows entering the system. This parameter will be ignored if the client terminal stores personal data on the disk and the account to be connected is in the list.
-   Server — the name of the trade server to be connected to. The server name is the same as the name of the corresponding .srv file stored in the /config directory. This parameter will be ignored if the information about the account to be connected was stored on the disk.
-   AutoConfiguration — "true" or "false" depending on whether the autoconfiguration of Data Center setting should be enabled or not. If this parameter is not specified, the value from the current server settings will be used.
-   DataServer — address of the data center. This record can be ignored if the server autoconfiguration s enabled. If this parameter is not specified, the value from the current server settings will be used.
-   EnableDDE — "true" or "false" depending on whether DDE server should be enabled or not. If this parameter is not specified, the value from the current server settings will be used.
-   EnableNews — "true" or "false" depending on whether receiving of news should be allowed or not. If this parameter is not specified, the value from the current server settings will be used.

-   MQL5Login — [MQL5.community](https://www.mql5.com/ "MQL5.community") account.
-   MQL5Password — password to connect to the specified [MQL5.community](https://www.mql5.com/ "MQL5.community") account.

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;;&nbsp;common&nbsp;settings</span><br><span class="f_CodeExample">&nbsp;&nbsp;Profile=test&nbsp;3</span><br><span class="f_CodeExample">&nbsp;&nbsp;MarketWatch=set2.set</span><br><span class="f_CodeExample">&nbsp;&nbsp;Login=12345</span><br><span class="f_CodeExample">&nbsp;&nbsp;Password=xxxxxx</span><br><span class="f_CodeExample">&nbsp;&nbsp;Server=MetaQuotes-demo</span><br><span class="f_CodeExample">&nbsp;&nbsp;AutoConfiguration=false</span><br><span class="f_CodeExample">&nbsp;&nbsp;DataServer=192.168.0.1:443</span><br><span class="f_CodeExample">&nbsp;&nbsp;EnableDDE=true</span><br><span class="f_CodeExample">&nbsp;&nbsp;EnableNews=false</span></p></td></tr></tbody></table>

## Proxy Server Settings

-   ProxyEnable — "true" or "false" depending on whether or not a proxy server should be used for connection to the trade server.
-   ProxyServer — proxy server address.
-   ProxyType — proxy server type.It can be "HTTP", "SOCKS4", or "SOCKS5".
-   ProxyLogin — login to be authorized on proxy server.
-   ProxyPassword — password to access to proxy server.

If any of the above parameters are not specified, the current settings of the client terminal are used (proxy settings in the ["Server" tab of the client terminal settings](/en/docs/mt4/terminal/setup/setup_server)).

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample">;</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">proxy</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">settings</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample">ProxyEnable=</span><span class="f_CodeExample" style="font-weight: bold;">true</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample">ProxyServer=proxy.company.com:</span><span class="f_CodeExample">3128</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample">ProxyType=HTTP</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample">ProxyLogin=user45</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample">ProxyPassword=xxx</span></p></td></tr></tbody></table>

## FTP Settings

-   FTPEnable — enable/disable publishing. The possible values are "true" or "false".
-   FTPPassiveMode — enable/disable the passive mode of data transfer. The possible values are "true" or "false".
-   FTPAccount — the number of the account the state of which to be sent to the FTP.
-   FTPServer — FTP server address.
-   FTPLogin — the login for authorization on the FTP server.
-   FTPPassword — the password to access to the FTP server.
-   FTPPath — the name of the FTP server directory in which the report is placed.
-   FTPPeriod — the periodicity, in minutes, of the reporting to the FTP server.

If any of the above-listed parameters are not specified, the current client terminal settings are used ([the "Publisher" tab in the server settings](/en/docs/mt4/terminal/setup/setup_publisher)).

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;;&nbsp;ftp&nbsp;settings</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPEnable=true</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPPassiveMode=false</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPAccount=12345</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPServer=ftp.company.com</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPLogin=admin</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPPassword=pAssWOrd123</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPPath=/inetpub</span><br><span class="f_CodeExample">&nbsp;&nbsp;FTPPeriod=10</span></p></td></tr></tbody></table>

## EA Settings

-   ExpertsEnable — enable/disable experts.
-   ExpertsDllImport — enable/disable DLL imports.
-   ExpertsExpImport — enable/disable import of functions from external experts or MQL4 libraries.
-   ExpertsTrades — enable/disable the experts trading.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: All parameters of an experts group can take values of either "true" or "false".</span></p></td></tr></tbody></table>

If any of the above-listed parameters is not specified, the current client terminal settings will be used ([the "Expert Advisors" in the server settings](/en/docs/mt4/terminal/setup/setup_experts)).

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;;&nbsp;experts&nbsp;settings</span><br><span class="f_CodeExample">&nbsp;&nbsp;ExpertsEnable=true</span><br><span class="f_CodeExample">&nbsp;&nbsp;ExpertsDllImport=true</span><br><span class="f_CodeExample">&nbsp;&nbsp;ExpertsExpImport=true</span><br><span class="f_CodeExample">&nbsp;&nbsp;ExpertsTrades=true</span></p></td></tr></tbody></table>

## The Expert and/or Script Single-Launch Settings

-   Symbol — the symbol of the security the chart of which should be opened immediately after the terminal startup. After the client terminal has been closed, the information about this extra chart is not saved. At the terminal restart, without the configuration file, this chart will not be opened. If this parameter is not specified, no extra chart will be opened.
-   Period — the chart timeframe (M1, M5, M15, M30, H1, H4, D1, W1, MN). If this parameter is not specified, H1 is used.
-   Template — the name of the template file (the \\templates directory), which should be applied to the chart.
-   Expert — the name of the expert that should be launched after the client terminal has started. The expert is launched in the chart, which has been opened according to the data specified in Symbol and Period. If the Symbol parameter has not been not specified, no extra chart opens, and the expert will be launched in the first chart of the current profile. If there are no charts in the current profile, the expert will not be launched. If this parameter has not been specified, no expert is launched.
-   ExpertParameters — the name of the file containing the expert parameters (the \\MQL4\\Presets directory). This file can be created [in the expert properties window](/en/docs/mt4/terminal/autotrading/experts/experts_launch) by pressing of the "Inputs - Save" button. It is normally used to save the inputs other than the default ones. If this parameter has not been specified, the default inputs are used.
-   Script — the name of the script, which must be launched after the client terminal startup. The script is launched according to the same rules that are eligible for the expert (described above).
-   ScriptParameters — the name of the file containing the script parameters (the \\MQL5\\Presets directory). This file is made in the same way as that for the expert.

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;;&nbsp;open&nbsp;chart&nbsp;and&nbsp;run&nbsp;expert&nbsp;and/or&nbsp;script</span><br><span class="f_CodeExample">&nbsp;&nbsp;Symbol=EURUSD</span><br><span class="f_CodeExample">&nbsp;&nbsp;Period=H4</span><br><span class="f_CodeExample">&nbsp;&nbsp;Template=popular.tpl</span><br><span class="f_CodeExample">&nbsp;&nbsp;Expert=MACD&nbsp;Sample</span><br><span class="f_CodeExample">&nbsp;&nbsp;ExpertParameters=macd.set</span><br><span class="f_CodeExample">&nbsp;&nbsp;Script=period_converter</span><br><span class="f_CodeExample">&nbsp;&nbsp;ScriptParameters==per_conv.set</span></p></td></tr></tbody></table>

## Settings of the Strategy Tester Launch

-   TestExpert — the name of the expert to be launched for testing. If this parameter has not been specified, no testing is launched.
-   TestExpertParameters — the name of the file containing parameters (the \\tester directory). The file can be created [in the Properties window of the expert under test](/en/docs/mt4/terminal/autotrading/tester/tester_parameters) by clicking the "Inputs - Save" button. It is normally used to save parameters other than the default ones. Other parameters of the expert under test [in the "Testing" and "Optimization" tabs (as well as in the "Inputs" tab if this parameter has not been specified)](/en/docs/mt4/terminal/autotrading/tester/tester_parameters) are filled up with the values automatically saved in the \\tester\\\[the expert name\].ini file after the latest test.
-   TestSymbol — the name of the symbol used for the expert testing. If this parameter has not been specified, the latest value used in the tester is used.
-   TestPeriod — the chart period (M1, M5, M15, M30, H1, H4, D1, W1, MN). If this parameter has not been specified, H1 is used.
-   TestModel — 0, 1, or 2, depending on the testing model (Every tick, Control points, Open prices only). If this parameter has not been specified, 0 is used (Every tick).

-   TestSpread — spread value that will be used for modeling Ask prices during testing. If 0 value is specified, the strategy tester will use the current spread of a symbol at the beginning of testing.

-   TestOptimization — enable/disable optimization. The values that can be taken are "true" or "false". If this parameter had not been specified, the "false" value is used.
-   TestDateEnable — enable/disable the "Use date" flag. The values that can be taken are "true" or "false". If this parameter had not been specified, the "false" value is used.
-   TestFromDate — the date, from which to start testing, appeared as YYYY.MM.DD. If this parameter has not been specified, this date is 1970.01.01.
-   TestToDate — the date, on which to finish testing, appeared as YYYY.MM.DD. If this parameter has not been specified, this date is 1970.01.01.
-   TestReport — the name of the test report file. The file will be created in the client terminal directory. A relative path can be specified, for example: tester\\MovingAverageReport". If the extension has not been specified in the file name, the ".htm" will be set automatically. If this parameter has not been specified, the test report will not be formed.
-   TestReplaceReport — enable/disable the repeated report file record. The values that can be taken are "true" or "false". If the "false" value is specified and a report file named in the same way exists already, the number in square brackets will be added to the file name. For example, "MovingAverageReport\[1\].htm". If this parameter had not been specified, the "false" value is used.
-   TestShutdownTerminal — enable/disable shutdown of the terminal after the testing has been finished. The values that can be taken are "true" or "false". If this parameter had not been specified, the "false" value is used. If the user has pressed the "Stop" button, the value of this parameter will be flushed to "false" since the control has been given to the user.

-   TestVisualEnable — enable (true) or disable  (false) the visual test mode. If the parameter is not specified, the current setting is used.

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;&nbsp;;&nbsp;start&nbsp;strategy&nbsp;tester</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestExpert=Moving&nbsp;Average</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestExpertParameters=ma0.set</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestSymbol=EURUSD</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestPeriod=H1</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestModel=2</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestSpread=0</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestOptimization=false</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestDateEnable=true</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestFromDate=1970.01.01</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestToDate=2006.06.06</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestReport=MovingAverageReport</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestReplaceReport=false</span><br><span class="f_CodeExample">&nbsp;&nbsp;TestShutdownTerminal=true</span></p></td></tr></tbody></table>

[Tools](/en/docs/mt4/terminal/service)

[History Center](/en/docs/mt4/terminal/service/history_center)