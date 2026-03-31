# Reporting DB (Repo DB) — Spotware Documentation
> Scraped from docs.spotware.com on 2026-03-31
> Source URLs:
>   - https://docs.spotware.com/Repo_DB
>   - https://docs.spotware.com/en/Repo_DB
>   - https://docs.spotware.com/en/Repo_DB/Establishing_a_Connection
>   - https://docs.spotware.com/en/Repo_DB/Use_Cases_Example_Queries

---

## Page: Repo DB
*Source: https://docs.spotware.com/Repo_DB*

# ¶ Reporting DB


The **Reporting DB** is a read-only replica of the production PostgreSQL database used by the cTrader backend. The replica can provide near real-time information about key server entities including traders, groups, balance operation histories, etc.

> If you are a non-broker entity, you cannot work with white labels through the Reporting DB. Please use other APIs or contact us at partners@spotware.com for clarifications.


# ¶ How the Reporting DB Works


The **Reporting DB** is a relational database that you can connect to using any DB client that supports the PostgreSQL (Postgres) system.


After establishing a connection, the **Reporting DB** can be interacted with by simply sending SQL queries to it. As a result, the **Reporting DB** can be easily integrated in any existing SQL-based reporting system you have. Alternatively, you may use it as a foundation of a new custom reporting service.


Note that the **Reporting DB** only allows for performing ‘READ’ operations out of all standard CRUD operations.

> The servers for the Reporting DB and the main production databases used by the cTrader backend are geographically dispersed, meaning that there may be some latency in communications between the ‘main’ database and its replica. On average, this latency should not exceed one (1) second; however, in some cases, it may reach 30 seconds. This also means that if anything happens to the ‘main’ production database, the Reporting DB should still remain in operation and contain data that was valid prior to the outage.


# ¶ Key Use Cases


The **Reporting DB** is similar in function to the [**Reporting API**](/Reporting_API) in that it can be used to receive up-to-date information on all major server entities. Compared to the [**Reporting API**](/Reporting_API), however, integration with the **Reporting DB** is less demanding in terms of development costs. We recommend integrating with the **Reporting DB** (rather than the **Reporting API**) in the following cases.


- When you want to implement a reporting solution where using real-time data is not required.

- When you need to investigate trading data for a particular period to handle a trade dispute.

- When you need to conduct an in-depth analysis of past data (e.g., to identify trends in traded symbols).

- When you want to add new analytics to your CRM suite that are not provided as part of the WebServices API (e.g., balance history).


> The Reporting DB does not contain real-time information on position P&L, account equity, and similar statistics. If it is imperative for you to receive any changes to such data in real-time, we recommend integrating with the Reporting API.


# ¶ Structure of the Documentation


The **Reporting DB** documentation includes the following guides.


- Establishing a connection

- Use cases and example queries

- Replication limitations

---

## Page: Establishing a Connection
*Source: https://docs.spotware.com/en/Repo_DB/Establishing_a_Connection*

# ¶ Establishing a Connection


To connect to the **Reporting API**, all you have to do is perform the following actions.


- Whitelist the necessary IPs and route your connection via Stunnel.

- Initiate a connection using a Postgres client of your choice.


# ¶ Whitelisting IPs and Using Stunnel


To whitelist your IPs, simply provide them to Spotware’s service assurance team.


Afterward, you will need to route your connection via [**Stunnel**](https://www.stunnel.org/), a well-known provider of TSL/SSL encryption functionality. To do so, you will need to ensure that **Stunnel** is deployed successfully and is configured to match our requirements. This configuration can be provided by Spotware’s service assurance team upon request.


# ¶ Initiating a Connection via a Postgres Client


After routing your connection via **Stunnel**, you can freely connect to the **Reporting DB** using any suitable Postgres client of your choice. The credentials for doing so are summarised below.

| Name | Value (Demo) | Value (Live) |
| --- | --- | --- |
| `host` | `{stunnelHost}` | `{stunnelHost}` |
| `port` | `{stunnelPort}` | `{stunnelPort}` |
| `username` | `{plantId}_{environmentName}_repo` | `{plantId}_{environmentName}_repo` |
| `password` | `{stunnelHost}`0 | `{stunnelHost}`1 |
| `{stunnelHost}`2 | `{stunnelHost}`3 | `{stunnelHost}`4 |

> The values of `{stunnelHost}`5 and `{stunnelHost}`6 depend on the way you have chosen to deploy Stunnel. For example, if you are running Stunnel via a Docker container, `{stunnelHost}`7 would need to reference the container name.

> The values of `{stunnelHost}`8, `{stunnelHost}`9, `{stunnelHost}`0, and `{stunnelHost}`1 are provided by Spotware’s service assurance team.


In the example below, we use the `{stunnelHost}`2 Nuget package to connect to the **Reporting DB** via C#. The example retrieves the names of the first 100 entries in the `{stunnelHost}`3 table of the database.


```c
static class Program
{
    public static async Task Main() {

    		string username = "plantOne_live_repo";

        string password = "strongPassword";

        string stunnelHost = "localhost";

        string stunnelPort = "5432";

        var connectionString = "Host={stunnelHost};Port={stunnelPort};Username={username};Password={password};Database=ctrader_spotware";
        await using var dataSource = NpgsqlDataSource.Create(connectionString);

        await using (var cmd = dataSource.CreateCommand("SELECT * FROM \"tables_demo\".\"asset\" LIMIT 100"))
        await using (var reader = await cmd.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {
                Console.WriteLine(reader.GetString(1));
            }
        }
    }
}

```

---

## Page: Use Cases and Example Queries
*Source: https://docs.spotware.com/en/Repo_DB/Use_Cases_Example_Queries*

# ¶ Use Cases and Example Queries


This guide contains simple examples of queries you can make to the **Reporting DB** to receive data on essential statistics and operations. The examples are sorted by the type of server entity that they cover.


## ¶ Group Profiles


See the 10 commission profiles with the largest minimum commissions.


```sql
SELECT commission_profile_id, name, min_commission
FROM "tutorialdb_demo"."commission_profile"
ORDER BY min_commission DESC
LIMIT 10;

```


## ¶ Groups

See all groups in which traders can change stop out types and fair stop outs are disabled.


```sql
SELECT trader_group_id, name
FROM "tutorialdb_demo"."trader_group"
WHERE fair_stop_out = false AND allow_trader_change_so = true;

```


## ¶ Deals

See the last 1000 deal IDs (and the related symbol IDs) whose status equaled `ERROR`.


```sql
SELECT deal_id, symbol_id
FROM "tutorialdb_demo"."deal"
WHERE deal_status = 6
ORDER BY deal_id DESC
LIMIT 1000;

```


## ¶ Positions

See 100 positions with the largest used margin that were open by the start of the current day.


```sql
SELECT trader_id, position_id, symbol_id, margin, net_unrealized_pnl
FROM "tutorialdb_demo"."daily_open_positions"
ORDER BY margin DESC
LIMIT 100;

```


## ¶ Symbols

See the top 10 symbols for the volume of all currently open positions is the largest.


```sql
SELECT s.symbol_id, name, description, SUM(d.volume) AS total_volume
FROM "tutorialdb_demo"."symbol" s
INNER JOIN "tutorialdb_demo"."daily_open_positions" d ON s.symbol_id = d.symbol_id
GROUP BY s.symbol_id, name, description
ORDER BY total_volume DESC
LIMIT 10;

```


## ¶ Traders

See 10 traders with the largest negative balance deltas who currently have open positions.


```sql
SELECT b.trader_id, SUM(b.delta) AS total_delta
FROM "tutorialdb_demo"."balance_history" b
INNER JOIN "tutorialdb_demo"."daily_open_positions" o ON b.trader_id = o.trader_id
GROUP BY b.trader_id
ORDER BY total_delta ASC
LIMIT 10;

```

---
