"""Unit tests for MT5Collector.

All tests use mocked MT5Manager — no live server connection required.
"""

import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch, call

import pytest

# ── Patch path so collector modules are importable without uv install ──────────
_REPO = Path(__file__).parent.parent.parent
_PACKAGES = str(_REPO / "packages")
if _PACKAGES not in sys.path:
    sys.path.insert(0, _PACKAGES)
_SVC = str(_REPO / "services" / "collector-mt5")
if _SVC not in sys.path:
    sys.path.insert(0, _SVC)


# ── Fixtures ──────────────────────────────────────────────────────────────────

BROKER_ID    = uuid.UUID("00000000-0000-0000-0000-000000000001")
SERVER_ID    = uuid.UUID("00000000-0000-0000-0000-000000000002")
CONNECTION   = uuid.UUID("00000000-0000-0000-0000-000000000003")

MT5_CONFIG = {
    "server":   "192.0.2.1:443",
    "login":    1234,
    "password": "secret",
}


def _make_mt5_object(**kwargs):
    """Build a simple mock object with attribute access."""
    obj = MagicMock()
    for k, v in kwargs.items():
        setattr(obj, k, v)
    return obj


@pytest.fixture()
def mock_mt5manager(monkeypatch):
    """Monkeypatch MT5Manager in the collector module's namespace."""
    mt5_mod = MagicMock()

    manager_instance = MagicMock()
    mt5_mod.ManagerAPI.return_value = manager_instance
    # MT5Manager.Connect returns True on success (truthy), not 0
    manager_instance.Connect.return_value = True

    # Ensure collector module is imported first, then patch its MT5Manager reference
    import collector as coll_mod
    monkeypatch.setattr(coll_mod, "MT5Manager", mt5_mod)
    return mt5_mod, manager_instance


@pytest.fixture()
def mock_ingestion(monkeypatch):
    """Monkeypatch db.ingestion so tests don't need a real DB."""
    save_mock  = MagicMock(return_value=5)
    run_mock   = MagicMock()
    error_mock = MagicMock()

    import db.ingestion as ing
    monkeypatch.setattr(ing, "save_raw_records",   save_mock)
    monkeypatch.setattr(ing, "log_collector_run",   run_mock)
    monkeypatch.setattr(ing, "log_collector_error", error_mock)
    # Also patch on the already-imported collector module's namespace
    import collector as coll_mod
    monkeypatch.setattr(coll_mod, "save_raw_records",   save_mock)
    monkeypatch.setattr(coll_mod, "log_collector_run",   run_mock)
    monkeypatch.setattr(coll_mod, "log_collector_error", error_mock)

    return save_mock, run_mock, error_mock


@pytest.fixture()
def collector(mock_mt5manager, mock_ingestion):
    """Return a connected MT5Collector with all external calls mocked."""
    from collector import MT5Collector
    c = MT5Collector(
        broker_id=BROKER_ID,
        server_id=SERVER_ID,
        connection_id=CONNECTION,
        config=MT5_CONFIG,
    )
    c.connect()
    return c


# ── connect() tests ──────────────────────────────────────────────────────────

class TestConnect:
    def test_connect_creates_manager(self, mock_mt5manager, mock_ingestion):
        mt5_mod, manager_instance = mock_mt5manager
        from collector import MT5Collector
        c = MT5Collector(BROKER_ID, SERVER_ID, CONNECTION, MT5_CONFIG)
        c.connect()
        mt5_mod.ManagerAPI.assert_called_once()
        manager_instance.Connect.assert_called_once()

    def test_connect_sets_status(self, mock_mt5manager, mock_ingestion):
        _, manager_instance = mock_mt5manager
        from collector import MT5Collector
        c = MT5Collector(BROKER_ID, SERVER_ID, CONNECTION, MT5_CONFIG)
        c.connect()
        assert c.status == "connected"

    def test_connect_raises_on_auth_failure(self, mock_mt5manager, mock_ingestion):
        _, manager_instance = mock_mt5manager
        manager_instance.Connect.return_value = False  # falsy = error
        from collector import MT5Collector
        c = MT5Collector(BROKER_ID, SERVER_ID, CONNECTION, MT5_CONFIG)
        with pytest.raises(Exception):
            c.connect()


# ── health_check() tests ──────────────────────────────────────────────────────

class TestHealthCheck:
    def test_health_connected(self, collector):
        health = collector.health_check()
        assert health["status"] == "connected"

    def test_health_disconnected(self, mock_mt5manager, mock_ingestion):
        from collector import MT5Collector
        c = MT5Collector(BROKER_ID, SERVER_ID, CONNECTION, MT5_CONFIG)
        # Not connected — _manager is None
        health = c.health_check()
        assert health["status"] == "disconnected"


# ── fetch_entity() tests ──────────────────────────────────────────────────────

class TestFetchEntity:
    def _mock_user(self):
        return _make_mt5_object(Login=1001, Group="demo", Name="Test User",
                                Country="US", Balance=1000.0, Credit=0.0,
                                Leverage=100, Email="test@test.com",
                                Registration=1700000000, LastAccess=1700100000,
                                Enable=1, Rights=0)

    def _mock_deal(self):
        return _make_mt5_object(Deal=1, Login=1001, Symbol="EURUSD",
                                Volume=10000, Price=1.1000, TimeMsc=1700000000000,
                                Time=1700000000, Profit=10.0, Commission=-0.5,
                                Storage=0.0, Action=0, Entry=0,
                                PositionID=100, Order=200)

    def _mock_position(self):
        return _make_mt5_object(Position=100, Login=1001, Symbol="EURUSD",
                                Volume=10000, PriceOpen=1.1000,
                                PriceCurrent=1.1050, Profit=50.0,
                                Action=0, TimeMsc=1700000000000,
                                Time=1700000000, Storage=0.0,
                                Commission=-0.5)

    def test_fetch_accounts(self, collector):
        # _manager is the MagicMock manager_instance — all methods return MagicMock by default
        # Patch whatever user-request method collector calls for "accounts"
        collector._manager.UserRequestByGroup = MagicMock(return_value=[self._mock_user()])
        result = collector.fetch_entity("accounts")
        assert isinstance(result, list)

    def test_fetch_unknown_entity_raises(self, collector):
        with pytest.raises(ValueError, match="Unknown entity"):
            collector.fetch_entity("nonexistent")

    def test_fetch_returns_list(self, collector):
        collector._manager.UserRequestByGroup = MagicMock(return_value=[])
        result = collector.fetch_entity("accounts")
        assert isinstance(result, list)


# ── save_raw() tests ──────────────────────────────────────────────────────────

class TestSaveRaw:
    def test_save_raw_accounts_calls_ingestion(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        records = [{"Login": 1001, "Group": "demo", "Balance": 1000.0,
                    "Credit": 0.0, "Leverage": 100, "Name": "Test"}]
        collector.save_raw("accounts", records)
        save_mock.assert_called_once()
        table_arg = save_mock.call_args[0][0]
        assert table_arg == "raw_mt5_accounts"

    def test_save_raw_empty_returns_zero(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        result = collector.save_raw("accounts", [])
        assert result == 0
        save_mock.assert_not_called()

    def test_save_raw_deals_uses_correct_table(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        records = [{"Deal": 1, "Login": 1001, "Symbol": "EURUSD", "Price": 1.1,
                    "Volume": 10000, "Profit": 10.0, "TimeMsc": 1700000000000,
                    "Action": 0, "Entry": 0}]
        collector.save_raw("deals", records)
        table_arg = save_mock.call_args[0][0]
        assert table_arg == "raw_mt5_deals"

    def test_save_raw_unknown_entity_raises(self, collector, mock_ingestion):
        with pytest.raises(ValueError):
            collector.save_raw("unknown_entity", [{"x": 1}])


# ── log_run() and handle_error() tests ───────────────────────────────────────

class TestLogRun:
    def test_log_run_calls_ingestion(self, collector, mock_ingestion):
        _, run_mock, _ = mock_ingestion
        collector.log_run({
            "sync_mode": "incremental",
            "records_fetched": 10,
            "records_saved": 10,
            "duration_ms": 500,
        })
        run_mock.assert_called_once()
        args = run_mock.call_args[0][0]
        assert args["source_system"] == "mt5"
        assert args["broker_id"] == BROKER_ID

    def test_handle_error_calls_ingestion(self, collector, mock_ingestion):
        _, _, error_mock = mock_ingestion
        collector.handle_error(ValueError("test error"), {"entity": "deals"})
        error_mock.assert_called_once()
        args = error_mock.call_args[0][0]
        assert args["source_system"] == "mt5"
        assert "test error" in args["error_message"]


# ── bootstrap_sync() / incremental_sync() integration ────────────────────────

class TestSyncModes:
    def test_bootstrap_sync_returns_result(self, collector, mock_ingestion):
        save_mock, run_mock, _ = mock_ingestion
        # Patch fetch_entity to return empty lists (no live connection needed)
        with patch.object(collector, "fetch_entity", return_value=[]):
            result = collector.bootstrap_sync()
        assert "sync_mode" in result
        assert result["sync_mode"] == "bootstrap"
        assert "records_fetched" in result
        assert "duration_ms" in result
        run_mock.assert_called_once()

    def test_incremental_sync_returns_result(self, collector, mock_ingestion):
        save_mock, run_mock, _ = mock_ingestion
        with patch.object(collector, "fetch_entity", return_value=[]):
            result = collector.incremental_sync()
        assert result["sync_mode"] == "incremental"
        run_mock.assert_called_once()

    def test_bootstrap_updates_cursor(self, collector, mock_ingestion):
        with patch.object(collector, "fetch_entity", return_value=[]):
            collector.bootstrap_sync()
        assert collector.cursor is not None

    def test_entity_fetch_error_does_not_abort_sync(self, collector, mock_ingestion):
        """A single entity failure must not kill the whole bootstrap."""
        _, _, error_mock = mock_ingestion

        def _fail_sometimes(entity_name, **kwargs):
            if entity_name == "deals":
                raise RuntimeError("simulated DLL error")
            return []

        with patch.object(collector, "fetch_entity", side_effect=_fail_sometimes):
            result = collector.bootstrap_sync()
        # Should complete and log the error, not raise
        assert "sync_mode" in result
        error_mock.assert_called()
