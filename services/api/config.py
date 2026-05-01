import os

DB_URL          = os.environ.get("FXDEALER_DB_URL", "postgresql://fxdealer:fxdealer@localhost:5432/fxdealer")
JWT_SECRET      = os.environ.get("FXDEALER_JWT_SECRET", "dev-secret-change-in-prod")
JWT_ALGORITHM   = "HS256"
JWT_EXPIRY_SEC  = int(os.environ.get("FXDEALER_JWT_EXPIRY_SECONDS", "86400"))
