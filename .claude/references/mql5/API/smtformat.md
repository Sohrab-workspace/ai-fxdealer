# SMTFormat

> Source: https://support.metaquotes.net/en/docs/mt5/api/smtformat

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
        -   [Tools](/en/docs/mt5/api/reference_tools)
            -   [SMTFormat](/en/docs/mt5/api/smtformat)
                -   [Enumerations](/en/docs/mt5/api/smtformat/smtformat_enum)
                -   [FormatError](/en/docs/mt5/api/smtformat/smtformat_formaterror)
                -   [FormatDouble](/en/docs/mt5/api/smtformat/smtformat_formatdouble)
                -   [FormatMoney](/en/docs/mt5/api/smtformat/smtformat_formatmoney)
                -   [FormatPrice](/en/docs/mt5/api/smtformat/smtformat_formatprice)
                -   [FormatPrices](/en/docs/mt5/api/smtformat/smtformat_formatprices)
                -   [FormatVolume](/en/docs/mt5/api/smtformat/smtformat_formatvolume)
                -   [FormatVolumeDouble](/en/docs/mt5/api/smtformat/smtformat_formatvolumedouble)
                -   [FormatVolumeExt](/en/docs/mt5/api/smtformat/smtformat_formatvolumeext)
                -   [FormatSize](/en/docs/mt5/api/smtformat/smtformat_formatsize)
                -   [FormatVolumeOrder](/en/docs/mt5/api/smtformat/smtformat_formatvolumeorder)
                -   [FormatVolumeExtOrder](/en/docs/mt5/api/smtformat/smtformat_formatvolumeextorder)
                -   [FormatSizeOrder](/en/docs/mt5/api/smtformat/smtformat_formatsizeorder)
                -   [FormatDateTime](/en/docs/mt5/api/smtformat/smtformat_formatdatetime)
                -   [FormatDateTimeMsc](/en/docs/mt5/api/smtformat/smtformat_formatdatetimemsc)
                -   [FormatTime](/en/docs/mt5/api/smtformat/smtformat_formattime)
                -   [FormatTimeMsc](/en/docs/mt5/api/smtformat/smtformat_formattimemsc)
                -   [FormatIP](/en/docs/mt5/api/smtformat/smtformat_formatip)
                -   [FormatPositionType](/en/docs/mt5/api/smtformat/smtformat_formatpositiontype)
                -   [FormatOrderType](/en/docs/mt5/api/smtformat/smtformat_formatordertype)
                -   [FormatOrderStatus](/en/docs/mt5/api/smtformat/smtformat_formatorderstatus)
                -   [FormatOrderTypeFilling](/en/docs/mt5/api/smtformat/smtformat_formatordertypefilling)
                -   [FormatOrderTypeTime](/en/docs/mt5/api/smtformat/smtformat_formatordertypetime)
                -   [FormatOrderTypeReason](/en/docs/mt5/api/smtformat/smtformat_formatordertypereason)
                -   [FormatOrderPrice](/en/docs/mt5/api/smtformat/smtformat_formatorderprice)
                -   [FormatDealAction](/en/docs/mt5/api/smtformat/smtformat_formatdealaction)
                -   [FormatDealEntry](/en/docs/mt5/api/smtformat/smtformat_formatdealentry)
            -   [SMTMath](/en/docs/mt5/api/smtmath)
            -   [SMTSearch](/en/docs/mt5/api/smtsearch)
            -   [CMTArrayBase](/en/docs/mt5/api/cmtarraybase)
            -   [CMTStr](/en/docs/mt5/api/cmtstr)
            -   [CMTSync](/en/docs/mt5/api/cmtsync)
            -   [CMTThread](/en/docs/mt5/api/cmtthread)
            -   [SMTTime](/en/docs/mt5/api/smttime)
            -   [CMTFile](/en/docs/mt5/api/cmtfile)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)SMTFormat

# SMTFormat

This class is used for formatting strings. It contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formaterror" class="topiclink">FormatError</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Converts an error code used in the MetaTrader 5 platform into a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatdouble" class="topiclink">FormatDouble</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats a number with a given number of decimal places to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatmoney" class="topiclink">FormatMoney</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats a number with a given number of decimal places to a string. It is used to show sums of money with thousands separated.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatprice" class="topiclink">FormatPrice</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats a number into a string. Basic and additional accuracy are separately set for a number. As a rule, is used to format the position price.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatprices" class="topiclink">FormatPrices</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats values of Bid, Ask and Last from a passed structure MTTickShort to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatvolume" class="topiclink">FormatVolume</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats volume to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatvolumedouble" class="topiclink">FormatVolumeDouble</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats order volume (double) to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatvolumeext" class="topiclink">FormatVolumeExt</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats extended accuracy volume to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatsize" class="topiclink">FormatSize</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats size in units to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatvolumeorder" class="topiclink">FormatVolumeOrder</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats order volume to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatvolumeextorder" class="topiclink">FormatVolumeExtOrder</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats order volume specified with extended accuracy to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatsizeorder" class="topiclink">FormatSizeOrder</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats order size in units to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatdatetime" class="topiclink">FormatDateTime</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats date and time to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatdatetimemsc" class="topiclink">FormatDateTimeMsc</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats date and time into a string with an indication of milliseconds.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formattime" class="topiclink">FormatTime</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats time into a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formattimemsc" class="topiclink">FormatTimeMsc</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats time into a string with an indication of milliseconds.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatip" class="topiclink">FormatIP</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats an IP address and a port to a string.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatpositiontype" class="topiclink">FormatPositionType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats the type of a position in a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatordertype" class="topiclink">FormatOrderType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats the type of an order in a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatorderstatus" class="topiclink">FormatOrderStatus</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats the state of an order in a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatordertypefilling" class="topiclink">FormatOrderTypeFilling</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats order filling type in a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatordertypetime" class="topiclink">FormatOrderTypeTime</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats order expiration type in a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatordertypereason" class="topiclink">FormatOrderTypeReason</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats the order placing reason in a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatorderprice" class="topiclink">FormatOrderPrice</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats the order price and its triggering price (if any) in a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatdealaction" class="topiclink">FormatDealAction</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats the type of action performed by a deal to a string with a text description.</span></p></td></tr><tr class="table"><td class="table" style="width:158px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_formatdealentry" class="topiclink">FormatDealEntry</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Formats the type of action performed by a deal relative to a position, to a string with a text description.</span></p></td></tr></tbody></table>

The SMTFormat class contains one enumeration:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/smtformat/smtformat_enum#constants" class="topiclink">constants</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Description of constants used.</span></p></td></tr></tbody></table>

[Tools](/en/docs/mt5/api/reference_tools)

[Enumerations](/en/docs/mt5/api/smtformat/smtformat_enum)