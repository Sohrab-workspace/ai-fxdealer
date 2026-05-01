"""Create a test user in the DB for API testing.

Usage:
    python scripts/create_test_user.py
"""
import os
import sys
import uuid
from pathlib import Path

repo_root = str(Path(__file__).parent.parent)
sys.path.insert(0, str(Path(repo_root) / "packages" / "db"))

from sqlalchemy import create_engine, text
from passlib.context import CryptContext

DB_URL = os.environ.get("FXDEALER_DB_URL", "postgresql://fxdealer:fxdealer@localhost:5432/fxdealer")
engine = create_engine(DB_URL)
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

BROKER_ID = "00000000-0000-0000-0000-000000000001"
EMAIL = "admin@test.com"
PASSWORD = "admin123"
FULL_NAME = "Test Admin"

with engine.begin() as conn:
    # Ensure broker exists
    broker = conn.execute(
        text("SELECT id FROM brokers WHERE id = :bid"),
        {"bid": BROKER_ID},
    ).fetchone()
    if not broker:
        conn.execute(
            text("INSERT INTO brokers (id, name, slug, status) VALUES (:id, :name, :slug, 'active')"),
            {"id": BROKER_ID, "name": "Test Broker", "slug": "test-broker"},
        )
        print(f"Created broker: {BROKER_ID}")

    # Ensure admin role exists
    role = conn.execute(
        text("SELECT id FROM roles WHERE name = 'admin'"),
    ).fetchone()
    if not role:
        role_id = str(uuid.uuid4())
        conn.execute(
            text("INSERT INTO roles (id, name, description) VALUES (:id, 'admin', 'Full access')"),
            {"id": role_id},
        )
        print(f"Created admin role: {role_id}")
    else:
        role_id = str(role.id)

    # Ensure dealer role exists
    dealer_role = conn.execute(text("SELECT id FROM roles WHERE name = 'dealer'")).fetchone()
    if not dealer_role:
        conn.execute(
            text("INSERT INTO roles (id, name, description) VALUES (:id, 'dealer', 'Dealer access')"),
            {"id": str(uuid.uuid4())},
        )

    # Ensure readonly role exists
    readonly_role = conn.execute(text("SELECT id FROM roles WHERE name = 'readonly'")).fetchone()
    if not readonly_role:
        conn.execute(
            text("INSERT INTO roles (id, name, description) VALUES (:id, 'readonly', 'Read-only access')"),
            {"id": str(uuid.uuid4())},
        )

    # Create or update user
    existing = conn.execute(
        text("SELECT id FROM broker_users WHERE broker_id = :bid AND email = :email"),
        {"bid": BROKER_ID, "email": EMAIL},
    ).fetchone()

    hashed = pwd.hash(PASSWORD)
    if existing:
        user_id = str(existing.id)
        conn.execute(
            text("UPDATE broker_users SET hashed_password = :hp, full_name = :fn WHERE id = :id"),
            {"hp": hashed, "fn": FULL_NAME, "id": user_id},
        )
        print(f"Updated user: {EMAIL}")
    else:
        user_id = str(uuid.uuid4())
        conn.execute(
            text(
                "INSERT INTO broker_users (id, broker_id, email, hashed_password, full_name, status) "
                "VALUES (:id, :bid, :email, :hp, :fn, 'active')"
            ),
            {"id": user_id, "bid": BROKER_ID, "email": EMAIL, "hp": hashed, "fn": FULL_NAME},
        )
        print(f"Created user: {EMAIL}")

    # Assign admin role
    role_id = conn.execute(text("SELECT id FROM roles WHERE name = 'admin'")).scalar()
    existing_role = conn.execute(
        text(
            "SELECT id FROM user_broker_roles WHERE user_id = :uid AND broker_id = :bid AND role_id = :rid"
        ),
        {"uid": user_id, "bid": BROKER_ID, "rid": str(role_id)},
    ).fetchone()
    if not existing_role:
        conn.execute(
            text(
                "INSERT INTO user_broker_roles (id, user_id, broker_id, role_id) "
                "VALUES (:id, :uid, :bid, :rid)"
            ),
            {"id": str(uuid.uuid4()), "uid": user_id, "bid": BROKER_ID, "rid": str(role_id)},
        )
        print(f"Assigned admin role to {EMAIL}")

print(f"\nTest user ready:")
print(f"  Email:       {EMAIL}")
print(f"  Password:    {PASSWORD}")
print(f"  Broker slug: test-broker")
print(f"  Role:        admin")
