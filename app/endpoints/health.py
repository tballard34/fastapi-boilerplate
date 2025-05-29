import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.config import settings
from app.models import HealthResponse, MessageResponse

logger: logging.Logger = logging.getLogger(__name__)

router: APIRouter = APIRouter(prefix="", tags=["Health"])


@router.get("/", response_model=MessageResponse)
async def root():
    logger.info("Hit / endpoint")
    logger.info(f"Environment: {settings.environment}")
    response: MessageResponse = MessageResponse(message="Hello from FastAPI!")
    return JSONResponse(content=response.model_dump(), status_code=200)


@router.get("/health", response_model=HealthResponse)
async def health():
    logger.info("Hit /health endpoint")
    response: HealthResponse = HealthResponse(status="ok")
    return JSONResponse(content=response.model_dump(), status_code=200)
