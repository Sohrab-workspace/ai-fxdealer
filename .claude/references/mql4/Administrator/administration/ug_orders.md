# Orders

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_orders

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
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
                -   [Order Deleting and Restore](/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore)
                -   [Order Database Optimization](/en/docs/mt4/administrator/administration/ug_orders/order_base_optimization)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Orders

# Orders

You can request information about all trade operations of any accounts in the "Orders" section. Parameters are set in the "Group" and "Database" fields, the "Open only" check box allows to request only open orders. The "Request" button or the corresponding context menu command allows to proceed the request.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The "Open only" option works only when requesting orders by login or group. When requesting a specific order it is not considered.</span></p></td></tr></tbody></table>

To search a necessary entry according a certain criterion among the results of the request from the database, you should use the "Find" window. Activation of this window can be performed with "Ctrl+F" buttons.

![Orders](/en/docs/mt4/administrator/img/br_orders.png "Orders")

Information about the time of closing a position, agent's commission, and the futures contract expiring dates is located in this window. The "Order" window also allows to change information about trade operations. The "Delete" button and the corresponding context menu command will delete the selected orders.The execution of the "Delete Orders" command is not sufficient to delete orders. After that, it is necessary to execute "Check balance" and "Fix balance" commands in the group operations window in the ["Accounts"](/en/docs/mt4/administrator/administration/ug_accounts) section. You can find more details in the [Order Removing and Restore](/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore) section.

On the "Edit order..." context menu command, the detailed information window will appear:

![Order Administration](/en/docs/mt4/administrator/img/win_orders_detail.png "Order Administration")

-   Order — order number;
-   Login — account login;
-   Reason — a reason of placing the order:

-   Client — the order is placed manually by a client via the client terminal;
-   Expert — the order is placed by a client using an Expert Advisor;
-   Dealer — the order is placed by a dealer via the manager terminal;
-   Signal — the order is placed as a result of copying a [trade signal](https://www.mql5.com/en/signals) according to a subscription in the client terminal;

-   Gateway — the order is placed via the [STP gateway](/en/docs/mt4/administrator/administration/gateway).

-   Mobile — the order is placed via MetaTrader 4 for IPhone or Android.
-   Web — the order is placed via WebTerminal.
-   API — the order is placed via Server API or Manager API.

-   Type — type of operation (buy, sell, sell limit, buy limit, buy stop, sell stop, balance, credit);
-   Lots — the volume of the lot of a position;
-   Symbol — financial instrument;
-   Open time — time of opening a position;
-   Close time — time of closing a position;
-   Open price — opening price of a position;
-   Close price — closing price of a position;
-   S / L — the level of the Stop Loss order indicated;
-   T / P — the level of the Take Profit order indicated;
-   1st conv. rate — the base currency rate of the instrument against the deposit currency by the moment of opening a position. The algorithm of conversion is the same as the one used for [margin calculation](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation#conversion);
-   2nd conv. rate — the base currency rate of the instrument against the deposit currency by the moment of closing a position. The algorithm of conversion is the same as the one used for [margin calculation](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation#conversion);
-   Margin rate — the coefficient of conversion of the order margin currency into the deposit currency. The algorithm is described in the ["Margin calculation"](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation#conversion) section;
-   Swaps — swaps being accounted;
-   Commission — the amount of commission;
-   Agent Commission — the amount of agent commission;
-   Taxes — taxes for commission;
-   Comment — the text of the comment;
-   Profit — the trade operation profit;
-   Expiration date — the date of expiration of the order;
-   Magic — order identifier (Magic Number) set by a client's Expert Advisor.
-   Value date — the date of credit repayment;
-   Gateway order — order number (ticket) at an external MetaTrader 4 server when working through the [gateway](/en/docs/mt4/administrator/administration/gateway);

-   Gateway lots — the volume used when the order was passed to an external trade server via the gateway. [Coverage percentage](/en/docs/mt4/administrator/administration/gateway#coverage) is configured in the gateway rules;
-   Open price delta — difference between the order open price in the external system and the order open price on the local trade server. Specified in pips. The total open price on the gateway is obtained by adding the difference to the order open price on the local server;
-   Close price delta — difference between the order close price in the external system and the order close price on the local trade server. Specified in pips. The total close price on the gateway is obtained by adding the difference to the order close price on the local server.

The "Update" button saves modifications made in an order.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">When changing the account login of the order, it is necessary to make sure that the "Commission", "Swap", "Profit", "1st conv. rate", "2nd conv. rate" parameters are set correctly. In the other case, significant distortion of the client's trade account parameters can occur. For example, if the order belonged to a client having JPY as basic currency, and it was transferred to the client having USD as basic currency, false (too high) values of margin demands, commission, swaps, and profits are possible.</span></li><li class="p_tableatten"><span class="f_tableatten">After modifying an order, you should correct the account balance. To do it, execute the <a href="/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations" class="topiclink">"Group Operations..."</a> command in the context menu of the necessary account and run the "Fix Balance" procedure.</span></li></ul></td></tr></tbody></table>

## Reopening Orders

Orders in the trade history of a client can be reopened. To do it, go to the "Orders" section, open the order and then click "Reopen":

![Reopening an order](/en/docs/mt4/administrator/img/order_reopen.png "Reopening an order")

### Pending Orders

When reopening a pending order, check what price it has. The order should not trigger right after being reopened.

### Market Orders

When reopening, carefully check the Stop Loss and Take Profit levels of the order. In the current market situation, these levels may be already hit and thus the reopened order will be closed again on the next tick.

Also one should consider the margin state of the client after reopening the order. The client should not fall under stop out, as the server will force position closing.

After reopening a market order, fix the client's balance. Select the [client account](/en/docs/mt4/administrator/administration/ug_accounts) in the corresponding section and execute "Group operations" in the context menu. Click "Fix Balance" in the appeared window.

![Group operations](/en/docs/mt4/administrator/img/win_account_group.png "Group operations")

[Account Redirection](/en/docs/mt4/administrator/administration/ug_accounts/account_allocation_url)

[Order Deleting and Restore](/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore)