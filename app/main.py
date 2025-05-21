import logging

from fastapi import FastAPI

from app.utils import setup_logging

setup_logging()
logger: logging.Logger = logging.getLogger(__name__)

app: FastAPI = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


@app.get("/health")
def health():
    return {"status": "ok"}
