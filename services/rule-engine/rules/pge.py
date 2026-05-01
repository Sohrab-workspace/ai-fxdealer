"""Price Gap Exploitation (PGE) Rule Engine.

Detects traders opening positions to profit from price gaps at market open,
after news events, or around rollover windows — capturing guaranteed directional
movement with minimal risk.

Scoring model (total weights = 100):
  A — Gap Entry Timing     20  (positions opened during gap windows)
  B — Win Rate on Gaps     20  (profit rate specifically on gap-window trades)
  C — Short Duration       20  (holding period very short — in and out quickly)
  D — Volume Concentration 15  (large volume on gap trades vs normal trades)
  E — Directional Accuracy 15  (consistent correct direction on gap entries)
  F — Repetition           10  (recurring pattern across multiple gap events)
"""

from __future__ import annotations

from datetime import datetime, timezone, timedelta

import structlog
from sqlalchemy import text

from base_rule import BaseRule, MetricResult, RuleEvalResult

log = structlog.get_logger()

# Default gap windows (UTC hours) — market opens and typical news windows
_DEFAULT_GAP_WINDOWS = [
    (0, 1),    # midnight open (rollover gap)
    (7, 9),    # London open
    (13, 15),  # NY open
    (22, 24),  # Friday close / weekend gap reopen
]


class PGERule(BaseRule):
    """Price Gap Exploitation detection."""

    HANDLER = "PGE"

    METRIC_WEIGHTS = {
        "gap_entry_timing":     20,
        "win_rate_gap":         20,
        "short_duration":       20,
        "volume_concentration": 15,
        "directional_accuracy": 15,
        "repetition":           10,
    }

    def get_default_config(self) -> dict:
        return {
            "evaluation_window_hours": 168,
            "min_score_alert": 50,
            "min_deals": 10,
            "gap_windows_utc": _DEFAULT_GAP_WINDOWS,
            "short_duration_max_ms": 300_000,     # < 5 min = very short
            "min_gap_deals": 3,                   # minimum gap-window trades to score
            "win_rate_threshold": 0.75,           # 75%+ win rate on gaps
            "volume_concentration_threshold": 2.0, # gap trades 2× avg volume
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
                "SELECT symbol, direction, volume_lots, profit, swap, commission, "
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

        gap_windows = cfg["gap_windows_utc"]

        def _in_gap_window(deal_time_msc: int | None) -> bool:
            if not deal_time_msc:
                return False
            dt = datetime.fromtimestamp(deal_time_msc / 1000, tz=timezone.utc)
            for start_h, end_h in gap_windows:
                if start_h <= dt.hour < end_h:
                    return True
            return False

        gap_deals = [d for d in deals if _in_gap_window(d["deal_time_msc"])]
        non_gap_deals = [d for d in deals if not _in_gap_window(d["deal_time_msc"])]

        # ── A: Gap Entry Timing ────────────────────────────────────────────
        gap_ratio = len(gap_deals) / len(deals) if deals else 0.0
        min_gap = cfg["min_gap_deals"]
        if len(gap_deals) < min_gap:
            gap_timing_score = 0
        else:
            # 0% gap deals → 0, 50%+ → 100
            gap_timing_score = min(100, int(gap_ratio * 2 * 100))

        metrics.append(MetricResult(
            metric_group="A",
            metric_name="gap_entry_timing",
            metric_value=round(gap_ratio, 4),
            metric_score=gap_timing_score,
            weight=self.METRIC_WEIGHTS["gap_entry_timing"],
            detail={"gap_deals": len(gap_deals), "total_deals": len(deals)},
        ))

        # ── B: Win Rate on Gap Trades ──────────────────────────────────────
        if gap_deals:
            winning_gap = [d for d in gap_deals if (d["profit"] or 0) > 0]
            gap_win_rate = len(winning_gap) / len(gap_deals)
        else:
            gap_win_rate = 0.0

        threshold_b = cfg["win_rate_threshold"]
        if gap_win_rate < threshold_b or len(gap_deals) < min_gap:
            win_score = 0
        else:
            win_score = min(100, int((gap_win_rate - threshold_b) / (1.0 - threshold_b) * 100))

        metrics.append(MetricResult(
            metric_group="B",
            metric_name="win_rate_gap",
            metric_value=round(gap_win_rate, 4),
            metric_score=win_score,
            weight=self.METRIC_WEIGHTS["win_rate_gap"],
            detail={"winning_gap_deals": len(winning_gap) if gap_deals else 0},
        ))

        # ── C: Short Duration ──────────────────────────────────────────────
        max_short_ms = cfg["short_duration_max_ms"]
        short_gap_deals = [d for d in gap_deals if d["duration_ms"] and d["duration_ms"] < max_short_ms]
        short_ratio = len(short_gap_deals) / len(gap_deals) if gap_deals else 0.0
        # 0% short → 0, 80%+ → 100
        short_score = min(100, int(short_ratio * 1.25 * 100))

        avg_gap_duration = (
            sum(d["duration_ms"] for d in gap_deals if d["duration_ms"]) / len(gap_deals)
            if gap_deals else 0
        )

        metrics.append(MetricResult(
            metric_group="C",
            metric_name="short_duration",
            metric_value=round(short_ratio, 4),
            metric_score=short_score,
            weight=self.METRIC_WEIGHTS["short_duration"],
            detail={"short_gap_deals": len(short_gap_deals), "avg_gap_duration_ms": avg_gap_duration},
        ))

        # ── D: Volume Concentration ────────────────────────────────────────
        avg_gap_vol = (
            sum(d["volume_lots"] or 0 for d in gap_deals) / len(gap_deals) if gap_deals else 0
        )
        avg_non_gap_vol = (
            sum(d["volume_lots"] or 0 for d in non_gap_deals) / len(non_gap_deals)
            if non_gap_deals else avg_gap_vol
        )

        if avg_non_gap_vol > 0:
            vol_ratio = avg_gap_vol / avg_non_gap_vol
        else:
            vol_ratio = 1.0

        threshold_d = cfg["volume_concentration_threshold"]
        if vol_ratio < threshold_d or len(gap_deals) < min_gap:
            vol_score = 0
        else:
            vol_score = min(100, int((vol_ratio - threshold_d) / threshold_d * 100))

        metrics.append(MetricResult(
            metric_group="D",
            metric_name="volume_concentration",
            metric_value=round(vol_ratio, 3),
            metric_score=vol_score,
            weight=self.METRIC_WEIGHTS["volume_concentration"],
            detail={"avg_gap_lots": avg_gap_vol, "avg_normal_lots": avg_non_gap_vol},
        ))

        # ── E: Directional Accuracy ────────────────────────────────────────
        if gap_deals:
            correct_dir = [d for d in gap_deals if (d["profit"] or 0) > 0]
            dir_accuracy = len(correct_dir) / len(gap_deals)
            # 50% = random → 0, 90%+ → 100
            dir_score = max(0, min(100, int((dir_accuracy - 0.5) / 0.5 * 100)))
        else:
            dir_accuracy = 0.5
            dir_score = 0

        metrics.append(MetricResult(
            metric_group="E",
            metric_name="directional_accuracy",
            metric_value=round(dir_accuracy, 4),
            metric_score=dir_score,
            weight=self.METRIC_WEIGHTS["directional_accuracy"],
            detail={"correct_direction_deals": len(correct_dir) if gap_deals else 0},
        ))

        # ── F: Repetition ──────────────────────────────────────────────────
        gap_days = set()
        for d in gap_deals:
            if d["deal_time_msc"]:
                day = datetime.fromtimestamp(d["deal_time_msc"] / 1000, tz=timezone.utc).date()
                gap_days.add(day)

        repeat_days = len(gap_days)
        max_days = window_hours // 24
        repeat_score = min(100, int(repeat_days / max(max_days, 1) * 100))

        metrics.append(MetricResult(
            metric_group="F",
            metric_name="repetition",
            metric_value=float(repeat_days),
            metric_score=repeat_score,
            weight=self.METRIC_WEIGHTS["repetition"],
            detail={"gap_trading_days": repeat_days},
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
