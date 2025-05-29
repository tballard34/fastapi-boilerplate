import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.config import settings
from app.models import MessageResponse

logger: logging.Logger = logging.getLogger(__name__)

router: APIRouter = APIRouter(prefix="/v1/example", tags=["Example"])


@router.get("/example_endpoint", response_model=MessageResponse)
async def example():
    logger.info("Hit /v1/example/example_endpoint endpoint")
    logger.info(f"Environment: {settings.environment}")
    response: MessageResponse = MessageResponse(message="Hello from Example Endpoint")
    return JSONResponse(content=response.model_dump(), status_code=200)
