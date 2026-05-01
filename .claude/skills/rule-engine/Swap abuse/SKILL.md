

# 💰 Swap-Free Hedging Abuse Detection (SFA)

---

## 1. Rule Definition

```md
Rule Name: Swap-Free Hedging Abuse Detection  
Rule Handler: SFA  
Objective: Detect traders exploiting swap-free grace periods by maintaining hedged positions and cycling legs to capture positive swap while avoiding negative swap charges.
```

---

# 2. Concept Explanation

Swap-Free Abuse (real version) is a strategy where a trader exploits the **swap-free grace period (e.g., 14 or 30 days)** to generate **risk-free swap income** using **fully hedged positions**.

Under normal conditions:

* Swap applies daily on open positions
* One direction = positive swap
* Opposite direction = negative swap

Under swap-free conditions:

* No swap is charged during the grace period

This creates a loophole:

> Trader can construct a **hedged position with zero market exposure**, then selectively **harvest positive swap while resetting negative swap legs before they become chargeable**.

---

# 3. Abuse Mechanism (Real Flow)

## Core Strategy

1. Trader opens a **swap-free account**
2. Identifies symbols with **high swap asymmetry**
3. Opens **fully hedged positions**:

   * Buy position
   * Sell position
     → Net PnL ≈ 0 (market neutral)

---

## Rollover Cycle Exploitation

At each swap rollover:

### Step 1 — Identify swap directions

* One leg = positive swap
* One leg = negative swap

---

### Step 2 — Close negative swap leg

* Before swap becomes chargeable (or before grace logic triggers)
* Trader closes the **negative swap position**

---

### Step 3 — Reopen negative leg

* Immediately reopens same direction
* Reset holding timer → avoids swap charging window

---

### Step 4 — Keep positive leg running

* Positive swap leg is **not closed**
* Continues accumulating swap

---

### Step 5 — Repeat daily

Result:

* Market exposure = neutral
* PnL from price = ~0
* Swap = **net positive income**

---

## Key Insight

> Trader converts swap-free feature into a **synthetic risk-free yield engine**.

---

# 4. Abuse Objective

Trader is exploiting:

* swap-free grace period
* asymmetric swap rates
* position reset mechanics
* lack of enforcement on hedged structures

Goal:

* generate **risk-free swap income**
* avoid negative swap completely
* maintain **zero exposure strategy**

---

# 5. Advanced Abuse Patterns

---

## 5.1 Multi-Symbol Swap Farming

* Trader runs strategy across multiple symbols
* Targets highest positive swap opportunities
* Diversifies swap income streams

---

## 5.2 Partial Hedge Optimization

* Not always 100% hedge
* Slight directional bias to increase return

---

## 5.3 Mixed Strategy Camouflage

* Runs normal trading strategy
* Runs swap abuse in parallel
* Makes account look “legit”

---

## 5.4 Multi-Account Optimization

* Different accounts → different symbols
* Or splitting hedge legs across accounts

---

## 5.5 Precision Rollover Execution

* Closing negative leg **seconds before rollover**
* Reopening immediately after
* Extremely consistent timing

---

# 6. Principles of the Abuse Pattern

---

## Principle 1: Zero Market Risk

* Fully hedged positions
* No directional exposure

---

## Principle 2: Profit from Swap Only

* PnL ≈ 0
* Swap = positive

---

## Principle 3: Systematic Leg Reset

* Negative leg constantly recycled
* Positive leg persists

---

## Principle 4: Time-Based Exploitation

* Strategy depends on:

  * rollover timing
  * grace period rules

---

## Principle 5: High Repeatability

* Happens every day
* Same symbols
* Same timing

---

# 7. Metrics and Factors

---

## 7.1 Hedge Ratio

* Buy volume vs Sell volume per symbol

Metric:

* |Buy Volume − Sell Volume|

Expected:

* near zero

---

## 7.2 Swap Accumulation

* total swap gained
* swap vs PnL ratio

---

## 7.3 Leg Duration Asymmetry

* positive leg → long duration
* negative leg → short duration

---

## 7.4 Rollover Behavior

* close timing near rollover
* reopen timing immediately after

---

## 7.5 Position Cycling

* repeated close/open on same symbol
* same volume
* same direction

---

## 7.6 PnL Neutrality

* low price-based PnL variance
* high swap-based income

---

## 7.7 Symbol Selection

* high positive swap symbols

---

## 7.8 Cross-Strategy Activity

* presence of other trades
* hidden abuse within mixed behavior

---

# 8. Detection Logic

---

## Core Detection Idea

Detect accounts where:

* positions are hedged
* negative legs are frequently reset
* positive legs accumulate swap
* PnL is neutral but swap is positive

---

## Step-by-Step Detection

---

### Step 1 — Identify Hedged Structures

* same symbol
* opposite positions
* similar volume

---

### Step 2 — Detect Leg Cycling

* repeated close of one direction
* immediate reopen

---

### Step 3 — Analyze Timing

* events near rollover
* consistent execution timing

---

### Step 4 — Measure Swap Gain

* swap > threshold
* swap / pnl ratio high

---

### Step 5 — Confirm Neutral Exposure

* minimal net PnL
* minimal directional bias

---

# 9. Rules & Metrics for System

---

## Rule Group A — Hedging Structure

### A1: Full Hedge Detection

Metric:

* buy vs sell volume difference

Threshold:

* < 5–10% difference

---

## Rule Group B — Leg Cycling

### B1: Negative Leg Reset Pattern

Metric:

* repeated close + reopen

Threshold:

* X times per day

---

## Rule Group C — Rollover Timing

### C1: Pre-Rollover Closing

Metric:

* close timestamp proximity to rollover

---

### C2: Post-Rollover Reopen

Metric:

* reopen within seconds/minutes

---

## Rule Group D — Swap Profit Dominance

### D1: Swap vs PnL Ratio

Metric:

* swap / total profit

Threshold:

* > 60–80%

---

## Rule Group E — Duration Asymmetry

### E1: Leg Holding Difference

Metric:

* avg duration long vs short leg

Pattern:

* strong imbalance

---

## Rule Group F — Repetition

### F1: Daily Pattern

Metric:

* repeated cycles

---

## Rule Group G — Multi-Symbol

### G1: Parallel Execution

Metric:

* multiple symbols running same pattern

---

# 10. Scoring Model Example

| Factor             | Weight |
| ------------------ | ------ |
| hedge structure    | 20     |
| leg cycling        | 20     |
| rollover timing    | 15     |
| swap dominance     | 20     |
| duration asymmetry | 10     |
| repetition         | 10     |
| multi-symbol       | 5      |

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

* swap values per position
* trade timestamps (ms precision)
* rollover time
* position history
* volume per direction
* PnL breakdown (price vs swap)
* symbol swap rates
* order lifecycle

---

# 12. Differentiation from Legit Trading

Legit trader:

* directional exposure
* closes positions normally
* swap is side-effect

Abuser:

* neutral exposure
* constant hedge
* swap is primary profit source
* repetitive rollover manipulation

---

# 13. System Actions

---

## Level 1 — Monitor

* track hedge + swap pattern

---

## Level 2 — Restrict

* disable hedge on swap-free
* apply early swap charging

---

## Level 3 — Financial Review

* calculate unfair swap gain
* adjust balance

---

## Level 4 — Enforcement

* warning
* profit deduction
* convert account type
* terminate account

---

# 14. Evidence Package

* hedge structure snapshot
* trade timing logs
* rollover execution pattern
* swap accumulation chart
* leg duration comparison
* repeated cycle proof

---

# 15. One-Line Definition

**Swap-Free Hedging Abuse is the systematic use of hedged positions and rollover timing to accumulate positive swap while continuously resetting negative swap exposure within swap-free grace periods.**

---

# 16. Engine Definition (Short)

**Trigger when a trader maintains hedged positions, repeatedly resets negative swap legs around rollover, and generates profit primarily from swap while maintaining near-zero market exposure.**

---

# 🔥 Final Reality

This is one of the **cleanest “risk-free profit engines”** traders can build.

If your system misses this:

* You won’t see it in PnL
* You won’t see it in exposure
* You’ll only see it… in slow bleeding swap cost

And by the time you notice, they’ve already scaled it.

---


