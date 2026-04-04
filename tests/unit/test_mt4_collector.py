"""Unit tests for MT4Collector.

All tests use mocked ctypes DLL interface — no real DLL or server needed.
"""

import ctypes
import os
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock, patch, PropertyMock

import pytest

# ── Patch path so collector modules are importable without uv install ──────────
_REPO = Path(__file__).parent.parent.parent
# Add packages/ parent so `import shared` and `import db` resolve correctly
_PACKAGES = str(_REPO / "packages")
if _PACKAGES not in sys.path:
    sys.path.insert(0, _PACKAGES)
# Add collector-mt4 service dir so `import collector` and `import ctypes_wrapper` work
_SVC = str(_REPO / "services" / "collector-mt4")
if _SVC not in sys.path:
    sys.path.insert(0, _SVC)


# ── Fixtures ──────────────────────────────────────────────────────────────────

BROKER_ID  = uuid.UUID("00000000-0000-0000-0000-000000000011")
SERVER_ID  = uuid.UUID("00000000-0000-0000-0000-000000000012")
CONNECTION = uuid.UUID("00000000-0000-0000-0000-000000000013")

FAKE_DLL   = "C:\\fake\\mt4api.dll"


def _dummy_user_dict(**overrides) -> dict:
    base = {
        "login": 1001,
        "group": "demo",
        "password": "",
        "enable": 1,
        "enable_change_password": 0,
        "read_only": 0,
        "enable_otp": 0,
        "password_phone": "",
        "name": "Demo Trader",
        "country": "US",
        "city": "New York",
        "state": "",
        "zipcode": "",
        "address": "",
        "phone": "",
        "email": "demo@test.com",
        "comment": "",
        "id": "",
        "status": "",
        "regdate": 1700000000,
        "lastdate": 1700100000,
        "leverage": 100,
        "agent_account": 0,
        "timestamp": 1700100000,
        "balance": 10000.0,
        "prevmonthbalance": 9000.0,
        "prevbalance": 9000.0,
        "credit": 0.0,
        "interestrate": 0.0,
        "taxes": 0.0,
        "prevmonthequity": 9000.0,
        "prevequity": 9000.0,
        "publickey": "",
    }
    base.update(overrides)
    return base


def _dummy_trade_dict(close_time: int = 0, **overrides) -> dict:
    base = {
        "order": 5001,
        "login": 1001,
        "symbol": "EURUSD",
        "digits": 5,
        "cmd": 0,         # BUY
        "volume": 100,    # 1.00 lot
        "open_time": 1700000000,
        "state": 1,
        "open_price": 1.10000,
        "sl": 0.0,
        "tp": 0.0,
        "close_time": close_time,
        "value_date": 0,
        "expiration": 0,
        "reason": "\x00",
        "conv_rate1": 1.0,
        "conv_rate2": 1.0,
        "commission": -2.0,
        "commission_agent": 0.0,
        "storage": -0.5,
        "close_price": 1.10500,
        "profit": 50.0,
        "taxes": 0.0,
        "magic": 12345,
        "comment": "EA signal",
        "activation": 0,
        "gw_volume": 0,
        "gw_open_price": 0.0,
        "gw_close_price": 0.0,
        "margin_rate": 1.0,
        "timestamp": 1700000100,
        "internal_id": 0,
    }
    base.update(overrides)
    return base


def _dummy_online_dict(**overrides) -> dict:
    # Matches actual OnlineRecord: counter, reserved, login, ip, group
    base = {
        "counter": 1,
        "reserved": 0,
        "login": 1001,
        "ip": 167772161,   # 10.0.0.1 packed
        "group": "demo",
    }
    base.update(overrides)
    return base


@pytest.fixture()
def mock_mt4manager():
    """Return a mocked MT4Manager with preset return values."""
    with patch("collector.MT4Manager") as MockCls:
        instance = MagicMock()
        MockCls.create.return_value = instance
        instance.get_users_by_group.return_value = [_dummy_user_dict()]
        instance.get_trades_by_group.return_value = [_dummy_trade_dict(close_time=0)]
        instance.get_history_by_group.return_value = [_dummy_trade_dict(close_time=1700200000)]
        instance.get_online.return_value = [_dummy_online_dict()]
        instance.get_symbols.return_value = []
        instance.get_margin_levels.return_value = []
        instance.get_summary.return_value = []
        yield MockCls, instance


@pytest.fixture()
def mock_ingestion(monkeypatch):
    """Mock db.ingestion so no real DB is needed."""
    save_mock  = MagicMock(return_value=3)
    run_mock   = MagicMock()
    error_mock = MagicMock()

    import db.ingestion as ing
    import collector as coll_mod
    monkeypatch.setattr(ing, "save_raw_records",    save_mock)
    monkeypatch.setattr(ing, "log_collector_run",    run_mock)
    monkeypatch.setattr(ing, "log_collector_error",  error_mock)
    # Also patch on the already-imported collector module's namespace
    monkeypatch.setattr(coll_mod, "save_raw_records",   save_mock)
    monkeypatch.setattr(coll_mod, "log_collector_run",   run_mock)
    monkeypatch.setattr(coll_mod, "log_collector_error", error_mock)
    return save_mock, run_mock, error_mock


@pytest.fixture()
def collector(mock_mt4manager, mock_ingestion):
    from collector import MT4Collector
    config = {
        "dll_path": FAKE_DLL,
        "server":   "192.0.2.1:443",
        "login":    52,
        "password": "secret",
    }
    c = MT4Collector(BROKER_ID, SERVER_ID, CONNECTION, config)
    with patch("os.path.exists", return_value=True):
        c.connect()
    return c


# ── MT4Manager unit tests ─────────────────────────────────────────────────────

class TestMT4ManagerCreate:
    def test_create_raises_if_dll_missing(self):
        from ctypes_wrapper import MT4Manager
        with pytest.raises(FileNotFoundError):
            MT4Manager.create("/nonexistent/path/mt4.dll", "host", 1, "pass")

    def test_create_returns_instance(self, tmp_path):
        fake_dll = tmp_path / "mt4.dll"
        fake_dll.write_bytes(b"\x00" * 64)  # create a dummy file
        from ctypes_wrapper import MT4Manager
        mgr = MT4Manager.create(str(fake_dll), "host:443", 1, "pass")
        assert isinstance(mgr, MT4Manager)
        assert mgr.server == "host:443"
        assert mgr.login == 1


class TestStructToDict:
    def test_user_record_to_dict(self):
        from ctypes_wrapper import UserRecord, struct_to_dict
        rec = UserRecord()
        rec.login = 1001
        rec.balance = 5000.0
        rec.leverage = 100
        rec.group = b"demo"
        d = struct_to_dict(rec)
        assert d["login"] == 1001
        assert d["balance"] == 5000.0
        assert d["group"] == "demo"

    def test_trade_record_to_dict(self):
        from ctypes_wrapper import TradeRecord, struct_to_dict
        rec = TradeRecord()
        rec.order = 9001
        rec.login = 1001
        rec.symbol = b"EURUSD"
        rec.close_time = 0   # open order
        rec.open_price = 1.10000
        rec.profit = 55.0
        d = struct_to_dict(rec)
        assert d["order"] == 9001
        assert d["symbol"] == "EURUSD"
        assert d["close_time"] == 0

    def test_online_record_to_dict(self):
        from ctypes_wrapper import OnlineRecord, struct_to_dict
        rec = OnlineRecord()
        rec.counter = 3
        rec.login = 1001
        rec.ip = 167772161
        rec.group = b"demo"
        d = struct_to_dict(rec)
        assert d["login"] == 1001
        assert d["ip"] == 167772161
        assert d["group"] == "demo"
        assert d["counter"] == 3


class TestUnpackIp:
    def test_unpack_known_ip(self):
        from ctypes_wrapper import unpack_ip
        # 10.0.0.1 in big-endian = 0x0A000001 = 167772161
        assert unpack_ip(167772161) == "10.0.0.1"

    def test_unpack_zero(self):
        from ctypes_wrapper import unpack_ip
        result = unpack_ip(0)
        assert result == "0.0.0.0"


class TestStructSizes:
    """Verify ctypes struct sizes match MT4ManagerAPI.h values."""

    def test_user_record_size(self):
        from ctypes_wrapper import UserRecord
        assert ctypes.sizeof(UserRecord) == 1120

    def test_trade_record_size(self):
        from ctypes_wrapper import TradeRecord
        assert ctypes.sizeof(TradeRecord) == 224

    def test_online_record_size(self):
        from ctypes_wrapper import OnlineRecord
        assert ctypes.sizeof(OnlineRecord) == 32


# ── MT4Collector tests ────────────────────────────────────────────────────────

class TestConnect:
    def test_connect_calls_mt4manager_create(self, mock_mt4manager, mock_ingestion):
        MockCls, _ = mock_mt4manager
        from collector import MT4Collector
        config = {"dll_path": FAKE_DLL, "server": "192.0.2.1:443",
                  "login": 52, "password": "secret"}
        c = MT4Collector(BROKER_ID, SERVER_ID, CONNECTION, config)
        with patch("os.path.exists", return_value=True):
            c.connect()
        MockCls.create.assert_called_once_with(
            dll_path=FAKE_DLL,
            server="192.0.2.1:443",
            login=52,
            password="secret",
        )

    def test_connect_sets_connected_status(self, mock_mt4manager, mock_ingestion):
        from collector import MT4Collector
        config = {"dll_path": FAKE_DLL, "server": "192.0.2.1:443",
                  "login": 52, "password": "secret"}
        c = MT4Collector(BROKER_ID, SERVER_ID, CONNECTION, config)
        with patch("os.path.exists", return_value=True):
            c.connect()
        assert c.status == "connected"

    def test_connect_raises_without_dll_path(self, mock_mt4manager, mock_ingestion):
        from collector import MT4Collector
        config = {"server": "192.0.2.1:443", "login": 52, "password": "secret"}
        c = MT4Collector(BROKER_ID, SERVER_ID, CONNECTION, config)
        with pytest.raises(ValueError, match="dll_path"):
            c.connect()


class TestHealthCheck:
    def test_health_connected(self, collector):
        health = collector.health_check()
        assert health["status"] == "connected"

    def test_health_disconnected(self, mock_mt4manager, mock_ingestion):
        from collector import MT4Collector
        config = {"dll_path": FAKE_DLL, "server": "host", "login": 1, "password": "x"}
        c = MT4Collector(BROKER_ID, SERVER_ID, CONNECTION, config)
        health = c.health_check()
        assert health["status"] == "disconnected"


class TestFetchEntity:
    def test_fetch_accounts(self, collector):
        result = collector.fetch_entity("accounts")
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["login"] == 1001

    def test_fetch_orders_filters_open(self, collector):
        result = collector.fetch_entity("orders")
        assert isinstance(result, list)
        # Only close_time==0 records returned
        for r in result:
            assert r.get("close_time", 0) == 0

    def test_fetch_deals_filters_closed(self, collector):
        now = 1700300000
        result = collector.fetch_entity("deals",
                                         from_ts=1700000000,
                                         to_ts=now)
        assert isinstance(result, list)
        for r in result:
            assert r.get("close_time", 0) > 0

    def test_fetch_online(self, collector):
        result = collector.fetch_entity("online")
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["login"] == 1001

    def test_fetch_unknown_raises(self, collector):
        with pytest.raises(ValueError, match="Unknown entity"):
            collector.fetch_entity("unknown_thing")

    def test_fetch_raises_if_not_connected(self, mock_mt4manager, mock_ingestion):
        from collector import MT4Collector
        config = {"dll_path": FAKE_DLL, "server": "host", "login": 1, "password": "x"}
        c = MT4Collector(BROKER_ID, SERVER_ID, CONNECTION, config)
        with pytest.raises(RuntimeError, match="Not connected"):
            c.fetch_entity("accounts")


class TestSaveRaw:
    def test_save_raw_accounts(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        records = [_dummy_user_dict()]
        collector.save_raw("accounts", records)
        save_mock.assert_called_once()
        assert save_mock.call_args[0][0] == "raw_mt4_accounts"

    def test_save_raw_orders(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        collector.save_raw("orders", [_dummy_trade_dict(close_time=0)])
        assert save_mock.call_args[0][0] == "raw_mt4_orders"

    def test_save_raw_deals(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        collector.save_raw("deals", [_dummy_trade_dict(close_time=1700200000)])
        assert save_mock.call_args[0][0] == "raw_mt4_deals"

    def test_save_raw_online(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        collector.save_raw("online", [_dummy_online_dict()])
        assert save_mock.call_args[0][0] == "raw_mt4_online"

    def test_save_raw_empty_returns_zero(self, collector, mock_ingestion):
        save_mock, _, _ = mock_ingestion
        result = collector.save_raw("accounts", [])
        assert result == 0
        save_mock.assert_not_called()


class TestLogRun:
    def test_log_run_calls_ingestion(self, collector, mock_ingestion):
        _, run_mock, _ = mock_ingestion
        collector.log_run({"sync_mode": "incremental",
                           "records_fetched": 10, "records_saved": 10,
                           "duration_ms": 250})
        run_mock.assert_called_once()
        args = run_mock.call_args[0][0]
        assert args["source_system"] == "mt4"
        assert args["broker_id"] == BROKER_ID

    def test_handle_error_logs(self, collector, mock_ingestion):
        _, _, error_mock = mock_ingestion
        collector.handle_error(RuntimeError("DLL crash"), {"entity": "accounts"})
        error_mock.assert_called_once()
        args = error_mock.call_args[0][0]
        assert "DLL crash" in args["error_message"]


class TestSyncModes:
    def test_bootstrap_sync_completes(self, collector, mock_ingestion):
        _, run_mock, _ = mock_ingestion
        result = collector.bootstrap_sync()
        assert result["sync_mode"] == "bootstrap"
        assert "records_fetched" in result
        assert "duration_ms" in result
        run_mock.assert_called_once()

    def test_incremental_sync_completes(self, collector, mock_ingestion):
        _, run_mock, _ = mock_ingestion
        result = collector.incremental_sync()
        assert result["sync_mode"] == "incremental"
        run_mock.assert_called_once()

    def test_bootstrap_updates_cursor(self, collector, mock_ingestion):
        assert collector.cursor is None
        collector.bootstrap_sync()
        assert collector.cursor is not None

    def test_fetch_error_continues_sync(self, collector, mock_ingestion):
        """Error in one entity must not abort the whole bootstrap_sync."""
        _, _, error_mock = mock_ingestion
        original = collector.fetch_entity

        call_count = {"n": 0}

        def _sometimes_fail(entity, **kwargs):
            call_count["n"] += 1
            if entity == "accounts":
                raise RuntimeError("simulated DLL failure")
            return []

        collector.fetch_entity = _sometimes_fail
        result = collector.bootstrap_sync()
        assert "sync_mode" in result
        error_mock.assert_called()
        assert call_count["n"] > 1


# ── Field extraction tests ────────────────────────────────────────────────────

class TestExtractMt4Fields:
    """Verify _extract_mt4_fields maps to correct DB column names."""

    def test_accounts_uses_group_name(self):
        from collector import _extract_mt4_fields
        rec = _dummy_user_dict(group="demo")
        result = _extract_mt4_fields("accounts", rec)
        assert "group_name" in result
        assert result["group_name"] == "demo"
        assert "group" not in result

    def test_accounts_regdate_as_int(self):
        from collector import _extract_mt4_fields
        rec = _dummy_user_dict(regdate=1700000000)
        result = _extract_mt4_fields("accounts", rec)
        # regdate should be BigInteger (int), not datetime
        assert isinstance(result["regdate"], int)

    def test_orders_open_time_as_int(self):
        from collector import _extract_mt4_fields
        rec = _dummy_trade_dict(close_time=0, open_time=1700000000)
        result = _extract_mt4_fields("orders", rec)
        assert isinstance(result["open_time"], int)
        assert result["order_id"] == rec["order"]

    def test_deals_close_time_as_int(self):
        from collector import _extract_mt4_fields
        rec = _dummy_trade_dict(close_time=1700200000)
        result = _extract_mt4_fields("deals", rec)
        assert isinstance(result["close_time"], int)
        assert result["close_time"] == 1700200000

    def test_online_has_group_name(self):
        from collector import _extract_mt4_fields
        rec = _dummy_online_dict()
        rec["group"] = "demo"
        result = _extract_mt4_fields("online", rec)
        assert "group_name" in result
        assert "login" in result
        assert "ip" in result

    def test_online_maps_group_to_group_name(self):
        from collector import _extract_mt4_fields
        rec = _dummy_online_dict()
        rec["group"] = "real"
        result = _extract_mt4_fields("online", rec)
        assert result["group_name"] == "real"

    def test_deals_reason_converted_to_int(self):
        from collector import _extract_mt4_fields
        rec = _dummy_trade_dict(close_time=1700200000, reason="\x03")
        result = _extract_mt4_fields("deals", rec)
        # reason should be integer (close reason code)
        assert result["reason"] in (None, 3)  # \x03 = 3
