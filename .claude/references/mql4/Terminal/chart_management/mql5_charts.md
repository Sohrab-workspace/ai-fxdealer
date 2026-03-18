# Publishing Charts Online

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/chart_management/mql5_charts

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
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
            -   [Chart Opening](/en/docs/mt4/terminal/chart_management/charts_open)
            -   [Setup](/en/docs/mt4/terminal/chart_management/charts_setup)
            -   [Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)
            -   [Publishing Charts Online](/en/docs/mt4/terminal/chart_management/mql5_charts)
            -   [Quick Trading](/en/docs/mt4/terminal/chart_management/chart_trading)
            -   [Charts Print](/en/docs/mt4/terminal/chart_management/charts_print)
            -   [Deleted Charts](/en/docs/mt4/terminal/chart_management/charts_deleted)
            -   [Templates and Profiles](/en/docs/mt4/terminal/chart_management/templates)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Working with Charts](/en/docs/mt4/terminal/chart_management)Publishing Charts Online

# Publishing Charts Online

The client terminal is integrated into [MQL5.community](https://www.mql5.com/ "MQL5.community") to provide traders with access to powerful and useful services. One of these services is MQL5 Charts. It allows to publish screenshots of the client terminal online. In just a few clicks you can publish a screenshot, get the link to share it with your fellow traders or send it to one of the popular social networks (Facebook, Twitter, VKontakte, Google+, etc.).

You even do not need to have MQL5.community account to publish screenshots. If your account is not specified in the terminal settings, a screenshot will be published anonymously and you will just get the links to it.

However, publication with binding to MQL5.community account provides a number of obvious advantages: you will be able to create your own images gallery and manage it via "Charts" tab of your MQL5.community profile.

## Making a Screenshot [#](mql5_charts#screenshot)

To make a screenshot of a chart, execute "![Save As Picture](/en/docs/mt4/terminal/img/save_as_picture_icon.png "Save As Picture") Save As Picture" command in its context menu. After that the following window will appear:

![save_as_picture](/en/docs/mt4/terminal/img/save_as_picture.png)

The following options will be available:

-   Active workspace — save the entire window of the client terminal.
-   Active chart (as is) — save the current chart in its current size.
-   Active chart — specify the size of the saved chart (in pixels).
-   Post image online in MQL5 Charts service and get the link — if this option is disabled, the chart will be saved on a user's PC. When clicking "ОК", the standard file saving window will appear. If this option is enabled, the chart will be saved online in MQL5 Charts service. Comments to the chart can be added in the empty field below.

## Publishing Charts Online in MQL5 Charts [#](mql5_charts#publish)

Enable "Post image online in MQL5 Charts service and get the link" option to publish a screenshot of the client terminal online. Text comments can be added to the published image. A new browser window with the published image will be opened immediately after clicking "OK" button:

![Published screenshot of the client terminal](/en/docs/mt4/terminal/img/mql5community_charts_link.png "Published screenshot of the client terminal")

The following data is located at the top of the chart display window:

-   Automatically generated header — current chart symbol and period, publication date and trade server name.
-   Views — number of screenshot views.
-   Commands for publishing screenshots in social networks — VKontakte, Facebook, Twitter, Google+, Evernote, Pinterest, LinkedIn, LiveJournal. Clicking one of these buttons will take you to the appropriate web resource. If you are already authorized in a social network, a screenshot will be published immediately via your profile.

The screenshot itself comes next. The comment field is located below. If a comment has not been added during the publication, automatically generated caption containing the current chart symbol and period is displayed.

Various links to the screenshot are displayed at the bottom:

-   Link to this page — a link to the screenshot view page.
-   Image — a direct link to the image.
-   HTML — a link for insertion in HTML page source code.
-   bbCode — a link for insertion in an editor supporting bbCode markup language (used by many web resources, forums, etc.).

A date of the screenshot publication is displayed at the bottom of the window. When hovering the mouse pointer over this line, delete button appears. Thus, any published screenshot can be deleted.

## Screenshots Gallery in MQL5.community Profile

As noted above, if a user has specified his/her MQL5.community account in the [terminal settings](/en/docs/mt4/terminal/setup/settings_mql5community), a screenshot is bound to that account during the publication. Each user has "Charts" section in MQL5.community profile where all images published by that user are stored:

!["Charts" section in MQL5.community user profile](/en/docs/mt4/terminal/img/mql5community_charts.png ""Charts" section in MQL5.community user profile")

Clicking on a miniature copy of an image, you will go to the [display](/en/docs/mt4/terminal/chart_management/mql5_charts#publish) window. "Charts" tab allows to easily manage your image gallery and share screenshots with other community members and friends in social networks.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">You even do not need to have MQL5.community account to publish screenshots. In case account data is not specified, a screenshot will be published anonymously.</span></p></td></tr></tbody></table>

[Lists of Objects Applied](/en/docs/mt4/terminal/chart_management/charts_control/charts_objects_list)

[Quick Trading](/en/docs/mt4/terminal/chart_management/chart_trading)