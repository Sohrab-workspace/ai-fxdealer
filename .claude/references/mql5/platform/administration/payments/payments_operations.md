# Controlling Payments

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/payments/payments_operations

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
            -   [Payments](/en/docs/mt5/platform/administration/payments)
                -   [Payment Gateways](/en/docs/mt5/platform/administration/payments/payments_wallets)
                -   [Payment Processing Rules](/en/docs/mt5/platform/administration/payments/payments_rules)
                -   [Controlling Payments](/en/docs/mt5/platform/administration/payments/payments_operations)
                -   [Processing Payments](/en/docs/mt5/platform/administration/payments/payments_processing)
                -   [Payments in Client Terminals](/en/docs/mt5/platform/administration/payments/payments_clients)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Payments](/en/docs/mt5/platform/administration/payments)Controlling Payments

# Controlling Payments

Service usage can be monitored using the Active and History sections. The sections feature the transactions that are currently being [processed by managers](/en/docs/mt5/platform/administration/payments/payments_processing), as well as the history of completed/rejected transactions.

![History of payments](/en/docs/mt5/platform/img/payments_operations.png "History of payments")

To view transactions, request them from the server. Specify the filter to the right of the icon ![Find](/en/docs/mt5/platform/img/find_button.png "Find"):

-   By accounts — specify one or several account numbers separated by commas.
-   By trader group — select a group from the list or specify the group name manually.
-   By login — specify one or several accounts separated by commas.
-   By wallet — filter records by [wallet](/en/docs/mt5/platform/administration/payments/payments_wallets).

For the payment history additional options are available:

-   By date — select a predefined period using the ![Period ](/en/docs/mt5/platform/img/calendar.png "Period ") button or specify the dates manually.

Specify the desired filters and press "Request". Select an operation in the list to view its details.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Access to viewing and managing payments is subject to separate <a href="/en/docs/mt5/platform/administration/admin_managers#payments" class="topiclink">manager account</a> permissions.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">For additional payment control, use <a href="/en/docs/mt5/platform/administration/automation/automation_trigger#payments" class="topiclink">special automation triggers</a>. You can use them to set up notifications about any transactions and export data to external systems.</span></li></ul></td></tr></tbody></table>

## General Payment Details [#](payments_operations#common)

![Payment in processing](/en/docs/mt5/platform/img/payments_operation_common.png "Payment in processing")

The following information is shown for each payment:

-   Status — payments can have one of the following statuses:
    -   Initial — payment created on the server. Only used for internal purposes.
    -   Processing — the operation is being processed by the payment provider.
    -   Waiting — the operation is pending to be processed by the manager.
    -   Locked — the operation is [captured by the manager](/en/docs/mt5/platform/administration/payments/payments_processing) for further processing.
    -   Done — the payment was successfully completed.
    -   Rejected — the operation was rejected by the manager.

-   -   Rejected without refund — used when rejecting payments made through wallets that do not support automatic refunds. For further details please read "[Refunds](/en/docs/mt5/platform/administration/payments/payments_processing#refund)".

-   -   Canceled — the transaction was rejected by the payment provider.
    -   Failed — an error occurred while processing the payment.
-   Created — the date of the transaction in the client terminal.
-   Trading account — login of the account on which the operation is performed.
-   Amount — the operation amount requested by the client. Specified in the deposit currency.
-   Commission — commission charged by the broker in accordance with the [settings](/en/docs/mt5/platform/administration/payments/payments_wallets#commissions).
-   Deal — ticket of the [balance operation](/en/docs/mt5/platform/administration/admin_deals) via which funds are credited to or debited from the trading account.
-   Wallet — the name of the [wallet](/en/docs/mt5/platform/administration/payments/payments_wallets) via which the operation is performed.
-   Amount — the amount of the transaction on the side of the payment provider. It is specified in the currency selected by the user on the client terminal side when making the operation.
-   Commission — the payment provider's commission for the operation.
-   Conversion Rate — the rate of conversion from the client's currency to the payment system currency (or vice versa).
-   Transaction — transaction ID assigned by the payment system.
-   Transaction Status — transaction status transmitted by the payment system.
-   Manager — the login and name of the manager who [processed the operation](/en/docs/mt5/platform/administration/payments/payments_processing). It is filled only for manually processed transactions.
-   Description — additional information about the operation. Can be filled in by payment systems or manually by managers.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Changing the payment status manually does not trigger any processing events. If "Canceled" is set for a successful top-up, the amount is not debited from the account. This should be done manually. If "Rejected" is set for a withdrawal operation being processed, the previously blocked amount is not released. To do this, the payment should be rejected via the <a href="/en/docs/mt5/platform/administration/payments/payments_processing" class="topiclink">manager terminal</a>.</span></p></td></tr></tbody></table>

## Details [#](payments_operations#details)

Information in this section depends on the payment method: card, e-wallet, or bank transfer. The details depend on the payment system.

-   For cards, these include card number, expiration date and owner's name
-   For wallets, wallet number or ID is shown
-   Bank transfers provide account details: bank name, division and code, account number, client name, etc.

![Payment details](/en/docs/mt5/platform/img/payments_operation_details.png "Payment details")

## History [#](payments_operations#history)

For efficient employee performance monitoring and secure storage of information, all changes in payment transactions are tracked and displayed in the Versions section. Version support allows you to see all changes made to the transaction. You can revert changes if necessary, since all earlier specified data are stored in the platform.

![History of actions from payment transactions](/en/docs/mt5/platform/img/payments_operation_history.png "History of actions from payment transactions")

Information on each change contains the number and date of the change as well as the relevant manager's login. To view more detailed information about the changes, click on the row. The details show each changed parameter: its name, previous value and new value.

## Payment Accounts [#](payments_operations#accounts)

At the moment, payment accounts are used only for transactions with bank cards. They store card details. Payment accounts are created when a user [adds a new card](/en/docs/mt5/platform/administration/payments/payments_operations#add_card) or makes a deposit from a new card (the card is also added in this case).

To view the payment account details, go to the Payments \\ Accounts section and query the records. Select a record to view its details:

![Payment Accounts](/en/docs/mt5/platform/img/payments_account.png "Payment Accounts")

The following details are provided for payment accounts:

-   ID — unique account ID within the MetaTrader 5 platform.
-   Trading Account — details of the trading account for which the account is saved: holder's name, account number, group, leverage.
-   Gateway — payment provider.
-   Type — type of payment method: card, PayPal, WebMoney, etc.
-   External ID — unique ID used by the payment system to identify the account.

-   Currency — currency with which the payment method operates. This field is required for some providers who link cards to a specific currency. If no currency is specified, the payment instrument can use any currency for transactions.

-   Card token — unique ID used by the payment system to identify the card. Unlike the external ID, the token for the same card can change.
-   Card Number — masked card number. The system does not store full card numbers.
-   Card Expiration — card expiration date.
-   Cardholder Name — the name of the card holder.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The payment system does not store full card details (number and CVV) due to legal restrictions. This would require an organization to hold a special license. Instead, the system stores a unique token, by which the external system can identify the card.</span></p></td></tr></tbody></table>

### Adding Cards [#](payments_operations#add_card)

Due to specific requirements of some payment providers, the system needs to know in advance which card will be used to withdraw funds. If the user has not previously added cards and has not deposited funds (cards are added automatically during deposits), then when withdrawing funds in the client terminal, the user must first add the card:

![Adding a card](/en/docs/mt5/platform/img/payments_add_card.png "Adding a card")

Upon pressing Add, the user is forwarded to the payment system page and specifies card details. The system performs a special operation of 1 USD to authorize the card. This amount is locked on the card and then immediately unlocked, so nothing is debited from the user. After that, a payment account is created in the platform, which stores a special token — a unique identifier by which the payment system can identify the card.

After that, the user returns to the payment page, selects a card and performs the transaction.

![Added card is available](/en/docs/mt5/platform/img/payments_added_card.png "Added card is available")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">During deposit operations, the used cards are added to the system automatically. It is not necessary to add cards separately. The user can enter the amount and click Continue.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If <a href="/en/docs/mt5/platform/administration/payments/payments_wallets#permissions" class="topiclink">creation of accounts is disabled</a> in the payment gateway settings, the option for adding new cards will disappear from the terminal. It will only be possible to add a new card by making a deposit.</span></li></ul></td></tr></tbody></table>

## Payments in Accounts [#](payments_operations#account_payments)

[Account properties](/en/docs/mt5/platform/administration/admin_accounts/account_edit) store all related transactions and payment accounts. Select a transaction in the list to view the details.

![Transactions and payment accounts associated with the account](/en/docs/mt5/platform/img/payments_operations_account.png "Transactions and payment accounts associated with the account")

[Payment Processing Rules](/en/docs/mt5/platform/administration/payments/payments_rules)

[Processing Payments](/en/docs/mt5/platform/administration/payments/payments_processing)