# Constants

> Source: https://support.metaquotes.net/en/docs/mt5/api/smtmath/smtmath_constants

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
            -   [SMTMath](/en/docs/mt5/api/smtmath)
                -   [Constants](/en/docs/mt5/api/smtmath/smtmath_constants)
                -   [Price Functions](/en/docs/mt5/api/smtmath/smtmath_price)
                -   [Volume Functions](/en/docs/mt5/api/smtmath/smtmath_volume)
                -   [Functions of Monetary Units](/en/docs/mt5/api/smtmath/smtmath_money)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[SMTMath](/en/docs/mt5/api/smtmath)Constants

# Constants

The MetaTrader 5 API providers a number of volume and price constants:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:167px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:167px;"><p class="p_fortable"><span class="f_fortable">MTAPI_VOLUME_DIV</span></p></td><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">10000.0</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A factor for converting the volume.</span></p></td></tr><tr class="table"><td class="table" style="width:167px;"><p class="p_fortable"><span class="f_fortable">MTAPI_VOLUME_DIGITS</span></p></td><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">4</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Precision of the volume value.</span></p></td></tr><tr class="table"><td class="table" style="width:167px;"><p class="p_fortable"><span class="f_fortable">MTAPI_VOLUME_MAX</span></p></td><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">(UINT64)10000000000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The maximum possible value of the volume.</span></p></td></tr><tr class="table"><td class="table" style="width:167px;"><p class="p_fortable"><span class="f_fortable">MTAPI_PRICE_MAX</span></p></td><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">100000000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The maximum possible value of the price.</span></p></td></tr><tr class="table"><td class="table" style="width:167px;"><p class="p_fortable"><span class="f_fortable">MTAPI_PRICE_DIGITS_MAX</span></p></td><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">8</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The maximum number of digits after the decimal point in the price.</span></p></td></tr></tbody></table>

[SMTMath](/en/docs/mt5/api/smtmath)

[Price Functions](/en/docs/mt5/api/smtmath/smtmath_price)