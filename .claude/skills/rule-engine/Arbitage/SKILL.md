

# ⚡ Latency Arbitrage Detection (LARB)

---

## 1. Rule Definition

```md
Rule Name: Latency Arbitrage Detection  
Rule Handler: LARB  
Objective: Detect traders exploiting latency differences between broker price feed and real market prices to secure risk-free or low-risk profits.
```

---

# 2. Concept Explanation

Latency Arbitrage is a trading abuse strategy where a trader exploits the time delay between:

* broker price update
* actual market price (LP / reference feed)

The trader enters trades using **outdated (stale) prices** and closes after the system catches up.

This is not prediction.
This is **speed + infrastructure exploitation**.

---

# 3. Abuse Mechanism

## Core Flow

1. Market moves quickly (usually during volatility or micro-movements)
2. Broker price lags behind real market
3. Trader detects delay (via faster feed / VPS / colocated infra)
4. Trader executes order on stale price
5. Price updates to real level
6. Trader closes instantly → profit locked

---

## Key Insight

> The trader already knows the future price — because your system is behind.

---

## Execution Variants

### A. Entry Arbitrage

* Trader opens at stale price
* Market already moved
* Instant profit after update

---

### B. Exit Arbitrage

* Trader holds position
* Waits for favorable stale quote
* Closes at unrealistic price

---

### C. Two-sided rapid execution

* Buy and Sell rapidly based on micro delays
* Captures micro inefficiencies repeatedly

---

### D. News spike exploitation

* During high volatility
* LP moves instantly
* Broker lags → trader attacks

---

# 4. Abuse Objective

Trader aims to exploit:

* stale quotes
* execution delay
* price feed latency
* slow bridge / LP sync
* server-side inefficiencies

Goal:

* near risk-free profit
* extremely high win rate
* minimal drawdown

---

# 5. Advanced Abuse Patterns

---

## 5.1 VPS / Co-location Advantage

Trader uses:

* VPS near broker server
* ultra-low latency (1–5 ms)
* faster execution than system correction

---

## 5.2 Multi-feed Monitoring

Trader compares:

* broker feed
* external feed (LP / ECN / other brokers)

Executes when mismatch detected.

---

## 5.3 Scalping Burst Pattern

* Many trades in short time
* extremely short holding time
* consistent micro-profits

---

## 5.4 EA / Bot Execution

* automated execution
* precise timing
* zero hesitation

---

## 5.5 Hybrid Abuse (Latency + Gap)

Combines:

* latency delay
* price spike

Very hard to detect if rules are weak.

---

# 6. Principles of the Abuse Pattern

---

## Principle 1: Profit from time advantage, not price movement

Trader wins because:

* system is slow
  NOT because:
* market direction was predicted

---

## Principle 2: Entry price is already “wrong”

At execution time:

* real market ≠ broker price

---

## Principle 3: Extremely short exposure

Trader avoids risk:

* enters → exits quickly
* avoids real market fluctuation

---

## Principle 4: High consistency

* high win rate
* low variance
* repeated behavior

---

## Principle 5: Execution precision

* millisecond timing
* abnormal efficiency

---

# 7. Metrics and Factors

---

## 7.1 Latency Metrics

* Ping (client → server)
* Execution time
* Order round-trip time

---

## 7.2 Price Deviation Metrics

* Broker price vs reference price at execution
* Deviation in points/pips
* Directional advantage

---

## 7.3 Trade Duration

* holding time (very low)
* time to profit realization

---

## 7.4 Profit Behavior

* high win rate
* low drawdown
* consistent micro gains

---

## 7.5 Execution Timing

* clustered trades
* reaction to price updates
* microsecond/millisecond precision

---

## 7.6 Trade Pattern

* rapid open/close
* repeated entries
* no swing or long trades

---

## 7.7 Environment Context

* volatile periods
* news windows
* rapid tick changes

---

## 7.8 Cross-Account Metrics

* same IP / VPS
* mirrored behavior
* synchronized trades

---

# 8. Detection Logic

---

## 8.1 Core Detection Idea

Detect mismatch between:

* execution price
* real market price

AND

* trader consistently benefits from that mismatch

---

## 8.2 Step-by-Step Detection

### Step 1: Identify Price Deviation

Check:

* execution price vs reference price
* deviation at execution timestamp

---

### Step 2: Validate Advantage

* did deviation favor trader?
* was it systematically profitable?

---

### Step 3: Analyze Timing

* ultra-fast execution
* short holding time

---

### Step 4: Pattern Recognition

* repeated behavior
* consistent profit structure

---

### Step 5: Cross-check with Market

* was market already moved?
* was broker late?

---

# 9. Rules & Metrics for System

---

## Rule Group A — Price Deviation

### A1: Execution Deviation Score

Metric:

* |Execution Price - Reference Price|

Threshold:

* exceeds X points

Score:

* proportional to deviation

---

## Rule Group B — Directional Advantage

### B1: Favorable Deviation

Metric:

* % of trades where deviation benefits trader

Threshold:

* > 70% favorable

---

## Rule Group C — Trade Duration

### C1: Ultra Short Trades

Metric:

* holding time

Threshold:

* < 5–30 seconds

---

## Rule Group D — Win Rate

### D1: Abnormal Win Rate

Metric:

* % profitable trades

Threshold:

* > 75–85%

---

## Rule Group E — Repetition

### E1: Pattern Frequency

Metric:

* number of similar trades

Threshold:

* repeated within short window

---

## Rule Group F — Latency Efficiency

### F1: Low Ping + High Precision

Metric:

* ping vs execution success

Pattern:

* low latency + high profit efficiency

---

## Rule Group G — Market Timing

### G1: Volatility Exploitation

Metric:

* trades during high tick velocity

---

## Rule Group H — Cross Account

### H1: Correlated Accounts

Metric:

* shared infra + mirrored trades

---

# 10. Scoring Model Example

| Factor                | Weight |
| --------------------- | ------ |
| Price deviation       | 25     |
| Directional advantage | 15     |
| Trade duration        | 10     |
| Win rate              | 15     |
| Repetition            | 10     |
| Latency efficiency    | 10     |
| Market timing         | 5      |
| Cross-account         | 10     |

---

## Score Bands

| Score | Result          |
| ----- | --------------- |
| 0–24  | Normal          |
| 25–49 | Monitor         |
| 50–69 | Suspicious      |
| 70+   | Abuse Candidate |

---

# 11. Required Data Inputs

Critical:

* millisecond timestamps
* execution price
* bid/ask history
* reference feed price
* ping
* order execution time
* trade duration
* tick stream
* device/IP/VPS data

Without reference price → detection becomes weak.

---

# 12. Differentiation from Legit Trading

Legit trader:

* takes risk
* holds trades
* mixed results
* reacts slower

Latency abuser:

* near-perfect timing
* very short trades
* consistent profit
* exploits system delay

---

# 13. System Actions

---

## Level 1 — Monitor

* track behavior

---

## Level 2 — Restrict

* execution delay
* slippage control
* routing change

---

## Level 3 — Financial Review

* validate profits
* compare with LP

---

## Level 4 — Enforcement

* warning
* profit deduction
* account limitation
* termination

---

# 14. Evidence Package

Must include:

* execution timestamp
* price comparison (broker vs market)
* deviation chart
* trade duration
* repeated pattern
* latency metrics
* cross-account links

---

# 15. One-Line Definition

**Latency Arbitrage is the systematic exploitation of delayed broker pricing relative to the real market to execute trades at stale prices and capture near risk-free profit.**

---

# 16. Engine Definition (Short)

**Trigger when a trader consistently executes trades at prices deviating from real market levels due to latency and closes them quickly with statistically abnormal profitability.**

---

# 17. Structured Rule Template

```md
Rule Name: Latency Arbitrage Detection  
Handler: LARB  

Objective:
Detect exploitation of stale pricing caused by latency differences.

Core Mechanism:
Trader executes at outdated price → market catches up → instant profit.

Key Metrics:
- execution deviation
- latency/ping
- trade duration
- win rate
- repetition
- market timing

Detection Rules:
- deviation threshold
- favorable execution ratio
- ultra-short holding time
- repeated pattern
- latency advantage correlation

System Action:
- monitor
- restrict
- review
- enforce

Required Data:
- ms timestamps
- reference price
- execution logs
- tick data
- latency data
```

