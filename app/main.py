# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, Query
from loguru import logger
from starlette.responses import RedirectResponse

from com_lib.logging_config import config_logging
from endpoints.tools import views as tools
from endpoints.health import views as health
from settings import (
    APP_VERSION,
    RELEASE_ENV,
)

# config logging start
config_logging()
logger.info("API Logging initiated")
# fastapi start
app = FastAPI(
    title="Test API",
    description="Checklist APIs",
    version=APP_VERSION,
    openapi_url="/openapi.json",
)
logger.info("API App initiated")

four_zero_four = {404: {"description": "Not found"}}
# Endpoint routers
# Converter router
app.include_router(
    tools.router, prefix="/api/v1/tools", tags=["tools"], responses=four_zero_four,
)

# Health router
app.include_router(
    health.router,
    prefix="/api/health",
    tags=["system-health"],
    responses=four_zero_four,
)

"""
for future use
app.include_router(socket.router,prefix="/api/v1/websocket",
tags=["websocket"],responses=four_zero_four,)
"""

# startup events
@app.on_event("startup")
async def startup_event():

    # initiate log with statement
    if RELEASE_ENV.lower() == "dev":
        logger.debug(f"Initiating logging for API")
        logger.info(f"API initiated Release_ENV: {RELEASE_ENV}")

    else:
        logger.info(f"API initiated Release_ENV: {RELEASE_ENV}")


@app.on_event("shutdown")
async def shutdown_event():

    logger.info("API shutting down")


@app.get("/")
async def root():
    """
    Root endpoint of API

    Returns:
        Redrects to openapi document
    """
    response = RedirectResponse(url="/docs")
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
