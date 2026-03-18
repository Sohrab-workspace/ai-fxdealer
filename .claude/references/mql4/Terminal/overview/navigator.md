# Navigator

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/navigator

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
            -   [Main Menu](/en/docs/mt4/terminal/overview/main_menu)
            -   [Toolbars](/en/docs/mt4/terminal/overview/toolbars)
            -   [Market Watch](/en/docs/mt4/terminal/overview/market_watch)
            -   [Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)
            -   [Data Window](/en/docs/mt4/terminal/overview/data_window)
            -   [Navigator](/en/docs/mt4/terminal/overview/navigator)
            -   [Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)
            -   [Client terminal](/en/docs/mt4/terminal/overview/terminal)
            -   [Tester](/en/docs/mt4/terminal/overview/strategy_tester)
            -   [Search](/en/docs/mt4/terminal/overview/search)
            -   [Fast Navigation](/en/docs/mt4/terminal/overview/fast_nav)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)Navigator

# Navigator

This window allows to get a quick access to various features of the terminal. This window can be opened/closed by pressing accelerating keys of Ctrl+N, by the ["View — Navigator" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_view) command, or by pressing of the !["Navigator" Window](/en/docs/mt4/terminal/img/tb_standard_navigator.png ""Navigator" Window") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).

![navigator](/en/docs/mt4/terminal/img/navigator.png)

The list of features is listed as a tree and contains five groups: "Accounts", "Indicators", "Expert Advisors", "Custom Indicators", and "Scripts".

## Accounts

The "Accounts" group includes the list of open accounts. Using a context menu, one can open a new demo account or delete the old one.

![navigator_accounts_menu](/en/docs/mt4/terminal/img/navigator_accounts_menu.png)

-   Open an Account — An unlimited amount of demo accounts can be opened from the terminal. To do so, one has to execute the "Open an Account" context menu command or press the Insert button. More details about opening of accounts can be found in the [corresponding section](/en/docs/mt4/terminal/userguide/open_an_account).
-   Login to Trade Account — to authorize an existing account (whether a demo or a real one), one has to execute the "Login to Trade Account" command or double-click with the left mouse button on the desired account line.

-   Login to Web Terminal — the web terminal allows trading on financial markets and conducting technical analysis just using a web browser. The web platform is safe to use - any transmitted information is securely encrypted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">At the moment, the web terminal use under testing and not all of its planned features are available. The web terminal may be unavailable if the broker doesn't update the trade server to the latest version and doesn't enable web trading.</span></li><li class="p_tableatten"><span class="f_tableatten">The web trading is available at MQL5.community in the <a href="https://www.mql5.com/en/trading" target="_blank" class="weblink" title="Web trading at MQL5.community">"Trading"</a> section.</span></li></ul></td></tr></tbody></table>

-   Login to MQL5.community — open the [settings](/en/docs/mt4/terminal/setup/settings_mql5community) of the trading platform to login to [MQL5.community](https://www.mql5.com/ "MQL5.community") and get additional services.
-   Change Password — open the window of [changing the password of the trade account](/en/docs/mt4/terminal/setup/setup_server#passwords).

-   Delete — delete a selected account. The same action can be performed by pressing the Delete key.
-   Add to Favorites — add the selected account to [favorites](/en/docs/mt4/terminal/overview/navigator#favorites).

-   Register as Signal — register a selected account in the ["Signals"](https://www.mql5.com/en/signals "Trade Signals") service. After executing this command, you'll go to the [signal registration page](/en/docs/mt4/terminal/signals/signal_provider#add) at MQL5.community. The selected account and the right broker server will be automatically specified in the registration form.

-   Register a virtual server — this command allows you to [allocate a virtual server](/en/docs/mt4/terminal/virtual_hosting) for the terminal's continuous round-the-clock operation. Unlike renting ordinary VDS or VPS from third-party companies, you are able to select the server that is the closest to your broker minimizing the network latency when sending orders from the terminal to the trade server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Real accounts cannot be started from the terminal, they are opened only by a brokerage company.</span></p></td></tr></tbody></table>

## Indicators [#](navigator#indicators)

This group contains indicators — the main tools for analyzing the price dynamics:

-   Built-in [technical indicators](/en/docs/mt4/terminal/analytics/tech_indicators) divided into four categories: Trend, Oscillators, Volumes, Bill Williams.
-   Indicators downloaded from the [source code library at MQL5.community](/en/docs/mt4/terminal/overview/terminal/toolbox_codebase). Displayed in Downloads sub-category.
-   Indicators purchased from the [Market](/en/docs/mt4/terminal/overview/terminal/toolbox_market) — the store of applications for the trading platform. Displayed in Market sub-category.
-   Built-in examples of indicators with the source codes. Displayed in Exmaples sub-category.
-   [Custom indicators](/en/docs/mt4/terminal/autotrading/custom_indicators) located in /MQL4/Indicators folder; displayed according to the structure of sub-folders they are stored in.

The Navigator shows only executable indicator files (\*.EX4).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the diamond in the lower right corner of a program icon is gray (for example, <img class="help" alt="No source code/Couldn't be compiled" title="No source code/Couldn't be compiled" width="15" height="15" src="/en/docs/mt4/terminal/img/no_code_icon.png">), it means </span><span class="f_txt">that the program doesn't have source code files or it couldn't be compiled.</span></p></td></tr></tbody></table>

![navigator_cust_indicators_menu](/en/docs/mt4/terminal/img/navigator_cust_indicators_menu.png)

The following commands can be executed in the context menu:

-   Attach to Chart — apply a selected indicator to the active chart. The same action can be performed by a double click on the indicator. Besides, using the Drag'n'Drop method one can apply an analytical tool to any chart or a subwindow of already attached indicator.
-   Modify — open the source code file (\*.MQ4) of a selected indicator in [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor). The same action can be performed by selecting an indicator and pressing the Enter key.
-   Delete — delete a selected custom indicator. This action deletes both its executable file (\*.EX4) and its source code file (\*.MQ4). The same action can be performed by clicking the Delete key.

-   Buy from the Market — go to the [Market](/en/docs/mt4/terminal/overview/terminal/toolbox_market) — the store of applications for the trading platform.

-   Order your own Program — go to ordering a development of an MQL4 program at the ["Freelance" service at MQL5.community](https://www.mql5.com/en/job "Development of any MQL5 programs at the \"Freelance\" service at MQL5.community").
-   Create in MetaEditor — go to the creation of a custom indicator. The execution of this command opens MQL4 Wizard in [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor) where an indicator can be created. The same action can be performed by clicking the Insert key.
-   Add to Favorites — add a selected indicator to [favorites](/en/docs/mt4/terminal/overview/navigator#favorites).
-   Set hotkey — assign a [hotkey](/en/docs/mt4/terminal/overview/navigator#favorites) to the selected indicator.
-   Refresh — re-read the information about existing compiled indicators from the hard disk. The execution of this command is necessary when copying already compiled files to the corresponding folder of the client terminal.
-   Online library — go to "Code Base" section, where you can easily download programs published in the corresponding section of the [MQL5.community](https://www.mql5.com/en/code "MQL5.community, Code Base") website.

## Expert Advisor [#](navigator#experts)

The "Expert Advisors" group contains the list of all available [expert advisors](/en/docs/mt4/terminal/autotrading/experts). Expert Advisors in the terminal are programs allowing to automate analytical and trading activities. To create and modify them, the built-in editor, [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor), is used. More details about creation and working with experts can be found in the ["Auto Trading" section](/en/docs/mt4/terminal/autotrading).

The "Create" context menu command allows to create a new expert, "Modify" — to modify an existing one, and "Delete" — to delete an expert from the terminal. The "Attach to a Chart" command or double-click with the left mouse button allow to impose the expert into the active chart. After that, when a new tick incomes, the expert will start working. Experts can be imposed into any chart with the "Drag'n'Drop" technique.

## Hot Keys [#](navigator#hotkeys)

Hot keys can be assigned to call any elements of the "Navigator" window, except for those in the "Accounts" group.

![navigator_hot_keys](/en/docs/mt4/terminal/img/navigator_hot_keys.png)

To set a hot key for an element, one has to execute the "Set hotkey" command of this element's context menu. The hot keys set have a higher priority being compared to those predefined. For example, Ctrl+O is predefined to call the [terminal setting window](/en/docs/mt4/terminal/setup). If this pair of keys is set to call the [On Balance Volume](/en/docs/mt4/terminal/analytics/tech_indicators/on_balance_volume) indicator, the terminal setting window will not be called by pressing of Ctrl+O anymore.

## Favorites Tab [#](navigator#favorites)

The "Favorites" tab is intended for a quick access to objects mostly used.

![navigator_favourites](/en/docs/mt4/terminal/img/navigator_favourites.png)

In this tab, for example, only necessary accounts, [indicators](/en/docs/mt4/terminal/analytics/tech_indicators), [scripts](/en/docs/mt4/terminal/autotrading/scripts), and [experts](/en/docs/mt4/terminal/autotrading/experts) can be placed. This allows to accelerate the trader's work, especially, if there is a need to act promptly. To move a necessary object into the "Favorites" tab, one has to execute the corresponding context menu command. If the object is not necessary anymore, it can be deleted from the tab using the "Delete from favorites" context menu command.

Attention: All objects included in the "Favorites" can function without any limitations. All managing commands placed in the context menu can also be called directly from this tab.

[Data Window](/en/docs/mt4/terminal/overview/data_window)

[Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)