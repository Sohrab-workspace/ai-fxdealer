"""Swap-Free Hedging Abuse (SFA) Rule Engine.

Detects traders exploiting swap-free grace periods by maintaining hedged
positions and cycling negative swap legs to accumulate positive swap income
while avoiding negative swap charges.

Scoring model (total weights = 100):
  A — Hedge Structure      20  (buy/sell volume balance)
  B — Leg Cycling          20  (repeated close+reopen of one direction)
  C — Rollover Timing      15  (closing near server rollover time)
  D — Swap Profit Dominance 20  (swap / total_profit ratio)
  E — Duration Asymmetry   10  (positive leg holds longer than negative)
  F — Repetition           10  (daily cycle count)
  G — Multi-Symbol          5  (same pattern across symbols)
"""

from __future__ import annotations

import math
from datetime import datetime, timezone, timedelta

import structlog
from sqlalchemy import text

from base_rule import BaseRule, MetricResult, RuleEvalResult, score_to_severity

log = structlog.get_logger()

# Rollover hour (UTC) — most MT5/MT4 servers roll at 00:00 EET = 22:00 UTC
_ROLLOVER_HOUR_UTC = 22
_ROLLOVER_WINDOW_MINUTES = 30  # close within 30 min before rollover = suspicious


class SFARule(BaseRule):
    """Swap-Free Hedging Abuse detection."""

    HANDLER = "SFA"

    METRIC_WEIGHTS = {
        "hedge_ratio":         20,
        "leg_cycling_score":   20,
        "rollover_timing":     15,
        "swap_dominance":      20,
        "duration_asymmetry":  10,
        "repetition":          10,
        "multi_symbol":         5,
    }

    def get_default_config(self) -> dict:
        return {
            "evaluation_window_hours": 168,      # 7-day lookback
            "min_score_alert": 50,
            "min_deals": 10,                     # minimum deals to evaluate
            "hedge_ratio_threshold": 0.90,       # hedge ratio above this = fully hedged
            "min_leg_cycles": 3,                 # minimum close+reopen cycles
            "swap_pnl_ratio_threshold": 0.60,    # swap > 60% of profit = suspicious
            "rollover_hour_utc": _ROLLOVER_HOUR_UTC,
            "rollover_window_minutes": _ROLLOVER_WINDOW_MINUTES,
            "min_symbols": 2,                    # multi-symbol threshold
        }

    def evaluate_account(
        self,
        source_account_id: str,
        broker_id: str,
        conn,
        config: dict,
    ) -> RuleEvalResult | None:
        cfg = self.merge_config(config)
        window_hours = cfg["evaluation_window_hours"]
        cutoff = datetime.now(timezone.utc) - timedelta(hours=window_hours)

        # ── Fetch deals from norm_deals within window ──────────────────────
        rows = conn.execute(
            text(
                "SELECT source_deal_id, symbol, direction, volume_lots, profit, "
                "swap, commission, open_time_msc, close_time_msc, deal_time_msc, "
                "duration_ms, deal_type "
                "FROM norm_deals "
                "WHERE broker_id = :broker_id "
                "  AND source_account_id = :account_id "
                "  AND deal_time >= :cutoff "
                "  AND deal_type = 'trade' "
                "  AND symbol IS NOT NULL AND symbol != '' "
                "ORDER BY deal_time_msc ASC"
            ),
            {
                "broker_id": broker_id,
                "account_id": source_account_id,
                "cutoff": cutoff,
            },
        ).mappings().fetchall()

        if len(rows) < cfg["min_deals"]:
            return None

        deals = [dict(r) for r in rows]

        # ── Fetch account info for login ───────────────────────────────────
        acct = conn.execute(
            text(
                "SELECT login, swap_free FROM norm_accounts "
                "WHERE broker_id = :broker_id AND source_account_id = :account_id "
                "AND status = 'active' LIMIT 1"
            ),
            {"broker_id": broker_id, "account_id": source_account_id},
        ).mappings().fetchone()

        login = acct["login"] if acct else None

        # Only target swap-free accounts (the whole exploit requires swap-free)
        if acct and acct["swap_free"] == 0:
            return None

        now = datetime.now(timezone.utc)
        evaluation_id = self.make_evaluation_id()
        metrics: list[MetricResult] = []

        # ── A: Hedge Structure (hedge_ratio) ───────────────────────────────
        symbols = set(d["symbol"] for d in deals)
        symbol_hedge_scores = []
        for sym in symbols:
            sym_deals = [d for d in deals if d["symbol"] == sym]
            buy_vol = sum(d["volume_lots"] or 0 for d in sym_deals if (d["direction"] or 0) == 0)
            sell_vol = sum(d["volume_lots"] or 0 for d in sym_deals if (d["direction"] or 0) == 1)
            total_vol = buy_vol + sell_vol
            if total_vol == 0:
                continue
            net_vol = abs(buy_vol - sell_vol)
            hedge_r = 1.0 - (net_vol / total_vol)
            symbol_hedge_scores.append(hedge_r)

        hedge_ratio = max(symbol_hedge_scores) if symbol_hedge_scores else 0.0
        threshold_a = cfg["hedge_ratio_threshold"]
        # Score 0 if below threshold, scales 0→100 from threshold→1.0
        if hedge_ratio < threshold_a:
            hedge_score = 0
        else:
            hedge_score = min(100, int((hedge_ratio - threshold_a) / (1.0 - threshold_a) * 100))

        metrics.append(MetricResult(
            metric_group="A",
            metric_name="hedge_ratio",
            metric_value=round(hedge_ratio, 4),
            metric_score=hedge_score,
            weight=self.METRIC_WEIGHTS["hedge_ratio"],
            detail={"buy_symbols": len([s for s in symbols]), "max_hedge_ratio": hedge_ratio},
        ))

        # ── B: Leg Cycling (close+reopen same direction same symbol) ───────
        cycle_count = 0
        for sym in symbols:
            sym_deals = sorted(
                [d for d in deals if d["symbol"] == sym],
                key=lambda d: d["deal_time_msc"] or 0,
            )
            # Count consecutive close then reopen of same direction within 60 min
            for i in range(1, len(sym_deals)):
                prev, curr = sym_deals[i - 1], sym_deals[i]
                if prev["direction"] == curr["direction"]:
                    gap_ms = (curr["deal_time_msc"] or 0) - (prev["deal_time_msc"] or 0)
                    if 0 < gap_ms < 3_600_000:  # within 1 hour
                        cycle_count += 1

        min_cycles = cfg["min_leg_cycles"]
        if cycle_count < min_cycles:
            cycling_score = 0
        else:
            # 3 cycles → 20 score, 10 cycles → 100
            cycling_score = min(100, int((cycle_count - min_cycles + 1) / (10 - min_cycles + 1) * 100))

        metrics.append(MetricResult(
            metric_group="B",
            metric_name="leg_cycling_score",
            metric_value=float(cycle_count),
            metric_score=cycling_score,
            weight=self.METRIC_WEIGHTS["leg_cycling_score"],
            detail={"cycle_count": cycle_count, "threshold": min_cycles},
        ))

        # ── C: Rollover Timing ─────────────────────────────────────────────
        rollover_h = cfg["rollover_hour_utc"]
        window_min = cfg["rollover_window_minutes"]
        rollover_closes = 0
        for d in deals:
            if d["close_time_msc"]:
                close_dt = datetime.fromtimestamp(d["close_time_msc"] / 1000, tz=timezone.utc)
                minutes_before_rollover = (
                    (rollover_h - close_dt.hour) * 60 - close_dt.minute
                ) % (24 * 60)
                if 0 < minutes_before_rollover <= window_min:
                    rollover_closes += 1

        total_closes = len([d for d in deals if d["close_time_msc"]])
        rollover_ratio = rollover_closes / total_closes if total_closes > 0 else 0.0
        # 0% rollover closes → 0, 20%+ → 100
        rollover_score = min(100, int(rollover_ratio * 5 * 100))

        metrics.append(MetricResult(
            metric_group="C",
            metric_name="rollover_timing",
            metric_value=round(rollover_ratio, 4),
            metric_score=rollover_score,
            weight=self.METRIC_WEIGHTS["rollover_timing"],
            detail={"rollover_closes": rollover_closes, "total_closes": total_closes},
        ))

        # ── D: Swap Profit Dominance ───────────────────────────────────────
        total_swap = sum((d["swap"] or 0) for d in deals)
        total_profit = sum((d["profit"] or 0) for d in deals)
        total_commission = sum((d["commission"] or 0) for d in deals)
        net_pnl = total_profit + total_swap + total_commission

        if net_pnl <= 0 or total_swap <= 0:
            swap_ratio = 0.0
            swap_score = 0
        else:
            swap_ratio = total_swap / net_pnl
            threshold_d = cfg["swap_pnl_ratio_threshold"]
            if swap_ratio < threshold_d:
                swap_score = 0
            else:
                swap_score = min(100, int((swap_ratio - threshold_d) / (1.0 - threshold_d) * 100))

        metrics.append(MetricResult(
            metric_group="D",
            metric_name="swap_dominance",
            metric_value=round(swap_ratio, 4),
            metric_score=swap_score,
            weight=self.METRIC_WEIGHTS["swap_dominance"],
            detail={"total_swap": total_swap, "total_profit": total_profit, "net_pnl": net_pnl},
        ))

        # ── E: Duration Asymmetry (positive legs held longer than negative) -
        buy_durations = [d["duration_ms"] for d in deals if (d["direction"] or 0) == 0 and d["duration_ms"]]
        sell_durations = [d["duration_ms"] for d in deals if (d["direction"] or 0) == 1 and d["duration_ms"]]

        if buy_durations and sell_durations:
            avg_buy = sum(buy_durations) / len(buy_durations)
            avg_sell = sum(sell_durations) / len(sell_durations)
            max_dur = max(avg_buy, avg_sell)
            min_dur = min(avg_buy, avg_sell)
            duration_ratio = max_dur / min_dur if min_dur > 0 else 1.0
            # ratio 1 (equal) → 0 score, ratio 5+ → 100
            asym_score = min(100, int((duration_ratio - 1.0) / 4.0 * 100))
        else:
            duration_ratio = 1.0
            asym_score = 0

        metrics.append(MetricResult(
            metric_group="E",
            metric_name="duration_asymmetry",
            metric_value=round(duration_ratio, 3),
            metric_score=asym_score,
            weight=self.METRIC_WEIGHTS["duration_asymmetry"],
            detail={"avg_buy_duration_ms": avg_buy if buy_durations else None,
                    "avg_sell_duration_ms": avg_sell if sell_durations else None},
        ))

        # ── F: Repetition (active days with cycles) ────────────────────────
        days_with_cycles = set()
        for sym in symbols:
            sym_deals = sorted(
                [d for d in deals if d["symbol"] == sym],
                key=lambda d: d["deal_time_msc"] or 0,
            )
            for i in range(1, len(sym_deals)):
                prev, curr = sym_deals[i - 1], sym_deals[i]
                if prev["direction"] == curr["direction"]:
                    gap_ms = (curr["deal_time_msc"] or 0) - (prev["deal_time_msc"] or 0)
                    if 0 < gap_ms < 3_600_000:
                        if curr["deal_time_msc"]:
                            day = datetime.fromtimestamp(
                                curr["deal_time_msc"] / 1000, tz=timezone.utc
                            ).date()
                            days_with_cycles.add(day)

        repeat_days = len(days_with_cycles)
        # 0 days → 0, 7+ days → 100 (within window_hours/24 possible days)
        max_possible_days = min(window_hours // 24, 30)
        repeat_score = min(100, int(repeat_days / max(max_possible_days, 1) * 100))

        metrics.append(MetricResult(
            metric_group="F",
            metric_name="repetition",
            metric_value=float(repeat_days),
            metric_score=repeat_score,
            weight=self.METRIC_WEIGHTS["repetition"],
            detail={"days_with_cycles": repeat_days, "window_days": max_possible_days},
        ))

        # ── G: Multi-Symbol ────────────────────────────────────────────────
        hedged_symbols = []
        for sym in symbols:
            sym_deals = [d for d in deals if d["symbol"] == sym]
            buy_vol = sum(d["volume_lots"] or 0 for d in sym_deals if (d["direction"] or 0) == 0)
            sell_vol = sum(d["volume_lots"] or 0 for d in sym_deals if (d["direction"] or 0) == 1)
            total_vol = buy_vol + sell_vol
            if total_vol > 0:
                net_vol = abs(buy_vol - sell_vol)
                if 1.0 - (net_vol / total_vol) >= cfg["hedge_ratio_threshold"]:
                    hedged_symbols.append(sym)

        symbol_count = len(hedged_symbols)
        min_syms = cfg["min_symbols"]
        if symbol_count < min_syms:
            multi_score = 0
        else:
            multi_score = min(100, int((symbol_count - min_syms + 1) / (5 - min_syms + 1) * 100))

        metrics.append(MetricResult(
            metric_group="G",
            metric_name="multi_symbol",
            metric_value=float(symbol_count),
            metric_score=multi_score,
            weight=self.METRIC_WEIGHTS["multi_symbol"],
            detail={"hedged_symbols": hedged_symbols},
        ))

        return RuleEvalResult(
            handler=self.HANDLER,
            broker_id=broker_id,
            source_account_id=source_account_id,
            login=login,
            evaluation_id=evaluation_id,
            metrics=metrics,
            evaluated_at=now,
        )
