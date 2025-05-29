from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models import HealthResponse, MessageResponse

router: APIRouter = APIRouter()


@router.get("/", response_model=MessageResponse)
async def read_root():
    response: MessageResponse = MessageResponse(message="Hello from FastAPI!")
    return JSONResponse(content=response.model_dump(), status_code=200)


@router.get("/health", response_model=HealthResponse)
async def health():
    response: HealthResponse = HealthResponse(status="ok")
    return JSONResponse(content=response.model_dump(), status_code=200)
