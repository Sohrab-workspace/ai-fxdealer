"""JWT authentication middleware — validates token and resolves broker context."""

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import JWT_SECRET, JWT_ALGORITHM
from database import get_db

_bearer = HTTPBearer()


class BrokerContext(BaseModel):
    user_id: str
    broker_id: str
    email: str
    role: str   # admin | dealer | readonly


def get_broker_context(
    creds: HTTPAuthorizationCredentials = Depends(_bearer),
    db: Session = Depends(get_db),
) -> BrokerContext:
    token = creds.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    exp = payload.get("exp")
    if exp and datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    return BrokerContext(
        user_id=payload["sub"],
        broker_id=payload["broker_id"],
        email=payload.get("email", ""),
        role=payload.get("role", "readonly"),
    )
