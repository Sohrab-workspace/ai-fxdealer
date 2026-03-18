# MetaTrader 5 WebTerminal

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/web_terminal

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

[MetaTrader 5](/en/docs/mt5)WebTerminal

# MetaTrader 5 WebTerminal

The MetaTrader 5 WebTerminal enables financial market trading using any web browser. It works in all operating systems and browsers, while requiring no extra software installations. All transmitted data is securely encrypted.

The web terminal supports all types of market and pending orders, as well as one-click trading. Traders can view real-time quotes and analyze charts using basic graphical objects. Charts can be analyzed using 30 technical indicators.

The terminal is a modern HTML5 application that can be easily integrated into any website via a simple iframe widget.

The web terminal is located entirely on the broker's access servers. It operates as an individual web terminal, which only works with your platform. This provides maximum security and full control for the broker.

When connecting to the web terminal via your website, the trader should only enter the login and password, without having to select a server. The platform will determine which server (demo, real, main or additional trading server) the account belongs to. For the seamless web terminal integration with the clients area on the broker website, the user login can be pre-selected to let your client enter a password only. If a user saves a password in a browser storage, the account will be connected automatically on the next run.

![MetaTrader 5 Web Terminal](/en/docs/mt5/platform/img/webterminal_new.png "MetaTrader 5 Web Terminal")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The web terminal only operates with the trading platform version 3440 or higher.</span></li><li class="p_tableatten"><span class="f_tableatten">If your platform license does not include the web terminal, <a href="https://support.metaquotes.net/en/market/product/248" target="_blank" class="weblink" title="Order MetaTrader 5 Web Terminal">order it via the App Store section</a> of the Support Center website.</span></li></ul></td></tr></tbody></table>

## How to set up the platform

The web terminal operates on an [access server](/en/docs/mt5/platform/components/access_server) which acts as a web server.

Register a domain (or a subdomain for your existing domain) where the web terminal will run. Below we use the domain webtrading.broker.com as an example — you should replace it with your own domain.

Associate your domain with the [public IP address](/en/docs/mt5/platform/administration/admin_network/network_add_edit#public) of your access server. For this purpose, the appropriate record must be specified on the DNS hosting. For example, for webtrading.broker.com host, the following entry should be registered in DNS: "XXX.XXX.XXX.XXX webtrading.broker.com", where XXX.XXX.XXX.XXX is the public address of the access server.

Next, open [Integration \\ Web services](/en/docs/mt5/platform/administration/integration/integration_web_services) in MetaTrader 5 Administrator and add an SSL certificate for the domain. The certificate will enable connections to the access server using the HTTPS protocol.

You can add extra certificates for your White Label partners to provide a separate web terminal for each required company's domain. After that, in the relevant field, specify which company the domain belongs to.

![Add a certificate for the domain where the web terminal will run](/en/docs/mt5/platform/img/webterminal_webservices.png "Add a certificate for the domain where the web terminal will run")

It is recommended to have port 443 available on the server for HTTPS connections. In this case, your clients will not need to explicitly specify the port in the address bar to open the web terminal page.

No other settings are needed. Your web terminal will be available at https://webtrading.broker.com/terminal/.

## If you have multiple access servers

For each platform we [recommend](/en/docs/mt5/platform/platform_installation/requirements#recommended) using at least two access servers: for the main and backup configuration. As your customer database grows and your business geography expands, the number of servers will increase to ensure high-quality service.

To enable connections to your web terminal via any of your access servers, add A-records with their public addresses to the DNS server. Thus, you will have several records with different addresses but with the same domain:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">XXX.XXX.XXX.XXX webtrading.broker.com</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">YYY.YYY.YYY.YYY webtrading.broker.com</span></p><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">ZZZ.ZZZ.ZZZ.ZZZ webtrading.broker.com</span></p></td></tr></tbody></table>

XXX, YYY and ZZZ are the addresses of your access servers. There can be any number of them.

No additional actions are required on the platform side. The domain certificate uploaded via the Integration \\ Web Services section is used for all access servers.

To balance the load by distributing connections to the web terminal between access servers, use GeoDNS or GLSB services. Please check with your hosting provider whether this service is available.

## If you hold multiple licenses

If you have multiple MetaTrader 5 platform licenses, for example, the main cluster for live accounts and an [additional cluster for demo accounts](https://support.metaquotes.net/en/market/product/569), you should configure web terminals separately for each of them. The web terminal runs on access servers which belong to a particular platform, and thus they do not know about the existence of other platforms.

With such a configuration, you will have different web terminal links for each platform. You need to provide the option to select the desired platform for your customers. For example, you can implement a drop-down list on your website.

## How to add the web terminal to your site

To install the web terminal on your site, simply place the <iframe> tag on the desired page. The address of your web terminal should be specified as the source in this tag:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;!</span><span class="f_CodeExample" style="color: #993300;">DOCTYPE</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #993300;">html</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">html</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">head</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">meta</span><span class="f_CodeExample">&nbsp;charset=</span><span class="f_CodeExample" style="color: #219161;">"UTF-8"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">title</span><span class="f_CodeExample">&gt;Web&nbsp;Terminal&lt;</span><span class="f_CodeExample" style="color: #993300;">/title</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;/</span><span class="f_CodeExample" style="color: #993300;">head</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">body</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://webtrading.broker.com/terminal?mode=connect&amp;marketwatch=EURUSD,GBPUSD,USDJPY&amp;utm_campaign=webterminal&amp;utm_source=site"</span><span class="f_CodeExample">&nbsp;width=</span><span class="f_CodeExample" style="color: #219161;">"100%"</span><span class="f_CodeExample">&nbsp;height=</span><span class="f_CodeExample" style="color: #219161;">"1000"</span><span class="f_CodeExample">&gt;&lt;/</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;/</span><span class="f_CodeExample" style="color: #993300;">body</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;/</span><span class="f_CodeExample" style="color: #993300;">html</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

Additional web terminal settings can be specified as URL parameters:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://webtrading.broker.com/terminal</span><span class="f_CodeExample" style="color: #219161; background-color: #dce6f2;">?parameter1=value1&amp;parameter2=value2</span><span class="f_CodeExample" style="color: #219161;">"</span><span class="f_CodeExample">&gt;&lt;/</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

The following parameters are supported:

first\_name, second\_name, email — first name, last name and email to be inserted into the demo and real account registration form. By using these parameters, you can make account opening easier for traders who have already registered on your site and provided the required data. Example:

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?mode=demo&amp;</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">first_name=John&amp;second_name=Smith&amp;email=johnsmith%40mail.com</span></p></td></tr></tbody></table>

Please note that the example includes the "mode=demo" parameter to automatically open the demo account registration form upon the web terminal launch.

utm\_campaign, utm\_source — utm parameters that will be added to the [relevant fields of accounts](/en/docs/mt5/platform/administration/admin_accounts/account_edit#leadsource) opened via the web terminal. Using them, you can analyze how efficiently you attract traders via web terminals. For further details please see ["How to track accounts opened via the web terminal"](/en/docs/mt5/platform/components/web_terminal#track). Example:

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">utm_campaign=webterminal&amp;utm_source=site</span></p></td></tr></tbody></table>

The parameters are used only at the first start. After that the web terminal will use the user-specified data.

mode — the web terminal page that opens on first launch. Supported values:

-   demo — demo account registration form
-   real — real account registration form
-   connect — existing account connection form

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">mode=connect</span></p></td></tr></tbody></table>

The parameter is used only if the user has not previously connected to the account. If the web terminal has a saved account, it will be connected immediately upon startup.

login — trading account for connection. If this parameter is specified, the web terminal will be launched with a pre-filled account connection dialog. The user will only have to enter a password. Use this parameter to create convenient client areas.

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">login=123456</span></p></td></tr></tbody></table>

If an account is specified in the URL, no demo account will be crated at the first launch (the option is managed via [platform settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups)). This also prevents from connecting using a previously saved account.

marketwatch — the list of symbols to be displayed by default in Market Watch is specified by the marketwatch parameter. Example:

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">marketwatch=EURUSD,GBPUSD,AUDCAD,USDJPY</span></p></td></tr></tbody></table>

The parameter also determines the order in which the symbols are displayed. In the example above, on the first web terminal launch the user will see only four specified symbols in the Market Watch window, EURUSD will be the first and USDJPY will be the last. Later the user can re-configure the list of symbols, and the new settings will be saved in the browser. The maximum number of symbols in the parameter is 300.

theme-mode — theme for the application interface. Possible values:

-   0 — light (default)
-   1 — dark

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">theme-mode=1</span></p></td></tr></tbody></table>

The parameter is only used for the first start. After that the web terminal will use user-specified settings. If necessary, you can force a user-defined theme to be overridden. This may be useful, for example, if your site supports light and dark themes. This will allow the synchronization of interface switching modes of the site and the web terminal.

To switch the color scheme of the web terminal, call postMessage on the <iframe> element, through which the web terminal is loaded. Specify the parameters type: 'mt5\_update' and theme-mode: 0 (for the light theme) or 1 (for the dark theme):

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="font-weight: bold;">const</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&nbsp;=&nbsp;document.getElementById(</span><span class="f_CodeExample" style="color: #219161;">'iframe'</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">.</span><span class="f_CodeExample" style="color: #993300;">contentWindow</span><span class="f_CodeExample">.</span><span class="f_CodeExample" style="color: #993300;">postMessage</span><span class="f_CodeExample">({</span><br><span class="f_CodeExample">&nbsp;&nbsp;type:&nbsp;</span><span class="f_CodeExample" style="color: #219161;">'mt5_update'</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #219161;">'theme-mode'</span><span class="f_CodeExample">:&nbsp;1,</span><br><span class="f_CodeExample">},&nbsp;</span><span class="f_CodeExample" style="color: #219161;">'*'</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

theme — color scheme for the application interface. Possible values:

-   greenRed — red and green (default)
-   blueRed — blue and red
-   blackWhite — black and white
-   neutral — neutral

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">theme=blueRed</span></p></td></tr></tbody></table>

The parameter is used only at the first start. After that, the web terminal will apply user-specified settings.

The parameter is only used for the first start. Then the web terminal will apply user-specified settings.

lang — web terminal interface language. The following languages are currently supported:

-   English (en), Arabic (ar), Bulgarian (bg), Czech (cs), Chinese Simplified (zh), Chinese Traditional (zt), Hebrew (he), Hungarian (hu), Dutch (nl), French (fr) ), German (de), Greek (el), Hindi (hi),
-   Indonesian (id), Italian (it), Japanese (ja), Korean (ko), Malay (ms), Persian (fa), Polish (pl), Portuguese (pt), Romanian (ro), Russian (ru), Spanish (es), Thai (th), Turkish (tr), Ukrainian (uk), Uzbek (uz), Vietnamese (vi)

<table class="help" cellspacing="0" cellpadding="5" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:5px; border:none"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal?</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">lang=de</span></p></td></tr></tbody></table>

The parameter is used only at the first start. After that, the web terminal will apply user-specified settings.

The size of the web terminal window on the page can be set using standard "width" and "height" parameters in the <iframe> tag, for example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://webtrading.broker.com/terminal"</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="background-color: #dce6f2;">width=</span><span class="f_CodeExample" style="color: #219161; background-color: #dce6f2;">"100%"</span><span class="f_CodeExample" style="background-color: #dce6f2;">&nbsp;height=</span><span class="f_CodeExample" style="color: #219161; background-color: #dce6f2;">"1000"</span><span class="f_CodeExample">&gt;&lt;/</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

Generally we recommended to set the width and height to 100% so that the web terminal block takes up all the available web page space. If you specify an absolute size in pixels, some elements may be out of the visible window on some devices.

## How to set up the account opening form

To configure the account opening form, use MetaTrader 5 Administrator. Go to the [Allocations](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups) section and set available account types, leverages and balance. These settings apply to all terminals, including desktop, mobile and web.

## Security settings

Prevent the web terminal page from loading in IFRAME. An attacker can place an invisible IFRAME containing the page of your website with the web terminal and combine the web terminal control element (such as a button) with another link on their website. Thus, when clicking a link, a user may actually perform an action necessary to the attacker.

Add [X-Frame-Options: DENY](https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options "Example of X-Frame-Options: DENY configuration") HTTP header to your page containing the web terminal in order to disable page loading in IFRAME and protect users.

Only use the web terminal widget on https pages. The page on which the widget is installed must work over a secure https protocol (not http). Otherwise, the operation of the web terminal will not be possible in some browsers (for example Chrome version 60 and higher).

## How to track accounts opened via the web terminal [#](web_terminal#track)

Special UTM parameters are added to all accounts opened via the web terminal. Such UTM parameters inform the broker that the potential client has come from a web terminal operating on the broker's website. The UTM tags are added to the [trading account parameters](/en/docs/mt5/platform/administration/admin_accounts/account_edit#leadsource):

-   The Comment field will contain "WebTerminal \[short name of the domain from which the account was opened\]". Example: "WebTerminal mysite.com". The "www" part is removed from the address.
-   The domain name with 'www' is also added in the 'Lead source'‌ field. Example: "www.mysite.com". The value can be overridden by adding utm\_source to the widget parameters.
-   The 'Lead campaign' field is not filled by default. You may add utm\_campaign to widget parameters in order to write the name of your marketing campaign to this field.

To use your own UTM parameters for tracking clients, add the [utm\_source and utm\_campaign parameters](/en/docs/mt5/platform/components/web_terminal#utm) to the web terminal widget.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExampleWrap"><span class="f_CodeExampleWrap">https://webtrading.broker.com/terminal</span><span class="f_CodeExampleWrap" style="background-color: #dce6f2;">?utm_campaign=webterminal&amp;utm_source=site</span></p></td></tr></tbody></table>

For the widget added to the www.abcbroker.com site, account parameters will be filled as follows:

-   Comment = WebTerminal
-   Lead source = www.abcbroker.com
-   Lead campaign = web.demo

![Tracking account registrations via the web terminal](/en/docs/mt5/platform/img/webterminal_utm.png "Tracking account registrations via the web terminal")

## Mobile version of the web platform [#](web_terminal#mobile)

The MetaTrader 5 web platform includes a special version adapted for iOS and Android smartphones and tablets. This enables convenient trading from mobile browsers in addition to desktop ones.

No additional settings for the mobile version are needed. The web terminal will automatically detect the user's device by the browser's "user-agent" and will adapt the interface.

![Mobile version of the MetaTrader 5 web platform](/en/docs/mt5/platform/img/webterminal_new_mobile.png "Mobile version of the MetaTrader 5 web platform")

You can also embed a web terminal in your mobile app. To do this, create a web form in it with the web terminal <iframe>.

## Minimum browser versions

The web terminal supports the following web browser versions and above:

-   Microsoft Edge 15
-   Mozilla Firefox 54
-   Google Chrome 51
-   Safari 12
-   Opera 38

## Troubleshooting

If a trader receives a 404 error when trying to open the web terminal page, check the following:

-   The SSL certificate you uploaded in the Integration \\ Web Service section is valid and has not expired
-   Your company name is specified correctly in the SSL certificate — it must match the company name specified in the license/White Label
-   Your platform does not run under a test license — in this case the web terminal is not available
-   The web terminal is included in your platform license. Contact the [support team](https://support.metaquotes.net/en/support) to check the license

## Web terminal widget example

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">!DOCTYPE</span><span class="f_CodeExample">&nbsp;html&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">html</span><span class="f_CodeExample">&nbsp;lang=</span><span class="f_CodeExample" style="color: #219161;">"en"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">head</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">meta</span><span class="f_CodeExample">&nbsp;http-equiv=</span><span class="f_CodeExample" style="color: #219161;">"Content-Type"</span><span class="f_CodeExample">&nbsp;content=</span><span class="f_CodeExample" style="color: #219161;">"text/html;&nbsp;charset=utf-8"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">title</span><span class="f_CodeExample">&gt;WebTerminal&nbsp;for&nbsp;the&nbsp;MetaTrader&nbsp;5&nbsp;platforms&lt;</span><span class="f_CodeExample" style="color: #993300;">/title</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">style</span><span class="f_CodeExample">&nbsp;type=</span><span class="f_CodeExample" style="color: #219161;">"text/css"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;body&nbsp;{margin:&nbsp;0;&nbsp;padding:&nbsp;0;&nbsp;font-family:&nbsp;Arial,&nbsp;Tahoma;&nbsp;font-size:&nbsp;16px;&nbsp;color:&nbsp;#000;&nbsp;background-color:&nbsp;#FFF;&nbsp;min-width:&nbsp;1010px}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.top&nbsp;{background-color:&nbsp;#0055A7;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.top&nbsp;h1&nbsp;{margin:&nbsp;10px&nbsp;20px&nbsp;10px&nbsp;10px;&nbsp;font-size:&nbsp;25px;&nbsp;font-weight:&nbsp;normal;&nbsp;color:&nbsp;#FFF;&nbsp;display:&nbsp;inline-block;&nbsp;vertical-align:&nbsp;middle;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.top&nbsp;.menu,&nbsp;.top&nbsp;.menu&nbsp;li&nbsp;{margin:&nbsp;0;&nbsp;padding:&nbsp;0;&nbsp;list-style:&nbsp;none;&nbsp;display:&nbsp;inline-block;&nbsp;vertical-align:&nbsp;middle;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.top&nbsp;.menu&nbsp;li&nbsp;{margin:&nbsp;0;&nbsp;padding:&nbsp;0;&nbsp;list-style:&nbsp;none;&nbsp;display:&nbsp;inline-block;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.top&nbsp;.menu&nbsp;li&nbsp;a&nbsp;{padding:&nbsp;20px;&nbsp;font-size:&nbsp;16px;&nbsp;color:&nbsp;#FFF;&nbsp;text-decoration:&nbsp;none;&nbsp;text-align:&nbsp;center;&nbsp;display:&nbsp;block;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.top&nbsp;.menu&nbsp;li&nbsp;a:hover&nbsp;{background-color:&nbsp;#0B6ABF;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.top&nbsp;.menu&nbsp;li&nbsp;a.selected&nbsp;{background-color:&nbsp;#2989DF;&nbsp;color:&nbsp;#FFF;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.content&nbsp;{&nbsp;box-shadow:&nbsp;0&nbsp;0&nbsp;20px&nbsp;rgba(0,0,0,0.5);&nbsp;position:&nbsp;relative;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.footer&nbsp;{text-align:&nbsp;center;&nbsp;padding:&nbsp;20px;&nbsp;color:&nbsp;#0A0A0A;&nbsp;font-size:&nbsp;14px}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">/style</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/head</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">body</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"top"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">h1</span><span class="f_CodeExample">&gt;BROKER&lt;</span><span class="f_CodeExample" style="color: #993300;">/h1</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">ul</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"menu"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&gt;Analytics&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"selected"</span><span class="f_CodeExample">&gt;WebTerminal&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&gt;News&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">li</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">a</span><span class="f_CodeExample">&nbsp;href=</span><span class="f_CodeExample" style="color: #219161;">"#"</span><span class="f_CodeExample">&gt;Contacts&lt;</span><span class="f_CodeExample" style="color: #993300;">/a</span><span class="f_CodeExample">&gt;&lt;</span><span class="f_CodeExample" style="color: #993300;">/li</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">/ul</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"content"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;Web&nbsp;Terminal&nbsp;Code&nbsp;Start&nbsp;--&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&nbsp;src=</span><span class="f_CodeExample" style="color: #219161;">"https://webtrading.broker.com/terminal?mode=connect&amp;marketwatch=EURUSD,GBPUSD,USDJPY&amp;utm_campaign=webterminal&amp;utm_source=site"</span><span class="f_CodeExample">&nbsp;width=</span><span class="f_CodeExample" style="color: #219161;">"100%"</span><span class="f_CodeExample">&nbsp;height=</span><span class="f_CodeExample" style="color: #219161;">"1000"</span><span class="f_CodeExample">&gt;&lt;/</span><span class="f_CodeExample" style="color: #993300;">iframe</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;Web&nbsp;Terminal&nbsp;Code&nbsp;End&nbsp;--&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">div</span><span class="f_CodeExample">&nbsp;class=</span><span class="f_CodeExample" style="color: #219161;">"footer"</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;Copyright&nbsp;2000-2015,&nbsp;Broker</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&lt;</span><span class="f_CodeExample" style="color: #993300;">/div</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/body</span><span class="f_CodeExample">&gt;</span><br><span class="f_CodeExample">&lt;</span><span class="f_CodeExample" style="color: #993300;">/html</span><span class="f_CodeExample">&gt;</span></p></td></tr></tbody></table>

[Tablet Version](/en/docs/mt5/android/tablet)

[API](/en/docs/mt5/api)