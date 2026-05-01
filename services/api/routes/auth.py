"""Authentication routes — login, token refresh."""

from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRY_SEC
from database import get_db

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")


class LoginRequest(BaseModel):
    email: str
    password: str
    broker_slug: str   # identifies the tenant (subdomain key)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    broker_id: str
    role: str


@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest, db: Session = Depends(get_db)):
    broker = db.execute(
        text("SELECT id FROM brokers WHERE slug = :slug AND status = 'active'"),
        {"slug": req.broker_slug},
    ).fetchone()
    if not broker:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    user = db.execute(
        text(
            "SELECT id, hashed_password FROM broker_users "
            "WHERE broker_id = :bid AND email = :email AND status = 'active'"
        ),
        {"bid": str(broker.id), "email": req.email},
    ).fetchone()
    if not user or not _pwd.verify(req.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    role_row = db.execute(
        text(
            "SELECT r.name FROM user_broker_roles ubr "
            "JOIN roles r ON r.id = ubr.role_id "
            "WHERE ubr.user_id = :uid AND ubr.broker_id = :bid "
            "ORDER BY CASE r.name WHEN 'admin' THEN 0 WHEN 'dealer' THEN 1 ELSE 2 END LIMIT 1"
        ),
        {"uid": str(user.id), "bid": str(broker.id)},
    ).fetchone()
    role = role_row.name if role_row else "readonly"

    exp = datetime.now(timezone.utc) + timedelta(seconds=JWT_EXPIRY_SEC)
    token = jwt.encode(
        {
            "sub": str(user.id),
            "broker_id": str(broker.id),
            "email": req.email,
            "role": role,
            "exp": exp,
        },
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )
    return TokenResponse(
        access_token=token,
        expires_in=JWT_EXPIRY_SEC,
        broker_id=str(broker.id),
        role=role,
    )
