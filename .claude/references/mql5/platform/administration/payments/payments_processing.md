# Processing Payments

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/payments/payments_processing

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Payments](/en/docs/mt5/platform/administration/payments)Processing Payments

# Processing Payments

Using [payment processing rules](/en/docs/mt5/platform/administration/payments/payments_rules#action), you can flexibly configure the system and process some transactions in a fully automatic mode, while requiring manual confirmation by the manager for others. This provides additional operation security. For example, you can require manual control for suspiciously large withdrawal operations. All bank transfers are always processed manually.

Manual payment processing is implemented through the Manager terminal. Open the Payments \\ Processing section. The bottom part displays a list of all payments pending processing.

![Processing payments in the Manager terminal](/en/docs/mt5/platform/img/payments_process_lock.png "Processing payments in the Manager terminal")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To process payments, the manager should have the "Access payments" and "Process payments" <a href="/en/docs/mt5/platform/administration/admin_managers#payments" class="topiclink">permissions</a>. The manager can receive for processing only payments made by account from <a href="/en/docs/mt5/platform/administration/admin_managers#groups" class="topiclink">groups available to the manager</a>.</span></p></td></tr></tbody></table>

Select the desired payment, and then click "Lock" at the top. The captured payment is removed from the queue, and no other manager can process it at the same time. After checking the payment details, you can approve or reject it. If you do not want to process the payment, press "Unlock", and it will be returned to the queue.

![After checking the payment details, accept or reject it](/en/docs/mt5/platform/img/payments_process_action.png "After checking the payment details, accept or reject it")

Further actions depend on the payment type and the system through which it is performed.

### Payments by Cards and e-Wallets

Depending on the type, such transactions are sent to manual verification at different stages:

-   Deposits are forwarded for manual confirmation after they have been successfully completed in the payment system. If the manager confirms the transaction, the amount will immediately be credited to the user's trading account as a separate balance transaction. If the manager rejects the transaction, the amount will not be credited to the account. Further actions related to returning the funds to the client depend on the payment provider. For further details please read "[Refunds](/en/docs/mt5/platform/administration/payments/payments_processing#refund)".
-   Withdrawals require manual confirmation before being sent to the payment system. The amount is immediately debited from the user's account using a balance operation. If the manager confirms the operation, a request to transfer funds will be sent to the payment system. If the manager rejects the transaction, the user will receive a refusal and the money will be credited back to the trading account as a separate balance operation.

### Bank Transfer

This type is always processed manually, without external payment systems. When you receive a request for a deposit or withdrawal via bank transfer, you should pass the relevant information to the company's accountant. Click on the row of a locked operation to open its details:

![Pass the bank transfer information to the accountant](/en/docs/mt5/platform/img/payments_process_bank_transfer.png "Pass the bank transfer information to the accountant")

In the case of a deposit, the accountant must check your bank account and verify that the transfer has been completed. After that, the manager can confirm the operation. Next, the system will credit the funds to the trading account as a separate balance operation.

In case of withdrawal, funds are first debited from the trading account by a balance transaction. Next, the accountant must perform the transfer using the specified details. The manager can then confirm the operation.

Additional information is available in the [Bank Transfer](/en/docs/mt5/platform/administration/payments/payments_wallets/payments_bank_transfer) section.

## Refunds [#](payments_processing#refund)

Funds deposited by clients into their accounts can be returned according to two main scenarios.

### Rejection during initial processing by manager

The initial processing occurs when the client replenishes the account, and the transaction is forwarded to the manager for manual confirmation. The manager may reject this transaction for some reason, for example, in accordance with the company's AML policy.

Deposits are forwarded for manual confirmation after they have been successfully completed in the payment system. Therefore, after rejection on the MetaTrader 5 side, the funds must be returned to the client back to the used payment method: card, wallet, etc. If the provider company through which the deposit transaction was made supports automatic refunds, then after the transaction is rejected, the platform will automatically send a corresponding request to the provider. In this case, no additional actions are required from the manager.

If the provider does not support automatic refunds, the funds will need to be returned manually. If you try to reject such a transaction, the system will display the following warning:

![Manual refund warning](/en/docs/mt5/platform/img/refund_warning.png "Manual refund warning")

When you reject the payment, it will be set to the "Rejected without refund" [state](/en/docs/mt5/platform/administration/payments/payments_operations#common). After that, go to your account/dashboard on the payment provider's portal and cancel the corresponding deposit transaction. After this, on the MetaTrader 5 side, you should manually change the payment status to "Rejected".

![After canceling the transaction with the provider, change the payment status on the platform side](/en/docs/mt5/platform/img/refund_state_change.png "After canceling the transaction with the provider, change the payment status on the platform side")

### Canceling a completed payment

If the payment has already been accepted and credited to the client's trading account, the refund procedure is slightly different:

-   Write off the corresponding amount from the trading account balance using the Manager terminal
-   Go to your account/dashboard at the payment provider through which the top-up was made and create a refund for the corresponding transaction. In this case, no automatic returns are possible; the procedure must be performed manually.
-   Open the corresponding payment on the MetaTrader 5 side and change its status to "Rejected" or "Canceled". The reason for cancellation can be additionally specified in the "Description" field.

[Controlling Payments](/en/docs/mt5/platform/administration/payments/payments_operations)

[Payments in Client Terminals](/en/docs/mt5/platform/administration/payments/payments_clients)