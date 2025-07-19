import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.config import settings
from app.models import HealthResponse, MessageResponse

logger: logging.Logger = logging.getLogger(__name__)

router: APIRouter = APIRouter(prefix="", tags=["Health"])


@router.get("/", response_model=MessageResponse)
async def root():
    """Root endpoint that returns a welcome message."""
    logger.info("Hit / endpoint")
    logger.info("Environment: %s", settings.environment)
    response: MessageResponse = MessageResponse(message="Hello from FastAPI!")
    return JSONResponse(content=response.model_dump(), status_code=200)


@router.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint to verify the application is running."""
    logger.info("Hit /health endpoint")
    response: HealthResponse = HealthResponse(status="ok")
    return JSONResponse(content=response.model_dump(), status_code=200)
