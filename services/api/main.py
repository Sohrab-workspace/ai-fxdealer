"""AI FXDealer API — FastAPI application entry point."""

import sys
import os

# Add service root to path so local imports work
sys.path.insert(0, os.path.dirname(__file__))

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.accounts import router as accounts_router
from routes.deals import router as deals_router
from routes.positions import router as positions_router
from routes.ticks import router as ticks_router
from routes.rules import router as rules_router
from routes.collectors import router as collectors_router
from routes.overview import router as overview_router
from routes.raw_tables import router as raw_tables_router

structlog.configure(
    processors=[structlog.dev.ConsoleRenderer(colors=False)],
)
log = structlog.get_logger()

app = FastAPI(
    title="AI FXDealer API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(deals_router)
app.include_router(positions_router)
app.include_router(ticks_router)
app.include_router(rules_router)
app.include_router(collectors_router)
app.include_router(overview_router)
app.include_router(raw_tables_router)


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
