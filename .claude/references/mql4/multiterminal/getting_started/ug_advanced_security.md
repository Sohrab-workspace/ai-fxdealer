# Security System

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/getting_started/ug_advanced_security

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
        -   [Getting Started](/en/docs/mt4/multiterminal/getting_started)
            -   [Security System](/en/docs/mt4/multiterminal/getting_started/ug_advanced_security)
            -   [Live Update](/en/docs/mt4/multiterminal/getting_started/ug_liveupdate)
            -   [Terminal Settings](/en/docs/mt4/multiterminal/getting_started/ug_setup)
        -   [Client Accounts](/en/docs/mt4/multiterminal/accounts)
        -   [Trading](/en/docs/mt4/multiterminal/trading)
        -   [Analytics](/en/docs/mt4/multiterminal/analytics)
        -   [User Interface](/en/docs/mt4/multiterminal/user_interface)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Getting Started](/en/docs/mt4/multiterminal/getting_started)Security System

# Security System

Data exchange between the Terminal and the server is performed by encryption based on 128-bit keys. This is sufficient to ensure security of trading. However, besides this system, terminal allows to use one more system: Advanced Security system based on digital signature algorithm of RSA. It is an asymmetric encryption algorithm that implies presence of a public and a private key. Public key can be freely distributed and used for checking the authenticity of a message signed with a private key. Knowing of the public key is guaranteed not to be possible basis for decoding the private one within an acceptable period of time. Decoding of the private key on the basis of the public one will take tens or hundreds of years even with modern powerful computers.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">The Advanced Security system based on electronic digital signatures can be enabled on the server.</span></li><li class="p_tableatten"><span class="f_tableatten">If the Advanced Security system is enabled for a trading account, for working at another computer, it is necessary to transfer the generated RSA keys into this other computer. The keys represent files with KEY extension and are stored in the /profiles folder.</span></li><li class="p_tableatten"><span class="f_tableatten">If either key has been lost or damaged, it is necessary to refer to the brokerage company technical support service.</span></li></ul></td></tr></tbody></table>

[Getting Started](/en/docs/mt4/multiterminal/getting_started)

[Live Update](/en/docs/mt4/multiterminal/getting_started/ug_liveupdate)