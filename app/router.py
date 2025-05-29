from fastapi import APIRouter

from app.endpoints import example, health

router: APIRouter = APIRouter()

router.include_router(health.router)
router.include_router(example.router)
