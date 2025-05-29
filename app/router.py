from fastapi import APIRouter

from app import endpoint

router: APIRouter = APIRouter()

router.include_router(endpoint.router, prefix="", tags=["Health"])
