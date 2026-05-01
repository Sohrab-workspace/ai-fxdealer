
---

# 1. Rule Engine Framework

## 1.1 Objective

The Rule Engine Framework is responsible for:

* Monitoring trading behavior in real time
* Detecting abnormal or abusive patterns
* Scoring accounts using configurable weighted metrics
* Classifying accounts into severity levels
* Creating reviewable cases for Dealers/Admins
* Supporting configurable, extensible rule engines

This framework is shared across all rule engines, including:

* Price Gap Abuse (PGE)
* Latency Arbitrage (LARB)
* Toxic Flow
* Swap Abuse
* Custom rules created by Admin

---

## 1.2 Core Principles

### Weighted Scoring System

Each rule evaluates multiple metrics.
Each metric contributes a score → final score = weighted sum.

No single metric defines abuse unless explicitly configured.

---

### Fully Configurable by Admin/Dealer

Each rule engine must allow:

* Add / remove metrics
* Enable / disable metrics
* Configure metric thresholds
* Configure metric weights
* Configure severity score boundaries
* Enable / disable rule engine
* Reset to default configuration
* Create new custom rules

---

### Modular Design

* Same framework for all rules
* Different logic per rule
* Same case lifecycle
* Same flagging system
* Same dealer workflow

---

### Monitoring Scope

Only **Trade-Enabled accounts** are monitored.

If account becomes **Trade Disabled → automatically removed from monitoring**

---

# 2. Severity Classification Model

Each account is classified per rule:

1. Normal Activity
2. Under Monitor
3. Suspicious
4. Abuse Candidate

---

## Severity Meaning

| Level           | Meaning            |
| --------------- | ------------------ |
| Normal          | No meaningful risk |
| Under Monitor   | Early signals      |
| Suspicious      | Requires review    |
| Abuse Candidate | Strong evidence    |

---

# 3. Scoring System

## 3.1 Formula

```
Final Score = Σ (Metric Score × Weight)
```

---

## 3.2 Configurable Elements

Admin can configure:

* Metric weights
* Metric thresholds
* Severity score ranges
* Default presets
* Reset to default

---

## 3.3 Example Severity Mapping

| Score | Severity        |
| ----- | --------------- |
| 0–24  | Normal          |
| 25–49 | Monitor         |
| 50–69 | Suspicious      |
| 70+   | Abuse Candidate |

---

# 4. Metrics Framework

## 4.1 Available Metrics (Examples)

* Symbol
* IP / CID
* Ping
* Session
* PnL
* Spread at execution
* Tick behavior
* Trade duration
* Order type
* Execution deviation
* Reference price comparison
* Device fingerprint
* Cross-account linkage

---

## 4.2 Metric Capabilities

Admin can:

* Add/remove metrics
* Enable/disable metrics
* Set thresholds
* Assign weights
* Define custom conditions

---

## 4.3 Custom Rule Creation

Admin can create new rule engines:

* Custom name
* Custom handler
* Selected metrics
* Custom scoring
* Custom thresholds

---

# 5. Rule Engine Definition

Each rule contains:

## Basic Fields

* Rule Name
* Rule Handler (Required)
* Description
* Status (Enabled / Disabled)
* Default Preset

---

## Rule Handler (Critical)

* Mandatory field
* Cannot be empty
* Used in tagging

Example:

* Price Gap Exploitation → **PGE**

---

## Configurable Sections

* Metrics
* Metric conditions
* Score weights
* Severity thresholds

---

# 6. Account Flagging System

Each account has **two independent tags**:

---

## 6.1 Severity Tag

* Normal
* Monitor
* Suspicious
* Abuse Candidate

---

## 6.2 Rule Handler Tag

Indicates which rule triggered detection.

Example:

* Severity: Suspicious
* Tag: PGE

---

## 6.3 Multi-Rule Support

Accounts can have multiple tags:

* Suspicious (PGE, LARB)

---

# 7. Case Management System

---

## 7.1 Case Trigger

Cases are created when:

* Severity = Suspicious
* Severity = Abuse Candidate

---

## 7.2 Case Status Lifecycle

* Null
* Pending
* Under Review
* Resolved
* Terminated

---

## Status Definitions

### Null

No active case, monitoring continues.

---

### Pending

* System detected issue
* Awaiting dealer assignment

---

### Under Review

* Dealer is investigating

---

### Resolved

* Reviewed without termination
* Monitoring resumes

---

### Terminated

* Account closed
* Removed from monitoring

---

# 8. Case Assignment

Cases are assigned to:

* Online Dealers/Admins
* "Accept Case" enabled

---

## Distribution Methods

* Round-robin
* Load-based
* Manual override

---

# 9. Dealer Actions

Dealer can:

* Send Warning
* Deduct Profit
* Adjust Balance
* Continue Monitoring
* Terminate Account

---

# 10. Action Outcomes

---

## 10.1 Termination

System must:

* Disable trading
* Deduct profit
* Send email
* Set status → Terminated
* Remove from monitoring

---

## 10.2 Warning Only

System must:

* Send warning
* Reset case to Null
* Resume monitoring
* Increase Review Count

---

## 10.3 Deduction (No Termination)

System must:

* Record deducted profit
* Send email
* Reset to Null
* Resume monitoring
* Increase Review Count

---

## 10.4 Continue Monitoring

* Resume monitoring
* Preserve history
* Increase Review Count

---

# 11. Post-Review Monitoring Logic

---

## Key Rule

System must NOT:

* Forget past behavior
* Immediately re-flag after review

---

## Correct Behavior

* Old activity → stored as history
* New activity → evaluated fresh
* Old data → used for comparison

---

## Repeat Offender Logic

If behavior repeats:

* Faster escalation
* Higher scoring
* Lower tolerance

---

# 12. Required Data Inputs

System must collect:

* Trade timestamps (ms precision)
* Tick data
* Bid/Ask history
* Spread history
* Order lifecycle
* Execution logs
* Reference market data
* Account linkage data
* Device/IP info

---

# 13. Account Fields

Each account must store:

* Severity
* Rule Tags
* Case Status
* Assigned Dealer
* Review Count
* Deducted Profit
* Last Review Date
* Last Action
* Monitoring Status

---

# 14. Case Entity Structure

Each case includes:

* Case ID
* Account ID
* Rule Engine
* Rule Handler
* Severity
* Status
* Assigned Dealer
* Action Taken
* Deduction Amount
* Evidence Snapshot
* Metric Snapshot

---

# 15. Audit Logging

Every action must be logged:

* Rule changes
* Score changes
* Dealer actions
* Case updates

Each log must include:

* User
* Timestamp
* Old value
* New value
* Action

---

# 16. System Summary

**The system is a configurable, weighted, multi-rule detection engine with structured case management, designed to identify, score, and handle abusive trading behavior while maintaining full auditability and post-review intelligence.**


