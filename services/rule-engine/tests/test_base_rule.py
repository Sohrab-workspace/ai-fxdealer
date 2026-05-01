"""Unit tests for base rule engine framework."""

import pytest
from datetime import datetime, timezone

import sys
import os
# Add service root to path so base_rule is importable directly
_SERVICE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _SERVICE_ROOT not in sys.path:
    sys.path.insert(0, _SERVICE_ROOT)

from base_rule import (
    MetricResult,
    RuleEvalResult,
    score_to_severity,
    SEVERITY_BANDS,
)


class TestSeverityBands:
    def test_normal(self):
        assert score_to_severity(0) == "normal"
        assert score_to_severity(24) == "normal"

    def test_monitor(self):
        assert score_to_severity(25) == "monitor"
        assert score_to_severity(49) == "monitor"

    def test_suspicious(self):
        assert score_to_severity(50) == "suspicious"
        assert score_to_severity(69) == "suspicious"

    def test_abuse_candidate(self):
        assert score_to_severity(70) == "abuse_candidate"
        assert score_to_severity(100) == "abuse_candidate"


class TestMetricResult:
    def test_weighted_score(self):
        m = MetricResult(
            metric_group="A",
            metric_name="hedge_ratio",
            metric_value=0.95,
            metric_score=80,
            weight=20,
        )
        assert m.weighted_score == 16.0

    def test_weighted_score_zero_weight(self):
        m = MetricResult(
            metric_group="A",
            metric_name="test",
            metric_value=1.0,
            metric_score=100,
            weight=0,
        )
        assert m.weighted_score == 0.0


class TestRuleEvalResult:
    def _make_result(self, scores_and_weights) -> RuleEvalResult:
        metrics = []
        for group, name, value, score, weight in scores_and_weights:
            metrics.append(MetricResult(
                metric_group=group,
                metric_name=name,
                metric_value=value,
                metric_score=score,
                weight=weight,
            ))
        return RuleEvalResult(
            handler="TEST",
            broker_id="test-broker",
            source_account_id="12345",
            login=12345,
            evaluation_id="eval-001",
            metrics=metrics,
            evaluated_at=datetime.now(timezone.utc),
        )

    def test_total_score_zero(self):
        result = self._make_result([
            ("A", "m1", 0.0, 0, 50),
            ("B", "m2", 0.0, 0, 50),
        ])
        assert result.total_score == 0
        assert result.severity == "normal"

    def test_total_score_abuse(self):
        result = self._make_result([
            ("A", "hedge_ratio", 0.95, 100, 20),
            ("B", "leg_cycling", 8.0, 80, 20),
            ("C", "rollover", 0.3, 90, 15),
            ("D", "swap_dom", 0.9, 100, 20),
            ("E", "duration", 3.0, 60, 10),
            ("F", "repetition", 5.0, 70, 10),
            ("G", "multi_sym", 3.0, 60, 5),
        ])
        assert result.total_score > 70
        assert result.severity == "abuse_candidate"

    def test_score_breakdown_groups(self):
        result = self._make_result([
            ("A", "m1", 1.0, 100, 30),
            ("A", "m2", 1.0, 50, 20),
            ("B", "m3", 1.0, 80, 50),
        ])
        breakdown = result.score_breakdown
        assert "A" in breakdown
        assert "B" in breakdown
        # A: (100*30/100) + (50*20/100) = 30 + 10 = 40
        assert abs(breakdown["A"] - 40.0) < 0.01
        # B: (80*50/100) = 40
        assert abs(breakdown["B"] - 40.0) < 0.01

    def test_total_score_capped_at_100(self):
        result = self._make_result([
            ("A", "m1", 1.0, 100, 60),
            ("B", "m2", 1.0, 100, 60),  # weights sum > 100
        ])
        assert result.total_score <= 100
