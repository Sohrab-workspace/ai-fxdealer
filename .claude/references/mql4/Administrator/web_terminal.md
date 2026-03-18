# MetaTrader 4 WebTerminal

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/web_terminal

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

[MetaTrader 4](/en/docs/mt4)WebTerminal

# MetaTrader 4 WebTerminal

MetaTrader 4 WebTerminal allows trading in the financial markets via a web browser. It works in all operating systems and browsers requiring no additional software. All transmitted data is securely encrypted.

The WebTerminal allows setting all types of market and pending orders, as well as supports one-click trading. Traders can view real-time quotes and analyze charts using basic graphical objects. The terminal also allows analyzing charts via 30 technical indicators.

The terminal is a modern HTML5 application that can be easily integrated into any website via a simple iframe widget.

Similar to the desktop platform, traders should select a server from the list, enter login and password when connecting to the web terminal via your website. For the seamless web terminal integration with clients area on your website, server and login can be pre-selected to let your client enter a password only. If a users saves a password in a browser storage, the platform will login to the trading account automatically on the next run.

![MetaTrader 4 WebTerminal](/en/docs/mt4/administrator/img/web-terminal.png "MetaTrader 4 WebTerminal")

To get the terminal, [order it in the App Store section](https://support.metaquotes.net/en/market/product/295 "Order MetaTrader 4 WebTerminal") of the Support website.

[Order WebTerminal](https://support.metaquotes.net/en/market/product/295 "Order WebTerminal")  [Configure WebTerminal](https://support.metaquotes.net/en/market/whitelabel/mt4# "Configure WebTerminal")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The server should be updated to build 890 for the web terminal operation.</span></li><li class="p_tableatten"><span class="f_tableatten"><a href="https://mql5.com" target="_blank" class="weblink" title="MQL5.community">MQL5.community</a> account is not required.</span></li></ul></td></tr></tbody></table>

## How to Add the WebTerminal Widget to Your Website

To install the WebTerminal widget on your site, visit the "[App Store \\ White Labels \\ MetaTrader 4](https://support.metaquotes.net/en/market/whitelabel/mt4#) " section of the technical support site. Then click "Show widget code \\ Customize":

![Customize the WebTerminal widget](/en/docs/mt4/administrator/img/webterminal_customize.png "Customize the WebTerminal widget")

Set the WebTerminal operation parameters. After that, a special code will be generated for you, which should be inserted into your website.

The following parameters are supported (the corresponding parameters in the widget code are displayed in brackets, you can change them manually if necessary).

-   Version (version) — default web terminal version: MetaTrader 4 or MetaTrader 5. The parameter is important only if you use both versions of the platform at the same time — if the widget settings have no restrictions on used servers or the servers of both versions are present in the server list (servers). The parameter is used only for the first launch of the web terminal. Further on, the platform version will be defined based on the last used account. The detailed description is given in the section [If you have two platforms: MetaTrader 5 and MetaTrader 4](/en/docs/mt4/administrator/web_terminal#version).
-   Restrict trade servers \\ Trade server list (servers) — limit servers available for use in your web terminal. All servers of all brokers are available by default. Simply enter a name in the new account opening or in the existing account login dialog.  
    If you enable the "Restrict trade servers" option and set the list of available servers, the list of certain servers instead of the server name input box will be available in the appropriate dialogs.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Server names are case sensitive. Be sure to specify the exact name.</span></p></td></tr></tbody></table>

-   Default login (login) — default trading account selected in the login dialog. Use this option to create convenient client areas by immediately substituting the necessary account into the web terminal.
-   Default trade server (server) — default server selected in the connection dialog. Use this option to create convenient client areas by immediately substituting the necessary server into the web terminal.
-   Allow opening demo accounts on any servers (demoAllServers) — disable the option if you want to allow opening demo accounts via the web terminal only on demo servers from the "Trade server list" parameter. If enabled, demo accounts can be opened on any servers (regardless of the "Restrict trade servers" parameter). The server name input box is displayed instead of the list of available servers in the appropriate dialog.

-   Demo account types (demoType) — demo account type, multiple comma-separated values can be added. To open demo accounts in the "demoforex" group, specify "forex" (the "demo" prefix is added automatically). If not specified, all account types configured in the terminal White Label are used. At the moment, you can add this parameter to the terminal widget only by specifying it in the code manually.
-   Leverage (demoLeverage) — the leverage for the demo account, multiple comma separated options can be added. If not specified, all options configured in the terminal White Label are used. At the moment, you can add this parameter to the terminal widget only by specifying it in the code manually.

-   First Name and Second Name (demoName) — the first name and the second name to be automatically inserted into the demo account registration form in the web terminal. These parameters can be added to the embed code only manually. Use the parameters to display the web terminal with appropriate data to the users who are authorized on the site and whose first and second name are known.

-   Email (demoEmail) — the email address to be automatically inserted into the demo account registration form in the web terminal. Thia parameter can only be added to the embed code manually. Use the parameter to display the web terminal with appropriate data to the users who are authorized on the site and whose emails are known in advance.

-   Allow the Phone field in the demo account opening dialog (demoAllowPhone) — show the Phone input box in the demo account registration form ("true" value).
-   UTM campaign \\ UTM Source (utmCampaign \\ utmSource) — UTM tags to be added to accounts opened via the web terminal. The tags allow you to analyze the efficiency of this tool. For more details, see ["How to track accounts opened via the web terminal"](/en/docs/mt4/administrator/web_terminal#track).
-   Width (width) — terminal widget width in % or pixels. The recommended value is 100% to allow the web terminal to automatically adjust to the maximum available width on the web page.
-   Height (height) — terminal widget height in % or pixels. The recommended value is "600px" to make the entire widget visible even on small screens without the need to scroll.
-   What to do at the start for new visitors (startMode) — web terminal launch mode:

-   Open the demo account creation dialog (open\_demo) — display a demo account opening window (instead of the login window) for users who do not have accounts stored in the web terminal. If accounts exist in the local storage, connection to the last used account is established.
-   Create a demo account automatically (create\_demo) — open a demo account automatically for a user when launching the web terminal. The account is opened only if the user's web terminal has no previously saved accounts.
-   Show login dialog (login) —  show account login window for users when launching the web terminal. Login to the last used account is not conducted automatically even if a user saved the account password in the browser storage previously.

-   Chart color scheme (colorScheme) — default color scheme applied to charts. Possible values: black\_on\_white, yellow\_on\_black and green\_on\_black.
-   Language (lang) — default web terminal interface language. Users can select a necessary language in the web terminal menu: View -> Languages. In this case, the value of this parameter is ignored. Currently, the following languages are supported:

-   Arabic (ar)
-   Bulgarian (bg)
-   Chinese (zh)
-   Croatian (hr)
-   Czech (cs)
-   Danish (da)
-   Dutch (nl)
-   English (en)
-   Estonian (et)
-   Finnish (fi)
-   French (fr)
-   German (de)
-   Greek (el)
-   Hebrew (he)
-   Hindi (hi)
-   Hungarian (hu)
-   Indonesian (id)
-   Italian (it)
-   Japanese (ja)
-   Korean (ko)
-   Latvian (lv)
-   Lithuanian (lt)
-   Malay (ms)
-   Mongolian (mn)
-   Persian (fa)
-   Polish (pl)
-   Portuguese (pt)
-   Romanian (ro)
-   Russian (ru)
-   Serbian (sr)
-   Slovak (sk)
-   Slovenian (sl)
-   Spanish (es)
-   Swedish (sv)
-   Tajik (tg)
-   Thai (th)
-   Traditional Chinese (zt)
-   Turkish (tr)
-   Ukrainian (uk)
-   Uzbek (uz)
-   Vietnamese (vi)

Sample web terminal code to be inserted into a website:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;id=</span><span class="f_CodeExample" style="color: #219161;">"webterminal"</span><span class="f_CodeExample">&nbsp;style=</span><span class="f_CodeExample" style="color: #219161;">"width:100%;height:600px;"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://metatraderweb.app/trade/widget.js"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;MetaTraderWebTerminal(&nbsp;"webterminal",&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version:&nbsp;4,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server:&nbsp;"MetaQuotes-Demo",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;demoAllServers:&nbsp;true,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startMode:&nbsp;"create_demo",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lang:&nbsp;"en",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colorScheme:&nbsp;"black_on_white"</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;);</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">Configuring the account opening form (type, leverage, balance)</span></p><p class="p_tableatten"><span class="f_tableatten">Available account types, leverage and balance in the account opening form are determined by your White Label settings. To change them, go to <a href="https://support.metaquotes.net/en/download/mt4" target="_blank" class="weblink">App Store \ Download \ MetaTrader 4\ MetaTrader 4 WhiteLabels</a> on the technical support website.</span></p><p class="p_tableatten"><span class="f_tableatten">&nbsp;</span></p><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">Disable downloading the web terminal page in IFRAME</span></p><p class="p_tableatten"><span class="f_tableatten">An attacker can place an invisible IFRAME containing the page of your website with the web terminal and combine the web terminal control element (such as a button) with another link on their website. Thus, when clicking a link, a user may actually perform an action necessary to the attacker.</span></p><p class="p_tableatten"><span class="f_tableatten">Add <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options" target="_blank" class="weblink" title="Example of X-Frame-Options: DENY configuration">X-Frame-Options: DENY</a> HTTP response header to your page containing the web terminal in order to disable downloading the page in IFRAME and protect users.</span></p><p class="p_tableatten"><span class="f_tableatten">&nbsp;</span></p><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">The web terminal widget should only be used on https pages</span></p><p class="p_tableatten"><span class="f_tableatten">The page on which the widget is installed must work over a secure https protocol (not http). Otherwise, the operation of the web terminal will not be possible in some browsers (for example Chrome version 60 and higher).</span></p></td></tr></tbody></table>

## How to track accounts opened via the web terminal [#](web_terminal#track)

Special UTM parameters are added to all demo accounts opened from the web terminal. Such UTM tags inform the broker that the potential client has come from a web terminal operating on the broker's website. The tags are added to the [trading account parameters](/en/docs/mt4/administrator/administration/ug_accounts#leadsource):

-   The Comment field contains the following details: "WebTerminal \[the short name of the domain from which the account was opened\]". Example: "WebTerminal mysite.com". The "www" part is removed from the address.
-   The domain name with 'www' is also added in the 'Lead source'‌ field. Example: "www.mysite.com". The value can be overridden by adding utm\_campaign to the widget parameters.

To use your own tags for tracking clients, add the [utmSource and utmCampaign parameters](/en/docs/mt4/administrator/web_terminal#utm) to the web terminal widget.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;id=</span><span class="f_CodeExample" style="color: #219161;">"webterminal"</span><span class="f_CodeExample">&nbsp;style=</span><span class="f_CodeExample" style="color: #219161;">"width:100%;height:600px;"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://metatraderweb.app/trade/widget.js"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;MetaTraderWebTerminal(&nbsp;"webterminal",&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version:&nbsp;4,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server:&nbsp;"MetaQuotes-Demo",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #dce6f2;">utmCampaign:&nbsp;"www.abcbroker.com"</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #dce6f2;">utmSource:&nbsp;"web.demo"</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;demoAllServers:&nbsp;true,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startMode:&nbsp;"create_demo",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lang:&nbsp;"en",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colorScheme:&nbsp;"black_on_white"</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;);</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

For the widget added to the www.abcbroker.com site, account parameters will be filled as follows:

-   Comment = abcbroker.com
-   Lead source = www.abcbroker.com

![Tracking account registrations via the web terminal](/en/docs/mt4/administrator/img/webterminal_utm.png "Tracking account registrations via the web terminal")

## Detecting the WebTerminal Language

The web terminal determines the interface language based on the following priorities:

-   The language selected by the user in the web terminal
-   The language specified in lang (if the language is supported in the web terminal)
-   The preferred language in the user's web browser (if the language is supported in the web terminal)

If the web terminal cannot determine the language, English will be used.

## Operation Features

The maximum number of symbols a client can enable in the Market Watch window is 300 for all browsers, except for Internet Explorer/Edge — 50. A greater number of symbols in Internet Explorer/Edge slows down the web terminal operation.

## If you have two platforms: MetaTrader 5 and MetaTrader 4 [#](web_terminal#version)

A single web terminal is used for both platform versions. If you only use one platform (MetaTrader 4 or MetaTrader 5), no additional actions are required. Simply select the necessary one [when receiving the code for insertion](/en/docs/mt4/administrator/web_terminal#version_param).

If you simultaneously use two versions of the trading platform, you do not need to configure WebTerminals separately. If the web terminal finds servers of both versions in the "[Trade server list](/en/docs/mt4/administrator/web_terminal#servers)" parameter, a switch between the two versions appears in the web terminal interface. It is available in the account connection dialog, in the account opening dialog and in the File menu.

![Switching between WebTerminal Versions](/en/docs/mt4/administrator/img/webterminal_version.png "Switching between WebTerminal Versions")

### Setting the default version

In order to set a default version that will be selected during the web terminal launch, use the [Version parameter](/en/docs/mt4/administrator/web_terminal#version_param):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;id=</span><span class="f_CodeExample" style="color: #219161;">"webterminal"</span><span class="f_CodeExample">&nbsp;style=</span><span class="f_CodeExample" style="color: #219161;">"width:100%;height:600px;"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://metatraderweb.app/trade/widget.js"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;MetaTraderWebTerminal(&nbsp;"webterminal",&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #dce6f2;">version:&nbsp;4</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #dce6f2;">servers:&nbsp;["ForexBroker4-Live","ForexBroker5-Live"]</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;demoAllServers:&nbsp;true,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startMode:&nbsp;"create_demo",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lang:&nbsp;"en",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colorScheme:&nbsp;"black_on_white"</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;);</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

In this example, the versions switch is set to MetaTrader 4 by default.

If a user switches to another platform, the selection will be remembered. During the next launch of the WebTerminal, it will be switched to the latest used version of the platform.

## Supported Browser Versions

The web terminal supports the following web browser versions and above:

-   Internet Explorer 11
-   Microsoft Edge 12
-   Mozilla Firefox 34
-   Google Chrome 43
-   Safari 8
-   Opera 32

## Example of Adding a WebTerminal Widget

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">!DOCTYPE</span><span class="f_CodeExample">&nbsp;html&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">html</span><span class="f_CodeExample">&nbsp;lang=</span><span class="f_CodeExample" style="color: #219161;">"en"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">head</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">meta</span><span class="f_CodeExample">&nbsp;http-equiv=</span><span class="f_CodeExample" style="color: #219161;">"Content-Type"</span><span class="f_CodeExample">&nbsp;content=</span><span class="f_CodeExample" style="color: #219161;">"text/html;&nbsp;charset=utf-8"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">title</span><span class="f_CodeExample">&gt;WebTerminal&nbsp;for&nbsp;the&nbsp;MetaTrader&nbsp;4&nbsp;and&nbsp;MetaTrader&nbsp;5&nbsp;platforms&lt;</span><span class="f_CodeExample" style="color: #993300;">/title</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">style</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/css"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">body&nbsp;{margin:&nbsp;0;&nbsp;padding:&nbsp;0;&nbsp;font-family:&nbsp;Arial,&nbsp;Tahoma;&nbsp;font-size:&nbsp;16px;&nbsp;color:&nbsp;#000;&nbsp;background-color:&nbsp;#FFF;&nbsp;min-width:&nbsp;1010px}</span><br><span class="f_CodeExample">.top&nbsp;{background-color:&nbsp;#0055A7;}</span><br><span class="f_CodeExample">.top&nbsp;h1&nbsp;{margin:&nbsp;10px&nbsp;20px&nbsp;10px&nbsp;10px;&nbsp;font-size:&nbsp;25px;&nbsp;font-weight:&nbsp;normal;&nbsp;color:&nbsp;#FFF;&nbsp;display:&nbsp;inline-block;&nbsp;vertical-align:&nbsp;middle;&nbsp;}</span><br><span class="f_CodeExample">.top&nbsp;.menu,&nbsp;.top&nbsp;.menu&nbsp;li&nbsp;{margin:&nbsp;0;&nbsp;padding:&nbsp;0;&nbsp;list-style:&nbsp;none;&nbsp;display:&nbsp;inline-block;&nbsp;vertical-align:&nbsp;middle;&nbsp;}</span><br><span class="f_CodeExample">.top&nbsp;.menu&nbsp;li&nbsp;{margin:&nbsp;0;&nbsp;padding:&nbsp;0;&nbsp;list-style:&nbsp;none;&nbsp;display:&nbsp;inline-block;}</span><br><span class="f_CodeExample">.top&nbsp;.menu&nbsp;li&nbsp;a&nbsp;{padding:&nbsp;20px;&nbsp;font-size:&nbsp;16px;&nbsp;color:&nbsp;#FFF;&nbsp;text-decoration:&nbsp;none;&nbsp;text-align:&nbsp;center;&nbsp;display:&nbsp;block;}</span><br><span class="f_CodeExample">.top&nbsp;.menu&nbsp;li&nbsp;a:hover&nbsp;{background-color:&nbsp;#0B6ABF;}</span><br><span class="f_CodeExample">.top&nbsp;.menu&nbsp;li&nbsp;a.selected&nbsp;{background-color:&nbsp;#2989DF;&nbsp;color:&nbsp;#FFF;}</span><br><span class="f_CodeExample">.content&nbsp;{&nbsp;box-shadow:&nbsp;0&nbsp;0&nbsp;20px&nbsp;rgba(0,0,0,0.5);&nbsp;position:&nbsp;relative;&nbsp;}</span><br><span class="f_CodeExample">.footer&nbsp;{text-align:&nbsp;center;&nbsp;padding:&nbsp;20px;&nbsp;color:&nbsp;#0A0A0A;&nbsp;font-size:&nbsp;14px}</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/style</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/head</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">body</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"top"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">h1</span><span class="f_CodeExample">&gt;BROKER&lt;</span><span class="f_CodeExample" style="color: #993300;">/h1</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">ul</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"menu"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&gt;Analytics&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"selected"</span><span class="f_CodeExample">&gt;WebTerminal&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&gt;News&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&gt;Contacts&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/ul</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"content"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;!--&nbsp;Web&nbsp;Terminal&nbsp;Code&nbsp;Start&nbsp;--&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;id=</span><span class="f_CodeExample" style="color: #219161;">"webterminal"</span><span class="f_CodeExample">&nbsp;style=</span><span class="f_CodeExample" style="color: #219161;">"width:100%;height:600px;"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://metatraderweb.app/trade/widget.js"</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">script</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/javascript"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;new&nbsp;MetaTraderWebTerminal(&nbsp;"webterminal",&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version:&nbsp;4,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server:&nbsp;"MetaQuotes-Demo",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;demoAllServers:&nbsp;true,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startMode:&nbsp;"create_demo",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lang:&nbsp;"en",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colorScheme:&nbsp;"black_on_white"</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;);</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/script</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;!--&nbsp;Web&nbsp;Terminal&nbsp;Code&nbsp;End&nbsp;--&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"footer"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">Copyright&nbsp;2000-2015,&nbsp;Broker</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/body</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/html</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

[Trading platform video guides](/en/docs/mt4/metaeditor/video_guides)

[MultiTerminal](/en/docs/mt4/multiterminal)