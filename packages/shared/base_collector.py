from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID


class BaseCollector(ABC):
    """
    Abstract base class for all AI FXDealer collector services.

    Required metadata attributes (set in __init__ of each subclass):
        broker_id (UUID)       — tenant scope
        source_system (str)    — mt4 | mt5 | ctrader | fxbo | bridge | lp | news | calendar
        connection_id (UUID)   — unique connection identifier
        server_id (UUID)       — trading server identifier
        sync_mode (str)        — bootstrap | incremental
        cursor                 — last processed timestamp or ID
        last_success_at (datetime | None)
        status (str)           — connected | disconnected | error | syncing
    """

    @abstractmethod
    def connect(self) -> None:
        """Establish connection to source system."""
        pass

    @abstractmethod
    def health_check(self) -> dict:
        """Verify connection is alive. Return status dict."""
        pass

    @abstractmethod
    def bootstrap_sync(self, start_time=None, end_time=None) -> dict:
        """Full historical backfill for all entities."""
        pass

    @abstractmethod
    def incremental_sync(self, cursor=None) -> dict:
        """Ongoing collection from last known cursor."""
        pass

    @abstractmethod
    def fetch_entity(self, entity_name: str, **kwargs) -> list[dict]:
        """Fetch a specific entity from source. Returns raw dicts."""
        pass

    @abstractmethod
    def save_raw(self, entity_name: str, records: list[dict]) -> int:
        """Store raw records exactly as received. Returns count saved."""
        pass

    @abstractmethod
    def log_run(self, result: dict) -> None:
        """Write collector run result to raw_collector_runs."""
        pass

    @abstractmethod
    def handle_error(self, error: Exception, context: dict) -> None:
        """Handle and log error to raw_collector_errors."""
        pass
