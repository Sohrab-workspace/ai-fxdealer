# History Center

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/service/history_center

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Tools](/en/docs/mt4/terminal/service)History Center

# History Center

Technical analysis is the market movements research made in order to forecast future price movements. the market is often analyzed using charts. So it is very important to have available historical data for all symbols and timeframes used. Historical data are constantly formed and stored on the server. Connecting to it, the client terminal downloads all necessary data. They will be then used for drawing of charts,[testing](/en/docs/mt4/terminal/autotrading/tester) and [optimization of Expert Advisors](/en/docs/mt4/terminal/autotrading/tester_optimization). To control historical data, the terminal has a special window named "History Center". This window can be opened by executing the command ["Tools — History Center"](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) or by pressing F2.

After the terminal has been shut down, all accumulated historical data will be stored in the "History Center". Sizes of files containing historical quotes do not exceed values defined in [settings](/en/docs/mt4/terminal/setup/setup_charts). If the amount of historical data accumulated exceeds the value set in the field of " Max. bars in history:", the oldest bars will be deleted when storing. For each timeframe, a separate history file is formed named as SSSSSSPP.hst (where SSSSSS - symbol name, PP - timeframe in minutes) and saved in the /HISTORY. Later on, the saved data will be used to draw charts, as well as for [testing trading strategies](/en/docs/mt4/terminal/autotrading/tester).

In the "History Center" window, the available data can be changed. For this, it is necessary to select the desired symbol and timeframe in the left part of the window.The corresponding data will be loaded in form of a table. To add a record about a new bar, it is necessary to press the button of the same name, fill out all necessary fields in the new window and press "OK". After that, the new bar will appear in the history. One can modify the bar by selecting the corresponding record and pressing the "Modify" button. To delete a bar, it is necessary to select it and press the button of the same name.

## Load of Historical Data

It is possible to load quotes for basic currency pairs starting with year 1999 from the historical data server. To do it, it is necessary to select the desired symbol and press "Download".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The loaded data can differ from historical data stored on the broker's trade server.</span></p></td></tr></tbody></table>

Upon pressing the button, data of M1 timeframe will be loaded. Other timeframes will be automatically recalculated from М1. At that, the time of the downloaded data will be automatically recalculated according to the active account time zone.

When downloading historical data, it is recommended to control [amount of bars in history and in charts](/en/docs/mt4/terminal/setup/setup_charts#bars_count).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The deeper is the history used, the more PC resources are needed.</span></p></td></tr></tbody></table>

Quotes are weekly updated on the server of historical data. Further, at restarts, only updated quotes will be downloaded.

## Exports and Imports of Historical Data

Historical data can be exported into files formatted as CSV, PRN and HTM. For this, it is necessary to select the desired symbol in the left part of the "History Center" window and press "Export". Then it is necessary to select on of three file formats and specify the path of location on the hard disk.

Historical data as CSV, PRN, TXT, HTM and HST can also be imported into terminal.

Historical data in the file can be represented as follows (any other separator can be used instead of space):

-   YYYY.MM.DD HH:MM O H L C V
-   YYYY-MM-DD HH:MM O H L C V
-   YYYY/MM/DD HH:MM O H L C V
-   DD.MM.YYYY HH:MM O H L C V
-   DD-MM-YYYY HH:MM O H L C V
-   DD/MM/YYYY HH:MM O H L C V

First of all, it is necessary to select a symbol and a timeframe, for which the import will be performed, in the left part of the "History Center" window. Then it is necessary to set up import parameters by pressing "Import":

-   Separator — data separator in the file to be imported. Comma, semicolon, space or tabulation character can be used as separators;
-   Skip columns — skip columns when importing. This can be helpful when the imported file contains more data types than necessary;
-   Skip lines — skip rows (lines) when importing;
-   Time shift — shift data by several hours in time;
-   Selected only — import only selected data. Data are selected by lines using "Ctrl" and "Shift";
-   Volumes — enable/disable importing of volumes.

After historical data have been imported, they can be used to show charts and [test Expert Advisors](/en/docs/mt4/terminal/autotrading/tester).

[Configuration at Startup](/en/docs/mt4/terminal/service/start_conf_file)

[Export of Quotes](/en/docs/mt4/terminal/service/dde)