# Checking and Fixing Balance and Credit Funds

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/account_balance_check

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
                -   [Creating Account](/en/docs/mt5/platform/administration/admin_accounts/account_add)
                -   [Editing Account](/en/docs/mt5/platform/administration/admin_accounts/account_edit)
                -   [Preliminary Accounts](/en/docs/mt5/platform/administration/admin_accounts/preliminary_accounts)
                -   [Archive and Backup Bases](/en/docs/mt5/platform/administration/admin_accounts/accounts_archive)
                -   [Import of Accounts from File](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export)
                -   [Import of Accounts from MetaTrader 5](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt)
                -   [Checking and Fixing Balance](/en/docs/mt5/platform/administration/admin_accounts/account_balance_check)
                -   [Account Allocation Settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups)
                -   [Corporate Links](/en/docs/mt5/platform/administration/admin_accounts/corporate_links)
                -   [Links to Depositing and Withdrawing](/en/docs/mt5/platform/administration/admin_accounts/deposit_withdrawal)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Accounts](/en/docs/mt5/platform/administration/admin_accounts)Checking and Fixing Balance

# Checking and Fixing Balance and Credit Funds

["Accounts"](/en/docs/mt5/platform/administration/admin_accounts) section provides the ability to check clients' balance and credit funds based on [deals](/en/docs/mt5/platform/administration/admin_deals) history. Corrections can be necessary for [restoring the accounts](/en/docs/mt5/platform/administration/admin_accounts/accounts_archive) and manual correction of trade history.

To perform a check, enable "Balance" and "Credit" columns via the [context menu](/en/docs/mt5/platform/administration/admin_accounts#context).

![Balance and credit funds check](/en/docs/mt5/platform/img/accounts_balance.png "Balance and credit funds check")

Select one or several accounts, for which you want to check the balance and credit funds, and execute "Balance - Check Balance" command in the context menu. If an incorrect balance or credit funds value is revealed, the appropriate account will be highlighted in red.

![Balance and credit funds check results](/en/docs/mt5/platform/img/accounts_balance_checked.png "Balance and credit funds check results")

Two values will be displayed in "Balance" and "Credit" columns: the current balance/credit funds value will be displayed on the left, while the value calculated using the deals history - on the right.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Credit funds are checked by deals of <a href="/en/docs/mt5/platform/administration/admin_deals" class="topiclink">"Credit" type</a> (specified in "Action" field).</span></p></td></tr></tbody></table>

Check result is also displayed in the [journal](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal). If the calculated value differs from the current one, the following message will appear in the journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">account</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">xxx</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">has</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">invalid</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">balance:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">xxx.xx,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">valid:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">xxx.xx</span></p></td></tr></tbody></table>

To correct the balance/credit funds value, execute "Balance - Fix Balance" command in the context menu. The calculated value will be inserted as the current one. Correction results are also shown in the [journal](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">balance&nbsp;of&nbsp;account&nbsp;'1030390'&nbsp;has&nbsp;been&nbsp;fixed&nbsp;from&nbsp;9&nbsp;968.70&nbsp;to&nbsp;9&nbsp;999.80</span></p></td></tr></tbody></table>

[Import of Accounts from MetaTrader 5](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt)

[Account Allocation Settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups)