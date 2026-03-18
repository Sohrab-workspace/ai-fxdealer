# MQL5 Cloud Protector: Advanced Protection for Your Programs

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/development/mql5_cloud_protector

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

# MQL5 Cloud Protector: Advanced Protection for Your Programs

MQL5 Cloud Protector is an online service that proves advanced protection for MQL-programs.

Executable files EX4/EX5 are reliably protected from compilation. MQL5 Cloud Protector provides an advanced protection level for your applications. A similar method is used in the largest store of trading applications [MetaTrader Market](https://www.mql5.com/en/market), where the EX4/EX5 product files submitted by sellers are additionally compiled to [native code](https://en.wikipedia.org/wiki/machine_code). The only difference of MQL5 Cloud Protector from the mechanism used in the Market, is that the file is not linked to the user's computer. It can be run on any computers similar to common EX4/EX5 files.

## How It Works

MQL5 Cloud Protector is a secure service. Additional protection is only applied to a compiled file. The source code is not passed to the service. First, the program code is compiled into an EX4/EX5 file on the user's computer. Further, the executable part of the file is sent to the service via a secure connection. The service encrypts the file using modern asymmetric algorithms and signs it using a unique [private key](https://en.wikipedia.org/wiki/public-key_cryptography).

## How to Protect Your Program

In order to apply advanced protection to your executable file, open the project or the main source file of your MQL5 program and execute the "![MQL5 Cloud Protector](/en/docs/mt5/metaeditor/img/mql5_cloud_protector_icon.png "MQL5 Cloud Protector")MQL5 Cloud Protector" command from the Tools menu:

![Protecting a program via MQL5 Cloud Protector](/en/docs/mt5/metaeditor/img/mql5_cloud_protector.png "Protecting a program via MQL5 Cloud Protector")

The resulting executable file will be created in the same directory, where the project/the main source MQ5 file is located. The path to the file will be additionally specified in the compilation log.