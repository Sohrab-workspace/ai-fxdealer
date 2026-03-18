# Authentication

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_rest_authentication

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
            -   [Getting Started](/en/docs/mt5/api/webapi_preparing)
            -   [Format of Commands](/en/docs/mt5/api/webapi_https)
            -   [Authentication](/en/docs/mt5/api/webapi_rest_authentication)
            -   [Escaping Special Characters](/en/docs/mt5/api/webapi_screening)
            -   [Maintaining Connections](/en/docs/mt5/api/webapi_pings)
            -   [Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)
            -   [Examples](/en/docs/mt5/api/webapi_examples)
            -   [Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)Authentication

# Authentication

To send commands to the server, a client should pass authentication there. The two commands are used for that:

-   /api/auth/start — authentication start command.
-   /api/auth/answer — authentication request response command.

Authentication is performed in several stages, at which both the server and the client send these commands with various parameters.

-   [Request to Start Authentication](/en/docs/mt5/api/webapi_rest_authentication#client_start)
-   [Start of Authentication on the Access Server](/en/docs/mt5/api/webapi_rest_authentication#server_start)
-   [Response to the Server](/en/docs/mt5/api/webapi_rest_authentication#client_answer)
-   [End of Authentication](/en/docs/mt5/api/webapi_rest_authentication#server_answer)

Authentication examples for JavaScript and PHP are available in the [Examples](/en/docs/mt5/api/webapi_examples) section.

## Request to Start Authentication [#](webapi_rest_authentication#client_start)

A client should send a request to start authentication using the /api/auth/start command, for example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;https://server.address:443/api/auth/start?version=484&amp;agent=test&amp;login=14&amp;type=manager</span></p></td></tr></tbody></table>

The following parameters separated by the "&" character are passed in the command:

-   version — the version of the web client. Use this field to control you application versions. The specified version will be printed to the access server log when the web client connects to the platform. For example, '1000': login (Manager WebAPI build 3470). For convenience, you can specify the current platform build here. If you do not need version control, enter any number but not less than 484.
-   agent — an arbitrary name of the Web agent. The name should not be empty and should not contain spaces.
-   login — a login of an [account](/en/docs/mt5/api/webapi_preparing#account_create), under which authorization should be performed.
-   type — account type. Only one value is currently supported, which is 'manager'. This means connection using a [manager account](/en/docs/mt5/api/config_manager/imtconmanager). The account used fully determines connection permissions, including the [list of IP addresses](/en/docs/mt5/api/config_manager/imtconmanageraccess) allowed for connection.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">No more than 10 seconds should pass between the authentication start request (/api/auth/start) and sending of a response to the server (/api/auth/answer). Otherwise, authentication will fail.</span></p></td></tr></tbody></table>

## Start of Authentication on the Access Server [#](webapi_rest_authentication#server_start)

In response to the authentication start command, the access server sends the response containing a response code and a random sequence.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"version_access"&nbsp;:&nbsp;"1290",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"srv_rand"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;"d4e005317e38bc0c349a51a0d73a07eb"</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

The following parameters separated by the "|" character are passed in the command:

-   retcode — a response code and its string description. 0 means successful completion.
-   version\_access — version of the access server that is used for connection to the trade server;
-   srv\_rand — a random 16-byte sequence in the Hex format, generated by the server. A password should be applied to this sequence when sending a response.

## Response to the Server [#](webapi_rest_authentication#client_answer)

After receiving a random sequence, a client should apply a password (hash of the password) to it and send it to the server using the /api/auth/answer command:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;https://server.address:443/api/auth/answer?srv_rand_answer=8b67609a264764a528ec8c709ab71df2&amp;cli_rand=34b6bccab8bfebdf462d1312043df1cc</span></p></td></tr></tbody></table>

The following parameters separated by the "&" character are passed in the command:

-   srv\_rand\_answer — MD5 hash of the random sequence and the password hash.
-   cli\_rand — a random sequence for server authentication which you should generate yourself. The sequence should be in the Hex format with 16 byte size.

### Password Hash [#](webapi_rest_authentication#hash)

The hash of the password is calculated the following way:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">Password</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">hash=MD5(MD5('Password')+'WebAPI')</span></p></td></tr></tbody></table>

Six characters of the WebAPI are added to the MD5 hash of the password and once again an MD5 hash is obtained from the result. Then, when sending to the server, the obtained hash is once again combined with the random sequence of the server. Hash is taken from the resulting value, which is then sent to the server. This ensures the maximum security of authentication.

A Sample Forming of srv\_rand\_answer:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">password&nbsp;hash=MD5(MD5('Password1')+'WebAPI')=</span><span class="f_CodeExample" style="background-color: #b8cde5;">904ba8ecb16273d2f0ae9c3b8a023752</span><br><span class="f_CodeExample">srv_rand=</span><span class="f_CodeExample" style="background-color: #e6b9b8;">73007dc7184747ce0f7c98516ef1c851</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Calculation&nbsp;formula:&nbsp;srv_rand_answer=MD5(password&nbsp;hash+srv_rand)</span><br><span class="f_CodeExample">srv_rand_answer=MD5(</span><span class="f_CodeExample" style="background-color: #b8cde5;">904ba8ecb16273d2f0ae9c3b8a023752</span><span class="f_CodeExample">+</span><span class="f_CodeExample" style="background-color: #e6b9b8;">73007dc7184747ce0f7c98516ef1c851</span><span class="f_CodeExample">)=77fe51827f7fa69dd80fbec9aa33f1bb</span></p></td></tr></tbody></table>

A step by step example of how srv\_rand\_answer is formed:

Let's analyze Web password=Password1 and srv\_rand="73007dc7184747ce0f7c98516ef1c851".

1\. We calculate MD5 of the password in Unicode (UTF-16-LE). In this case, unicode string Password1:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MD5('Password1')</span></p></td></tr></tbody></table>

The result as bytes:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">[&nbsp;236,46,146,255,112,191,70,145,174,12,104,224,47,220,108,34&nbsp;]</span></p></td></tr></tbody></table>

2\. Add a one-byte WebAPI string as 6 bytes (UTF-8) to the byte result:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MD5('Password1')+'WebAPI'</span></p></td></tr></tbody></table>

'WebAPI' is represented as = \[ 87,101,98,65,80,73 \]. The result as bytes:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">[&nbsp;236,46,146,255,112,191,70,145,174,12,104,224,47,220,108,34,87,101,98,65,80,73&nbsp;]</span></p></td></tr></tbody></table>

3\. Get the final hash of the password as MD5 of the byte result from step 2:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MD5(MD5('Password1')+'WebAPI')</span></p></td></tr></tbody></table>

The result as bytes:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">[&nbsp;144,75,168,236,177,98,115,210,240,174,156,59,138,2,55,82&nbsp;]</span></p></td></tr></tbody></table>

The result as a HEX string:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">904ba8ecb16273d2f0ae9c3b8a023752</span></p></td></tr></tbody></table>

4\. Combine the byte hash of the password from step 3 and SRV\_RAND:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MD5(MD5('Password1')+'WebAPI')+&nbsp;[&nbsp;115,0,125,199,24,71,71,206,15,124,152,81,110,241,200,81&nbsp;]</span></p></td></tr></tbody></table>

where \[ 115,0,125,199,24,71,71,206,15,124,152,81,110,241,200,81 \] is the HEX string 73007dc7184747ce0f7c98516ef1c851 converted to a byte array:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">srv_rand&nbsp;=&nbsp;73007dc7184747ce0f7c98516ef1c851&nbsp;=&nbsp;[&nbsp;115,0,125,199,24,71,71,206,15,124,152,81,110,241,200,81&nbsp;]</span></p></td></tr></tbody></table>

The final result of the combination (two byte arrays are simply joined together):

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">[&nbsp;144,75,168,236,177,98,115,210,240,174,156,59,138,2,55,82,115,0,125,199,24,71,71,206,15,124,152,81,110,241,200,81&nbsp;]</span></p></td></tr></tbody></table>

5\. Form the final SRV\_RAND\_ANSWER for response to the server as MD5 of the byte result from step 4:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MD5(MD5(MD5('Password1')+'WebAPI')&nbsp;+&nbsp;[&nbsp;115,0,125,199,24,71,71,206,15,124,152,81,110,241,200,81&nbsp;]</span></p></td></tr></tbody></table>

The result as bytes:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">[&nbsp;119,254,81,130,127,127,166,157,216,15,190,201,170,51,241,187&nbsp;]</span></p></td></tr></tbody></table>

The result is converted to a HEX representation:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">77fe51827f7fa69dd80fbec9aa33f1bb</span></p></td></tr></tbody></table>

The final parameter in the response string is as follows:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">srv_rand_answer=77fe51827f7fa69dd80fbec9aa33f1bb</span></p></td></tr></tbody></table>

## End of Authentication [#](webapi_rest_authentication#server_answer)

After authenticating a client through a trade server, an access server sends a response:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"version_access"&nbsp;&nbsp;:&nbsp;"1290",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"version_trade"&nbsp;&nbsp;&nbsp;:&nbsp;"1290",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"cli_rand_answer"&nbsp;:&nbsp;"8b67609a264764a528ec8c709ab71df2"</span><br><span class="f_CodeExample">}</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">LLLLKKKKFAUTH_ANSWER|RETCODE=0&nbsp;Done|CLI_RAND_ANSWER=8b67609a264764a528ec8c709ab71df2|CRYPT_RAND=HEX_256_bytes\r\n</span></p></td></tr></tbody></table>

The following parameters separated by the "|" character are passed in the command:

-   retcode — a response code and its string description. 0 means successful completion.
-   version\_access — version of the access server that is used for connection to the trade server;
-   version\_trade — trade server version;
-   cli\_rand\_answer — MD5 hash of the random sequence and the password hash. The sequence is in the Hex format with the size of 16 bytes.

To authenticate a server on a client, the same algorithm as for client's authentication on the server is used. In the cli\_rand\_answer parameter, the server sends an MD5 hash of a client's random sequence and a password hash.

A Sample Forming of cli\_rand\_answer:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">password&nbsp;hash=MD5(MD5('Password1')+'WebAPI')=</span><span class="f_CodeExample" style="background-color: #b8cde5;">904ba8ecb16273d2f0ae9c3b8a023752</span><br><span class="f_CodeExample">cli_rand=</span><span class="f_CodeExample" style="background-color: #d7e4bc;">4db98fec17aab4dc5a240bdc659e8395</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Calculation&nbsp;formula:&nbsp;cli_rand_answer=MD5(password&nbsp;hash+CLI_RAND)</span><br><span class="f_CodeExample">cli_rand_answer=MD5(</span><span class="f_CodeExample" style="background-color: #b8cde5;">904ba8ecb16273d2f0ae9c3b8a023752</span><span class="f_CodeExample">+</span><span class="f_CodeExample" style="background-color: #d7e4bc;">4db98fec17aab4dc5a240bdc659e8395</span><span class="f_CodeExample">)=1732021b1b332f51660b2b315eed3a35</span></p></td></tr></tbody></table>

[Format of Commands](/en/docs/mt5/api/webapi_https)

[Escaping Special Characters](/en/docs/mt5/api/webapi_screening)