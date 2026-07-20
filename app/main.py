from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.settings import settings
from app.core.logging import setup_logging
import logging
from app.api.v1.users import router as user_router
from app.api.v1.auth import router as auth_router
from app.exceptions.handlers import register_exception_handlers
# ---------------------------------------------------------------------
# Configure logging
# ---------------------------------------------------------------------
setup_logging()
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------
# Application Lifecycle
# ---------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown events.
    """

    logger.info("Starting %s...", settings.app_name)
    logger.info("Environment: %s", settings.app_environment)

    yield

    logger.info("Shutting down %s...", settings.app_name)


# ---------------------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------------------
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Production-ready Enterprise AI Platform",
    debug=settings.debug,
    lifespan=lifespan,
)
register_exception_handlers(app)
app.include_router(user_router) # Include the user router
app.include_router(auth_router) # Include the auth router
# ---------------------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------------------
@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint.
    """

    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_environment,
        "status": "running",
    }


# ---------------------------------------------------------------------
# Health Check
# ---------------------------------------------------------------------
@app.get("/health", tags=["Health"])
async def health():
    """
    Basic health check endpoint.
    """

    return {
        "status": "healthy",
    }