# WebTrader

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/net/net_webtrader

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
            -   [Getting Started](/en/docs/mt5/api/webapi_preparing)
            -   [Format of Commands](/en/docs/mt5/api/webapi_https)
            -   [Authentication](/en/docs/mt5/api/webapi_rest_authentication)
            -   [Escaping Special Characters](/en/docs/mt5/api/webapi_screening)
            -   [Maintaining Connections](/en/docs/mt5/api/webapi_pings)
            -   [Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)
            -   [Examples](/en/docs/mt5/api/webapi_examples)
            -   [Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)
                -   [Configuration Databases](/en/docs/mt5/api/webapi_main/webapi_config)
                -   [Trading](/en/docs/mt5/api/webapi_main/webapi_trading)
                -   [Users](/en/docs/mt5/api/webapi_main/webapi_users)
                -   [Clients](/en/docs/mt5/api/webapi_main/webapi_client)
                -   [Mail](/en/docs/mt5/api/webapi_main/webapi_mail)
                -   [News](/en/docs/mt5/api/webapi_main/webapi_news)
                -   [Prices](/en/docs/mt5/api/webapi_main/webapi_prices)
                -   [Daily Reports](/en/docs/mt5/api/webapi_main/webapi_daily)
                -   [Settings Files](/en/docs/mt5/api/webapi_main/webapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription)
                -   [Common Requests](/en/docs/mt5/api/webapi_main/webapi_common_request)
                -   [Outdated version of Rest API](/en/docs/mt5/api/webapi_main/webapi_old)
                -   [PHP Implementation of Protocol](/en/docs/mt5/api/webapi_main/php)
                -   [.NET Implementation of Protocol](/en/docs/mt5/api/webapi_main/net)
                    -   [MT5WebAPI Class](/en/docs/mt5/api/webapi_main/net/net_mtwebapi)
                    -   [WebTrader](/en/docs/mt5/api/webapi_main/net/net_webtrader)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)[.NET Implementation of Protocol](/en/docs/mt5/api/webapi_main/net)WebTrader

# WebTrader

The .NET implementation of the MetaTrader 5 Web API protocol includes an example of its use in the form of a source code of a finished website. Example is a Microsoft Visual Studio project. It is located in directory /Examples/NET/WebTrader.

## Running the Demo Site in Your Local Computer

For the first start of the demo site, open the WebTrader Microsoft Visual Studio project.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To compile the project, you will need Microsoft Visual Studio Web Developer 2008 Express Edition with ASP.NET MVC 2.</span></p></td></tr></tbody></table>

After opening the project, open the file Web.config, which is in the root directory of the project.

![The WebTrader project in Microsoft Visual Studio](/en/docs/mt5/api/img/webapi_net_studio.png "The WebTrader project in Microsoft Visual Studio")

In the block <appSettings> you must configure the project to connect to your MetaTrader 5 platform. Replace the values (value="") of the following parameters:

-   metatrader\_server — the IP address of your trading platform.
-   metatrader\_port —  the port of the access server, through which connection to the platform is established.
-   metatrader\_login — the login of the [manager account](/en/docs/mt5/api/webapi_preparing#manager_configuration) that will be used for connection.
-   metatrader\_password — the API password of the manager account.
-   metatrader\_crypt — data encryption type. A value of 1 means that encryption is enabled. A value of 0 means that encryption is disabled.
-   metatrader\_pump — the data pumping mode for connection. Currently pumping is not supported for this parameter, so use the default 0 value.
-   metatrader\_default\_deposit — the deposit that will be used for demo accounts created form the WebTrader interface.

After you specify all the settings, compile the project. Then run the system utility program IIS Manager. Select Sites and choose "Add a Web Site" from the context menu:

![Adding a Web Site in IIS Manager](/en/docs/mt5/api/img/webapi_net_iss_manager.png "Adding a Web Site in IIS Manager")

This will bring up a window to add a website:

![Adding a Website](/en/docs/mt5/api/img/webapi_net_iss_manager_add.png "Adding a Website")

Specify the following parameters in this window:

-   Web site name — any name. In this example it is WebTrader.
-   Physical path — the path to the folder of the WebTrader project. In this example the path is D:\\Program Files\\MetaTrader 5 Web API\\Web\\Examples\\Net\\WebTrader.
-   Host name (block Binding) — the address at which the WebTrader page will open. In this case it is www.WebTrader.api.

After setting up the site, click "OK." To open the specified address on your computer, open the file hosts, located in the directory C:\\Windows\\System32\\drivers\\etc. Add the following entry to this file:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">127.0.0.1&nbsp;WebTrader.api</span></p></td></tr></tbody></table>

After you save the changes, go back to the IIS Manager and run the website. Then you can open a demo site in your browser.

## The Features of the Demo Site

Below is the homepage of the demo site:

![Home](/en/docs/mt5/api/img/webapi_net_start_page.png "Home")

Clicking "Registration" will take you to creation of a new demo account on the trading server. Account registration form will open:

![Account registration](/en/docs/mt5/api/img/webapi_net_registration.png "Account registration")

Also on the home page you can go to the trader's personal area. To do this, enter the login and password of an existing account. The trader's personal area contains the list of orders, deals and positions:

![Trader's area](/en/docs/mt5/api/img/webapi_net_room.png "Trader's area")

You can use all of these features of the demo site in your project by copying and modifying the source code of the WebTrader project.

[CustomSend](/en/docs/mt5/api/webapi_main/net/net_mtwebapi/net_custom/net_customsend)

[SQL Export](/en/docs/mt5/api/sql_export)