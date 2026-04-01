"""FXBO Collector — Deferred pending live DB access.

FXBO uses a direct MySQL database connection (read-only replicator user).
The DB schema must be built from a live introspection of the source database —
per CLAUDE.md rule: "Do NOT design raw schemas from imagination."

Status: DEFERRED — MySQL port 3306 on 88.218.200.135 is not reachable from
this network. Schema cannot be designed until a live connection is established.

To activate:
1. Whitelist the collector host IP at the FXBO MySQL server firewall
2. Run: python -c "import pymysql; c=pymysql.connect(...); ..."
3. Capture all table names and column definitions
4. Design raw_fxbo_* table schemas from real column types
5. Create models in packages/db/models.py
6. Create Alembic migrations 0028+
7. Implement FXBOCollector methods below

Current class is a correctly-shaped stub that satisfies the BaseCollector
interface so ARQ workers can import it without crashing.
"""

from datetime import datetime, timezone
from uuid import UUID

import structlog

from shared.base_collector import BaseCollector
from db.ingestion import log_collector_error

log = structlog.get_logger()


class FXBOCollector(BaseCollector):
    """FXBO CRM collector — stub pending live DB access."""

    source_system = "fxbo"

    def __init__(
        self,
        broker_id: UUID,
        server_id: UUID | None,
        connection_id: UUID,
        config: dict,
    ):
        self.broker_id     = broker_id
        self.server_id     = server_id
        self.connection_id = connection_id
        self.config        = config
        self.sync_mode     = "incremental"
        self.cursor        = None
        self.last_success_at = None
        self.status        = "deferred"
        self._log = log.bind(broker_id=str(broker_id), source_system=self.source_system)

    def connect(self) -> None:
        raise NotImplementedError(
            "FXBOCollector is deferred. MySQL 88.218.200.135:3306 is not reachable. "
            "Whitelist collector host IP, then implement per CLAUDE.md rules."
        )

    def health_check(self) -> dict:
        return {"status": "deferred", "reason": "MySQL unreachable — see collector.py docstring"}

    def bootstrap_sync(self, start_time=None, end_time=None) -> dict:
        raise NotImplementedError("FXBOCollector is deferred.")

    def incremental_sync(self, cursor=None) -> dict:
        raise NotImplementedError("FXBOCollector is deferred.")

    def fetch_entity(self, entity_name: str, **kwargs) -> list[dict]:
        raise NotImplementedError("FXBOCollector is deferred.")

    def save_raw(self, entity_name: str, records: list[dict]) -> int:
        raise NotImplementedError("FXBOCollector is deferred.")

    def log_run(self, result: dict) -> None:
        pass

    def handle_error(self, error: Exception, context: dict) -> None:
        self._log.error("collector.fxbo.error", error=str(error))
        log_collector_error({
            "broker_id":     self.broker_id,
            "source_system": self.source_system,
            "connection_id": self.connection_id,
            "server_id":     self.server_id,
            "error_type":    type(error).__name__,
            "error_message": str(error),
            "context_json":  context,
            "collected_at":  datetime.now(timezone.utc),
        })
