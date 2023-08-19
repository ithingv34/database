from fastapi import FastAPI

from src.api import router
from src.db import Engine
from src.config import app_config


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()


@app.get("/")
async def root_path():
    return {"message": f"You are visiting: {app_config.name} v{app_config.version}"}


@app.on_event("startup")
async def create_db_client():
    """Initialize DB connection."""

    await Engine.connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_db_client():
    """Close DB connection."""

    await Engine.close_mongo_connection()
