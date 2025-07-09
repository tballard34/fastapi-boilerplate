from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.config import settings
from app.models import ExampleRequest, ExampleResponse
from app.utils import get_logger

logger = get_logger(__name__)

router: APIRouter = APIRouter(prefix="", tags=["Example"])


@router.post("/v1/example/example_endpoint", response_model=ExampleResponse)
async def example(request: ExampleRequest):
    logger.info("Hit /v1/example/example_endpoint endpoint")
    logger.info("Environment: %s", settings.environment)
    response: ExampleResponse = ExampleResponse(message=f"Hello {request.name} from Example Endpoint")
    return JSONResponse(content=response.model_dump(), status_code=200)
