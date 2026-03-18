# IMTAttachment

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_client/imtattachment

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
                -   [IMTClient](/en/docs/mt5/api/reference_client/imtclient)
                -   [IMTClientArray](/en/docs/mt5/api/reference_client/imtclientarray)
                -   [IMTClientSink](/en/docs/mt5/api/reference_client/imtclientsink)
                -   [IMTComment](/en/docs/mt5/api/reference_client/imtcomment)
                -   [IMTCommentArray](/en/docs/mt5/api/reference_client/imtcommentarray)
                -   [IMTCommentSink](/en/docs/mt5/api/reference_client/imtcommentsink)
                -   [IMTDocument](/en/docs/mt5/api/reference_client/imtdocument)
                -   [IMTDocumentArray](/en/docs/mt5/api/reference_client/imtdocumentarray)
                -   [IMTDocumentSink](/en/docs/mt5/api/reference_client/imtdocumentsink)
                -   [IMTAttachment](/en/docs/mt5/api/reference_client/imtattachment)
                    -   [Enumerations](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_enum)
                    -   [Release](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_release)
                    -   [Assign](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_assign)
                    -   [Clear](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_clear)
                    -   [RecordID](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_recordid)
                    -   [RelatedClient](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_relatedclient)
                    -   [FileType](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filetype)
                    -   [FileName](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filename)
                    -   [FileContent](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filecontent)
                    -   [FileSize](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filesize)
                    -   [FileFlags](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_fileflags)
                -   [IMTAttachmentArray](/en/docs/mt5/api/reference_client/imtattachmentarray)
            -   [Users](/en/docs/mt5/api/reference_user)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Clients](/en/docs/mt5/api/reference_client)IMTAttachment

# IMTAttachment

The IMTAttachment class is designed for working with [document](/en/docs/mt5/api/reference_client/imtdocument) files and [attachments in comments](/en/docs/mt5/api/reference_client/imtcomment). The interface contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_release" class="topiclink">Release</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the current object.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_assign" class="topiclink">Assign</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a passed object to the current one.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_clear" class="topiclink">Clear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear an object.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_recordid" class="topiclink">RecordID</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the attachment identifier.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_relatedclient" class="topiclink">RelatedClient</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the client ID with which the attachment is associated.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filetype" class="topiclink">FileType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the file type.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filename" class="topiclink">FileName</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the file name.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filecontent" class="topiclink">FileContent</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the attached file contents.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_filesize" class="topiclink">FileSize</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the attached file size.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_fileflags" class="topiclink">FileFlags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set file flags.</span></p></td></tr></tbody></table>

The IMTAttachment class contains the following enumerations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Enumeration</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_enum#enfiletype" class="topiclink">EnFileType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">File types.</span></p></td></tr><tr class="table"><td class="table" style="width:135px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_client/imtattachment/imtattachment_enum#enfileflags" class="topiclink">EnFileFlags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">File flags.</span></p></td></tr></tbody></table>

[OnDocumentDelete](/en/docs/mt5/api/reference_client/imtdocumentsink/imtdocumentsink_ondocumentdelete)

[Enumerations](/en/docs/mt5/api/reference_client/imtattachment/imtattachment_enum)