from typing import Literal

from pydantic import BaseModel

# Environment types
EnvironmentType = Literal["local", "dev", "staging", "prod"]

# Logging level types
LogLevelType = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class MessageResponse(BaseModel):
    message: str


class HealthResponse(BaseModel):
    status: str


class ExampleRequest(BaseModel):
    name: str


class ExampleResponse(BaseModel):
    message: str
