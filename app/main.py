import logging

from dotenv import load_dotenv
from fastapi import FastAPI

from app.utils import setup_logging

load_dotenv()

setup_logging()
logger: logging.Logger = logging.getLogger(__name__)

app: FastAPI = FastAPI(
    title="Title",
    description="Description",
    version="0.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


@app.get("/health")
def health():
    return {"status": "ok"}
