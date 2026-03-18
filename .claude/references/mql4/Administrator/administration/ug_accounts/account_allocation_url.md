# Account Redirection

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_accounts/account_allocation_url

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
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
                -   [Group Operations](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations)
                -   [Account Restore](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore)
                -   [Account Archive](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_archive)
                -   [Account Redirection](/en/docs/mt4/administrator/administration/ug_accounts/account_allocation_url)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Accounts](/en/docs/mt4/administrator/administration/ug_accounts)Account Redirection

# Account Redirection

In ["Account allocation URL"](/en/docs/mt4/administrator/administration/ug_options#allocation_url) parameter available in "Common" section one can the address a client is redirected to when opening an account from the client terminal. If the address is set, a trader is redirected to the specified web page when opening an account from the client terminal:

![Redirecting when opening an account](/en/docs/mt4/administrator/img/account_allocation_url.png "Redirecting when opening an account")

Request parameters separated by "&" symbol are additionally passed in the address line:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">https://www.accountallocation.url/?type=demo&amp;acp=1251&amp;label=CompanyName&amp;server=ServerName&amp;interface=English&amp;cid=3c8e1d9cd303dbd0d5686b729689d556</span></p></td></tr></tbody></table>

-   type — account type: demo or real.
-   acp — code page used by a trader.
-   label — name of the company which owns the terminal White Label.
-   server — name of the server a trader has selected when opening an account.
-   interface — client terminal's interface language.
-   cid — trader PC's unique ID.

When forming a request, the presence of "?" symbol in Account allocation URL parameter is checked. In other words, it is checked whether the specified address contains its own request parameters:

-   If there is no "?" symbol in the address, it is formed with the standard set of parameters described above. For example, https://www.mycompany.com.
-   If "?" symbol is present in the address, standard parameters are added to the specified custom ones. For example, if https://www.mycompany.com?utm\_campaign=terminal address is specified, the final line has the following look: https://www.mycompany.com?utm\_campaign=terminal&type=demo&acp=.... .

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The link address must start with "https://" or "http://".</span></p></td></tr></tbody></table>

[Account Archive](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_archive)

[Orders](/en/docs/mt4/administrator/administration/ug_orders)