import logging

from dotenv import load_dotenv
from fastapi import FastAPI

from app.router import router
from app.utils import setup_logging

load_dotenv()

setup_logging()
logger: logging.Logger = logging.getLogger(__name__)

app: FastAPI = FastAPI(
    title="Example Title",
    description="Example Description",
    version="0.0.0",
)

app.include_router(router)
