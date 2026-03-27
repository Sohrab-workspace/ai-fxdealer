import uuid

from sqlalchemy import (
    BigInteger,
    Column,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Broker(Base):
    __tablename__ = "brokers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True)  # subdomain identifier: broker-name.fxdealer.com
    status = Column(String, nullable=False, server_default="active")  # active | archived
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    servers = relationship("BrokerServer", back_populates="broker")
    users = relationship("BrokerUser", back_populates="broker")


class BrokerServer(Base):
    """A trading server connection belonging to a broker."""

    __tablename__ = "broker_servers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), ForeignKey("brokers.id"), nullable=False)
    name = Column(String, nullable=False)
    source_system = Column(String, nullable=False)  # mt4 | mt5 | ctrader
    host = Column(String)
    port = Column(Integer)
    status = Column(String, nullable=False, server_default="active")  # active | archived
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    broker = relationship("Broker", back_populates="servers")

    __table_args__ = (
        Index("ix_broker_servers_broker_id", "broker_id"),
    )


class BrokerUser(Base):
    """A user account scoped to a specific broker tenant."""

    __tablename__ = "broker_users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), ForeignKey("brokers.id"), nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    broker = relationship("Broker", back_populates="users")
    user_broker_roles = relationship(
        "UserBrokerRole",
        back_populates="user",
        foreign_keys="UserBrokerRole.user_id",
    )

    __table_args__ = (
        UniqueConstraint("broker_id", "email", name="uq_broker_users_broker_email"),
        Index("ix_broker_users_broker_id", "broker_id"),
    )


class Role(Base):
    """Platform roles: admin, dealer, readonly."""

    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)  # admin | dealer | readonly
    description = Column(String)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    user_broker_roles = relationship("UserBrokerRole", back_populates="role")


class UserBrokerRole(Base):
    """
    Junction table: assigns a role to a user within a specific broker tenant.
    A user can hold different roles across different brokers.
    """

    __tablename__ = "user_broker_roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("broker_users.id"), nullable=False)
    broker_id = Column(UUID(as_uuid=True), ForeignKey("brokers.id"), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"), nullable=False)
    assigned_by = Column(UUID(as_uuid=True), ForeignKey("broker_users.id"))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    user = relationship("BrokerUser", back_populates="user_broker_roles", foreign_keys=[user_id])
    role = relationship("Role", back_populates="user_broker_roles")
    assigner = relationship("BrokerUser", foreign_keys=[assigned_by])

    __table_args__ = (
        UniqueConstraint("user_id", "broker_id", "role_id", name="uq_user_broker_roles"),
        Index("ix_user_broker_roles_broker_id", "broker_id"),
        Index("ix_user_broker_roles_user_id", "user_id"),
    )


class AuditLog(Base):
    """
    Immutable audit trail of all actions taken within the platform.

    Rules (from CLAUDE.md):
    - No soft delete, no archive, no modification — ever
    - broker_id and actor_id are stored as bare UUIDs (no FK constraint)
      so the log survives user or broker deletion
    - All action attempts are logged including rejected ones
    """

    __tablename__ = "audit_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)   # no FK — survives tenant deletion
    actor_id = Column(UUID(as_uuid=True), nullable=False)    # no FK — survives user deletion
    action = Column(String, nullable=False)                  # e.g. "account.restrict", "rule.update"
    resource_type = Column(String, nullable=False)           # e.g. "account", "rule", "user"
    resource_id = Column(String)                             # external or internal ID of affected resource
    detail_json = Column(JSONB)                              # action payload, before/after state, evidence refs
    ip_address = Column(String)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    __table_args__ = (
        Index("ix_audit_logs_broker_id", "broker_id"),
        Index("ix_audit_logs_actor_id", "actor_id"),
        Index("ix_audit_logs_broker_resource", "broker_id", "resource_type", "resource_id"),
    )


class BrokerCrmConnection(Base):
    """
    A CRM system connection belonging to a broker.

    Credentials are stored in AWS Secrets Manager — not here.
    Only non-secret config (host, crm_type, secret reference key) lives in this table.
    """

    __tablename__ = "broker_crm_connections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), ForeignKey("brokers.id"), nullable=False)
    name = Column(String, nullable=False)
    crm_type = Column(String, nullable=False)          # fxbo | other
    host = Column(String)                              # CRM API base URL or host
    secret_key_ref = Column(String)                   # AWS Secrets Manager key name (not the secret itself)
    status = Column(String, nullable=False, server_default="active")  # active | archived
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    broker = relationship("Broker")

    __table_args__ = (
        Index("ix_broker_crm_connections_broker_id", "broker_id"),
    )


class BrokerIntegration(Base):
    """
    A third-party integration connection belonging to a broker.

    Covers bridge providers, LP connections, notification connectors, and similar.
    Credentials are stored in AWS Secrets Manager — not here.
    Non-secret config stored in config_json.
    """

    __tablename__ = "broker_integrations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), ForeignKey("brokers.id"), nullable=False)
    name = Column(String, nullable=False)
    integration_type = Column(String, nullable=False)  # bridge | lp | notification | market_data | other
    config_json = Column(JSONB)                        # non-secret config (host, port, timeouts, etc.)
    secret_key_ref = Column(String)                   # AWS Secrets Manager key name (not the secret itself)
    status = Column(String, nullable=False, server_default="active")  # active | archived
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    broker = relationship("Broker")

    __table_args__ = (
        Index("ix_broker_integrations_broker_id", "broker_id"),
    )


class RawMT5Deal(Base):
    """
    Raw MT5 deal records stored exactly as returned by MT5Manager.DealRequestByGroup().

    Hybrid raw storage: key fields extracted for indexing/filtering,
    full source payload preserved unchanged in payload_json.

    TimescaleDB hypertable — partitioned by collected_at.
    Retention policy: 2 years (see migration).

    Source: MT5Manager.DealRequestByGroup() — real payload captured 2026-03-23
    Fields: 38 total (Action, ActionGateway, Comment, Commission, ContractSize,
            Deal, Dealer, Digits, DigitsCurrency, Entry, ExpertID, ExternalID,
            Fee, Flags, Gateway, Login, MarketAsk, MarketBid, MarketLast,
            ModificationFlags, ObsoleteValue, Order, PartyID, PositionID, Price,
            PriceGateway, PricePosition, PriceSL, PriceTP, Profit, ProfitRaw,
            RateMargin, RateProfit, Reason, Storage, Symbol, TickSize, TickValue,
            Time, TimeMsc, Value, Volume, VolumeClosed, VolumeClosedExt,
            VolumeExt, VolumeGatewayExt)
    """

    __tablename__ = "raw_mt5_deals"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))  # bare UUID, no FK — raw tables are independent

    # --- Extracted MT5 fields (hybrid raw storage pattern) ---
    deal_id = Column(BigInteger, nullable=False)        # Deal — MT5 deal ticket
    login = Column(BigInteger, nullable=False)           # Login — trading account login
    symbol = Column(String)                              # Symbol — empty string for balance/credit ops
    action = Column(Integer, nullable=False)             # Action — EnDealAction int value
    entry = Column(Integer)                              # Entry — 0=in, 1=out, 2=inout, 3=out_by
    order_id = Column(BigInteger)                        # Order — linked order ticket
    position_id = Column(BigInteger)                     # PositionID — linked position
    volume = Column(BigInteger)                          # Volume — MT5 internal units (÷10000 = lots)
    price = Column(Float)                                # Price — execution price
    profit = Column(Float)                               # Profit
    commission = Column(Float)                           # Commission
    storage = Column(Float)                              # Storage (swap)
    time_msc = Column(BigInteger, nullable=False)        # TimeMsc — unix millisecond epoch
    source_timestamp = Column(DateTime(timezone=True))   # derived from TimeMsc at ingest time
    external_id = Column(String)                         # ExternalID — gateway/bridge deal ID

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)    # hypertable partition key
    ingestion_hash = Column(String)                                    # SHA-256 of payload_json for dedup
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        # Deduplication: one active record per (broker, server, deal ticket)
        Index(
            "uq_raw_mt5_deals_active",
            "broker_id", "server_id", "deal_id",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        # Standard base index — all raw tables
        Index("ix_raw_mt5_deals_broker_collected", "broker_id", "collected_at"),
        # Account-level queries (investigation panel, rule engine)
        Index("ix_raw_mt5_deals_broker_login_collected", "broker_id", "login", "collected_at"),
        # Symbol-level queries (exposure, abuse detection)
        Index("ix_raw_mt5_deals_broker_symbol_collected", "broker_id", "symbol", "collected_at"),
    )


class RawMT5Account(Base):
    """
    Raw MT5 account (user) snapshots stored exactly as returned by MT5Manager.UserGet().

    Plain PostgreSQL table (low-volume config/reference per CLAUDE.md).
    Collected as periodic snapshots — each sync creates a new active record,
    prior record becomes superseded.

    Source: MT5Manager.UserGet() — 46 fields, real payload captured 2026-03-23.
    Key fields: Login, Group, Name, Balance, Credit, Leverage, Rights,
                Country, LastIP, Registration, LastAccess.
    """

    __tablename__ = "raw_mt5_accounts"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- Extracted MT5 fields ---
    login = Column(BigInteger, nullable=False)          # Login — trading account login
    group_name = Column(String)                         # Group — e.g. "managers\administrators"
    name = Column(String)                               # Name — full display name
    balance = Column(Float)                             # Balance
    credit = Column(Float)                              # Credit
    leverage = Column(Integer)                          # Leverage
    rights = Column(Integer)                            # Rights — permissions bitmask
    country = Column(String)                            # Country
    last_ip = Column(String)                            # LastIP — last login IP (fraud detection)
    registration = Column(BigInteger)                   # Registration — account creation unix timestamp
    last_access = Column(BigInteger)                    # LastAccess — last login unix timestamp
    source_timestamp = Column(DateTime(timezone=True))  # derived from Registration at ingest time

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt5_accounts_active",
            "broker_id", "server_id", "login",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt5_accounts_broker_login", "broker_id", "login"),
        Index("ix_raw_mt5_accounts_broker_group", "broker_id", "group_name"),
        Index("ix_raw_mt5_accounts_broker_country", "broker_id", "country"),
    )


class RawMT5Order(Base):
    """
    Raw MT5 order records stored exactly as returned by MT5Manager.HistoryRequestByGroup()
    (same MTOrder structure as active orders from OrderGetByGroup).

    Plain PostgreSQL table per task scope. Contains both historical (filled/cancelled)
    and active (pending) orders depending on collection mode.

    Source: MT5Manager.HistoryRequestByGroup() — 30 fields, real payload captured 2026-03-23.
    Key fields: Order, Login, Symbol, Type, State, PositionID, VolumeInitial,
                VolumeCurrent, PriceOrder, TimeSetupMsc, TimeDoneMsc.
    """

    __tablename__ = "raw_mt5_orders"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- Extracted MT5 fields ---
    order_id = Column(BigInteger, nullable=False)       # Order — MT5 order ticket
    login = Column(BigInteger, nullable=False)           # Login
    symbol = Column(String)                              # Symbol
    type = Column(Integer)                               # Type — EnOrderType (buy/sell/buy_limit etc)
    state = Column(Integer)                              # State — 4=filled, 3=cancelled etc
    position_id = Column(BigInteger)                     # PositionID — linked position
    volume_initial = Column(BigInteger)                  # VolumeInitial — original volume (MT5 units)
    volume_current = Column(BigInteger)                  # VolumeCurrent — remaining unfilled volume
    price_order = Column(Float)                          # PriceOrder — requested price
    price_current = Column(Float)                        # PriceCurrent — market price at collection
    time_setup_msc = Column(BigInteger)                  # TimeSetupMsc — order placement ms epoch
    time_done_msc = Column(BigInteger)                   # TimeDoneMsc — fill/cancel ms epoch
    source_timestamp = Column(DateTime(timezone=True))   # derived from TimeSetupMsc
    external_id = Column(String)                         # ExternalID — gateway order ID

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt5_orders_active",
            "broker_id", "server_id", "order_id",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt5_orders_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt5_orders_broker_login_collected", "broker_id", "login", "collected_at"),
        Index("ix_raw_mt5_orders_broker_symbol_collected", "broker_id", "symbol", "collected_at"),
    )


class RawMT5Position(Base):
    """
    Raw MT5 open position snapshots stored exactly as returned by MT5Manager.PositionGetByGroup().

    Plain PostgreSQL table. Each collection run snapshots currently open positions —
    closed positions become superseded on the next sync.

    Source: MT5Manager.PositionGetByGroup() — 30 fields, real payload captured 2026-03-23.
    Key fields: Position, Login, Symbol, Action, Volume, PriceOpen,
                PriceCurrent, Profit, Storage, TimeCreateMsc, TimeUpdateMsc.
    """

    __tablename__ = "raw_mt5_positions"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- Extracted MT5 fields ---
    position_id = Column(BigInteger, nullable=False)     # Position — MT5 position ticket
    login = Column(BigInteger, nullable=False)            # Login
    symbol = Column(String)                               # Symbol
    action = Column(Integer)                              # Action — 0=buy, 1=sell
    volume = Column(BigInteger)                           # Volume (MT5 units, ÷10000 = lots)
    price_open = Column(Float)                            # PriceOpen — position open price
    price_current = Column(Float)                         # PriceCurrent — current market price
    profit = Column(Float)                                # Profit — floating P&L
    storage = Column(Float)                               # Storage — accrued swap
    time_create_msc = Column(BigInteger)                  # TimeCreateMsc — position open ms epoch
    time_update_msc = Column(BigInteger)                  # TimeUpdateMsc — last update ms epoch
    source_timestamp = Column(DateTime(timezone=True))    # derived from TimeCreateMsc
    external_id = Column(String)                          # ExternalID — gateway position ID

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt5_positions_active",
            "broker_id", "server_id", "position_id",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt5_positions_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt5_positions_broker_login_collected", "broker_id", "login", "collected_at"),
        Index("ix_raw_mt5_positions_broker_symbol_collected", "broker_id", "symbol", "collected_at"),
    )


class RawMT5Symbol(Base):
    """
    Raw MT5 symbol configuration snapshots stored exactly as returned by MT5Manager.SymbolGetArray().

    Plain PostgreSQL table (low-volume config/reference per CLAUDE.md).
    Re-synced periodically to capture spread, swap, and contract changes.

    Source: MT5Manager.SymbolGetArray() — 89 fields, real payload captured 2026-03-23.
    Key fields: Symbol, Description, Path, CurrencyBase, CurrencyProfit,
                CurrencyMargin, Digits, ContractSize, Spread, TradeMode,
                CalcMode, SwapLong, SwapShort.
    """

    __tablename__ = "raw_mt5_symbols"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- Extracted MT5 fields ---
    symbol = Column(String, nullable=False)              # Symbol — e.g. "EURUSD"
    description = Column(String)                         # Description — e.g. "Euro vs US Dollar"
    path = Column(String)                                # Path — e.g. "FX\Forex\EURUSD"
    currency_base = Column(String)                       # CurrencyBase — e.g. "EUR"
    currency_profit = Column(String)                     # CurrencyProfit — e.g. "USD"
    currency_margin = Column(String)                     # CurrencyMargin
    digits = Column(Integer)                             # Digits — price decimal places
    contract_size = Column(Float)                        # ContractSize — e.g. 100000.0 for forex
    spread = Column(Integer)                             # Spread — in points (0 = floating)
    trade_mode = Column(Integer)                         # TradeMode — 0=disabled … 4=full
    calc_mode = Column(Integer)                          # CalcMode — margin calculation mode
    swap_long = Column(Float)                            # SwapLong — overnight swap buy rate
    swap_short = Column(Float)                           # SwapShort — overnight swap sell rate

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt5_symbols_active",
            "broker_id", "server_id", "symbol",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt5_symbols_broker_symbol", "broker_id", "symbol"),
    )


class RawMT5Group(Base):
    """
    Raw MT5 group configuration snapshots stored exactly as returned by MT5Manager.GroupRequestArray().

    Plain PostgreSQL table (low-volume config/reference per CLAUDE.md).
    Group configs change infrequently — re-synced on schedule to detect config changes.

    Source: MT5Manager.GroupRequestArray() — 42 fields, real payload captured 2026-03-23.
    Key fields: Group, Currency, CurrencyDigits, MarginCall, MarginStopOut,
                TradeFlags, PermissionsFlags.
    """

    __tablename__ = "raw_mt5_groups"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- Extracted MT5 fields ---
    group_name = Column(String, nullable=False)          # Group — e.g. "managers\administrators"
    currency = Column(String)                             # Currency — account currency e.g. "USD"
    currency_digits = Column(Integer)                     # CurrencyDigits
    margin_call = Column(Float)                           # MarginCall — margin call level %
    margin_stop_out = Column(Float)                       # MarginStopOut — stop out level %
    trade_flags = Column(Integer)                         # TradeFlags — trading permissions bitmask
    permissions_flags = Column(Integer)                   # PermissionsFlags

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt5_groups_active",
            "broker_id", "server_id", "group_name",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt5_groups_broker_id", "broker_id"),
    )


class RawMT5Tick(Base):
    """
    Raw MT5 tick records stored exactly as returned by MT5Manager.TickLast().

    TimescaleDB hypertable — partitioned by collected_at.
    Retention policy: 90 days (CLAUDE.md: raw tick data).

    Note: MTTick payload does NOT include the symbol name — the symbol is the
    argument passed to TickLast(symbol). The collector must add `symbol` to
    each record before storing.

    Source: MT5Manager.TickLast() — 8 fields, real payload captured 2026-03-23.
    Payload fields (lowercase): ask, bid, datetime, datetime_msc, flags, last, volume, volume_ext.
    """

    __tablename__ = "raw_mt5_ticks"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- Extracted fields ---
    symbol = Column(String, nullable=False)              # added by collector (not in MTTick payload)
    ask = Column(Float)                                  # ask — best ask price
    bid = Column(Float)                                  # bid — best bid price
    last = Column(Float)                                 # last — last trade price (0 for OTC FX)
    volume = Column(BigInteger)                          # volume — tick volume
    datetime_msc = Column(BigInteger, nullable=False)    # datetime_msc — unix millisecond epoch
    source_timestamp = Column(DateTime(timezone=True))   # derived from datetime_msc

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)  # hypertable partition key
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    __table_args__ = (
        # Primary tick query: all ticks for a symbol in a time range
        Index("ix_raw_mt5_ticks_broker_symbol_collected", "broker_id", "symbol", "collected_at"),
        # Standard base index
        Index("ix_raw_mt5_ticks_broker_collected", "broker_id", "collected_at"),
    )


class RawMT5Exposure(Base):
    """
    Raw MT5 currency exposure snapshots stored exactly as returned by MT5Manager.ExposureGetAll().

    Each record is one currency's net exposure across all client accounts.
    Plain PostgreSQL (low-volume aggregate snapshot per CLAUDE.md).
    Re-synced on schedule — prior active record per currency becomes superseded.

    Note: Symbol here is a CURRENCY name (e.g. "EUR", "USD"), not a trading symbol.

    Source: MT5Manager.ExposureGetAll() — 6 fields, real payload captured 2026-03-23.
    All 6 fields are extracted (small record).
    """

    __tablename__ = "raw_mt5_exposure"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- All MT5 fields extracted (6 total — full hybrid) ---
    symbol = Column(String, nullable=False)    # Symbol — currency name e.g. "EUR"
    digits = Column(Integer)                   # Digits — decimal precision
    price_rate = Column(Float)                 # PriceRate — FX rate to broker base currency
    volume_clients = Column(Float)             # VolumeClients — net client exposure (negative = short)
    volume_coverage = Column(Float)            # VolumeCoverage — hedged/covered portion
    volume_net = Column(Float)                 # VolumeNet — total net exposure after coverage

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        # One active exposure record per currency per (broker, server)
        Index(
            "uq_raw_mt5_exposure_active",
            "broker_id", "server_id", "symbol",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt5_exposure_broker_collected", "broker_id", "collected_at"),
    )


class RawMT5Summary(Base):
    """
    Raw MT5 symbol-level position summaries stored exactly as returned by MT5Manager.SummaryGetAll().

    Each record is one symbol's aggregated open interest across all client accounts.
    Plain PostgreSQL (low-volume aggregate snapshot per CLAUDE.md).
    Re-synced on schedule — prior active record per symbol becomes superseded.

    Source: MT5Manager.SummaryGetAll() — 22 fields, real payload captured 2026-03-23.
    Key fields: Symbol, PositionClients, ProfitClients, ProfitUncovered,
                VolumeSellClients, VolumeBuyClients, VolumeNet.
    """

    __tablename__ = "raw_mt5_summary"

    # --- Platform / tenant ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # --- Extracted MT5 fields ---
    symbol = Column(String, nullable=False)                    # Symbol — trading symbol e.g. "EURUSD"
    digits = Column(Integer)                                   # Digits
    position_clients = Column(Integer)                         # PositionClients — open position count
    profit_clients = Column(Float)                             # ProfitClients — floating P&L (clients)
    profit_full_clients = Column(Float)                        # ProfitFullClients — incl. commission/storage
    profit_uncovered = Column(Float)                           # ProfitUncovered — unhedged P&L exposure
    profit_uncovered_full = Column(Float)                      # ProfitUncoveredFull
    volume_buy_clients = Column(BigInteger)                    # VolumeBuyClients (MT5 units)
    volume_sell_clients = Column(BigInteger)                   # VolumeSellClients (MT5 units)
    volume_buy_clients_ext = Column(BigInteger)                # VolumeBuyClientsExt
    volume_sell_clients_ext = Column(BigInteger)               # VolumeSellClientsExt
    volume_net = Column(Float)                                 # VolumeNet — net buy minus sell

    # --- Full raw payload — never modified after insert ---
    payload_json = Column(JSONB, nullable=False)

    # --- Raw table housekeeping ---
    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")  # active | archived | superseded
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        # One active summary record per symbol per (broker, server)
        Index(
            "uq_raw_mt5_summary_active",
            "broker_id", "server_id", "symbol",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt5_summary_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt5_summary_broker_symbol", "broker_id", "symbol"),
    )


class RawCollectorRun(Base):
    """
    Operational log of every collector sync run — success or failure.

    Written by the collector at the end of every bootstrap_sync() and incremental_sync() call.
    Used for: monitoring collector health, debugging missed data, cursor tracking,
    Prometheus metrics source, Grafana collector status dashboard.

    TimescaleDB hypertable — partitioned by collected_at.
    Retention policy: 180 days (CLAUDE.md: connectivity and collector logs).

    No payload_json / status / archived_at — internal platform log, not source data.
    """

    __tablename__ = "raw_collector_runs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    source_system = Column(String, nullable=False)   # mt4|mt5|ctrader|fxbo|bridge|lp|news|calendar
    connection_id = Column(UUID(as_uuid=True))
    server_id = Column(UUID(as_uuid=True))
    entity = Column(String)                          # deals|orders|positions|accounts|ticks|etc.
    sync_mode = Column(String, nullable=False)        # bootstrap|incremental
    status = Column(String, nullable=False)           # success|error|partial
    records_fetched = Column(Integer)
    records_saved = Column(Integer)
    duration_ms = Column(Integer)
    cursor_from = Column(String)                     # cursor at start of run
    cursor_to = Column(String)                       # cursor at end of run (new position on success)
    error_message = Column(String)                   # null on success
    collected_at = Column(DateTime(timezone=True), nullable=False)   # hypertable partition key
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    __table_args__ = (
        # Per CLAUDE.md indexing standard for collector tables
        Index("ix_raw_collector_runs_broker_system_collected", "broker_id", "source_system", "collected_at"),
    )


class RawCollectorError(Base):
    """
    Detailed error log written on every collector failure event.

    Written by the collector inside handle_error() for connection failures,
    fetch failures, save failures, and circuit breaker events.
    Also written after exhausting retries on a source system.

    TimescaleDB hypertable — partitioned by collected_at.
    Retention policy: 180 days (CLAUDE.md: connectivity and collector logs).

    No payload_json / status / archived_at — internal platform log, not source data.
    """

    __tablename__ = "raw_collector_errors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    source_system = Column(String, nullable=False)   # mt4|mt5|ctrader|fxbo|bridge|lp|news|calendar
    connection_id = Column(UUID(as_uuid=True))
    server_id = Column(UUID(as_uuid=True))
    entity = Column(String)                          # which entity was being fetched when error occurred
    sync_mode = Column(String)                        # bootstrap|incremental
    error_type = Column(String)                       # connection|fetch|save|circuit_breaker
    error_code = Column(String)                       # MT5 retcode, Python exception class, HTTP status, etc.
    error_message = Column(String, nullable=False)    # full error text
    context_json = Column(JSONB)                      # cursor position, retry count, partial payload info
    collected_at = Column(DateTime(timezone=True), nullable=False)   # hypertable partition key
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    __table_args__ = (
        # Per CLAUDE.md indexing standard for collector tables
        Index("ix_raw_collector_errors_broker_system_collected", "broker_id", "source_system", "collected_at"),
    )


# ---------------------------------------------------------------------------
# MT4 raw tables
# ---------------------------------------------------------------------------
# Key MT4 structural differences vs MT5:
#   - Single TradeRecord struct used for BOTH orders (close_time=0) and deals (close_time>0)
#   - Timestamps are unix seconds — no millisecond precision
#   - Field names are lowercase (ctypes convention), not PascalCase
#   - IP addresses stored as packed uint32 integers
#   - Volume stored as lots×100 (÷100 = standard lots), not MT5's ÷10000
#   - Ticks have only 3 fields: ctm, bid, ask — symbol injected by collector
# ---------------------------------------------------------------------------


class RawMT4Account(Base):
    """
    Raw MT4 user records stored exactly as returned by manager->UsersRequest().

    Plain PostgreSQL table (low-volume config/reference per CLAUDE.md).
    Periodic snapshots — each sync supersedes the prior active record per login.

    Source: mtmanapi.dll UsersRequest() — 22 fields from MT4ManagerAPI.h, captured 2026-03-26.
    Note: last_ip is a packed uint32 integer (not a string).
    """

    __tablename__ = "raw_mt4_accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # Extracted MT4 fields
    login = Column(Integer, nullable=False)              # login — account login
    group_name = Column(String)                          # group — e.g. "real\managers"
    enable = Column(Integer)                             # enable — 1=active, 0=disabled
    name = Column(String)                                # name — full name
    country = Column(String)                             # country
    city = Column(String)                                # city
    leverage = Column(Integer)                           # leverage
    balance = Column(Float)                              # balance
    credit = Column(Float)                               # credit
    margin_level = Column(Float)                         # margin_level — snapshot at collection time
    regdate = Column(BigInteger)                         # regdate — registration unix timestamp
    lastdate = Column(BigInteger)                        # lastdate — last login unix timestamp
    last_ip = Column(BigInteger)                         # last_ip — packed uint32 IP address
    source_timestamp = Column(DateTime(timezone=True))   # derived from regdate

    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_accounts_active",
            "broker_id", "server_id", "login",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_accounts_broker_login", "broker_id", "login"),
        Index("ix_raw_mt4_accounts_broker_group", "broker_id", "group_name"),
        Index("ix_raw_mt4_accounts_broker_country", "broker_id", "country"),
    )


class RawMT4Order(Base):
    """
    Raw MT4 open orders/positions stored exactly as returned by manager->TradesRequest().

    These are TradeRecord entries where close_time == 0.
    Includes both open market positions (cmd 0-1) and pending orders (cmd 2-5).
    Plain PostgreSQL table per task scope.

    Source: mtmanapi.dll TradesRequest() — TradeRecord struct (28 fields),
    captured 2026-03-26 from MT4ManagerAPI.h header + live sample.

    MT4 note: cmd 0=BUY, 1=SELL, 2=BUY_LIMIT, 3=SELL_LIMIT, 4=BUY_STOP, 5=SELL_STOP,
              6=BALANCE, 7=CREDIT. Volume is lots×100 (÷100 = standard lots).
    """

    __tablename__ = "raw_mt4_orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # Extracted MT4 TradeRecord fields
    order_id = Column(Integer, nullable=False)           # order — MT4 ticket number
    login = Column(Integer, nullable=False)               # login
    symbol = Column(String)                               # symbol — empty for balance ops
    cmd = Column(Integer)                                 # cmd — trade command (0=BUY, 1=SELL, etc.)
    volume = Column(Integer)                              # volume — lots×100 (÷100 = standard lots)
    open_time = Column(BigInteger)                        # open_time — position open unix timestamp
    state = Column(Integer)                               # state — 0=open, 1=remand, 2=restored
    open_price = Column(Float)                            # open_price — entry price
    sl = Column(Float)                                    # sl — stop loss (0=none)
    tp = Column(Float)                                    # tp — take profit (0=none)
    close_price = Column(Float)                           # close_price — current market price (close_time=0)
    profit = Column(Float)                                # profit — floating P&L
    commission = Column(Float)                            # commission
    storage = Column(Float)                               # storage — accrued swap
    magic = Column(Integer)                               # magic — EA magic number (0=manual)
    expiration = Column(BigInteger)                       # expiration — pending order expiry (0=GTC)
    timestamp = Column(BigInteger)                        # timestamp — last modification unix time
    source_timestamp = Column(DateTime(timezone=True))    # derived from open_time

    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_orders_active",
            "broker_id", "server_id", "order_id",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_orders_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt4_orders_broker_login_collected", "broker_id", "login", "collected_at"),
        Index("ix_raw_mt4_orders_broker_symbol_collected", "broker_id", "symbol", "collected_at"),
    )


class RawMT4Deal(Base):
    """
    Raw MT4 closed trade records stored exactly as returned by manager->TradesUserHistory().

    These are TradeRecord entries where close_time > 0 — fully closed positions
    and balance/credit operations (cmd=6/7).

    MT4 has no separate "deal" entity like MT5. A closed TradeRecord IS the deal.
    close_price is the actual exit price; profit is realized P&L.
    Plain PostgreSQL table per task scope.

    Source: mtmanapi.dll TradesUserHistory() — same TradeRecord struct as orders (28 fields),
    captured 2026-03-26 from MT4ManagerAPI.h header + live sample.
    """

    __tablename__ = "raw_mt4_deals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # Extracted MT4 TradeRecord fields
    order_id = Column(Integer, nullable=False)            # order — MT4 ticket number
    login = Column(Integer, nullable=False)                # login
    symbol = Column(String)                                # symbol — empty for balance/credit ops
    cmd = Column(Integer)                                  # cmd — 0=BUY, 1=SELL, 6=BALANCE, 7=CREDIT
    volume = Column(Integer)                               # volume — lots×100 (÷100 = standard lots)
    open_time = Column(BigInteger)                         # open_time — position open unix timestamp
    close_time = Column(BigInteger, nullable=False)        # close_time — close unix timestamp (always > 0)
    state = Column(Integer)                                # state — 3=closed_normal, 4=closed_part, etc.
    open_price = Column(Float)                             # open_price — entry price (0 for balance ops)
    close_price = Column(Float)                            # close_price — exit price
    profit = Column(Float)                                 # profit — realized P&L
    commission = Column(Float)                             # commission
    storage = Column(Float)                                # storage — total swap over holding period
    magic = Column(Integer)                                # magic — EA magic number
    reason = Column(Integer)                               # reason — close reason (0=client, 3=stopout etc.)
    timestamp = Column(BigInteger)                         # timestamp — last modification unix time
    source_timestamp = Column(DateTime(timezone=True))     # derived from close_time

    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_deals_active",
            "broker_id", "server_id", "order_id",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_deals_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt4_deals_broker_login_collected", "broker_id", "login", "collected_at"),
        Index("ix_raw_mt4_deals_broker_symbol_collected", "broker_id", "symbol", "collected_at"),
    )


class RawMT4Symbol(Base):
    """
    Raw MT4 symbol info snapshots stored exactly as returned by manager->SymbolInfoGet().

    Plain PostgreSQL table (low-volume config/reference per CLAUDE.md).
    10-field market watch snapshot: current bid/ask, spread, daily high/low.
    Re-synced periodically to capture config and spread changes.

    Source: mtmanapi.dll SymbolInfoGet() — 10 fields from MT4ManagerAPI.h, captured 2026-03-26.
    Note: All 10 fields extracted (small record, full hybrid).
    """

    __tablename__ = "raw_mt4_symbols"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # All 10 MT4 fields extracted
    symbol = Column(String, nullable=False)              # symbol — e.g. "EURUSD"
    digits = Column(Integer)                              # digits — price decimal places
    spread = Column(Integer)                              # spread — in points
    spread_float = Column(Integer)                        # spread_float — 1=floating spread
    bid = Column(Float)                                   # bid — current best bid
    ask = Column(Float)                                   # ask — current best ask
    session_price = Column(Float)                         # session_price — session open price
    high = Column(Float)                                  # high — daily high
    low = Column(Float)                                   # low — daily low
    time = Column(BigInteger)                             # time — last quote unix timestamp

    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_symbols_active",
            "broker_id", "server_id", "symbol",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_symbols_broker_symbol", "broker_id", "symbol"),
    )


class RawMT4Group(Base):
    """
    Raw MT4 group configuration snapshots stored exactly as returned by manager->GroupsRequest().

    Plain PostgreSQL table (low-volume config/reference per CLAUDE.md).
    ConGroup struct key fields extracted; per-symbol securities array (ConGroupMargin[128])
    stored only in payload_json due to size and complexity.

    Source: mtmanapi.dll GroupsRequest() — ConGroup struct from MT4ManagerAPI.h, captured 2026-03-26.
    """

    __tablename__ = "raw_mt4_groups"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # Extracted ConGroup key fields
    group_name = Column(String, nullable=False)           # group — e.g. "real\managers"
    currency = Column(String)                              # currency — account currency e.g. "USD"
    default_leverage = Column(Integer)                     # default_leverage
    default_deposit = Column(Float)                        # default_deposit — new account starting balance
    stopping_level = Column(Integer)                       # stopping_level — stop-out level %
    margin_call = Column(Integer)                          # margin_call — margin call level %
    trading = Column(Integer)                              # trading — 1=enabled, 0=disabled
    commission_base = Column(Float)                        # commission_base
    commission_type = Column(Integer)                      # commission_type — 0=disabled, 1=per lot, 2=%
    commission_lots = Column(Float)                        # commission_lots
    balance_min = Column(Float)                            # balance_min — minimum allowed balance
    interest_rate = Column(Float)                          # interest_rate — % on balance
    tax = Column(Float)                                    # tax — % on profits
    hedge_prohibited = Column(Integer)                     # hedge_prohibited — 1=no hedging
    close_fifo = Column(Integer)                           # close_fifo — 1=FIFO required

    # securities (ConGroupMargin[128]) stored only in payload_json — complex nested array
    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_groups_active",
            "broker_id", "server_id", "group_name",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_groups_broker_id", "broker_id"),
    )


class RawMT4Tick(Base):
    """
    Raw MT4 tick records stored exactly as returned by manager->TicksRequest().

    TimescaleDB hypertable — partitioned by collected_at.
    Retention policy: 90 days (CLAUDE.md: raw tick data).

    MT4 ticks have only 3 fields: ctm (unix seconds), bid, ask.
    No "last" price, no volume — unlike MT5 ticks.
    Symbol is not in the payload; the collector must inject it before storing.

    Source: mtmanapi.dll TicksRequest() — TickAPI struct (3 fields) from MT4ManagerAPI.h,
    captured 2026-03-26. Ticks are append-only — no status/archived_at.
    """

    __tablename__ = "raw_mt4_ticks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # Extracted fields
    symbol = Column(String, nullable=False)              # added by collector (not in TickAPI payload)
    ctm = Column(BigInteger, nullable=False)             # ctm — unix second timestamp
    bid = Column(Float)                                  # bid
    ask = Column(Float)                                  # ask
    source_timestamp = Column(DateTime(timezone=True))   # derived from ctm

    payload_json = Column(JSONB, nullable=False)

    # Ticks are append-only — no status, ingestion_hash, updated_at, archived_at
    collected_at = Column(DateTime(timezone=True), nullable=False)   # hypertable partition key
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    __table_args__ = (
        Index("ix_raw_mt4_ticks_broker_symbol_collected", "broker_id", "symbol", "collected_at"),
        Index("ix_raw_mt4_ticks_broker_collected", "broker_id", "collected_at"),
    )


class RawMT4Online(Base):
    """
    Raw MT4 online session snapshots stored exactly as returned by manager->OnlineRequest().

    Plain PostgreSQL table. Point-in-time snapshot of all connected clients.
    Re-synced on schedule — prior active record per login becomes superseded.

    Source: mtmanapi.dll OnlineRequest() — OnlineRecord struct (7 fields) from MT4ManagerAPI.h,
    captured 2026-03-26. Note: ip is a packed uint32 integer (not a string).
    All 7 fields extracted (small record, full hybrid).
    """

    __tablename__ = "raw_mt4_online"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # All 7 MT4 OnlineRecord fields extracted
    login = Column(Integer, nullable=False)              # login
    group_name = Column(String)                          # group — e.g. "real\managers"
    ip = Column(BigInteger)                              # ip — packed uint32 IP address
    login_time = Column(BigInteger)                      # login_time — session start unix timestamp
    last_access = Column(BigInteger)                     # last_access — last activity unix timestamp
    agent = Column(String)                               # agent — client string e.g. "MetaTrader 4"
    version = Column(Integer)                            # version — client build number e.g. 1360
    source_timestamp = Column(DateTime(timezone=True))   # derived from login_time

    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_online_active",
            "broker_id", "server_id", "login",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_online_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt4_online_broker_login", "broker_id", "login"),
    )


class RawMT4Margin(Base):
    """
    Raw MT4 margin level snapshots stored exactly as returned by manager->MarginLevelGet().

    Plain PostgreSQL table. Real-time account financial state:
    balance, equity, margin usage, free margin, floating P&L.
    Re-synced on schedule — prior active record per login becomes superseded.

    Source: mtmanapi.dll MarginLevelGet() — MarginLevel struct (13 fields) from MT4ManagerAPI.h,
    captured 2026-03-26. All 13 fields extracted (small record, full hybrid).
    """

    __tablename__ = "raw_mt4_margin"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # All 13 MT4 MarginLevel fields extracted
    login = Column(Integer, nullable=False)              # login
    group_name = Column(String)                          # group
    balance = Column(Float)                              # balance
    equity = Column(Float)                               # equity — balance + floating P&L + credit
    margin = Column(Float)                               # margin — margin used
    margin_free = Column(Float)                          # margin_free — free margin available
    margin_level = Column(Float)                         # margin_level — equity/margin × 100 %
    margin_initial = Column(Float)                       # margin_initial
    margin_maintenance = Column(Float)                   # margin_maintenance
    profit_loss = Column(Float)                          # profit_loss — realized + unrealized P&L
    assets = Column(Float)                               # assets
    liabilities = Column(Float)                          # liabilities
    floating = Column(Float)                             # floating — unrealized P&L only

    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_margin_active",
            "broker_id", "server_id", "login",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_margin_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt4_margin_broker_login", "broker_id", "login"),
    )


class RawMT4Summary(Base):
    """
    Raw MT4 symbol position summaries stored exactly as returned by manager->SummaryGet().

    Plain PostgreSQL table. Server-level aggregate open interest per symbol:
    total position count, net volume, buy/sell split, floating P&L, hedged volume.
    Re-synced on schedule — prior active record per symbol becomes superseded.

    Source: mtmanapi.dll SummaryGet() — SymbolSummary struct (9 fields) from MT4ManagerAPI.h,
    captured 2026-03-26. All 9 fields extracted (small record, full hybrid).
    """

    __tablename__ = "raw_mt4_summary"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    broker_id = Column(UUID(as_uuid=True), nullable=False)
    server_id = Column(UUID(as_uuid=True))

    # All 9 MT4 SymbolSummary fields extracted
    symbol = Column(String, nullable=False)              # symbol — e.g. "EURUSD"
    count = Column(Integer)                              # count — number of open positions
    volume = Column(Integer)                             # volume — total volume (lots×100)
    volume_buy = Column(Integer)                         # volume_buy — buy side volume (lots×100)
    volume_sell = Column(Integer)                        # volume_sell — sell side volume (lots×100)
    profit = Column(Float)                               # profit — total floating P&L
    hedged = Column(Integer)                             # hedged — hedged volume (lots×100)
    hedged_buy = Column(Float)                           # hedged_buy
    hedged_sell = Column(Float)                          # hedged_sell

    payload_json = Column(JSONB, nullable=False)

    collected_at = Column(DateTime(timezone=True), nullable=False)
    ingestion_hash = Column(String)
    status = Column(String, nullable=False, server_default="active")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    updated_at = Column(DateTime(timezone=True))
    archived_at = Column(DateTime(timezone=True))

    __table_args__ = (
        Index(
            "uq_raw_mt4_summary_active",
            "broker_id", "server_id", "symbol",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
        Index("ix_raw_mt4_summary_broker_collected", "broker_id", "collected_at"),
        Index("ix_raw_mt4_summary_broker_symbol", "broker_id", "symbol"),
    )
