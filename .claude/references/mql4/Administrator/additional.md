# Additional Features

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/additional

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)Additional Features

# Additional Features

This section describes additional features of the components of the MetaTrader 4 trading platform:

-   [URL Schemes](/en/docs/mt4/administrator/additional#scheme)
-   [Marketing Campaigns](/en/docs/mt4/administrator/additional#lead)

## URL Schemes [#](additional#scheme)

Mobile terminals [MetaTrader 4 for iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=ru&utm_campaign=download&utm_source=metatrader4.help "iPhone") and [MetaTrader 4 for Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=ru&utm_campaign=download&utm_source=metatrader4.help "Android") support a special URL scheme for launching the application with predefined settings on a device. Currently, the terminal can be launched with a certain account. Create a link of the following look on your website:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">metatrader4://account/?login=</span><span class="f_CodeExample" style="font-weight: bold; background-color: #dce6f2;">&lt;account_login&gt;</span><span class="f_CodeExample">&amp;server=</span><span class="f_CodeExample" style="font-weight: bold; background-color: #dce6f2;">&lt;account_server&gt;</span></p></td></tr></tbody></table>

where <account\_login> and <account\_server> are trading account login and server. When such a link is clicked from a mobile device browser, MetaTrader 4 starts and tries to connect to the specified account. If the account is already present in the terminal and has a predefined password, connection is performed successfully. Otherwise, the account connection form is shown with the account and server already specified, and a user is prompted to enter the password.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A server name should exactly match the name in the White Label.</span></p></td></tr></tbody></table>

## Marketing Campaigns [#](additional#lead)

A user record in the trading platform has a special field [LeadSource](/en/docs/mt4/administrator/administration/ug_accounts#leadsource). It is used for marketing campaigns allowing you to track where a client came from.  To receive the data, add the following to the client or mobile platform download link:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">https://download.terminal.free/cdn/web/metaquotes.software.corp/mt4/mt4setup.exe</span><span class="f_CodeExample" style="background-color: #dce6f2;">?utm_campaign=YourLeadSource</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt4/ios</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_campaign=YourLeadSource</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt4/android</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_campaign=YourLeadSource</span></p></td></tr></tbody></table>

Where YourLeadSource is a name of a campaign. In the "server" parameter of the mobile platform links, enter the list of your servers to be shown to traders when they open an account.

When opening a demo account and connecting to any trading account via the terminal downloaded using such a link, utm\_campaign value is set in a client record at the server side. Additional information is available in the article [New Analytics in MetaTrader 4/5: from Website and Installer to Opening an Account. What are the Advantages for Brokers?](https://support.metaquotes.net/en/articles/415)

[API](/en/docs/mt4/administrator/articles/ug_articles_api)

[Manager](/en/docs/mt4/manager)