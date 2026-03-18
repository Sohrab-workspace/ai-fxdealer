# Operation of WebServices API

> Source: https://support.metaquotes.net/en/docs/mt4/api/webservices_api/web_api_dev

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
    -   [API](/en/docs/mt4/api)
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
            -   [Operation Principles](/en/docs/mt4/api/webservices_api/web_api_dev)
            -   [Example: Quotes on a Website](/en/docs/mt4/api/webservices_api/web_api_example)
            -   [Commands](/en/docs/mt4/api/webservices_api/web_api_command)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[WebServices API](/en/docs/mt4/api/webservices_api)Operation Principles

# Operation of WebServices API

Interaction with a trade server is performed over a TCP connection, using text commands.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The IP address of the Web server, from which web commands will be sent, must be registered in the list of allowed IP addresses for web services (option 'IP access list of web services' on the 'Common' tab in MetaTrader Administrator settings).</span></p></td></tr></tbody></table>

## Caching Server Operation Results

When using the Web Services API, all references to the MetaTrader server are implemented from the IP address that hosts your website. If the number of connections is too large, the MetaTrader server will accept the request activity as a DoS attack, and will block incoming requests from the web server.

In order to solve this problem, it is recommended to use caching of results received from the server. Add the code for saving request results to the program block responsible for accessing the server. In order to cache the request, it is necessary to calculate the hash code of the request string (e.g., using PHP functions crc32 or md5) and to save the result to a file containing the name of the computed hash code. During the next request, it is necessary to check if there is a file whose name contains the hash code of the request string, and to check its relevance. If the file cache is relevant, its contents should be displayed instead of connecting to a server.

## Session Start

In order to start operation, it is necessary to create a TCP connection to a server (e.g. IP address: 192.168.0.1; port: 443).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">PHP is used in all examples.</span></li><li class="p_tableatten"><span class="f_tableatten">All open TCP connections must always be closed after use.</span></li></ul></td></tr></tbody></table>

Example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">=fsockopen(</span><span class="f_CodeExample" style="color: #008000;">'192.168.0.1'</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008000;">443</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample" style="color: #808080;">//&nbsp;Checking&nbsp;errors</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">&nbsp;(!</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">){</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">echo</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">"Connection&nbsp;error"</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">exit</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

## Sending the web service use flag to the server.

After establishing the TCP connection, pass the web service use flag to the server — the symbol 'W'. In case of connection through a data cetner, pass 'Z' instead of 'W'.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">fputs(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008000;">'W'</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

## Passing commands of WebService API to the server

Each command transmitted to the server must end with a newline character, in PHP it is a combination of symbols "\\n".

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">fputs(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008000;">"WAPQUOTES-EURUSD,USDCHF,GBPUSD\n"</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

The web service operation flag and the first command can be combined into one line:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//&nbsp;The&nbsp;beginning&nbsp;of&nbsp;operation&nbsp;flag&nbsp;and&nbsp;the&nbsp;first&nbsp;command&nbsp;in&nbsp;a&nbsp;single&nbsp;line</span><br><span class="f_CodeExample">fputs(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008000;">"WWAPQUOTES-EURUSD,USDCHF,GBPUSD\n"</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

## Reading and Processing Server Responses

After sending a command to the server, it is necessary to read the response from the server and to process the result. A sign that the server has finished sending results is the string "end\\r\\n".

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">while</span><span class="f_CodeExample">(!feof(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">))</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;Reading&nbsp;the&nbsp;string&nbsp;of&nbsp;symbols</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #800080;">$line</span><span class="f_CodeExample">=fgets(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008000;">128</span><span class="f_CodeExample">);&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;End&nbsp;of&nbsp;result&nbsp;transmission&nbsp;flag</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #800080;">$line</span><span class="f_CodeExample">==</span><span class="f_CodeExample" style="color: #008000;">"end\r\n"</span><span class="f_CodeExample">)&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">break</span><span class="f_CodeExample">;&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;Processing</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">print</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #800080;">$line</span><span class="f_CodeExample">;&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #800080;">$buf</span><span class="f_CodeExample">&nbsp;.=&nbsp;</span><span class="f_CodeExample" style="color: #800080;">$line</span><span class="f_CodeExample">;&nbsp;</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span></p></td></tr></tbody></table>

## Session Completion

To complete operation with the server, send the 'QUIT' command and close the TCP connection.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">fputs(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008000;">"QUIT\n"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">fclose(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

If you are using scripting languages ​​such as PHP, ASP and other, it is advisable to include the symbol of the beginning, the API command, and the operation completion command to a string sent to the server.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//&nbsp;Beginning,&nbsp;API&nbsp;command&nbsp;and&nbsp;operation&nbsp;completion&nbsp;in&nbsp;the&nbsp;same&nbsp;line</span><br><span class="f_CodeExample">fputs(</span><span class="f_CodeExample" style="color: #800080;">$ptr</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008000;">"WWAPQUOTES-EURUSD,USDCHF,GBPUSD\nQUIT\n"</span><span class="f_CodeExample">);</span></p></td></tr></tbody></table>

[WebServices API](/en/docs/mt4/api/webservices_api)

[Example: Quotes on a Website](/en/docs/mt4/api/webservices_api/web_api_example)