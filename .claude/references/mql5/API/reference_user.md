# Users

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_user

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
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
            -   [Trade](/en/docs/mt5/api/reference_trading)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
                -   [IMTUser](/en/docs/mt5/api/reference_user/imtuser)
                -   [IMTUserArray](/en/docs/mt5/api/reference_user/imtuserarray)
                -   [IMTUserSink](/en/docs/mt5/api/reference_user/imtusersink)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)Users

# Users

The MetaTrader 5 API allows managing a client base on a trade server. Using the API, you can add or remove users, edit their data and handle events of changes in the client base.

An important feature of a client base is that users are bound to a certain trade server. Accordingly, an application can manage only those user accounts that belong to the same server, on which the manager account used for connection has been created.

The following user interfaces are available:

-   [IMTUser](/en/docs/mt5/api/reference_user/imtuser)  
    An interface that provides access to all the main user settings.
-   [IMTUserArray](/en/docs/mt5/api/reference_user/imtuserarray)  
    An interface for working with the arrays of users.
-   [IMTUserSink](/en/docs/mt5/api/reference_user/imtusersink)  
    An interface that contains handlers of events associated with changes in user settings.

To help you understand the purpose of interfaces intended for working with users, the below figure shows their compliance with the elements in MetaTrader 5 Administrator:

![Working with users in MetaTrader 5 Adminsitrator](/en/docs/mt5/api/img/users.png "Working with users in MetaTrader 5 Adminsitrator")

The following elements are shown above:

1.  [User login](/en/docs/mt5/api/reference_user/imtuser/imtuser_login).
2.  [Username](/en/docs/mt5/api/reference_user/imtuser/imtuser_name).
3.  [User group](/en/docs/mt5/api/reference_user/imtuser/imtuser_group).
4.  [City of residence of a user](/en/docs/mt5/api/reference_user/imtuser/imtuser_city).
5.  [Email address of a user](/en/docs/mt5/api/reference_user/imtuser/imtuser_email).
6.  [The current balance of a user](/en/docs/mt5/api/reference_user/imtuser/imtuser_balance).
7.  A tab of personal information, such as [Company](/en/docs/mt5/api/reference_user/imtuser/imtuser_company), [City](/en/docs/mt5/api/reference_user/imtuser/imtuser_city), [Phone number](/en/docs/mt5/api/reference_user/imtuser/imtuser_phone), [Address](/en/docs/mt5/api/reference_user/imtuser/imtuser_address) etc.
8.  A tab of security settings for [passwords](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userpasswordchange) and [certificates](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercertdelete).
9.  [The color of trade requests](/en/docs/mt5/api/reference_user/imtuser/imtuser_color) of a user in the manager terminal.
10.  [Leverage](/en/docs/mt5/api/reference_user/imtuser/imtuser_leverage).
11.  [User account in an external bank](/en/docs/mt5/api/reference_user/imtuser/imtuser_account).
12.  [Agent account](/en/docs/mt5/api/reference_user/imtuser/imtuser_agent).
13.  [User permissions](/en/docs/mt5/api/reference_user/imtuser/imtuser_rights).
14.  [Client's accounts in external systems](/en/docs/mt5/api/reference_user/imtuser/imtuser_externalaccountadd).

[SearchRight](/en/docs/mt5/api/reference_client/imtattachmentarray/imtattachmentarray_searchright)

[IMTUser](/en/docs/mt5/api/reference_user/imtuser)