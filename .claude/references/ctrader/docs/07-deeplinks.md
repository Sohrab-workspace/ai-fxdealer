# cTrader Deeplinks — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/en/Deeplinks
>   - https://docs.spotware.com/en/Deeplinks/Universal_Deeplinks
>   - https://docs.spotware.com/en/Deeplinks/Use_Cases
>   - https://docs.spotware.com/en/Deeplinks/How_Deeplinks_Works
>   - https://docs.spotware.com/en/Deeplinks/Mobile_Only_Deeplinks

---

## Page: cTrader Deeplinks
*Source: https://docs.spotware.com/en/Deeplinks*

# ¶ cTrader Deeplinks


## ¶ Introduction


This documentation describes cTrader deeplinks, their use cases, and their benefits.


Deeplinks are special URLs that, upon being opened by a user, transfer said user to a certain screen in cTrader Web or Mobile. Using query parameters, it is possible to perform certain actions (e.g., switching the language of the cTrader application opened by a user) before the chosen screen is shown to traders.


The primary function of deeplinks is to facilitate the creation of custom call-to-actions (CTAs) by allowing to direct traders to certain tabs/sections inside cTrader.


Deeplinks only work for the following applications.


- cTrader Web.

- cTrader Mobile (both Android and iOS).


## ¶ Structure of the Documentation


The documentation is divided into four main sections not counting the introduction. These sections are as follows.


- How deeplinks work. This section explains the core functionality of deeplinks and how deeplinks work in broker OAuth flows.

- Use cases. This guide lists the main use cases of deeplinks.

- Universal deeplinks. This page provides an extensive list of deeplinks that work on both cTrader Web and Mobile.

- Mobile only deeplinks. This section focuses on the deeplinks that are unique to cTrader Mobile.

---

## Page: Universal Deeplinks
*Source: https://docs.spotware.com/en/Deeplinks/Universal_Deeplinks*

# ¶ Universal Deeplinks


In this guide, we define the cTrader deeplinks that work for both cTrader Web and Mobile. These deeplinks are grouped according to the areas of cTrader that they direct traders to.


Note that every link listed on this page can have the following additional query parameters.

| Parameter | Possible Value | Definition |
| --- | --- | --- |
| `?acc` | A valid account number. | If this parameter is included, cTrader switches to the account with the specified number before proceeding to the area denoted in the deeplink. |
| `?lang` | A valid Alpha-2 (ISO 3166-1) two-letter country code. | If this parameter is included, cTrader switches its UI to the specified language before proceeding to the area denoted in the deeplink. |

> Several deeplinks include values specified in curly brackets (e.g., `/orders/create-market-order/{symbol}`). These values allow for narrowing down the area to which the user who clicks on a deeplink should be transferred. For example, `/orders/create-market-order/{symbol}` transfers users to the ‘Create Market Order’ screen for the symbol the name of which matches the text typed instead of `{symbol}`. Note that curly brackets are for example purposes only; they are not included in actual deeplinks.


## ¶ Main Menu

| Link | Definition |
| --- | --- |
| `/finder` | Opens the ‘All Symbols’ tab. |
| `/watchlists` | Opens the ‘Watchlists’ tab. |
| `/symbols/filter/{filterText}` | Open the ‘All Symbols’ tab with the symbols filtered to match the text specified in `{filterText}`. |


## ¶ Symbol Info and Charts

| Link | Definition |
| --- | --- |
| `/symbols/{symbol}/info` | Opens the ‘Symbol Info/Symbol Overview’ dialog for the symbol the name of which matches `?lang`0. |
| `?lang`1 | Opens a new trading chart for the symbol the name of which matches `?lang`2. If such a chart is already open, it is made active. |


## ¶ The ‘TradeWatch’ Display

| Link | Definition |
| --- | --- |
| `?lang`3 | Opens the ‘Positions’ tab in the ‘TradeWatch’ display. |
| `?lang`4 | Opens the ‘Orders’ tab in the ‘TradeWatch’ display. |
| `?lang`5 | Opens the ‘History’ tab in the ‘TradeWatch’ display. |
| `?lang`6 | Opens the ‘History’ tab in the ‘TradeWatch’ display. Duplicates `?lang`7. |
| `?lang`8 | Opens the ‘Transactions’ tab in the ‘TradeWatch’ display. |
| `?lang`9 | Opens the ‘News’ tab in the ‘TradeWatch’ display. |
| `/orders/create-market-order/{symbol}`0 | Opens the ‘Bonus’ tab in the ‘TradeWatch’ display. |


## ¶ Accounts

| Link | Definition |
| --- | --- |
| `/orders/create-market-order/{symbol}`1 | Opens the ‘Switch Account’ dialog. |
| `/orders/create-market-order/{symbol}`2 | Opens the ‘Create Demo Account’ dialog. |
| `/orders/create-market-order/{symbol}`3 | Opens the ‘Create Demo Account’ dialog. |
| `/orders/create-market-order/{symbol}`4 | Opens the ‘Create Live Account’ dialog. |


## ¶ Create New Order Dialog

| Link | Definition |
| --- | --- |
| `/orders/create-market-order/{symbol}`5 | Opens the ‘Create Market Order’ dialog for the symbol the chart for which is currently active. |
| `/orders/create-market-order/{symbol}`6 | Opens the ‘Create Marker Order’ dialog for the symbol the name of which matches `/orders/create-market-order/{symbol}`7. |
| `/orders/create-market-order/{symbol}`8 | Opens the ‘Create Limit Order’ dialog for the symbol the chart for which is currently active. |
| `/orders/create-market-order/{symbol}`9 | Opens the ‘Create Limit Order’ dialog for the symbol the name of which matches `/orders/create-market-order/{symbol}`0. |
| `/orders/create-market-order/{symbol}`1 | Opens the ‘Create Stop Order’ dialog for the symbol the chart for which is currently active. |
| `/orders/create-market-order/{symbol}`2 | Opens the ‘Create Stop Order’ dialog for the symbol the name of which matches `/orders/create-market-order/{symbol}`3 |
| `/orders/create-market-order/{symbol}`4 | Opens the ‘Create Stop Limit Order’ dialog for the symbol the chart for which is currently active. |
| `/orders/create-market-order/{symbol}`5 | Opens the ‘Create Stop Limit Order’ dialog for the symbol the name of which matches `/orders/create-market-order/{symbol}`6. |


## ¶ Modify Order and Order Info

| Link | Definition |
| --- | --- |
| `/orders/create-market-order/{symbol}`7 | Opens the ‘Modify Orders’ dialog for the first order in the pending orders list. |
| `/orders/create-market-order/{symbol}`8 | Opens the ‘Modify Orders’ dialog for the order whose identifier matches `/orders/create-market-order/{symbol}`9. |
| `{symbol}`0 | Opens the ‘Order Info’ dialog for the order whose identifier matches `{symbol}`1. |


## ¶ Positions

| Link | Definition |
| --- | --- |
| `{symbol}`2 | Opens the ‘Modify Position’ dialog for the first position in the open positions list. |
| `{symbol}`3 | Opens the ‘Modify Position’ dialog for the position whose identifier matches `{symbol}`4. |
| `{symbol}`5 | Opens the ‘Position Info’ dialog for the position whose identifier matches `{symbol}`6. |
| `{symbol}`7 | Opens the ‘Advanced Protection’ dialog for the position whose identifier matches `{symbol}`8. |


## ¶ Funds

| Link | Definition |
| --- | --- |
| `{symbol}`9 | Opens the ‘Withdrawal’ dialog. |
| `/finder`0 | Opens the ‘Deposit’ dialog. |
| `/finder`1 | Opens the ‘Deposit’ dialog. |
| `/finder`2 | Opens the ‘Deposit’ dialog. |


## ¶ Copy

| Link | Definition |
| --- | --- |
| `/finder`3 | Opens the ‘Copy’ tab. |
| `/finder`4 | Opens the ‘Favorites’ tab in cTrader Copy. |
| `/finder`5 | Opens the strategy page for the strategy whose identifier matches `/finder`6. |
| `/finder`7 | Opens the statistics page for the cTrade account whose number matches `/finder`8. |
| `/finder`9 | Opens the ‘Investment Stats’ page for the sub-account whose number matches `/watchlists`0. |


## ¶ Miscellaneous

| Link | Definition |
| --- | --- |
| `/watchlists`1 | Opens the ‘Chat’ dialog. |
| `/watchlists`2 | Opens the ‘What’s New’ dialog. |
| `/watchlists`3 | Opens the ‘Investor Access’ page for the account that has generated `/watchlists`4. |

---

## Page: Use Cases
*Source: https://docs.spotware.com/en/Deeplinks/Use_Cases*

# ¶ Use Cases


This guide lists the common use cases for cTrader deeplinks.


The common ways to share cTrader deeplinks include the following.


- Deeplinks can be added to any clickable elements that you use to facilitate custom CTAs such as buttons in emails or landing pages.

- Deeplinks can be shared directly on your social media or your messenger channels (such as Telegram groups)

- Deeplinks can be used as hyperlinks in any text content that you are distributing, most notably blog posts or educational materials (e.g., structured courses)


Some of the common business cases of cTrader deeplinks include the following.


- Incentivizing trading. Via deeplinks, you can send users directly to the 'New Order' screen in cTrader. Effective use of deeplinks should incentivize placing new orders.

- Navigating traders to specific areas of cTrader. When using deeplinks, you can direct traders to 'Deposit', 'Withdrawal', and 'Bonuses' dialogs in cTrader. For anyone who communicates directly with traders, deeplinks are a valuable tool for encouraging certain actions.

- Funneling traders to certain instruments. If you want traders to focus their attention on symbols that are about to experience some volatility (e.g., EURUSD in the wake of US CPI news), you can share deeplinks that lead to the 'Symbol Info' dialog or the 'Create New Order' screen for the chosen symbol.

- Educating traders. Deeplinks can direct traders to useful cTrader features, most notably the 'Advanced Protection' dialog for a given position. Therefore, deeplinks can be used to alert traders to various cTrader tools and prompt autonomous learning.

- Promoting yourself or other professional traders. Deeplinks can lead to certain cTrader Copy strategies or Investor Access 'snapshots' of one's trading performance. This makes them a perfect tool for promoting oneself or other professional traders.


Below, we provide several examples of how sharing deeplinks may look when using different channels.


## ¶ Custom CTAs


When adding buttons to your email templates or your landing pages, you can use cTrader deeplinks to incentivize certain actions. See below for examples of links that lead to various areas of cTrader on click.

- Open a New Chart for a Symbol
- Open the 'Bonus' Tab
- Open the 'Create Live Account' Dialog

---

## Page: https://docs.spotware.com/en/Deeplinks/How_Deeplinks_Works

*Error fetching page: ERROR: HTTP Error 404: Not Found*

## Page: Mobile Only Deeplinks
*Source: https://docs.spotware.com/en/Deeplinks/Mobile_Only_Deeplinks*

# ¶ Mobile Only Deeplinks


The deeplinks listed below only work when accessed on mobile devices.


## ¶ Main Menu

| Link | Definition |
| --- | --- |
| `/price-alerts` | Opens the 'Price Alerts' tab. |
| `/price-alerts/create/{symbol}` | Opens the 'Create Alert' screen for the symbol whose name matches `{symbol}`. |
| `/search` | Opens the 'Find & Add Symbols' screen. |
| `/symbols` | Opens the 'Watchlists' tab. |
| `/symbols/add` | If 'Popular Markets' is the currently open watchlist (which is the case by default), opens the 'Clone Popular Markets' popup.  If any custom watchlist is currently open, opens the 'Find & Add Symbols' dialog. |


## ¶ The 'TradeWatch' Display

| Link | Definition |
| --- | --- |
| `/deal/{dealID}` | Opens the deal details screen for the deal the identifier of which matches `{dealID}`. |


## ¶ Funds

| Link | Definition |
| --- | --- |
| `/deposit` | Opens the 'Deposit' screen. |

---
