# Connecting Accounts

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/accounts/ug_account_connect

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
        -   [Client Accounts](/en/docs/mt4/multiterminal/accounts)
            -   [Adding Accounts](/en/docs/mt4/multiterminal/accounts/ug_accounts)
            -   [Connecting Accounts](/en/docs/mt4/multiterminal/accounts/ug_account_connect)
            -   [Account Details](/en/docs/mt4/multiterminal/accounts/ug_account_details)
            -   [Open Orders](/en/docs/mt4/multiterminal/accounts/ug_account_orders)
            -   [Trade History](/en/docs/mt4/multiterminal/accounts/ug_account_history)
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

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Client Accounts](/en/docs/mt4/multiterminal/accounts)Connecting Accounts

# Connecting Accounts

To start managing trade accounts, it is necessary to connect them to the server. News, quotes, mail messages start to income in the terminal after connection, one can manage trade positions and place orders then.

One can connect all accounts to the server using the "File — Connect All" menu command, the corresponding button in the toolbar, or the "Connect All Accounts" command of the "Accounts" window context menu. A separate account can be connected to the server using the "Connect Account" command of the "Accounts" window context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The terminal sets limitations on the amount of demo accounts connected simultaneously. Only 10 demo accounts from the list of managed accounts can be connected to the server simultaneously. As for real accounts, the maximal number of simultaneously connected accounts is 128.</span></p></td></tr></tbody></table>

One can disconnect all accounts from the server using the "File — Disconnect All Accounts" menu command, the corresponding button in the toolbar, or the "Disconnect All Accounts" command of the "Accounts" window context menu. A separate account can be disconnected from the server using the "Disconnect Account" command of the "Accounts" window context menu.

If there are connected accounts with different deposit currencies, an additional command "Summary currency" appears in the context menu. It allows choosing the currency that will be used for the representation of the total result of all accounts, also it affects the calculation of the [allocation of the total volume between orders](/en/docs/mt4/multiterminal/getting_started/ug_setup#distribution) when opening positions.

[Adding Accounts](/en/docs/mt4/multiterminal/accounts/ug_accounts)

[Account Details](/en/docs/mt4/multiterminal/accounts/ug_account_details)