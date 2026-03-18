# Creating Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/account_add

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Accounts](/en/docs/mt5/platform/administration/admin_accounts)Creating Account

# Creating Accounts

To create an account, execute the "![New](/en/docs/mt5/platform/img/add_button.png "New") New" command in the ["Edit"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, standard part of the [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) or in the [context menu](/en/docs/mt5/platform/administration/admin_accounts#context) of the corresponding section.

![New Account](/en/docs/mt5/platform/img/account_new.png "New Account")

For convenience, the account settings in the window of account creation are divided into two boxes.

## Details

In this box the client's details are specified:

-   Preferred Login — account number. If you specify "Next" in this field the the closest free number will be assigned to the account. Do not use logins of deleted account when creating new ones.
-   Group — selection of a [group](/en/docs/mt5/platform/administration/admin_groups) the account will be created in.
-   Preferred Client — the [client](/en/docs/mt5/platform/administration/clients) to whom the account should be linked. Specify the ID, name or contact information in the Existing Client field and then click "Request". Then select the required client from the list.
-   Name — first name of the account owner.
-   Last Name — second name of the account owner.
-   Middle Name — middle name of the account owner.
-   Company — name of the client's company.
-   E-Mail — e-mail address.
-   Phone — phone number.
-   Country — country of residence.
-   State — state (region) of residence.
-   City — city of residence.
-   Zip code — postal code.
-   Address — exact address.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Additional account settings can be specified when <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit" class="topiclink">editing</a> it.</span></p></td></tr></tbody></table>

## Passwords

In this box the account passwords are specified. At the creation of account the passwords are generated automatically, however they can be manually specified in the corresponding fields:

-   Master — master password of the account.
-   Investor — investor password (without ability to trade).
-   Phone — phone password that is intended for the identification of the account owner when performing trade operations by phone.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">All passwords, including master and investor, must contain four character types: lowercase letters, uppercase letters, numbers and <a href="https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters" target="_blank" class="weblink">symbols</a> (#, @, !, etc.). For example, 1Ar#pqkj. The minimum password length is determined by <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#minimum_password" class="topiclink">group settings</a>, while the lowest possible value is 8 characters. The maximum length is 16 characters.</span></p></td></tr></tbody></table>

In order to create the account, press the OK button. To cancel the creation press the Cancel button.

[Accounts](/en/docs/mt5/platform/administration/admin_accounts)

[Editing Account](/en/docs/mt5/platform/administration/admin_accounts/account_edit)