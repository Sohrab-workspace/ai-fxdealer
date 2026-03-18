# Additional Features

> Source: https://support.metaquotes.net/en/docs/mt5/platform/additional

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)Additional Features

# Additional Features

This section describes additional features of the components of the MetaTrader 5 trading platform:

-   [URL Schemes](/en/docs/mt5/platform/additional#scheme)
-   [Marketing Campaigns](/en/docs/mt5/platform/additional#lead)

## URL Schemes [#](additional#scheme)

Mobile terminals [MetaTrader 5 for iPhone](https://download.terminal.free/cdn/mobile/mt5/ios?hl=ru&utm_campaign=download&utm_source=metatrader5.help "iPhone") and [MetaTrader 5 for Android,](https://download.terminal.free/cdn/mobile/mt5/android?hl=ru&utm_campaign=download&utm_source=metatrader5.help "Android")support the Deep Linking technology. This technology allows using links that bring users to a specified location within a mobile app.

For example, quick account connection links can be added to registration emails and to the trader's room on the website. A click on this link opens a trader's mobile terminal with the selected account connection section, in which the account number and server are automatically specified. The trader will only need to enter a password.

Launch of the application and navigation to the selected section is implemented through links starting with metatrader5://... . The part of link before "://" is called [a URL scheme](https://en.wikipedia.org/wiki/URL).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The metatrader5 URL scheme is registered in the operating system of the mobile device during terminal installation. If the terminal is not installed, the links will not open.</span></p></td></tr></tbody></table>

The general scheme of links:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader5://path?par1=val1&amp;...&amp;parN=valN</span></p></td></tr></tbody></table>

where:

-   'path' is the destination section of the application
-   par is the list of parameters

### Connection to a specified account on the server

The link should contain the application section, to which you want to link your traders, as well as the 'login' and 'server' parameters containing the account number and the name of the server to connect to. Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader5://account?login=123456&amp;server=MetaQuotes-Demo</span></p></td></tr></tbody></table>

Upon a click on such a link, the MetaTrader 5 app starts and tries to connect to the specified account. If the account already exists in the terminal and its password has been saved, connection is performed successfully. Otherwise, the account connection form is shown with the account and server already specified, and a user is prompted to enter the password. A server name should exactly match the name in the White Label.

-   If the server name is not specified, the server of the current account or of the first account from the list will be used.
-   If the account number is not specified, and the server name is specified, any account from the specified server will be selected. If there are no such accounts, the scheme will not be executed.
-   If both the account and the server are not specified, the current account or the first account from the list will be used.

### Link to a specified section

In order to forward users to the specified section, specify the appropriate 'path' value in the link:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader5://&lt;path&gt;?login=123456&amp;server=MetaQuotes-Demo</span></p></td></tr></tbody></table>

After <path>, you can specify the account number and the server name, to which the terminal should connect before opening the section. If the account or server is not specified, the connection rules described above apply.

-   account — no specific section will be opened, it is used for connection to a specified account and server.
-   marketwatch — quotes. The example contains the additional 'symbols' parameter, in which financial instruments to be displayed in the window are specified.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader5://marketwatch?server=MetaQuotes-Demo&amp;symbols=USDRUB,EURRUB,GOLD,XAUUSD,%23DIS,%23IBM</span></p></td></tr></tbody></table>

-   chart/symbol/period is a chart with the specified symbol and timeframe, e.g.:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader5://chart/XAUUSD/H1?server=MetaQuotes-Demo</span></p></td></tr></tbody></table>

-   trade — Trade tab, the list of open positions and orders, e.g.:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader5://trade?server=MetaQuotes-Demo</span></p></td></tr></tbody></table>

-   trade/symbol — a trade dialog, from which a trading operation on the specified symbol can be performed, e.g.:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader5://trade/SILVER?server=MetaQuotes-Demo&amp;login=1145990</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Illegal characters in URI links must be encoded. For example, the #GOOG must be specified as %23GOOG. Names of financial instruments are case sensitive.</span></p><p class="p_tableatten"><span class="f_tableatten">Some email services may erase links beginning with "metatrader4://" or "metatrader5://". In this case, instead of deep link, insert a link to a certain section of your website, which in turn re-directs users to the mobile application.</span></p></td></tr></tbody></table>

### Extra parameters

It is possible to specify additional parameters for each deep linked section:

-   'login' and 'server' can be used for connection with the specified account number and server name.
-   symbols — one or more symbols separated by commas, which should be added to the Quotes section after connection to an account defined by the 'login' and 'server' parameters. Illegal characters in URI links must be encoded. For example, the #GOOG must be specified as %23GOOG. Names of financial instruments are case sensitive. Symbols passed do not replace those already displayed in the "Quotes" section, they are added in the current list.

-   account\_type — run the demo or real account opening wizard on the first application start. 1 is used for demo accounts and 2 for real ones. To use this feature, you should correctly specify [account allocation settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups). If the required group for opening an account is not found, the wizard will not run.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Further information is provided in the article "<a href="https://support.metaquotes.net/en/articles/433" target="_blank" class="weblink">Deep Linking to MetaTrader mobile terminals and to their selected parts</a>"</span></p></td></tr></tbody></table>

## Marketing Campaigns [#](additional#lead)

The client record contains two special fields in the trading platform: [Lead Source](/en/docs/mt5/platform/administration/admin_accounts/account_edit#leadsource) and [Lead Campaign](/en/docs/mt5/platform/administration/admin_accounts/account_edit#leadsource). They are used for marketing campaigns allowing you to track where a client came from. To receive the data, add the following labels to the client or mobile platform download link:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">https://download.terminal.free/cdn/web/metaquotes.ltd/mt5/mt5setup.exe</span><span class="f_CodeExample" style="background-color: #dce6f2;">?utm_source=YourWebsite&amp;utm_campaign=YourCampaign</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt5/ios</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_source=YourWebsite&amp;utm_campaign=YourCampaign</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt5/android</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_source=YourWebsite&amp;utm_campaign=YourCampaign</span></p></td></tr></tbody></table>

where YourCampaign is a campaign name, while YourWebsite is a website the link has been placed at. In the 'server' parameter of the mobile platform links, enter the list of your servers to be shown to traders when they open an account.

When opening a demo account and connecting to any trading account via the terminal downloaded using such a link, utm\_source and utm\_campaign values are set in a client record at the server side. If the fields are already filled, the label values are not overwritten when re-connecting to the account (even if the terminal used for connection was downloaded by a link containing other labels).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Lead Source and Lead Campaign data from terminal download links can be written to created accounts only if the broker has a <a href="/en/docs/mt5/platform/administration/integration/integration_finteza" class="topiclink">Finteza license</a>.</span></p></td></tr></tbody></table>

[Technical Support](/en/docs/mt5/platform/support)

[Administrator](/en/docs/mt5/platform/administrator)