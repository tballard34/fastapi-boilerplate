import logging

from fastapi import FastAPI

from app.router import router
from app.utils import setup_logging

setup_logging()
logger: logging.Logger = logging.getLogger(__name__)

logger.info("example-name starting up - logging configured")

app: FastAPI = FastAPI(
    title="Example Title",
    description="Example Description",
    version="0.0.0",
)

app.include_router(router)
