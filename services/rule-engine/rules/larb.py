"""Latency Arbitrage (LARB) Rule Engine.

Detects traders exploiting price feed latency between the broker's feed
and a reference market price, entering positions moments after the true
market has moved but before the broker's platform reflects the new price.

Scoring model (total weights = 100):
  A — Short Entry Duration      20  (very short holding period before exit)
  B — Win Rate                  20  (abnormally high win rate)
  C — Consistent Profitability  15  (profit across many instruments/sessions)
  D — Trade Timing Pattern      20  (trades during high-latency windows)
  E — Volume Concentration      10  (large lots on profitable trades)
  F — Repetition                10  (consistent pattern over time)
  G — Multi-Instrument           5  (same pattern across many symbols)
"""

from __future__ import annotations

from datetime import datetime, timezone, timedelta
from statistics import stdev

import structlog
from sqlalchemy import text

from base_rule import BaseRule, MetricResult, RuleEvalResult

log = structlog.get_logger()


class LARBRule(BaseRule):
    """Latency Arbitrage detection."""

    HANDLER = "LARB"

    METRIC_WEIGHTS = {
        "short_entry_duration": 20,
        "win_rate":             20,
        "consistent_profit":    15,
        "timing_pattern":       20,
        "volume_concentration": 10,
        "repetition":           10,
        "multi_instrument":      5,
    }

    def get_default_config(self) -> dict:
        return {
            "evaluation_window_hours": 168,
            "min_score_alert": 50,
            "min_deals": 15,
            "short_duration_max_ms": 60_000,          # < 60 seconds = very short
            "win_rate_threshold": 0.70,                # 70%+ win rate
            "min_profitable_symbols": 3,               # symbols with consistent profit
            "high_latency_hours_utc": [(0, 2), (7, 9), (13, 16)],  # market open windows
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

        rows = conn.execute(
            text(
                "SELECT symbol, direction, volume_lots, profit, "
                "open_time_msc, close_time_msc, deal_time_msc, duration_ms "
                "FROM norm_deals "
                "WHERE broker_id = :broker_id AND source_account_id = :account_id "
                "AND deal_time >= :cutoff AND deal_type = 'trade' "
                "AND symbol IS NOT NULL AND symbol != '' "
                "ORDER BY deal_time_msc ASC"
            ),
            {"broker_id": broker_id, "account_id": source_account_id, "cutoff": cutoff},
        ).mappings().fetchall()

        if len(rows) < cfg["min_deals"]:
            return None

        acct = conn.execute(
            text(
                "SELECT login FROM norm_accounts WHERE broker_id = :broker_id "
                "AND source_account_id = :account_id AND status = 'active' LIMIT 1"
            ),
            {"broker_id": broker_id, "account_id": source_account_id},
        ).mappings().fetchone()
        login = acct["login"] if acct else None

        deals = [dict(r) for r in rows]
        now = datetime.now(timezone.utc)
        evaluation_id = self.make_evaluation_id()
        metrics: list[MetricResult] = []

        # ── A: Short Entry Duration ────────────────────────────────────────
        max_short_ms = cfg["short_duration_max_ms"]
        durations = [d["duration_ms"] for d in deals if d["duration_ms"] is not None]
        short_trades = [d for d in deals if d["duration_ms"] and d["duration_ms"] < max_short_ms]
        short_ratio = len(short_trades) / len(deals) if deals else 0.0

        # 0% short → 0, 60%+ → 100
        short_score = min(100, int(short_ratio / 0.6 * 100))
        avg_duration = sum(durations) / len(durations) if durations else 0

        metrics.append(MetricResult(
            metric_group="A",
            metric_name="short_entry_duration",
            metric_value=round(short_ratio, 4),
            metric_score=short_score,
            weight=self.METRIC_WEIGHTS["short_entry_duration"],
            detail={"short_trades": len(short_trades), "avg_duration_ms": avg_duration},
        ))

        # ── B: Win Rate ────────────────────────────────────────────────────
        winning = [d for d in deals if (d["profit"] or 0) > 0]
        win_rate = len(winning) / len(deals) if deals else 0.0
        threshold_b = cfg["win_rate_threshold"]

        if win_rate < threshold_b:
            win_score = 0
        else:
            win_score = min(100, int((win_rate - threshold_b) / (1.0 - threshold_b) * 100))

        metrics.append(MetricResult(
            metric_group="B",
            metric_name="win_rate",
            metric_value=round(win_rate, 4),
            metric_score=win_score,
            weight=self.METRIC_WEIGHTS["win_rate"],
            detail={"winning_trades": len(winning), "total_trades": len(deals)},
        ))

        # ── C: Consistent Profitability ────────────────────────────────────
        symbols = set(d["symbol"] for d in deals)
        profitable_symbols = []
        for sym in symbols:
            sym_deals = [d for d in deals if d["symbol"] == sym]
            if len(sym_deals) < 3:
                continue
            sym_wins = [d for d in sym_deals if (d["profit"] or 0) > 0]
            if len(sym_wins) / len(sym_deals) >= threshold_b:
                profitable_symbols.append(sym)

        min_profit_syms = cfg["min_profitable_symbols"]
        if len(profitable_symbols) < min_profit_syms:
            consistent_score = 0
        else:
            consistent_score = min(100, int(len(profitable_symbols) / (min_profit_syms + 3) * 100))

        metrics.append(MetricResult(
            metric_group="C",
            metric_name="consistent_profit",
            metric_value=float(len(profitable_symbols)),
            metric_score=consistent_score,
            weight=self.METRIC_WEIGHTS["consistent_profit"],
            detail={"profitable_symbols": profitable_symbols},
        ))

        # ── D: Trade Timing Pattern ────────────────────────────────────────
        high_latency_windows = cfg["high_latency_hours_utc"]

        def _in_latency_window(deal_time_msc: int | None) -> bool:
            if not deal_time_msc:
                return False
            dt = datetime.fromtimestamp(deal_time_msc / 1000, tz=timezone.utc)
            for start_h, end_h in high_latency_windows:
                if start_h <= dt.hour < end_h:
                    return True
            return False

        latency_window_deals = [d for d in deals if _in_latency_window(d["deal_time_msc"])]
        latency_ratio = len(latency_window_deals) / len(deals) if deals else 0.0
        # 0% → 0, 50%+ → 100
        timing_score = min(100, int(latency_ratio * 2 * 100))

        metrics.append(MetricResult(
            metric_group="D",
            metric_name="timing_pattern",
            metric_value=round(latency_ratio, 4),
            metric_score=timing_score,
            weight=self.METRIC_WEIGHTS["timing_pattern"],
            detail={"latency_window_deals": len(latency_window_deals)},
        ))

        # ── E: Volume Concentration on winning trades ──────────────────────
        losing = [d for d in deals if (d["profit"] or 0) <= 0]
        avg_win_vol = (
            sum(d["volume_lots"] or 0 for d in winning) / len(winning) if winning else 0
        )
        avg_lose_vol = (
            sum(d["volume_lots"] or 0 for d in losing) / len(losing) if losing else avg_win_vol
        )

        if avg_lose_vol > 0:
            vol_ratio = avg_win_vol / avg_lose_vol
        else:
            vol_ratio = 1.0

        # ratio 1 → 0, ratio 3+ → 100
        vol_score = min(100, int((vol_ratio - 1.0) / 2.0 * 100))

        metrics.append(MetricResult(
            metric_group="E",
            metric_name="volume_concentration",
            metric_value=round(vol_ratio, 3),
            metric_score=max(0, vol_score),
            weight=self.METRIC_WEIGHTS["volume_concentration"],
            detail={"avg_win_lots": avg_win_vol, "avg_lose_lots": avg_lose_vol},
        ))

        # ── F: Repetition ──────────────────────────────────────────────────
        active_days = set()
        for d in deals:
            if d["deal_time_msc"] and d["duration_ms"] and d["duration_ms"] < max_short_ms:
                day = datetime.fromtimestamp(d["deal_time_msc"] / 1000, tz=timezone.utc).date()
                active_days.add(day)

        repeat_days = len(active_days)
        max_days = window_hours // 24
        repeat_score = min(100, int(repeat_days / max(max_days, 1) * 100))

        metrics.append(MetricResult(
            metric_group="F",
            metric_name="repetition",
            metric_value=float(repeat_days),
            metric_score=repeat_score,
            weight=self.METRIC_WEIGHTS["repetition"],
            detail={"active_days": repeat_days},
        ))

        # ── G: Multi-Instrument ────────────────────────────────────────────
        symbol_count = len(symbols)
        min_profit_syms = cfg["min_profitable_symbols"]
        if symbol_count < min_profit_syms:
            multi_score = 0
        else:
            multi_score = min(100, int(symbol_count / (min_profit_syms + 5) * 100))

        metrics.append(MetricResult(
            metric_group="G",
            metric_name="multi_instrument",
            metric_value=float(symbol_count),
            metric_score=multi_score,
            weight=self.METRIC_WEIGHTS["multi_instrument"],
            detail={"symbols_traded": list(symbols)},
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
